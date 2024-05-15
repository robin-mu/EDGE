In memory, the `screen` variable keeps track of the current screen or game state. The current selection on each screen is saved in different variables.

# Menu screens
| Value of `screen` | Screen                                                          |
|-------------------|-----------------------------------------------------------------|
| 0                 | Black screen. Can not be reached in-game and can not be exited. |
| 1                 | Black screen. Can not be reached in-game and can not be exited. |
| 2                 | Start screen ("hi [name]")                                      |
| 3                 | Level pack select ("edge challenge")                            |
| 4                 | Normal level select                                             |
| 5                 | Bonus level select                                              |
| 6                 | Extended level select                                           |
| 7                 | Bonus level message. Can not be reached in-game.                |
| 8                 | Instructions                                                    |
| 9                 | Options                                                         |
| 10                | Credits                                                         |
| 11                | Scores select                                                   |
| 12                | Normal scores                                                   |
| 13                | Bonus scores                                                    |
| 14                | Extended scores                                                 |
| 15                | Exit game                                                       |
| 16                | Level loading screen                                            |
| 17                | In level                                                        |
| 18                | Pause screen                                                    |
| 19                | Level clear screen                                              |
| 20                | Normal all clear screen and credits                             |
| 21                | Bonus all clear screen and credits                              |
| 22                | Extended all clear screen and credits                           |
| 23                | Black screen. Can not be reached in-game and can not be exited. |

# Screen transitions
Here is a graph of all possible screen transitions:
[[images/MenuScreensAndGameState/gamestates.png]]

Notes:
- Colored arrows (or text) denote that a transition can also be triggered by pressing certain buttons, regardless of the current selection. These buttons are:
  - Red: escape, backspace or right-click
  - Green: space or enter
  - Yellow: a
  - Blue: d
- There is no way to reach screen 7, a screen telling the player to join the EDGE Steam community. It looks like this:
    
    [[images/MenuScreensAndGameState/screen7.png]]
- Screen 16 (loading screen) always directly leads to screen 17 (in level), with no way for the player to control this transition

# Buttons and other screen elements
Each screen has its own memory region at `edge.exe+1F91B4, 8*[value of screen]+44, [second offset]` which handles button selections, animations etc. 

Some second offsets with universal function are:
- `4`: Animation timer (fade in)
- `8`: Animation timer (fade out)
- `C`: Previous selection
- `10`: Button selection

## Level select
TODO

## Screen scroll
In the credits (accessed through options or the all clear screen), the pointer `edge.exe+1F91B4, 94/E4/EC/F4, 4C` (as a float) shows the scroll position of the screen, ranging from -4.0 to 6060.0 (6068.0 on all clear screen). The pointer `edge.exe+1F91B4, 94/E4/EC/F4, 50` (as float) shows the scroll speed, changing from 4.0 to 16.0 when you hold up, down, space, enter, or the left mouse button.

On screens where the player is able to scroll (scores, instructions), the pointers `edge.exe+1F91B4, A4/AC/B4, 68/6C/70` for scores and `edge.exe+1F91B4, 84, 24/28/2C` for instructions show the maximal scroll position, current scroll position and target scroll position respectively. Smooth scrolling is achieved by setting the target scroll position and then smoothly changing the current scroll position until it matches the target.

## Other
TODO

# Unintended transitions
Here is a table detailing what happens when you manually change the `screen` value. All transitions not listed here work as expected.

