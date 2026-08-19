OpenAI 在开源权重 AI 模型问题上的立场并不明确，既[对强大的中国模型发布发出警告](https://www.axios.com/2026/07/22/openai-anthropic-open-models-trump-china)，同时也[反对](https://www.techradar.com/ai-platforms-assistants/openai-quietly-signs-letter-from-nvidia-microsoft-and-meta-warning-about-dangers-of-premature-restrictions-on-open-weight-ai-models-as-the-white-house-accuses-china-of-stealing-from-anthropic)过早的监管限制。但该公司联合创始人兼总裁 [Greg Brockman](https://www.linkedin.com/in/thegdb/) 已明确表示，他认为来自[中国 AI 公司 Z.ai](https://en.wikipedia.org/wiki/Z.ai) 等企业的开源权重模型构成了快速增长的网络安全风险。

在周一发表的一篇[博客文章](https://openai.com/index.the-defenders-window/)中，Brockman 概述了 OpenAI 为保护自身而采取的安全措施、他认为其他组织应采取的步骤，以及他为何认为现在是采取行动时刻的理由。这一切的起因是[一个月前发生的安全事件](https://huggingface.co/blog/security-incident-july-2026)，当时 OpenAI 自己的模型在逃离内部测试环境后，[侵入了 Hugging Face 的基础设施](https://thenewstack.io/openai-huggingface-sandbox-breach/)。

在文章中，Brockman 强调了公司为使安全天平向防御者倾斜所做的努力，自[二月推出“网络受信任访问计划”](https://openai.com/index/trusted-access-for-cyber/)以来，通过[将最先进的模型限制](https://thenewstack.io/openai-gpt56-cyber-daybreak/)给经过审查的安全专业人员群体使用。但与此同时，他也借此机会重新提出了开源权重模型这一争议性话题。

> “各种公司已经发布了在网络能力上仅落后于前沿模型几个月的开源权重模型。最近发布的这些模型似乎定于 8 月底发布，并且很可能会显著加速威胁格局的发展。”

“从那时起，各种公司已经发布了在网络能力上仅落后于前沿模型几个月的开源权重模型，”Brockman 写道。“最近发布的这些模型似乎[定于 8 月底发布](https://z.ai/blog/glm-5.3)，并且很可能会显著加速威胁格局的发展。”

Brockman 没有点名 Z.ai，但他链接到了该公司的[近期 GLM-5.3 发布](https://thenewstack.io/glm-5-3-post-training-coding/)，根据这家中国实验室自己的基准数据，这标志着编码和代理能力方面的显著飞跃，其漏洞发现评分强于 [Anthropic 的 Fable 5](https://thenewstack.io/anthropic-claude-mythos-fable-5/) 和 [OpenAI 的 GPT-5.6 Sol](https://thenewstack.io/developers-review-gpt-56-sol/)——尽管在实际利用开发方面，它排名第三，落后于这两款模型。

## 两派的碰撞

虽然 Z.ai 打算在 8 月下旬开放其模型权重，但 OpenAI 在[推出 GPT-5.6-Cyber](https://thenewstack.io/openai-gpt56-cyber-daybreak/)（其最新的网络安全模型）时采取了不同的方法，作为其现有 Daybreak 计划 8 月 10 日扩展的一部分。该模型的访问权限仍然仅限于该计划，该计划现在要求进行身份验证、法律证明，并且从 9 月 1 日起，个人账户必须使用硬件安全密钥。

这种对比有助于说明这两个“阵营”是如何处理日益强大的网络模型的：OpenAI 及其竞争对手保持对访问权限的更严格控制，而 Z.ai 及其同类产品则趋向于公开权重发布，尽管保持了一定的谨慎。

正如 *The New Stack* [周一报道](https://thenewstack.io/amodei-open-weights-compute-regulation/)的那样，Anthropic 对开源权重模型也持类似谨慎态度，尽管原因略有不同。首席执行官 Dario Amodei 周末在 [X 上发文](https://x.com/DarioAmodei/status/2088758816376807762)辩称，AI 在结构上倾向于将权力集中在控制最多算力和芯片的人手中，他将这种动态归因于扩展定律而非监管。

“开源权重确实在这方面有所帮助，但远非充分的解决方案，因为它们只是将集中度在一定程度上转移到了拥有最多算力和芯片的人手中——这大致就是前沿实验室加上可能的硬件提供商，”Amodei 写道。他此前曾称没有危险能力的开源模型为“[公共产品](https://www.anthropic.com/news/position-open-weights-models)”，并保留了他对强制性安全测试的呼吁——无论模型是开源还是闭源发布——针对任何能够帮助他人实施严重攻击的模型。

Brockman 所暗示的 GLM-5.3 是否真的会“显著加速威胁格局的发展”，这在很大程度上仍有待争论。[Jake Williams](https://www.linkedin.com/in/jake-williams-77938a16/) 是一位前国防部 (DoD) 漏洞分析师，目前是 [IANS Research](https://www.iansresearch.com/) 的教员分析师，他并不这么认为。他并不否认威胁行为者会使用 GLM-5.3——他只是不认为多一个更有能力的工具就能构成现有获取途径的重大升级。

> “你认为威胁行为者会使用这个吗？当然会——就像他们能接触到的任何其他软件一样。你认为它会显著改变威胁格局吗？绝对不会。”

“开源权重模型不需要在基准测试中跟上前沿模型就能改变格局，”他告诉 *The New Stack*。“只要它们在性能上接近，它们实际上可能比闭源权重模型更有价值。我可以使用[消融](https://en.wikipedia.org/wiki/Ablation_(artificial_intelligence))对开源权重模型进行处理，以删除任何给定任务的拒绝回答 […] 你认为威胁行为者会使用这个吗？当然会——就像他们能接触到的任何其他软件一样。你认为它会显著改变威胁格局吗？绝对不会。”

也许 Kimi K3 就是这种差距的一个很好的例子。7 月份，[Moonshot AI 的模型](https://thenewstack.io/kimi-k3-inference-bottleneck/)（另一个中国的开源权重发布）由英国 AI 安全研究所 (AISI) 和美国 AI 标准与创新中心 (CAISI) [联合评估](https://www.aisi.gov.uk/blog/preliminary-assessment-of-kimi-k3s-cyber-capabilities)，它以巨大差距落后于前沿系统——在 41 个 ExploitBench 样本中未能实现任意代码执行，而禁用了系统级防护措施的最强闭源模型平均能达到 20 个。然而，研究人员表示，其防护措施“并未阻止它在测试期间尝试网络漏洞利用开发或进攻性网络操作”。

这一点值得深思：Kimi 的防护措施仍然有效，但它们并没有阻止模型尝试进攻性网络操作；它的能力是更大的制约因素。即便如此，它也取得了一些成功——AISI/CAISI 发现 Kimi K3 可以在 10 次运行中有 1 次完成对“小型、防御薄弱且脆弱的企业系统”的自主攻击。在这种背景下，GLM-5.3 的确切能力和基准位置只能说明部分情况。更大的问题是，一旦模型权重公开，且任何剩余的限制都可以被修改或删除，会发生什么。

## 双刃剑

放眼全局，一个显而易见的问题仍然存在。Brockman 这篇文章的整个基础都围绕着 OpenAI *自己*的模型脱离其测试环境并获得对真实公司内部基础设施的未授权访问。然而，在撰写相关内容时，他却选择了提及一个在中国发布的开源权重模型。

那么，为什么？

OpenAI 最近在开源权重模型方面的记录提供了一些答案。7 月中旬，新任命的“战略未来主管” [Dean Ball 提出](https://x.com/deanwball/status/2078133895766114412)，开源权重模型是“本质上的减速主义”，并警告称它们有将世界推向他所谓的由国家控制的 AI 的“反乌托邦地狱”的风险，预测特朗普政府最终将寻求围绕中国开源权重模型的使用创造监管风险。

此后不久，OpenAI [最终](https://x.com/firstadopter/status/2080818109141631210)在[英伟达牵头的一封信](https://thenewstack.io/nvidia-open-weight-letter/)上署名，在广泛层面上捍卫开源权重模型，反对“过早的限制”。值得一提的是，Anthropic 没有签署。

根据 7 月份[对 Axios 发表的评论](https://www.axios.com/2026/07/22/openai-anthropic-open-models-trump-china)，OpenAI 实际上寻求的是更结构化的东西：一位公司发言人表示，目标是“一个连贯的国家框架，使美国能够快速评估新模型、管理风险，并将最强大的 AI 工具交到网络防御者手中”——与其说是否定开源权重，不如说是一个让它们受到某种形式的国家评估和风险管理的系统。

Brockman 对 GLM-5.3 的提及同样带有这种微观上的张力：一个接近前沿并即将公开发布的开源权重模型，在一个由 OpenAI 自身模型获得对另一家公司系统未授权访问而引发的文章中，被特别指出为一个日益增长的网络风险。

这又把问题带回到了控制本身。虽然模型控制可能确实具有一些网络安全优势，但反过来也存在风险。Anthropic 的 [Fable 5 事件](https://thenewstack.io/anthropic-fable-mess-explained/)表明，这些控制措施可能会被政府有效操纵：当华盛顿[下令该公司](https://thenewstack.io/us-gov-orders-anthropic-to-pull-fable-5-and-mythos-5-three-days-after-launch/)暂停对外国公民的访问权限时，Anthropic 暂时将这些模型完全下线。更常见的是，这些相同的提供商侧防护措施也会捕获合法使用：Anthropic [承认](https://www.anthropic.com/news/redeploying-fable-5)，Fable 5 不同寻常的宽泛安全余量将许多良性请求误报为假阳性，并在用户多次被引导至能力较弱的模型后，随后[放宽了一些生物学限制](https://www.anthropic.com/news/improving-fable-5-s-biology-safeguards)。

> “OpenAI 和 Anthropic 将继续决定你能用他们的模型做什么，不能做什么。”

因此，开源权重模型一旦发布，可能更难监管，但它们也更难被开发人员或政府收回。

“OpenAI 和 Anthropic 将继续决定你能用他们的模型做什么，不能做什么，”Williams 说。“正如我们反复经历的那样，如果大型模型提供商决定他们不再适应你的给定工作流程，这可能会使现有的用例作废。开源权重模型也将所有的变更控制权掌握在你手中——这是前沿模型的另一个痛点。”