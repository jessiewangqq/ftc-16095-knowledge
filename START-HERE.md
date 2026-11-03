# 新队员从这里开始

先选一件小事走完，不用第一天就读完所有文档。

## 第一步：能打开、能找到

让仓库维护者确认你的 GitHub 账号和访问权限。先在网页上打开 [README](README.md)，找到[规则](rules/README.md)、[任务看板](plan/BOARD.md)和[手柄操作](code/CONTROLS.md)。

要在电脑上使用，可通过 Git 工具克隆 `https://github.com/jessiewangqq/ftc-16095-knowledge.git`。这是知识库地址；机器人程序要从[程序仓库](https://github.com/pengjinDaniel/FTC-16095-FatDragon-2027-Public)单独获取。

`.md` 是 Markdown 文本，可以用 GitHub 网页、编辑器或 Obsidian 阅读。如果用 Obsidian，把这份克隆目录作为一个独立 vault 打开即可；`.obsidian/` 的个人配置不会上传。现有个人笔记不需要搬进这个仓库。

## 第二步：看一项任务

打开 [RB 卡球处理任务](tasks/P2-RB-UNJAM.md)，再看[对应测试示例](tests/RB-UNJAM-EXAMPLE.md)。留意哪些是代码里已经写好的行为，哪些还要拿车验证。

在[任务看板](plan/BOARD.md)登记自己要做的事。先问清楚哪台车、什么版本、何时能用场地，以及谁可以帮你检查。

## 第三步：第一次只改一张说明

跟着 [15 分钟双人练习](learning/PAIR-EXERCISE.md)，补一张测试卡，建分支、提交、推送、发 PR，然后请队友检查。没做过的测试写“待测”。

## 第四步：上车前确认版本和停止方式

阅读[构建安装说明](code/BUILD-DEPLOY.md)和[硬件配置](hardware/CONFIGURATION.md)。安装前确认原版本有记录、配置对应这台车。由了解机器人操作的队友陪同完成第一次演示，先弄清取消动作和 DS STOP 分别怎么用。

第一次看到动作成功，只能记录这一次的结果。后续按任务卡重复测试，把失败也记下来。
