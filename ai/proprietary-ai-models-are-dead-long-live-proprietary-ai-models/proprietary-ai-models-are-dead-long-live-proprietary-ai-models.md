# 私有 AI 模型已死，私有 AI 模型万岁

翻译自 [Proprietary AI Models Are Dead. Long Live Proprietary AI Models](https://thenewstack.io/proprietary-ai-models-are-dead-long-live-proprietary-ai-models/)  。

尽管开源模型将占主导地位，但仍有理由需要私有的基础模型。

![](https://cdn.thenewstack.io/media/2023/05/f73aef17-image2-1024x683.jpg)


在过去的几周里，有人宣称[开源生成人工智能模型](https://techcrunch.com/2023/05/11/making-foundation-models-accessible-the-battle-between-closed-source-and-open-source-ai/)将主导该领域。权威人士引用了一份[泄露的谷歌备忘录](https://www.nbcnews.com/tech/tech-news/leaked-google-engineer-memo-warns-big-tech-lose-ai-race-little-guys-rcna83146)，该备忘录称，由于开源模型，这家搜索巨头已经失去了在生成人工智能领域的竞争优势。论点是这样的：

1. 开源机器学习算法已经超出了私有算法的能力。
2. 当使用开源算法在开源数据集上训练[模型](https://roadmap.sh/guides/introduction-to-llms)时，“基础”模型的性能相对于基准非常好。
3. 使用“微调”（将您的数据与开源数据相结合的过程）等技术来构建模型，无需使用大型科技公司的专有数据集。
4. 因此，私有模型已死。

然后是[谷歌 I/O 2023 ](https://io.google/2023/)。 [Google Bard](https://bard.google.com/)  ，一个基于自己的专有数据集的生成式 AI 搜索引擎，[受到好评如潮](https://indianexpress.com/article/technology/artificial-intelligence/10-things-bard-can-do-that-chatgpt-cant-8605341/)。引用最多的功能是它能够将实时数据合并到其模型中。让我们通过分析上面的论点，看看为什么私有模型将在未来发挥有价值的作用：

1. 开源机器学习算法是否超出了私有算法的能力？是的。谷歌的内部备忘录讨论了开源社区算法的性能和创新如何使其自身的发展步伐黯然失色。
2. 当使用开源算法在开源数据集上训练模型时，“基础”模型的性能相对于基准是否良好？当心基准。如果模型的目标只是理解英语，那么使用开源数据语料库就可以了。但是，如果您的模型可以从实时数据中受益，就像用户如何从 Bard 的实时数据搜索中受益一样呢？然后基准测试将需要具有理解英语和理解世界上最近事件的能力。
3. 像“微调”这样的技术来构建模型是否消除了使用大型科技公司数据集的需要？同样，您的用户关心什么？您的私有数据集能否提供您需要的所有实时上下文？
4. 那么私有的基础模型真的死了吗？没那么快。

## 生成式 AI 成功的代价

事实证明，访问实时数据来构建模型是昂贵的。谷歌花费数十亿美元来构建基础设施，以实时索引网络以构建他们的生成模型，你可以打赌这将是私有的。

让我们以两个基于两个不同基础模型构建的航空旅行聊天机器人为例;一个聊天机器人是开源的，另一个是实时数据的私有聊天机器人。旅行聊天机器人使用私有的航班信息数据集进行“微调”，以推荐乘坐哪些航班。在许多情况下，两个聊天机器人将提供相同的答案。但是，如果一场大风暴袭击机场，使用私有实时数据构建的聊天机器人将提供航班信息，避免受风暴影响的航班。这对用户来说是无价的;因此，它对开发人员也很有价值。

## 基础 AI 模型的未来

那么，这是否意味着每个生成式 AI 用例都需要一个基于私有实时数据构建的基础模型？否，但还有其他原因需要私有的基础模型：

1. 私有的第一方数据集。考虑这个例子：Google Bard 利用整个 YouTube 来创建其基础模型。如果您的生成式 AI 用例可以从上传到 YouTube 的大量信息和知识中受益，那么您可能希望使用 Google 的基础模型。
2. 个性化数据集。当使用个性化数据训练基础模型时，该模型（也称为神经网络）将包含个人信息的各个方面。使用这些模型进行推理可以以不泄露个人信息的方式完成，但如果导出[整个模型](https://thenewstack.io/the-next-wave-of-big-data-companies-in-the-age-of-chatgpt/)，则可以通过查看模型的参数来提取特定用户的个人信息。尽管联邦学习取得了进步，但没有一种万无一失的方法可以在不损害隐私的情况下导出模型。

那么未来的基础模型会是什么样子呢？大概是这样的：

1. 算法将是开源的。
2. 在某些情况下，由于维护实时数据集和个性化的成本，数据集将是私有的，而在其他情况下则是开源的。

假设这是流行的架构，次要影响是什么？

1. 希望构建生成式 AI 的企业可能需要依赖大公司的基础模型，这些公司拥有支票簿来维护自己的实时数据基础设施和其他用例的开源基础模型。
2. 企业所依赖的专有数据集也将越来越实时。预计数据将驻留在 NoSQL 实时数据库中，如 Apache Cassandra ，使用 Apache Pulsar 等技术流式传输到功能存储中。
3. 出于实践目的，模型推理可能会发生在 AWS ， Microsoft 和 Google 等基础模型提供商拥有的数据中心。这意味着在人工智能时代，超大规模企业的重要性可能会增加。基于基础开源模型的模型推理可以在客户的数据中心执行。

DataStax（我的雇主）的次要影响也很重要。作为数据管理提供商，我们通过 DataStax Astra DB 在云中提供服务的投资可能会随着生成式 AI 在企业中变得越来越普遍而增长。

虽然我们鼓励和支持使用 [Hugging Face](https://huggingface.co/) 等公司的开源基础模型，但我们也与三大云提供商建立了强大的 AI 合作伙伴关系。最重要的是，我们正在使用社区贡献流程来上游 Cassandra 的功能，例如[向量vector-search-is-coming-to-apache-cassandra/)，以确保公司可以为实时 AI 创建自己的真实数据集。