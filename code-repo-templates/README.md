# 给代码仓库采用的模板

这里是副本，**尚未复制到真实机器人仓库，也未启用远端保护或 CI**。由整合负责人核对现有文件后，通过一个独立 PR 采用，避免覆盖原有约定。

| 本目录文件 | 采用位置 |
|---|---|
| [CONTRIBUTING.md](CONTRIBUTING.md) | 代码仓库根目录，合并已有内容 |
| [pull_request_template.md](.github/pull_request_template.md) | 代码仓库 `.github/pull_request_template.md` |
| [CODEOWNERS.example](.github/CODEOWNERS.example) | 填真实账号/团队后才考虑 `.github/CODEOWNERS` |

## 建议的 GitHub 设置

代码主干保持 `master`，知识库主干 `main`。建议要求 PR、禁止直接/强制推送、要求已配置的构建检查和讨论解决；普通至少 1 名非作者 review。核心控制按团队约定需 2 名非作者，其中一位了解实车。

分支保护通常按目标分支设必需审批数，不能假装放一份模板就能自动按风险分成 1/2 人。可以统一主干要求 2 人，或基础要求 1 人再由整合负责人对核心控制检查第二人；若采用额外自动化，需另外配置并验证。本次未设置。

建议启用新增提交后使旧批准失效；更新主干、解决冲突后重测受影响用例并重新批准。要求分支保持最新等策略要与队伍的实际合并方式匹配。[GitHub 分支保护说明](https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/managing-protected-branches/about-protected-branches)

CODEOWNERS 用于指定所有者及审查请求；**仅放这个文件不自动等于强制审批，也不保证两人批准**。强制所有者 review 需要相应保护设置；同一条有多个所有者时，通常一位所有者批准即可满足该项。账号要真实、有适当权限，团队须真实 `@组织/团队slug`。本例全部注释，避免虚构账号。[GitHub 代码所有者说明](https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/customizing-your-repository/about-code-owners)

实际可用设置受仓库类型、权限和 GitHub 方案影响。先核对当前设置，再建立约束；不能把文档中的勾选框当平台已经执行的保护。
