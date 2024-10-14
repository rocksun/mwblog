# 人工智能增强代码的可追溯性：开发者指南

![Featued image for: Traceability in AI-Enhanced Code: A Developer’s Guide](https://cdn.thenewstack.io/media/2024/10/a2b257f3-krishna-pandey-knzhytpre18-unsplash-1024x576.jpg)

[Krishna Pandey](https://unsplash.com/@krishna2803?utm_content=creditCopyText&utm_medium=referral&utm_source=unsplash) on [Unsplash](https://unsplash.com/photos/text-KNZHyTpre18?utm_content=creditCopyText&utm_medium=referral&utm_source=unsplash).

生成式人工智能的快速普及已渗透到全球各行各业。随着转录工具和内容创作的广泛应用，人工智能重塑未来的潜力无限。从[人工智能将淘汰的软件工具](https://thenewstack.io/5-software-development-skills-ai-will-render-obsolete/)到新的编码方式，它对软件开发和整个行业都提出了严峻的挑战。

如今，行业面临着一个难题：如果开发者使用人工智能修改了一段代码，它是否仍然是相同的代码？[软件开发者面临的重大挑战](https://thenewstack.io/the-challenges-of-marketing-software-tools-to-developers/)之一是如何在不影响创造力或越过版权或许可法律界限的情况下做到这一点。

迄今为止，官方对此束手无策。人工智能的监管环境仍在不断发展，政策制定者和监管机构正在努力解决人工智能技术带来的潜在伦理、安全和法律挑战。美国版权局已经探索了人工智能生成作品与版权法的交叉点。然而，仍然需要一个专门针对人工智能开发者如何使用受版权保护的材料的既定、全面的代码或法律框架。在英国，知识产权局 (IPO) [最近确认](https://www.ft.com/content/a10866ec-130d-40a3-b62a-978f1202129e) 无法促成一项自愿行为准则协议，该协议将规范人工智能开发者对版权作品的使用。

在人工智能不断发展的同时，平衡知识产权与技术进步仍然是一个重大问题。

## 人工智能与开源软件——完美匹配

开源软件为训练人工智能模型提供了肥沃的土壤，因为它没有与专有软件相关的限制。它[让人工智能能够访问运行全球基础设施的许多标准代码](https://thenewstack.io/infrastructure-from-code-gives-ops-needed-freedom/)库。同时，它也暴露于人工智能带来的加速和改进，进一步增强了[开源开发](https://thenewstack.io/osis-definition-of-open-source-ai-raises-critical-legal-concerns-for-developers-and-businesses/)能力。

开发者也从人工智能中获得了巨大的益处，因为他们可以提出问题、获得答案，并且无论对错，都可以将人工智能作为创建可操作内容的基础。这种显著的生产力提升正在迅速加速和完善编码。开发者可以利用人工智能快速解决平凡的任务、获得灵感或寻找他们认为是完美解决方案的替代示例。

## 绝对确定性和透明度

然而，并非所有都是积极的。人工智能与开源软件的集成使许可证问题变得复杂。通用公共许可证 (GPL) 是一系列广泛使用的自由软件许可证（还有其他许可证），或称为“版权共享”，它保证最终用户享有四项自由：运行、学习、分享和修改软件。根据这些许可证，任何软件修改都需要在相同的软件许可证下发布。如果代码在 GPL 下获得许可，则任何修改也必须在 GPL 下获得许可。

问题就在这里。除非对软件的训练方式具有完全透明度，否则无法确定适当的许可要求或如何首先获得许可。为了避免版权侵犯和其他法律纠纷，可追溯性至关重要。此外，还存在伦理问题——如果开发者修改了一段代码，它是否仍然是相同的代码？我们已经[在这里](https://aiven.io/blog/navigating-the-creative-commons-ai-ownership-and-software-development)更详细地讨论了这个问题。

## 可追溯性
因此，迫切的问题是：开发人员可以采取哪些实际步骤来保护自己免受他们产生的代码的侵害，而软件社区的其他成员——OSS 平台、监管机构、企业和 AI 公司——可以在帮助他们做到这一点方面发挥什么作用？OSS 提供透明度以支持完整性和可追溯性的信心，因为一切都暴露在外，可以被观察到。专有软件中的错误或疏忽可能会发生，但由于它是一个封闭系统，看到、理解和修复错误的可能性实际上为零。在 OSS 中工作的开发人员在数百万人的社区面前公开运作。[社区需要确定第三方来源代码的来源](https://thenewstack.io/how-to-give-and-receive-technical-help-in-open-source-communities/)——是人类还是 AI？

## 基础
[Apache 软件基金会](https://www.apache.org/legal/generative-tooling.html) 有一项指令，要求其项目的维护人员不应使用 AI 生成的源代码。AI 可以帮助他们，但他们贡献的代码是开发人员的责任。如果发现存在问题，那么开发人员有责任解决问题。许多公司，包括 [Aiven](https://aiven.io/)，都有类似的协议。我们的指南规定，开发人员只能使用预先批准的受限生成式 AI 工具。尽管如此，[开发人员对其输出负责，需要](https://thenewstack.io/ai-engineering-what-developers-need-to-think-about-in-2024/)仔细审查和分析，而不仅仅是照单全收。这样，我们可以确保我们符合最高标准。贵公司制定了哪些指南和标准，您如何帮助制定这些标准？如果不存在，这些都是值得问的问题。
除此之外，使用 OSS 的组织可以通过采取措施来保护其流程中的风险，从而发挥作用。这包括建立一个内部 [AI 战术发现团队](https://aiven.io/blog/why-every-business-needs-an-ai-tactical-discovery-team)——专门创建来关注 AI 带来的挑战和机遇。在一个案例中，我们的团队领导了一个项目，对 OSS 代码库进行批判性分析，使用 [软件成分分析](https://thenewstack.io/software-composition-analysis-and-sboms-a-united-defense/) 等工具来分析 AI 生成的代码库，将其与已知的开源存储库和漏洞数据库进行比较。

## 在 AI 中创建信任根
尽管今天做出了努力，但围绕 AI 在 [软件开发中的作用制定新的许可和法律将需要时间](https://thenewstack.io/no-time-for-test-automation/)。关于 AI 的作用的具体内容以及用于描述它的术语，需要达成共识，而这将通过调查、审查和讨论来实现。这种挑战因 AI [开发及其在代码中的应用](https://newstack.io/3-recommended-low-code-tools-for-application-development/) 的速度而被放大。这个过程比那些试图制定参数来控制它的人快得多。

在评估 AI 是否在其输出中提供了复制的 OSS 代码时，需要考虑诸如适当的归属、许可证兼容性以及确保相应的开源代码和修改的可用性等因素。如果 AI [公司开始在其源代码中添加可追溯性](https://newstack.io/entrepreneurship-for-engineers-open-source-company-ethics/)，这将有所帮助。这将创建一个信任根，有可能在软件开发中释放出巨大的好处。

[
YOUTUBE.COM/THENEWSTACK
技术发展迅速，不要错过任何一集。订阅我们的 YouTube
频道以流式传输我们所有的播客、访谈、演示等。
](https://youtube.com/thenewstack?sub_confirmation=1)