# 手柄操作卡：先看驾驶站选中了谁

分析版本：`c600214842e1c2c4d3b75428453c4d8f3fb9f3e3`。下列是**代码写出的行为**，不是实车验收结果。换入口、改参数或换车后，要重新核对。

## Red / Blue / Practice Blue 的操作

主程序只使用 **gamepad1**，没有 `gamepad2` 分工。LT/RT 是扳机，按下数值严格大于 `0.1` 才生效；RB/LB 是肩键，不能混用。

| 操作 | 代码行为 |
|---|---|
| 左摇杆 | 前后、横移，通常按驾驶参考方向控制；Pinpoint 朝向不可用时退回车身方向控制 |
| 右摇杆 X | 普通驾驶时转向；`Red/Blue` 按 RT 时由自动瞄准接管；`Practice Blue` 按 RT 时仍可手动转向 |
| L3（按下左摇杆） | 把当前朝向设为驾驶参考前方，不是把场地坐标清零 |
| LT | 请求取球和输送；吸球功率还受球数、传感器和其他按键影响 |
| RT | `Red/Blue` 瞄准目标，按距离设射手转速与 Pitch，就绪后送球。`Practice Blue` 不自动转向，但仍需有效定位来计算距离 |
| RB | 处理卡球：吸球反转、输送反转、射手停止；RT 中也优先处理 RB |
| LB | 吸球反转，输送按 `0.4` 正向运行；与 RB 同按时按 RB 处理 |
| B | 软件停止底盘、射手、吸球、输送并取消送球；解除条件见下文 |
| A / X / Y、十字键、R3 | 主驾驶入口未绑定功能 |
| DS STOP | 结束当前 OpMode，执行结束清理；检查真实机构是否停止 |

