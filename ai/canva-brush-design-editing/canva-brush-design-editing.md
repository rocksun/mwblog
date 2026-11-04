<!--
title: Canva的新设计模型不生成图片：它靠写代码来修改设计
cover: https://cdn.thenewstack.io/media/2026/11/dd3198a3-handonmouse.png
summary: Canva推出了全新的视觉语言模型Canva Brush，它不生成图片，而是通过编写和执行代码来理解结构并精准修改设计，展现了垂直领域模型在效率和成本上的独特优势。
-->

Canva推出了全新的视觉语言模型Canva Brush，它不生成图片，而是通过编写和执行代码来理解结构并精准修改设计，展现了垂直领域模型在效率和成本上的独特优势。

> 译自：[Canva’s new design model doesn’t generate images. It writes code to edit them.](https://thenewstack.io/canva-brush-design-editing/)
> 
> 作者：Adrian Bridgwater

澳大利亚图形设计软件公司 [Canva](https://www.canva.com/en_gb/) 上周推出了 [Canva Brush](https://www.canva.com/newsroom/news/canva-brush/)，这是其为设计师打造的全新视觉语言模型。Brush 是一个编辑模型，而不是图像生成器：它是一个[视觉语言模型](https://thenewstack.io/a-developers-guide-to-vision-language-models/)，能够理解设计师项目背后的意图并解释设计修改请求。

Canva 表示，Canva Pro 用户可以使用 Brush，它能够读取设计的内容和结构，编写并执行一小段代码来进行修改，然后检查自身的运行结果。在 Canva 首个内部图像生成模型 [Canva Craft](https://www.canva.com/newsroom/news/canva-craft/)（于 10 月 22 日发布）推出一周后，Canva Brush 便正式登场了。

## 设计很复杂；设计编辑则更为复杂

根据 Canva 的发布博客，生成高质量设计是 AI 模型面临的最大挑战之一，而“现在编辑设计则更为复杂”。这是因为模型需要理解设计师想要更改的内容、设计的结构，以及重要的是，什么需要保持原样。否则，一个简单的编辑请求可能会导致“一堆没人要求的改动”。

在面对诸如“为我的面包店制作一个包含新艺术运动视觉效果和背景的 3 页宣传册”这样的提示词时，智能体必须做出长串的决策。它需要规划跨页面的叙事、生成并放置文本、选择图像，并保持从第一页到最后一页的排版、颜色和间距的一致性。每个决策都与下一个决策息息相关，微小的失误累积起来就会导致设计偏离品牌调性或显得格格不入。

Canva 表示：“这正是我们构建 Brush 旨在解决的挑战。Brush 没有将设计视为一系列孤立的决策，而是能够持续评估和改进其工作，帮助[用户]将一个粗略的草图转化为准备好分享的精致设计。在幕后，它使用了一个智能体循环，通过编写和运行代码来调整设计元素，然后可以检查页面上发生的事情来指导下一步的操作。”

> “在定义明确、特定任务的受限问题上，小型专业模型多年来一直在悄悄击败大型通用模型。”

## 这不是前沿实验室的挑战；它比这更聪明

那么问题来了：来自澳大利亚的艺术和设计专注型 AI 模型实验室，能否在长期内挑战前沿模型巨头在复杂图像设计编辑任务上的地位？

企业 AI 架构师兼 [Besk Tech](https://besk.tech/) 创始人 [Vladimir Beskorovainyi](https://www.linkedin.com/in/vladimirbesk/) 告诉 *The New Stack*，这个问题在隐喻和字面上都“被框错了框架”。

Beskorovainyi 说：“Canva 并不是在挑战前沿模型；事实上，它是在拒绝与它们竞争。一个能够读取设计组装方式（并对其进行编辑）的模型正在解决一个受限问题（一个具有明确参数和有限范围的定义明确的特定任务），而小型专业模型多年来一直在受限问题上悄悄战胜大型通用模型。”

Beskorovainyi 敦促我们超越 Canva Brush 模型的各项能力，转而更直接地关注每次编辑的成本，他认为“[这里的护城河](https://en.wikipedia.org/wiki/Economic_moat)是产出物，而不是权重”，主要是因为 Canva 可以根据真实设计的实际组合方式进行训练。

Beskorovainyi 断言：“前沿实验室可以匹配像 Canva Brush 这样的工具的基础处理能力；训练信号是更难匹配的东西，因为它来自于拥有设计本身。垂直化在任何数据是产品的副产品而不是需要购买的东西的地方都会获胜。这是大多数模型开发者仍然低估的部分。”

## 设计专业知识，加上匿名洞察

Brush 最初使用的是一个未指定的开源权重模型，然后 Canva 使用设计专业知识以及选择帮助改进 Canva AI 的人们的匿名洞察组合，对真实的设计和编辑任务进行了后训练。因此，它不仅了解最终结果的外观，还了解实现该结果所需的步骤。

该公司在公告中指出：“我们将后训练与大规模强化学习相结合，为模型提供了完成整个设计和编辑任务的机会，从成功中学习，并不断塑造其未来的行为。”

> “一次美丽的编辑仍然可能是一项昂贵的校对任务。”

随着业内许多人敦促他们放下 Rotring 笔和 Pantone 色彩指南，转而采用智能体驱动的工具集，营销传播行业的许多人对这些新服务有着切身的体会，他们对设计师的现实需求十分敏感。

[Dr. Rissy’s](https://www.drrissyswriting.com/) 写作与营销公司的创始人 [Dr. Morissa Schwartz](https://www.linkedin.com/in/morissaschwartz/) 告诉 *The New Stack*，多年来她使用过许多自动化工具，虽然尚未用过 Canva Brush，但她很清楚如果使用的话会怎么做。

Schwartz 解释说：“这是我会对其进行的营销和出版测试。当一个‘更改此标题’的命令仍然能让价格、免责声明和布局保持完整时，AI 设计师编辑器就算物有所值了。Canva 的机遇在于使这些细小、频繁的修订变得足够可靠，从而让营销团队花更少的时间去检查还有什么地方发生了变动。”

她指出，她会针对同一个获批的设计，将 Brush 与通用模型进行进一步测试，并衡量非预期更改、可读性以及人工批准所需的时间，而不是去对比图像生成的排名。

Schwartz 补充说：“一次美丽的编辑仍然可能是一项昂贵的校对任务。”

> “前沿模型了解互联网；Canva 知道数以亿计的人实际上是如何在幻灯片演示文稿中进行操作的。在一个垂直领域中，品味和分发渠道胜过参数量。”

## Canva 正在前沿实验室的缝隙中“另辟蹊径”

深科技风险投资工作室 [The Capital Index](https://thecapitalindex.com/) 的联合创始人兼 CTO [Rodion Sorokin](https://www.linkedin.com/in/rodion-sorokin-1a4bb2178/) 告诉 *The New Stack*，他赞同目前所表达的观点，并表示从实际情况来看，“Canva 并不是在试图与前沿实验室硬拼；而是在它们的缝隙中另辟蹊径”。

Sorokin 说：“Brush 从一个开源权重模型开始，并针对 Canva 自己的设计师所称的*优秀设计*进行了强化学习训练，这是一个任何资金充足的垂直领域玩家现在都可以复制的剧本。前沿模型了解互联网；Canva 知道数以亿计的人实际上是如何在幻灯片演示文稿中进行操作的。在一个垂直领域中，品味和分发渠道胜过参数量。”

Sorokin 补充道：“巧妙之处在于 Brush 不画像素：它读取图层、编写小段代码来更改它们并检查自己的工作，这才是设计师编辑的方式，而不是图像生成器猜测的方式。Canva 表示，这使其速度比其上一个设计智能体快高达 69%，每项任务的成本降低了 46%。如果这在发布博客之外也能成立，那么专业模型将凭借单元经济学取胜，而不仅仅是质量：生成将成为商品，而编辑将成为商业。”

## AI 模型基准测试平台排名

据 Canva 称，Craft（而非 Brush）在众包基准测试平台 [Design Arena](https://www.designarena.ai/leaderboard?tab=image) 上首次亮相时排名第四，落后于 OpenAI 专注于精准度的图像生成与编辑模型 [GPT Image 2.5 Sunburst](https://developers.openai.com/api/docs/models/gpt-image-2.5-sunburst)、专注于速度的图像生成模型 [GPT Image 2.5 Flare](https://developers.openai.com/api/docs/models/gpt-image-2.5-flare) 以及 [GPT Image 2](https://developers.openai.com/api/docs/models/gpt-image-2)。Canva 研究部门内部由 160 人组成的 AI 实验室开发了 Canva Craft 和全新的 Canva Brush 模型。Canva 关于 Brush 的速度和成本数据是由该公司自行报告的，并且是将其与公司先前的设计智能体进行对比，而非与前沿模型进行对比。

Canva 表示，Canva Brush 创建的所有内容都是完全可编辑的。从文本、图像到颜色、布局和更精细的细节，每个元素都可供设计师根据自己的喜好进行编辑、操作和重新排列。

该组织还确认，这次发布代表了 Brush 的第一个版本，“未来还会有更多功能”，因为该公司已经在着手开发引用附件的能力、改进 Brush 处理图像繁重布局的方式，以及未来对 Brand Kit 的支持。