
<!--
title: Curl与来自HackerOne的大量AI生成的漏洞报告作斗争
cover: https://cdn.thenewstack.io/media/2025/05/2a944577-sky-2713230_1280.jpg
summary: `Curl`遭 HackerOne 上大量 AI 生成的低质量 Bug 报告“DDoS 攻击”，维护者不堪其扰。HackerOne 虽不禁 AI 辅助，但严禁垃圾信息。`Curl` 推出 AI 使用新规，要求报告必须人工验证，抵御 `LLM` 幻觉。社区热议 AI 在漏洞赏金计划中的应用，及如何避免“AI 垃圾”泛滥。
-->

`Curl`遭 HackerOne 上大量 AI 生成的低质量 Bug 报告“DDoS 攻击”，维护者不堪其扰。HackerOne 虽不禁 AI 辅助，但严禁垃圾信息。`Curl` 推出 AI 使用新规，要求报告必须人工验证，抵御 `LLM` 幻觉。社区热议 AI 在漏洞赏金计划中的应用，及如何避免“AI 垃圾”泛滥。

> 译自：[Curl Fights a Flood of AI-Generated Bug Reports From HackerOne](https://thenewstack.io/curl-fights-a-flood-of-ai-generated-bug-reports-from-hackerone/)
> 
> 作者：David Cassel

本月早些时候，Curl 维护者 Daniel Stenberg 在 LinkedIn 上抱怨大量涌入的“AI 垃圾”bug 报告。“就这样了。我受够了，”他写道。“我将阻止这种疯狂行为。”

他写道，该项目“实际上受到了 DDoS 攻击”。罪魁祸首是漏洞赏金网站 HackerOne 的志愿者。

Stenberg 的 LinkedIn 帖子吸引了超过 250 条评论和超过 600 次转发。该事件引发了网络上关于我们偶然进入的 AI 驱动时代的更广泛讨论，以及我们应该如何应对 AI 辅助的人类。

![](https://cdn.thenewstack.io/media/2025/05/b4121bed-screemnshot-from-daniel-stenberg-linkedin-post-about-curl-ai-slop-reports.png)

因此，虽然 Stenberg 仍然感谢来自 HackerOne 的众包安全报告，但他明确表示，他希望看到未来的一些变化，包括小的和大的变化。

## 结果而非起源

上周发生了两件事。5 月 16 日星期五，HackerOne 联合创始人/CTO/CISO Alex Rice 重申了 HackerOne 的行为准则“不禁止使用 AI 协助编写报告”的立场，但它禁止垃圾邮件。“包含幻觉漏洞、模糊或不正确的技术内容或其他形式的低质量噪音的报告将被严格视为垃圾邮件，并将根据我们的行为准则采取强制措施。”

在回答 The New Stack 的问题时，Rice 强调报告需要“清晰、准确和可操作”，但 HackerOne 仍然正式关注结果，而不是起源。“我们相信，当负责任地使用 AI 时，它可以成为研究人员的强大工具，提高生产力、规模和影响力。这个领域的创新正在加速，我们支持使用 AI 来提高工作质量和效率的研究人员。

“关于数量问题，我们实际上看到报告质量总体上有所提高，因为 AI 帮助研究人员理清了他们的工作，”Rice 补充道。“虽然我们没有发现广泛的 AI 生成幻觉的证据，但这些报告可能非常难以验证，因此是我们正在积极解决的问题。”

Stenberg 并不反对 AI 识别 Curl 的漏洞。“我确信将来会出现使用 AI 来实现此目的的工具，至少在部分时间里会（更好）地工作，”他在 2024 年初写道，“所以我不能也不会说 AI 用于发现安全问题一定总是坏主意。

“但是，我怀疑，如果你只是在其中添加一个非常小的（智能）人工检查，那么任何此类工具的使用和结果都会变得更好。我怀疑在未来很长一段时间内也是如此。”

本月，Stenberg 在 LinkedIn 上表示，“我们仍然没有看到任何通过 AI 帮助完成的有效安全报告。” 但 AI 生成的报告可能已经帮助了其他项目。在 LinkedIn 上，Stenberg 确定了“真正让我感到受不了”的“AI 垃圾”报告。但软件工程师 Randy Clinton 指出，同一位记者似乎已经从包括 Adobe 和 Starbucks 在内的其他 HackerOne 参与者那里获得了超过 1,900 美元的漏洞赏金。

在对 The New Stack 的评论中，Rice 补充了他的观点。“总的来说，我们看到报告质量总体上有所提高，因为 AI 帮助研究人员理清了他们的工作，尤其是在英语是第二语言的情况下……关键是确保 AI 增强报告，而不是引入噪音。”

简而言之，他说，HackerOne 的目标“是鼓励推动更好安全结果的创新，同时对所有提交的内容保持同样的高标准。”

## Stenberg 采取行动

与此同时，5 月 15 日星期四，Stenberg [宣布](https://mastodon.social/@bagder/114511780991862687)了 Curl 的[人工智能使用新指南](https://curl.se/dev/contribute.html#on-ai-use-in-curl)，明确了他希望在未来看到的内容。“如果你要求人工智能工具查找 curl 中的问题，你必须在报告中说明这一事实。”（Stenberg 在 [Mastodon 上](https://mastodon.social/@bagder/114450295029056683) 警告说，回答“是”保证会有一连串的后续问题，以证明报告的另一端存在一些真正的人类智能。）

![](https://cdn.thenewstack.io/media/2025/05/8b3c64ce-daniel-stenberg-on-mastodon-new-ai-screening-question-for-hackerone.png)

到 2024 年 1 月，[Curl](https://thenewstack.io/you-too-could-have-made-curl-daniel-stenberg-at-fosdem/) 已经支付了 70,000 美元的漏洞赏金（用于 64 个已确认的安全问题），Stenberg 在[一篇博文中写道](https://daniel.haxx.se/blog/2024/01/02/the-i-in-llm-stands-for-intelligence/)。但是一份“糟糕”的安全报告意味着“我们错过了修复错误或开发新功能的时间。更不用说处理垃圾会耗费你的精力。”

因此，本月新的人工智能使用指南警告贡献者，“在向我们报告之前，你还必须仔细检查调查结果，以验证这些问题是否确实存在并且与人工智能所说的完全一致。基于人工智能的工具经常生成不准确或捏造的结果。” 该指南警告说，人工智能检测到的错误报告可能过于冗长（甚至在它们过于常见的“捏造细节”之前），该指南告诉用户首先验证问题是否真实，然后“自己编写报告并解释你所了解的问题。

“这确保了人工智能生成的不准确和捏造的问题在浪费更多人的时间之前尽早被过滤掉。”

这是一个真诚的尝试，旨在解释“人工智能垃圾”如何干扰项目的推进，因为 Curl 必须认真对待安全报告并及时进行调查。“这项工作既耗时又耗费精力，使我们无法进行其他有意义的工作。

“虚假和其他编造的安全问题实际上阻止了我们进行实际的项目工作，并浪费了我们的时间和资源。

“我们会立即禁止向项目提交编造的虚假报告的用户。”

Stenberg 似乎也希望有经济处罚，因为他在 LinkedIn 帖子中补充说：“如果可以的话，我们会向他们收取浪费我们时间的费用。”

## “让它听起来很吓人”

本月早些时候，Stenberg [告诉 Ars Technica](https://arstechnica.com/gadgets/2025/05/open-source-project-curl-is-sick-of-users-submitting-ai-slop-vulnerabilities/)，他对这个问题受到关注感到“非常高兴”，“这样我们就可以采取一些措施……” 他认为这是一个教导更大社区的机会，“LLM [大型语言模型] 无法发现安全问题，至少不像他们在这里使用的方式那样。” Stenberg 还告诉该网站，在一个星期内，他收到了

*四份*明显由人工智能生成的漏洞报告——而且它们很容易被发现，因为它们友好而礼貌，英语完美，并且有漂亮的要点。“普通人第一次写作时永远不会这样做……”
Stenberg 回忆说，一位用户实际上将他们的提示留在了错误报告中——“他以‘让它听起来很吓人’结尾。”

5 月初，一份[报告](https://hackerone.com/reports/3125832)声称它发现了内存损坏的证据，分析显示来自以下函数的堆栈递归：

`ngtcp2_http3_handle_priority_frame`.

但只有一个问题。

“没有像这样的函数……” Stenberg [发现自己发布了](https://hackerone.com/reports/3125832#activity-34392850)。 后来，他同意嵌入式系统顾问 [Jean-Luc Aufranc](https://www.linkedin.com/in/cnxsoft/) 的观点，后者在 LinkedIn 上[总结](https://www.linkedin.com/feed/update/urn:li:activity:7324820893862363136?commentUrn=urn%3Ali%3Acomment%3A%28activity%3A7324820893862363136%2C7324823934531432448%29&replyUrn=urn%3Ali%3Acomment%3A%28activity%3A7324820893862363136%2C7325150930834743296%29&dashCommentUrn=urn%3Ali%3Afsd_comment%3A%287324823934531432448%2Curn%3Ali%3Aactivity%3A7324820893862363136%29&dashReplyUrn=urn%3Ali%3Afsd_comment%3A%287325150930834743296%2Curn%3Ali%3Aactivity%3A7324820893862363136%29)了这种情况：“[T]人工智能创建了一个随机函数……该函数在代码中不存在，以及一个随之而来的安全漏洞。”

在之后的评论中，Stenberg表示这是一个[日益增长的现象](https://www.linkedin.com/feed/update/urn:li:activity:7324820893862363136?commentUrn=urn%3Ali%3Acomment%3A%28activity%3A7324820893862363136%2C7324854476945719296%29&replyUrn=urn%3Ali%3Acomment%3A%28activity%3A7324820893862363136%2C7324901273827217408%29&dashCommentUrn=urn%3Ali%3Afsd_comment%3A%287324854476945719296%2Curn%3Ali%3Aactivity%3A7324820893862363136%29&dashReplyUrn=urn%3Ali%3Afsd_comment%3A%287324901273827217408%2Curn%3Ali%3Aactivity%3A7324820893862363136%29)。在他2024年的博客文章中，Stenberg强调了一份疑似[AI生成的报告](https://hackerone.com/reports/2199174)，该报告“混合搭配了旧安全问题的事实和细节，创造并编造了一些与现实无关的新东西……” 然而，Stenberg本月在LinkedIn上补充说：“几年前根本不存在这类报告，而且这种趋势似乎正在增加。”

因此，虽然AI生成的评论“仍然没有淹没我们……但趋势看起来并不好。”

## “更强大的东西”

Stenberg还告诉*Ars Technica*，他希望看到HackerOne“做一些事情，更强大的事情，来采取行动”。他甚至愿意帮助他们构建必要的基础设施，以创建“更多工具来打击这种行为”。

但是，当LinkedIn上的安全测试人员[建议](https://www.linkedin.com/feed/update/urn:li:activity:7324820893862363136?commentUrn=urn%3Ali%3Acomment%3A%28activity%3A7324820893862363136%2C7325880597157928960%29&dashCommentUrn=urn%3Ali%3Afsd_comment%3A%287325880597157928960%2Curn%3Ali%3Aactivity%3A7324820893862363136%29)“是时候放弃漏洞赏金众包模式，并雇用全职的专门人员”时，Stenberg并不同意。

“我们的漏洞赏金已经为78个已确认的漏洞支付了86,000美元。没有专业人士能达到如此接近的成本/性能比。” 此外，他指出Curl设法资助了一名全职员工。“我很想雇用更多的人，但我们很难让公司支持我们。”

网络安全公司XOR的联合创始人[Tobias Heldt](https://www.linkedin.com/in/tobias-heldt-214561264/) [想知道](https://www.linkedin.com/feed/update/urn:li:activity:7324820893862363136?commentUrn=urn%3Ali%3Acomment%3A%28activity%3A7324820893862363136%2C7325545476110409729%29&dashCommentUrn=urn%3Ali%3Afsd_comment%3A%287325545476110409729%2Curn%3Ali%3Aactivity%3A7324820893862363136%29)漏洞报告流程是否需要一些摩擦——比如“如果研究人员必须为他们的提交支付少量押金”，只有当他们的报告被评为达到基本信息阈值时才能退还。 后来，Heldt将这个想法称为“安全报告债券”，并认为“如果没有它，很快大部分报告将来自暴力破解赏金计划的机器人。”
Stenberg同意“这可能是一个可行的模型”，并建议像HackerOne这样的公司应该带头。

![](https://cdn.thenewstack.io/media/2025/05/204d3b7f-python-seth_larson-300x225.jpg)

*Python软件基金会的Seth Larson (Pycon 2025)。*

IT/服务公司Varadius Ltd的董事[Jim Clover](https://www.linkedin.com/in/jim-clover-obe-996b8724/)提出了一个[新颖的解决方案](https://www.linkedin.com/feed/update/urn:li:activity:7324820893862363136?commentUrn=urn%3Ali%3Acomment%3A%28activity%3A7324820893862363136%2C7324864784556769280%29&dashCommentUrn=urn%3Ali%3Afsd_comment%3A%287324864784556769280%2Curn%3Ali%3Aactivity%3A7324820893862363136%29)。他通过询问ChatGPT o3来审查“AI垃圾”，ChatGPT正确地回应说它是“技术上不健全的……引用了不存在的函数”。 Clover的结论是什么？ “你能把这些通过AI（多么讽刺）作为一个BS检查器来节省你们的时间吗？”

但是[Python](https://thenewstack.io/what-is-python/)的安全驻场开发者[Seth Larson](https://thenewstack.io/pythons-new-security-developer-has-plans-to-secure-the-language/)已经得出了相反的结论，[分享](https://www.linkedin.com/feed/update/urn:li:activity:7324820893862363136/?commentUrn=urn%3Ali%3Acomment%3A%28activity%3A7324820893862363136%2C7324864784556769280%29&replyUrn=urn%3Ali%3Acomment%3A%28activity%3A7324820893862363136%2C7325554175856062465%29&dashCommentUrn=urn%3Ali%3Afsd_comment%3A%287324864784556769280%2Curn%3Ali%3Aactivity%3A7324820893862363136%29&dashReplyUrn=urn%3Ali%3Afsd_comment%3A%287325554175856062465%2Curn%3Ali%3Aactivity%3A7324820893862363136%29)了他三月份写的一篇题为“[不要把垃圾带到垃圾战中](https://sethmlarson.dev/dont-bring-slop-to-a-slop-fight)”的博客文章。

“[使]用AI来检测和过滤AI内容只会意味着将使用更多的生成式AI，而不是更少。 这不是我们想要发送给风险投资家的信号，他们正在决定是否为这些公司提供更多的投资。”

## 回应与反应
接下来会发生什么还不清楚。“那些想要滥用系统的人，无论是否存在复选框，都会继续这样做，”高级全栈开发人员 [Damian Mulligan](https://www.linkedin.com/in/damian-mulligan-896b303a/) [在LinkedIn上发帖](https://www.linkedin.com/feed/update/urn:li:activity:7324820893862363136?commentUrn=urn%3Ali%3Acomment%3A%28activity%3A7324820893862363136%2C7325948820868005891%29&dashCommentUrn=urn%3Ali%3Afsd_comment%3A%287325948820868005891%2Curn%3Ali%3Aactivity%3A7324820893862363136%29)。

Databricks软件工程师 [Hasnain Lakhani](https://www.linkedin.com/feed/update/urn:li:activity:7324820893862363136?commentUrn=urn%3Ali%3Acomment%3A%28activity%3A7324820893862363136%2C7324870102380617729%29&dashCommentUrn=urn%3Ali%3Afsd_comment%3A%287324870102380617729%2Curn%3Ali%3Aactivity%3A7324820893862363136%29) 想知道，当人们简单地谎称他们使用了人工智能时，他该怎么办。（“这似乎是一场军备竞赛，”他建议说，项目需要工具来 *筛选* 人工智能。）

Heldt发出了一个不祥的警告。“人工智能垃圾正在 *今天* 淹没维护者，它不会止步于Curl，而只是从那里开始。”

但也许解决这个问题的有效努力已经开始了。当Mastodon上的某人问Stenberg是否可以将Curl关于人工智能贡献的新指南用于另一个项目时，Stenberg立即给出了答案。

“[当然可以](https://mastodon.social/@bagder/114512085821167451)！”