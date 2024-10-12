
<!--
title: OSI最终确定了开源人工智能的“谦逊”初步定义
cover: https://cdn.thenewstack.io/media/2024/10/74582bf8-osi-finalizes-a-humble-first-definition-of-open-source-ai.jpg
-->

开源计划的发布候选 1 标识了四类数据，并要求共享数据、源代码和模型参数。

> 译自 [OSI Finalizes a ‘Humble’ First Definition of Open Source AI](https://thenewstack.io/osi-finalizes-a-humble-first-definition-of-open-source-ai/)，作者 Heather Joslyn。

经过近三年的规划，包括社区会议和[长达数月的全球“路演”](https://thenewstack.io/open-source-initiative-hits-the-road-to-define-open-source-ai/)以[收集反馈](https://thenewstack.io/open-source-ai-osi-wrestles-with-a-definition/)，[开源计划 (OSI)](https://opensource.org/) 已发布[其期待已久的开源人工智能定义的候选版本 1](https://opensource.org/deepdive/drafts/the-open-source-ai-definition-1-0-rc1)。

该文件发布于 10 月 2 日，其中包括四种不同类型数据的定义：开放数据、公共数据、可获取数据和不可共享数据。

它还要求带有开源标签的人工智能技术的创建者和赞助者保持透明度，要求这些创建者共享数据（如果可共享），以及用于训练和运行系统的源代码，以及模型的参数。

候选版本 1 中没有的内容：任何解决安全或风险限制的尝试。OSI 执行董事 Stefano Maffulli 告诉 The New Stack，这些问题应该由政府处理。

“世界各国政府对可接受的风险或什么是道德的、可持续的、有价值的有不同的理解框架，”他说。“所有这些词都伴随着取舍。决定它们是什么不是我们的工作。”

他建议，OSI 制定该定义的目标是在定义中为政府留出空间，以便它们能够根据自己的判断采取行动。“我们希望确保该定义不会成为障碍，”Maffulli 说。“否则，它就无法交付，对吧？

## “没有新功能，只有错误修复”

OSI 正在继续收集（在 [hackmd](https://hackmd.io/@opensourceinitiative/osaid-1-0-RC1) 和 [OSI 论坛](https://discuss.opensource.org/) 上）关于候选版本 1 的反馈和[认可](https://opensource.org/deepdive/drafts/the-open-source-ai-definition-1-0-rc1#endorse)，预计将于 10 月 28 日在北卡罗来纳州罗利举行的 [All Things Open](https://www.eventbrite.com/e/all-things-open-2024-tickets-916649672847?discount=NEWS20) 大会上推出。Maffulli 说，在推出之前，可能会有足够的小调整来证明候选版本 2 的合理性。但现在的目的是开始把它包装起来。

“随着今天候选版本周期的开始，起草过程将转移重点：没有新功能，只有错误修复，”[OSI 网站上的一条注释写道](https://discuss.opensource.org/t/the-open-source-ai-definition-v-1-0-rc1-is-available-for-comments/628)。“我们将关注提出的新问题，关注可能需要对文本进行重大修改的重大缺陷。主要重点将放在随附文档、清单和常见问题解答上。”

然而，Maffulli 说，[该定义将是一个正在进行的工作](https://thenewstack.io/why-open-source-ai-has-no-meaning/)：“这是 1.0 版本，但这是一个非常谦逊的 1.0 版本。我们并不是说这是最终版本，我们永远不会再看它，也不要打扰我们——就像，放下麦克风回家一样。

“将会发生的事情是，我们预计 1.0 版本将可以投入使用，这意味着公司、研究机构、学者等、部署者、用户可以将其作为参考，开始解释他们在 [Hugging Face](https://thenewstack.io/how-hugging-face-positions-itself-in-the-open-llm-stack/) 或其他地方发现的内容。他们看到一个模型，现在他们有了一个参考。”

Maffulli 补充说：“我们基本上构建的东西更像是一个宣言，而不是一个实际可用的、用于评估法律文件的 10 点清单定义。我们还处于非常早期的阶段，这就是为什么它是一个谦逊的 1.0 版本。”

## 候选版本 1 中有什么？

“开源意味着让任何人都能够[有意义地分叉（研究和修改）您的系统](https://thenewstack.io/linux-foundation-joins-opentf-to-fork-for-terraform-into-opentofu/)，而无需额外的许可，使其对他们自己和每个人都更有用，”候选版本 1 随附的常见问题解答写道。

根据这一原则，常见问题解答指出，开源人工智能是“一个在条款下以某种方式提供的人工智能系统，该系统授予以下自由：

*   **将**系统用于任何目的，而无需请求许可。
*   **研究**系统的工作原理并检查其组件。
*   **修改**系统以用于任何目的，包括更改其输出。
*   **共享**系统供他人使用，无论是否进行修改，均可用于任何目的。

那么，这个接近最终版本的开源人工智能定义 1.0 版本中有什么？以下是一些关键组件：

### 对透明度的要求

如前所述，OSI 的发布候选版本 1 要求开源 AI 项目创建者共享用于训练系统的数据信息、用于训练和运行系统的完整代码以及模型参数，“例如权重和其他配置设置”。

根据此定义，开源 AI 所需的透明度级别是否会导致某些 AI 项目创建者将其保留为专有？

“我认为这正是将会发生的事情，”Maffulli 说。但他补充说，这[也是开源软件更普遍的现象](https://thenewstack.io/whats-next-for-companies-built-on-open-source/)。“像 [Microsoft](https://news.microsoft.com/?utm_content=inline+mention) 和 [Oracle](https://developer.oracle.com/?utm_content=inline+mention) 这样的公司，他们不会发布其——姑且称之为‘皇冠上的明珠’的源代码，比如 Windows、Microsoft Office 和 Oracle 数据库。

“这些源代码是不可用的。它不透明。但这并不意味着开源就消失了或类似的事情。只是它是生态系统的另一部分，你知道它的存在。”

### 4 种不同的数据类别

该文档的常见问题解答部分将数据分为四类，并指出所有四类数据都可能用于训练语言模型：

* **开放的：**“可以复制、保存、修改和重新共享的数据，”常见问题解答中写道。
* **公共的：**“只要数据仍然可用，其他人就可以查看的数据，”常见问题解答中描述道，并指出“随着链接或引用丢失或从网络可用性中删除，这些数据可能会降级。”
* **可获取的：**“可以获取的数据，包括付费获取的数据。”
* **不可共享的：**“由于可解释的原因（如个人身份信息）而无法共享的数据。”

对于属于“不可共享”类别的数据，实现该技术的“有意义的分支”的目标是指导原则：

“[研究]系统某些偏差的能力需要对数据进行详细描述——它是什么，它是如何收集的，它的特征等等——以便用户能够理解系统背后的偏差和分类。这必须详细披露，例如，医院可以使用自己的患者数据创建具有相同结构的数据集。”

这四种类别反映了 OSI 在其长期研究和社区反馈过程中遇到的一些混乱的现实。

Maffulli 说，当这个过程开始时，人们的冲动是坚持开源 AI 的所有三个要素——数据、代码和参数——都应该是开源的。“

但是，他补充说，“然后你开始更深入地研究，我们发现了两个主要问题。一个是参数本身，参数权重。这些东西是什么？从法律角度来看，不清楚它们上面是否有版权或其他专有权利。所以，好吧，在这个框上打一个大大的问号。”

然后，他说，还有数据：“马上就有一个问题，好吧，所以也许有私人数据，有受版权保护的数据，有医疗数据，还有一些数据是你不能分发的——你可以阅读它并复制一份，但你不能重新分发。”

这提出了一个[难题](https://opensource.org/blog/how-we-passed-the-ai-conundrums)。“为了简化讨论，”Maffulli 说，“我们确定了这四个模块。”

常见问题解答承认，在导致发布候选版本 1 的整个讨论过程中，数据以及围绕数据的透明度一直是一个长期存在的症结所在。

“有些人认为，完全不受限制地访问所有训练数据（不区分其类型）至关重要，他们认为，任何少于此的做法都会损害 AI 系统的完全可重复性、透明度和安全性，”常见问题解答中写道。“这种做法会将开源 AI 降级到只能使用开放数据进行训练的 AI 的一个小众市场……与开源在传统软件生态系统中占据的小众市场相比，这个小众市场将是微不足道的。”

随着数据“变得越来越细化和复杂，”Maffulli 告诉 The New Stack，“最终形式的定义本身就提供了一条逃生路线，”它适应了数据的差异，并允许出现更多开源 AI 项目。

像 [OpenAI](https://thenewstack.io/openais-realtime-api-takes-a-bow/) 这样的大公司和组织，“从技术上讲，做任何他们想做的事情都没有任何障碍。他们在技术上和法律上都没有任何障碍，可以使用这四种数据中的任何一种进行开发训练。”但他说，资源较少、无法与数据提供商建立商业合作伙伴关系的组织处于劣势。

他补充说，“要么开源的定义必须通过排除某些类型的数据来限制开源 AI 的可用性，要么我们需要为公众和整个开源社区提供一种访问[大型语言模型](https://thenewstack.io/llm/)的方式，就像大型公司可以做的那样。而这正是我们正在做的。”

**说明：** 本文已经过修改，与先前版本不同，以便为 Maffulli 关于 OSI 开源定义通过数据类型分类提供“逃生路线”的评论提供更多背景信息。
