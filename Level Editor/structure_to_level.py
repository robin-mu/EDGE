import json
import os
import sys
import shutil
import subprocess
import xml.etree.ElementTree as et

from PIL import Image
from nbt import nbt

elements: dict[str, list[et.Element]] = {}
moving_platforms: dict[str, et.Element] = {}
moving_platforms_by_position: dict[str, str] = {}
waypoints: dict[str, dict[int, et.Element]] = {}


class DynamicPart:
    def __init__(self, name, timing: tuple = (), visible: bool = False, radius: bool = False, position: bool = True,
                 higher_pos: bool = False, items: dict = None):
        self.name = name
        self.timing = timing
        self.visible = visible
        self.radius = radius
        self.position = position
        self.higher_pos = higher_pos
        self.items = items if items else {}

    def to_element(self, container: list, pos: tuple[int, int, int]=(0, 0, 0), orientation: str = None):
        params = {}
        if self.position:
            params['Position'] = v3d(pos, self.higher_pos)

        # count items
        items = {}
        book = {}
        for e in container:
            id = e['id'].value
            items[id] = items.get(id, 0) + e['Count'].value

            if id in ('minecraft:writable_book', 'minecraft:written_book'):
                book.update(read_book(e['tag']['pages']))

        if self.timing:
            first_timing = str(items.get('minecraft:iron_ingot', 0) * 30 + items.get('minecraft:iron_nugget', 0))
            if first_timing != '0':
                params[self.timing[0]] = first_timing
            if len(self.timing) > 1:
                second_timing = str(items.get('minecraft:gold_ingot', 0) * 30 + items.get('minecraft:gold_nugget', 0))
                if second_timing != '0':
                    params[self.timing[1]] = second_timing

        if self.visible:
            if 'minecraft:glass' in items:
                params['Visible'] = 'False'
            elif 'minecraft:white_stained_glass' in items:
                params['Visible'] = 'Null'

        if self.radius:
            r = f'{items.get("minecraft:prismarine_shard", 0)},{items.get("minecraft:stick", 0)}'
            if r != '0,0':
                params['Radius'] = r

        for i in self.items:
            if i in items:
                for p in self.items[i]:
                    params[p] = self.items[i][p].replace('%', str(items[i]))

        params.update(book)

        if self.name == 'MovingPlatform':
            # for attaching buttons
            if 'ID' in params:
                moving_platforms_by_position[v3d(pos)] = params['ID']

            first_item = container[0]
            waypoint_item = first_item['id'].value
            count = first_item['Count'].value
            if count > 1:
                params['LoopStartIndex'] = count

            waypoint = {'Position': v3d(pos, True)}
            if 'TravelTime' in params:
                waypoint['TravelTime'] = params.pop('TravelTime')

            if 'PauseTime' in params:
                waypoint['PauseTime'] = params.pop('PauseTime')

            moving_platforms[waypoint_item] = et.Element(self.name, params)
            if waypoint_item in waypoints:
                waypoints[waypoint_item][0] = et.Element('Waypoint', waypoint)
            else:
                waypoints[waypoint_item] = {0: et.Element('Waypoint', waypoint)}
        elif self.name == 'Waypoint':
            first_item = container[0]
            waypoint_item = first_item['id'].value
            count = first_item['Count'].value
            if waypoint_item in waypoints:
                waypoints[waypoint_item][count] = et.Element(self.name, params)
            else:
                waypoints[waypoint_item] = {count: et.Element(self.name, params)}
        elif self.name == 'Bumper':
            direction = {}
            if 'StartDelay' in params:
                direction['StartDelay'] = params.pop('StartDelay')
            if 'PulseRate' in params:
                direction['PulseRate'] = params.pop('PulseRate')

            bumper = et.Element(self.name, params)
            bumper.append(et.Element(orientation, direction))
            if self.name in elements:
                elements[self.name].append(bumper)
            else:
                elements[self.name] = [bumper]
        elif self.name in ('OtherCube', 'DarkCube'):
            shorthands = {'n': 'North', 's': 'South', 'w': 'West', 'e': 'East', 'd': 'Down', 'u': 'Up'}
            events = []
            if 'KeyEvents' in params:
                events = params.pop('KeyEvents').split(',')

            params['PositionTrigger'] = params.pop('Position')

            if 'PositionCube' in params:
                new_pos = []
                for i, coord in enumerate(params['PositionCube'].split(',')):
                    if coord[0] == '~':
                        new_pos.append(pos[i] + int(coord[1:]))
                    else:
                        new_pos.append(int(coord))
                params['PositionCube'] = v3d(tuple(new_pos))

            cube = et.Element(self.name, params)
            for e in events:
                cube.append(et.Element(f'{shorthands[e[0].lower()]}{shorthands[e[1].lower()]}', {'TimeOffset': e[2:]}))

            if self.name in elements:
                elements[self.name].append(cube)
            else:
                elements[self.name] = [cube]
        else:
            if self.name == 'Checkpoint':
                params['RespawnZ'] = str(int(params.get('RespawnZ', 0)) + pos[1])

            if self.name in elements:
                elements[self.name].append(et.Element(self.name, params))
            else:
                elements[self.name] = [et.Element(self.name, params)]