| Special conditions                                                                       | From             | To                 | Effect                                                                                                                                                                                                                                                                                                                  |
|------------------------------------------------------------------------------------------|------------------|--------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Screen 3 has not been manually loaded yet                                                | Any              | 3                  | Shows the screen with "new game" and "instructions" buttons that can otherwise only be seen on a newly installed game.                                                                                                                                                                                                  |
|                                                                                          | Any except 17-22 | 0, 1               | Black screen                                                                                                                                                                                                                                                                                                            |
|                                                                                          | Any except 17    | 4-6, 8, 11-14      | Crash                                                                                                                                                                                                                                                                                                                   |
| No level loaded before                                                                   | Any except 17    | 16                 | Show blank loading screen and crash                                                                                                                                                                                                                                                                                     |
| Level loaded before                                                                      | Any except 17    | 16                 | Black screen                                                                                                                                                                                                                                                                                                            |
|                                                                                          | Any except 17-22 | 17                 | Black screen                                                                                                                                                                                                                                                                                                            |
| No level loaded before                                                                   | Any except 17-22 | 18                 | Crash                                                                                                                                                                                                                                                                                                                   |
| Level loaded before                                                                      | Any except 17-22 | 18                 | Show pause menu with black background. Selecting "resume", "last checkpoint" or "retry" will crash.                                                                                                                                                                                                                     |
| No level loaded before                                                                   | Any except 17-22 | 19                 | Show the clear screen appearing and crash                                                                                                                                                                                                                                                                               |
| Level loaded before                                                                      | Any except 17-22 | 19                 | Show a fully functional clear screen with black background.                                                                                                                                                                                                                                                             |
| All clear screen has not been reached properly yet                                       | Any except 17-22 | 20-22              | Show all clear screen with black background and no congratulations message. Clicking "next" won't show the credits but take you back to screen 2.                                                                                                                                                                       |
| All clear screen has been reached properly before, but credits have not been watched yet | Any except 17-22 | 20-22              | Show normal all clear screen and credits                                                                                                                                                                                                                                                                                |
| All clear screen has been reached properly and credits have been watched before          | Any except 17-22 | 20-22              | Show all clear screen with "GAME OVER"                                                                                                                                                                                                                                                                                  |
|                                                                                          | Any except 17    | 23                 | Black screen                                                                                                                                                                                                                                                                                                            |
|                                                                                          | Any except 17    | Any higher than 23 | Crash                                                                                                                                                                                                                                                                                                                   |
|                                                                                          | 17               | Any except 18-22   | Disable movement and unload the minimap.                                                                                                                                                                                                                                                                                |
|                                                                                          | 17               | 18, 20-22          | Disable movement and unload the minimap. Move the camera to the left but show no screen there.                                                                                                                                                                                                                          |
|                                                                                          | 17               | 19                 | Disable movement and unload the minimap. Make all prisms have their glow effect.                                                                                                                                                                                                                                        |
|                                                                                          | 18-22            | `x` (except 18-22) | Same as from Any except 17-22 to `x`, but show the skybox of the current level instead of a black background.                                                                                                                                                                                                           |
|                                                                                          | 18               | 20-22              | Same as from Any except 17-22 to 20-22, but show the current level instead of a black background.                                                                                                                                                                                                                       |
| Clear screen has not been reached properly                                               | 19               | 18                 | Show normal, fully functional pause menu                                                                                                                                                                                                                                                                                |   
| Clear screen has been reached properly                                                   | 19               | 18                 | Show pause menu. Selecting "resume" will make the clear screen reappear; Changing to 18 again will show a pause menu with no buttons. Selecting "last checkpoint" will return to last checkpoint and allow you to play normally, but continuously play the cube finishing animation. Everything else works as expected. |
| Clear screen has been reached properly                                                   | 19               | 20-22              | Crash                                                                                                                                                                                                                                                                                                                   |
| All clear screen has been reached properly                                               | 20-22            | 18, 19             | Show pause menu or clear screen. Selecting "resume", "last checkpoint", "retry" or "next" allows you to play the credits level.                                                                                                                                                                                         |


# Memory Pointers and Offsets

| Variable Name                        | Pointer and Offsets             | Comment                                                                                                                                                                          |
|--------------------------------------|---------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Menu screen                          | `edge.exe+1F9080, 50`           | See [Menu screens table](#Menu-screens) for values                                                                                                                               |
| Start screen selection               | `edge.exe+1F91B4, 54, 10`       | 0 if the "edge challenge" button is highlighted, 1 if "scores" etc.                                                                                                              |
| Level pack selection                 | `edge.exe+1F91B4, 5C, 10`       |                                                                                                                                                                                  |
| Level select back/go button          | `edge.exe+1F91B4, 64/6C/74, 10` | Normal/Bonus/Extended level select. Is set to 1 if "back" is pressed, 2 if "go" is pressed, -1 if either was pressed but the mouse was moved away, 0 when level select is loaded |
| Bonus level message back/join button | `edge.exe+1F91B4, 7C, 10`       |                                                                                                                                                                                  |
| Instructions back button             | `edge.exe+1F91B4, 84, 10`       |                                                                                                                                                                                  |
| Instructions edge time               | `edge.exe+1F91B4, 84, 34`       |                                                                                                                                                                                  |
| Options selection                    | `edge.exe+1F91B4, 8C, 10`       |                                                                                                                                                                                  |
| Scores selection                     | `edge.exe+1F91B4, 9C, 10`       |                                                                                                                                                                                  |
| Scores back button                   | `edge.exe+1F91B4, A4/AC/B4, 10` | Normal/Bonus/Extended scores screen                                                                                                                                              |
| Exit game selection                  | `edge.exe+1F91B4, BC, 10`       |                                                                                                                                                                                  |
| Pause menu selection                 | `edge.exe+1F91B4, D4, 10`       |                                                                                                                                                                                  |
| Pause options selection              | `edge.exe+1F91B4, D4, 50`       |                                                                                                                                                                                  |
| Pause main menu selection            | `edge.exe+1F91B4, D4, 54`       |                                                                                                                                                                                  |
| Clear screen selection               | `edge.exe+1F91B4, DC, 10`       |                                                                                                                                                                                  |
| All clear and credits selection      | `edge.exe+1F91B4, E4/EC/F4, 10` | Normal/Bonus/Extended credits screen                                                                                                                                             |
