<!--
title: AWS 打造智能体AI实验沙盒
cover: https://cdn.thenewstack.io/media/2026/02/523d346e-puzzle-creative-lvkafmpkwry-unsplash-scaled.jpg
summary: AWS 推出 Strands Labs，作为其实验性智能体AI项目的沙盒。该平台旨在隔离前沿研究，避免影响生产级SDK的稳定性。首批项目包括AI Functions（自然语言生成代码）和Strands Robots（连接LLM与硬件）。此举反映了AI智能体框架日益增长的行业投入。
-->

AWS 推出 Strands Labs，作为其实验性智能体AI项目的沙盒。该平台旨在隔离前沿研究，避免影响生产级SDK的稳定性。首批项目包括AI Functions（自然语言生成代码）和Strands Robots（连接LLM与硬件）。此举反映了AI智能体框架日益增长的行业投入。

> 译自：[AWS creates a sandbox for its agent experiments](https://thenewstack.io/aws-strands-labs-launch/)
> 
> 作者：Frederic Lardinois

[亚马逊网络服务](https://aws.amazon.com/?utm_content=inline+mention) (AWS) 正在 [推出](https://aws.amazon.com/blogs/opensource/introducing-strands-labs-get-hands-on-today-with-state-of-the-art-experimental-approaches-to-agentic-development/) [一个专门的 GitHub 组织](https://github.com/strands-labs)，用于其最具实验性的智能体 AI 工作。

周一，该公司推出了 Strands Labs，亚马逊的各个团队将在其中发布尚未准备好纳入该公司生产级 Strands Agents SDK 的前沿项目。

初始版本包括两个项目：AI Functions（AI 函数），它根据自然语言规范在运行时生成代码；以及 Strands Robots（Strands 机器人），它通过视觉-语言-动作 (VLA) 模型将大型语言模型连接到物理硬件。

## 为什么要一个独立的组织？

据 AWS 高级首席工程师 Clare Liguori 介绍，Strands Agents SDK 于 2025 年 5 月首次由 AWS 开源，至今已被下载 1400 万次。Clare Liguori 负责 Strands 和 Kiro AI 编码助手的开发工作。该 SDK 现在支持 Python 和 TypeScript，AWS 内部将其用于生产工作负载。

正是这种吸引力让 Liguori 的团队觉得需要在稳定的 SDK 发布版本和更具实验性的工作之间划清界限。Liguori 告诉 *The New Stack*：“我们希望确保 SDK 继续专注于生产就绪的解决方案。”

> “我们希望确保 SDK 继续专注于生产就绪的解决方案……[Strands Labs] 为亚马逊内部团队和更广泛的 Strands 社区提供了一个迭代的场所……”

她补充说，Strands Labs 为亚马逊内部团队和更广泛的 Strands 社区提供了一个迭代想法的场所，在那里“接口可能会发生很大变化”，而不会破坏核心 SDK 的 API 表面稳定性。

因此，尽管所有 Strands Labs 项目都将附带文档、功能代码和基本测试，但用户应该预料到会有重大变更。

甚至在 Strands Labs 推出之前，AWS 就已经将一些实验推入了 Strands SDK，但正如 Liguori 承认的那样，如今这些实验很可能会首先进入 Strands Labs。其中之一就是控制智能体的实验。

## AI Functions：提示而非代码

对于开发人员来说，这两个当前实验中最有趣的大概是 AI Functions。它允许开发人员用自然语言定义 Python 函数应该做什么，同时还有作为防护栏的先决条件和后置条件。在运行时，一个编码智能体随后生成实现。

由于智能体并非总是完美的，内置的确定性防护栏应确保如果输出不正确，智能体会自我纠正并再次尝试。

Liguori 以收据解析器为例。收据格式千差万别，使得确定性代码变得脆弱。使用 AI Functions，开发人员指定函数必须返回供应商名称、总价和行项目，智能体则处理边缘情况。

这里重要的是，从程序的角度来看，这看起来就像任何其他函数。“它不是一个独立的智能体，”Liguori 说。“它是一个嵌入在其他确定性逻辑中的普通函数。”

```py
@ai_function(
    code_execution_mode="local",
    code_executor_additional_imports=["pandas.*"],
)
def fuzzy_merge_products(invoice: DataFrame) -> DataFrame:
    """
    Find product names that denote different versions of the same product, normalize them
    by removing version suffixes and unifying spelling variants, update the product names
    with the normalized names, and return a DataFrame with the same structure
    (same columns and rows).
    """

    # Load a JSON (the agent has to inspect the JSON to understand how to map it to a DataFrame)
    df = import_invoice('data/invoice.json')
    print("Invoice total:", df['price'].sum())

    # Load a SQLite database. The agent will dynamically check the schema and generate
    # the necessary queries to read it and convert it to the desired format)
    df = import_invoice('data/invoice.sqlite3')
    # Merge revisions of the same product
    df = fuzzy_merge_products(df)
```

从长远来看，团队将 AI Functions 视为通往反馈循环的途径：在生产环境中运行智能体函数数百万次，观察出现哪些代码路径，并最终将结果合并回不再需要模型调用的确定性代码。

Strands 团队一直强调的一点是，他们相信模型只会变得更好，因此智能体框架应尽可能地不碍事。在许多方面，AI Functions 也是朝着这个方向推动的，它专注于模型根据需要编写代码的能力。

## 云端推理机器人

Strands Robots 解决了一个非常不同的问题。它将运行在本地硬件上的轻量级、低延迟 VLA 模型与云端的前沿 LLM 配对。毕竟，前沿模型计算量太大，无法直接在机械臂上运行。但为了让机器人高效工作，需要尽可能降低延迟。

AWS 正在与 Nvidia 和 Hugging Face 合作开展该项目，团队还发布了一个模拟环境，以便开发人员无需物理机器人即可进行迭代。

Liguori 表示，团队一直在与 AWS 客户进行概念验证工作，她指出亚马逊本身显然运行着庞大的仓库机器人群。但她也看到了车载 AI 等应用，以及其他需要领域特定本地推理和现代 LLM 提供的长期规划能力的边缘场景。

## 无处不在的智能体框架

AWS 显然不是唯一一个在智能体框架上大力投资的超大规模服务商 ([这有其原因](https://thenewstack.io/agent-framework-container-wars/))。Google 的 [开源智能体开发工具包](https://google.github.io/adk-docs/)（在 Cloud Next 2025 上宣布）旨在实现多智能体编排。Microsoft 的 [智能体框架](https://learn.microsoft.com/en-us/agent-framework/overview/?pivots=programming-language-csharp)（少数支持 .NET 的智能体框架之一）最近 [达到了](https://devblogs.microsoft.com/foundry/microsoft-agent-framework-reaches-release-candidate/) 候选发布版本状态。CrewAI、LangGraph 等初创公司也已成为该领域的主要参与者，个人智能体也因 [OpenClaw](https://thenewstack.io/deno-sandbox-security-secrets/) 的炒作而兴起。