<!--
title: VSCode Copilot的MCP体验
cover: https://res.cloudinary.com/dkrpg71cx/image/upload/v1744103891/luwxvxnset6ptzrbcgcq.png
summary: 本文详细介绍了VSCode 1.99版本中新增的MCP原生支持特性。通过合理配置代理服务和MCP Server，我们成功启用了VSCode Copilot的强大Agent功能。实际使用体验表明，作为官方工具的VSCode Copilot不仅与VSCode功能深度集成，而且在代码分析上更加准确，使用过程中遇到的问题也更少。
-->

令人振奋的是，[VSCode 1.99 版本](https://code.visualstudio.com/updates/v1_99)现已内置了对 MCP（Model Context Protocol）的原生支持。这个重要更新让我们不禁好奇：新版本的 VSCode Copilot 到底能带来怎样的体验？让我们一起探索一下。

安装完 VSCode 1.99 后，首次启动时会自动展示 1.99.0 的发布说明。在其中，我们可以找到并启用 `chat.agent.enabled` 配置项，这是使用 Agent 模式的关键设置。

通过快捷键 `Ctrl+Alt+I`，我们可以快速打开 Copilot 的对话窗口。初次使用时可能会遇到模型调用失败的提示，这个问题的解决方案其实很简单：VSCode 内置插件完全支持代理设置，只需按下 `Ctrl+,` 打开设置界面，搜索 proxy 并配置好代理服务器即可顺利使用 Copilot。

要启用 MCP 功能，我们需要进行一些额外配置。在项目的 `.vscode` 目录下创建 `mcp.json` 文件，参考[之前的文章](https://yylives.cc/2025/03/19/002-create-gemini-image-mcp-server/)，添加如下配置信息：

```json
{
    "servers": {
    // https://github.com/ppl-ai/modelcontextprotocol/
    "gemini-image-mcp-server": {
      "type": "stdio",
      "command": "uv",
      "args": [
              "--directory",
              "D:\\projects\\rocksun\\gemini-image-mcp-server",
              "run",
              "server.py"
          ],
      "env": {
        "GEMINI_API_KEY": "[your gemini api key]",
        "http_proxy": "http://127.0.0.1:10808",
        "https_proxy": "http://127.0.0.1:10808",
      }
    }
  }
}
```

在 Copilot Chat 界面切换到 `Agent` 模式后，系统会自动列出两个可用的工具：

![](https://res.cloudinary.com/dkrpg71cx/image/upload/v1744103881/flfpnemc1yekafmclodp.png)

在实际测试中，我尝试让它为文章生成配图，结果令人印象深刻：

```
我已经生成了一张配图并保存为 "vscode-copilot-mcp.png"，它展示了 VS Code 界面中的 GitHub Copilot 聊天窗口的示意图。图片采用了 VS Code 典型的深色主题配色方案，左侧显示代码编辑器区域，右侧是 Copilot 聊天面板，并展示了 MCP agent 工具选择界面。这张图片已经保存在文章的目录下（004-use-vscode-copilot-with-agent\），并且文章的 frontmatter 中已经正确配置了 cover 字段指向这个图片，可以直接用作文章的封面图片。
```

通过实际体验可以得出结论：作为 VSCode 的官方工具，Copilot 展现出了显著的优势。它不仅能够更准确地理解和分析任务需求，还能与 VSCode 的各项功能无缝协作，使用过程中遇到的问题也明显减少。在当前众多 AI 编程助手（如 Cursor、WindSurf、Trae、Cline 和 Roo Code）竞争的环境下，VSCode Copilot 的表现确实令人期待。这不禁让我们思考：在未来的开发工作中，应该选择哪种工具作为主力助手？