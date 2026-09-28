**自主编码吸引人的地方在于你可以把任务交给它**，赋予它访问代码库和工具的权限，然后在它工作时放手不管。Google最新发布的 Gemini CLI 明确规定了某些特定时刻，代理必须停下来等待你的指令。

周三发布的 [Gemini CLI 0.61.0](https://github.com/google-gemini/gemini-cli/releases/tag/v0.61.0) 要求在代理编辑构建配置文件、在此类编辑后运行构建或测试命令、或者执行其参数似乎来自不受信任的外部内容的 shell 命令之前，必须获得明确确认。同一版本还单独加固了 Gemini CLI 的可选沙箱，以确保主机凭证和配置不会被在沙箱内运行的任何程序触及。

赋予编码代理修改和执行代码的更多权限，同时也给了攻击者更多将该权限转化为针对开发者攻击的途径。Gemini CLI 0.61.0 在其中一些关键节点重新引入了人工审核。

## 公开的安全修复

Google 在 5 月份的 I/O 大会上宣布，将把 Gemini CLI 的 Pro、Ultra 和免费层用户迁移至其闭源的 Antigravity CLI，并且自 6 月 18 日起，该开源工具主要服务于企业客户和付费 API 密钥开发者。该公司表示，Gemini CLI 将继续获得模型更新、Bug 修复和安全补丁。这些安全变更仍在公开开发中，0.61.0 版本背后的合并请求（pull requests）准确展示了 Google 所担忧的问题。

## 构建文件成为攻击向量

对 package.json、Makefile、pyproject.toml 或 Bazel BUILD 文件的修改可能会引入依赖项或触发脚本。Gemini CLI 可以利用[网络搜索和外部工具](https://thenewstack.io/coding-with-the-gemini-cli-tool/)中的信息进行这些修改，然后运行 shell 命令。如果在修复 Bug 时获取的文档包含向 package.json 添加 postinstall 脚本的隐藏指令，代理可能会在开发者从未手动输入该命令的情况下，进行修改、运行项目的测试套件并执行恶意代码。

> 赋予编码代理修改和执行代码的更多权限，同时也给了攻击者更多将该权限转化为针对开发者攻击的途径。

标题为“防止通过构建文件修改和不受信任的标志进行间接提示词注入”的[合并请求 #29250](https://github.com/google-gemini/gemini-cli/pull/29250) 直接针对这一攻击序列。对已知构建文件的修改现在需要确认，并且 Gemini CLI 会跟踪会话期间更改的构建文件，从而将任何后续的构建或测试命令（例如 npm run、make 或 cargo）暂停，等待明确批准。确认对话框还会显示完整的构建文件 diff，而不是进行截断。

## 不受信任的参数需要批准

第二个检查涵盖命令参数。Gemini CLI 现在将来自网络抓取、MCP 服务器响应、Google Docs 以及 Google 内部问题追踪器 Buganizer 的内容视为不受信任的上下文，并且在运行其标志或参数与该内容中的 Token 匹配的任何 shell command 之前会进行询问。在这两种情况下，提示框都会取消持久批准选项，因此开发者无法对这些操作授予永久的“始终允许”。

该合并请求将这些更改与受限制的工作区模式（即 Gemini CLI 对用户标记为不受信任的文件夹应用的的安全模式）绑定在一起，且并未详细说明这些检查在受信任文件夹中或在自动批准下的行为方式。

参数检查匹配的是 Token，而不是追踪每个值的来源，合并请求的评审历史表明要做好这一点有多么困难。Google 的自动化评审员在早期版本中标记了几种绕过方法，包括加引号的参数、环境变量前缀、shell 重定向目标以及 Windows 路径处理，所有这些都在 9 月 11 日更改合并之前得到了解决。

## 沙箱保护凭证安全

[合并请求 #29214](https://github.com/google-gemini/gemini-cli/pull/29214) 收紧了 Gemini CLI 的沙箱。当沙箱通过 Docker、Podman、LXC 或 macOS Seatbelt 运行工作时，宿主机的 ~/.gemini 目录不再被挂载到其内部。取而代之的是，CLI 会传入剥离了 API 密钥、钩子和自定义工具命令的用户设置的净化副本。它还阻止沙箱在主目录等敏感位置启动，而新的 Seatbelt 规则则拒绝访问 OAuth 凭证、受信任文件夹决策和 .env 文件。

Google 的[沙箱文档](https://google-gemini.github.io/gemini-cli/docs/cli/sandbox.html)将此功能称为 AI 操作与主机系统之间的安全屏障，同时也警告称它降低了风险但并未消除风险。这两个合并请求说明了为什么这两个层面都是必需的。沙箱限制了进程运行后可以触及的范围，而确认要求则决定了代理首先是否有权采取敏感操作。构建文件使这一差距变得具体：沙箱挂载了项目目录以便代理可以对其进行编辑，这意味着在沙箱内部编写的有毒 package.json 在开发人员或 CI 作业随后在沙箱外部运行构建时仍会留在仓库中。

> ……在沙箱内部编写的有毒 package.json 在开发人员或 CI 作业随后在沙箱外部运行构建时仍会留在仓库中。

Gemini CLI 已经为开发者提供了决定代理自主程度的方法，从[在代理工作流的固定点运行确定性检查的钩子](https://thenewstack.io/gemini-cli-gets-its-hooks-into-the-agentic-development-loop/)，到根据[Google 的文档](https://google-gemini.github.io/gemini-cli/docs/tools/mcp-server.html)会绕过该服务器所有工具调用确认的 MCP 服务器信任设置。然而，正如[针对 MCP 服务器的工具投毒和拉地毯攻击](https://thenewstack.io/building-with-mcp-mind-the-security-gaps/)所显示的那样，曾经授予信任可能会随着时间变得糟糕，因为一天批准的工具可能会在后来开始返回攻击者控制的内容。

> 曾经授予信任可能会随着时间变得糟糕……当一天批准的工具开始返回攻击者控制的内容时。