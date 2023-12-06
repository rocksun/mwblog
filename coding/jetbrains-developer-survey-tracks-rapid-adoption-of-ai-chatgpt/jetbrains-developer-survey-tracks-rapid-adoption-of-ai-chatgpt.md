<!--
title: JetBrains开发者人工智能应用调查
cover: https://cdn.thenewstack.io/media/2023/12/e9afcd47-jetbrains-dev-survey-1-1024x576.jpg
-->

据 JetBrains 的一项新调查，四分之三的开发人员使用 ChatGPT，近一半使用 GitHub Copilot。但很少有开发人员认为生成式 AI 会接管所有编码任务。

> 译自 [JetBrains Developer Survey Tracks Rapid Adoption of AI](https://thenewstack.io/jetbrains-developer-survey-tracks-rapid-adoption-of-ai-chatgpt/)，作者 Lawrence E Hecht 几乎为期25年的时间里一直在为企业IT B2B市场和技术政策问题生成可操作的见解和报告。他经常与客户合作开发和分析有关开源生态系统的研究。除了他的咨询工作之外，...

近一年来，ChatGPT-3的推出在开发者社区中引发了广泛的[兴奋](https://thenewstack.io/the-next-wave-of-big-data-companies-in-the-age-of-chatgpt/)和[担忧](https://thenewstack.io/chatgpt-smart-but-not-smart-enough/)，[根据JetBrains的最新开发者调查](https://www.jetbrains.com/lp/devecosystem-2023/)，超过四分之三的开发者正在使用这一[生成式AI](https://thenewstack.io/ai/)工具。

调查报告显示，77%的开发者使用[OpenAI的ChatGPT](https://openai.com/chatgpt)，46%的开发者使用[GitHub Copilot](https://thenewstack.io/github-copilot-a-powerful-controversial-autocomplete-for-developers/)。

6月StackOverflow开发者调查的发现与此相呼应，其中显示[70%的开发者正在使用或计划使用AI来完成他们的工作](https://thenewstack.io/70-percent-of-developers-using-or-will-use-ai-says-stack-overflow-survey/)。

这份JetBrains调查基于来自196个国家和地区的26，348名开发者的反馈。它不仅深入研究了开发者使用的工具以及他们的使用方式，还研究了编程语言、工作行为、薪资、人口统计数据，甚至开发者的心理健康和生活方式。

## 语言: Rust 和 Python 

与往年一样，原始数据发布时，The New Stack 将进行额外分析。与此同时，这里有更多重要发现，包括Python Web框架和基础设施供应工具的使用率正在下降。

- **与2021年相比，使用Python进行Web开发更少见。**
- 47%的Python开发者将其用于数据分析，其次是42%用于机器学习，37%用于Web开发。虽然Python开发者中的数据分析和机器学习使用略有增加，但[Web开发](https://thenewstack.io/python-and-webassembly-elevating-performance-for-web-apps/)从2021年的49%下降。
- 这种下降部分是因为较老的框架失去了用户。在Python开发者中，[Django](https://thenewstack.io/djangos-place-in-a-web-development-world-ruled-by-react/)的使用率从2021年的45%下降到2023年的40%，而Flask的采用率从46%下降到38%。
- FastAPI是一个专门用于用Python构建API的框架，似乎正在获得市场份额，而Django和Flask则在下降。在Python开发者中，FastAPI的采用率从2021年的14%上升到2023年的25%。

- **Rust用户没有跳上WebAssembly的潮流。**
- 根据[2023年WebAssembly状态报告](https://thenewstack.io/whos-leading-webassembly-adoption-so-far-vendors/)，69%的[WebAssembly(Wasm)](https://thenewstack.io/webassembly/)开发者在其应用程序中使用Rust。然而，这并不意味着他们会自动开始使用Wasm。虽然JetBrains调查中的20%的Rust开发者将Wasm作为其Rust应用程序的目标平台，[但这个比例比去年的22%有所下降](https://thenewstack.io/developers-most-likely-to-learn-go-and-rust-in-2023-survey-says/)，远低于2019年报告的36%。我们[两年前](https://thenewstack.io/fewer-rust-developers-target-webassembly/)第一次报道了这一现象。
- JetBrains调查中[Rust](https://thenewstack.io/the-case-for-rust-as-the-future-of-javascript-infrastructure/)的增长仅有增量，从2022年的9%上升到2023年的10%。这比最新[StackOverflow研究](https://thenewstack.io/70-percent-of-developers-using-or-will-use-ai-says-stack-overflow-survey/)报告的40%增长要慢。随着Rust走出早期使用者，使用它的开发者似乎较少将其用于某些人认为是下一代技术的地方。
- 35%的Rust用户没有用它来替换另一种语言。在那些迁移的人中，35%是从C++迁移过来的。

![](https://cdn.thenewstack.io/media/2023/11/47636901-rust-migration-1024x490.png)

*来源:JetBrains开发者生态系统调查2023*

## 职业倦怠、时间管理和注意力集中度

调查跟踪了开发者的福祉以及他们在工作中度过的时间。主要发现包括:

- 超过一半(53%)的受访者在[会议和工作相关的聊天](https://thenewstack.io/tech-works-how-can-we-break-our-obsession-with-meetings/)中花费了超过20%的时间。对于那些参与管理或协作开发的人来说，这可能不是一个问题，但期望初级开发者花更多时间编写代码。
- 无论年龄或角色如何，57%的受访者表示他们超过一半的时间用于与代码相关的活动。
- 62%的调查参与者表示，他们经常或一直处于高度集中注意力的状态，使他们无法注意周围发生的事情和时间的流逝。
- 47%的人使用自我监测应用或设备来跟踪他们的身体活动、睡眠质量和其他健康参数。不幸的是，这项研究没有问后续问题关于这些应用程序的有效性。

## 远程开发

调查还询问了关于远程开发实践的问题:

- 略少于一半(49%)的受访者编辑过远程机器上的代码，比2022年的53%有所下降。
- 在那些进行过远程开发的人中，30%[使用云开发环境(CDE)](https://thenewstack.io/are-cloud-based-ides-the-future-of-software-engineering/)，比2022年的25%有所增加。
- GitHub Codespaces是最广泛使用的CDE，被42%的受访者引用。 29%的受访者使用JetBrains Space的份额可能高估了更广泛市场中的采用率，因为JetBrains用户完成调查的意愿可能较高。

![](https://cdn.thenewstack.io/media/2023/11/c3657680-cdes-used-1024x616.png)

*来源:JetBrains开发者生态系统调查2023*

## AI帮助开发者

存在一种共识，AI永远不会完全接管编写代码的工作：只有13%的开发者这样认为。其他主要发现包括:

- 总的来说，60%的受访者认为[AI编码工具将从根本上改变就业市场](https://thenewstack.io/how-will-generative-ai-change-the-tech-job-market/)，主要是向好的方向。事实上，51%的人相信AI驱动的代码生成将增加对专业软件开发者的需求。
- 如果有机会的话，56%的受访者会让AI助手编写代码注释和文档。相比之下，只有17%的人会将代码编写的任务交给AI助手。

![](https://cdn.thenewstack.io/media/2023/11/8b0f1cde-delegation-of-activities-to-ai-assistant-1024x875.png)

*来源:JetBrains开发者生态系统调查2023*

## DevOps: 基础设施工具使用率下降

- 总体而言，11%的受访者担任[DevOps](https://thenewstack.io/devops/)工程师/基础设施开发者角色。在这些专业人士中，2023年使用[Terraform](https://thenewstack.io/navigating-the-future-of-terraform-and-opentofu/)的比例为33%，而2022年为37%。
- 用于供应基础设施的配置管理工具的使用也出现了明显的下降。
- 与此同时，30%的DevOps受访群体表示他们不使用任何基础设施供应工具。

![](https://yylives.cc/wp-content/uploads/2023/12/terraform-use.jpg)

