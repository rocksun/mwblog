Anthropic 在周三[宣布](https://claude.com/blog/cowork-chrome-side-panel)对其 Chrome 扩展进行了一项重大更新，将 [Claude in Chrome](https://chromewebstore.google.com/detail/claude/fcoeoabgfenejglbffodgkkbkcdhcgfn?hl=en-US&pli=1) 从一个实用但相对孤立的体验，转变为浏览器中一个完整的 Claude Cowork 客户端，支持在 Anthropic 的各类应用间保持会话同步。

更新后的扩展程序现已向所有 Max 和 Team 计划订阅者开放，并计划在未来几周内推向 Pro 用户。

在此之前，Claude in Chrome 的功能相对独立，几乎与 Claude 的其他应用完全脱节，虽然在浏览器环境下很有用，但无法作为其他 Claude 平台的配套工具。事实上，这正是用户在 [Chrome 应用商店](https://chromewebstore.google.com/detail/claude/fcoeoabgfenejglbffodgkkbkcdhcgfn/reviews?hl=en-US)中对该扩展程序的主要吐槽点之一。

由于该扩展程序现在与整个 Claude 生态系统紧密相连，所有对话都会保存到用户的历史记录中。因此，用户可以轻松地在桌面端或移动端应用上发起对话，然后在浏览器中继续进行。

同样重要的是，用户的所有技能（skills）和连接器（connectors）现在也可以在 Chrome 的 Claude 侧边栏中使用。

![](https://cdn.thenewstack.io/media/2026/08/34c12201-chrome-extension-thumbnail-1024x576.png)

图片来源：Anthropic。

浏览器扩展的主要优势在于它能够使用浏览器并“看到”用户正在查看的内容。

Anthropic 解释道：“你每天使用的许多工具都[直接连接到 Claude](http://claude.com/connectors)，但其他工具（如内部仪表盘、旧系统和供应商门户）则不然。通过 Claude in Chrome，Claude 可以在浏览器中操作这些应用。”

## Claude Cowork 成为默认选项

几周前，Anthropic 才刚刚将 [Cowork 引入 Web 和移动端](https://thenewstack.io/claude-cowork-cloud-mobile/)。这项工作很可能是为了在 Chrome 扩展中实现 Cowork 功能所必须的。毕竟，在此之前，Cowork 仅存在于桌面应用中。但现在，它正逐渐成为使用 Claude 的事实标准。

或许 Anthropic 未来会逐渐整合 Cowork 和基础的 Claude Chat。这将消除许多用户在选择使用常规聊天还是 Cowork 时的困惑，因为归根结底，Cowork 不仅能完成基础聊天的所有功能，还能做到更多。

![](https://cdn.thenewstack.io/media/2026/08/bb951072-6a7ccc8227b8db87f3b33e7b_image-16-1024x576.png)

图片来源：Anthropic。

## 通过自动模式确保安全

正如 Anthropic 指出的那样，“Claude in Chrome 承担着与任何在浏览器中运行的 AI 智能体相同的风险，主要是[提示词注入](https://www.anthropic.com/research/prompt-injection-defenses)。”

如果恶意攻击者在网站上隐藏了针对智能体的指令，这可能会带来问题。但随着此次更新，Anthropic 本质上将其 [Claude 自动模式](https://thenewstack.io/claude-code-auto-mode/)也扩展到了基于浏览器的智能体上，智能体会自动检查是否有异常情况，而无需用户不断批准每一个操作（从而避免产生通知疲劳）。

> “虽然这些措施有效地降低了风险，但无法彻底消除它。”——Anthropic。

值得庆幸的是，在进行任何购买或共享个人数据之前，Claude 仍会征求用户的同意。你肯定不希望回家后发现一堆意外的亚马逊包裹，仅仅因为 Claude 自作主张购买了昂贵的内存条。

然而，在智能体领域不存在绝对的安全，因此 Anthropic 正确地指出，“虽然这些措施有效地降低了风险，但无法彻底消除它。”

## 可用性

新的扩展体验目前正在向 Max 和 Team 计划的用户推送。Pro 用户将在未来几周内体验到。对于企业计划（Enterprise plans）的用户，该功能默认处于关闭状态，但管理员可以启用它并将其使用范围限制在特定域名内。

另外需要注意的一点是：尽管还有许多其他基于 Chromium 的浏览器，但 Anthropic 指出该扩展程序无法在这些浏览器（或移动端）上运行。