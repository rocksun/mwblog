## Copilot Enterprise 引入搜索和自定义最佳实践

![Copilot Enterprise 引入搜索和自定义最佳实践的特色图片](https://cdn.thenewstack.io/media/2024/02/31891c9f-copilotmascot-1024x538.png)

[GitHub Copilot Enterprise](https://github.blog/2024-02-27-github-copilot-enterprise-is-now-generally-available/) 已退出测试版，并进入通用版本，其中包括新功能，例如能够根据组织的最佳实践和文档对 [Copilot](https://thenewstack.io/github-copilot-a-powerful-controversial-autocomplete-for-developers/) 进行训练。Copilot 现在还集成了必应搜索，以便在聊天中提供最新的上下文。

负责监督 Copilot 的 GitHub 产品副总裁 [Mario Rodriguez](https://www.linkedin.com/in/mariorodriguez3/) 表示，第一个功能意味着组织可以将自己的自定义最佳实践和文档添加到 Copilot 中，以支持开发人员。

Rodriguez 说：“他们告诉我们的其中一件事是，‘GitHub，我有一些最佳实践，我希望我们的开发人员遵循，有时我将它们放在文档中，有时将它们放在所有这些地方，但它们没有得到使用。’我们能否让 Copilot 访问这些最佳实践，然后开发人员可以询问 Copilot，然后 Copilot 会回答他们。”

Rodriguez 解释说，该功能称为知识库，本质上是 GitHub 可以使用组织仓库中的文本或 markdown 文件为企业制作的 [模型自定义](https://thenewstack.io/nvidia-intros-large-language-model-customization-services/)。他补充说，这是一个技术过程，需要 GitHub 执行实际自定义。

在内部，GitHub 使用知识库将工程、安全和 [无障碍最佳实践](https://thenewstack.io/a11y-github-brings-accessibility-to-85-of-open-source/) 灌输到 Copilot 中。例如，它可能能够告诉 [开发人员组织如何部署 Kubernetes 集群](https://thenewstack.io/why-kubernetes-cluster-management-needs-to-be-easier-for-developers/)。

他说：“这三个仓库有一组最佳实践，我们希望我们的开发人员遵循并理解我们做事的原因。”“它真正根据贵组织的做法进行定制，这对这些企业来说本身也是巨大的。”

### Copilot 生成拉取请求摘要

Rodriguez 补充说，Copilot 还可以生成 GitHub 拉取请求摘要，并分析开发人员的拉取请求 (PR) 差异。

他说：“你可以轻松地花两个小时来总结所有内容。如果你说，‘嘿，Copilot，看看这些文件中所做的所有更改？帮我总结一下，并将其放入 PR 的描述中，以便审阅者在看到它时能够理解我所做的更改以及这些更改的原因，’那不是很好吗？”“这对 PR 的作者来说是一种提高生产力的方式。”

他补充说，一些拉取请求可以更改 1,000 个文件，这可能会让开发人员难以对所有更改进行总结，并且非常耗时。

GitHub 也正在扩展以提供差异摘要，即两个文件版本之间的差异。

他说：“每当你成为审阅者时，你都会想，‘好的，这个代码库中发生了什么变化，以便我真正理解？’因此，如果你刚刚结束会议并进入代码审查，你只会对所做的更改有一个大致了解。”“现在，你可以直接询问 Copilot，并说，‘向我描述一下这个差异是什么。告诉我它真正改变了什么。’然后我获得了该上下文，然后我可以为我的同事提供更好的代码审查。”

该功能已于 11 月添加到测试版中。

### Copilot 的未来发展

未来的计划包括使用企业自己的代码微调代码的能力。该功能目前处于 alpha 阶段，约有 10 位客户参与其中。在将该功能移至通用版本之前，计划进行测试版。

他说：“通过微调，你可以让建议接受率大幅提高，然后你的生产力也会因此提高。”“因此，对于不在正常训练集中出现的晦涩语言，微调是一种很好的方法。”

一个用例可能是组织如何进行 [C++ 编程](https://thenewstack.io/c-on-the-move/)。他说，即使是同一种语言，C++ 的实现也可能因组织而异，因为符号和代码的实现方式可能有所不同。

他补充说，它还允许公司在内部工具和库上训练 Copilot，这将改进代码补全器提供的建议。

他说，GitHub 的目标是在整个软件开发生命周期中注入人工智能，而且进展很快：事实上，这是 Rodriguez 在其职业生涯中看到的采用周期最快的。
“我们已经过了人工智能炒作的阶段，”罗德里格斯告诉 The New Stack。“现在有超过 50,000 家组织在使用 Copilot，超过 130 万付费用户。我们已经跨越了鸿沟。这不再是早期采用者的东西了。我们现在真正处于一个时代，我们认为，我们现在正处于人工智能转型时代，而不是数字化转型时代。”

[YOUTUBE.COM/THENEWSTACK](https://youtube.com/thenewstack?sub_confirmation=1)
技术发展迅速，不要错过任何一集。订阅我们的 YouTube 频道，以流式传输我们所有的播客、采访、演示等。