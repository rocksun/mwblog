
<!--
title: 微软看到开发者拥抱“范式转变”迈向 GenAIOps
cover: https://cdn.thenewstack.io/media/2024/10/a92e2bdd-the-blowup-pguirt0m-m0-unsplash-1.jpg
-->

随着组织不断快速采用生成式 AI，他们正在看到从 MLOps 和 LLMOps 框架演进的必要性。微软对此发表了看法。

> 译自 [Microsoft Sees Devs Embracing a ‘Paradigm Shift’ to GenAIOps](https://thenewstack.io/microsoft-sees-devs-embracing-a-paradigm-shift-to-genaiops/)，作者 Jeffrey Burt。

组织和开发者继续努力跟上围绕[生成式 AI (GenAI)](https://thenewstack.io/generative-ai-in-2023-genai-tools-became-table-stakes/) 的前所未有的创新速度，他们希望让新兴技术为他们所用。

在 OpenAI 几乎两年前首次推出其 ChatGPT 聊天机器人后，GenAI 在企业中的快速采用导致需要通过 AI 模型的微调和[检索增强生成](https://thenewstack.io/writer-coms-graph-based-rag-alternative-to-vector-retrieval/) (RAG) 的使用来将技术弯曲到业务的意愿，这是一个允许组织用其企业数据增强[大型语言模型 (LLM)](https://thenewstack.io/llm/) 训练的过程，以便产生的 AI 更准确，更符合他们的需求。

同样，管理、扩展和运营 AI 模型的工具和流程也一直在稳步发展。[用于机器学习环境的 MLOps](https://thenewstack.io/kitops-is-the-open-source-tool-that-turns-devops-pipelines-into-mlops-pipelines/) 演变为 LLMOps 以应对大型语言模型的兴起。

现在出现了 GenAIOps，它已经出现几个月了，并有望成为开发、测试和部署 GenAI 解决方案的首选流程。在最近的一篇博文中，[Yina Arenas](https://www.linkedin.com/in/yinaa/)，微软 AI 核心平台产品副总裁，将从[MLOps 和 LLMOps 到 GenAIOps 的转变称为“范式转变”](https://techcommunity.microsoft.com/t5/ai-ai-platform-blog/the-future-of-ai-the-paradigm-shifts-in-generative-ai-operations/ba-p/4254216)，它更好地涵盖了该技术已成为的样子。

“GenAIOps 扩展到 LLMOps 之外，以解决生成式 AI 操作的全部范围，包括[小型语言模型 (SLM)](https://thenewstack.io/the-rise-of-small-language-models/) 和多模态模型，”Arenas 写道，并指出它包括从实践和工具到基础模型和框架的一切。“这种转变从仅仅管理大型模型转变为确保生成式 AI 应用程序的持续开发、部署、监控和治理。”

她列出了组织在部署和扩展 GenAI 时面临的运营挑战，从输入模型的数据的质量和数量到性能、效率、成本、安全性和合规性。

## 寻找合适的 GenAI 模型

另一个障碍是浏览复杂的 GenAI 模型环境，以找到不仅满足性能需求，而且还能很好地与企业现有基础设施集成的模型。[Nick Patience](https://www.linkedin.com/in/nickpatience/)，分析师公司[The Futurum Group](https://futurumgroup.com/) 的 AI 负责人，将找到合适的模型称为一项艰巨的任务，并补充说“有数千种可供选择，包括商业许可和开源，开源模型环境正在迅速发展。”

“与经典机器学习相比，GenAI 的主要区别之一是，在几乎所有情况下，GenAI 模型都不是由开发人员组织构建的；而是通过 API 获得许可或访问它，或者从开源存储库（如[Hugging Face](https://huggingface.co/)）下载它，”Patience 告诉 The New Stack。“这使得为任务选择合适的模型变得更加重要。将其与使用经典机器学习的更窄的预测模型进行对比，这些模型通常使用组织自己的数据构建和训练。”

许多 LLM 规模庞大，GenAIOps 将为收集、整理、清理和创建适当的数据集以及以特定检查点进行模型的适当测量创建带来更规范的流程，[Andy Thurai](https://www.linkedin.com/in/andythurai/)，[Constellation Research](https://www.constellationr.com/) 的首席分析师，告诉 The New Stack。

“否则，由于多种原因，它会导致混乱，”Thurai 说。“如果模型没有得到适当的训练，这也可能导致巨大的基础设施成本。到目前为止，许多开发人员使用随机技术和程序来创建 ML 模型甚至 LLM。这些定义的流程、技术和程序为这些模型的创建、部署和维护带来了一些秩序。”

## 变革正在进行中

Arenas 的博客是即将发布的一系列文章的开篇，这些文章将深入探讨[微软的 GenAIOps 框架](https://learn.microsoft.com/en-us/azure/machine-learning/prompt-flow/concept-llmops-maturity?view=azureml-api-2)，但她明确表示，GenAI 将改变组织的运营方式及其内部的角色。
“数据团队将成为 AI 洞察力协调者，而 IT 运维将演变为 AI 基础设施专家，”她写道。“软件开发人员将常规地整合 AI 组件，业务分析师将把 AI 功能转化为战略优势。法律团队也将整合 AI 治理，高管将推动 AI 优先战略。”

负责任地创新技术将是关键，并导致建立 AI 伦理委员会和卓越中心，这是 Futurum 的 Patience 也正在看到的。他说，AI 治理将成为 GenAIOps 的一部分，更少关注性能，更多关注其对用户的影响，例如偏差、伦理和隐私等问题。

还有安全问题。GenAI 创造了他所说的新型安全风险，因为开发人员可以控制输入，并且对输出的控制甚至比他们对更狭窄的传统预测模型的控制更少。

“然后是使用微调和检索增强生成等技术带来的更广泛的数据相关挑战，”Patience 说。“GenAIOps 也需要能够处理这些问题。”

## 方向明确

随着企业继续采用该技术，GenAIOps 应运而生。贝恩资本 6 月份的一份报告称，[十家企业中有九家已经部署](https://www.bain.com/about/media-center/press-releases/2024/generative-ai-virtually-ubiquitous-in-global-business-as-the-technology-spreads-at-a-near-unprecedented-rate--bain--company-proprietary-survey/#:~:text=Bain's%20latest%20proprietary%20cross%2Dindustry,rapidly%20across%20all%20use%20cases.) 或正在试点 GenAI 技术，并且在大约 75% 的情况下，它达到了或超出了预期。

该报告的作者写道：“GenAI 现在在全球企业中几乎无处不在，主要公司已对其进行了高度优先的承诺，并且 AI 部署以近乎前所未有的速度传播，以采用一项仍在加速发展的新技术。”

根据市场研究公司 Statista 的数据，全球 GenAI 市场预计今年将超过 360 亿美元，到 [2030 年将达到 3560 亿美元](https://www.statista.com/outlook/tmo/artificial-intelligence/generative-ai/worldwide)，在此期间平均每年增长 46.47%。

Patience 说，他预计企业和开发人员也将越来越多地采用 GenAIOps。

“我认为 GenAIOps 将成为整体应用程序开发过程的关键部分，因为 AI 越来越多地集成到其中，”他说。“GenAIOps 和 MLOps 之间的区别将变得模糊，甚至可能消失，因为开发人员寻求一套通用的工具来处理 AI 模型，无论它们是传统的确定性模型还是概率性模型。”
