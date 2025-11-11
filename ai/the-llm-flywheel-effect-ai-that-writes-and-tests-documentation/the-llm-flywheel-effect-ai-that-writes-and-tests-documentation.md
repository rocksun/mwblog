
<!--
title: 大模型飞轮效应：AI 助力文档创作与测试
cover: https://cdn.thenewstack.io/media/2025/11/1188f9b7-a-c-depazdna2hc-unsplashb.jpg
summary: AI 助手能创建和测试文档，形成“飞轮效应”。通过人类协调，迭代优化 MCP 服务器，加速项目上手。
-->

AI 助手能创建和测试文档，形成“飞轮效应”。通过人类协调，迭代优化 MCP 服务器，加速项目上手。

> 译自：[The LLM Flywheel Effect: AI That Writes and Tests Documentation](https://thenewstack.io/the-llm-flywheel-effect-ai-that-writes-and-tests-documentation/)
> 
> 作者：Jon Udell

为了帮助团队成员快速上手一个项目，我不得不学习并记录如何在 Mac 环境中同时设置 Node.js 和 .NET 运行时。我从未在 Mac 上使用过 .NET，所以这份文档的第一个“客户”就是我自己。

很自然地，我求助于我的 AI 助手团队，他们集体拥有关于这个主题的大量知识。他们编写说明，我跟着操作并报告问题，我们通过迭代找到了解决方案。

然后我恍然大悟：这些 AI 助手不仅可以帮助编写说明，他们还可以阅读并帮助我重现它们。我决定称之为**飞轮效应**。这不是自动的；我还没有像其他人所说的那样拥有无需干预的 AI 体验，但那也不是我的目标。我不想置身事外；我希望高效地参与其中：启动飞轮旋转，然后策略性地推动它以积蓄动能。

## MCP 服务器在 AI 工作流程中的作用

实现这一情景的关键是文件系统 MCP 服务器，它使像 Claude 和 Cursor 这样的代理能够读写文件。Anthropic 的[参考实现](https://github.com/modelcontextprotocol/servers/tree/main/src/filesystem)授予了读写不断演进的文档所需的访问权限。它没有授予运行必要系统命令的权限，因此我坚定地参与其中：复制/粘贴他们建议的命令，运行它们，复制/粘贴输出，然后讨论下一步。

> 我不想置身事外，我希望高效地参与其中：启动飞轮旋转，然后策略性地推动它以积蓄动能。

这运作得很顺利，除了在助理团队中管理 MCP 配置持续存在的困难。每个助理都有自己的配置文件，尽管 MCP 协议本身是标准的，但这些配置文件的位置和格式却不是。

在[LLM 如何引导我们找到配置和编码的理想路径](https://thenewstack.io/how-llms-guide-us-to-a-happy-path-for-configuration-and-coding/)中，我观察到配置是新的难题——一个超越了缓存失效、命名和差一错误的问题。你可以让 AI 助手来调试它们自己的配置，但我希望那些运行[我们自己的 MCP 服务器](https://github.com/xmlui-org/xmlui-mcp)的人不必这样做；这太扫兴了。有没有更好的方法来处理这个问题？如果有，请告诉我，我洗耳恭听。

你也可以使用 Claude Code 或 Codex 以更直接的方式完成这类事情。为了测试这种方法，我清除了安装，并要求 Claude Code 阅读说明，遵循步骤，在我的允许下运行所有必要的命令，评估输出，并生成一份最终报告。一切都安装好了，后端服务器启动了，前端应用程序也成功运行了。这是报告。

```
  1. Verify Node.js/npm prerequisites

  node --version && npm --version
  Output: v20.19.0 and 10.8.2 ✅ (meets v20+ requirement)

  ---
  2. Install .NET 9.0 SDK on macOS

  brew install dotnet
  Output:
  - Successfully installed to /opt/homebrew/Cellar/dotnet/9.0.8
  - Note about potentially needing DOTNET_ROOT environment variable
  - Installation completed without errors ✅

  ---
  3. Verify .NET SDK installation

  dotnet --version
  Output: 9.0.109 ✅ (confirms SDK, not just runtime, was installed)

  ---
  4. Install frontend dependencies

  npm install
  Output:
  - Installed 895 packages in 12 seconds
  - Deprecation warnings (as expected per guide)
  - Completed successfully ✅

  ---
  5. Start backend API server

  npm run start:backend
  Output evaluated:
  - Compilation warnings (expected C# nullable reference warnings)
  - Key success message: "Starting MWD Mock Server:"
  - "Now listening on: http://localhost:5001"
  - "Application started. Press Ctrl+C to shut down." ✅

  ---
  6. Start frontend development server

  npm run start
  Output evaluated:
  - Starting with options: { withMock: false, withProxy: undefined }
  - "➜  Local:   http://localhost:5173/"
  - CJS deprecation warning (informational, not blocking) ✅

  ---
  7. Copy test files

  cp tests/fixtures/* ~/mwd/shares/Documents/
  Verification:
  ls -lh ~/mwd/shares/Documents/
  Output evaluated:
  - test.jpeg (58K) ✅
  - test.pdf (3.8K) ✅
  - test.xlsx (8.1K) ✅
  - Plus additional pre-existing files

  ---
  8. Test backend API endpoint

  curl -H "Authorization: SessionID 12345" "http://localhost:5001/api/v3/ListFolder?path=:sh:Documents:/"
  Output evaluated:
  - Received valid JSON array with 9 file objects
  - Each object contains: name, path, created, modified, attributes, size
  - Test files present with correct sizes:
    - test.jpeg: 59,276 bytes
    - test.pdf: 3,908 bytes
    - test.xlsx: 8,337 bytes
  - HTTP 200 response ✅

  ---
  Key Validation Points:

  1. Installation process: brew install dotnet worked without manual PATH configuration
  2. Build process: Backend compiled with warnings but ran successfully
  3. Server startup: Both servers started and listened on expected ports
  4. File system: Backend correctly created ~/mwd/shares/Documents/ structure
  5. API authentication: Hardcoded SessionID 12345 worked as documented
  6. Data flow: Files copied to filesystem were accessible via API

  Documentation Accuracy:

  All steps executed successfully in order without modifications or workarounds.

```

在 [Gist](https://gist.github.com/judell/815a9b81cec4f37aac756e307beb8588) 上查看代码。

长期以来，我们一直将文档视为一流的软件工程学科，但其具体含义一直不甚明朗。现在，这一图景正变得清晰。AI 助手不仅可以帮助我们[创建文档](https://thenewstack.io/code-in-context-how-ai-can-help-improve-our-documentation/)，还可以帮助我们[测试文档](https://thenewstack.io/how-llms-guide-us-to-a-happy-path-for-configuration-and-coding/)——就像我们测试代码一样。如果你曾努力编写可重现的文档，或者因安装说明不符而感到沮丧，你将会体会到这种飞轮效应的强大力量。

## 通过 AI 反馈迭代 MCP 服务器

当我使用 Claude 帮助构建 [XMLUI MCP 服务器](https://github.com/xmlui-org/xmlui-mcp)的第一个版本时，我惊讶地发现，由于 Claude 也是该服务器的客户端，我可以要求它反思从 MCP 服务器提供的工具中获得的响应，然后调整服务器代码以改进这些响应。一个主要的优先事项是[将代理锚定到事实真相](https://thenewstack.io/how-to-upgrade-your-mcp-server-with-context-engineering/)，因此我们安排所有响应都包含严厉警告：不要发明语法，只使用和推荐由包含工作示例的文档支持的技术，始终引用这些文档的 URL。

> 代理到代理架构可能在未来出现。

有了这些指导，编码代理表现得比以前好，但它们通常仍然会忽略指导，需要互动提醒才能遵循。更大声地对它们喊叫是没用的。问题的根源在于 MCP 服务器没有独立的代理能力。它可以尝试影响代理如何选择和使用其工具，但最终无法控制这种选择和使用。我的预感是 MCP 服务器需要变得更像代理，这样它才能与编码助手的代理在更平等的地位上协作。代理到代理架构可能在未来出现。

与此同时，当我招募我的助理团队来评估 MCP 服务器时，他们都认为冗长的指导浪费了 token。例如，反馈中提到：“强制性（MANDATORY）指导块重复冗余，每次失败会消耗约 2k token。”一个相关问题是搜索结果可能过于冗长，同样会消耗 token 预算。

我选择 Kiro 来精简响应，然后重建了服务器，并要求它重新评估那些产生了冗长响应的示例查询。以下是它所看到的结果。

*- 失败消息现在简洁明了：只有三个要点，而不是 20 多个“强制性（MANDATORY）”警告（每次失败节省约 1.5k token）*

*- 结果截断功能正常：成功的搜索显示 20 个结果，并带有“… X more results omitted …”消息（比旧的“use JSON for full list”更清晰）*

*- 摘要截断：长行在 200 个字符处截断，并带有“…”*

*- 所有工具都受到影响：改进适用于 xmlui\_search、xmlui\_search\_howto 和 xmlui\_examples*

因为这是一项团队合作，所以我接着让 Cursor 做了同样的评估。这是它注意到的：

*问题：当没有结果时，代码总是包含无用的基本规则提醒：*

*“引用包含文件路径和 URL 的来源”（无来源可引用）*

*“如果可用，从 documentation\_urls 提供 URL”（无可用 URL）*

*这些提醒对于成功搜索有用，但对于失败则无用。*

好主意！我将反馈转达给了 Kiro，它进行了隐含的更改，我通过整个团队的一轮反馈验证了这些更改。

## 人类开发人员在良性循环中的作用

虽然我怀疑新生的[代理到代理协议](https://thenewstack.io/googles-agent2agent-protocol-helps-ai-agents-talk-to-each-other/)将使这类事情更自主地发生，但我很高兴能担任协调者的角色，而且我认为我永远不会完全放弃这个角色。

这让我想起了关于边飞行边造飞机的老话。在这种情况下，奇怪而奇妙的是，感知到问题的飞行员也是修复它们的机械师。在这种情景中我是谁？如果我强行解释这个比喻，我想我就是航空公司的经理，负责设定目标、组建团队、启动飞轮旋转，并在正确的时间以正确的方式推动它，以加速改进的良性循环。