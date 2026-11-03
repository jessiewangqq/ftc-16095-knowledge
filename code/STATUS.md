# 目前程序到哪一步了

**结论：已有手动驾驶和射击相关实现；自动有路线和动作编排，但默认配置还不能运行路线；电脑检查未全通过；实车进展尚未取得足够记录。** 不能从公开代码直接推断孩子们的实车完成比例。

2026-11-03 复核的公开版本：`c600214842e1c2c4d3b75428453c4d8f3fb9f3e3`，仍与 2026-11-01 检查的版本相同。本页没有把旧测试当作本次重新执行的结果。

## 已经写进代码的能力

| 能力 | 代码目前有什么 | 还要怎样确认 |
|---|---|---|
| 主驾驶 | Red/Blue、场地参考驾驶、参考前方重设 | 方向、低速可控性、Pinpoint 异常时的驾驶变化 |
| 取球与输送 | LT、距离计数、满 4 反转、RB/LB 处理卡球 | 进球成功率、残球、误计/漏计、组合键恢复 |
| 辅助射击 | 视觉定位、自动转向、距离两点插值、射手速度反馈、送球状态机 | 红蓝定位、不同距离命中、丢目标与取消行为 |
| 停止与取消 | B 软件停止、松 RT 结束、DS STOP 清理路径 | 实际停止时间、挡板和舵机位置、恢复是否符合预期 |
| 自动路线 | 七段路径、两段沿路取球、三次射击动作 | 标定、起点、方向、超时策略和 30 秒内的真实完成情况 |
| 诊断工具 | 独立瞄准、射手和 Dashboard 入口；离线检查 | 操作卡一致、参数来源、第二位同学能否复测 |

以上实现位置见[架构](ARCHITECTURE.md)和[操作卡](CONTROLS.md)，不代表这些项目已在车上通过。

## 现在要优先处理的明确问题

| 项目 | 已核实事实 | 下一步要拿到什么 |
|---|---|---|
| 自动入口配置 | `foresightConfig=null`，入口会提示并退出 | 对应这台车的标定导出、配置提交；先分段再整段测 |
| 自动等待时间 | `shootFor` 等距离/ready/HIGH 没有截止时间；900 ms 从 FEEDING 才计时。路径也没有外层阶段截止时间 | 明确最多等多久、失败后停下还是跳过、怎样留时间完成末段；补用例 |
| 自动起始朝向 | 初始 pose 是 90°，第一段起点是 270° | 实际摆车和坐标说明，验证后决定是否修改；不凭差值直接改 |
| 红蓝自动 | 当前自动只创建红方 Vision，固定红方目标 | 确认本次参赛需要哪些起点/联盟；需要蓝方时另做路线与验证 |
| 球数的含义 | 松 RB 清零；取消已开挡板的射击也可能清零，未直接确认车内排空 | 残球试验；明确软件计数如何与真实控球对应，再决定改法 |
| 定点保持 | 控制器存在，但 `positionHoldCalibrated=false` | 若策略确实需要，标定并测试；不能仅把开关改成 true 就算完成 |
| Flower 操作 | 方法存在，生产入口未绑定；具体实物用途未确认 | 先讲清机构用途、按键和动作预期，再决定是否接入 |
| 射击诊断 | Red/Blue 的遥测在定位诊断后提前返回，没有显示后面已有的射手转速/放行诊断 | 若现场难定位问题，先补只读遥测，保留原控制行为 |

