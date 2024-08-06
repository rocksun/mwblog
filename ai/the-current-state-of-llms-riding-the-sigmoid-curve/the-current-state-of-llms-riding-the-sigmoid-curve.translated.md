# 大型语言模型的现状：沿着 S 型曲线前进

![大型语言模型的现状：沿着 S 型曲线前进的特色图片](https://cdn.thenewstack.io/media/2024/08/e0b6a2da-graph-1024x574.png)

如果你最近一直在关注人工智能领域，你可能已经注意到了一种转变。一年前的无拘无束的乐观情绪已经让位于更加沉稳、现实的展望。作为一名周末大部分时间都沉浸在人工智能代码中，并为 [LangChain](https://python.langchain.com/v0.2/docs/integrations/toolkits/cassandra_database/) 和 [LlamaIndex](https://docs.llamaindex.ai/en/stable/examples/tools/cassandra/) 等项目做出贡献的人，我亲眼目睹了这种转变。

最近，我参加了两个 AI 会议——AI 质量大会和 [AI 工程师世界博览会](https://thenewstack.io/mozilla-llamafile-builders-projects-shine-at-ai-engineers-worlds-fair/)——人们的情绪变化是显而易见的。这感觉像是 [人工智能之旅](https://thenewstack.io/ai/) 的一个重要里程碑，我想分享我对我们身处何处以及我们要去往何处的想法。

## S 型曲线：对人工智能增长的全新视角

还记得我们曾经认为人工智能增长呈指数级增长，准备将我们所有人抛在身后吗？好吧，现实情况并非如此。人工智能社区现在正在采用一种不同的模型：[S 型曲线](https://news.ycombinator.com/item?id=40683845)。这种 S 形曲线表明，在最初的快速增长阶段之后，随着我们遇到自然限制，进展开始趋于平缓。

为什么视角会发生转变？这归结于我们在 [大型语言模型](https://www.datastax.com/guides/what-is-a-large-language-model?utm_medium=byline&utm_source=hackernoon&utm_campaign=LLM&utm_content=sigmoid) 开发中面临的限制。

## 三重威胁：数据、能源和经济

首先是数据可用性。互联网虽然庞大，但高质量数据的数量仍然有限。当然，像 OpenAI 这样的公司正在争先恐后地达成协议，以获取更多数据来训练 GPT-5，但当我们需要 GPT-6 的 10 倍数据时会发生什么？合成数据将有助于弥补一些差距，但这很难解决。

然后是能源和基础设施成本。[训练这些庞大的模型](https://thenewstack.io/nvidia-shaves-up-to-30-off-large-language-model-training-times/) 需要惊人的计算能力。我们谈论的是一排排的 GPU 不断运行，产生的热量足以温暖一个小镇。这不仅昂贵，而且正在达到收益递减的临界点。在某些情况下，资源可用性限制了甚至可能实现的目标。位于田纳西州孟菲斯的 [新的 xAI 数据中心](https://www.bloomberg.com/news/features/2024-07-25/in-memphis-elon-musk-s-xai-supercomputer-stirs-hope-and-concern) 每天需要惊人的 100 万加仑水和 150 兆瓦电力。[研究人员](https://venturebeat.com/ai/new-transformer-architecture-could-enable-powerful-llms-without-gpus/) 和 [初创公司](https://www.theregister.com/2024/06/26/etched_asic_ai/) 正在寻求消除对 GPU 的需求，但这还处于早期阶段。

最后，还有经济可行性的问题。目前，大型前沿模型正在由财力雄厚的云提供商补贴。但随着 LLM 的真实成本变得明朗，我们可能会看到这些 [模型的开发和部署方式](https://thenewstack.io/arrikto-ml-model-deployments-on-kubernetes-can-get-better/) 发生转变。训练一个前沿模型是一个 [数十亿美元的俱乐部](https://www.washingtonpost.com/technology/2024/04/25/microsoft-google-ai-investment-profit-facebook-meta/)，需要英伟达首席执行官黄仁勋的私人手机号码。

## 人工智能信任危机

如果这些限制还不够，我们还面临着所谓的 “[人工智能信任危机](https://simonwillison.net/2024/Jun/27/ai-worlds-fair/#slide.032.jpeg)”。这是 AI 工程师大会上的一个热门话题。问题是什么？从设计上来说，LLM 往往会变得……有创意。这对于创作下一部伟大的美国小说来说很棒，但对于自动化关键业务流程来说却不行。这种脱节是关于人工智能的幻想思维，以及对实施缺乏了解。LLM 是一个概率模型；在某些情况下，它们会迷路。
我亲眼目睹了一些客户的做法：试图通过将大量数据输入 LLM 来替换分析流程，或者更糟糕的是，试图通过让 LLM 无监督地工作来替换整个工作类别。当然，这些想法都没有成功，让发起者感到沮丧，并对新 AI 的能力持负面看法。即使是内部人士也意识到，Transformer 架构 [还不够](https://www.sequoiacap.com/article/new-ideas-for-agi/)，我们正在所有模型中都达到 [GPT4](https://thenewstack.io/openais-gpt-4-can-analyze-visual-images-pass-bar-exam/) 级别的性能。我们距离可信的自动化或每个人最喜欢的流行词 AGI（通用人工智能）只有一到两次突破。

## 进入低谷：来自 Gartner  hype cycle 的证据
如果你想知道我们在 AI 过山车的哪个位置，那就看看 Gartner hype cycle。这个可靠的工具为我们提供了技术成熟度和采用率的直观表示。由于许可原因，我无法嵌入 Gartner AI hype cycle 的图表，但我可以链接到 [演示](https://www.linkedin.com/video/live/urn:li:ugcPost:7222239254624530432/)，Gartner 的人做了很多图形。花几分钟时间看看你最喜欢的最新技术如何排队是值得的。

根据 Gartner 在 AI hype cycle 中所说，基础模型和生成式 AI 正在进入“幻灭的低谷”。不要被这个名字所迷惑——这不是一件坏事。这是任何技术成熟的必要步骤。早期采用者让每个人都兴奋起来，而高级用户发现了许多早期的好处。后期采用者开始比较更成熟的技术，并发现尖锐的边缘，宣称它“全是炒作”（我指的是你，企业）。最终，会有诸如支持合同、架构图以及大量产品之类的东西，使这一切变得更加可靠和安全。啊，启蒙的曙光。

## S 型曲线的希望
现在，在你开始认为一切都黯淡无光之前，请让我向你保证，这个 S 型曲线和“幻灭的低谷”有一些重大的好处。如果你准备相信这个过程，这里有一些让你感到高兴的事情。

**适应时间**——随着变化速度的放缓，组织有机会喘口气，并弄清楚如何有效地使用这些工具。不再需要不断地争先恐后地跟上最新的模型，而最新的模型会使上周的工作过时。这就是让你不会陷入无休止的 POC 并最终交付一些东西的原因。**改进的风险管理**——通过清楚地了解 AI 的能力和局限性，公司可以对在哪里以及如何实施这些技术做出更明智的决策。即使是一点点 AI 也能对你的产品和最终用户的生产力产生惊人的影响。**战略规划机会**——随着炒作的迷雾消散，前进的道路变得更容易看到。公司可以开始规划他们的 AI 战略，对未来的能力有更现实的看法。不久前，人们对解雇整个软件工程团队或所有营销人员有一些疯狂的猜测。AI 会做所有事情，对吧？现在，很明显，AI 是这些职业中的一项新技能，它提高了生产力并增加了新的功能。相应地进行规划。
## 当前的游戏状态：从“哇”到“如何”
那么，这让我们处于什么位置？如果我们看看 Gartner hype cycle，我们会发现，虽然基础模型和 GenAI 正在进入低谷，但其他 AI 技术处于不同的阶段。例如，知识图谱终于从低谷中走了出来，这可能是由于它们在 AI 应用中的有用性而推动的。

关键的要点是什么？AI 不会消失，但它正在进入一个更加衡量、现实的进步阶段。我们正在从“哇”阶段过渡到“如何”阶段：我们如何真正地实施这些技术，以增加真正的价值？在我吸收了我们当前状态之后，我的建议是：放松身心，适应我们今天拥有的东西。如果你正在构建一个聊天机器人，你应该以某种方式提高用户的生产力。否则，你只是在进行更多 AI 研究。

## 展望未来
当我们沿着这个 S 型曲线前进时，我们可以期待什么？我相信我们将迎来一个整合和改进的时期。模型之间的差距正在缩小，许多模型的质量都达到了 GPT-4 级。这对高级用户来说是个好消息，他们现在可以建立在更稳定的基础之上。

我们也可能看到向更专注、更高效的模型转变。 “更大总是更好”的时代即将结束，取而代之的是一种更细致入微的方法，它平衡了能力和效率。
虽然我们可能没有以惊人的速度朝着 AGI 迈进，但我们正在进入一个可能更加令人兴奋的阶段。这是一个实用创新的时代，人工智能对现实世界的影响将开始变得清晰。所以，各位人工智能爱好者，系好安全带。旅程可能比预期更平稳，但远未结束。

[YOUTUBE.COM/THENEWSTACK](https://youtube.com/thenewstack?sub_confirmation=1) 科技发展迅速，不要错过任何一集。订阅我们的 YouTube 频道，观看我们所有的播客、访谈、演示等。