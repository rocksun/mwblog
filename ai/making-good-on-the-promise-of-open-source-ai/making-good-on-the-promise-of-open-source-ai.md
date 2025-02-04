
<!--
title: 开源AI的承诺兑现
cover: https://cdn.thenewstack.io/media/2025/01/64612841-womanizer-toys-8ob43mw658c-unsplash-1.jpg
-->

初创公司Oumi已走出隐身模式，获得1000万美元融资，并推出其高管称之为真正开源的AI平台。

> 译自 [Making Good on the Promise of Open Source AI](https://thenewstack.io/making-good-on-the-promise-of-open-source-ai/)，作者 Jeffrey Burt。

两年多前，[OpenAI](https://openai.com/)发布其[ChatGPT](https://thenewstack.io/openai-launches-new-chatgpt-interface-designed-for-coding/)聊天机器人，开启了生成式AI](https://thenewstack.io/generative-ai-in-2023-genai-tools-became-table-stakes/)时代，此后发展迅速，AI行业似乎一直在试图定义“开放”和“开源”在这一时代中的含义。

AI领域主要由少数几家资金雄厚的大公司及其AI模型和工具主导，例如OpenAI的GPT系列模型、[微软的Copilot](https://thenewstack.io/microsoft-makes-github-copilot-free-in-vs-code/)和[谷歌](https://cloud.google.com/?utm_content=inline+mention)[的Gemini](https://blog.google/technology/ai/google-gemini-ai/)。其他公司，其中[Meta](https://about.meta.com/?utm_content=inline%20mention&utm_source=the%20new%20stack&utm_medium=referral&utm_campaign=tns%20platform)凭借其[Llama模型](https://thenewstack.io/get-started-with-metas-llama-stack-using-conda-and-ollama/)最为引人注目，都吹嘘自己是开放的，尽管一些批评者[质疑它们到底有多开放](https://thenewstack.io/why-open-source-ai-has-no-meaning/)。

然而，除了关于定义的争论之外，缺乏真正广泛使用的开源AI平台正在阻碍行业创新，并[造成令人不安的人才缺口假象](https://thenewstack.io/upskilling-engineering-teams-for-the-ai-era/)，曾在谷歌、微软和Meta等巨头公司从事AI技术工作的[Manos Koukoumidis](https://www.linkedin.com/in/koukoumidis/)表示。

“通常情况下，人们发布开放权重模型，只是模型本身和权重，”Koukoumidis告诉The New Stack。“[人们]不知道它是如何开发的，使用了什么代码，使用了什么数据，他们称之为开源，但这并不是一个非常准确的描述。现实情况是，即使是目前的努力，即使是少数开源的——因为Meta的‘开放权重’——即使是少数开源的，人们也很难进行实验，继续创新并在此工作上相互合作。这是阻碍开源世界进步的事情。”

正是这一点促使Koukoumidis和[Oussama Elachqar](https://www.linkedin.com/in/oussamaelachqar/)——他在微软、苹果和推特（现为X）拥有机器学习经验——启动了[Oumi](https://oumi.ai/)，这是一家今天刚刚走出隐身模式的初创公司，它提供两者都称之为真正开源平台的东西。它还获得了由风险投资公司[Venrock](https://www.venrock.com/)和[Obvious Ventures](https://obvious.com/)领投的1000万美元种子资金。

## AI的Linux

Koukoumidis，同时也是Oumi的首席执行官，表示该平台——与来自11家机构的研究人员合作开发，包括[麻省理工学院](https://www.mit.edu/)（MIT）、[加州大学伯克利分校](https://www.berkeley.edu/)和[卡内基梅隆大学](https://www.cmu.edu/)——基本上充当AI模型和工具的Linux，使研究人员、开发人员和AI专家能够广泛合作和贡献，他们将能够在彼此的工作基础上进行构建。

这不仅会加速创新，还会让这些机构的AI学生能够使用该平台来获得行业急需的技能。它有助于向更多人开放这项关键的先进技术，而不仅仅是目前少数几家权力掮客。

他说：“我们从让其他人能够轻松地进行实验和合作作为关键设计原则开始。如果其他人不容易在彼此的工作基础上进行构建，并且继续在彼此的工作基础上进行构建，那么开源将永远无法实现它所需的增长和速度。”

## 真正开放AI

使AI技术更加开放一直是业界一个棘手的问题。如前所述，像Meta这样的公司正在创建比一些竞争对手更开放的模型。[开源倡议](https://opensource.org/)在经过多年的规划后，于2024年10月[发布](https://thenewstack.io/osi-finalizes-a-humble-first-definition-of-open-source-ai/)了其[开源AI的初步定义](https://opensource.org/?utm_source=the+new+stack&utm_medium=referral&utm_content=inline-mention&utm_campaign=tns+platform)，该定义涉及四种不同类型的数据，并要求构建和赞助AI技术的公司共享他们可以共享的数据，以及模型的参数和用于训练和运行系统的源代码。
随着[自主AI](https://thenewstack.io/the-architects-guide-to-understanding-agentic-ai/)的兴起，[思科](https://www.cisco.com/)和其他厂商正在规划通信网络——他们称之为[“代理互联网”](https://outshift-headless-cms-s3.s3.us-east-2.amazonaws.com/Jan2025_CREA-842_Internet%20of%20Agents%20Whitepaper.pdf)——这将允许来自不同厂商和行业的AI代理自主连接和协作以解决复杂的问题，并强调其需要开源。

## DeepSeek的出现

最近，中国人工智能初创公司[DeepSeek](https://unsloth.ai/blog/deepseek-r1)本月发布了其DeepSeek-R1推理模型，该模型正在搅动人工智能行业，因为它据报道其性能与[OpenAI的o1模型](https://thenewstack.io/openais-realtime-api-takes-a-bow/)相当——该模型可以在给出答案之前进行推理——并且仅用560万美元在两个月内完成训练。它也是开源的，因此人工智能开发人员和研究人员可以合作并在其基础上进行构建。

R1发布后，[英伟达、微软和其他人工智能巨头的股票暴跌](https://abcnews.go.com/Business/nvidia-microsoft-shares-tumble-china-based-ai-app/story?id=118136157)，[DeepSeek将OpenAI](https://www.cnbc.com/2025/01/27/chinas-deepseek-ai-tops-chatgpt-app-store-what-you-should-know.html)从其在苹果App Store上下载量最多的免费应用程序的宝座上挤下。

“DeepSeek的发布不可否认地展示了开源AI的巨大潜力，”安全开发公司[Black Duck](https://www.blackduck.com/)的高级研发经理说。“通过在MIT许可下提供如此强大的模型，它不仅使人们能够获得最先进的技术，而且还促进了全球AI社区的创新和合作。”

然而，这位经理表示，DeepSeek使用OpenAI的思维链数据进行初始训练，这突显了对透明度和共享资源的需求，并补充说，“至关重要的是，底层的训练和评估数据必须是开放的，初始架构和生成的模型权重也必须是开放的。”

## DeepSeek助力开源论证

表示，DeepSeek的成功验证了战略。建立在Meta的Llama和[PyTorch](https://thenewstack.io/why-pytorch-gets-all-the-love/)等其他开源工作之上，使这家中国公司能够进行创新，并创建似乎正在缩小与OpenAI专有模型差距的模型。

DeepSeek建立在Meta的PyTorch和Llama等其他开源工作之上。这些开源工作使DeepSeek团队能够继续创新，并开发出似乎正在缩小与OpenAI专有模型差距的模型。他表示，在一个像这样的平台上，社区可以共同构建下一个DeepSeek。

表示，DeepSeek也应该为美国敲响警钟。

“尽管DeepSeek在数学和编码等领域表现令人印象深刻，但其偏见和审查制度表明了人工智能发展未来的风险，”他说。“为了让美国继续在人工智能领域保持领先地位，我们需要开源和开放合作来开发值得信赖且可解释的模型。如果美国比中国更不开放，美国的研究人员将处于劣势。”

## 沟通与协作

和称之为一个正在推出第一个无条件开源AI平台的人工智能实验室。它提供具有开放代码、开放数据和开放权重的基础模型，并为研究人员和开发人员提供协作和贡献的工具。它是一个统一的平台，可以支持所有常见的基础模型工作流程。

开发人员可以使用SFT、LoRA、QLoRA和DPO等技术来训练各种规模的模型，从1000万到4050亿个参数，获得对PyTorch和其他AI工具的支持，使用文本和多模态模型，如Llama、通义千问（由[阿里云](https://www.alibabacloud.com/en?_p_lc=5)构建的LLM系列）和微软的Phi小型语言模型（SLM）。

他们可以使用vLLM和SGLang等多个推理引擎，通过标准基准评估模型，并在任何环境中运行他们的模型，从他们自己的笔记本电脑到[亚马逊网络服务](https://aws.amazon.com/?utm_content=inline+mention)和[微软Azure](https://azure.microsoft.com/en-us/)的云基础设施，再到谷歌云平台和[Lambda](https://lambdalabs.com/)。此外，开发人员可以将他们的模型与来自OpenAI、[Anthropic](https://www.anthropic.com/)、谷歌的[Vertex AI](https://cloud.google.com/vertex-ai)和其他公司的开放模型或商业API集成。

它还原生支持[Jupyter](https://jupyter.org/)笔记本和Microsoft Visual Studio代码调试。还包括用于各种操作（包括训练后操作）的预构建工作流程和配方。
“当有新项目时，当他们有研究想法时，他们想执行它，”Elachqar告诉The New Stack。“但是，他们必须弄清楚很多事情才能测试这个想法，这个假设。我们为他们提供的是最常见的流程，他们需要微调模型或生成数据或进行推理。我们为他们提供非常可靠的起点，他们可以使用并调整到他们的用例。”


## 押注正确的马

Oumi的创始人表示，该行业向真正的开源发展，远离公司幕后构建的一次性AI模型至关重要。创新将更快地发生，并且将有更多可用的人才可以使用，他们相信生态系统中的参与者——从云提供商到加速器供应商，再到小型公司和研究机构——都希望开源AI能够成功。

Elachqar说，资源最多的公司无法独自解决挑战，并指出他和Koukoumidis与这些供应商多年的经验。开放协作至关重要；否则，AI开发人员将在孤岛中工作，创建与其他人相同的工具，而不是在已完成的工作的基础上进行构建。

这也将保护行业本身。Koukoumidis预计许多公司在未来几年内将崩溃，这些公司正在制作封闭模型。他提到了[Inflection AI](https://inflection.ai/)，这家初创公司直到去年年底还在推出管理人员所说的可能挑战领导者的模型。现在它已经退出了模型构建游戏，转向创建企业可以使用其他人构建的AI模型的工具。

首席执行官说：“比赛中有两匹马。”“有一匹闭源的马说，‘我需要自己做所有事情。我需要自己付出全部努力来开发，我必须承担这样做的全部成本。’然后你有一匹开源的马，很多人都在为它提供资源。他们正在帮助它更快地移动，它正在整合来自所有不同实体的所有贡献——人力和金钱贡献。问题是，你认为哪一个最终会更快、更经济可持续？我们押注第二匹马。”
