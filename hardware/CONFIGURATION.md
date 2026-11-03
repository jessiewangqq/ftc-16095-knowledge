# 硬件配置：把代码名和实物对上

代码版本：`c600214842e1c2c4d3b75428453c4d8f3fb9f3e3`；核对日期：2026-11-03。**下表“代码要求”已从源码确认；实物型号、端口、方向效果和标定结果仍待现场填写。** 参数写在代码里，不能代替实测。

机器人标识 / 硬件负责人 / 程序负责人 / 复核者：待填写。配置导出版本 / 日期：待填写。

## 设备名称必须完全一致

主程序通过 `hardwareMap.get` 按名称取设备，没有自动寻找别名。名称和类型不匹配会影响初始化；表中的名称区分大小写。

| 机构 | RC 配置名 | 代码类型及要求 | 实物型号、Hub 端口、方向验证 |
|---|---|---|---|
| 左前 / 左后底盘 | `leftFrontMotor` / `leftBackMotor` | DcMotorEx，REVERSE，零功率 BRAKE | 待确认 |
| 右前 / 右后底盘 | `rightFrontMotor` / `rightBackMotor` | DcMotorEx，FORWARD，零功率 BRAKE | 待确认 |
| 定位模块 | `pinpoint` | GoBildaPinpointDriver；4-Bar 定位轮配置；X/Y 偏移 −96/−74 mm；两个编码器方向 FORWARD | 型号、固件、轮型、实际偏移、方向待确认 |
| 吸球 | `intakeMotor` | DcMotor，FORWARD，RUN_WITHOUT_ENCODER | 待确认 |
| 球检测 | `cds` | DistanceSensor，以 cm 读取；名字里有 color，但当前按距离使用 | 实际器件型号、安装位置待确认 |
| 两侧 Flower 机构 | `leftFlowerServo` / `rightFlowerServo` | Servo；具体机械用途先对照实物解释 | 用途、端口、行程待确认 |
| 输送 | `transitMotor` | DcMotor，REVERSE，RUN_WITHOUT_ENCODER | 待确认 |
| 挡板 | `limitServo` | Servo | 待确认 |
| 左 / 右射手 | `leftShooterMotor` / `rightShooterMotor` | DcMotorEx；左 REVERSE、右 FORWARD；RUN_WITHOUT_ENCODER；读取速度后由 Java PIDF 算功率 | 电机/编码器/飞轮型号、方向待确认 |
| 射手 Pitch | `pitchServo` | Servo，位置范围由代码限制 | 连杆、实际角度、机械限制待确认 |
| 视觉 | `limelight` | Limelight3A；蓝 pipeline 0、红 pipeline 1；50 Hz | 固件、两套 pipeline/fmap、相机安装外参待确认 |

