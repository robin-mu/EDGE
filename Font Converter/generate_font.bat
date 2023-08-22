@echo off

echo ======================================================================
echo EDGE Font Converter
echo This tool converts the font.bin file from EDGE to .svg and .ttf files.
echo ======================================================================
echo The python module svgwrite is needed. Installing...
pip install svgwrite

python.exe font_bin_parser.py

echo FontForge is used to generate the .ttf file.
set /P "FF=Enter the path to your FontForgeBuilds folder: "
set "PATH=%FF%;%FF%\bin;%PATH:"=%"

echo Generating .ttf file...
ffpython fontforge_script.py
pause