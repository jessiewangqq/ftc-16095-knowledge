# BIOBUZZ 规则速读

核对：2026-11-03。依据完整手册 TU07；本页主要使用[第 10 章 TU05](https://ftc-resources.firstinspires.org/ftc/archive/2027/game/manual-10)与[第 11 章 TU07](https://ftc-resources.firstinspires.org/ftc/archive/2027/game/manual-11)。

## 一场比赛是谁和谁配合

场上通常有四台机器人：红联盟两支参赛队、蓝联盟两支参赛队。一个“参赛队”与一个“联盟”不是同一个概念。即使几支队伍来自同一所学校，也要按本场赛程所属的红、蓝联盟参加比赛。排位赛队友由赛程分配，不是自己临场换；淘汰赛的联盟在选盟后固定。依据：[§10.1](https://ftc-resources.firstinspires.org/ftc/archive/2027/game/manual-10)、[§13.6.2、§13.7](https://ftc-resources.firstinspires.org/ftc/archive/2027/game/manual-13)。

赛前与队友商量各自的起点、路线、取球区和停车位置。两台车可以分担任务；“双方都是熟人”不改变场上的计分、犯规和公平比赛要求。依据：[G201、G202](https://ftc-resources.firstinspires.org/ftc/archive/2027/game/manual-11)。

## 先认清球和得分装置

| 看到的东西 | 名称 | 主要作用 |
|---|---|---|
| 黄色球 | POLLEN，花粉 | 收集后投向 HIVE，也可进入 FLOWER 或 GARDEN |
| 红色 / 蓝色球 | NECTAR，花蜜 | 属于相应联盟；FLOWER 的归属和底部奖励看它的位置 |
| 会翻转的蜂巢装置 | HIVE | 向朝上的 CELL 投球，使它完成有效翻转（TIP） |
| HIVE 上装球的部分 | CELL | 发射前确认哪一侧朝上 |
| 四个竖直花塔 | FLOWER | 顶部放球、底部取 POLLEN；计分范围不是整个塔 |
| 地面的联盟花园区域 | GARDEN | 终场在区域内的有效球给该颜色联盟得分 |
| 装载区域 | LOADING ZONE | 人员投球首先落地的位置，也是停车计分区域 |

结构与边界按[第 9 章 ARENA（TU06）](https://ftc-resources.firstinspires.org/ftc/archive/2027/game/manual-09)和[第 16 章术语（V1）](https://ftc-resources.firstinspires.org/ftc/archive/2027/game/manual-16)查看。

## 开场的 40 个黄球在哪里

| 位置 | 计算 | 黄球数量 |
|---|---|---:|
| 四个 FLOWER | 每个 4 个 | 16 |
| 红、蓝两个 GARDEN | 每边 4 个 | 8 |
| 四台机器人预装 | 每台 4 个 | 16 |
| **合计** | 16 + 8 + 16 | **40** |

“每台预装 4 个”已经算在总数 40 中，不是在 40 之外再加 16 个。预装球要与机器人接触；可在车内、车上，或在地垫上接触机器人，并完全位于本方半场。依据：[§10.3.1、§10.3.4](https://ftc-resources.firstinspires.org/ftc/archive/2027/game/manual-10)。

NECTAR 另算：红、蓝各 8 个，总计 16 个。每方 3 个预置在对应颜色的朝上 CELL，另 5 个放在该联盟场外区域，等待合法投入。FIRST Championship / Premier Events 可能调整摆场，参见 §10.3.1 的适用说明。

## 时间怎样分

| 阶段 | 时长 | 可以怎样操作 |
|---|---:|---|
| AUTO 自动阶段 | 30 秒 | 按预先编好的程序运行，驾驶员不能用手柄引导它；开始、停止及规则列出的例外另论 |
| 转换 | 8 秒 | 机器人不能有电力驱动的运动，准备切换到 TELEOP |
| TELEOP 手动阶段 | 120 秒 | 驾驶员操作，也可以调用程序辅助动作 |
| TELEOP 最后 60 秒 | 包含在上面的 120 秒内 | 可以把 NECTAR 放入 FLOWER 计分体积；场外尚未解锁的 NECTAR 此时也可投入场内 |

依据：[§10.4](https://ftc-resources.firstinspires.org/ftc/archive/2027/game/manual-10)、[G401、G403、G404、G410、G426](https://ftc-resources.firstinspires.org/ftc/archive/2027/game/manual-11)。最后 60 秒不是另加一分钟，以场地正式计时器为准。

## TIP 解锁一枚 NECTAR 是什么意思

本方 HIVE 每完成一次 TIP，人员就多获得一次把一枚本方场外待投 NECTAR 放入场内的许可。不是新生成一个球，也不是要求立刻投。若已经解锁两枚但只投了一枚，就还有一枚已获许可的球可以随后投。最后 60 秒时，其余待投 NECTAR 都可投入。

投入时，球必须先接触本方 LOADING ZONE 的地垫，再接触机器人或其他场地结构；不能直接递到机器人里。飞出场外的本方 NECTAR 按 G427 可重新投入，另有相应条件。依据：[G426、G427](https://ftc-resources.firstinspires.org/ftc/archive/2027/game/manual-11)。

注意：**“可以投进场内”不等于“可以提前放进 FLOWER”。** 后者仍受 G410 的最后 60 秒限制。

## 自动与手动任务怎么分

下面是本队制定计划的办法，不是官方规定的动作顺序，也不是已经完成的实车能力。

- **自动阶段先测一条完整得分路线。** 从合法起点出发，瞄准朝上 CELL 发射，确认真实 TIP；如果要继续第二次，先确认新朝上目标，再按剩余球量决定是否补球，并留出停止时间。能做几次，应由 30 秒实测决定。
- **手动阶段把重复得分做顺。** 取球、移动、瞄准、投球、卡球处理都要能连起来，操作手知道什么时候该停、该重新观察。
- **最后一分钟与队友分工。** 谁投 NECTAR、谁继续翻转、谁负责哪座 FLOWER，什么时候回装载区停车，提前商量。

离墙与停车可以作为失误后保住分数的方案，但不应据此假定全部自动目标只是“开走再停下”。同样，计划写“多次翻转”之前，要先拿到真实的完成时间和成功情况。把计划写进[任务卡](../tasks/TEMPLATE.md)，把测试写进[测试记录](../tests/TEMPLATE.md)。

[下一步：计分与排名](SCORING-AND-RANKING.md) · [返回规则导航](README.md)
