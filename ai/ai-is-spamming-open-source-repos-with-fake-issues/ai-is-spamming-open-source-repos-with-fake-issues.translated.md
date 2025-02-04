# AI Is Spamming Open Source Repos With Fake Issues

![Featued image for: AI Is Spamming Open Source Repos With Fake Issues](https://cdn.thenewstack.io/media/2025/02/f41ddf87-fake_ai_issues_hit_repos-1024x576.jpg)

According to several maintainers, AI is being used to open fake feature requests in open source code repositories.  So far, AI-generated issues have been reported in Curl, React, CSS, and Apache Airflow.

The extent of the problem is unclear, but it's become serious enough that maintainers are starting to publicly discuss it.  [Name], a committer and PMC member of Apache Airflow—an open-source platform that allows users to design, schedule, and monitor data pipelines—publicly discussed the AI-submitted requests on LinkedIn last week and spoke with TNS about his experience.

## Issue Numbers Double

Apache Airflow maintainers noticed the number of issues they received per day nearly doubled, jumping from the usual 20-25 to 50.  They investigated and found the issues looked very similar but were nonsensical. They began to suspect the fake issues were AI-created.

“In the last few days and weeks, we started receiving a lot of meaningless issues, which are either copies of other issues or completely useless and meaningless,” [Name] explained in the LinkedIn post. “This wastes valuable time for maintainers who have to evaluate and close these issues.”

[Name] explained that AI-submitted issues don't just add more work for maintainers; they also cause legitimate issues to be overlooked or mistakenly closed.

“We have about 30 issues a day, maybe 40, but now in 24 hours, we have 30 more, so it’s a 100% increase, which means we can’t make as many decisions on other things because we have to decide: Is this a good issue or a bad issue?” he said. “Because of its very harmful impact, at least two or three issues were created by real people, some already sensitive maintainers, who closed it as spam.”

He later reviewed those issues and noticed two or three issues that were closed but were legitimate. He reopened them, but the possibility of missing real issues remains. He also heard from other maintainers experiencing similar problems with “weird” requests, though they weren't receiving as many issues as AirFlow.

## Tracking Down the AI Issues

[Name] pleaded with those involved with the AI-generated issues to explain what happened. One committer contacted him and apologized.

The person also said they had been watching a training video on using AI to submit issues to code repositories. The person didn't realize they were submitting to real repositories.

“[Name], you did wrong,” [Name] wrote in the LinkedIn post, tagging Outlier. “Please stop all the people you induced to create AI-generated, completely meaningless issues in many open-source code repositories.”

Outlier is a platform that recruits subject matter experts to help train generative AI. It's also a Silicon Valley unicorn company, a subsidiary of Scale AI.

Initially, [Name] thought Outlier was trying to somehow leverage their responses to the requests to train AI, but that proved incorrect.

“[Name], you did wrong. Please stop all the people you induced to create AI-generated, completely meaningless issues in many open-source code repositories.”

— [Name], Apache Airflow committer and PMC member

[Name] said Scale representatives told him they didn't intend for people watching the video to submit requests to actual repositories. It was supposed to be an exercise in creating issues. They also denied they were trying to leverage the repositories to train their AI.

“You will participate in a variety of projects, from generating training data in your area of expertise to improve these models to evaluating the performance of the models,” their FAQ states.

Scale declined a request for an on-the-record interview but directed The New Stack to their LinkedIn response, where [Name], head of operations at Scale AI, wrote:

“For context, we’ve been exploring new ways to train and evaluate models; coding is an area of interest. The specific goal of this project was to teach a model how to help developers analyze issues and implement code changes—not to submit these tickets to your repositories,” he wrote. “Unfortunately, some of our contributors misunderstood the project requirements and took that extra step. We immediately updated the requirements to make them clearer.”
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

*TNS高级编辑 Joab Jackson 为本文做出了贡献。*

[YOUTUBE.COM/THENEWSTACK](https://youtube.com/thenewstack?sub_confirmation=1)  技术发展迅速，不要错过任何一集。订阅我们的 YouTube 频道，收看我们所有的播客、访谈、演示等等。