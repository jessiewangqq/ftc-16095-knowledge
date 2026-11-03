# 2026-11-01 电脑检查证据

本目录整理既有工程笔记中的历史记录；2026-11-03 只做复核和脱敏，**没有重新运行构建或测试，也没有连接机器人**。代码完整 SHA：`c600214842e1c2c4d3b75428453c4d8f3fb9f3e3`。

- [manifest.json](manifest.json)：版本、环境、安装包校验值和检查结果摘要。历史 APK 未在这里发布，也未认定为比赛可用版本。
- [Java 逐项结果](java-check-results.json)：原始结果文件原样保存，9 个活动检查中 8 通过、1 失败；另 7 个全注释文件未执行。
- [Python 结果](python-offline-after-build.log)：保留全部测试结果与错误；个人电脑的仓库绝对路径替换为 `<code-repo>`，未改动用例名、行号、错误或结果。
- [构建摘要](build-summary.txt)：从原始日志抽取成功、任务数量及警告行；是节选，不是完整构建日志。

原始文件名分别为 `java-check-results.json`、`python-offline-after-build.log`、`build-attempt-01.log`、`build-attempt-01.exit`、`apk.json`、`environment.json`，来自 2026-11-01 工程笔记附件。这里不公开个人电脑路径或原始环境目录清单。

检查失败的源码核对及后续任务见[当前状态](../../STATUS.md)。离线检查使用模拟硬件和合成输入，不能证明真实射击、路径跟踪或安装已经通过。