源码：[底盘与 Pinpoint](https://github.com/pengjinDaniel/FTC-16095-FatDragon-2027-Public/blob/c600214842e1c2c4d3b75428453c4d8f3fb9f3e3/TeamCode/src/main/java/org/firstinspires/ftc/teamcode/subsystems/drive/Drive.java#L27-L47)、[名称与方向](https://github.com/pengjinDaniel/FTC-16095-FatDragon-2027-Public/blob/c600214842e1c2c4d3b75428453c4d8f3fb9f3e3/TeamCode/src/main/java/org/firstinspires/ftc/teamcode/subsystems/drive/DriveConstants.java#L9-L27)、[吸球、传感器、Flower](https://github.com/pengjinDaniel/FTC-16095-FatDragon-2027-Public/blob/c600214842e1c2c4d3b75428453c4d8f3fb9f3e3/TeamCode/src/main/java/org/firstinspires/ftc/teamcode/subsystems/intake/Intake.java#L32-L40)、[输送与挡板](https://github.com/pengjinDaniel/FTC-16095-FatDragon-2027-Public/blob/c600214842e1c2c4d3b75428453c4d8f3fb9f3e3/TeamCode/src/main/java/org/firstinspires/ftc/teamcode/subsystems/transit/Transit.java#L31-L38)、[射手与 Pitch](https://github.com/pengjinDaniel/FTC-16095-FatDragon-2027-Public/blob/c600214842e1c2c4d3b75428453c4d8f3fb9f3e3/TeamCode/src/main/java/org/firstinspires/ftc/teamcode/subsystems/shooter/Shooter.java#L33-L58)、[Limelight](https://github.com/pengjinDaniel/FTC-16095-FatDragon-2027-Public/blob/c600214842e1c2c4d3b75428453c4d8f3fb9f3e3/TeamCode/src/main/java/org/firstinspires/ftc/teamcode/subsystems/vision/Vision.java#L82-L89)。

`teamwebcamcalibrations.xml` 不是 Control Hub 的接线配置，也不能证明 Limelight 参数已经正确。现场需要保存脱敏的 RC 配置导出、端口表与机构照片；不上传 Wi-Fi 密码、密钥、私人设备标识。

## 当前代码参数：用于核对，不是让新手直接照着试

| 项目 | 当前值 | 需要验证什么 |
|---|---|---|
| 吸球正常 / RT 供球 / 反转 | 1.0 / 0.6 / −1.0 | 方向、球路、允许连续运行时长 |
| 普通输送 / LB 配合 / 射击送球 / RB 反转 | 0.6 / 0.4 / 0.65 / −0.7 | 各模式下的真实流向与卡球情况 |
| 射击前反转 | −0.4，0.1 秒 | 挡板打开后的顺序和是否按预期送球 |
| 球检测阈值 | 进入 ≤2.0 cm；离开 ≥2.5 cm；软件上限 4 | 球在传感器附近停留、连续进球、残球和误计数 |
| Flower 抬起 / 展开 | 左右均 0.5 / 0.2 | 具体用途、机械行程；生产入口尚未绑定展开操作 |
| 挡板关闭 / 打开 | 0.4 / 0.7 | 闭合是否挡住球、打开是否干涉 |
| Pitch 初值 / 代码范围 | 0.5 / 0–0.55 | 0–1 是舵机位置，不是角度；实际安全范围需实测 |
| 射手默认预热 | 功率 0.7 | START、退出 RT、退出 RB、解除 B 后的预热行为 |
| 射手速度就绪 | 左右速度误差容差 6%，稳定 0.05 秒 | 实际速度波动、送球扰动和电池变化 |
| Pitch 等待 | 改变量超过 0.005 后等 0.2 秒 | 实物到位时间是否足够 |

依据：[吸球与 Flower 参数](https://github.com/pengjinDaniel/FTC-16095-FatDragon-2027-Public/blob/c600214842e1c2c4d3b75428453c4d8f3fb9f3e3/TeamCode/src/main/java/org/firstinspires/ftc/teamcode/subsystems/intake/IntakeConstants.java#L8-L26)、[输送与挡板参数](https://github.com/pengjinDaniel/FTC-16095-FatDragon-2027-Public/blob/c600214842e1c2c4d3b75428453c4d8f3fb9f3e3/TeamCode/src/main/java/org/firstinspires/ftc/teamcode/subsystems/transit/TransitConstants.java#L8-L19)、[射手、Pitch 和就绪参数](https://github.com/pengjinDaniel/FTC-16095-FatDragon-2027-Public/blob/c600214842e1c2c4d3b75428453c4d8f3fb9f3e3/TeamCode/src/main/java/org/firstinspires/ftc/teamcode/subsystems/shooter/ShooterConstants.java#L16-L47)。

**INIT 已可能移动舵机**：Flower 抬起、挡板关闭、Pitch 到初值。开始试车前确认机构周围和行程；代码方向的 FORWARD/REVERSE 不等于已经验证实物一定“向前”或“向后”。

## 距离、速度和坐标别混单位

| 内容 | 本版约定 |
|---|---|
| Pinpoint 安装偏移 | mm |
| Pedro 路径位置 | 英寸，0–144 的场地坐标；传给 HIVE 坐标时 X、Y 各减 72 |
| 视觉/HIVE 场地坐标 | 中心为 0/0，位置英寸；+X 朝观众 |
| 射击表中的距离 | **车中心到当前 CELL 四个 Tag 中心的水平距离**，cm；不是相机斜距或到开口的距离 |
| 射手速度 | 编码器 ticks/s，不是 RPM |
| Pitch、挡板、Flower | 0–1 舵机位置，不是角度 |
| 射手朝向 | 相对车头 yaw=180°，核对车头和射击方向时别当成同一方向 |

依据：[路径定位单位](https://github.com/pengjinDaniel/FTC-16095-FatDragon-2027-Public/blob/c600214842e1c2c4d3b75428453c4d8f3fb9f3e3/TeamCode/src/main/java/org/firstinspires/ftc/teamcode/pedro/Constants.java#L36-L44)、[坐标平移](https://github.com/pengjinDaniel/FTC-16095-FatDragon-2027-Public/blob/c600214842e1c2c4d3b75428453c4d8f3fb9f3e3/TeamCode/src/main/java/org/firstinspires/ftc/teamcode/subsystems/vision/AutoHiveTarget.java#L86-L89)、[场地与射手方向](https://github.com/pengjinDaniel/FTC-16095-FatDragon-2027-Public/blob/c600214842e1c2c4d3b75428453c4d8f3fb9f3e3/TeamCode/src/main/java/org/firstinspires/ftc/teamcode/subsystems/vision/VisionConstants.java#L18-L39)、[射击距离与速度定义](https://github.com/pengjinDaniel/FTC-16095-FatDragon-2027-Public/blob/c600214842e1c2c4d3b75428453c4d8f3fb9f3e3/TeamCode/src/main/java/org/firstinspires/ftc/teamcode/subsystems/shooter/ShooterConstants.java#L26-L33)。

当前两点射击表为：

| 标定点 | 距离 cm | 速度 ticks/s | Pitch |
|---|---:|---:|---:|
| center | 62.1 | 1650 | 0.54 |
| wall | 139.0 | 1840 | 0.22 |

两点之间线性插值，范围外夹到端点，不向外推算。代码只检查参数是否合法，不证明命中率。[插值和数值检查](https://github.com/pengjinDaniel/FTC-16095-FatDragon-2027-Public/blob/c600214842e1c2c4d3b75428453c4d8f3fb9f3e3/TeamCode/src/main/java/org/firstinspires/ftc/teamcode/subsystems/shooter/Shooter.java#L87-L125)。

## 现场需要补齐的记录

- RC/DS 软件版本、机器人配置版本、实际 APK 与代码 SHA。
- 电池状态、线号与端口、机构固定、方向、机械行程；能够使用的测试球和场地条件。
- Pinpoint READY 状态、直线/横移/旋转对照记录，以及实际安装偏移。
- Limelight 固件、pipeline、fmap、相机外参的版本和来源。
- 射手两点及中间距离的逐次结果，别只记平均命中率。
- 安全停止、取消和恢复的实测结果，尤其残球与软件计数的对应。

`flowerPositionsCalibrated=true`、`limitPositionsCalibrated=true`、`velocityControlCalibrated=true` 都是代码中的人工设置，不是机器人自动验证后的证明。改硬件后要重新核对旧参数和回退包是否适配。标定流程见[校准记录办法](CALIBRATION.md)，每次试验使用[测试模板](../tests/TEMPLATE.md)。