dynamic_parts = {
    'minecraft:white_shulker_box': DynamicPart('MovingPlatform', timing=('TravelTime', 'PauseTime'), position=False,
                                               items={
                                                   'minecraft:quartz_slab': {'FullBlock': 'False'},
                                                   'minecraft:red_wool': {'AutoStart': 'False'}
                                               }),
    'minecraft:chest': DynamicPart('Waypoint', timing=('TravelTime', 'PauseTime'), higher_pos=True),
    'minecraft:light_gray_shulker_box': DynamicPart('Button', visible=True, items={
        'minecraft:stone_button': {'DisableCount': '%'}
    }),
    'minecraft:dropper': DynamicPart('FallingPlatform', timing=('FloatTime',), higher_pos=True),
    'minecraft:barrel': DynamicPart('Bumper', timing=('StartDelay', 'PulseRate'), items={
        'minecraft:red_wool': {'Enabled': 'False'}
    }),
    'minecraft:red_shulker_box': DynamicPart('ResizerGrow', visible=True, radius=True),
    'minecraft:green_shulker_box': DynamicPart('ResizerShrink', visible=True, radius=True),
    'minecraft:orange_shulker_box': DynamicPart('OtherCube', radius=True),
    'minecraft:black_shulker_box': DynamicPart('DarkCube', radius=True),
    'minecraft:blue_shulker_box': DynamicPart('Checkpoint', radius=True, items={'minecraft:arrow': {'RespawnZ': '%'}}),
    'minecraft:pink_shulker_box': DynamicPart('CameraTrigger', timing=('StartDelay', 'Duration'))
}


def v3d(data: tuple, higher=False) -> str:
    return f'{data[0]},{data[2]},{data[1] + int(higher)}'


def read_book(pages: list, has_title=False) -> tuple[str, dict] | dict:
    lines = sum([page.split('\n') for page in [tag.value for tag in pages]], start=[])
    if has_title:
        return lines[0], {i.split('=')[0]: i.split('=')[1] for i in lines[1:] if '=' in i}
    else:
        return {i.split('=')[0]: i.split('=')[1] for i in lines if '=' in i}


mc_static_blocks = {
    'minecraft:quartz_block': (0xFF, 0xFF, 0xFF),
    'minecraft:quartz_slab': (0xFF, 0xFF, 0x80),
    'minecraft:oak_planks': (0xFF, 0x80, 0xFF),
    'minecraft:spruce_planks': (0xFF, 0x40, 0xFF),
    'minecraft:dark_oak_planks': (0xFF, 0x00, 0xFF),
    'minecraft:oak_slab': (0xFF, 0x80, 0x80),
    'minecraft:spruce_slab': (0xFF, 0x40, 0x80),
    'minecraft:dark_oak_slab': (0xFF, 0x00, 0x80),
    'minecraft:smooth_stone': (0xE0, 0x00, 0x00),
    'minecraft:smooth_stone_slab': (0xC0, 0x00, 0x00),
    'minecraft:white_stained_glass': (0x00, 0xFF, 0xFF),
    'minecraft:light_gray_stained_glass': (0x00, 0x80, 0xFF),
    'minecraft:gray_stained_glass': (0x00, 0x40, 0xFF),
    'minecraft:black_stained_glass': (0x00, 0x00, 0xFF),
    'minecraft:glass': (0xFF, 0x00, 0x00)
}

world_folder = sys.argv[1]
structure_name = sys.argv[2]

world_folder_path = os.path.join(os.path.expanduser('~'), 'AppData', 'Roaming', '.minecraft', 'saves', world_folder,
                                 'generated', 'minecraft', 'structures')

structure_files = [f for f in os.listdir(world_folder_path) if f.startswith(structure_name)]
print(f'Found {len(structure_files)} structure files: {structure_files}')

if len(structure_files) == 1:
    file = nbt.NBTFile(os.path.join(world_folder_path, structure_files[0]))
    level_size = tuple(tag.value for tag in file['size'])
else:
    coords = [f.split('_')[-1].split('.')[:-1] for f in structure_files]
    max_coords = [str(max(int(f[i]) for f in coords)) for i in range(3)]
    max_file = nbt.NBTFile(os.path.join(world_folder_path, f'{structure_name}_{".".join(max_coords)}.nbt'))
    level_size = tuple(48 * int(max_coords[i]) + max_file['size'][i].value for i in range(3))

