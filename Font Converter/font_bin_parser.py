import svgwrite
import struct


def byte(file):
    return struct.unpack_from('<B', file.read(1))[0]


def int16(file):
    return struct.unpack_from('<h', file.read(2))[0]


chars = (list('ABCDEFGHIJKLMNOPQRSTUVWXYZ') +
         [f'{i}_lower' for i in 'abcdefghijklmnopqrstuvwxyz'] +
         list('0123456789%') +
         [f'uniFF1{i}' for i in range(1, 10)] +
         [',', '.', 'question', '!', 'colon'] +
         list("'()_-=+@") +
         ['slash', 'quotedbl', 'ccedilla_lower', 'germandbls', 'aacute', 'adieresis', 'eacute_lower', 'edieresis',
          'imacron', 'iacute', 'oacute', 'odieresis', 'uacute_lower', 'udieresis_lower', 'greater', 'less', '[', ']',
          'ntilde', 'exclamdown', 'Agrave', '$', 'Eacute', 'ecircumflex', 'Udieresis', 'dotlessi', 'scedilla', 'gbreve',
          'Ccedilla', 'ecaron', 'ccaron', 'rcaron', 'yacute', 'ncaron', 'scaron', 'zcaron', 'Uring', 'dcaron_lower',
          'Dcaron', 'otilde', 'atilde', 'Uacute', 'acircumflex', 'cacute', 'eogonek', 'zacute', 'lslash', 'aogonek',
          'sacute_lower', 'nacute', 'zdotaccent', 'Sacute'])

pixelsize = 50

try:
    with open('font.bin', 'rb') as f:
        space_width = byte(f)
        height = byte(f)  # line_spacing

        num_chars = int16(f)
        for i in range(min(len(chars), num_chars)):
            num_rects = byte(f)
            width = byte(f)

            svg = svgwrite.Drawing(chars[i] + '.svg', size=(width * pixelsize, height * pixelsize))

            for _ in range(num_rects):
                svg.add(svg.rect(insert=(byte(f) * pixelsize, byte(f) * pixelsize),
                                 size=(byte(f) * pixelsize, byte(f) * pixelsize)))

            try:
                svg.save(pretty=True)
            except Exception as e:
                print(str(e))
except FileNotFoundError:
    print('ERROR: font.bin not found. You have to copy font.bin into the folder where this batch is located.')
