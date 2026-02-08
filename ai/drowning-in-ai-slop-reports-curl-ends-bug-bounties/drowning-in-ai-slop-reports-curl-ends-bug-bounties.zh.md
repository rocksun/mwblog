够了。流行的开源互联网文件传输协议 [cURL](https://curl.se/) 的首席开发者兼创始人 Daniel Stenberg [正在关闭 cURL 的漏洞赏金计划](https://github.com/curl/curl/pull/20312)，将于一月底生效。

为什么？因为 cURL 的维护者正被“AI 垃圾”所淹没。在通过 Mastodon 进行的采访中，Stenberg 告诉 The New Stack，“我们试图消除提交虚假报告的动机。提交的质量直线下降；不仅很多提交明显是垃圾，而且那些不明显是 AI 的报告在很大程度上也更糟糕（可能是因为它们也是 AI，只是隐藏得更好）。我们需要采取措施防止我们被淹没。”

## AI 垃圾对开源安全的影响

他并不是唯一一个对 AI 垃圾漏洞报告感到厌倦的人。[sbomify](https://sbomify.com/) 的创始人兼 [Screenly](https://www.screenly.io/) 的联合创始人 Viktor Petersson 在一篇 LinkedIn 帖子中首次发布了 cURL 这一变化的消息，他写道：“我们 Screenly 可能只看到了 cURL 所收到数量的一小部分，但[漏洞赏金中大量的 AI 垃圾报告对人工审查员来说负担巨大](https://www.linkedin.com/feed/update/urn:li:activity:7419042849993682945/)。”此言极是。

Stenberg 继续说道：“计划是在一月底关闭它，所以项目可能会在下周发布更多相关消息。这也与我那个周末在 [FOSDEM](https://fosdem.org/) 上关于开源安全和 AI 的演讲时间契合。”

这一举动不足为奇。Stenberg 一直是滥用 AI 漏洞报告最强烈的反对者。早在 2025 年 5 月，他就曾[抱怨过来自漏洞赏金网站 HackerOne 的“AI 垃圾”漏洞报告泛滥成灾](https://thenewstack.io/curl-fights-a-flood-of-ai-generated-bug-reports-from-hackerone/)。他曾在 LinkedIn 上表示：“我们现在[立即禁止任何提交我们认定为 AI 垃圾报告的报告者](https://www.linkedin.com/posts/danielstenberg_hackerone-curl-activity-7324820893862363136-glb1/)。我们已经达到了一个极限。我们实际上正在遭受 DDoS 攻击。如果可以，我们会向他们收取浪费我们时间的费用。我们仍然没有看到一份由 AI 辅助完成的有效安全报告。”

## 区分 AI 垃圾和有效的 AI 辅助漏洞发现

然而，这并不是说 Stenberg 拒绝使用 AI 来发现漏洞。他并没有。例如，在 2025 年 9 月，他在 Mastodon 上赞扬了 Joshua Rogers，因为他发送了“[一份通过其 AI 辅助工具发现的 #curl 潜在问题的大量清单](https://mastodon.social/@bagder/115241241075258997)”。到处都是代码分析器风格的细节问题。大部分是小错误，但仍然是错误，其中可能有一两个实际的安全漏洞。实际上，这些发现真是太棒了。

你看，Stenberg 的问题不在于 AI 本身；而在于懒惰的人们如何不假思索地使用 AI 来寻找赏金或作为安全研究人员的声誉。

请注意，如果你确实发现了一个真正的漏洞，无论是否借助 AI 帮助，cURL 维护者仍然希望知道。但是，如果你确实使用了 AI，则必须遵循 [cURL 的 AI 使用规则](https://curl.se/dev/contribute.htm)。这不是可选的。如果你不遵守这些规则，你就不会为 cURL 做出贡献。考虑到 cURL 维护者被 AI 垃圾淹没的程度，你不能责怪他们采取如此严格的立场。如果我是他们，我也会这样做。