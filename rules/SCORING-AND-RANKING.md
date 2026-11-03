# 计分与排名

核对：2026-11-03。计分依据[第 10 章 TU05，§10.5–§10.6、表 10-2 / 10-3 / 10-4](https://ftc-resources.firstinspires.org/ftc/archive/2027/game/manual-10)；排位依据[第 13 章 V1，§13.6.3](https://ftc-resources.firstinspires.org/ftc/archive/2027/game/manual-13)。完整手册基线为 TU07。

## 先分清三种“分”

- **MATCH points，单场比赛分：** 翻转、停车、球的位置等带来的分数，用来判断本场胜负。
- **RP，排名积分：** 排位赛每场根据胜负和任务奖励获得，不能直接加到本场的机器人得分里。
- **RS，排名分数：** 本队有效排位场次的平均 RP，用于排位排序。

## 单场怎样得分

| 项目 | 分值 | 什么时候、怎样算 |
|---|---:|---|
| LEAVE 离墙 | 每台 3 分 | AUTO 结束时，机器人不再接触围墙 |
| AUTO PARK | 每台 5 分 | AUTO 结束时，至少部分进入本方 LOADING ZONE |
| TELEOP PARK | 每台 5 分 | 比赛结束时，至少部分进入本方 LOADING ZONE |
| HIVE TIP | 每次 20 分 | AUTO、TELEOP 均可得；必须是有效翻转 |
| 朝上 CELL 的剩余球 | 每个 2 分 | 终场静止后，朝上 CELL 内剩余的 POLLEN / NECTAR |
| 已归属的 FLOWER 中的有效球 | 每个 2 分 | 终场按归属算给一个联盟；不是谁投的就归谁 |
| FLOWER 最低有效 NECTAR 奖励 | 每塔 5 分 | 给该 NECTAR 颜色对应的联盟 |
| GARDEN 中的有效球 | 每个 1 分 | 终场至少部分在区域内；给花园颜色对应的联盟 |

LEAVE 与 AUTO PARK 在 AUTO 结束时判定；TELEOP PARK 在终场判定。CELL、FLOWER、GARDEN 的最终球数在终场全部静止后确定。TIP 的评定会持续到终场球与机器人静止；在 TELEOP 开始前完成的 TIP 归 AUTO。不能因此在禁动时段继续主动得分。详见 §10.5 及 G403、G404。

### 怎样才算一次 TIP

HIVE 从一个稳定状态翻到另一个稳定状态，原本朝下的 CELL 朝上，并且原先未接触框架的缓冲件随后接触框架，才满足定义。只看到晃动、射出一批球或软件记了一次，都不能替代真实 TIP。

只能通过向朝上的 CELL 发射球使其翻转。翻转过程中继续射向已经朝下的一侧，可能妨碍它完成翻转。依据：[§10.5.1](https://ftc-resources.firstinspires.org/ftc/archive/2027/game/manual-10)、[G417](https://ftc-resources.firstinspires.org/ftc/archive/2027/game/manual-11)。

### FLOWER 归谁，先看哪些球有效

球至少有一部分处于顶环与中环之间的计分体积，才参与 FLOWER 计分；已经掉到计分体积以下的球不算。

1. 找**最高的有效 NECTAR**：它的颜色决定这座 FLOWER 归哪个联盟，该联盟获得所有有效球每个 2 分。
2. 找**最低的有效 NECTAR**：它的颜色对应联盟另得 5 分。
3. 没有有效 NECTAR，就没有 FLOWER 归属，黄球不会单独带来这项每球 2 分的得分。

例子：计分体积内有 3 个黄球、底部 1 个红 NECTAR、顶部 1 个蓝 NECTAR。蓝联盟得到 5 × 2 = 10 分，红联盟得到底部奖励 5 分。若只有一枚有效 NECTAR，它可以同时决定归属并取得底部奖励。依据：§10.5.2。

## 排位赛的 RP 怎么拿

**下表门槛只适用于表 10-3 的 All Other Events。** 本队赛事级别待确认；Regional Championships 与 FIRST Championship 的门槛当前仍为 TBA，Premier Events 可以设自己的门槛。

| 项目 | 当前门槛 | 获得的 RP |
|---|---|---:|
| SWARM | 联盟两台车的 LEAVE + AUTO PARK + TELEOP PARK 合计至少 16 比赛分 | +1 |
| POLLINATOR 1 | 联盟累计至少 4 次 TIP | +1 |
| POLLINATOR 2 | 联盟累计至少 7 次 TIP | +1 |
| WIN | 赢得本场 | +3 |
| TIE | 本场平局 | +1 |
| LOSS | 输掉本场 | +0 胜负 RP |

这些任务奖励看**整个联盟**，不是每台机器人单独完成一份。7 次 TIP 同时达到 4 次与 7 次两档，所以得到 2 RP；不会再把“7 次”额外算成另一个 4 次任务。

三个计算例子：

- 两台车 AUTO 都离墙，共 6 分；终场都 PARK，共 10 分。6 + 10 = 16，达到 SWARM。并不要求两台都在 AUTO 停车。
- 赢得比赛，并完成三个任务奖励：3 + 1 + 1 + 1 = **6 RP**。
- 输掉比赛，但完成三个任务奖励：0 + 1 + 1 + 1 = **3 RP**。任务奖励不要求同时获胜。

依据：§10.5.5，表 10-2、表 10-3。赢、平、输是互斥结果，不能同时相加。

## 多场打完怎样排队

先算 RS：把计入排名的各场 RP 相加，除以相应场次数。例如 4、2、6、3、5 RP，平均为 4.0。

RS 相同时，依次比较：

1. 平均联盟比赛分，不含对手 MINOR / MAJOR FOUL 送来的分。
2. 平均 TIP 次数。
3. 平均 AUTO 分。
4. 仍相同则由赛事系统随机排序。

赛程标注的 SURROGATE 补充场次不计该队排名；被取消资格的那一场，该队各排序项按 0 计。排位赛取消资格只影响被取消资格的队，不直接使其联盟队友一起取消资格。依据：§13.6.2、§13.6.3、T601。

淘汰赛不再累计 RP，按固定联盟的胜负推进。排位名次、淘汰赛结果、赛季晋级是不同事项；晋级还涉及第 4 章规定与本场名额，不能说“RP 最高就一定晋级”。参见[§13.7](https://ftc-resources.firstinspires.org/ftc/archive/2027/game/manual-13)、[第 4 章](https://ftc-resources.firstinspires.org/ftc/archive/2027/game/manual-04)。

## 犯规怎样影响分数

MINOR FOUL 是轻度犯规处罚，给对方 **5 比赛分**；MAJOR FOUL 是重度犯规处罚，给对方 **20 比赛分**。具体条款还可能附带警告、黄牌、红牌或停用机器人。不是每条违规都只扣一次固定分，也不是“先警告就可以试着犯一次”。依据：§10.6、表 10-4 与具体 G 条款。

[下一步：动作限制](LIMITS.md) · [返回规则导航](README.md)
