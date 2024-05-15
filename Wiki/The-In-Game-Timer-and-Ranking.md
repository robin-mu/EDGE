# The In-Game Timer

In EDGE, there are only 22 possible values for milliseconds that the timer can show:

```python
.00, .04, .09, .13, .18, .22, .27, .31, .36, .40, .45, 
.50, .54, .59, .63, .68, .72, .77, .81, .86, .90, .95
```

These correspond to n/22 for every n from 0 to 21 rounded down to 2 decimals. 
The in-game timer cycles through these values, going to the next value every **tick**. 
**Ticks** are used for most timing-related variables in EDGE, and one tick corresponds to 1/30 of a second. However, since one in-game second is only 22 ticks long, the in-game timer effectively runs about 36% faster than real time.
As explained [here](https://twitter.com/Mobigame/status/1263226260618002432) by Mobigame, the reason for this timing mismatch is that the first version of the game, developed for J2ME mobile phones, ran at 22 FPS due to hardware limitations.

In memory, the `timer` variable stores the number of ticks since the level started. Timing starts after the loading screen fades out and ends before the clear screen appears. Pausing the game or minimizing the window stops the timer. Dying or selecting “last checkpoint” does not reset the timer to when the checkpoint was first reached, even when no checkpoint has been activated yet and dying sends you to the beginning of the level.

# EDGE Time

When you start to gain EDGE time, the `edging` variable is set from 0 to 1. The `current_edge_time` variable is set to 0 and is incremented every tick. This is the time that gets displayed next to the cube.

When you stop gaining EDGE time, the `edging` variable is set to 0. `current_edge_time` stops increasing and its value is added to the `total_edge_time` variable.

After finishing a level, `timer` is converted to minutes, seconds and milliseconds and displayed as “level time”, `total_edge_time` is displayed as “edge time”, and `timer - total_edge_time` is stored in `final_edge_time` and displayed underneath. This is the time used for determining your rank.

As can be seen in [this video](https://www.youtube.com/watch?v=LFC-D2SqThE), the timer next to the cube correctly displays the current EDGE Time only up to 999 seconds. However, `current_edge_time` stops increasing after reaching 1362.27 seconds, or 29970 ticks, which is equal to 999 real time seconds.

# Ranking and Records
After finishing a level, `final_edge_time` is compared with the `TimeThresholds` [times saved in the level file](https://github.com/robin-mu/EDGE/wiki/Ranking-Criteria) to determine your rank. Ranks S and S+ are only awarded if you also collected every prism in the level.

To show the "new record" text and update your time on the level select and scores screen, you have to either
1. collect the same number of prisms as you did in your current record and beat the level in a shorter time, or
2. collect more prisms than in your current record, regardless of your time.

The second condition shows that it is possible to update your record with a slower time by simply collecting more prisms than in your previous record. If you collect fewer prisms than in your current record, you can't get a new record, even when you beat the level with a faster time. <br/> The time displayed on the Steam leaderboards is your best time ignoring all prism-related conditions.

For speedrunners: This means that the time displayed on the level select screen is always your "EDGE Time 100%" PB while your time on the Steam leaderboards is your "EDGE Time Any%" PB.

All records are saved at `Steam/userdata/<Your Steam-ID>/38740/remote/savedata.ttsav`. The file can be decompressed with WEGFan's [PC Savefile Editor](https://github.com/WEGFan/Edge-PC-Savefile-Editor).

# Memory Pointers and Offsets

| Variable            | Type    | Pointer and Offsets    |
|---------------------|---------|------------------------|
| `timer`             | 4 Bytes | `edge.exe+1F9064, 10C` |
| `edging`            | Byte    | `edge.exe+1F9064, 6C`  |
| `current_edge_time` | 4 Bytes | `edge.exe+1F9064, 78`  |
| `total_edge_time`   | 4 Bytes | `edge.exe+1F9064, 108` |
| `final_edge_time`   | 4 Bytes | `edge.exe+1F9064, 110` |