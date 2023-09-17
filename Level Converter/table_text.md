| Name | Block | Timing | Visibility | Radius | Extra | Additional data | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| **Item** |  / | 1. **Iron Nugget** (1 tick) and **Iron Ingot** (1 second)<br/>2. **Gold Nugget** (1 tick) and **Gold Ingot** (1 second) | `False` = **Glass**<br/>`Null` = **White Stained Glass** | `x` = **Prismarine Shard**<br/>`y` = **Stick** | Various | **Book** with one `key=value` pair per line. Parameters in the book overwrite items in the container. |  |
| MovingPlatform | **White Shulker Box** | 1. `TravelTime` (of first waypoint) <br/>2. `PauseTime` (of first waypoint) | - | - | `WaypointItem`: Arbitrary item (Amount = `LoopStartIndex`)<br/>`FullBlock` = False: **Quartz Slab**<br/>`AutoStart = False`: **Red Wool** | `ID`, `RelatedTo`, `Offset` | Block position defines position of first waypoint |
| Waypoint | **Chest** | 1. `TravelTime`<br/>2. `PauseTime` | - | - | - | - |  |
| FallingPlatform | **Dropper** | 1. `FloatTime` | - | - | - | - |  |
| Bumper | **Barrel** | 1. `StartDelay`<br/>2. `PulseRate` | - | - | `Enabled = False`: **Red Wool** | `ID` | Bumper orientation = Barrel orientation |
| Button | **Light Gray Shulker Box** | - | `True` (default), `False`, `Null` | - | `DisableCount`: Amount of **Stone Button** | `ID`, `Mode`, `TriggerAchievements`, `AffectMovingPlatforms`, `AffectButtons`, `AffectBumpers` | Will be attached to a moving platform underneath it if it has an `ID` |
| ResizerGrow | **Red Shulker Box** | - | `True` (default), `False` | `[x],[y]` | - | - |  |
| ResizerShrink | **Green Shulker Box** | - | `True` (default), `False` | `[x],[y]` | - | - |  |
| OtherCube | **Orange Shulker Box** | - | - | `[x],[y]` | - | `PositionCube`, `MovingBlockSync`, `KeyEvents` | Shulker Box position denotes `PositionTrigger`<br/>Relative coordinates (~) can be used for `PositionCube` |
| DarkCube | **Black Shulker Box** | - | - | `[x],[y]` | - | `PositionCube`, `MovingBlockSync`, `KeyEvents` | Shulker Box position denotes `PositionTrigger`<br/>Relative coordinates (~) can be used for `PositionCube` |
| Checkpoint | **Blue Shulker Box** | - | - | `[x],[y]` | `RespawnZ`: **Arrow** (Amount = height above checkpoint) | - |  |
| CameraTrigger | **Pink Shulker Box** | 1. `StartDelay`<br/>2. `Duration` | - | - | - | `Zoom`, `Angle`, `FieldOfView`, `SingleUse` |  |
| ButtonSequence | **Lectern** | - | - | - | - | `ButtonIDs`, `SequenceInOrder`, `TriggerAchievements`, `AffectMovingPlatforms`, `AffectButtons`, `AffectBumpers` | Can be placed anywhere in the structure |
| Prism | **Prismarine** | - | - | - | - | - |  |