import os
import pandas as pd
from bs4 import BeautifulSoup as bs

# execute script in a place with a folder called "levels" containing the decompiled level xml files
# compile the modified files and overwrite the original game files (make a backup first)

for file in [f for f in os.listdir('levels') if f.endswith('.xml') and f != 'mapping.xml']:    
    soup = ''
    with open(f'levels/{file}', 'r') as f:
        soup = bs(f.read(), 'xml')
    
    for checkpoint in soup.find_all('Checkpoint'):
        position = checkpoint['Position'].split(',')
        position_x = position[0]
        position_y = position[1]
        position_z = position[2]
        
        respawn_z = checkpoint['RespawnZ'] if checkpoint.has_attr('RespawnZ') else 0
        radius_x = checkpoint['Radius'].split(',')[0] if checkpoint.has_attr('Radius') else 0
        radius_y = checkpoint['Radius'].split(',')[1] if checkpoint.has_attr('Radius') else 0
    
        for x in range(int(position_x) - int(radius_x), int(position_x) + int(radius_x) + 1):
            for y in range(int(position_y) - int(radius_y), int(position_y) + int(radius_y) + 1):
                new = soup.new_tag('OtherCube')
                new['PositionTrigger'] = ','.join([str(x), str(y), position_z])
                new['PositionCube'] = ','.join([position_x, position_y, respawn_z])
                soup.Level.append(new)
    
    with open(f'levels/{file}', 'w') as f:
        f.write(soup.prettify())