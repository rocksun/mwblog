今年早些时候，[Anthropic 推出了 Claude Security](https://thenewstack.io/anthropics-claude-security-beta/)，这是一款帮助开发团队扫描代码库中的安全漏洞并进行修复的企业级工具。周五，该公司通过将 [Claude Mythos 5 模型引入该服务](https://claude.com/blog/bringing-claude-mythos-5-to-more-defenders)，对 Claude Security 进行了一次重大升级。

此外，Anthropic 还在与其他网络安全公司合作，帮助它们将 Mythos 5 集成到各自的产品中，并启动了一个新的“防御者优势基金”（Defender Advantage Fund，简称 0xDAF），该基金将提供 3500 万美元的积分，用于发现和修复开源软件中的漏洞。

Anthropic 此前还推出了 [网络验证计划（Cyber Verification Program）](https://support.claude.com/en/articles/14604842-real-time-cyber-safeguards-on-claude-opus-and-sonnet)，让经过审查的防御者能够以更少的限制在 Opus 和 Sonnet 上进行双重用途的网络安全工作。Anthropic 表示，这些组织很快也将获得安全访问 Claude Mythos 的权限。

## Mythos 5 的故事：好到无法发布

[Mythos 5](https://www.anthropic.com/news/claude-fable-5-mythos-5) 当然就是那个在执行高风险领域任务时表现过于出色，以至于 Anthropic 没有将其公开发布的模型。相反，它在 6 月份推出了 Fable 5，本质上是 Mythos 5，但带有非常严格的护栏。

当时，Mythos 5 仅提供给 Anthropic “Project Glasswing”计划中的约 150 个合作伙伴（此外还有关于 Fable 5 在发布三天后被美国政府[禁止](https://thenewstack.io/us-gov-orders-anthropic-to-pull-fable-5-and-mythos-5-three-days-after-launch/)又[解禁](https://thenewstack.io/how-anthropic-is-bringing-fable-5-back/)的完整背景故事）。

## Claude Security 中的 Mythos 5

那么，为什么该公司现在觉得将 Mythos 5 添加到 Claude Security 很妥当呢？

“当用户可以直接访问模型时，风险行为就会发生，恶意行为者可能会试图引导模型进行有害的使用，”Anthropic 在公告中写道。“但如果用户只能收到特定的输出，例如漏洞补丁或安全警报，那么风险就会低得多。我们宣布的这些变化为用户提供了更好的防御成果，同时在模型直接访问方面保持了适当的护栏。”

## 安全防护

从本质上讲，由于 Anthropic 在此负责，且所有这些都在其工具和架构内部运行，该公司认为现在可以安全地将 Mythos 5 提供给所有企业。用户获得的是发现结果和补丁，而不是直接访问模型，Anthropic 表示 Claude Security “使用 Mythos 5 来扫描您拥有的代码。”

该公司还补充说，它及其合作伙伴“已采取滥用预防措施，以确保模型保持在预期的范围内。”

由于许多代码库包含开源库，所有权变得有点难以界定。此外，开发人员如果将广泛部署的库克隆到公司存储库中，然后让 Mythos 5 对其进行扫描，将得到攻击者所寻找的相同发现结果。毕竟，该漏洞将存在于发布该库的任何地方。我们将不得不看看这种情况会如何发展。

在实践中，这意味着 Mythos 5 现在已向所有想要使用 Claude Security 的 Claude Enterprise 用户开放公测。管理员可以为用户启用它，然后开发人员和安全团队可以使用它，在 Mythos 5 的主导下扫描其存储库，并在发现问题时提供修复建议。

不过，Mythos 5 的代币并不便宜。Anthropic 对每百万输入代币收费 10 美元，对每百万输出代币收费 50 美元。