源码：[空配置](https://github.com/pengjinDaniel/FTC-16095-FatDragon-2027-Public/blob/c600214842e1c2c4d3b75428453c4d8f3fb9f3e3/TeamCode/src/main/java/org/firstinspires/ftc/teamcode/pedro/Constants.java#L47-L64)、[自动门槛与联盟](https://github.com/pengjinDaniel/FTC-16095-FatDragon-2027-Public/blob/c600214842e1c2c4d3b75428453c4d8f3fb9f3e3/TeamCode/src/main/java/org/firstinspires/ftc/teamcode/opmodes/autos/Test.java#L77-L95)、[路径等待](https://github.com/pengjinDaniel/FTC-16095-FatDragon-2027-Public/blob/c600214842e1c2c4d3b75428453c4d8f3fb9f3e3/TeamCode/src/main/java/org/firstinspires/ftc/teamcode/opmodes/autos/Test.java#L146-L159)、[射击等待与结束](https://github.com/pengjinDaniel/FTC-16095-FatDragon-2027-Public/blob/c600214842e1c2c4d3b75428453c4d8f3fb9f3e3/TeamCode/src/main/java/org/firstinspires/ftc/teamcode/opmodes/autos/Test.java#L185-L237)、[起始角度](https://github.com/pengjinDaniel/FTC-16095-FatDragon-2027-Public/blob/c600214842e1c2c4d3b75428453c4d8f3fb9f3e3/TeamCode/src/main/java/org/firstinspires/ftc/teamcode/opmodes/autos/Test.java#L42-L44)、[RB 清零](https://github.com/pengjinDaniel/FTC-16095-FatDragon-2027-Public/blob/c600214842e1c2c4d3b75428453c4d8f3fb9f3e3/TeamCode/src/main/java/org/firstinspires/ftc/teamcode/subsystems/intake/Intake.java#L47-L64)、[射击取消清零](https://github.com/pengjinDaniel/FTC-16095-FatDragon-2027-Public/blob/c600214842e1c2c4d3b75428453c4d8f3fb9f3e3/TeamCode/src/main/java/org/firstinspires/ftc/teamcode/commands/ShootAssistCommand.java#L168-L175)、[保持配置](https://github.com/pengjinDaniel/FTC-16095-FatDragon-2027-Public/blob/c600214842e1c2c4d3b75428453c4d8f3fb9f3e3/TeamCode/src/main/java/org/firstinspires/ftc/teamcode/subsystems/drive/DriveConstants.java#L31-L39)、[保持启用判断](https://github.com/pengjinDaniel/FTC-16095-FatDragon-2027-Public/blob/c600214842e1c2c4d3b75428453c4d8f3fb9f3e3/TeamCode/src/main/java/org/firstinspires/ftc/teamcode/subsystems/drive/PositionHoldController.java#L124-L140)、[Flower 方法](https://github.com/pengjinDaniel/FTC-16095-FatDragon-2027-Public/blob/c600214842e1c2c4d3b75428453c4d8f3fb9f3e3/TeamCode/src/main/java/org/firstinspires/ftc/teamcode/subsystems/intake/Intake.java#L108-L118)、[遥测提前返回](https://github.com/pengjinDaniel/FTC-16095-FatDragon-2027-Public/blob/c600214842e1c2c4d3b75428453c4d8f3fb9f3e3/TeamCode/src/main/java/org/firstinspires/ftc/teamcode/opmodes/teleops/TeleOpBase.java#L165-L219)。

这些事实不都等于“代码有 bug”。例如是否只在 HIGH 发射、丢标签后能否继续、退出 RB 后是否恢复预热，先由比赛策略和驾驶需求确定预期，再判断实现是否正确。详见[操作卡中的边界](CONTROLS.md)。

## 电脑检查：已有历史结果，不是实车结果

以下来自 2026-11-01 原始记录，本次复核并脱敏整理，**2026-11-03 没有重跑**：

| 检查 | 历史结果 |
|---|---|
| `:TeamCode:assembleDebug` | 退出码 0，生成 APK；有编译/打包警告 |
| 活动 Java 检查 | 9 项中 8 项通过；`RtCalibrationCheck` 失败 |
| Python 上传工具测试 | 17 项中 16 项通过；`test_check_mode_never_calls_adb` 报错 |
| 7 个整文件注释的旧 Java 检查 | 未执行，不能计为通过 |
| 设备安装、实车试验、整场模拟 | 本组记录没有这些证据；待向现场队员核实 |

[历史证据目录](evidence/2026-11-01/README.md)保存逐项结果和脱敏失败日志。

### RT 校准检查失败，应先对齐测试要求

测试用 100→102→104 cm 的样本，期望三帧不被接受；生产位置容差却是 30 cm，4 cm 没跨过这个阈值。源码确实按第一帧锚点并补偿里程计运动进行比较，所以现有证据不支持“只比较相邻两帧”的旧推断。先问清 30 cm/30°/10° 的依据，再修测试样本或正式参数；不要为让测试变绿，直接把诊断试验中的更窄阈值当作实车参数。[失败用例](https://github.com/pengjinDaniel/FTC-16095-FatDragon-2027-Public/blob/c600214842e1c2c4d3b75428453c4d8f3fb9f3e3/local-tests/RtCalibrationCheck.java#L187-L203)、[生产容差](https://github.com/pengjinDaniel/FTC-16095-FatDragon-2027-Public/blob/c600214842e1c2c4d3b75428453c4d8f3fb9f3e3/TeamCode/src/main/java/org/firstinspires/ftc/teamcode/subsystems/vision/VisionConstants.java#L9-L13)、[实际窗口比较](https://github.com/pengjinDaniel/FTC-16095-FatDragon-2027-Public/blob/c600214842e1c2c4d3b75428453c4d8f3fb9f3e3/TeamCode/src/main/java/org/firstinspires/ftc/teamcode/subsystems/vision/Vision.java#L394-L429)。

### 上传脚本测试失败，不能直接等同于传输坏了

上传器先检查本机 ADB 与 APK 是否存在；测试只模拟了 ADB 调用，没有隔离这两个文件条件。历史构建后 APK 已存在，但 ADB 写死的路径不符合那台电脑，仍报错。可以拆成“ADB 路径可配置”和“测试隔离本机文件”两个小任务，再重跑；目前仍记为失败。[硬编码路径](https://github.com/pengjinDaniel/FTC-16095-FatDragon-2027-Public/blob/c600214842e1c2c4d3b75428453c4d8f3fb9f3e3/upload-offline.py#L16-L19)、[检查顺序](https://github.com/pengjinDaniel/FTC-16095-FatDragon-2027-Public/blob/c600214842e1c2c4d3b75428453c4d8f3fb9f3e3/upload-offline.py#L238-L251)、[测试夹具](https://github.com/pengjinDaniel/FTC-16095-FatDragon-2027-Public/blob/c600214842e1c2c4d3b75428453c4d8f3fb9f3e3/local-tests/test_upload_offline.py#L172-L177)。

## 到现场先补六项信息

1. 这台车装的代码 SHA、所选 OpMode、安装包和参数是什么；是否有未提交的改动。
2. 队员演示一轮取球→瞄准→射击，并说清哪些动作稳定、哪些偶发失败。
3. 演示 RB+LT、RB+RT、B 解除和 DS STOP，核对残球和软件计数。
4. 让队员展示自动标定、分段测试和整段计时记录；如果只有本地未公开代码，先保留并比较版本。
5. 核对 [硬件表](../hardware/CONFIGURATION.md)：设备名、接线、机构方向、Pinpoint、Limelight 配置。
6. 换一位同学照着操作卡重复一次，并把不清楚的地方写进任务，而不是只说“还需要练”。

结果进入[任务看板](../plan/BOARD.md)与[测试记录](../tests/TEMPLATE.md)。负责人、实车结果、通过日期都由真实认领和实际测试补全；合并条件按[验收门槛](../tests/MERGE-GATE.md)。
