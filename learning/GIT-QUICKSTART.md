# 用 Git 一起改文档和程序

Git 记录文件的历史。GitHub 把仓库放到网上，方便队友共享和检查。Sourcetree 等工具可以用按钮完成操作。机器人只会运行实际安装到车上的程序，上传 GitHub 不等于安装到车上。

## 先分清几个动作

| 名字 | 在做什么 | 结束后看哪里 |
|---|---|---|
| Clone，克隆 | 把仓库复制到自己的电脑 | 目录和远端地址是否正确 |
| Branch，分支 | 从某个版本开始单独修改 | 当前是不是自己的分支 |
| Diff，差异 | 看改动前后哪些行不同 | 有没有改到无关文件 |
| Stage，暂存 | 选出这次准备提交的内容 | 是否只选了本次改动 |
| Commit，提交 | 把暂存内容记进本机历史 | 提交编号和说明 |
| Push，推送 | 把本机提交发到远端 | GitHub 网页有没有这次提交 |
| Fetch，获取 | 拿到远端新提交的信息 | 远端分支多了什么；当前工作分支还没自动合入 |
| Pull，拉取并整合 | 获取远端提交并整合进当前分支 | 是否有冲突，本机已有修改是否妥善保存 |
| PR，合并请求 | 请队友看修改，讨论能否合到目标分支 | 修改内容、测试记录、检查意见 |
| Review，检查 | 阅读差异、依据和测试，给出意见 | 意见对应的是哪个版本 |

SHA 是一次提交的编号。测试文档写完整编号，平时讨论可用短编号辅助辨认。知识库和程序仓库各有各的提交编号。

## 用网页练一次

1. 打开这个知识库，确认自己有写权限。
2. 从 `main` 建一个练习分支，例如 `docs/p2-test-pair01`。
3. 编辑一张测试卡，提交到这条分支。网页编辑直接提交到远端，不需要额外 push。
4. 发起 PR，目标选 `main`，说明改了哪项内容以及怎样检查的。
5. 请搭档看差异，指出一个需要补充的地方。
6. 继续在原分支修改并提交，这个 PR 会更新。对方确认后再合并。

只有查看权限时，先让维护者确认协作方式，不要为了练习把私有材料复制到公开仓库。

## 用本机练一次

先用自己的 GitHub 账号登录工具，用自己的姓名和提交邮箱配置 Git。不要沿用其他同学的身份。

首次克隆知识库：

```sh
git clone https://github.com/jessiewangqq/ftc-16095-knowledge.git
cd ftc-16095-knowledge
```

开始修改前先查看 `git status`。若有未提交改动，先保存并说明归属，不要直接覆盖或丢弃。工作区干净后：

```sh
git switch main
git pull --ff-only
git switch -c docs/p2-test-pair01
```

`--ff-only` 遇到两边都增加提交时会停下来，先和队友确认分支怎样整合。下面以修改一个练习记录为例，文件名换成你实际创建的那份：

```sh
git diff
git add tests/2026-11-03-pair01.md
git diff --cached
git commit -m "docs: 补充 RB 测试的起始球数和通过条件"
git push -u origin docs/p2-test-pair01
```

随后到 GitHub 发 PR。检查意见来了，仍在同一分支修改、commit、push。

Sourcetree 中对应的是“分支、工作区差异、暂存、提交、推送”。实际按钮名称可能随版本变化，先确认选中的仓库和分支。

## 冲突与恢复

出现冲突时，先找出双方各想实现什么。涉及机器人行为的冲突，请相关作者一起看，不直接全部选“我的”或“对方的”。处理后重测受影响功能，再请队友检查。

`revert` 会新增一次撤销提交，保留历史。机器人上已安装的程序不会跟着 Git 自动变化；恢复装车版本还要核对配置、重新安装并测试，见[比赛版本检查](../releases/CHECKLIST.md)。

进一步阅读：[GitHub flow](https://docs.github.com/en/get-started/using-github/github-flow)、[GitHub PR 检查说明](https://docs.github.com/en/pull-requests/reference/pull-request-reviews)、[Pro Git](https://git-scm.com/book/zh/v2)。
