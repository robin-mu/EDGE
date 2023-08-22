import fontforge
import os

pixelsize = 50
space_width = 9
bearing = 20
font = fontforge.font()
font.familyname = 'edge'
font.fontname = 'edge'
font.fullname = 'edge'
font.encoding = 'UnicodeFull'
font.em = 512

font.createMappedChar('space').width = pixelsize * space_width // 2

for f in [file[:-4] for file in os.listdir() if file.endswith('.svg')]:
    name = f[:-6] if f.endswith('_lower') else f
    char = font.createMappedChar(name)
    char.importOutlines(f + '.svg')
    char.left_side_bearing = bearing
    char.right_side_bearing = bearing

font.generate('edge.ttf')
