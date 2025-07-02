<!--
title: 为何AI应用不应从模型开始
cover: https://cdn.thenewstack.io/media/2025/06/a1e5326e-evaluating_ai_models.jpg
summary: 开发者通常从前沿模型入手，但成本高昂。随后转向较小的开放权重模型，牺牲准确性换取成本优势。评估AI应用应侧重于构建基础评估，而非直接选择模型。不应过早绑定特定模型，需构建代码以便灵活更换，并关注推理成本、性能和安全功能。
-->

开发者通常从前沿模型入手，但成本高昂。随后转向较小的开放权重模型，牺牲准确性换取成本优势。评估AI应用应侧重于构建基础评估，而非直接选择模型。不应过早绑定特定模型，需构建代码以便灵活更换，并关注推理成本、性能和安全功能。

> 译自：[Why the Model Is the Wrong Starting Point for AI Apps](https://thenewstack.io/why-the-model-is-the-wrong-starting-point-for-ai-apps/)
> 
> 作者：Loraine Lawson

在选择模型时，开发者通常从前沿模型入手，也就是尖端的大型语言模型，例如 OpenAI 的 GPT-4、Google 的 Gemini Ultra 和 Anthropic 的 Claude 3 系列。

但前沿模型很快就会变得成本高昂。据 Forrester 首席分析师 [Rowan Curran](https://www.forrester.com/analyst-bio/rowan-curran/BIO4966) 称，这时开发者往往会寻找较小的模型，这些模型可能会牺牲一些准确性来换取成本上的优势。Curran 的研究重点是人工智能、机器学习和数据科学。

他解释说，在了解了大型前沿模型能做什么之后，开发者对问题以及自身对风险的承受程度有了更深入的理解。这时他们会转向一个或多个较小的、开放权重的模型。[开放权重模型](https://www.ntia.gov/programs-and-initiatives/artificial-intelligence/open-model-weights-report/background)是指经过训练的参数（又称权重）可以公开访问，通常可以下载。

但这不一定是一对一的映射。Curran 举例说，这些模型的准确率可能达到 85%，但运行成本只有 20%。

“我们也开始看到这种转变，人们开始分解问题：从如何只使用一个模型来解决所有问题，到如何真正围绕相对便宜的模型进行优化，”他说。“在达到应用程序的 v2 版本并了解 v1 的实际结果之前，你无法真正做到这一点。”

他补充说，这也是你经常看到 AI 应用提供点赞/点踩选项来为结果提供反馈的原因之一：它可以帮助公司了解哪些有效，从而更好地微调其产品。

## AI 应用的评估和其他注意事项

当你试图决定为你的应用程序使用哪个模型时，你的第一步可能根本不应该是模型。Thesys 首席执行官 [Rabi Shanker Guha](https://www.linkedin.com/in/rabisg/) 建议，你应该更多地关注构建一个[基础评估](https://thenewstack.io/where-ai-benchmarks-fall-short-and-how-to-evaluate-models-instead/)，而不是选择一个模型。

[Thesys 是一家生成式用户界面 (GenUI)](https://thenewstack.io/generative-ui-for-devs-more-than-ai-assisted-design/) 公司，专门从事 AI 驱动的界面。当 Guha 和他的联合创始人（设计师 Parikshit Deshmukh）刚开始时，他们首先进行了一次评估——或者在 AI 中通常简称为 eval。

> “……人们开始分解问题：从如何只使用一个模型来解决所有问题，到如何真正围绕相对便宜的模型进行优化。”
> 
> **— Rowan Curran, Forrester 首席分析师**

“我们做的第一件事是，我们提出了一个评估这些模型的基础评估，”Guha 说。

对于他们的评估，他们跟踪了一个 Web 开发领域 LLM 基准测试和一个名为 [τ-benc (tau-bench)](https://arxiv.org/abs/2406.12045) 的基准测试。

“理想情况下，我们需要一个在这两件事上都得分足够高的模型，并且基于此，我们有了这些评估，”Guha 解释说。“所以我们实际上并没有测试数百个模型，而是基于现有的两个基准测试加上我们自己的基准测试，测试了前五个顶级模型。”

通过使用这些基准测试，以及用人眼来衡量 UI 的实际输出，他们能够将选择范围缩小到两到三个模型，然后他们开始进行实验。

IT 咨询公司 Everest Group 的实践主管 [Abhishek Sengupta](https://www.linkedin.com/in/abhisheksengupta88/?originalSubdomain=in) 警告说，开发者应该考虑的不仅仅是模型。

Sengupta 建议说：“用于训练模型的数据集、推理成本、针对相关测试用例的性能以及安全功能是一些需要牢记的标准。”

## 不要把自己嫁给一个 AI 模型

前端托管公司 Vercel 的开发者体验负责人 [Lee Robinson](https://www.linkedin.com/in/leeerob/) 说，随着新模型似乎每周都在推出，而且价格持续下降，开发者明智的做法是不要太快地将自己与一个模型或公司联系起来。

“不要对一个特定的模型过于依恋。让你可以轻松地在模型之间移动，然后在尝试不同模型时进行[验证和测试](https://thenewstack.io/test-driven-development-with-llms-never-trust-always-verify/)，”Robinson 建议说。“你希望在它们之间有一个抽象层，这样你就可以轻松移动，因为几乎可以肯定的是，在很短的时间内就会出现更新、更好的模型。”

他继续说，这意味着确保你以正确的方式构建代码，以便你可以根据需要更换模型。

越来越多地，迎合 AI 开发工作的公司正在为开发者提供轻松切换模型并尝试哪些有效的方法的机会。例如，Robinson 指出 [Vercel 提供了一个 AI SDK](https://thenewstack.io/vercels-next-big-thing-ai-sdk-and-accelerator-for-devs/)，它允许你用一行代码更改 AI 模型。就在上周，Vercel 推出了 [AI Gateway](https://thenewstack.io/frontend-ai-vercel-abstracts-model-chaos-in-one-interface/)，它抽象掉了切换模型的麻烦，让开发者可以访问大约 100 个模型，而无需担心 API 密钥、提供商帐户或速率限制。

类似地，[SAP 今年使其企业开发者更容易使用不同的模型](https://thenewstack.io/sap-unveils-new-ai-tools-for-developers/)，通过添加一个抽象层来确保 AI 模型的安全性、伦理、数据隐私和保护。

SAP 商业技术平台总裁 [Michael Ameling](https://www.linkedin.com/in/michael-ameling/?originalSubdomain=de) 告诉 The New Stack：“无论是 OpenAI、Mistral 还是 Anthropic，我们可以灵活地根据应用程序的需求来使用这些大型语言模型，因为它们在成本、准确性、性能以及最佳用例方面都有所不同。”“我们可以根据应用程序中的用例来使用不同的模型。”