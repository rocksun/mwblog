
<!--
title: MetalBear Mirrord 为 AI 代理提供测试代码的预演环境
cover: https://cdn.thenewstack.io/media/2025/09/396152b0-metalbear-foundersphoto.jpg
summary: Mirrord 是一款开发者工具，用于在 Kubernetes staging 环境中测试应用。它通过拦截本地进程并将其路由到 staging 集群，避免了繁琐的本地环境设置和部署流程。随着 AI 编码代理的兴起，Mirrord 解决了集成测试的瓶颈问题，使开发者和 AI 代理能够更高效地进行测试和调试。MetalBear 提供 Mirrord 的商业版本，增加了企业功能，如访问控制和监控。
-->

Mirrord 是一款开发者工具，用于在 Kubernetes staging 环境中测试应用。它通过拦截本地进程并将其路由到 staging 集群，避免了繁琐的本地环境设置和部署流程。随着 AI 编码代理的兴起，Mirrord 解决了集成测试的瓶颈问题，使开发者和 AI 代理能够更高效地进行测试和调试。MetalBear 提供 Mirrord 的商业版本，增加了企业功能，如访问控制和监控。

> 译自：[MetalBear's Mirrord Gives AI Agents a Staging Environment To Test Their Code](https://thenewstack.io/metalbears-mirrord-gives-ai-agents-a-staging-environment-to-test-their-code/)
> 
> 作者：Frederic Lardinois

[Mirrord](https://metalbear.com/mirrord/) 长期以来一直是开发者的热门工具，他们希望针对功能齐全的 staging 环境测试其基于 Kubernetes 的应用程序，而不是公司技术堆栈的本地模拟。

mirrord 无需设置本地环境，而是让开发人员直接针对 staging 环境进行编码，方法是让该工具拦截所有本地进程，并将它们直接重新路由到 staging 集群。这意味着开发人员可以保持工作流程，而无需经历将代码打包到容器上并将上下文切换到持续集成平台等过程。

随着 AI 编码代理的兴起，现在有更多的代码需要测试，并且代理本身也越来越需要访问这些 staging 环境。

测试正变得越来越成为瓶颈，除非开发人员想依赖不完整的本地测试，否则他们需要经历越来越多的内部开发循环之外的部署周期。

[![](https://cdn.thenewstack.io/media/2025/09/737dc215-metalbear-productphoto.png)](https://cdn.thenewstack.io/media/2025/09/737dc215-metalbear-productphoto.png)

*图片来源：MetalBear。*

“AI 已经解决了除 mirrord 所做的一切，” MetalBear 的 CEO 兼联合创始人 Aviram Hassan 告诉我。MetalBear 是一家初创公司，致力于 mirrord 的开发。“你可以使用 AI 生成代码。你可以在某种本地级别对其进行测试——单元测试、组件测试。你可以审查代码。但是，一旦涉及到集成测试，你实际上并没有一个好的解决方案。因此，这个瓶颈只会变得更加突出，因为有更多的代码需要使用相同的有限资源进行测试。”

他认为，对于每个循环都必须经历一个新的部署周期会增加太多的摩擦，并且在快速迭代日益成为竞争优势的时代减慢了业务发展。

“整个行业已经接受了这一点，认为这是正常的，但实际上这是当今软件开发中最大的隐藏瓶颈，”他说。

借助 mirrord，并且如果需要，还可以使用 Metalbear 的企业服务，开发人员可以在与完整的 staging 环境以及在其中运行的微服务、数据库、消息队列和第三方服务交互时调试他们的代码。

代理系统也可以根据需要使用相同的环境。正如 MetalBear CTO 兼联合创始人 Eyal Bukchin 告诉我的那样，该团队首先构建了一个 MCP 服务器。毕竟，这是连接 AI 代理和工具的显而易见的事情。但事实证明，通过使用 Agent.md 文件或类似的指令来告诉代理它可以访问此环境就足够了。

“我们意识到，今天，你可以给代理一个 Markdown 文件，他们在执行任何操作之前都会阅读该文件，然后在 Markdown 中，你写道：好的，Claude，要进行测试，这是你运行的命令。你可以阅读有关 mirrord 及其作用的信息——但老实说，它只是知道。最后，使用 mirrord 运行你的服务来测试集群，”Bukchin 解释说。

Bukchin 和 Hassan 将 mirrord 的开源版本描述为功能齐全，该团队目前主要专注于错误修复。MetalBear 的商业产品才是该团队目前最重视的地方。在那里，该团队刚刚筹集了 1250 万美元的种子轮融资以将该服务商业化，他们遵循了构建开源公司的成熟策略，即在 mirrord 之上添加企业功能。

这些功能包括能够更好地管理访问同一 staging 环境的多个客户端、支持部署到多个 Pod，以及通常的管理和支持功能，例如基于角色的访问控制以及监视和审计日志。MetalBear 的服务起价为 50 美元/席位/月。还有一个额外的企业计划可用，该计划增加了诸如支持 airgapped 集群和 CI 管道中的 mirrord 支持等功能。