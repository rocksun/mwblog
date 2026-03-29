开源软件正遭受新一轮供应链攻击。

过去几周对开源安全来说是糟糕透顶的。一切始于2026年3月19日，当时 [Aqua Security](https://www.aquasec.com/) 的 [Trivy 漏洞扫描器](https://trivy.dev/) 遭受了严重的供应链攻击，[黑客组织 TeamPCP 多次入侵该项目的持续集成和交付（CI/CD）管道](https://www.aquasec.com/blog/trivy-supply-chain-attack-what-you-need-to-know/) 和 GitHub 仓库。一旦入侵成功，攻击者就将 Trivy 二进制文件和操作木马化，以窃取 CI/CD 管道中的敏感凭据。

这对于一家安全公司来说可不是什么好事。

那很糟糕。你想知道更糟糕的是什么吗？这仅仅是针对其他开源项目的一系列此类攻击的开始。自 [Trivy](https://trivy.dev/) 遭到攻击以来，[TeamPCP 利用一种名为 CanisterWorm 的新三阶段攻击，入侵了数十个 NPM JavaScript 包](https://www.aikido.dev/blog/teampcp-deploys-worm-npm-trivy-compromise)。随后，同一组织成功利用从 Trivy 攻击中窃取的凭据，对流行的 Python 代理包 LiteLLM 造成了严重破坏。尽管 TeamPCP 并未声称对此次攻击负责，但有人使用相同的方法 [入侵了 Agentic 安全公司 Checkmarx。](https://checkmarx.com/blog/checkmarx-security-update/)

根据《International Cyber Digest》报道，[TeamPCP 声称“已获取300 GB的压缩凭据。”](https://x.com/IntCyberDigest/status/2036526495254876418) 如果对他们如何实施攻击有任何疑问，他们还被引用说：“TeamPCP 将长期存在。供应链万岁。”

如果他们能做到，那就不是吹牛。总而言之，该组织已编译的开源项目每月下载量超过1亿次。

TeamPCP 似乎在当前这一系列成功的攻击之前，就已经活跃了一段时间。根据云安全公司 [Upwind](https://www.upwind.io/) 的说法，这一切都始于“一个名为 hackerbot-claw 的自主 AI 机器人利用 Trivy 的 GitHub Actions 工作流中的 `pull_request_target` [配置错误](https://www.upwind.io/feed/trivy-supply-chain-incident-github-actions-compromise-breakdown) 窃取了个人访问令牌（Personal Access Token），最终实现了对仓库的完全控制。”

Aqua Security 修复了这个问题，但做得不够好。在不完整的修复中幸存下来的凭据被用来入侵该公司 GitHub 的 Aqua Bot 服务账户。

数据公司 [DreamFactory](https://dreamfactory.nl/) 的首席技术官 Kevin McGahey 在一篇博文中写道，[TeamPCP 正在进行“一场协调一致的供应链攻击](https://blog.dreamfactory.com/the-litellm-supply-chain-attack-a-complete-technical-breakdown-of-what-happened-who-is-affected-and-what-comes-next)，其影响范围从安全工具逐步升级到 AI 基础设施……这种进展是深思熟虑且具有战略性的：首先入侵安全扫描器（在 CI/CD 管道中以提升权限运行的工具），收集凭据，然后利用这些凭据毒害下游基础设施。

通过攻击 Trivy，一个许多组织都默认信任并广泛使用的安全工具，TeamPCP 获取了发布恶意 LiteLLM 版本所需的 PyPI 发布令牌和 GitHub 个人访问令牌。”

## 攻击是如何展开的

[Palo Alto Networks](https://www.paloaltonetworks.com/) 分析师 [描述了 Trivy 攻击的整个过程](https://www.paloaltonetworks.com/blog/cloud-security/trivy-supply-chain-attack/) 以及随后所有攻击，将其归为五阶段攻击链的一部分。

### 阶段1：凭据重用和仓库接管

利用初始入侵中获得的凭据，TeamPCP 劫持了 Aqua Bot 服务账户，并开始作为受信任的维护者进行提交。然后，他们将恶意 `v0.69.4` 标签推送到 Trivy 仓库。这启动了一个自动化发布过程，将后门二进制文件传播到 GitHub Releases、Docker Hub、GHCR 和 Amazon ECR。

### 阶段2：GitHub Actions 标签投毒

攻击者强制更新了 `aquasecurity/trivy-action` 中76个版本标签中的75个，使其现在引用恶意提交。任何固定到版本标签（例如 `@v0.28.0`）的 GitHub Actions 工作流都会悄无声息地拉取攻击者控制的代码，而工作流定义没有任何可见的变化。为了避免在 Git 历史中引起怀疑，恶意提交复制了原始作者元数据和时间戳，并且相同的技术也被用于毒害七个 `setup-trivy` 标签。

### 阶段3：三阶段凭据窃取

受污染的操作运行了一个三阶段数据窃取序列：

*   收集：恶意软件直接从 GitHub Actions 运行器内存中读取，绕过日志掩码，捕获了 SSH 密钥、云凭据（AWS、GCP、Azure）、Kubernetes 令牌、Docker 注册表登录信息、数据库密码、TLS 私钥和加密货币钱包数据。
*   加密：所有捕获的信息都使用 `AES-256-CBC` 进行加密，然后用 `RSA-4096` 进行包装，从而对抗大多数网络级检查。
*   外泄：加密的负载被发送到一个拼写错误的域名 (`scan.aquasecurtiy[.]org`)；如果失败，恶意软件使用受害者的 GitHub PAT 创建一个名为 `tpcp-docs` 的公共仓库，并将数据存储在那里，利用 GitHub 的可信基础设施。

### 阶段4：开发人员机器上的持久后门

当受感染的 Trivy 二进制文件在开发人员的机器上执行时，它会安装一个作为 `systemd service` (`sysmon.py`) 的持久后门。该服务大约每50分钟联系一次 Internet Computer (ICP) 区块链上的一个 `canister`，以获取命令和控制指令，利用难以中断的去中心化基础设施。

### 阶段5：CanisterWorm — 自传播 npm 供应链攻击

利用收集到的凭据，TeamPCP 发起了 CanisterWorm 攻击，入侵了多个范围内的47个 `npm packages`。后续的迭代将令牌窃取和自动恶意发布添加到 `postinstall hook` 中，因此任何安装了受影响包的开发人员工作站或 CI 管道都成为了无意中的传播节点。有一次爆发中，28个包在不到60秒内被植入后门。

最终结果是什么？Trivy 开源供应链被悄无声息地武器化了。

## GitHub 也应承担责任

然而，在指责 Trivy 之前，其他安全专业人士将此次安全漏洞的责任归咎于 GitHub。在一次电子邮件采访中，安全镜像公司 [Chainguard](https://www.chainguard.dev/) 的首席执行官兼联合创始人 Dan Lorenc 告诉 The New Stack，这次攻击“利用了其 GitHub Actions 配置中的一个弱点。他们基本上将不受信任的输入（在这种情况下是分支名称）传递到操作内部的脚本中，而没有正确地对其进行转义。攻击者能够发送带有不安全内容的分支名称的拉取请求。这使得恶意分子能够利用操作管道本身。一旦得手，攻击者就能将恶意提交推送到仓库或从 CI 系统中窃取凭据。”

Lorenc 继续说道：“很多默认设置都很糟糕，并且可能以微妙的方式被利用。这既影响了对 Trivy 的初始攻击，也影响了恶意软件如何通过使用 Trivy GitHub Action 的每个人的 CI 系统传播。因此，现在正发生另一波攻击，利用的是从那些 Trivy 用户那里窃取的所有凭据。”

简而言之，“这一整波攻击并非真正的新事物，但它无疑是迄今为止规模最大的一次。它正在影响多个生态系统，包括像 GitHub Actions 这样的新生态系统（想想 [Shai-Hulud](https://unit42.paloaltonetworks.com/npm-supply-chain-attack/) [臭名昭著的 npm 恶意软件攻击] 的升级版）。

## 轮换凭据，锁定操作

你能对此做些什么？Lorenc 建议：“任何在管道中使用了 Trivy 操作或在自己的系统上运行了它的人，很可能凭据已被窃取，需要轮换它们。”这包括云密钥、GitHub 令牌、SSH 密钥、Kubernetes 令牌、Docker 注册表凭据、数据库密码、TLS 密钥以及任何暴露的钱包。你还应该从干净、受信任的基线重新构建受影响的 CI 运行器和镜像，而不是试图原地“清理”它们。

为了防止此类攻击再次发生，你应该将 GitHub Actions 锁定到 `commit SHAs`，而不是标签。这样，你就可以将操作锁定到特定的提交哈希，而不是移动版本标签。你还应该通过明确的权限来锁定你的 GitHub 令牌和其他运行器令牌。例如，除非绝对需要，否则不允许写入权限。”

除此之外，这是一个痛苦的提醒，即使我们的安全工具也可能被用来对付我们。我们必须开始像对待其他任何依赖项一样对待安全工具。例如，跟踪它们的精确版本，验证校验和，并且不要为扫描器自动跟踪“最新”版本。

这还没有结束。你可以预期很快会有更多此类攻击。嘿，没有人说过软件开发安全很容易。我们希望它不要如此痛苦，尤其是现在我们甚至无法信任自己的安全程序。