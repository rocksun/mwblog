随着AI编码代理的兴起，开发人员已经开始尝试复杂的、多步骤的升级请求。由于Spring是目前最流行的Java框架，开发人员可以通过“请将此应用程序升级到Spring Boot 4”这样的自然语言命令来升级应用程序，这无疑是一个令人兴奋的前景。

然而实际上，以这种方式升级可能会令人扫兴，尤其是如果涉及的是一个非常庞大的遗留项目。开发人员必须等待20分钟甚至更长时间才能得到初步结果。在此之后，开发人员通常还需要进行多轮迭代来修复编码和编译错误，更不用说测试用例了。

升级一个在整个应用程序中使用的主要框架需要大量的测试和检查：即使代码能够编译并且看起来技术上是正确的，框架的运行方式也可能发生了微小的变化，或者升级中可能存在以微妙的新方式工作的新功能，这些功能直到运行时才会显现出来。

这种反复的过程在两个方面造成了成本累积：

1. 假设代码库不依赖于内部共享库或框架，这个过程已经消耗了1到2天的时间。而且，这并不能保证变更能够成功合并（例如，CI检查可能会失败，开发人员可能会拒绝PR等）。如果没有编码代理，这个过程可能需要更长的时间，但结果往往更具确定性：人类程序员的工作通常是有效的，并且是可以合并的。
2. 使用代码生成时，还需要考虑Token成本。这包括初始运行和每次迭代的成本。

如果框架升级的原因是为了解决CVE（常见漏洞与披露），时间就更为关键，尤其是当你需要进行重大升级时。你希望尽快部署补丁以消除任何潜在的安全风险。

## 示例：升级Spring Petclinic

作为一个例子，我们来看看将Spring Petclinic从Spring Boot 3.5.x升级到Spring Boot 4的过程。Spring Petclinic应用程序包含的实体非常少（兽医、所有者、预约），而且设计相对简单且良好。使用AI从Spring Boot 3.5.x迁移到Spring Boot 4，在规划阶段消耗了478,380个Token，在代码变更阶段消耗了908,900个Token……但最终还是失败了。

出了什么问题？编码助手试图进行一些我没有要求的更改，例如更新或重命名Spring启动器（starters）和导入语句。此外，还有几个关于使用已弃用方法的编译器警告，以及一个编译错误。这意味着我需要更多的迭代来修复它，从而消耗了更多的Token和时间。

*在Spring升级中使用AI编码代理的挑战：错误和已弃用的方法通常需要多次迭代才能解决，如Spring Petclinic示例所示。*

这还是从较新版本的Spring进行升级。如果我的目标是从旧版本（如2.7.x）升级到Spring Boot 4，情况会更糟，因为中间会有很多步骤可能出错。

在我的经验中，这*确实*会出错。值得注意的是，Broadcom估计，在2025年，仍有约50%的Spring Boot应用程序处于Spring Boot 2.7或更早版本。

## 当升级成为必然

