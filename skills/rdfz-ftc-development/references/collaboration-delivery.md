# 协作与交付

复用知识库现有约定，避免让队员维护两套相同记录。下列链接指向团队知识库；处理正式任务时读取当前内容，记录采用的版本。

## 分支与检查人

代码仓库主干是 `master`，知识库主干是 `main`。先保留未提交工作，核对最新主干；一项任务一条分支，分支名服从项目和当前执行环境约定。当前环境默认使用 `codex/` 前缀。

[CONTRIBUTING.md](https://github.com/jessiewangqq/ftc-16095-knowledge/blob/main/CONTRIBUTING.md) 约定：普通文字或局部低影响修改至少 1 位非作者检查；核心控制代码至少 2 位非作者，其中至少一位了解实车。核心控制包括驱动、取球、输送、发射、自动、停止、硬件参数和共享接口。规则解释、参数说明和动作预期的文档也需对应人员核对。

不要把 AI 检查、自动测试或作者自测填成队友批准。写了约定不代表 GitHub 已启用强制分支保护；通过接口或仓库设置核对实际情况。用户当前的明确授权优先，但不据“做完任务”推断已经豁免团队 review。

## 哪些结果支持合并

依照 [合并清单](https://github.com/jessiewangqq/ftc-16095-knowledge/blob/main/tests/MERGE-GATE.md)，检查与本次改动相关的正常、边界、取消恢复、STOP 和可能受影响的旧功能。文档修改检查事实与链接，无需整车跑一遍。

正式实车记录对应已提交的代码与参数、干净工作区和实际安装产物。记录完整代码 SHA、车辆与硬件配置、APK 校验值、步骤、每次结果、失败现象、检查人及证据位置。开发时临时改参数的探索记录可以保留，但不要称为该 SHA 的正式验收。

代码 PR 链接知识库固定提交下的测试记录，区分两个仓库的 SHA。主干更新、解决冲突或 review 后继续修改，需要复查受影响内容；合并后的最终 SHA 重新构建安装并核对受影响动作。操作细节见 [构建与装车](https://github.com/jessiewangqq/ftc-16095-knowledge/blob/main/code/BUILD-DEPLOY.md)，其中旧版本结果不自动适用于新版本。

## 写到知识库哪里

| 内容 | 位置 |
|---|---|
| 规则依据和适用版本 | [rules/SOURCES.md](https://github.com/jessiewangqq/ftc-16095-knowledge/blob/main/rules/SOURCES.md) |
| 代码提交与能力说明 | [code/BASELINE.md](https://github.com/jessiewangqq/ftc-16095-knowledge/blob/main/code/BASELINE.md)、code/STATUS.md |
| 功能目标与验收条件 | tasks/ 中对应任务卡，入口 [tasks/INDEX.md](https://github.com/jessiewangqq/ftc-16095-knowledge/blob/main/tasks/INDEX.md) |
| 当前任务状态 | [plan/BOARD.md](https://github.com/jessiewangqq/ftc-16095-knowledge/blob/main/plan/BOARD.md)，只在这里维护状态 |
| 参数、设备名和标定记录 | hardware/CONFIGURATION.md、[hardware/CALIBRATION.md](https://github.com/jessiewangqq/ftc-16095-knowledge/blob/main/hardware/CALIBRATION.md) |
| 测试步骤与实际结果 | tests/，沿用 [tests/TEMPLATE.md](https://github.com/jessiewangqq/ftc-16095-knowledge/blob/main/tests/TEMPLATE.md) |
| 谁负责、谁能接手 | team/ROLES.md；只有获得真实分工后才填姓名 |
| 当天新增事实、卡点、下次动作 | daily/日期.md，链接看板与测试记录，不复制一份状态表 |
| 重要技术选择 | decisions/，沿用已有模板 |
| 最终装车或比赛版本 | releases/REGISTRY.md |
| 换人操作说明 | handoff/，要求另一位队员按说明复现 |

知识库目前公开。工作记录应限于比赛与开发，不写私人评价、账号密钥或未经授权的影像。是否发布、合并、装车或启动车辆，按用户当前授权和仓库要求执行；Skill 不提供额外授权。

## 可直接使用的交接提纲

- 这次完成的动作与任务卡。
- 代码分支、完整 SHA、知识库记录链接、实际装车是否确认。
- 改动文件和原因，受影响的操作。
- 已执行检查与逐次结果；没有执行的实车检查。
- 使用的参数、单位、修改前后值和生效方式。
- 仍卡住的具体阶段、下一步复测方法、负责人与时间安排（已确认才填写）。

用语对同学直接一些，例如“车到位了，但还没满足发射条件；先看目标转速和实际转速”，不要写“完成自动化能力闭环”。
