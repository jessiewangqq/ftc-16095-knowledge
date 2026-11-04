# 团队程序开发 Skill

这份 Skill 让 AI 按团队约定协助开发、标定、排错和交接，默认对应人大附中 FTC 16095。它不会自动获得 GitHub 写入权限，也不会替代队友 review 或实车测试。

入口：[人大附中机器人团队程序开发 SKILL.md](rdfz-ftc-development/SKILL.md)。

| 想了解什么 | 阅读位置 |
|---|---|
| 开发时遵守哪些约定 | [Skill 主文件](rdfz-ftc-development/SKILL.md) |
| 交接截图说了什么，采用哪版代码 | [项目背景与版本记录](rdfz-ftc-development/references/project-context.md) |
| AutoTune 怎么打开，参数怎么保存，自动动作怎么接 | [自动程序开发与标定](rdfz-ftc-development/references/autonomous-workflow.md) |
| 分支、测试、review 和每天交接怎样做 | [协作与交付](rdfz-ftc-development/references/collaboration-delivery.md) |

## 怎样使用

在支持本地 Codex Skills 的环境中，将整个 `rdfz-ftc-development` 文件夹放进自己的 Skills 目录，通常是 `~/.codex/skills/`；若已设置 `CODEX_HOME`，使用该目录下的 `skills/`。保留 references 和 agents 子目录，不只复制 SKILL.md。以本仓库目录为维护源，更新后同步本机副本。

可以这样提出任务：

> 使用 $rdfz-ftc-development，检查当前最新代码，找出两次翻转自动路线还缺哪些连接。先分析，不修改程序。

> 使用 $rdfz-ftc-development，帮我们操作前梳理 Foresight 标定步骤，说明网页入口、车辆动作和参数保存位置。

> 使用 $rdfz-ftc-development，在任务分支实现指定自动动作，复用已有吸球和发射功能，完成相关检查并准备 PR。

在其他 AI 工具里，也可先提供 SKILL.md 和本次任务需要的参考文件；它们不会因“已经放进 GitHub”就自动被读取。

本 Skill 的新增和修改按 [知识库协作约定](../CONTRIBUTING.md)检查；截图来源和固定版本观察见 [项目背景](rdfz-ftc-development/references/project-context.md)。
