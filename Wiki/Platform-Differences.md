EDGE has been released for 7 Platforms: iOS, Java Mobile Phones, PlayStation Portable, Android, Steam, Wii U and Nintendo 3DS.  
The Java and PSP version feature the same level files and will be referred to as Java version.  
The iOS and Mobile version feature the same level files and will be referred to as Mobile version.  
The Steam, Wii U and 3DS version also feature the same levels and will be referred to as Steam version.

This page lists the differences between the Java, Mobile and Steam versions of EDGE.
Levels not listed here are the same on all versions.

It uses the level naming convention from the [speedrun.com leaderbord](https://www.speedrun.com/edge/levels), which prefixes the level names with their level number in the Steam version, e.g. N01 1st contact, E01 first step etc.

The contents of this page are summarized in [this spreadsheet](https://docs.google.com/spreadsheets/d/1RhS7fzXndsYxC3sYiWNMPsVhdV8m7CWqBt8ZRt3frYE/edit?usp=sharing).

# Steam
The EDGE Steam version features 124 level files.

## Playable (109 levels)
- Normal: 48 levels (N01-N48)
- Bonus: 17 levels (B01-B17)
- Extended 44 levels (E01-E44)

## Only in game files (15 levels)
- 4 hidden levels: 
  - scientist_803 (H02 scientist)
  - switchboard_807 (H03 switchboard)
  - islands_809 (H01 islands)
  - tide_814 (H04 tide)
- 3 winter levels (covered in snow, only playable in December): 
  - level309_winter (1st contact)
  - level541_winter (darkcube)
  - hangout_815_winter
- 8 ending levels (automatic levels that play during the credits): 
  - ending_bonus
  - ending_bonus_allcomplete
  - ending_demo_bonus
  - ending_demo_normal
  - ending_extended
  - ending_extended_allcomplete
  - ending_normal
  - ending_normal_allcomplete

Additionally, the Wii U and 3DS versions have level554 (path of piracy) only in their game files, totaling to 125 level files for these versions.
# Java
The Java versions (normal and extended) feature 91 level files.

## Playable (90 levels)
- Normal: 46 levels; N47 push me and N48 perfect cell are missing
- Extended: 44 levels

## Only in game files (1 level)
- level554 (path of piracy)

# Mobile
The Mobile versions (normal and extended) feature 130 level files.

## Playable (128 levels)
- Normal: 48 levels
- Bonus: 17 levels
- Extended: 48 levels; 44 levels from the other versions plus M01 minicube, M02 furious bot, M03 vertical way, and M04 cargo
- Extended Bonus: 15 levels (X01-X15)

## Only in game files (2 levels)
- level535 (first step)
- level554 (path of piracy)

# Mapping differences
- B16 winners and B17 zias and winners are swapped in the Mobile version, meaning that bonus level 16 is B17 zias and bonus level 17 is B16 winners.
- E03 click and E04 moving walls are swapped in Mobile and Java versions, meaning that extended level 3 is E04 moving walls and extended level 4 is E03 click.
- The Mobile version features 4 more extended levels than the other versions. These are 
  - Level 10: M01 minicube
  - Level 12: M02 furious bot
  - Level 14: M03 vertical way
  - Level 19: M04 cargo

# Level differences
- Between the Java and Mobile version, only four levels are different: N07 speedrun, N10 metro, N14 peripherique and E01 first step. All other levels are the same and will only be referred to as Mobile version.
- Mobile/Java levels save the time thresholds used for ranking multiplied by 100 compared to the Steam version. For example, if the time needed for S+ rank is 9 seconds, 9 gets saved in the Steam version while 900 gets saved in the Mobile/Java version. Since the thresholds are saved as 16-bit unsigned integers which have a limit of 65536, any time higher than 655 seconds will be saved incorrectly in the Mobile/Java files.
- Some levels had to be adjusted because of the different camera in the Mobile and Steam versions. For example, gaps in walls that could not be seen on the Mobile version had to be filled in the Steam version. (The right images show the respective Mobile level loaded in the Steam version)
  <img src="https://raw.githubusercontent.com/wiki/robin-mu/EDGE/images/PlatformDifferences/n23-gap.png" />
  <img src="https://raw.githubusercontent.com/wiki/robin-mu/EDGE/images/PlatformDifferences/n24-gap.png" />
  <img src="https://raw.githubusercontent.com/wiki/robin-mu/EDGE/images/PlatformDifferences/n30-gap.png" />
- In almost all normal levels and some extended levels, the respawn Z-coordinates and radii of many checkpoints are bigger in the Steam version. The Z-coordinate adjustments were probably necessary for a smoother gameplay since in the Mobile version, the camera just cuts to the cube after dying while it smoothly moves to the cube in the Steam version.

## N01 first contact
- Steam:
  - 1 additional prism, 2 moved prisms
    <img src="https://raw.githubusercontent.com/wiki/robin-mu/EDGE/images/PlatformDifferences/n01s-p+.png"/>
    <img src="https://raw.githubusercontent.com/wiki/robin-mu/EDGE/images/PlatformDifferences/n01-p.png"/>
  - 1 moved checkpoint
    <img src="https://raw.githubusercontent.com/wiki/robin-mu/EDGE/images/PlatformDifferences/n01-cp.png"/>
  - Camera triggers added
  - Added everything connected to the "Quick response" achievement: Invisible buttons at the exit, block at the north-east that will make the QR-code appear, additional checkpoint.
    <img src="https://raw.githubusercontent.com/wiki/robin-mu/EDGE/images/PlatformDifferences/n01s-cp+.png"/>

## N03 playground
- Steam:
  - 1 additional prism, 1 moved prism
    <img src="https://raw.githubusercontent.com/wiki/robin-mu/EDGE/images/PlatformDifferences/n03-p.png"/>
  - 2 additional checkpoints
    <img src="https://raw.githubusercontent.com/wiki/robin-mu/EDGE/images/PlatformDifferences/n03s-cp+.png"/>
  - Slightly different camera triggers

## N04 pushing stars
- Steam: Holocube trigger moved by 1 block
  <img src="https://raw.githubusercontent.com/wiki/robin-mu/EDGE/images/PlatformDifferences/n04-holo.png"/>
- Different time thresholds: 
  - S+: 35.5 seconds (Mobile) / 35 seconds (Steam)
  - S: 37.79 seconds (Mobile) / 37 seconds (Steam)

## N07 speedrun
- Steam:
  - 1 additional prism (and path to it), 2 moved prisms
  - 2 additional checkpoints
    <img src="https://raw.githubusercontent.com/wiki/robin-mu/EDGE/images/PlatformDifferences/n07s-cp+.png"/>
  - Lower spawn point
- Bridge at the end: 
  - Java: bridge, two prisms
  - Mobile: no bridge, two prisms
  - Steam: bridge but not accessible, no prisms
  <img src="https://raw.githubusercontent.com/wiki/robin-mu/EDGE/images/PlatformDifferences/n07.png"/>

## N08 milky way
- Different time thresholds: 
  - S+: 61.5 seconds (Mobile) / 61 seconds (Steam)

## N09 8-bit
- Different time thresholds:
  - S+: 47.8 seconds (Mobile) / 47 seconds (Steam)
- Mobile: 1 additional block under moving platforms that can't be seen in-game

## N10 metro
- Steam:
  - 1 additional prism
    <img src="https://raw.githubusercontent.com/wiki/robin-mu/EDGE/images/PlatformDifferences/n10s-p+.png"/>
  - 1 moved checkpoint
    <img src="https://raw.githubusercontent.com/wiki/robin-mu/EDGE/images/PlatformDifferences/n10-cp.png"/>
  - 1 additional falling platform
  - Invisible buttons behind the metro entry to trigger the "Turnstile jumper" achievement
  - Invisible buttons at both ends of the track to trigger the "Subway" achievement
- Blocks on height 5 and 6 represented by static blocks in the Steam version and by moving platforms in the Mobile version
- Last moving platform:
  - Java: The upper platform quickly moves back and forth at a constant rate
  - Mobile: The upper platform pauses a bit after moving back and forth twice
  - Steam: The upper platform slowly moves back and forth at a constant rate, the lower platform moves a bit faster  
  <img src="https://raw.githubusercontent.com/wiki/robin-mu/EDGE/images/PlatformDifferences/n10.gif"/>

## N12 vertex
- Different time thresholds:
  - S+: 67.8 seconds (Mobile) / 67 seconds (Steam)
  - S: 71.59 seconds (Mobile) / 71 seconds (Steam)

## N14 peripherique
- Steam:
  - 1 additional checkpoint, 1 moved checkpoint
    <img src="https://raw.githubusercontent.com/wiki/robin-mu/EDGE/images/PlatformDifferences/n14s-cp+.png"/>
    <img src="https://raw.githubusercontent.com/wiki/robin-mu/EDGE/images/PlatformDifferences/n14-cp.png"/>
  - Invisible buttons on all moving "cars" to trigger the "Jumper" achievement
- Prisms at the end:
  - Java: prism on the ground
  - Mobile: prism in front of the hole to the exit
  - Steam: prism at both spots
  <img src="https://raw.githubusercontent.com/wiki/robin-mu/EDGE/images/PlatformDifferences/n14.png"/>

## N18 edge time
- Different time thresholds:
  - S: 75.5 seconds (Mobile) / 75 seconds (Steam)

## N19 chase
- Mobile: One button invisible
  <img src="https://raw.githubusercontent.com/wiki/robin-mu/EDGE/images/PlatformDifferences/n19.png"/>

## N20 landing
- Steam: Added platform that saves the player if he isn't able to land on the first moving block. After three tries, the obstacle is skipped
  <img src="https://raw.githubusercontent.com/wiki/robin-mu/EDGE/images/PlatformDifferences/n20s.png"/>
- Different time thresholds:
  - S: 73.5 seconds (Mobile) / 73 seconds (Steam)

## N21 chess
- Steam: The path at the end is 1 block thinner and 4 blocks longer
  <img src="https://raw.githubusercontent.com/wiki/robin-mu/EDGE/images/PlatformDifferences/n21.png"/>

## N22 switch keep
- Steam: 1 moved checkpoint
  <img src="https://raw.githubusercontent.com/wiki/robin-mu/EDGE/images/PlatformDifferences/n22-cp.png"/>

## N24 higher
- Steam:
  - 2 additional checkpoints, 1 moved checkpoint
    <img src="https://raw.githubusercontent.com/wiki/robin-mu/EDGE/images/PlatformDifferences/n24s-cp+.png"/>
    <img src="https://raw.githubusercontent.com/wiki/robin-mu/EDGE/images/PlatformDifferences/n24-cp.png"/>
  - Shortcut with button and moving block near the last bridge
    <img src="https://raw.githubusercontent.com/wiki/robin-mu/EDGE/images/PlatformDifferences/n24s.png"/>
  - Hidden button, camera trigger and checkpoint at the exit to trigger the "Chicken" achievement
  - Invisible button and invisible resizer under the prism at the end of the wall section to trigger the "Tumbling travels" achievement when reached as a minicube
  - Holocube trigger moved by one block
    <img src="https://raw.githubusercontent.com/wiki/robin-mu/EDGE/images/PlatformDifferences/n24-holo.png"/>
- Mobile: Floating block that can't be seen in-game (The right image shows the Mobile level loaded in the Steam vesion)
  <img src="https://raw.githubusercontent.com/wiki/robin-mu/EDGE/images/PlatformDifferences/n24-gap.png"/>

## N25 squadron
- Steam: 1 additional checkpoint, 1 moved checkpoint (to prevent softlocking)
  <img src="https://raw.githubusercontent.com/wiki/robin-mu/EDGE/images/PlatformDifferences/n25s-cp+.png"/>
  <img src="https://raw.githubusercontent.com/wiki/robin-mu/EDGE/images/PlatformDifferences/n25-cp.png"/>
- Mobile: Hole in a roof near the exit
  <img src="https://raw.githubusercontent.com/wiki/robin-mu/EDGE/images/PlatformDifferences/n25m.png"/>

## N26 metronome
- Steam: 2 moved checkpoints
  <img src="https://raw.githubusercontent.com/wiki/robin-mu/EDGE/images/PlatformDifferences/n26-cp1.png"/>
  <img src="https://raw.githubusercontent.com/wiki/robin-mu/EDGE/images/PlatformDifferences/n26-cp2.png"/>

## N27 orion
- Steam: 4 blocks moved because they only looked correctly placed from the camera perspective of the Mobile version. (The right image shows the Mobile level loaded in the Steam version)
  <img src="https://raw.githubusercontent.com/wiki/robin-mu/EDGE/images/PlatformDifferences/n27.png"/>

## N30 beat
- Steam:
  - 1 additional checkpoint, 1 moved checkpoint
    <img src="https://raw.githubusercontent.com/wiki/robin-mu/EDGE/images/PlatformDifferences/n30s-cp+.png"/>
    <img src="https://raw.githubusercontent.com/wiki/robin-mu/EDGE/images/PlatformDifferences/n30-cp.png"/>
  - The start is at a lower X-coordinate
  - One moving platform that pushes the cube off the edge is slower
    <img src="https://raw.githubusercontent.com/wiki/robin-mu/EDGE/images/PlatformDifferences/n30s-mp.png"/>
  - Less moving platforms at the end, the platforms also move slower
  - Bigger exit platform in Steam version
    <img src="https://raw.githubusercontent.com/wiki/robin-mu/EDGE/images/PlatformDifferences/n30.png"/>
- 1 block saved as static block in the Steam version and as moving platform in the Mobile version

## N31 star castle
- Steam: Invisible button at the exit to trigger the "Perfect landing" achievement
- Different time thresholds:
  - S+: 66.5 seconds (Mobile) / 66 seconds (Steam)

## N32 sticker
- Steam: 1 additional checkpoint
  <img src="https://raw.githubusercontent.com/wiki/robin-mu/EDGE/images/PlatformDifferences/n32s-cp+.png"/>

## N38 speedrun 2
- Steam:
  - 1 prism moved above the exit, button and moving platform added to get there
    <img src="https://raw.githubusercontent.com/wiki/robin-mu/EDGE/images/PlatformDifferences/n38.png"/>
  - 1 additional checkpoint
    <img src="https://raw.githubusercontent.com/wiki/robin-mu/EDGE/images/PlatformDifferences/n38s-cp+.png"/>

## N39 edge master
- Steam: Slightly edited one obstacle (moving platform speed and walls)
  <img src="https://raw.githubusercontent.com/wiki/robin-mu/EDGE/images/PlatformDifferences/n39.gif"/>

## N40 cube invaders
- Steam: 
  - 1 additional checkpoint, 2 moved checkpoints
    <img src="https://raw.githubusercontent.com/wiki/robin-mu/EDGE/images/PlatformDifferences/n40s-cp+.png"/>
    <img src="https://raw.githubusercontent.com/wiki/robin-mu/EDGE/images/PlatformDifferences/n40-cp1.png"/>
    <img src="https://raw.githubusercontent.com/wiki/robin-mu/EDGE/images/PlatformDifferences/n40-cp2.png"/>
  - Additional moving platforms and invisible buttons to trigger the achievements "Invader" and "An enemy of my enemy"
    <img src="https://raw.githubusercontent.com/wiki/robin-mu/EDGE/images/PlatformDifferences/n40s-a.png"/>
- Different time thresholds:
  - D: 184.64 seconds (Mobile) / 840 seconds (Steam) (the Mobile time is not correct and caused by an unsigned short overflow since 84000-65536=18464)

## N41 starfield
- Steam: 
  - 2 moved prisms
    <img src="https://raw.githubusercontent.com/wiki/robin-mu/EDGE/images/PlatformDifferences/n41-p1.png"/>
    <img src="https://raw.githubusercontent.com/wiki/robin-mu/EDGE/images/PlatformDifferences/n41-p2.png"/>
  - 1 additional checkpoint, 1 moved checkpoint
    <img src="https://raw.githubusercontent.com/wiki/robin-mu/EDGE/images/PlatformDifferences/n41s-cp+.png"/>
    <img src="https://raw.githubusercontent.com/wiki/robin-mu/EDGE/images/PlatformDifferences/n41-cp.png"/>
- Blocks on height 5 represented by static blocks in the Steam version and by moving platforms in the Mobile version (In the right image you can see that the blocks don't have a checkered pattern to them because they are moving platforms). When starting the level, the blocks move shortly in the Mobile version
  <img src="https://raw.githubusercontent.com/wiki/robin-mu/EDGE/images/PlatformDifferences/n41.png"/>

## N42 bonus
- Steam: 3 additional checkpoints, 1 moved checkpoint
  <img src="https://raw.githubusercontent.com/wiki/robin-mu/EDGE/images/PlatformDifferences/n42s-cp+.png"/>
  <img src="https://raw.githubusercontent.com/wiki/robin-mu/EDGE/images/PlatformDifferences/n42-cp.png"/>

## N45 earthquake
- Steam:
  - 1 additional prism at the end
    <img src="https://raw.githubusercontent.com/wiki/robin-mu/EDGE/images/PlatformDifferences/n45s-p+.png"/>
  - 1 additional checkpoint
    <img src="https://raw.githubusercontent.com/wiki/robin-mu/EDGE/images/PlatformDifferences/n45s-cp+.png"/>
  - The moving platform with buttons on it moves one block less
    <img src="https://raw.githubusercontent.com/wiki/robin-mu/EDGE/images/PlatformDifferences/n45.png"/>
  - The moving platforms at the end move slower and with a more predictable rhythm
    <img src="https://raw.githubusercontent.com/wiki/robin-mu/EDGE/images/PlatformDifferences/n45.gif"/>

## N46 vertigo
- Steam: 1 additional checkpoint, 2 moved checkpoints
  <img src="https://raw.githubusercontent.com/wiki/robin-mu/EDGE/images/PlatformDifferences/n46s-cp+.png"/>
  <img src="https://raw.githubusercontent.com/wiki/robin-mu/EDGE/images/PlatformDifferences/n46-cp1.png"/>
  <img src="https://raw.githubusercontent.com/wiki/robin-mu/EDGE/images/PlatformDifferences/n46-cp2.png"/>
- Blocks on height 5 and above represented by static blocks in the Steam version and by moving platforms in the Mobile version

## N47 push me
- Steam: 2 additional checkpoints
  <img src="https://raw.githubusercontent.com/wiki/robin-mu/EDGE/images/PlatformDifferences/n47s-cp+.png"/>

## N48 perfect cell
- Steam: button changed to button with moving platform underneath
  <img src="https://raw.githubusercontent.com/wiki/robin-mu/EDGE/images/PlatformDifferences/n48.png"/>

## E01 first step and E04 moving walls
These levels are a bit difficult to differentiate: 
While the first extended level on Steam, Mobile and Java version is called "first step", the underlying filenames are not the same, 
i.e. the Steam version has `level537.bin` as the first level while the Mobile version has `level535_3D.bin` and the Java version has `level535.bin`.
The same applies for the level "moving walls" with the added difficulty of "click" and "moving walls" being swapped in the Mobile and Java versions compared to the Steam version.
Here is a table summarizing these differences:

|                      | Steam                            | Mobile                         | Java                          |
|----------------------|----------------------------------|--------------------------------|-------------------------------|
| **Extended Level 1** | `level537.bin` (first step)      | `level535_3D.bin` (first step) | `level535.bin` (first step)   |
| **Extended Level 3** | `level538.bin` (click)           | `level537.bin` (moving walls)  | `level537.bin` (moving walls) |
| **Extended Level 4** | `level535_3D.bin` (moving walls) | `level538.bin` (click)         | `level538.bin` (click)        |

Considering the level names and the fact that the sfx names found in `mapping.xml` are `ex_01_first_step`, `ex_03_moving_walls` and `ex_04_click`, the level order present in the Mobile and Java version seems more natural, while the Steam level order was probably changed afterward.

However, the content of these levels is only determined by their ID (the number in the filename), not by their in-game name or number on the level select screen, so the ID will be used for comparison.

### level535(_3D).bin

|                     | Java               | Mobile                                                                         | Steam                                                                                                                                                              |
|---------------------|--------------------|--------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Description**     | A very small level | Almost the same small level, but the level is built up using moving platforms. | The same small level as in the Mobile version, but there is a button where the exit in the Mobile version would be, leading to a completely new part of the level. |
| **Prisms**          | 1                  | 1 (at a different location)                                                    | 8                                                                                                                                                                  |
| **Checkpoints**     | 1                  | 4                                                                              | 10                                                                                                                                                                 |
| **Size**            | 6x8x4              | 21x8x4                                                                         | 14x19x4                                                                                                                                                            |
| **Time Thresholds** | 18, 21, 25, 28, 32 | 15, 18, 22, 25, 29                                                             | 55, 60, 70, 85, 100                                                                                                                                                |
<img src="https://raw.githubusercontent.com/wiki/robin-mu/EDGE/images/PlatformDifferences/e04.png"/>

### level537.bin
- Steam:
  - Added falling platforms and holes in the ground
  - Three blocks added to a moving platform
    <img src="https://raw.githubusercontent.com/wiki/robin-mu/EDGE/images/PlatformDifferences/e01.png"/>
  - Added one button with moving platform
    <img src="https://raw.githubusercontent.com/wiki/robin-mu/EDGE/images/PlatformDifferences/e01s-mp.png"/>
  - Faster moving platforms

## E02 climbing
- Steam: Same level, but with many moving platforms and invisible buttons activating moving platforms at the end

## E03 click
- Steam: 
  - 1 additional prism, 1 moved prism
    <img src="https://raw.githubusercontent.com/wiki/robin-mu/EDGE/images/PlatformDifferences/e03-3.png"/>
  - 1 additional checkpoint
    <img src="https://raw.githubusercontent.com/wiki/robin-mu/EDGE/images/PlatformDifferences/e03s-cp+.png"/>
  - The overall map is the same, but the puzzles have been extended by more buttons and moving platforms
    <img src="https://raw.githubusercontent.com/wiki/robin-mu/EDGE/images/PlatformDifferences/e03-1.png"/>
    <img src="https://raw.githubusercontent.com/wiki/robin-mu/EDGE/images/PlatformDifferences/e03-2.png"/>
    <img src="https://raw.githubusercontent.com/wiki/robin-mu/EDGE/images/PlatformDifferences/e03-3.png"/>
  - 1 added shortcut at the first puzzle
  - 1 added invisible button to trigger the "Minimalist" achievement

## E05 black robot
- Steam: 1 additional checkpoint and 1 additional falling platform
  <img src="https://raw.githubusercontent.com/wiki/robin-mu/EDGE/images/PlatformDifferences/e05s-cp+.png"/>

## E07 roots
- Steam:
  - 2 additional prisms, 1 moved prism (the middle prism in the Steam image is two blocks further north in the Mobile version, so it can't be seen)
    <img src="https://raw.githubusercontent.com/wiki/robin-mu/EDGE/images/PlatformDifferences/e07-2.png"/>
  - 1 additional checkpoint
    <img src="https://raw.githubusercontent.com/wiki/robin-mu/EDGE/images/PlatformDifferences/e07s-cp+.png"/>
  - Added growing roots (as moving platforms) and invisible buttons activating them
    <img src="https://raw.githubusercontent.com/wiki/robin-mu/EDGE/images/PlatformDifferences/e07-1.png"/>
    <img src="https://raw.githubusercontent.com/wiki/robin-mu/EDGE/images/PlatformDifferences/e07-3.png"/>
    <img src="https://raw.githubusercontent.com/wiki/robin-mu/EDGE/images/PlatformDifferences/e07-4.png"/>
- Different time thresholds:
  - S+: 73 seconds (Mobile) / 77 seconds (Steam)
  - S: 113 seconds (Mobile) / 118 seconds (Steam)

## E08 flick
- Steam:
  - Added 2 automatic bumpers and 2 bumpers which are activated by buttons in front of them
    <img src="https://raw.githubusercontent.com/wiki/robin-mu/EDGE/images/PlatformDifferences/e08s-bmp.png"/>
  - Exchanged many floor blocks with falling platforms

## E16 dark edge time
- Steam: 
  - 1 moved darkcube trigger to prevent softlocking (if you die, you respawn on the platform with no way to reach the darkcube trigger in the Mobile version, making progress impossible)
    <img src="https://raw.githubusercontent.com/wiki/robin-mu/EDGE/images/PlatformDifferences/e16.png"/>
  - One tower in the back of the level one block higher

## E18 paper wall
- Steam: 
  - 2 additional checkpoints
    <img src="https://raw.githubusercontent.com/wiki/robin-mu/EDGE/images/PlatformDifferences/e18s-cp+.png"/>
  - The moving platform waits a bit longer at the end
    <img src="https://raw.githubusercontent.com/wiki/robin-mu/EDGE/images/PlatformDifferences/e18s.png"/>

## E20 electric way
- Steam: some parts of the ground removed, probably for less frustration (getting kicked off the path by a bumper results in instantly returning to last checkpoint)
  <img src="https://raw.githubusercontent.com/wiki/robin-mu/EDGE/images/PlatformDifferences/e20.png"/>

## E24 don't click
- Steam:
  - 2 additional checkpoints
    <img src="https://raw.githubusercontent.com/wiki/robin-mu/EDGE/images/PlatformDifferences/e24s-cp+.png"/>
  - Moving platform with invisible button at the exit that activates the "Stubborn" achievement
  - 4 invisible buttons at different locations
    <img src="https://raw.githubusercontent.com/wiki/robin-mu/EDGE/images/PlatformDifferences/e24-btn1.png"/>
    <img src="https://raw.githubusercontent.com/wiki/robin-mu/EDGE/images/PlatformDifferences/e24-btn2.png"/>
    <img src="https://raw.githubusercontent.com/wiki/robin-mu/EDGE/images/PlatformDifferences/e24-btn3.png"/>
    <img src="https://raw.githubusercontent.com/wiki/robin-mu/EDGE/images/PlatformDifferences/e24-btn4.png"/>
  - 2 platforms start to move faster  
    <img src="https://raw.githubusercontent.com/wiki/robin-mu/EDGE/images/PlatformDifferences/e24.gif"/>
- Different time thresholds:
  - D: 95.64 seconds (Mobile) / 751 seconds (Steam) (the Mobile time is not correct and caused by an unsigned short overflow since 75100-65536=9564)

## E25 white spring
- Steam:
  - 2 additional prisms
    <img src="https://raw.githubusercontent.com/wiki/robin-mu/EDGE/images/PlatformDifferences/e25s-p.png"/>
  - 1 moved button
    <img src="https://raw.githubusercontent.com/wiki/robin-mu/EDGE/images/PlatformDifferences/e25-btn.png"/>
  - The moving wall at the end moves a bit faster
  - In the blind part at the end, the minimap is obfuscated using the minimap section of the level file in contrast to moving platforms being used in Mobile version

## E27 blind
- In the blind part, the minimap is obfuscated with the minimap section of the level file in the Steam version and with moving platforms in the Mobile version

## E28 wire
- Steam: 2 additional invisible buttons to trigger the "Hard wired" achievement

## E30 star factory
- Blocks on height 5 represented by static blocks in the Steam version and by moving platforms in the Mobile version (blocks move shortly in the Mobile version)

## E31 star dust
- Steam: 2 additional invisible buttons to trigger the "Hitchup" achievement

## E34 robot sport
- The level name is "Robot Sport" in the Mobile version and "robot sport" in the Steam version

## E38 highest flag
- Steam: 1 additional invisible button to trigger the "Flag" achievement
- Different time thresholds:
  - D: 6.64 seconds (Mobile) / 662 seconds (Steam) (the Mobile time is not correct and caused by an unsigned short overflow since 66200-65536=664)

## E40 rodeo
- Steam: 9 additional checkpoints and 2 moved checkpoints
  <img src="https://raw.githubusercontent.com/wiki/robin-mu/EDGE/images/PlatformDifferences/e40s-cp+.png"/>
  <img src="https://raw.githubusercontent.com/wiki/robin-mu/EDGE/images/PlatformDifferences/e40-cp.png"/>
- Blocks on height 5 represented by static blocks in the Steam version and by moving platforms in the Mobile version

# Other levels
## Java 1.1.1
The Java version 1.1.1 features 15 unique levels that are not present in any other version.
