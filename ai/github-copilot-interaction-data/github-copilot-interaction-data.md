<!--
title: GitHub Copilot将用你的数据训练AI，还和微软共享！
cover: https://cdn.thenewstack.io/media/2025/04/7b5ec6b7-mvimg_20171129_165458-scaled.jpg
summary: GitHub Copilot将使用用户数据训练AI模型并与微软共享，个人用户需手动选择退出。此举引发开发者褒贬不一的反应。
-->

GitHub Copilot将使用用户数据训练AI模型并与微软共享，个人用户需手动选择退出。此举引发开发者褒贬不一的反应。

> 译自：[GitHub will train AI models on your Copilot data — and share it with Microsoft](https://thenewstack.io/github-copilot-interaction-data/)
> 
> 作者：Meredith Shubel

另一个平台将使用你的数据来训练其AI模型。这次是GitHub。

[GitHub](https://github.com/) 本周宣布，它将根据GitHub首席产品官 Mario Rodriguez 的一篇[博客文章](https://github.blog/news-insights/company-news/updates-to-github-copilot-interaction-data-usage-policy/)，使用GitHub CoPilot用户的交互数据（例如，输入、输出、代码片段和相关上下文）来训练和改进其AI模型。

该更新于4月24日生效，适用于所有Copilot Free、Pro和Pro+用户，但你可以选择退出。正如GitHub在周三发送给其[Copilot用户](http://github-launches-its-coding-agent/)的电子邮件中所解释的，要选择退出：“前往GitHub账户设置；选择Copilot；选择是否允许你的数据用于AI模型训练。”

如果你之前已选择不让GitHub收集你的交互数据以改进产品（即，通过禁用名为“启用或禁用提示和建议收集”的设置），这些偏好将被保留，因此你可以跳过此步骤。

Copilot Business和Copilot Enterprise用户无需担心；他们不会受到此更新的影响。

## 你提供了什么，给谁

重要的是，如果你不选择退出，不仅GitHub会获得你的交互数据，其关联公司也会。

正如GitHub所指出的，这包括“我们公司家族中的公司，包括微软。”根据GitHub周三发布的[隐私声明和条款更新](https://github.blog/changelog/2026-03-25-updates-to-our-privacy-statement-and-terms-of-service-how-we-use-your-data/)，这些关联公司“现在可以出于额外目的使用共享数据，包括开发和改进人工智能和机器学习技术，但须遵守适用法律及其自身的隐私承诺。”

该平台表示，这些权限不适用于第三方AI模型提供商或其他独立服务提供商，尽管正如其在[常见问题和相关讨论](https://github.com/orgs/community/discussions/188488)中澄清的：“我们也可能聘请服务提供商代表我们协助进行模型训练，但须遵守合同义务，即数据仅用于向GitHub提供服务。”

如果你*不*选择退出，你究竟会向GitHub及其关联公司移交什么？

GitHub的公告中列出了七种交互数据类型，包括：“你接受或修改的输出”；“发送给GitHub Copilot的输入”；“光标位置周围的代码上下文”；“你编写的注释和文档”；“文件名、仓库结构和导航模式”；以及“与Copilot功能的交互（聊天、内联建议等）。”

模型训练中不会包含Copilot Business、Copilot Enterprise或企业拥有的仓库的交互数据，也不会包含“你的问题、讨论或静态私有仓库中的内容”。

在其公告中，GitHub提请注意此“静态”规范，指出该更新“在你积极使用Copilot时会处理私有仓库中的代码。”

当被问及交互数据保留多久以及用户是否可以查看或删除它时，GitHub表示保留时间因用例而异，并指出它可能会保留输入、输出、代码片段和相关上下文长达五年，尽管该期限通常会更短。

## 并非所有开发者都同意

在他的公告博客文章中，Rodriguez 提醒读者，GitHub最初的模型是使用公开可用数据和代码样本构建的。该平台表示，在过去一年中，它已整合了微软员工的交互数据，以实现“有意义的改进，包括多种语言的接受率提高。”

现在，GitHub旨在通过将用户交互数据纳入其训练中来获得类似的收益，希望帮助其模型更好地理解开发工作流程，提供更准确、安全的代码模式建议，并尽早发现bug。

但从[Reddit](https://www.reddit.com/r/GithubCopilot/comments/1s3ky4h/on_april_24_well_start_using_github_copilot/)和[Hacker News](https://news.ycombinator.com/item?id=47521799)上开发者社区的初步反应来看，并非所有人都相信这次更新能平等地惠及所有用户。

一个常见的抱怨是用户必须选择退出，而不是选择加入；其他人说GitHub提供了相互矛盾的退出说明，使其变得不必要地困难。

还有人批评GitHub使用个人用户数据而非企业数据的做法，正如Hacker News上的一位评论者所写：

> “你所描述的个人/企业不对称是B2B SaaS中的标准做法。Slack、Notion和Figma都在企业数据处理协议（DPA）中包含了机器学习训练豁免，而免费用户则没有。GitHub在这里并没有做任何不寻常的事情——他们只是用代码来做，这感觉比文档或消息更敏感，因为它可能真的是你正在从个人账户处理的雇主的IP。”

在其常见问题和相关讨论中，GitHub解释了这种差异，承认其与商业和企业客户签订了协议，禁止将Copilot交互数据用于模型训练，并再次强调个人用户可以随时选择退出。

其他开发者则不那么强烈批评，他们赞扬GitHub在其他公司狡猾时更加透明：“说实话，我很感谢他们为此添加了通知横幅。大多数公司会尽可能悄悄地做这件事，”一位redditor写道。

GitHub为将个人用户交互数据纳入模型训练的决定辩护，称这符合既定的行业惯例，并且此举“将改善所有用户的模型性能”，目前用户数量已超过2600万。由于有如此多的开发者使用GitHub Copilot，现在可用于AI模型训练的庞大数据量可能导致模型改进速度加快。

Rodriguez 在公司的公告文章中确认：“我们相信AI辅助开发的未来取决于开发者真实的交互数据。”