工程团队升级到新版本Spring Boot的主要原因之一是为了解决安全问题。这在当前尤为真实，Broadcom发现[漏洞发现出现了大规模激增](https://blogs.vmware.com/tanzu/how-to-prepare-for-the-world-of-ai-driven-exploits/)。许多组织现在认识到，升级是其安全准备策略的一部分。

像Petclinic这样的演示应用程序的升级烦恼/成本是一回事，但在生产环境中，组织比以往任何时候都更需要升级，以解决依赖于彼此的多个Git存储库中的安全问题。在这些情况下，实践[持续升级](https://blogs.vmware.com/tanzu/what-is-a-continuous-upgrade-culture-and-why-is-it-important/)非常有帮助。通过将所有依赖项版本保持在支持范围内并使用最新的补丁版本，持续升级文化减少了CVE影响你的代码的时间窗口，并让你能够获得Java和Spring的最新优化，从而节省基础设施成本。

此外，标准化促进了在所有应用程序中使用相同的Spring版本，从而能够跨应用程序共享内部Spring组件。虽然并不总是可行，但一个更同质化、或者至少在支持范围内的Spring生态确实有助于第2天的维护和持续升级，因为流程变得更加一致。为了促进标准化，你需要考虑规模化运营。因此，真正关键的问题是“我们如何能更高效地大规模升级Spring？”

正如我们在Petclinic这样简单的项目中发现的那样，尽管编码代理可以让你更快地编写升级更改，但编码代理并不完美，也不免费。毕竟，它们[按定义是非确定性的](https://thenewstack.io/the-non-deterministic-nature-of-ai-coding-agents/)，因此它们不可预测、不一致，也不会总是给出准确的结果。

> “编码代理可以让你更快地编写升级更改，但编码代理并不完美，也不免费。毕竟，它们按定义是非确定性的，因此它们是不可预测的。”

因此，主要问题是“如何在大规模应用AI进行升级时加速该过程并应用更正确的代码更改？”根据我的经验，要大规模获得良好的结果，你需要用能够执行类型安全且确定性重构的额外工具来增强你的编码代理。

为了理解人机回环（HITL）如何改进升级，让我们先为编码代理的工作原理打下基础。

## 类型感知的必要性：解决代理的局限性

[编码代理](https://thenewstack.io/open-source-coding-agents-like-opencode-cline-and-aider-are-solving-a-huge-headache-for-developers/)是旨在利用大语言模型（LLM）根据一组配置好的工具或技能来生成最佳答案的产品。编码代理是利用大语言模型（LLM）和工具来生成代码及相关工件（如配置和文档），并执行命令（包括编译、运行测试甚至部署代码）的应用程序。有些人更喜欢用“harness”而不是“编码代理”这个词。

在这种语境下，“工具”可以是任何命令行工具（如Maven或Gradle），而“技能”则是我们配置的自然语言描述和一些脚本，用以强制代理在特定情况下执行。

编码代理在设计时考虑了可扩展性；例如，这些工具可以通过（远程或本地）[MCP服务器](https://thenewstack.io/why-the-mcp-server-is-now-a-critical-microservice/)进行扩展。技能的设计简单且易于添加；它们本质上只是存储在特定目录中的Markdown文件。

一个常见的困惑是，开发人员假设编码代理会像人类一样对代码库进行语义分析以执行代码更改，从而获得更高的质量和保真度。我了解到这是不正确的。

默认情况下，编码代理（Claude、Cursor、Copilot）并不理解代码库中出现的每个表达式的类型或正确性，这就是为什么编码助手有时会引入编译错误的原因。

你可以通过[连接MCP服务器的语言服务器协议（Language Server Protocol）](https://github.com/isaacphi/mcp-language-server)来减少错误，这是一种某些IDE或开发工具支持的技术，但除了极少数情况外，将其用于执行代码更改并不常见。在Java方面，用于设计确定性代码更改（配方）的最灵活的开源技术是OpenRewrite，它作为Maven或Gradle插件执行，可以解析代码库中每个表达式的类型（是的，就像IDE的自动补全机制一样）。

为了解决这些问题，Tanzu Platform和Tanzu Spring拥有一些基于OpenRewrite的CLI命令，帮助编码代理规划和升级Spring应用程序。这些Tanzu解决方案引导你的编码代理大规模地规划和执行增量Spring升级。CLI将处理弃用、API更改、属性更改，甚至处理复杂的案例，例如依赖于Spring或其传递依赖项且必须首先升级的内部框架和第三方开源库升级。

如果你正在使用Tanzu Platform，最简单的入门方法是在终端中运行“cf repo unpack-skills”，然后让你的编码代理升级Spring。这将解压一个技能，使你的编码代理能够执行“cf repo upgrade-plan”来规划升级，并执行“cf repo apply-upgrade-plan”来执行计划的第一步，即应用代码更改。

否则，你可以使用Tanzu Spring Essentials，它包含了对App Advisor CLI的访问，你只需要使用[App Advisor本地MCP服务器](https://techdocs.broadcom.com/us/en/vmware-tanzu/spring/application-advisor/1-5/app-advisor/model-context-protocol-server.html)，它会教会你的编码代理使用相应的CLI命令来获取和应用升级计划，但每个开发人员都需要维护CLI版本和配置。

有时，工程团队需要在升级到Spring的主要版本之前进行高级规划。这种规划可能需要删除新版本中不再支持的项目，并迁移到兼容的替代方案，[例如Spring Boot 4中的Spock集成](https://github.com/spring-projects/spring-boot/wiki/Spring-Boot-4.0-Migration-Guide%23features-removed-from-this-release)。

可能还存在一些API破坏性更改，需要额外的上下文（例如，一种新类型的异常，或将方法修饰符更改为将公共方法变为受保护的方法）才能应用最合适的重构。这只是一个例子，每个组织都需要决定一个共同的方法来解决这些不兼容问题并集中化解决方案。

## 大规模平衡确定性与非确定性

当你决定如何解决Spring升级期间或任何内部库的问题时，VMware Tanzu Spring团队建议遵循这一原则：如果不兼容问题的解决方案是确定性的，我们建议组织创建自己的配方，并使用我们的Tanzu CLI工具配置常见的迁移模式（例如，从Spock迁移到JUnit）。

> “如果不兼容问题的解决方案是确定性的，我们建议组织创建自己的配方，并使用我们的Tanzu CLI工具配置常见的迁移模式。”

在大规模场景下，该解决方案的成本将远低于要求开发人员使用AI编码代理采取原始方法，因为使用App Advisor CLI不需要Token，无论是用于测试还是用于跨数百个Git存储库应用更改。

否则，如果某个不兼容问题的解决方案是非确定性的，我们建议你创建一个集中存储在Git存储库中的技能集，你的编码代理可以在应用Spring Boot升级之前或之后选择使用。

现在，如果你考虑大规模升级Spring，这个过程不应该由任何开发人员触发。它应该由你的[CI/CD](https://thenewstack.io/ci-for-coding-agents/)流水线自动触发，然后直接通过CLI配置，或者如果你有所需的额外技能，则通过AI编码代理进行配置。使用这种设置，你可以防止将大量Token用于不一定能提供良好结果的重复性任务，而可以将Token消耗在你实际的业务问题上，而不仅仅是升级框架。

*欲了解更多信息，请访问[VMware Tanzu Spring](https://www.vmware.com/products/app-platform/tanzu-spring)。*