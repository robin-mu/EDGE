import json
import subprocess
import os

os.chdir(os.path.dirname(os.path.realpath(__file__)))

try:
    os.mkdir('videos')
except FileExistsError:
    pass

files: list[str] = []
with open('filenames.txt', 'r') as f:
    files = json.load(f)

subprocess.run('ffmpeg.exe -filter_complex anullsrc=sample_rate=44100 -t 0.1 silence.wav')

for f in files:
    # add silence to each sound and make video clip for each sound
    subprocess.run(f'ffmpeg.exe -i .\logo.png -i "sounds/{f}" -i silence.wav -filter_complex "[1:0][2:0]concat=n=2:v=0:a=1[out]" -map 0:0 -map "[out]" -vf "drawtext=fontfile=NHaasGroteskTXPro-55Rg.ttf:text=\'{f}\':fontcolor=black:fontsize=72:x=w-tw-100:y=h-th-120" -ar 44100 "videos/{f[:-4]}.flv"')

# make file with all video filenames
with open('videos/f.txt', 'w') as file:
    for f in files:
        file.write(f'file {f[:-4]}.flv\n')

# concatenate all video files
subprocess.run('ffmpeg.exe -f concat -i videos/f.txt all_sounds.mp4')