依据：[摇杆](https://github.com/pengjinDaniel/FTC-16095-FatDragon-2027-Public/blob/c600214842e1c2c4d3b75428453c4d8f3fb9f3e3/TeamCode/src/main/java/org/firstinspires/ftc/teamcode/commands/DriveCommand.java#L20-L34)、[参考方向与失效时的行为](https://github.com/pengjinDaniel/FTC-16095-FatDragon-2027-Public/blob/c600214842e1c2c4d3b75428453c4d8f3fb9f3e3/TeamCode/src/main/java/org/firstinspires/ftc/teamcode/subsystems/drive/Drive.java#L151-L178)、[手柄绑定](https://github.com/pengjinDaniel/FTC-16095-FatDragon-2027-Public/blob/c600214842e1c2c4d3b75428453c4d8f3fb9f3e3/TeamCode/src/main/java/org/firstinspires/ftc/teamcode/opmodes/teleops/TeleOpBase.java#L59-L94)、[取球输入](https://github.com/pengjinDaniel/FTC-16095-FatDragon-2027-Public/blob/c600214842e1c2c4d3b75428453c4d8f3fb9f3e3/TeamCode/src/main/java/org/firstinspires/ftc/teamcode/commands/IntakeCommand.java#L39-L45)、[RT 中的输入](https://github.com/pengjinDaniel/FTC-16095-FatDragon-2027-Public/blob/c600214842e1c2c4d3b75428453c4d8f3fb9f3e3/TeamCode/src/main/java/org/firstinspires/ftc/teamcode/commands/ShootAssistCommand.java#L75-L105)、[射击与取消](https://github.com/pengjinDaniel/FTC-16095-FatDragon-2027-Public/blob/c600214842e1c2c4d3b75428453c4d8f3fb9f3e3/TeamCode/src/main/java/org/firstinspires/ftc/teamcode/commands/ShootAssistCommand.java#L136-L175)。

**START 后默认射手会按 `0.7` 功率预热。** 松开 RT、松开 RB 或解除 B 后，默认命令可能恢复预热；“退出这个动作”不等于“全部电机停机”。依据：[默认射手命令](https://github.com/pengjinDaniel/FTC-16095-FatDragon-2027-Public/blob/c600214842e1c2c4d3b75428453c4d8f3fb9f3e3/TeamCode/src/main/java/org/firstinspires/ftc/teamcode/opmodes/teleops/TeleOpBase.java#L73-L79)、[预热功率](https://github.com/pengjinDaniel/FTC-16095-FatDragon-2027-Public/blob/c600214842e1c2c4d3b75428453c4d8f3fb9f3e3/TeamCode/src/main/java/org/firstinspires/ftc/teamcode/subsystems/shooter/ShooterConstants.java#L16-L17)、[idle 实现](https://github.com/pengjinDaniel/FTC-16095-FatDragon-2027-Public/blob/c600214842e1c2c4d3b75428453c4d8f3fb9f3e3/TeamCode/src/main/java/org/firstinspires/ftc/teamcode/subsystems/shooter/Shooter.java#L164-L165)。

## 三组必须练清楚的组合

| 场景 | 代码目前怎么处理 | 上车必须确认 |
|---|---|---|
| RB + LT；随后只松 RB | RB 反转优先；松 RB 会清零软件球数，LT 仍保持则可能恢复取球 | 车内残留球、计数和后续进球是否一致 |
| RB + RT；随后只松 RB | 取消当前送球，射手停止、输送反转；松 RB 后 RT 仍按着，会重新进入射击准备 | 恢复时是否符合驾驶员预期；挡板、射手和输送顺序 |
| B 按下，再松 B | RT 仍按着：继续停止；RT 也松开且 B 已释放：下一循环解除停止 | 操作者是否理解解除条件，以及默认预热会恢复 |

依据：[松 RB 清零](https://github.com/pengjinDaniel/FTC-16095-FatDragon-2027-Public/blob/c600214842e1c2c4d3b75428453c4d8f3fb9f3e3/TeamCode/src/main/java/org/firstinspires/ftc/teamcode/subsystems/intake/Intake.java#L47-L64)、[RB 打断射击及恢复准备](https://github.com/pengjinDaniel/FTC-16095-FatDragon-2027-Public/blob/c600214842e1c2c4d3b75428453c4d8f3fb9f3e3/TeamCode/src/main/java/org/firstinspires/ftc/teamcode/commands/ShootAssistCommand.java#L136-L175)、[B 锁存和解除](https://github.com/pengjinDaniel/FTC-16095-FatDragon-2027-Public/blob/c600214842e1c2c4d3b75428453c4d8f3fb9f3e3/TeamCode/src/main/java/org/firstinspires/ftc/teamcode/opmodes/teleops/TeleOpBase.java#L98-L115)。需要结束整个程序时使用 DS STOP；B 是普通软件控制的一部分。

RT + LB 也要单独测试：代码会在射击更新后把输送功率改为 `0.4`，但这一步没有单独取消已打开的挡板。不要只看“LB 反转”就推断整条送球路径都反转。[RT + LB](https://github.com/pengjinDaniel/FTC-16095-FatDragon-2027-Public/blob/c600214842e1c2c4d3b75428453c4d8f3fb9f3e3/TeamCode/src/main/java/org/firstinspires/ftc/teamcode/commands/ShootAssistCommand.java#L92-L105)、[对应输送功率](https://github.com/pengjinDaniel/FTC-16095-FatDragon-2027-Public/blob/c600214842e1c2c4d3b75428453c4d8f3fb9f3e3/TeamCode/src/main/java/org/firstinspires/ftc/teamcode/subsystems/transit/Transit.java#L118-L120)。

## 记数、送球和丢目标：不要靠名称猜

- `cds` 在这里按**距离传感器**使用。球靠近到 ≤2.0 cm、离开到 ≥2.5 cm，形成一次进入/离开的判断；正向请求功率大于 0 才增加计数。代码没有在这里识别黄球或花蜜球颜色。[距离计数逻辑](https://github.com/pengjinDaniel/FTC-16095-FatDragon-2027-Public/blob/c600214842e1c2c4d3b75428453c4d8f3fb9f3e3/TeamCode/src/main/java/org/firstinspires/ftc/teamcode/subsystems/intake/Intake.java#L124-L144)。
- 软件计数达到 4 后，普通吸球会反转，即使 LT 已松开；RT 供球和 RB/LB 分支有更高优先级。程序计数不是车内球的直接测量。[功率优先级](https://github.com/pengjinDaniel/FTC-16095-FatDragon-2027-Public/blob/c600214842e1c2c4d3b75428453c4d8f3fb9f3e3/TeamCode/src/main/java/org/firstinspires/ftc/teamcode/subsystems/intake/Intake.java#L147-L160)。
- 松 RB 会清零软件球数；取消一个挡板已打开的射击流程也会清零。两者都没有逐个确认球是否已离开机器人。先做[RB 任务卡](../tasks/P2-RB-UNJAM.md)中的残球核对，再决定需不需要改策略。[RB 清零](https://github.com/pengjinDaniel/FTC-16095-FatDragon-2027-Public/blob/c600214842e1c2c4d3b75428453c4d8f3fb9f3e3/TeamCode/src/main/java/org/firstinspires/ftc/teamcode/subsystems/intake/Intake.java#L47-L64)、[取消射击清零](https://github.com/pengjinDaniel/FTC-16095-FatDragon-2027-Public/blob/c600214842e1c2c4d3b75428453c4d8f3fb9f3e3/TeamCode/src/main/java/org/firstinspires/ftc/teamcode/commands/ShootAssistCommand.java#L168-L175)。
- 挡板放行后，输送先反转 0.1 秒，再正向送球。进入这段流程后，单纯 `ready=false` 不会自动撤销；需要显式取消。松 RT、B、RB 或无效射击距离有相应取消路径。[送球状态机](https://github.com/pengjinDaniel/FTC-16095-FatDragon-2027-Public/blob/c600214842e1c2c4d3b75428453c4d8f3fb9f3e3/TeamCode/src/main/java/org/firstinspires/ftc/teamcode/subsystems/transit/Transit.java#L61-L98)、[命令结束](https://github.com/pengjinDaniel/FTC-16095-FatDragon-2027-Public/blob/c600214842e1c2c4d3b75428453c4d8f3fb9f3e3/TeamCode/src/main/java/org/firstinspires/ftc/teamcode/commands/ShootAssistCommand.java#L110-L117)、[取消条件](https://github.com/pengjinDaniel/FTC-16095-FatDragon-2027-Public/blob/c600214842e1c2c4d3b75428453c4d8f3fb9f3e3/TeamCode/src/main/java/org/firstinspires/ftc/teamcode/commands/ShootAssistCommand.java#L136-L175)。
- 相机暂时看不到标签，不一定等于“无有效射击距离”：程序可用已建立的定位和保留的 HIVE 几何继续计算。因此要分别测试短暂丢标签、定位无效、Pinpoint 异常，不能把它们当成一种情况。[保留几何与目标状态](https://github.com/pengjinDaniel/FTC-16095-FatDragon-2027-Public/blob/c600214842e1c2c4d3b75428453c4d8f3fb9f3e3/TeamCode/src/main/java/org/firstinspires/ftc/teamcode/subsystems/vision/Vision.java#L305-L313)、[定位有效性](https://github.com/pengjinDaniel/FTC-16095-FatDragon-2027-Public/blob/c600214842e1c2c4d3b75428453c4d8f3fb9f3e3/TeamCode/src/main/java/org/firstinspires/ftc/teamcode/subsystems/drive/Drive.java#L50-L70)。
- `Red/Blue` 的射击放行没有使用 `hasValidShootingTarget()` 的 HIGH 条件；不要宣称它会自动保证只向 HIGH 发射。是否添加这一条件属于比赛策略，需要先讨论。[HIGH 字段](https://github.com/pengjinDaniel/FTC-16095-FatDragon-2027-Public/blob/c600214842e1c2c4d3b75428453c4d8f3fb9f3e3/TeamCode/src/main/java/org/firstinspires/ftc/teamcode/subsystems/vision/Vision.java#L305-L312)、[实际放行条件](https://github.com/pengjinDaniel/FTC-16095-FatDragon-2027-Public/blob/c600214842e1c2c4d3b75428453c4d8f3fb9f3e3/TeamCode/src/main/java/org/firstinspires/ftc/teamcode/commands/ShootAssistCommand.java#L145-L163)。

## 调试入口的按钮不一样

| 入口 | 与主驾驶最容易混淆的地方 |
|---|---|
| `Shooter PID` | **RB 在 RT 松开时切换挡板；LB 处理卡球**。十字键上下调整目标转速，左右调整 Pitch；没有视觉瞄准要求 |
| `Shooter Test` | RT 仅测试距离射击设置；底盘每轮停止，不控制吸球和输送；松 RT 可恢复射手预热 |
| `Limelight Aim Test Red/Blue` | RT 测瞄准，左摇杆可移动；不创建射手 |
| `DashTuner` | 通过 Dashboard 操作，无主驾驶按键表；STOP 停电机，舵机不主动回到某个统一初值 |

依据：[Shooter PID 输入和输出](https://github.com/pengjinDaniel/FTC-16095-FatDragon-2027-Public/blob/c600214842e1c2c4d3b75428453c4d8f3fb9f3e3/TeamCode/src/main/java/org/firstinspires/ftc/teamcode/tests/ShooterPID.java#L76-L173)、[Shooter Test 循环](https://github.com/pengjinDaniel/FTC-16095-FatDragon-2027-Public/blob/c600214842e1c2c4d3b75428453c4d8f3fb9f3e3/TeamCode/src/main/java/org/firstinspires/ftc/teamcode/tests/ShooterTest.java#L49-L76)、[瞄准测试输入](https://github.com/pengjinDaniel/FTC-16095-FatDragon-2027-Public/blob/c600214842e1c2c4d3b75428453c4d8f3fb9f3e3/TeamCode/src/main/java/org/firstinspires/ftc/teamcode/tests/CoordinateAimTestBase.java#L69-L124)、[DashTuner START/STOP](https://github.com/pengjinDaniel/FTC-16095-FatDragon-2027-Public/blob/c600214842e1c2c4d3b75428453c4d8f3fb9f3e3/TeamCode/src/main/java/org/firstinspires/ftc/teamcode/tests/DashTuner.java#L71-L86)。

`toggleFlower()` 方法已经存在，但当前生产入口没有调用或按键绑定，不能当成“按某个键就能操作花朵”的功能。代码中的 Flower 机构具体做什么，也要先对照实物确认。[Flower 方法](https://github.com/pengjinDaniel/FTC-16095-FatDragon-2027-Public/blob/c600214842e1c2c4d3b75428453c4d8f3fb9f3e3/TeamCode/src/main/java/org/firstinspires/ftc/teamcode/subsystems/intake/Intake.java#L108-L118)。
