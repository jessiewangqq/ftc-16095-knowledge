# GitHub 仓库与成员设置

知识库地址：[jessiewangqq/ftc-16095-knowledge](https://github.com/jessiewangqq/ftc-16095-knowledge)。主干 `main`，按私有方式建立。机器人程序仍在原仓库独立管理。

## 当前状态

| 项目 | 状态 |
|---|---|
| 知识库首版 | 本次整理并上传 |
| 成员名单和 GitHub 账号 | 待队伍确认，没有自动邀请或发送通知 |
| 任务与问题模板 | 已放入 `.github/ISSUE_TEMPLATE/` |
| PR 模板 | 已放入 `.github/pull_request_template.md` |
| 必须经过 1–2 人检查的约定 | 已写入文档；平台强制分支保护尚未启用 |
| 自动检查 | 有本地链接检查工具，尚未配置 GitHub Actions |
| 机器人代码仓库设置 | 本次没有修改 |

## 维护者接下来做什么

1. 收集需要参与的同学和老师的 GitHub 账号，确认应有的读写权限，再通过仓库 Settings 管理访问。
2. 请成员打开仓库、克隆文件并完成一次小的文档 PR，确认权限真的能用。
3. 按账号方案和仓库支持情况设置主干保护。先要求 PR 和至少一位有效批准，再决定是否统一要求两人。
4. 对核心控制改动执行两位非作者检查。单靠一个 CODEOWNERS 文件不会自动区分所有改动，也不会自动保证两人批准。
5. 确认保护是否允许维护者绕过，并把实际约定告诉队员。不能把文档清单当成平台已经强制执行。

代码仓库采用模板的方法见 [code-repo-templates](code-repo-templates/README.md)。GitHub 的设置以当前界面与[官方说明](https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/managing-protected-branches/about-protected-branches)为准。
