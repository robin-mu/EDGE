import struct
import pandas as pd
import sys

# execute with path to text.loc as first argument

def int16(file):
    return struct.unpack_from('<h', file.read(2))[0]
    
def uint32(file):
    return struct.unpack_from('<I', file.read(4))[0]
    
def string_ascii(file, length):
    return struct.unpack_from(f'<{length}s', file.read(length))[0].decode('utf-8')
    
def string_unicode(file, length):
    return struct.unpack_from(f'<{length * 2}s', file.read(length * 2))[0].decode('utf-16')

file = sys.argv[1] if len(sys.argv) > 1 else 'text.loc'

with open(file, 'rb') as f:
    numlangs = int16(f)
    language_data = {string_ascii(f, 2): [] for _ in range(numlangs)}

    numstrings = int16(f)
    m_StringKeys = []

    for _ in range(numstrings):
        m_StringKeys.append(uint32(f))

        for lang in language_data.keys():
            string_length = int16(f)
            string_value = string_unicode(f, string_length)

            language_data[lang].append(string_value.rstrip('\x00'))

    pd.DataFrame(language_data, index=m_StringKeys).to_csv('text.csv')