<!--
title: GenAI革命呼应上世纪90年代的计算机行业
cover: https://cdn.thenewstack.io/media/2024/01/cbe96ca1-1990s-computers-2-1024x576.jpg
-->

2020年代，GenAI将广泛应用于个人和企业的各个计算领域。AI革命与上世纪90年代的计算机发展存在诸多耐人寻味的相似之处。

> 译自 [How the GenAI Revolution Reminds Us of 1990s Computing](https://thenewstack.io/how-the-genai-revolution-reminds-us-of-1990s-computing/)，作者 Janakiram MSV。

[生成式AI(GenAI)](https://thenewstack.io/ai/)代表了计算机发展的一个重大进步。我们已经看到过去几十年计算机是如何发展的，从大型机(1980年代)到客户端/服务器端(1990年代)再到网页(2000年代)以及云计算和移动设备(2010年代)。它有可能改变计算机的景观。

2020年代，我们将见证几乎每个计算机领域，无论是个人还是企业，都将[渗透生成式AI](https://thenewstack.io/how-generative-ai-can-support-devops-and-sre-workflows/)。

生成式AI的出现标志着一个类似1990年代技术革命的范式转变。让我们来探讨这两个时代之间的相似之处，强调今天的趋势正在塑造计算机的未来。

| 类别 | 1990年代计算 | 当前GenAI时代 |
|-|-|-|
| 芯片 | 基于DEC Alpha、SUN SPARC、Intel x86、Power PC的CPU | 来自NVIDIA、AWS Trainium、Azure Maia、Google TPU的AI加速器 |
| 硬件 | Compaq、[Dell](https://www.delltechnologies.com/en-us/index.htm?utm_content=inline-mention)、HP、[IBM](https://www.ibm.com/?utm_content=inline-mention)和Sun等OEM | [AWS](https://aws.amazon.com/?utm_content=inline-mention)、[Microsoft Azure](https://news.microsoft.com/?utm_content=inline-mention)和Google Cloud等公有云平台 |
| 操作系统 | Windows和Mac等商业OS; Linux等开源OS | [Llama 2](https://thenewstack.io/metas-llama-2-is-not-open-source-and-thats-ok/)等开源基础模型和[GPT-4](https://thenewstack.io/openais-gpt-4-can-analyze-visual-images-pass-bar-exam/)等专有模型 |
| 内置的OS工具和命令 | 与OS捆绑的内在命令和工具 | 基于向量数据库、检索模型和语义搜索的AI工具 |
| Shell | BASH的CLI和Windows与Mac的GUI | AI云平台和模型提供商公开的API |
| 软件应用程序 | 计算器、文字处理器等内置应用程序 | [Google Duet AI](https://thenewstack.io/googles-duet-ai-launches-genai-across-full-sdlc-in-the-cloud/)、[Microsoft Copilot](https://thenewstack.io/microsoft-one-ups-google-with-copilot-stack-for-developers/)、[Amazon Q](https://thenewstack.io/amazon-q-a-genai-to-understand-aws-and-your-business-docs/)等AI助手 |
| 集成开发环境 | Borland Delphi、Visual Studio和Eclipse | 用于构建自定义AI助手的工具,如Microsoft Copilot Studio、[Google Generative AI Studio](https://thenewstack.io/googles-generative-ai-stack-an-in-depth-analysis/)和[Amazon Bedrock](https://thenewstack.io/build-a-qa-application-with-amazon-bedrock-and-amazon-titan/) |

## 从多样的CPU架构到AI加速器

**从前**: 1990年代见证了CPU架构的多样性，DEC Alpha、SUN SPARC和Intel x86主导了市场。

**现在**: 亚马逊、谷歌、微软和英伟达成为GPU和AI加速器芯片的典范。

与1990年代多样的CPU架构相似，AI加速器正成为GenAI工作负载的主力。亚马逊在Trainium和Inferentia芯片上的投资，谷歌对张量处理单元(TPU)的重视，以及微软近期通过[Azure Maia](https://news.microsoft.com/source/features/ai/in-house-chips-silicon-to-service-to-meet-ai-demand/)正式进入这个领域，都证明了这一趋势。预计[OpenAI也将拥有自主研发的芯片](https://www.reuters.com/technology/chatgpt-owner-openai-is-exploring-making-its-own-ai-chips-sources-2023-10-06/)来训练基础模型。

与定制AI硬件一起，负责与其交互的软件层也在发展。尽管NVIDIA的CUDA在这个领域占主导地位，但[AWS Neuron SDK](https://aws.amazon.com/machine-learning/neuron/)、Azure Maia SDK和[ONNX](https://onnx.ai/)正获得越来越多的关注。为了充分利用定制硬件，像[TensorFlow](https://www.tensorflow.org/)、[PyTorch](https://pytorch.org/)和[JAX](https://github.com/google/jax)这样的深度学习框架进行了针对这些层的优化。

定制的AI加速器让我们想起1990年代可用的各种CPU架构。

## OEM动态的转变

**从前**: 传统的原始设备制造商(OEM)像Compaq、Dell、HP、IBM和Sun是硬件强者。

**现在**: 像AWS、Azure和Google Cloud这样的公有云平台已经成为新的OEM。它们在托管和部署AI技术方面起着关键作用。

Compaq、HP、IBM和Sun等OEM在1990年代基于特定CPU架构出货服务器。在当前背景下，公有云提供商可以与OEM相比较。

专有硬件、裸机或虚拟服务器以及定制软件层与某些供应商(如Sun)基于SPARC处理器、Solaris操作系统和运行工作负载所需的其他组件出货端到端堆栈非常相似。

## 从操作系统到基础模型

**从前**: Linux和Windows是核心操作系统，是计算的基础。

**现在**: 基础模型已经成为AI操作系统的内核，有些模型是开源的，有些是专有的。

关于开源和商业软件的争论可以追溯到1990年代，GNU和FOSS的兴起。快进到2024年，[我们仍在讨论开放和封闭基础模型的优缺点](https://thenewstack.io/large-language-models-open-source-llms-in-2023/)。

以Meta带头的[LLaMA](https://research.facebook.com/publications/llama-open-and-efficient-foundation-language-models/)，其他参与者如[Mistral](https://mistral.ai/)也正在获得重要性。另一方面，我们有OpenAI的[GPT-4](https://openai.com/research/gpt-4)，谷歌的Gemini，AWS的Titan LLM，以及一系列其他模型，如Anthropic的[Claude 2](https://www.anthropic.com/index/claude-2)，AI21的[Jurassic 2](https://www.ai21.com/blog/introducing-j2)和Cohere的[Command](https://cohere.com/models/command)。

[大语言模型(LLM)](https://thenewstack.io/what-is-a-large-language-model/)将变得如此重要，以至于它们将被集成到OS内核中，以提供生成式AI功能，甚至操作系统的自我修复。

## 从内置实用程序到AI工具

**从前**: 操作系统配备了必要的实用程序和命令。

**现在**: [向量数据库](https://thenewstack.io/how-large-language-models-fuel-the-rise-of-vector-databases/)、搜索和编排工具构成了AI实用程序的骨干，增强了AI平台的功能和效率。

几乎所有操作系统都内置了实用程序和命令来管理系统。从基本的文件管理到高级优化工具，操作系统都会捆绑这些工具。

与这些实用程序类似，[带有检索器和排名模型的向量数据库](https://thenewstack.io/top-5-vector-database-solutions-for-your-ai-project/)将成为AI栈的一个重要部分。新的AI栈将把它作为一个层，位于LLM之上以影响其响应并通过提示提供上下文输入。高级应用程序(如代理)将使用它们来自动化依赖于存储、搜索和检索的各种任务。

## 从Shell和图形界面到AI平台

**从前**: 由BASH和Zsh驱动的命令行接口，以及内置于Windows和MacOS的复杂图形界面，普及了计算访问。

**现在**: [Hugging Face](https://thenewstack.io/how-hugging-face-positions-itself-in-the-open-llm-stack/)、[Azure ML](https://thenewstack.io/build-and-deploy-a-machine-learning-model-with-azure-ml-service/)、Amazon Bedrock和[Google Vertex AI](https://thenewstack.io/an-introduction-to-google-vertex-ai-automl-training-and-inference/)等AI平台成为新的“操作系统Shell”，使AI技术更易于访问和更用户友好。

AI平台提供商提供的API以与Shell提供OS访问相同的方式提供对基础模型的访问。它们为预训练、微调、版本控制、部署模型和在新的OEM环境(公有云或私有云)中进行推理提供了一个简单的接口。

[低代码和无代码工具](https://thenewstack.io/low-code-vs-no-code/)类似于Windows和macOS中的可用GUI。它们通过使非开发人员和高级用户能够使用基础模型并构建现代应用程序来实现AI的民主化。

## 从软件应用程序到AI助手

**从前**: 软件应用程序由OEM或第三方开发。

**现在**: 像谷歌的Duet AI、亚马逊Q和微软Copilot这样的AI助手是新的应用程序，它们在消费者和企业环境中变得越来越重要。

如果说AI平台是新的Shell，那么AI助手就是新的应用程序。与操作系统提供商内置应用程序的同时还支持开发者创建定制应用程序相似，新的平台内置助手的同时还提供开发环境和工具来构建定制的AI助手。

[Duet AI](https://workspace.google.com/solutions/ai/)与Google工作区集成，而微软则将[Copilot](https://copilot.microsoft.com/)嵌入到几乎所有商业应用程序中。[Amazon Q](https://aws.amazon.com/q/)与AWS管理控制台紧密集成，以使用户能够执行常见任务。

## 开发环境: 从前和现在

**从前**: Borland Delphi、Visual Studio和Eclipse等IDE是软件开发的标准。

**现在**: Microsoft Copilot Studio、Google Generative AI Studio、Amazon Step Functions等环境代表了针对AI和机器学习定制的新一代开发工具。

开发者依赖Visual Studio、Eclipse和XCode等工具来构建自定义应用程序。在GenAI时代，基于云的工具如[Microsoft Copilot Studio](https://www.microsoft.com/en-us/microsoft-copilot/microsoft-copilot-studio)、[Google Generative AI Studio](https://cloud.google.com/generative-ai-studio?hl=en)和[Amazon Bedrock + AWS Step Functions](https://aws.amazon.com/blogs/aws/build-generative-ai-apps-using-aws-step-functions-and-amazon-bedrock/)已成为开发AI助手的首选IDE。它们使开发者能够集成不同的数据源、LLM、提示工程和护栏来构建企业级AI助手。

GenAI时代正在重定义计算格局，反映了1990年代的变革变化，但重点关注AI和云技术。作为领导者，拥抱这些变化并理解其影响对于推动组织在这个计算新时代向前发展至关重要。
