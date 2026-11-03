# 从代码到机器人：构建、安装和核对

分析版本：`c600214842e1c2c4d3b75428453c4d8f3fb9f3e3`。**提交到 GitHub、合并到主干、生成 APK、安装到车上，是四件不同的事。** 本页是队员操作步骤，不代表本次已安装或试车。

## 先把电脑环境对齐

| 项目 | 本版工程声明 |
|---|---|
| FTC SDK | 12.0.0 |
| FTCLib | 2.1.1 |
| Pedro | revhub 3.0.2 / tuning 1.0.1 |
| Dashboard | 0.6.0，使用仓库内 `local-maven` 制品 |
| Android Gradle Plugin / Gradle | 8.13.2 / wrapper 9.1.0 |
| Android | compileSdk 30、minSdk 24、targetSdk 28 |
| Java 源码级别 | Java 8；这不等于用 JDK 8 启动构建工具 |
| 安装应用 | `com.qualcomm.ftcrobotcontroller`，Robot Controller 应用 |

依据：[SDK 与 Dashboard](https://github.com/pengjinDaniel/FTC-16095-FatDragon-2027-Public/blob/c600214842e1c2c4d3b75428453c4d8f3fb9f3e3/build.dependencies.gradle#L8-L17)、[队伍依赖及本地制品](https://github.com/pengjinDaniel/FTC-16095-FatDragon-2027-Public/blob/c600214842e1c2c4d3b75428453c4d8f3fb9f3e3/TeamCode/build.gradle#L16-L37)、[构建插件](https://github.com/pengjinDaniel/FTC-16095-FatDragon-2027-Public/blob/c600214842e1c2c4d3b75428453c4d8f3fb9f3e3/build.gradle#L9-L11)、[Gradle wrapper](https://github.com/pengjinDaniel/FTC-16095-FatDragon-2027-Public/blob/c600214842e1c2c4d3b75428453c4d8f3fb9f3e3/gradle/wrapper/gradle-wrapper.properties#L1-L7)、[Android 与应用 ID](https://github.com/pengjinDaniel/FTC-16095-FatDragon-2027-Public/blob/c600214842e1c2c4d3b75428453c4d8f3fb9f3e3/build.common.gradle#L36-L40)、[Java 源级别与 NDK 声明](https://github.com/pengjinDaniel/FTC-16095-FatDragon-2027-Public/blob/c600214842e1c2c4d3b75428453c4d8f3fb9f3e3/build.common.gradle#L73-L81)。

使用 Android Studio 打开**代码仓库根目录**，确认 Gradle JDK 和 Android SDK 的配置；同步项目。电脑的 SDK 路径各不相同，不要把别人的个人路径抄进共享文件。新电脑需要下载依赖；已有缓存的电脑能离线构建，不代表新电脑也能离线完成准备。

2026-11-01 的构建记录使用 macOS、Android Studio 的 JBR 25.0.3 和 Gradle 9.1.0。它是一次实际环境记录，不是对所有电脑的版本要求；不为统一版本号而在赛前随意升级依赖。见[历史证据](evidence/2026-11-01/README.md)。

## 生成一份能追溯的安装包

在代码仓库根目录检查：

```sh
git status --short
git branch --show-current
git rev-parse HEAD
```

正式验收应先提交改动，确认工作区没有未提交修改，再构建。否则即使记录了 SHA，生成的安装包仍可能包含记录之外的变化。探索时可以边改边试，但修改后要重新做正式验收。

macOS / Linux 的构建命令：

```sh
./gradlew --no-daemon --console=plain :TeamCode:assembleDebug
```

Windows 使用仓库中的 `gradlew.bat` 执行同一任务。预期产物是 `TeamCode/build/outputs/apk/debug/TeamCode-debug.apk`。保存完整日志、退出码、代码 SHA、构建环境，以及**实际 APK 的 SHA-256**；同一源码重新构建也应重新记录包的校验值。

如果失败，保留错误位置，先判断是依赖下载、SDK/JDK 环境还是源代码编译问题。不要删改代码只为绕过错误，也不要用上一次留下的 APK 冒充刚生成的版本。

## “构建成功”之后还要检查什么

仓库的 `local-tests` 有独立 Java `main` 检查和 Python 测试；它们不是都自动接入了 `assembleDebug`，也不能只运行一个 Gradle `test` 就声称全部通过。

- Java 检查需要已编译的 TeamCode 类及真实 SDK、FTCLib、Pedro 依赖。运行时记录每个类的结果，不能把已注释的 7 个旧文件算作通过。
- Python 上传工具测试可在仓库根目录运行 `python3 local-tests/test_upload_offline.py`；它使用 mock/fake process，不代表真实 ADB 安装已验证。当前有已知环境依赖，详见[状态清单](STATUS.md)。
- 2026-11-01 的结果是：构建成功，Java 8/9 通过，Python 16/17 通过。**尚未全绿，也没有实车通过记录。** 原始失败要保留，新结果另存。

本次知识库整理没有重跑上述命令。完整历史摘要与脱敏日志见[电脑检查证据](evidence/2026-11-01/README.md)。

## 由现场队员安装并核对

1. 确认是哪台机器人、哪个已提交版本、哪一份 APK；先结束机器人正在运行的程序。
2. 保存当前硬件配置、参数以及上一份已验证安装包。确认安装目标是 Robot Controller / Control Hub，别选成 Driver Station。
3. 在 Android Studio 选择正确目标设备后部署；或者先确认队伍上传脚本的本机路径，再按它的交互步骤安装。不要把双击部署脚本当成“只做编译检查”。
4. 安装后在驾驶站核对入口名称、联盟、硬件配置；核对安装包与记录的对应关系。看见 `Blue` 这个名字，不能证明已经换成新版本。
5. 先查方向、停止和这次修改的动作，再做受影响的回归测试。合并到主干后，用**最终主干 SHA** 重新构建和检查。
6. 在[测试记录](../tests/TEMPLATE.md)和[版本登记](../releases/REGISTRY.md)写清结果。只有完成[比赛版检查](../releases/CHECKLIST.md)后，才能把某一版标为比赛可用。

遇到签名冲突或安装失败，先查原因、保留配置，不直接卸载应用或清数据来“试试看”。

## 上传脚本目前的边界

`upload-offline.py` 有设备选择、校验和安装流程，但 ADB 路径写在源码里，换电脑可能找不到。`--check` 只检查本地文件、不连接或安装；不过它仍要求 ADB 和 APK 文件存在。`ready_devices()` 返回所有已授权 ADB 设备，菜单写“USB”并不能自动证明选中的一定是 USB 目标。[路径定义](https://github.com/pengjinDaniel/FTC-16095-FatDragon-2027-Public/blob/c600214842e1c2c4d3b75428453c4d8f3fb9f3e3/upload-offline.py#L16-L19)、[本地检查](https://github.com/pengjinDaniel/FTC-16095-FatDragon-2027-Public/blob/c600214842e1c2c4d3b75428453c4d8f3fb9f3e3/upload-offline.py#L231-L251)、[设备选择](https://github.com/pengjinDaniel/FTC-16095-FatDragon-2027-Public/blob/c600214842e1c2c4d3b75428453c4d8f3fb9f3e3/upload-offline.py#L252-L279)。

它不会自动启动 OpMode，也不能凭安装包校验值证明“这个包一定来自当前源码”；源码、构建日志与包必须一起登记。涉及 Dashboard、AutoTune 等训练服务的比赛使用限制，按[规则资料](../rules/README.md)复核。
