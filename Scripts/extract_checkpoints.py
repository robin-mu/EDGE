import os
import pandas as pd
from bs4 import BeautifulSoup as bs

# execute script in a place with a folder called "levels" containing the decompiled level xml files

checkpoints = []

for file in [f for f in os.listdir('levels') if f.endswith('.xml') and f != 'mapping.xml']:
    soup = ''
    with open(f'levels/{file}', 'r') as f:
        soup = bs(f.read(), 'xml')
    
    id = soup.find('Level')['ID']
    name = soup.find('Level')['Name']
    
    for checkpoint in soup.find_all('Checkpoint'):
        data = {'id': id, 'name': name, 'position': checkpoint['Position']}
        data['respawn_z'] = checkpoint['RespawnZ'] if checkpoint.has_attr('RespawnZ') else 0
        data['radius_x'] = checkpoint['Radius'].split(',')[0] if checkpoint.has_attr('Radius') else 0
        data['radius_y'] = checkpoint['Radius'].split(',')[1] if checkpoint.has_attr('Radius') else 0
        checkpoints.append(data)
    
df = pd.DataFrame.from_records(checkpoints)
df.to_csv('checkpoints.csv', index=False)