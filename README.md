# 人大附中 FTC 16095 备赛知识库

把比赛规则、程序说明、训练进度和测试结果放在一起，方便队友找到资料、接着做。

**资料更新日期：2026-11-04。** 这里整理了已有资料和公开代码分析。今天的任务与人员安排已由老师确认，见[11 月 4 日自动训练清单](plan/2026-11-04-AUTO-TRAINING.md)；车上版本和实车成绩仍需逐次记录。本文档中的测试次数和训练安排是队内建议，不能当成 FIRST 官方要求。

## 第一次打开，先看这些

| 你现在想做什么 | 从这里开始 |
|---|---|
| 我想看 11 月 4 日的任务、分工和分支安排 | [今日自动训练清单](plan/2026-11-04-AUTO-TRAINING.md) · [当前进展](plan/BOARD.md) · [今日日报](daily/2026-11-04.md) |
| 我想让 AI 按团队约定协助程序开发 | [程序开发 Skill](skills/README.md) |
| 我刚加入，想知道怎样参与 | [新队员开始使用](START-HERE.md) |
| 我想弄懂今年怎么比赛、怎么算分 | [规则入口](rules/README.md) |
| 我想知道当前程序能做什么、还差什么 | [程序现状](code/STATUS.md) · [代码版本](code/BASELINE.md) |
| 我今天要认领一件事 | [任务看板](plan/BOARD.md) · [备赛安排](plan/MILESTONES.md) |
| 我改好了，准备测试和合并 | [测试模板](tests/TEMPLATE.md) · [合并要求](tests/MERGE-GATE.md) |
| 老师今天只有半小时了解进度 | [30 分钟现场检查](handoff/FIRST-VISIT-30MIN.md) |
| 我准备给同学讲 Git 协作 | [60 分钟课程与双人练习](learning/LESSON.md) |

## 当前能确认的情况

- 团队协作程序仓库是 [rdfz-robotics/FTC-16095-FatDragon-2027-Public](https://github.com/rdfz-robotics/FTC-16095-FatDragon-2027-Public)，默认分支是 `master`；原始公开仓库为 [pengjinDaniel/FTC-16095-FatDragon-2027-Public](https://github.com/pengjinDaniel/FTC-16095-FatDragon-2027-Public)。检查日期、完整提交编号和代码证据统一放在[代码版本](code/BASELINE.md)。
- 手动驾驶、取球和辅助射击已有代码基础，具体限制见[程序现状](code/STATUS.md)。代码存在不代表已经实车通过。
- 自动 30 秒争取 **2 次有效 TIP** 是当前备赛开发目标。实际能完成几次，要看测试记录；短离墙是调试步骤和失败备用方案。
- 11 月 4 日自动训练分工已记录在[人员分工](team/ROLES.md)和[看板](plan/BOARD.md)；其他尚未确认的职责仍留待认领。没有实测记录的任务不代填完成率或测试成绩。
- 本知识库与机器人程序分开管理。机器人仓库没有因本次建库而发生代码或权限变更。

## 资料放在哪里

| 目录 | 内容 |
|---|---|
| [rules/](rules/README.md) | 官方来源、得分、排名、限制和赛前检查 |
| [code/](code/BASELINE.md) | 程序版本、架构、手柄操作、构建安装和功能现状 |
| [hardware/](hardware/CONFIGURATION.md) | 端口、硬件配置、参数与待核对项 |
| [team/](team/ROLES.md) | 谁做什么、谁能接着做、谁来检查 |
| [plan/](plan/BOARD.md) | 任务当前状态和本周、下周安排 |
| [tasks/](tasks/INDEX.md) | 每项任务要做什么、怎么检查是否做好 |
| [tests/](tests/README.md) | 测试步骤、真实结果和合并条件 |
| [daily/](daily/2026-11-04.md) | 每天的新进展、卡住的地方和下一步 |
| [decisions/](decisions/TEMPLATE.md) | 重要选择及原因 |
| [releases/](releases/REGISTRY.md) | 最终装车版本、比赛检查和恢复方法 |
| [handoff/](handoff/TEMPLATE.md) | 现场了解进度和换人操作的记录 |
| [skills/](skills/README.md) | 团队程序开发 Skill、自动标定步骤、功能复用与交接约定 |
| [learning/](learning/LESSON.md) | Git 入门、课堂练习和 AI 使用方法 |
| [code-repo-templates/](code-repo-templates/README.md) | 供机器人代码仓库参考的 PR 等模板，尚未启用 |

## 每天怎样用

1. 开始前看[任务看板](plan/BOARD.md)，选一项任务，约好谁做、谁一起检查。
2. 改代码或文档时建自己的分支，小步提交。测试前固定程序版本，结果写进 [tests/](tests/README.md)。
3. 请队友 review（检查），按[贡献约定](CONTRIBUTING.md)合并。
4. 结束前更新看板，再写当天的新情况。任务状态只维护一份，日报用链接指向它。

普通改动由 **1 位非作者**检查。涉及驱动、取球、送球、射击、自动、停止、硬件参数或共享接口的代码改动，由 **2 位非作者**检查，其中至少一位了解这台车的实际动作。知识库里的文字批准不能代替实车测试。

## 使用范围

仓库目前公开，任何人都可以阅读。需要一起编辑的同学由仓库维护者确认账号并添加写入权限。只记录比赛工作需要的信息，不写个人评价、密码或未经同意的学生影像。视频放在团队授权的存储位置，这里记录链接和时间点。

资料依据见[来源与整理说明](SOURCES.md)。本库的 review 约定已经写入文档和 PR 模板；是否启用 GitHub 强制分支保护，见[仓库设置说明](GITHUB-SETUP.md)。
