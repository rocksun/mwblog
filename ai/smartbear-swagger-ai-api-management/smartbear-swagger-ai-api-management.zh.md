上周，[SmartBear](https://smartbear.com/) 宣布为其商业版 [Swagger](https://swagger.io/about/) 工具集推出新功能，旨在随着 AI 编程工具加速软件开发，帮助企业治理、验证并扩展 API。

此次更新的核心在于两项新增功能：一是经过重新设计的 Swagger Catalog（Swagger 目录），让平台团队能够集中查看 API 组合；二是具备漂移检测功能的契约测试，可持续验证 API 的行为是否符合 [OpenAPI](https://thenewstack.io/openapi-how-to-handle-file-management/) 规范。

SmartBear 表示，Swagger 支持横跨整个 AI 赋能的 API 全生命周期的设计、治理和测试，确保每一步的质量。它使用户能够构建面向人类、大语言模型（LLM）、智能体（Agent）以及持续创新的 API。

## AI 编写代码的速度已超过规范更新速度

该公司将这两项新功能置于“应用程序完整性”的旗帜下——SmartBear 的首席产品兼技术官 Vineeta Puranik 将这一术语定义为一种持续、可衡量的保证，即确保软件按预期运行，并具备能够以 AI 速度和规模运行的治理能力。

Vineeta Puranik 试图解决的问题是，像 [GitHub Copilot](https://thenewstack.io/github-copilot-wants-to-become-your-peer-programmer/) 和 [Claude](https://thenewstack.io/claudes-free-plan-can-now-remember-you/) 这样的工具可以在几分钟内生成或修改数千行代码，但这些 API 本应遵循的规范并不会自动更新。其结果就是 SmartBear 所说的“漂移”——即 API 契约与代码实际行为之间的偏差。

“平台负责人正面临碎片化的发现过程和生命周期可见性缺失的困扰，而工程和 [QA 团队](https://thenewstack.io/is-genai-replacing-your-qa-team-a-sobering-reality-check/) 则面临着规范与运行时之间无声的背离，”Vineeta Puranik 告诉 *The New Stack*。

## 要么左移，要么晚点付出代价

SmartBear 的漂移检测功能在 [CI/CD](https://thenewstack.io/a-brief-devops-history-the-road-to-ci-cd/) 流水中运行，在代码到达生产环境之前捕获偏差。这与 [Kong](https://thenewstack.io/kong-new-ai-infused-features-for-api-management-dev-tools/) 或 [Apigee](https://cloud.google.com/apigee) 等 [API 网关](https://thenewstack.io/ai-gateways-vs-api-gateways-whats-the-difference/) 提供的功能有所不同——那些工具是观察生产环境中的流量，这意味着错误已经发生了。Vineeta Puranik 表示，SmartBear 的主张是[左移（shift-left）](https://thenewstack.io/shifting-left-is-now-mainstream-for-developers-or-is-it/)：在构建周期中发现漂移，而不是在部署之后。

她指出，Swagger Catalog 解决了可见性方面的问题。随着 AI 工具大规模生成和修改 API，平台团队会失去对现有哪些 API、哪些符合规范以及哪些已准备好投入生产的追踪。该目录提供对组织完整 API 组合的生命周期追踪和治理执行——包括从代码库、[CI/CD 流水线](https://thenewstack.io/how-to-build-scalable-and-reliable-ci-cd-pipelines-with-kubernetes/)摄取的 API，以及从 Postman 等工具导入的规范。

## 一站式全景视图

在一家参与功能测试的汽车公司担任高级首席解决方案架构师的 Jason Burch 表示，该目录的价值既是技术性的，也是组织性的。

他在一份声明中说：“当你将数百个内部 API 集中展示在一个地方时，它为产品、开发和架构团队创造了跨团队的可见性——并以我们目前的流程无法实现的方式提升了治理水平。”

此次发布还包括本季度即将推出的多项 Swagger 平台更新。其中包括：具备 AI 驱动 API 生成功能的新编辑器、上下文感知文档、基于 Spectral 的治理执行、支持自然语言 API 自动化的 [MCP 服务器](https://thenewstack.io/mcp-the-missing-link-between-ai-agents-and-apis/) 支持，以及对 OpenAPI 3.1、AsyncAPI 3.0 和 [GraphQL](https://thenewstack.io/why-every-api-strategy-needs-graphql/) 扩展的协议支持。

## 作为智能体基础设施的 API

对 MCP 服务器的支持具有特殊意义。Vineeta Puranik 说，智能体之间的通信是通过 API 进行的，这意味着机器可读且最新的规范不再仅仅是最佳实践，而是一种硬性依赖。

在这种环境下，漂移不仅会破坏测试，还会破坏集成。Vineeta Puranik 直言不讳地指出：“智能体之间靠什么交谈？就是 API。”

除了目录和漂移检测外，SmartBear 还将一款名为 [BearQ](https://smartbear.com/product/bearq/) 的新型 AI 原生测试产品定位为应用程序完整性故事的一部分。该工具从一个 URL 开始，自主探索应用程序功能，生成测试用例，运行它们并标记失败——所有这些都不需要测试人员具备脚本编写知识。

“你可以告诉它去查看某个功能，它就会明白你的意思，”Vineeta Puranik 说，“你不需要告诉它任何脚本语言。”她表示，针对批量 [API 测试](https://thenewstack.io/reining-in-the-api-wild-west-5-api-testing-best-practices/)的智能体工作流（将工具指向整个代码库）计划于第二季度推出。

## 平台化策略，而非单一解决方案

SmartBear 的 Swagger 工具被全球 32,000 家机构的 1,600 多万名开发人员使用，包括三星、福特和万豪。由该公司委托 Forrester 咨询公司进行的一项总体经济影响研究发现，对于一家拥有 200 名开发人员的复合型企业，该平台在三年内实现了 227% 的投资回报率。

与此同时，SmartBear 在上月底发布了 [SmartBear Application Integrity Core](https://cts.businesswire.com/ct/CT?id=smartlink&url=https%3A%2F%2Fsmartbear.com%2Fapplication-integrity%2F&esheet=54472517&newsitemid=20260331994897&lan=en-US&anchor=SmartBear+Application+Integrity+Core&index=2&md5=27b72faf4974b2ea7006e6b5d061be95)。与这两个新发布的功能一样，这些能力改进并加速了应用程序测试，以跟上 AI 驱动代码生成速度和数量的增长。

这些新功能为人类主导的测试工作流增加了智能体和 AI 动力——包括针对本地应用利用 AI。这些举措紧随 SmartBear 最近发布的 BearQ 之后，进一步完善了其注入 AI 的应用程序测试产品组合。

增强功能包括：

* SmartBear 测试自动化平台 [Reflect](https://cts.businesswire.com/ct/CT?id=smartlink&url=https%3A%2F%2Freflect.run%2F&esheet=54472517&newsitemid=20260331994897&lan=en-US&anchor=Reflect&index=6&md5=a0eb90335f9bbd23ca1b48470c86660d) 中新增的智能体能力，允许开发人员和 QA 工程师直接从其编码环境生成自动化测试。通过 [SmartBear MCP 服务器](https://cts.businesswire.com/ct/CT?id=smartlink&url=https%3A%2F%2Fdeveloper.smartbear.com%2Fsmartbear-mcp%2Fdocs%2Fmcp-server&esheet=54472517&newsitemid=20260331994897&lan=en-US&anchor=SmartBear+MCP+server&index=7&md5=85485a9877179628a6fc2e2cf7dbcbf6)调用 Reflect，团队可以引入更丰富的上下文，借鉴现有的测试资产、统一的可见性与报告以及开发历史。这能够以智能体方式创建上下文感知测试，并在无需从零开始的情况下加速自动化采用。
* [Zephyr](https://cts.businesswire.com/ct/CT?id=smartlink&url=https%3A%2F%2Fsmartbear.com%2Ftest-management%2Fzephyr%2F&esheet=54472517&newsitemid=20260331994897&lan=en-US&anchor=Zephyr&index=8&md5=434ffb4010d0532e648caf2200c300c6) 新增的 Rovo 智能体技能，可在 Atlassian Jira 中实现自然语言查询，以评估测试覆盖率、搜索测试执行情况并评估发布就绪性，从而使 QA 团队能够快速识别缺漏并确定测试工作的优先级。
* 为 SmartBear 的桌面测试和安全本地环境工具增加 AI 能力——包括在 [ReadyAPI](https://cts.businesswire.com/ct/CT?id=smartlink&url=https%3A%2F%2Fsmartbear.com%2Fppc%2Fready-api%2Ftrial%2F%3Futm_source%3Dgoogle-paid%26utm_medium%3Dppcg%26utm_campaign%3DG%2B-%2BReadyAPI%2B-%2BNA%2B-%2BBR%26utm_term%3Dsmartbear%2520readyapi%26utm_content%3De%26gclsrc%3Daw.ds%26gad_source%3D1%26gad_campaignid%3D22677754068%26gbraid%3D0AAAAAD_lD115EYpIfhXyZNc_N-Pz-Nq_0%26gclid%3DCj0KCQjw7IjOBhDyARIsAFzrWQzLcmuWLqbP4glQIuJm4vyBIcrIOX9ySp2CjzAxHNMLi4MtRfgTWvMaArQ_EALw_wcB&esheet=54472517&newsitemid=20260331994897&lan=en-US&anchor=ReadyAPI&index=9&md5=57423f77eed27cbe2ca6aed96ec977b9) 中提供自然语言 AI 测试生成，用于构建复杂的多步骤 API 测试；并在 [TestComplete](https://cts.businesswire.com/ct/CT?id=smartlink&url=https%3A%2F%2Fsmartbear.com%2Fproduct%2Ftestcomplete%2Ffree-trial%2F%3Futm_source%3Dgoogle-paid%26utm_medium%3Dppcg%26utm_campaign%3DG%2B-%2BTestComplete%2B-%2BNA%2B-%2BBR%26utm_term%3Dtestcomplete%26utm_content%3De%26gclsrc%3Daw.ds%26gad_source%3D1%26gad_campaignid%3D22668117066%26gbraid%3D0AAAAAD_lD111N9JQpjkNohRX33XpToCZf%26gclid%3DCj0KCQjw7IjOBhDyARIsAFzrWQzfnxV0KVtTVGXh13avFcDk4GA8LtuxDzFZiRNVXxLxpAx2AsB7l_kaAmdsEALw_wcB&esheet=54472517&newsitemid=20260331994897&lan=en-US&anchor=TestComplete&index=10&md5=932cbdd2564532cffa33dba0ab32ed89) 中增强基于 AI 的对象检测。这将提高快速变化的应用的自动化可靠性，同时配合企业治理控制，以满足合规和质量标准。

“SmartBear 正在全力以赴，使 QA 团队能够更快行动并改进应用级测试。我们看到一些团队正奔向像 BearQ 这样完全自主的解决方案，而另一些团队则在部署支持 AI 的工具来辅助人工主导的自动化甚至手动流程，”Vineeta Puranik 在声明中表示。“我们通过帮助团队自信地采用 AI、有效地扩展测试并在软件交付加速时保持应用程序完整性，在客户的 AI 旅程中与他们并肩前行。”