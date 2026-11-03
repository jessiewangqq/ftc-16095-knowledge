# 调参以后，怎样让下一位同学也能复现

适用代码：`c600214842e1c2c4d3b75428453c4d8f3fb9f3e3`。本页给记录和核对顺序，不替代具体机构的现场操作指导；没有填写任何实车通过结论。

## 开始前，把比较条件固定下来

先填机器人、代码 SHA、硬件配置版本、电池状态、场地摆放、传感器配置，以及这次只改哪组参数。参数至少带上数值、单位、文件位置和预期效果；保留改前的值。一次改变几组无关参数，失败后很难判断原因。

## 根据当前代码，按依赖顺序确认

| 顺序 | 要确认什么 | 留什么记录 |
|---|---|---|
| 1. 接线和机械 | 配置名与端口、方向、行程、停止方式 | [硬件表](CONFIGURATION.md)及脱敏照片 |
| 2. Pinpoint | READY、轮型、偏移、直线/横移/旋转与读数一致 | 已知距离/角度和程序读数的对照 |
| 3. Limelight | pipeline/fmap/外参、红蓝目标、场地坐标 | 配置版本、位置对照、短暂丢标签和重新定位的记录 |
| 4. 射手与输送 | 实际速度、Pitch、挡板、距离点、进球和取消 | 每次球数、距离、电池、结果；不能只抄“看起来挺准”的参数 |
| 5. 自动路径 | 路径跟踪配置、起点、方向、各段时间、失败处理 | 先分段再整段，记录能否在阶段时间内完成 |

这份代码提供 Pedro AutoTune 入口。仓库说明的顺序是 Mecanum Tuner → Pinpoint Tuner → 替换对应完整导出并重建 → Foresight Tuner → 替换 `foresightConfig` 并重建 → Localization/Line/Curve/Hold 等测试。调参过程会让机器人运动，由现场人员按工具提示操作；不要通过删除空配置检查来绕过标定。[本版 Pedro 配置说明](https://github.com/pengjinDaniel/FTC-16095-FatDragon-2027-Public/blob/c600214842e1c2c4d3b75428453c4d8f3fb9f3e3/TeamCode/src/main/java/org/firstinspires/ftc/teamcode/pedro/README.md#L5-L19)。

## Dashboard 上改完，不等于已经保存进仓库

确认哪些值每轮读取，哪些只在初始化时读取。参数页面显示新数值，不代表当前创建好的对象都已经采用它；例如射手 PID 在周期中刷新，但电机方向是在构造时设置。[初始化读取](https://github.com/pengjinDaniel/FTC-16095-FatDragon-2027-Public/blob/c600214842e1c2c4d3b75428453c4d8f3fb9f3e3/TeamCode/src/main/java/org/firstinspires/ftc/teamcode/subsystems/shooter/Shooter.java#L33-L54)、[周期刷新 PID](https://github.com/pengjinDaniel/FTC-16095-FatDragon-2027-Public/blob/c600214842e1c2c4d3b75428453c4d8f3fb9f3e3/TeamCode/src/main/java/org/firstinspires/ftc/teamcode/subsystems/shooter/Shooter.java#L241-L251)。

验证有效后，把最终值写回对应的 Constants 文件，检查差异并提交，再用新 SHA 构建、装车和复测。保存代码参数与硬件配置的对应关系；测试记录不能只写“用了 Dashboard 最新参数”。

注意 `DashTuner` 的 SDK 编码器控制与生产 `Shooter` 的 Java PIDF 不是同一个控制器，不能因为参数都叫 P/I/D/F 就直接互抄。生产代码使用 `RUN_WITHOUT_ENCODER`、读取 `getVelocity()` 后计算电机功率。[生产射手初始化](https://github.com/pengjinDaniel/FTC-16095-FatDragon-2027-Public/blob/c600214842e1c2c4d3b75428453c4d8f3fb9f3e3/TeamCode/src/main/java/org/firstinspires/ftc/teamcode/subsystems/shooter/Shooter.java#L38-L54)、[生产射手计算输出](https://github.com/pengjinDaniel/FTC-16095-FatDragon-2027-Public/blob/c600214842e1c2c4d3b75428453c4d8f3fb9f3e3/TeamCode/src/main/java/org/firstinspires/ftc/teamcode/subsystems/shooter/Shooter.java#L254-L269)。

## 一条校准记录至少包含

- 改前值 → 改后值，单位、改动原因、对应代码和配置版本。
- 同样步骤下的逐次结果，以及失败或异常时发生了什么。
- 是否保留这组值；谁独立复测；还缺什么测试。
- 如果效果变差，退回哪个已验证版本；硬件变更后旧值是否仍适用。

目前所有实车校准结果均待队员提供。训练中的调参服务、电脑连接和数据流在正式比赛能否使用，请按[规则资料](../rules/README.md)核对。
