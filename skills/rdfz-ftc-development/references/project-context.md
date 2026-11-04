# 项目背景与版本记录

这是一份带日期的背景资料，不是实时进度。每次开发仍需读取当前代码、知识库和装车记录。

## 2026 年 11 月 4 日团队交接截图

来源：用户在本次对话提供的五条开发交接说明。未推断截图作者身份，未将对话中的个人评价纳入知识库。

| 交接说明的意思 | 在开发中如何采用 |
|---|---|
| 手动功能已完整，当前主要做自动 | 本阶段以自动为主要范围，复用现有手动能力；具体版本与实车验收另核对 |
| 自动使用 Pedro Pathing，参考官网及 Visualizer | 使用项目已采用的 Pedro 版本；Visualize 路径后仍需实车验证 |
| 底盘调参所需测试程序已经放在项目里 | 先找已有标定入口，不重复写一套；按相应版本官方说明完成配置 |
| 自动吸球、射球等复用手动 Command，Shooter 有自适应能力 | 先核对接口、手柄依赖、资源占用和结束条件；复用底层能力，不直接假设所有 Command 都能独立自动运行 |
| 自动程序写在 opmodes 下的 autos，参考已有 test | 作为目录与结构约定；Test 中坐标、朝向、目标和等待逻辑仍需核对 |

以上为团队交接内容，不是 FIRST 比赛规则，也不等于独立实车验收。

## 2026 年 11 月 4 日远端核对

| 项目 | 结果 |
|---|---|
| 程序仓库 | [FTC-16095-FatDragon-2027-Public](https://github.com/pengjinDaniel/FTC-16095-FatDragon-2027-Public) |
| 当前公开分支 | `master`；本次分支接口只列出该分支，不代表没有本地或已删除分支 |
| 当前公开提交 | `7e3ef88704a21512805587e041eb78827e04da54`，2026-11-03 17:37:11，中国标准时间 |
| 项目依赖 | Pedro `revhub:3.0.2`，`tuning:1.0.1`，FTCLib `2.1.1`，见 [TeamCode/build.gradle](https://github.com/pengjinDaniel/FTC-16095-FatDragon-2027-Public/blob/7e3ef88704a21512805587e041eb78827e04da54/TeamCode/build.gradle) |
| 自动入口 | [Test.java](https://github.com/pengjinDaniel/FTC-16095-FatDragon-2027-Public/blob/7e3ef88704a21512805587e041eb78827e04da54/TeamCode/src/main/java/org/firstinspires/ftc/teamcode/opmodes/autos/Test.java)，设备显示名小写 `test`，分组 `Auto` |
| 车上安装版本、实际配置、动作验收 | 仍需现场记录 |

## 此版本需要重点核对的地方

这些是固定版本的代码观察。以后修改完成，应更新本记录或注明新版本已经解决，不把历史问题永久写成项目限制。

- [Constants.java](https://github.com/pengjinDaniel/FTC-16095-FatDragon-2027-Public/blob/7e3ef88704a21512805587e041eb78827e04da54/TeamCode/src/main/java/org/firstinspires/ftc/teamcode/pedro/Constants.java#L47-L64) 的 `foresightConfig` 仍为空。公开版 `test` 会先提示标定然后退出；可能存在未同步的实车配置，应先查找。
- `Test.java` 固定红方一个 CELL；第二段发射等待同一目标 HIGH，未实现翻转后切换到另一个朝上 CELL。不能把三段定时送球当作三次有效 TIP。
- 自动发射没有调用手动瞄准锁定控制。路径预设朝向是否足够准确，或是否需要独立瞄准阶段，必须验证。
- 900 毫秒从首次正向送球开始计时，不包括前面的准备等待。已有停止清理，但各阶段最长等待和整条路线的时间策略仍需补齐。
- 新增追球是独立 [PollenChaseTest](https://github.com/pengjinDaniel/FTC-16095-FatDragon-2027-Public/blob/7e3ef88704a21512805587e041eb78827e04da54/TeamCode/src/main/java/org/firstinspires/ftc/teamcode/tests/PollenChaseTest.java)，未接入自动吸球流程。
- 定位方向和射击参数有变化。射击表中部分点注明为起始值，不能当作已有命中率记录；需针对当前路线实测。

2026 年 11 月 3 日对这个提交完成离线构建及 10 组启用的 Java 检查，均通过；7 个完全注释的检查未执行。它只说明该环境能构建、已有离线检查通过，不能证明实车路线、视觉、命中或两次 TIP 的成功率。

知识库较早的架构、硬件与构建说明以 `c6002148` 为基线；遇到差异，以固定提交源码和对应测试证据核对，不把旧测试改写为新版通过。

## 后续记录格式

新记录至少包含核对日期、机器人代码完整 SHA、装车是否确认、配置版本、代码观察和实测证据链接。规则来源沿用知识库 `rules/SOURCES.md`，不在 Skill 中固化赛季得分或更新编号。
