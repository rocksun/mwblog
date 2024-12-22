# CodeGate：开源工具保障AI编码助手安全

![CodeGate：开源工具保障AI编码助手安全的特色图片](https://cdn.thenewstack.io/media/2024/12/de20e3a0-codegate-ai-project-2-1024x576.jpg)

那个友好而乐于助人的AI编码助手？你不能相信它。

大多数程序员现在都使用诸如[GitHub Copilot](https://thenewstack.io/microsoft-makes-github-copilot-free-in-vs-code/)、[ChatGPT](https://thenewstack.io/how-to-learn-unfamiliar-software-tools-with-chatgpt/)和[Amazon Q Developer](https://thenewstack.io/amazon-q-developer-now-handles-your-entire-code-pipeline/)之类的[AI编码助手](https://thenewstack.io/ai-code-assistants-are-moving-beyond-auto-complete-heres-whats-next/)。事实上，根据2024年Stack Overflow的调查，[76%的受访者已经使用或计划使用AI编码助手](https://stackoverflow.blog/2024/05/29/developers-get-by-with-a-little-help-from-ai-stack-overflow-knows-code-assistant-pulse-survey-results/)。

这可能是一个很大的错误。

在一封电子邮件采访中，[Kubernetes的联合创始人之一](https://thenewstack.io/at-kubernetes-10th-anniversary-in-mountain-view-history-remembered/)以及软件供应链安全公司[Stacklok](https://stacklok.com/)的创始人兼首席执行官告诉The New Stack：“在过去几周里，我观察到AI编码助手将秘密信息泄露给OpenAI，并且我看到各种[大型语言模型]推荐已弃用和危险的（甚至是虚构的）软件包，然后AI编码助手试图安装这些软件包。”

哇！

情况更糟。“这变得更加复杂，因为外国对手一直在积极发布恶意软件包，其名称通常是虚构的，”补充道。

为了解决这个问题，他表示，StackLok 有一个新的开源项目，[CodeGate](https://codegate.ai/)。本地托管（即由开发人员在其自己的机器上运行）是他所说的“专注于隐私的解决方案，它作为开发人员生成式AI工作流程中必不可少的安全层”。

## CodeGate的工作原理

具体来说，CodeGate（在[Apache 2](https://opensource.org/license/apache-2-0)许可下授权）充当开发人员和AI编码助手之间的本地代理。该程序在一个专用的[Docker](https://www.docker.com/?utm_content=inline+mention)容器中运行。它确保敏感信息得到保护，同时利用AI的生产力优势。

CodeGate通过监控代码秘密（例如API密钥和凭据）的提示来实现这一点。当您的代码在您的工作站和AI服务之间来回传输时，它会动态加密您的秘密信息。

对隐私的承诺是一个突出的特点。该工具完全在您的本地机器上运行，确保除编码助手所需流量之外，没有任何数据离开您的系统。

该程序还通过使用实时数据库识别潜在有害的库和已弃用的依赖项，并在AI工具建议此类可疑组件时进行干预，从而阻止它们。正如告诉TNS的那样，“每当LLM推荐不安全的依赖项时，它都会提醒开发人员，否则它会在后台静静地运行。”

CodeGate目前支持与流行的AI提供商（如[OpenAI](https://openai.com/)和[Anthropic](https://www.anthropic.com/)）集成，以及GitHub Copilot和[continue.dev](https://www.continue.dev/)等工具。开发人员计划通过包含更多工具来扩展兼容性，例如AI结对编程工具[aider](https://aider.chat/)和AI代码编辑器[Cursor](https://www.cursor.com/)。

随着AI集成的软件开发环境不断发展，像CodeGate这样的工具将在平衡AI辅助的优势与安全和隐私的必要保障方面发挥至关重要的作用。[CodeGate的开源代码库](https://github.com/stacklok/codegate)邀请开发人员社区进行协作和审查，这应该有助于加快改进和广泛采用。

[YOUTUBE.COM/THENEWSTACK 技术发展迅速，不要错过任何一集。订阅我们的YouTube频道，收看我们所有的播客、访谈、演示等等。](https://youtube.com/thenewstack?sub_confirmation=1)