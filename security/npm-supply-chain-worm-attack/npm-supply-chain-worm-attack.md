<!--
title: npm 攻击揭秘：恶意软件如何将来源证明变为伪装掩护
cover: https://cdn.thenewstack.io/media/2024/06/d494bd17-blockchain.jpg
summary: 近期爆发的 npm 供应链攻击通过窃取开发者凭证，利用自动安装钩子植入蠕虫病毒。攻击者不仅利用 CI 环境传播恶意代码，还通过合法的来源证明机制进行伪装，导致安全校验失效。对此，工程团队需实现发布权限与依赖安装流程的彻底隔离。
-->

近期爆发的 npm 供应链攻击通过窃取开发者凭证，利用自动安装钩子植入蠕虫病毒。攻击者不仅利用 CI 环境传播恶意代码，还通过合法的来源证明机制进行伪装，导致安全校验失效。对此，工程团队需实现发布权限与依赖安装流程的彻底隔离。

> 译自：[The npm attack that turned provenance attestations into camouflage](https://thenewstack.io/npm-supply-chain-worm-attack/)
> 
> 作者：Amanda Caswell

**安全研究人员本周披露了**一起影响超过 400 个软件包的 npm 供应链攻击，其中包括与 Keyv 和 Cacheable 相关的项目。攻击者使用窃取的开发者凭证发布了恶意版本。

这起事件似乎指向了软件安全领域的一个趋势：攻击者正在针对那些已经被信任可以进行发布的开发者和工作流程下手。

> 攻击者正在针对那些已经被信任可以进行发布的开发者和工作流程下手。

## 蠕虫通过凭证传播

根据 [Microsoft Threat Intelligence](https://www.microsoft.com/en-us/security/blog/2026/08/04/chaindrop-supply-chain-compromise-anatomy-self-propagating-worm/) 的报告，恶意版本包含了一种 Mini Shai-Hulud 凭证窃取蠕虫的变体。它们在传播过程中绕过了源代码仓库，并从窃取的维护者凭证开始。一旦进入系统，蠕虫就会在开发者机器和 CI 环境中搜索任何可以利用的其他凭证。

当发现有效的 npm 发布令牌时，它会下载该账户可以访问的每个软件包的最新版本，注入恶意的 preinstall 生命周期钩子，增加补丁版本号并发布受感染的版本。由于 npm 会在安装完成前自动运行 preinstall 钩子，恶意软件可以在应用程序测试或安全检查开始之前，就在开发者的工作站和 [CI runners](https://thenewstack.io/anthropic-mendral-cicd-acquihire/) 上开始运行。

> 由于 npm 会在安装完成前自动运行 preinstall 钩子，恶意软件可以在应用程序测试或安全检查开始之前，就在开发者的工作站和 CI runners 上开始运行。

## Preinstall 钩子实现静默执行

在 CI 环境中，它保持与活动作业的连接，从而能够获取工作流机密、runner 凭证和发布权限。在工作站上，它可以在后台持续运行，并将启动文件注入到 Visual Studio Code 和 [Claude](https://thenewstack.io/anthropic-claude-containment-failure/) 中，包括 .vscode/tasks.json 和 .claude/settings.json。

此次攻击暴露了信任发布机制的弱点，突显出在授权工作流中运行的恶意软件可以请求其自己的短期令牌，而不是仅仅窃取长期发布凭证。由此产生的恶意软件包甚至可以携带有效的 [来源证明 (provenance attestations)](https://docs.npmjs.com/generating-provenance-statements/)。

## 来源证明并不能保证完整性

这场运动展示了攻击从开发者的机器移动到发布流程的其他部分有多快。共享的 CI 系统增加了另一个入口，因为 GitHub Actions 可以在工作流运行之间重用依赖项。GitHub 的 [文档](https://docs.github.com/en/actions/reference/workflows-and-actions/dependency-caching) 警告称，这些缓存文件既未签名也未经过验证。

工程团队得到的教训是：将发布权限与安装依赖的管道部分隔离开来。限制自动化流程权限的原则，呼应了业界在[如何重新思考 AI 辅助编程的全面权限](https://thenewstack.io/microsoft-copilot-token-budgets/)这一更大趋势。

> 这场运动展示了攻击从开发者的机器移动到发布流程的其他部分有多快。

## 将发布与依赖安装隔离

微软建议升级到 [npm CLI 12](https://github.blog/changelog/2026-06-09-upcoming-breaking-changes-for-npm-v12/)，锁定已知良好的版本，并使用 [min-release-age](https://docs.npmjs.com/cli/v11/using-npm/config) 来给团队在安装新版本之前留出审查时间。

一旦受感染的软件包运行了其生命周期脚本，仅轮换被盗令牌[可能是不够的](https://thenewstack.io/apple-ai-bug-report-caps/)。团队可能还需要重建受影响的机器和基础镜像，清除共享缓存，并使用受信任的依赖项重新创建软件构件。