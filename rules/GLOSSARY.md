# 常用术语：听到这个词，先想到什么

核对：2026-11-03。下表是便于交流的中文解释，不是逐字译文；精确定义见[第 16 章 Glossary，V1](https://ftc-resources.firstinspires.org/ftc/archive/2027/game/manual-16)。计分和判罚还要一起看相应条款。

## 场地与球

| 术语 | 直观理解 | 容易混淆的地方 |
|---|---|---|
| ALLIANCE | 联盟，每场由两支 FTC 队伍合作 | 一所学校不一定就是一个联盟 |
| FIELD | 围墙以内的比赛场地 | ARENA 范围更大，还包括排队、控制与计分设施等 |
| POLLEN | 花粉，黄色球 | 不分红、蓝联盟 |
| NECTAR | 花蜜，红色或蓝色球 | 有联盟颜色；不能控制对方的 NECTAR |
| SCORING ELEMENT | 得分物，本赛季指 POLLEN 与 NECTAR | G407 的 4 个上限合并计算两类球 |
| HIVE | 蜂巢，会翻转的装置 | “向它发射”不等于“已经翻转” |
| CELL | HIVE 上能装球的结构 | 要辨认当前哪侧朝上 |
| TIP | HIVE 从一个稳定状态完成到另一个稳定状态的有效翻转 | 具体计分条件看 §10.5.1 |
| FLOWER | 花塔，从顶部放球、底部可取 POLLEN | 只有指定体积内的球参与花塔计分 |
| GARDEN | 联盟花园区域 | 不是受保护区；也不是 LOADING ZONE |
| LOADING ZONE | 装载区，人员投球落地和机器人停车涉及的区域 | 按场地边界判断，不靠“差不多靠边” |
| ALLIANCE AREA | 联盟人员所在的场外区域 | 与机器人在场内的装载区不同 |

场地结构参见[第 9 章 TU06](https://ftc-resources.firstinspires.org/ftc/archive/2027/game/manual-09)，计分参见[第 10 章 TU05](https://ftc-resources.firstinspires.org/ftc/archive/2027/game/manual-10)。

## 比赛过程与处罚

| 术语 | 中文解释 |
|---|---|
| AUTO | 自动阶段，30 秒，机器人按预编程序运行 |
| TELEOP | 手动阶段，120 秒，驾驶员可操作，也可调用辅助功能 |
| LEAVE | 离墙得分，AUTO 结束时不再接触围墙 |
| PARK | 停车得分，按规定时刻检查是否至少部分在本方装载区 |
| CONTROL | 控制球：不只是装进仓，也包括托住、卡住或有意推到指定方向等情况 |
| PIN | 通过直接或间接接触阻止对方机器人移动；不能只译成“碰了一下” |
| MINOR FOUL | 给对方加 5 比赛分的犯规处罚 |
| MAJOR FOUL | 给对方加 20 比赛分的犯规处罚 |
| DISABLED | 裁判要求停用机器人，队员按 DS 停止并放下手柄 |
| DISQUALIFIED / DQ | 被取消本场资格；对排位赛与淘汰赛的影响不同 |
| RP | Ranking Points，排名积分，来自本场胜负和任务奖励 |
| RS | Ranking Score，排名分数，即计入排名场次的平均 RP |
| SWARM | 一项 RP 奖励，看联盟离墙与停车得分合计是否达到门槛 |
| POLLINATOR 1 / 2 | 两项 RP 奖励，分别看联盟 TIP 总次数是否达到门槛 |
| SURROGATE | 赛程安排的补充出场；该场不计这个队的排名，其他纪律影响仍按规则处理 |
| Team Update / TU | 官方赛季更新；章节和完整手册的 TU 编号可能不同 |

处罚与得分见[§10.5–§10.6](https://ftc-resources.firstinspires.org/ftc/archive/2027/game/manual-10)，具体行为见[第 11 章 TU07](https://ftc-resources.firstinspires.org/ftc/archive/2027/game/manual-11)，排名见[§13.6.3](https://ftc-resources.firstinspires.org/ftc/archive/2027/game/manual-13)。

## 本队讨论程序时用的词

下面是开发交流用语，不是本赛季专门的比赛规则。

| 用语 | 在我们工作中的意思 |
|---|---|
| RC / Robot Controller | 运行机器人程序的一端 |
| DS / Driver Station | 驾驶员用来选程序、启动、停止和接收信息的设备与 App |
| OpMode | 在 DS 中选择的一套机器人运行程序，例如某条自动路线或手动驾驶程序 |
| INIT | 初始化，为启动做准备；初始化也可能移动机构，必须实际检查 |
| 卡球处理 | 球卡住时用反转退球等方式恢复；处理后还要核对真实剩余球数 |
| SHA / 提交编号 | Git 中标识一次提交的编号，用于说明到底测了、安装了哪个版本 |
| review / 代码检查 | 非作者队友查看代码、说明和测试，提出遗漏或问题 |
| 回归检查 | 修改一个功能后，再检查原来能用的功能有没有被改坏 |
| 主干 | 团队集成代码的主要分支；分支名以实际仓库为准，可能叫 main 或 master |

[返回规则导航](README.md)
