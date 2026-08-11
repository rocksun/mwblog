<!--
title: 为何AI工具不懂你的公司？直到现在才有了改变
cover: https://cdn.thenewstack.io/media/2026/08/53d4086a-puneet-mishra-aqmors7rceg-unsplash-scaled.jpg
summary: Cloudflare推出开源AI工作空间平台CloudflareOS，通过基于能力的访问控制和业务上下文集成，解决企业AI工具缺乏内部业务认知及安全隐患问题，助力员工安全高效地运行动态AI应用。
-->

Cloudflare推出开源AI工作空间平台CloudflareOS，通过基于能力的访问控制和业务上下文集成，解决企业AI工具缺乏内部业务认知及安全隐患问题，助力员工安全高效地运行动态AI应用。

> 译自：[Why AI tools know nothing about your company — until now](https://thenewstack.io/cloudflare-os-agentic-workspace-security/)
> 
> 作者：Adrian Bridgwater

本周，Cloudflare 发布了其开源 AI 工作空间平台 CloudflareOS，承诺为每位员工提供配备 AI 工具并能访问公司内部系统的安全工作空间。

该平台不仅显著超越了传统的[虚拟桌面基础设施](https://azure.microsoft.com/en-us/resources/cloud-computing-dictionary/what-is-virtual-desktop-infrastructure-vdi)（VDI）服务——后者仅通过远程屏幕交付固定的应用程序——甚至超越了现代 VDI 迭代中的动态应用交付、[应用屏蔽](https://getnerdio.com/blog/fslogix-application-masking/)和流媒体技术，它提供了一种与公司内部工具、文档和系统交互的本质上更动态的工作方式。

Cloudflare 的 [CloudflareOS](https://blog.cloudflare.com/cloudflare-os/) 通过[安全连接点](https://thenewstack.io/how-devsecops-teams-should-approach-api-security/)使其应用程序和服务可访问，这些连接点会在授予访问权限之前验证每一个用户、每一个代理请求或连接点。

## 在 AI 领域，每一个新的工作会话都从零开始

其技术主张建立在一个基本事实之上：典型的企业 AI 工具对世界了解甚广，但对特定公司的运营方式、内部系统形态、审批流程或团队实际完成工作的方式几乎一无所知。

这意味着每一个新的工作会话都从零开始，员工必须不断重新解释那些 AI 本应已经掌握的背景信息。但如何安全地授予具有业务上下文感知能力的代理访问权限呢？

Cloudflare 开发者与 AI 副总裁 [Rita Koslov](https://www.linkedin.com/in/ritakozlov/) 告诉 *The New Stack*，赋能现代代理用例意味着“数据首次大规模地离开受控系统”。

“过去的情况是，例如，人们在[数据仓库](https://thenewstack.io/data-warehouses-are-terrible-application-backends/)中询问分析问题，而组织对此拥有控制权，”Koslov 说。“现在，员工正在为他们自己的工具、代理等申请 API 密钥。这产生了一类 Cloudflare OS 旨在解决的新型安全问题。”

## 基于能力的访问胜过直接移交原始 API 密钥

[Cloudflare](https://www.cloudflare.com/) 构建了所谓的基于能力的访问权限，该公司承诺这比直接将原始 API 密钥交给代理要好得多。

“API 密钥赋予代理对系统的广泛访问权限；而基于能力的访问方法允许我们授予一个特定的资源，然后准确记录代理观察到的内容，并验证任何查看其工作结果的人也有权访问该源，”Koslov 强调。

Cloudflare OS 使代理能够创建文档、幻灯片、电子表格、工作流、其他代理，甚至是全新的全栈应用程序——所有这些都根据员工的工作量身定制。它创建的内容可以保持与实时数据源的连接，被安全地修改和共享，并可供人和代理直接使用。

> “API 密钥赋予代理对系统的广泛访问权限；而基于能力的访问方法允许我们授予一个特定的资源，准确记录代理观察到的内容，并验证任何查看其工作结果的人也有权访问该源。”

就开发人员和系统运维专业人员应如何应对这一产品，Koslov 建议，如今“困难的问题不是生成一个应用程序”。相反，真正的挑战在于安全地运行成千上万（或数百万）个动态生成的应用程序，每个应用程序都需要持久状态和受控访问。

“Cloudflare OS 使用 [Dynamic Workers](https://developers.cloudflare.com/dynamic-workers/)，它们提供轻量级隔离运行时来按需加载每个应用的代码，并使用 [Durable Objects Facets](https://developers.cloudflare.com/dynamic-workers/usage/durable-object-facets/) 在平台监管下为应用提供隔离的 SQLite 存储。出站网络默认被禁用，Gatekeepers 只暴露用户明确授予的资源，”Koslov 说。“Dynamic Workers 和 Durable Objects Facets 的发明是因为这些操作以前是不可能实现的。”

为了完整起见——这再次是 Cloudflare 的原创技术服务——[Gatekeeper 是一个特定于服务的 Worker](https://github.com/cloudflare/cloudflare-os)，它位于 Cloudflare OS 和外部服务之间，用于解释和理解服务的 API、其资源以及可以在其上执行的操作。

## 当一切出错时会发生什么

Koslov 证实她知道在非托管环境中事情会失控到什么程度。

“我们从自己与其他公司交谈的经验中深知这一点。他们分享了内部数据被复制到 IT 不知情的 AI 工具中的案例、嵌入在代理构建应用程序中的 AI 密钥，甚至是数据被内部分享给原本没有权限（甚至被公开）的人，”她补充道。

构建一个定制的替代方案绝非易事；一个具有适当安全性和与内部系统真正集成的平台可能需要数年时间开发，维护成本高达数百万。在此期间，员工会寻找变通方法，IT 部门会丢失对正在运行的 AI 工具以及谁在使用它们的跟踪，成本不断堆积，却往往收效甚微。

CloudflareOS 从一个不同的前提出发：公司以 AI 能够实际执行的形式一次性捕获其知识、流程和工作方式，这些知识从第一天起就伴随着每位员工的工作空间。

## 我们如何衡量业务“背景”？

“在这种情况下，捕获的业务‘背景’可以包括公司术语、政策、操作程序、产品文档、技术标准、销售流程、模板以及执行重复工作的既定方式，”Koslov 证实。

CloudflareOS 最初是 Cloudflare 为运行其自身员工队伍而构建的平台。数千名 Cloudflare 员工每天都在使用它进行研究、创建连接到实时数据的文档、自动化重复性任务，并为他们的日常工作构建工作应用程序。

现在，该平台作为开源软件提供给任何组织。因为它通过开源并在公司自己的 Cloudflare 账户中运行，组织拥有他们在该平台上构建的所有成果。

平台本身适用于任何 AI 模型并能控制成本。通过 Cloudflare AI Gateway，组织可以使用任何 AI 模型提供商，因此不会被锁定在单一供应商中。管理员可以确切地看到支出情况，并按人、团队或应用程序进行细分。他们可以设置支出预算、速率限制，或在不需要顶级模型时将日常任务路由到更小、更经济的模型。

## 按 Token 为平台定价完全是错误的衡量标准

企业 AI 架构师兼 [Besk Tech](https://besk.tech/) 创始人 [Vladimir Beskorovainyi](https://www.linkedin.com/in/vladimirbesk/) 对这里正在发生的更广泛的故事持谨慎乐观态度，他告诉 *The New Stack*，传统上，业界是按 Token 对这些平台进行定价，“而在他看来，这完全是错误的衡量标准”。

“在 Cloudflare OS 的这个例子中，公司实际上购买的是写下 AI 驱动的业务流程究竟如何运作的义务，然后在业务发生变化时保持该描述的真实性，”Beskorovainyi 说。“模型是商品化部分。真正花钱的是经过策划的背景知识，没有人会为它从书写之日起就开始衰减这一事实做预算，而这恰恰决定了这一切能否在投入生产后存活下来。”

> “按人、团队和应用程序细分成本，这是我第一次看到供应商将支出视为工程信号而不是发票，并且将日常工作发送到较小的模型是大多数企业仍然未能采取的显而易见的下一步。”

Beskorovainyi 坚持认为，在这个游戏中获胜的组织“不一定是运行最好模型的组织”；而是那些在代理询问之前就已经能够“书面回答他们自己的审批流程是什么”的组织。

“按人、团队和应用程序细分成本，这是我第一次看到供应商将支出视为工程信号而不是发票，并且将日常工作发送到较小的模型是大多数企业仍然未能采取的显而易见的下一步，”Beskorovainyi 建议道。

## 拥有自己的背景并不意味着你的背景有多好

他澄清了自己的观点并解释说，这里的限定条件是“拥有自己的背景并不意味着你的背景有多好”，因此开源工具和社区连接加上组织自己的账户决定了谁拥有背景文件。

“两者都无法告诉我们，记录和登录到背景文件中的内容在本季度是否仍然真实。这项工作永久地留给客户，而我认为大多数此类部署都会在这里分崩离析，而不是在 Cloudflare 构建的任何东西上，”Beskorovainyi 补充道。

Cloudflare 联合创始人兼首席执行官 [Matthew Prince](https://www.linkedin.com/in/mprince/) 曾表示，他的团队构建 Cloudflare OS 的原因在于“没有其他东西能做我们需要做的事情”，因此现在，任何公司都可以从这里开始，而这正是该组织内部软件工程部门多年来才达到的水平。

这里明显的吸引力归结于 Cloudflare OS 的动态特性，以及它以默认零信任的自定义工程业务上下文感知水平与 AI 工具协作和应用的能力。该平台可以将任何输出转化为具有自身隔离数据库、实时功能和访问控制的工作应用程序——再说一次，这可不是老式的虚拟桌面，对吧？

## 无需开发人员（目前）

Cloudflare 的结论是，员工可以直接使用 Cloudflare OS 上的任何应用程序，或根据自己的需要对其进行调整，这属于“无需开发人员”的情况，或者至少在需要承担下一个集成任务、大事件到来或两者兼而有之时才需要开发人员介入。