This page lists all currently known memory pointers to relevant game variables. 
- Unless otherwise specified, all variables are signed 4 Byte variables. 
- The values of all timing related variables are in ticks.
- All offsets are notated as hexadecimal numbers.

# [Menu Screens and Game State](Menu-Screens-and-Game-State)
| Variable Name                        | Pointer and Offsets                           | Comment                                                                                                                                                                          |
|--------------------------------------|-----------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Menu screen                          | `edge.exe+1F9080, 50`                         | See [Menu screens table](Menu-Screens-and-Game-State#menu-screens) for values                                                                                                                               |
| Button selection                     | `edge.exe+1F91B4, 8*[value of screen]+44, 10` | Number of the button currently selected or pressed                                                                                                                               |
| Pause options selection              | `edge.exe+1F91B4, D4, 50`                     |                                                                                                                                                                                  |
| Pause main menu selection            | `edge.exe+1F91B4, D4, 54`                     |                                                                                                                                                                                  |

## Level select

| Variable Name      | Pointer and Offsets           | Comment                                |
|--------------------|-------------------------------|----------------------------------------|
| Level number       | `edge.exe+1F91B4, 64, 38`     | Number in level list (starting from 0) |
| Level ID           | `edge.exe+1F91B4, 64, 40, -4` |                                        |
| Beaten             | `edge.exe+1F91B4, 64, 40, 0`  |                                        |
| Best time          | `edge.exe+1F91B4, 64, 40, 4`  |                                        |
| Collected Prisms   | `edge.exe+1F91B4, 64, 40, 8`  |                                        |       
| Rank               | `edge.exe+1F91B4, 64, 40, C`  | 0 (D) to 5 (S+)                        |

These offsets only apply to the Normal level select screen. Change the first offset to `6C` or `74` for the Bonus or Extended menu variables respectively.

# Gameplay
For many of the variables here, their behavior is known, but it is not always clear for what they are used in the game's code.

| Variable Name | Pointer and Offsets        | Comment                                                                                          |
|---------------|----------------------------|--------------------------------------------------------------------------------------------------|
| Level ID      | `edge.exe+1F9040, 78`      |                                                                                                  |
| Total steps   | `edge.exe+1F9064, 34, 164` |                                                                                                  |
| Deaths        | `edge.exe+1F9064, 104`     |                                                                                                  |
| Level clear   | `edge.exe+1F9064, B5`      | 1 Byte. Set to 1 when touching the exit point of a level, set to 0 when exiting the clear screen |


## [Timing](The-In-Game-Timer-and-Ranking)

| Variable Name                        | Pointer and Offsets    | Comment                                                  |
|--------------------------------------|------------------------|----------------------------------------------------------|
| Time                                 | `edge.exe+1F9064, 10C` |                                                          |
| Edging                               | `edge.exe+1F9064, 6C`  | 1 if currently edging, 0 if not                          |
| Current EDGE Time                    | `edge.exe+1F9064, 7B`  | Time that gets displayed next to the cube when edging    |
| Total EDGE Time                      | `edge.exe+1F9064, 108` | Time that is shown in the second row of the clear screen |
| Final Time with EDGE Time subtracted | `edge.exe+1F9064, 110` | Time that is shown in the third row of the clear screen  |
| Total time spent in levels           | `edge.exe+1F9064, 4`   | Same as time, but never resets                           |

## Positioning

| Variable Name         | Pointer and Offsets          | Comment                                                                                                                |
|-----------------------|------------------------------|------------------------------------------------------------------------------------------------------------------------|
| Cube action           | `edge.exe+1F9064, 34, 4`     | 0: Standing, 1: Moving, 2: Climbing, 3: Falling, 6: Shrinking, 7: Growing                                              |
| Cube moving direction | `edge.exe+1F9064, 34, C`     | Moving: 1: NE, 2: SW, 3: NW, 4: SE; Climbing: 5: NE, 6: SW, 7: NW, 8: SE                                               |
| X Coordinate          | `edge.exe+1F9064, 34, 28/34` | Coordinates measured in blocks                                                                                         |
| Y Coordinate          | `edge.exe+1F9064, 34, 2C/38` |                                                                                                                        |
| Z Coordinate          | `edge.exe+1F9064, 34, 30/3C` |                                                                                                                        |
| X Subblock Coordinate | `edge.exe+1F9064, 34, 4C/70` | Coordinates measured in subblocks (1/30 of a block). Used for precise positioning, for example when moving as minicube |
| Y Subblock Coordinate | `edge.exe+1F9064, 34, 50/74` |                                                                                                                        |
| Z Subblock Coordinate | `edge.exe+1F9064, 34, 54/78` |                                                                                                                        |

All variables with the second offset between `28` and `12C` probably have something to do with the position of the cube, but it is not yet clear what exact function each variable has. 

## Cube size

| Variable Name    | Pointer and Offsets        | Comment                                                                                                                                  |
|------------------|----------------------------|------------------------------------------------------------------------------------------------------------------------------------------|
| Cube render size | `edge.exe+1F9064, 34, 134` | Normally 4096, increases to 12288 when shrinking, decreases to 4096 when growing. The higher the value, the smaller the cube is rendered |
| Cube size        | `edge.exe+1F9064, 34, 138` | 1: Normal, 3: Minicube; When set to 1, the cube will slowly accelerate, otherwise it will be at max speed instantly                      |
| Step size        | `edge.exe+1F9064, 34, 13C` | 30: Normal, 10: Minicube; The number of 30ths of a block that the cube will move with each step                                          |

## [Speed and acceleration](Speed-and-Acceleration)

| Variable Name  | Pointer and Offsets        | Comment     |
|----------------|----------------------------|-------------|
| Angle          | `edge.exe+1F9064, 34, 140` |             |
| Angle Speed    | `edge.exe+1F9064, 34, 144` |             |
| Speed          | `edge.exe+1F9064, 34, 148` |             |
| Starting Speed | `edge.exe+1F9064, 34, 14C` | Always 4505 |

## Prisms

| Variable Name                        | Pointer and Offsets        | Comment                                                                                 |
|--------------------------------------|----------------------------|-----------------------------------------------------------------------------------------|                                                                                        
| Prisms                               | `edge.exe+1F9064, 11C`     | Prisms currently collected                                                              |
| Total Prisms                         | `edge.exe+1F9040, 30`      | Total prisms in current level                                                           |
| Steps since last prism               | `edge.exe+1F9064, 34, 160` | The higher this value, the lower the cube's acceleration                                |
| Prism boost timer                    | `edge.exe+1F9064, 34, 168` | Steps since last prism does not increase for 100 ticks after a prism has been collected |

## Checkpoints
| Variable Name                        | Pointer and Offsets        | Comment                                                                                                                                                     |
|--------------------------------------|----------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Checkpoint                           | `edge.exe+1F9064, 120`     | Number of the last activated checkpoint. -1 means no checkpoint has been activated yet                                                                      |
| Steps since last prism at checkpoint | `edge.exe+1F9064, 124`     | Value of steps since last prism when the last checkpoint was activated                                                                                      |
| Total steps at checkpoint            | `edge.exe+1F9064, 128`     | Value of total steps when the last checkpoint was activated                                                                                                 |
| Cube size at checkpoint              | `edge.exe+1F9064, 12C`     | Value of cube size when the last checkpoint was activated. This value will be used to calculate cube render size and step size when returning to checkpoint |
| Prisms at checkpoint                 | `edge.exe+1F9064, 130`     | Value of prisms when the last checkpoint was activated                                                                                                      |

## Other cube
Changing the first offset from `34` to `38` yields the equivalent variables for other cubes (holocube and darkcube).

# Inputs
Keyboard inputs are managed in the memory region around `edge.exe+1F8BEB`. Here, each **byte** corresponds to a button. If its value is set to anything but 0, the corresponding button will be registered as being pressed. The most important buttons are:

| Button | Pointer           |
|--------|-------------------|
| W      | `edge.exe+1F8C27` |
| A      | `edge.exe+1F8C11` |
| S      | `edge.exe+1F8C23` |
| D      | `edge.exe+1F8C14` |
| Esc    | `edge.exe+1F8BEB` |
| Enter  | `edge.exe+1F8BDD` |
| Shift  | `edge.exe+1F8BE0` |

## Mouse
| Button             | Pointer           |
|--------------------|-------------------|
| Mouse X Coordinate | `edge.exe+1F8AE8` |
| Mouse Y Coordinate | `edge.exe+1F8AEC` |