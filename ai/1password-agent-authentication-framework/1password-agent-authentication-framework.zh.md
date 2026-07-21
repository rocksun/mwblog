随着 AI 代理承担越来越多的任务，例如[管理在线账户](https://thenewstack.io/safari-mcp-platform-infrastructure/)，身份验证已成为一个实际的工程问题。例如，像 [Coinbase](https://thenewstack.io/multi-model-ai-infrastructure/) 这样的公司已经在生产环境中运行了超过一千个代理。1Password 为 [Claude](https://thenewstack.io/ai-agent-infrastructure-reliability/) 推出的这项新功能应运而生，旨在让代理集群在不向大语言模型 (LLM) 暴露密码的情况下进行登录。

该公司将这种[新的浏览器集成](https://1password.com/blog/1password-for-claude)称为“零暴露安全框架”。凭据仅在需要时解密并直接传递给浏览器，从而使 Claude 能够完成操作，而无需接触底层密码或一次性身份验证码。

> ## 解密过程始终在设备本地完成

1Password 的首席技术官 Nancy Wang 告诉 *The News Stack*，凭据的解密和填充是在用户的 Mac 上使用 1Password 的标准自动填充引擎本地完成的。

“当代理需要进行身份验证时，1Password 会在设备本地解密凭据，并通过安全通道将其直接注入目标网站，” Wang 说道。“Claude 可以请求 1Password 执行该操作，但 1Password 不会将明文凭据返回给 Claude，也不会将其放入模型的上下文中。”

> 当代理需要进行身份验证时，1Password 会在设备本地解密凭据，并通过安全通道将其直接注入目标网站。

## 任务范围内的凭据访问

当 1Password 识别出兼容的 AI 代理正在控制浏览器时，扩展程序会进入一种称为“代理模式”（Agentic Mode）的受限状态，以强制执行最小权限原则。在这种状态下，代理无法浏览或搜索用户的库，也无法从不受限制的库内容中进行选择。

“一旦 AI 代理接管浏览器，1Password 会自动锁定，将访问权限限制为仅对当前任务明确授予的凭据，” Wang 表示。“1Password 库中的其他任何内容都无法被触及。”

Claude 的访问权限是按任务授予的，用户可以通过 Touch ID 或密码进行生物识别提示，从而对每次会话进行批准或拒绝。授权范围仅限于单个任务，并在任务结束时失效，这意味着会话之间不存在持续的访问权限。

> “一旦 AI 代理接管浏览器，1Password 会自动锁定，将访问权限限制为仅对当前任务明确授予的凭据。”

## 提示词注入依然存在风险

将凭据保护与会话控制区分开来非常重要。Wang 指出，保护机密信息本身并不能限制代理在身份验证后可能采取的所有操作。登录后，代理可能会利用用户已验证的会话与目标服务进行交互。

这意味着[提示词注入（Prompt injection）仍然是一个现实的风险](https://thenewstack.io/gpt-red-prompt-injection-testing/)。恶意注入可能会导致代理请求用户未授权的访问，或者在登录后执行意外操作。

为了降低这种风险，1Password 增加了一个独立的授权边界。批准请求会显示在 1Password 控制的 UI 中，用户可以在其中进行审查和拒绝。虽然这降低了凭据暴露风险并限制了潜在的破坏范围，但用户仍需密切关注代理在已验证会话期间的实际操作。作为预防措施，1Password 还会扫描每次自动填充后的页面，确保表单提交中没有任何内容被暴露，然后再将控制权交还给 Claude。

> 作为预防措施，1Password 还会扫描每次自动填充后的页面，确保表单提交中没有任何内容被暴露，然后再将控制权交还给 Claude。

> ## 通行密钥（Passkeys）与支付功能即将推出

1Password for Claude 现已面向所有计划的 Mac 用户开放。它需要 1Password 桌面应用和浏览器扩展程序，以及 Claude 桌面应用和浏览器扩展程序。

目前，该系统支持用户名、密码和 TOTP 验证码。Wang 指出，对社交登录、通行密钥、支付卡和身份详细信息的支持已被列入路线图。

虽然该实现最初仅针对 Claude 发布，但 Wang 预计其背后的原则——即代理应该能够在不接收或保留机密信息的情况下使用凭据——最终将适用于[其他代理框架](https://thenewstack.io/cloudflare-ai-web-economics/)。