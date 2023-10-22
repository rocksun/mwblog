<!--
# TECH WORKS：工程师应该何时使用生成式AI？
https://cdn.thenewstack.io/media/2023/02/617a689f-techworks_logo-1024x576.png
Image by Diana Gonçalves Osterfeld. 
 -->

制定一个生成式AI政策，以指导工程师应该如何使用ChatGPT、Copilot或者其他聊天机器人，以及不应该如何使用。

译自 [Tech Works: When Should Engineers Use Generative AI?](https://thenewstack.io/tech-works-when-should-engineers-use-generative-ai/) 。

> Tech Works是The New Stack撰稿人Jennifer Riggins的[每月专栏](https://thenewstack.io/tech-works-how-to-fill-the-27-million-ai-engineer-gap/)，探讨了工作环境、管理理念、职业发展和技术工作市场对构建和运行世界所依赖软件的人员的影响。我们欢迎您对未来专栏的反馈和想法。

您的开发人员已经开始使用[生成式AI](https://thenewstack.io/learning-to-love-generative-ai-in-software-development/)工具。您不可能完全禁止他们这么做完全禁止也许不是一个好主意，因为您会希望开发人员保持与技术发展的同步。毕竟，您希望开发人员能聚焦在有意义的工作上，像[亚马逊网络服务](https://aws.amazon.com/?utm_content=inline-mention)的[CodeWhisperer](https://thenewstack.io/developer-tool-integrations-with-ai-the-aws-approach/)和[GitHub的Copilot](https://thenewstack.io/github-copilot-a-powerful-controversial-autocomplete-for-developers/)等[大语言模型(LLM)](https://thenewstack.io/what-is-a-large-language-model/)驱动的[代码补全工具](https://thenewstack.io/top-5-code-completion-services/)具有极大潜力可以[提高开发者的生产力](https://thenewstack.io/how-google-unlocks-and-measures-developer-productivity/)。

但是，如果您没有制定生成式AI的使用政策，您的组织就有受到风险的可能，代码质量和可靠性也可能受到损害。

根据普渡大学研究人员在2022年8月的一项研究，[ChatGPT生成的代码错误率很高](https://arxiv.org/abs/2308.02312)。然而，超过[80%的世界500强企业在ChatGPT上已经拥有账号](https://openai.com/blog/introducing-chatgpt-enterprise)。您的声誉也可能因此受损。就拿三星最近的例子，一名工程师不小心[将内部源代码泄露到ChatGPT上](https://www.forbes.com/sites/siladityaray/2023/05/02/samsung-bans-chatgpt-and-other-chatbots-for-employees-after-sensitive-code-leak/)，导致三星全面禁用生成式AI助手。这可能是一个合理的短期做法，但从长远来看确实缺乏前瞻性。

为了利用[生成式AI](https://thenewstack.io/ai/)的生产力潜力，同时避免公关危机，您的组织迫切需要制定明确的生成式AI使用政策。

在本期Tech Works中，我与一些较早使用生成式AI的工程管理者进行了交谈，以帮助您决定如何鼓励软件工程团队使用生成式AI，以及在哪些情况下应该制止他们使用聊天机器人以避免组织面临隐私与安全风险。

## 消费级与企业级生成式AI工具

目前存在许多生成式AI工具，例如CodeWhisperer、[Google Bard](https://thenewstack.io/googles-generative-ai-stack-an-in-depth-analysis/)、[Meta的AI LLaMA](https://thenewstack.io/why-open-source-developers-are-using-llama-metas-ai-model/)、Copilot和OpenAI的[ChatGPT](https://thenewstack.io/chatgpt-smart-but-not-smart-enough/)等。但目前在工程团队中最受关注的似乎是后面两个。选择哪种生成式AI工具主要取决于用途。

开发者文档平台公司Joggr的联合创始人兼CTO [Zac Rosenbauer](https://www.linkedin.com/in/zacrosenbauer/)对The New Stack表示:“人们只是把问题扔进ChatGPT，希望得到正确的答案。但ChatGPT只是一个OpenAI的研究工具，任何人都可以免费使用。这样做只是在为OpenAI提供免费研究训练数据。”(ChatGPT默认会保存用户的聊天记录，并用这些对话进一步训练其模型。)

Rosenbauer然后向我展示了一系列幻灯片，解释了LLM的工作原理，它更像是通过猜测单词概率来填充文字游戏，而不是努力给出最准确的回复。“这就是为什么它会给出非常愚蠢的答案，”他说，“因为它会尽力回答提问，不管答案对错。”

普渡大学的研究发现，[ChatGPT生成的代码有52%都是错误的](https://arxiv.org/abs/2308.02312)，即使看上去很有说服力。因此，必须明确告知聊天机器人，只在确定知道正确答案时才给出回复。

此外，任何部门的员工都可能会把个人身份信息或企业机密复制粘贴到公开的ChatGPT等工具中，这相当于在[训练它们使用企业的私密数据](https://thenewstack.io/using-chatgpt-for-questions-specific-to-your-company-data/)。

鉴于质量和隐私方面的问题，目前任何团队想从新推出的[ChatGPT Enterprise](https://openai.com/blog/introducing-chatgpt-enterprise)获得竞争优势还为时过早。但是，出于质量和隐私的考量，您应该避免工程师在大部分工作中使用普通版本的ChatGPT。

云架构师首席[James Gornall](https://www.linkedin.com/in/jamesgornall/)说:“我们对任何与我们合作的公司的第一建议就是确保使用正确的生成式AI工具。”他所在的公司CTS专注利用数据分析(包括Google云的[Vertex AI](https://cloud.google.com/vertex-ai)在内)实现Google客户的业务需求。“要区分消费级工具和企业级工具。”

> “现在每个公司都或多或少在使用生成式AI工具，员工可能正在使用您不知道的工具。”
> 
> —— CTS的James Gornall

尽管ChatGPT最受欢迎，但它主要面向消费者。务必提醒您的团队：免费不等于没有成本。这意味着切忌将私人信息输入面向消费者的工具。

“企业不应该将Bard或ChatGPT作为策略工具使用。” Gornall告诉The New Stack。消费级的免费工具个人使用可能没什么大碍，“但一旦您开始询问与企业业务、战略或内容相关的问题”(包括代码)，“您就应该使用更加封闭安全的企业工具。”

更多时候，生成式AI的效果来源于特定领域的数据。您需要企业内部的开发者聊天机器人，使用内部策略和流程进行训练，而不是面向全世界。

“现在每家公司在某种程度上都可称得上是‘生成式AI公司’，不管您是否喜欢。员工可能已经开始在这些工具中提问，因为太容易获取了。” Gornall说。

“甚至不需要企业账号，任何人都可以在ChatGPT上注册并询问问题，比如‘帮我审核这个合同’或者像三星的例子‘检查这个代码’，这很容易造成严重后果。”

保持在组织边界内不仅可以提高隐私和安全性，还可以提升应用速度。

> GenAI “可以节省大量时间；例如，生成文档或生成注释——这些开发人员通常不喜欢做的事情。但在其他时候，我们尝试使用这项技术，实际上却会花费两倍的时间，因为现在我们必须仔细检查它生成的所有内容。”
> 
> —— Datasaur的Ivan Lee

Datasaur的副总裁兼工程主管Karol Danutama建议，对于标准化程度较高、很多公司可能需要类似功能的内容，可以更安全地使用LLM生成代码建议。但切忌使用消费级生成式AI工具处理机密或核心业务内容。 

当然，还要考虑道德选择。Gornall说，企业级AI策略必须覆盖解释性、可重复性和透明度等方面，并以所有利益相关者(包括客户)都可以理解的方式进行。

* Tech Works: [如何填补2700万AI工程师空缺](https://yylives.cc/2023/08/27/tech-works-how-to-fill-the-27-million-ai-engineer-gap/)

## 上下文是开发者效率的关键

如果使用针对企业内部策略和文档进行训练的LLM，那么总体来说可以获得更高的准确性和应用速度。上下文相关的聊天机器人需要与人类内容创作者进行交互，帮助加速或省去开发者工作中枯燥的部分。生成式AI的早期工程应用包括:

- 生成代码段
- 生成文档和代码示例
- 创建函数
- 导入库
- 创建类
- 生成线框
- 运行质量和安全扫描
- 总结代码

这样可以“真正省去键入对开发者意义不大的代码前的大量背景工作，这需要开发者输入很多字符。” Gornall说。仍需要手动检查其相关性和准确性。“但可以获取一些指导和想法来构建一些真实有效的代码。”

对于编码，它生成的想法可能适合也可能不适合直接投产，但生成式AI可以帮助思考如何解决问题。只要使用内部的生成式AI工具，就可以将编码标准、编程风格、策略文档和指南模板提供给聊天机器人。它会将这些内容与外部训练的持续改进相结合，但会将提示和响应保密。

Gornall说：“您可以在很短时间内扫描整个代码库，‘找到任何不符合此标准的内容’或者‘查找任何使用要废弃的内容的代码’。”

但是他建议不要完全封闭数据集，仍需要继续在第三方数据上进行训练，否则就会在模型中造成“回音室”效应，它只会给出错误的答案。适当结合两者，可以保持控制并降低风险。

## 生成式AI用于文档

最需要提升效率的功能之一是[文档](https://thenewstack.io/documentation-is-more-than-your-thinnest-viable-platform/)。内部文档对自助服务至关重要，但通常过时(如果存在的话)，难以找到和搜索。

此外，文档通常和软件开发工作流程脱钩，导致更多上下文切换和流程中断，去外部Wiki或类似Confluence、Notion等平台查阅。

“如果您了解开发人员，他们通常会忽略不在自己日常工作流程和IDE中的内容。” Rosenbauer说。

这使文档非常适合内部生成式AI应用。

“我们发现近年来[开发者效率](https://thenewstack.io/can-devex-metrics-drive-developer-productivity/)有所下降，因为要求他们做的事情太多。” Rosenbauer说，“相比我觉得10到15年前，现在开发者的认知负荷大得多，尽管有更多工具化。” 

> “生成式AI没有提高工程师的核心工作能力，但可以消除很多无价值的干扰和时间消耗。”
>
> —— CTS的James Gornall

他回想了自己和Joggr联合创始人兼弟弟[Seth Rosenbauer](https://www.linkedin.com/in/sethrosenbauer/)为什么在一年多前决定离开工程团队负责人的工作。

例如，Zak Rosenbauer指出，“尽管[DevOps](https://thenewstack.io/devops/)初衷是好的，但对许多非DevOps工程师来说，它增加了很多痛点。[’左移’方法论](https://thenewstack.io/the-great-shift-left-what-changes-for-developers-and-security-teams/)本质上很重要——我认为这是一种增强——但它也强制人们做此前不做的工作。”

因此，Rosenbauer兄弟在接下来的六个月里探索了导致开发者生产力降低和认知负荷增加的原因。他们意识到，内部文档的缺失或不足是一个重要因素。

于是，他们创建了Joggr，这是一个生成式AI工具，可以“重新生成内容”，Zac Rosenbauer说。公司的一个重点是自动重新生成代码段落以维护文档、描述、文本部分、代码链接等。目前约三分之一的Joggr客户来自[平台工程](https://thenewstack.io/platform-engineering/)领域，预计这一比例会增长。

## 生成式AI会抢走工作岗位吗?

Gornall说:“我们经常被问到它[是否会抢走工作](https://thenewstack.io/how-will-generative-ai-change-the-tech-job-market/)。我不这么认为。我认为它正在改变人们的工作，人们需要学习如何与其互动并获得最大利益，但我认为这仍处于非常早期阶段。”

“生成式AI没有提高工程师的核心工作能力，而是消除了许多无关价值的时间浪费。”

生成式AI的开发和采用速度不太可能放慢，所以您的组织需要尽快制定生成式AI使用政策。它还必须包括培训工程师如何使用的计划。

就像他这一代通过谷歌和StackOverflow学习搜索引擎的使用一样，Datasaur的CEO兼创始人[Ivan Lee](https://www.linkedin.com/in/iylee/)认为，下一代计算机科学毕业生会询问ChatGPT或Copilot。团队中的每个人都需要提高对生成式AI的认识。不要忘记，识别他人代码中的缺陷一直是工程工作的一个关键部分——现在也需要将这项技能应用到机器生成的代码上。

Lee补充说：“我们需要非常小心，了解如何进行审查，理解这项技术的优势和劣势。”