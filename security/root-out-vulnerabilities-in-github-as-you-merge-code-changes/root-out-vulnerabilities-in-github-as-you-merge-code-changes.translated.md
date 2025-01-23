# Eradicating Vulnerabilities in GitHub During Code Merges

![Eradicating Vulnerabilities in GitHub During Code Merges](https://cdn.thenewstack.io/media/2025/01/db8e76c9-code-1024x597.jpg)

While there's been much talk about the need to "shift security left" to earlier stages of the software development lifecycle, not much has actually been done to make developers' lives easier, says James Wickett, CEO and co-founder of DryRun Security.

"In reality, it shifts a lot of burden to developers without really improving their lives...As an industry, we've taken tools that were designed for penetration testers and application security code reviewers, tools that were designed to run for a long time [then be triaged]. We shift those tools left...and then make developers deal with the output of those tools," he says.

"And those tools are too noisy, they easily generate too many of what we call false positives. They don't generate actionable results for developers, and they take too long to run. So those three facts alone are enough to make them unsuitable for developers, unhelpful for developers. But generally, that's the state of most tools today."

Austin, Texas-based DryRun Security applies AI and machine learning in GitHub to eradicate vulnerabilities with every code change. It recently launched Natural Language Code Policies (NLCP), enabling users to define security policies for all codebases using simple, conversational language, without worrying about languages or frameworks.

## Generating More Code, Faster

The use of AI coding assistants like GitHub Copilot is [growing rapidly](https://thenewstack.io/a-developer-health-check-on-github-copilot-and-ai-assistants/)—in a Stack Overflow survey, 76% of respondents are using or plan to use them. This means developers are [generating more and more code faster](https://thenewstack.io/code-quality-becomes-even-more-vital-in-the-ai-era/).

"Generating more code is great, but it's what happens after you generate the code—and there's a lot that happens after that. From security testing to unit testing, to overall governance, the number of deployments, and the number of dependencies that are introduced," says Martin Reynolds, field CTO at Harness, discussing Harness's 2025 State of Software Delivery report.

DryRun says that adding more security controls in the development process adds to build times, making developers reluctant to use them or reducing the frequency of code changes.

DryRun aims to help developers find problems quickly. It maintains that its contextual security analysis process running in GitHub takes only 10 seconds.

Contextual security analysis uses contextual data collected as developers write code (code path, function, author, language) to perform near real-time, context-aware assertions. It's designed for modern applications that are distributed, microservices-based, and heavily reliant on APIs and third-party components.

"The process checks five key factors of any code change...we use the acronym SLIDE to think about contextual security analysis: Surface, Language, Intent, Design, and Environment, and we gather a lot of data around all of those elements and build this contextual window for that particular code change," Wickett explains.

Using Natural Language Code Policies, you can ask questions about changes and associated risks in plain English.

## More Than Just Matching Patterns

Most security tools use Static Application Security Testing (SAST) or Software Composition Analysis (SCA)—only two data points—when there's actually a wealth of [other data that can inform the risk of a code change](https://www.linkedin.com/pulse/unpacking-contextual-security-analysis-dryrun-securitys-amit-jhvze/?trackingId=QLk5Bl8gS4%2BwvPowV1wwsQ%3D%3D), explains co-founder Ken Johnson in a LinkedIn post.

"All these previous tools that have accumulated in our industry, they're all pattern-based, and actually, we've taken the same approach to code analysis, I don't know, 20-25 years or even longer," Wickett says.
它们都基于正则表达式和模式，调用语法树。这通常是每种工具，甚至是更现代的工具所采用的方法。但这只有在你提前知道要查找哪些模式的情况下才有效，而且它也给你的开发人员或应用安全人员带来了很大的负担，他们必须编写大量的规则，并学习另一种领域特定语言，用它来表达针对不同编程语言的规则，无论是Java、Python还是其他语言。

DryRun提供了一系列分析器，用于检查身份验证/授权是否正确使用，是否暴露了秘密或敏感信息等等。

我们有自己的策略，开箱即用，可以满足大约80%到90%用户的需求。然后，通常情况下，我们的客户会发现他们有一些问题，或者他们有关于授权问题、加密设置以及与他们合作的第三方供应商更改的特定代码策略。这就是人们如何使用自然语言问题扩展产品——例如，“这个代码更改是否影响了我们的密码重置流程？”“这个代码更改是否修改了加密？”“这个代码更改是否改变了我们公司进行授权的方式？”他们可以填写与他们相关的更多详细信息，Wickett说。

## 应用大型语言模型提供相关上下文

这家拥有10名员工的初创公司于2023年成立，最近宣布获得870万美元的种子轮融资。Wickett和Johnson是应用安全领域的资深人士，定期在网络研讨会和会议上发表演讲，最近一次是关于在应用安全中整合大型语言模型（LLM）。

他们像其他人一样正在学习AI，并记录了他们如何将LLM整合到他们的工作中。

“人们使用LLM和AI做的一些事情，就是获取一段代码并将其交给AI系统，看看它会说什么。我们有自己的知识库，基于我们所有的语言和框架。我们还发现了自己独特的代码查询方法，它完全基于LLM。因此，在我们收集所有这些上下文并能够回答问题时，我们每一层都在使用LLM。

“但是……我们能够快速、准确地为开发人员提供真正的指导……我们不会将他们引导到网络上某个通用的地方，上面写着‘嘿，你看，你这里有跨站脚本，或者你有IDOR（不安全的直接对象引用）或其他漏洞。’我们实际上是在用他们自己的代码、他们自己的变量、他们的函数以及他们正在调用的方法来解释他们代码中的问题。所以它与开发人员高度相关。”Wickett说。

他坚持认为，AI和LLM能够解决传统SAST方法无法解决的问题。

“这一点尤其正确，我们发现这几乎适用于我们所有客户的授权问题，他们发布新的端点，但没有正确应用授权。开发人员意外地将错误的角色或错误的授权组件放在不同的端点上，这是一个真正的安全问题，传统的SAST工具由于其匹配模式的方式而无法解决。”

DryRun是一个在GitHub内部工作的应用程序，它与Copilot协同工作。GitLab版本正在开发中。Wickett认为，现代IDE越来越能够消除许多简单的错误，但错误只会变得越来越复杂，这强化了这样一个观点：开发人员需要快速、上下文相关的帮助来解决这些错误。

“GitHub集成确保我们的开发人员直接在其工作流程中获得精确和即时的反馈，使他们能够毫不费力地修复安全问题。该工具不仅帮助我们及早发现硬编码凭据等风险，而且还培养了开发人员的安全文化。DryRun Security是我们应用安全工具包中不可或缺的一部分，”PlanetArt的CTO Gary Gonzalez说。

[YOUTUBE.COM/THENEWSTACK 技术发展迅速，不要错过任何一集。订阅我们的YouTube频道，收看我们所有的播客、访谈、演示等等。](https://youtube.com/thenewstack?sub_confirmation=1)