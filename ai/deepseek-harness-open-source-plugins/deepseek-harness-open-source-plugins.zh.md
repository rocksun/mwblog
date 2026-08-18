DeepSeek周四[开源了 DeepSeek Harness](https://x.com/deepseek_ai/status/2087887408440164663)，这是一个面向开发者的新型Agent运行环境。

该基于Node.js的框架现已在[GitHub](https://github.com/deepseek-ai/deepseek-harness)上以开发者预览版形式发布，并采用MIT许可证。

显然，人们对这个新框架兴趣浓厚。仅仅几个小时内，该仓库就获得了超过33,000个GitHub星标，且数量仍在快速攀升。目前已经形成了一个繁荣的[社区插件生态系统](https://github.com/topics/dsh-plugin)。

DeepSeek Harness的独特之处在于DeepSeek所宣称的“万物皆插件”。该团队确实贯彻了这一理念。模型适配器、工具注册表、会话日志以及Agent循环本身都是插件，且每一个都是可替换的。

![](https://cdn.thenewstack.io/media/2026/08/da2cbcb1-feat-plugin.en_-1024x640.png)

DeepSeek Harness插件。图片来源：DeepSeek。

项目文档指出，这里“没有需要修补的特权核心”，因此扩展该框架只需将插件安装在其他插件旁边即可。

其整体架构基于[Cordis](https://github.com/cordiverse/cordis)，即一个“[时空可组合性的元框架](https://github.com/cordiverse/paper)”。在某种程度上，这听起来比实际情况要复杂。其核心理念是：现代AI框架等软件工具需要动态组合，这意味着在不影响系统其余部分的情况下，必须能够轻松添加和删除组件，并且这些组件需要能够轻松交互并理解它们如何相互依赖。

一篇由来自北京大学和DeepSeek的三位研究人员撰写的[近期论文](https://github.com/cordiverse/paper/blob/main/paper.pdf)更详细地解释了这一点，并构成了Cordis和DeepSeek Harness的[基础](https://deepseek-harness.github.io/deepseek-harness/en/reference/cordis-primer)。

## 四种模式，一个模型

该框架本身附带四种预设。*Standard*模式为开发者提供了完整的编码Agent，具有文件系统工具、Shell访问、网络搜索功能、子Agent和规划模式。而在另一端，*Minimal*模式将其简化为仅包含两个工具：`bash`和`str_replace_editor`。

此外还有*Code*模式，它改变了工具与模型交互的方式。它不再将这些工具暴露为单独的函数调用，而是生成一个TypeScript SDK，并让模型编写针对该SDK的程序，因此原本需要五次往返的序列只需一次调用即可完成。

第四种预设，*Creator*模式，旨在为希望创建自定义Agent预设的开发者准备。它继承了*Standard*模式的所有功能，并增加了运行时检查、插件实验和预设编写指南。

## 模型可见的一切都会被记录

该框架的另一个核心功能是它保留了一个仅追加的会话日志。任何到达模型请求的内容都必须能够从该日志中重建。

这也意味着对话历史不仅仅是一个实现细节。相反，恢复、分支、重放、转录、遥测和Web UI等核心功能都基于这一单一事件流。因此，添加任何新类型的模型可见输入意味着添加一个新的会话事件。

Agent沙盒同样严格——正如任何Agent框架所应有的那样。本地后端通过DeepSeek编写的Node插件，将子进程封装在Linux的[Landlock](https://landlock.io/)、macOS的[Seatbelt](https://sandboxicon.com/tech/seatbelt/)或Windows的ACL限制令牌运行器中。

![](https://cdn.thenewstack.io/media/2026/08/b0af4f5e-trajectory-real-view.en_-1024x640.png)

Agent日志。图片来源：DeepSeek。

## 使用他人的模型

值得强调的是，框架中没有任何内容将其绑定到DeepSeek的模型上。事实上，提供商目录涵盖了Anthropic、OpenAI、AWS Bedrock、Microsoft Azure和Google的[Gemini Enterprise Agent Platform](https://thenewstack.io/google-gemini-agent-platform/)（尽管文档仍称其为Vertex），以及DeepSeek自己的端点。此外还可以选择为其他推理提供商添加自定义的兼容OpenAI的网关。

有趣的是，该框架还附带了两个子Agent提供商，可以将工作直接委托给Anthropic的[Claude Code](https://github.com/deepseek-ai/deepseek-harness/tree/master/packages/subagent/subagent-claude-code)和OpenAI的[Codex](https://github.com/deepseek-ai/deepseek-harness/tree/master/packages/subagent/subagent-codex)，从主机PATH中解析每个产品的二进制文件，因此用户需要自行提供安装和登录信息。两者默认均处于关闭状态。

DeepSeek还提供了桥接程序，可以针对框架自身的拦截点运行用户现有的`hooks.json`（来自上述任一产品），README将其描述为一种兼容性路径，而非更佳的设计。

此外，它还支持MCP客户端、Agent Client Protocol，并且框架可以读取`AGENTS.md`和`CLAUDE.md`文件。

## 暂无Pull Request

关于为该项目做出贡献，DeepSeek目前指出：“我们很抱歉，目前无法接受外部的Pull Request。”相反，它建议有志于贡献的人前往GitHub Discussions进行讨论，并转而开发插件。

该公司表示，它并不认为官方仓库中的包比社区的更重要，读者应将该仓库视为“一个想法、一个官方展示和灵感来源，而不是我们的指令。”

当然，目前这类框架随处可见，每个主要实验室现在都发布了编码Agent。在中国实验室中，阿里巴巴的Qwen Code和字节跳动的Trae Agent均于2025年中期发布，月之暗面的Kimi CLI紧随其后，智谱的ZCode则于7月推出。

DeepSeek显然认为其插件架构是主要的差异化优势，虽然大多数竞争对手也是开源的，但对新框架的早期反应表明，尽管竞争激烈，DeepSeek可能确实触及了开发者正在寻找的东西。