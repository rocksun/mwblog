
<!--
title: AI正在向开源代码库发送垃圾邮件，制造虚假问题
cover: https://cdn.thenewstack.io/media/2025/02/f41ddf87-fake_ai_issues_hit_repos.jpg
-->

维护人员找到了一家 AI 公司，该公司表示垃圾邮件是一个错误。但报告显示，这个问题更加普遍，而且还在增长。

> 译自 [AI Is Spamming Open Source Repos With Fake Issues](https://thenewstack.io/ai-is-spamming-open-source-repos-with-fake-issues/)，作者 Loraine Lawson。

据一些维护者称，人工智能被用于在开源仓库中创建虚假功能请求。到目前为止，Curl、React、CSS和Apache Airflow等项目中都已报告了由人工智能驱动的问题。

目前尚不清楚这一问题的普遍程度，但已经严重到维护者开始发声。雅雷克·Potiuk （Jarek Potiuk）是Apache Airflow的提交者和PMC成员，Apache Airflow是一个允许用户设计、安排和监控数据管道的开源平台。Potiuk 上周在领英上公开了关于人工智能提交的请求，并与TNS分享了他的经历。

## 双倍问题

Apache Airflow 的维护人员发现有一天收到的错误报告数量几乎翻了一倍，从通常的20到25个增加到50个。他们调查后发现这些问题似乎非常相似，但其实毫无意义。他们开始怀疑这些虚假问题是人工智能生成的。

Potiuk 在他的领英帖子中解释说：“在过去的几天和几周里，我们收到了大量毫无意义的错误报告，这些报告要么是其他问题的副本，要么完全无用且毫无意义。”

Potiuk 向我们解释，人工智能提交的问题不仅会增加维护人员的工作量，还可能导致真正的问题被忽视或错误地关闭。

“我们一天大概有30个问题，或许40个，但现在在24小时内，又多了30个，也就是说增加了100%，这意味着我们无法像以往一样对其他事务做出太多决策，因为我们需要先决定：这是一个好问题还是坏问题？”他说道。“由于这些问题的负面影响很大，至少有两三个问题是真正的人提出的，而一些已经比较敏感的维护者，把它们当作垃圾信息关闭了。”

他后来重新审视了这些问题，发现有两到三个问题虽然被关闭了，但实际上是合理的。他重新打开了这些问题，但确实有可能会错过真正的问题。他也听说其他维护者也遇到过类似的“奇怪”的请求问题，尽管他们没有像AirFlow遇到的那么多问题。

## 追踪人工智能问题

Potiuk 恳求那些与人工智能驱动问题有关联的人解释到底发生了什么。一位提交者发来了道歉。这个人还告诉 Potiuk ，

他们一直在观看一个关于使用人工智能向代码仓库提交问题的Outlier AI培训视频。这个人并不知道自己提交的是一个真实的代码仓库。

Potiuk 在领英上发帖并艾特了Outlier：“Outlier，你做错了。请停止欺骗那些人，让他们不要再在许多开源代码仓库中创建由人工智能生成的、毫无意义的问题。”

Outlier是一个招募专家来帮助训练生成式人工智能的平台。它也是硅谷独角兽公司Scale AI的子公司。

起初，Potiuk 以为Outlier是想通过他们对这些请求的回应来训练人工智能，但后来发现事实并非如此。

> “离经叛道者。你做错了。请停止那些被你欺骗去在许多开源仓库中创建完全无意义的AI生成问题的人。”——Jarek Potiuk，Apache Airflow的提交者和PMC成员

Potiuk 表示，Scale的代表告诉他，他们并不打算让视频观众向实际的代码库提交请求。这本应只是一个创建问题的练习。他们还否认了他们试图使用代码库来训练他们的人工智能。

Outlier在其常见问题解答中表示：“你将从事各种项目，从生成你所在领域的训练数据以推进这些模型，到评估模型的性能。”

Scale拒绝了面对面的采访，但将《新栈》网站引向他们在领英上的回应，Scale AI的运营负责人 George Quraishi 在回应中写道：

“为了说明背景，我们一直在探索训练和评估模型的新方法；编码是其中一个感兴趣的领域。这个项目的具体目标是教会一个模型如何帮助开发人员分析问题并实施代码更改——而不是将这些工单提交到你的代码库。”他写道，“不幸的是，我们的一些贡献者误解了项目要求，并采取了这一步。我们立即更新了要求，使其更加明确。”

他继续说，Scale重视维护人员的工作，他们“绝对没有故意提交工单来给维护人员添麻烦的意图”。

这并非Outlier第一次因其行为而引起媒体关注。去年夏天，Inc.com报道称[一些员工指控Outlier是骗局](https://www.inc.com/sam-blum/its-a-scam-accusations-of-mass-non-payment-grow-against-scale-ais-subsidiary-outlier-ai.html)，因为该公司没有支付他们的工资。

## AI垃圾邮件安全

这个问题不太可能仅仅是由一家AI公司造成的。AI也被用于发送安全报告的垃圾邮件。

这个问题至少可以追溯到2024年初，当时[cURL作者Daniel Stenberg对此进行了撰写](https://daniel.haxx.se/blog/2024/01/02/the-i-in-llm-stands-for-intelligence/)。最近，Python软件基金会的驻场安全开发人员[Seth Larson也指出了这个问题](https://sethmlarson.dev/slop-security-reports)。

Larson写道：“最近，我注意到开源项目中极其低质量、垃圾邮件和LLM幻觉的安全报告有所增加。“在LLM时代，这些报告乍一看似乎可能是合法的，因此需要时间来驳斥。”

Larson写道，这个问题“分布在数千个开源项目中，由于报告的安全性敏感性，开源维护人员不愿分享他们的经验或寻求帮助”。

> “最近，我注意到开源项目中极其低质量、垃圾邮件和LLM幻觉的安全报告有所增加。”
>
> ——Seth Larson，Python软件基金会驻场安全开发人员

Larson恳求开发人员不要使用AI或LLM来检测漏洞。

他写道：“目前的这些系统无法理解代码，发现安全漏洞需要理解代码以及理解人类层面的概念，例如意图、常见用法和上下文。”

他还建议多思考一下。

他写道：“一些报告者会运行各种安全扫描工具，并根据结果打开漏洞报告，似乎没有经过片刻的批判性思考。”“例如，[urllib3](https://pypi.org/project/urllib3/)最近收到了一份报告，因为一个工具检测到我们使用SSLv2是不安全的，即使我们使用它的目的是明确禁用SSLv2。”

## 一些攻击可能是国家行为者吗？

[Craig McLuckie](https://www.linkedin.com/in/craigmcluckie/), [Kubernetes](https://thenewstack.io/build-an-open-source-kubernetes-gitops-platform-part-1/)的联合创始人，现任Stacklok的创始人兼首席执行官，告诉TNS，他的团队发现有人试图通过创建与知名软件包名称相似的软件包来伏击代码库。

他们发现有人试图欺骗[Tea协议](https://tea.xyz/resources/about)，这是一个用于管理开源软件开发者认可和补偿的去中心化框架。

McLuckie说：“他们发布了成千上万个软件包，其唯一目的是让这些软件包看起来像是开源生态系统的重要组成部分。”“仅仅是这些伏击式软件包的数量，就正在迅速增长，在我看来，要产生我们看到的这种数量和细微变化，幕后可能有一个生成式AI代理。”

他与Tea协议的开发者进行了交谈，他们同意这“绝对是不良行为”，然后与[npm](https://www.w3schools.com/whatis/whatis_npm.asp)合作删除了这些软件包。

McLuckie怀疑幕后是国家行为者。

他说：“越来越多的生成式AI被用来创建某事物的轻微变体，并且大规模地这样做，我认为这种情况只会越来越糟。”

## 应对AI提交

一位GitHub工程师在Potiuk的LinkedIn帖子中发帖称他们正在调查这个问题，因此TNS询问了[GitHub](https://thenewstack.io/root-out-vulnerabilities-in-github-as-you-merge-code-changes/)如何应对AI向代码库提交的问题。

一位发言人告诉TNS：“GitHub拥有超过1.5亿开发者，在超过4.2亿个代码库中进行构建，并致力于为开发者提供安全可靠的平台。”“我们有专门的团队致力于检测、分析和删除违反我们可接受使用政策的内容和帐户。”

GitHub补充说，他们采用人工审核和使用机器学习的大规模检测，并不断发展和适应对抗性策略。

发言人说：“我们还鼓励客户和社区成员举报滥用和垃圾邮件。”
Potiuk 还建议维护者继续向 GitHub 报告 AI 提交的内容。他还建议开源组织与“优秀”的 AI 公司合作，以识别虚假问题。他的团队正在与一家名为 [Dosu](https://dosu.dev/) 的 AI 公司合作，他发现这对于筛选问题很有帮助。他补充说，这是一种非常不同的体验，因为这家 AI 公司正在与团队紧密合作。

“他们会根据人们创建的内容自动为问题添加标签，这使我们能够对问题进行分类，而无需花费大量时间，”他告诉 TNS。“他们与我们进行了交流。我们与他们进行了通话，他们向我们解释了情况，并且他们免费为我们提供了用于开源项目的工具。”