level_images = [Image.new(mode='RGB', size=(level_size[0], level_size[2])) for _ in range(level_size[1])]
level_settings = {'Size': f'{level_size[0]}x{level_size[2]}x{level_size[1]}'}
level_filename = ''
print(f'Level size: {level_size}')

for f in structure_files:
    print(f'Loading file: {f}')
    file = nbt.NBTFile(os.path.join(world_folder_path, f))
    mc_palette = [tag['Name'] for tag in file['palette']]

    for e in file['blocks']:
        block = str(mc_palette[e['state'].value])
        pos= tuple(
            (48 * int(f.split('_')[-1].split('.')[:-1][i]) if len(structure_files) > 1 else 0) + e['pos'][i].value for i
            in range(3))
        if block == 'minecraft:lectern':
            try:
                title, data = read_book(e['nbt']['Book']['tag']['pages'], has_title=True)

                if title.startswith('Level'):
                    level_filename = title[6:]
                    level_settings.update(data)
                else:
                    DynamicPart('ButtonSequence', position=False).to_element([e['nbt']['Book']])
            except Exception as e:
                print(str(e))
        elif block == 'minecraft:gold_block':
            level_settings['SpawnPoint'] = v3d(pos)
        elif block == 'minecraft:emerald_block':
            level_settings['ExitPoint'] = v3d(pos, True)
        elif block == 'minecraft:oak_sign':
            text = json.loads(e['nbt']['front_text']['messages'][0].value)['text']
            level_images[pos[1]].putpixel(xy=(pos[0], pos[2]),
                                          value=tuple(int(text[i * 2:(i + 1) * 2], 16) for i in range(3)))
        elif block in mc_static_blocks:
            level_images[pos[1]].putpixel(xy=(pos[0], pos[2]), value=mc_static_blocks[block])
        elif block == 'minecraft:prismarine':
            if 'Prism' in elements:
                elements['Prism'].append(et.Element('Prism', {'Position': v3d(pos)}))
            else:
                elements['Prism'] = [et.Element('Prism', {'Position': v3d(pos)})]
        elif block in dynamic_parts:
            if block == 'minecraft:barrel':
                dynamic_parts[block].to_element(e['nbt'].get('Items', []), pos, file['palette'][e['state'].value]['Properties']['facing'].value.title())
            else:
                dynamic_parts[block].to_element(e['nbt'].get('Items', []), pos)
        else:
            level_images[pos[1]].putpixel(xy=(pos[0], pos[2]), value=(0x00, 0x00, 0x00))

if 'ID' not in level_settings:
    print('Error: Level ID missing')

if 'SpawnPoint' not in level_settings:
    print('Error: Spawn point missing')

if 'ExitPoint' not in level_settings:
    print('Error: Exit point missing')

print('Writing XML')
root = et.Element('Level', level_settings)

for item, e in moving_platforms.items():
    for waypoint in dict(sorted(waypoints[item].items())).values():
        e.append(waypoint)
    root.append(e)

for elem in elements.get('Button', []):
    pos = tuple(int(i) for i in elem.get('Position').split(','))
    pos_platform = f'{pos[0]},{pos[1]},{pos[2] - 1}'
    if pos_platform in moving_platforms_by_position:
        elem.attrib.pop('Position')
        elem.attrib['MovingPlatformID'] = moving_platforms_by_position[pos_platform]

for elem in elements.get('ButtonSequence', []):
    if 'ButtonIDs' in elem.attrib:
        button_ids = elem.get('ButtonIDs').split(',')
        buttons = {button.get('ID'): button for button in elements.get('Button', []) if button.get('ID') in button_ids}
        for button in buttons.values():
            elements.get('Button', []).remove(button)

        for id in button_ids:
            elem.append(buttons[id])

        elem.attrib.pop('ButtonIDs')

for part in elements:
    for elem in elements[part]:
        root.append(elem)

et.ElementTree(root).write(f'{level_filename}.xml')

print('Writing images')
for i, im in enumerate(level_images):
    im.save(fp=f'{level_filename}.{i}.png')

print('Compiling level')
subprocess.run(f'EdgeTool.exe {level_filename}.xml')

print('Moving compiled files')
shutil.move(os.path.realpath(f'{level_filename}.bin'),
            os.path.join(r'C:\Program Files (x86)\Steam\steamapps\common\EDGE\levels', f'{level_filename}.bin'))
eso = [f for f in os.listdir() if f.endswith('.eso')][0]
shutil.move(os.path.realpath(eso), os.path.join(r'C:\Program Files (x86)\Steam\steamapps\common\EDGE\models', eso))

print('Removing files')
os.remove(f'{level_filename}.xml')
for i in range(len(level_images)):
    os.remove(f'{level_filename}.{i}.png')
