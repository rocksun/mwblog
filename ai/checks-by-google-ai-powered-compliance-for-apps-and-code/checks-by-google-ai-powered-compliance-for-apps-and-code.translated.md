# Google Checks: AI-Powered Compliance for Apps and Code
![Featured image for Google Checks: AI-Powered Compliance for Apps and Code](https://cdn.thenewstack.io/media/2024/10/a672fe71-checksbygoogle-1024x577.jpg)

Google is making its AI-powered compliance platform publicly available as [Google Checks](https://checks.google.com/). It includes three new products that will check apps, code, and soon, [AI models](https://thenewstack.io/beyond-prompt-engineering-governing-prompts-and-ai-models/) for compliance issues, including personally identifiable information, government regulatory requirements, and whether developer models will “say the wrong thing,” providing controversial or inappropriate responses.

Google Checks originated from [Google’s Area 120 incubator](https://area120.google.com/) and was used internally to test Google’s own large language models, said [Fergus Hurley](https://www.linkedin.com/in/fergushurley/), co-founder and general manager of Google Checks.

“We’re providing insights and tools for these companies because most of them don’t have the insights and tools they need,” he said. “Some of our customers include the top five social media apps, the top five gaming companies, the top five financial apps, these companies are well-resourced, but they just don’t have the insights to get the job done. We’re bridging the gap between development teams and compliance teams.”

Google Checks integrates with [Vertex](https://cloud.google.com/vertex-ai), Google Cloud’s generative AI product, but also works with other major model providers. Vertex offers more than 150 generative AI models, including [Anthropic’s Claude](https://thenewstack.io/a-nue-ux-web-framework-plus-anthropic-openai-boost-ai-apis/) and [Mistral](https://thenewstack.io/gemma-google-takes-on-small-open-models-llama-2-and-mistral/).

## App Compliance
Google Checks offers three products: [App Compliance](https://checks.google.com/app-compliance/), which is now available, and [Code Compliance](https://checks.google.com/code-compliance/) and [AI Safety](https://checks.google.com/ai-safety/), which are currently in closed beta and require a waitlist.

App Compliance checks apps, websites, or services to see if they comply with rules for collecting user data. For example, it can check for compliance with Europe’s [GDPR](https://www.gdpradvisor.co.uk/gdpr-countries), California’s [CCPA](https://oag.ca.gov/privacy/ccpa), and Brazil’s [LGPD](https://www.dlapiperdataprotection.com/index.html?t=law&c=BR).

“We look at what apps need to do based on different regulations around the world,” Hurley said. “We cover those rules, and if you have users in those regions, we turn those checks on.”

App Compliance can also analyze publicly available apps to check for compliance with any organization’s privacy policies. It relies on an LLM fine-tuned for understanding privacy policies, comparing them to what the app or product actually does, and performing dynamic and static analysis, he said. For example, checking the app running on an actual physical device, monitoring network traffic coming from the app, and the user experience.

“We have a smart AI crawler that looks at what the app actually does. It can play games, it can log into apps if you give it login credentials, but it’s a smart AI crawler.”

— Fergus Hurley, co-founder and general manager of Google Checks
“We’ve built our own fine-tuned model for understanding privacy policies, and now many teams at Google use it,” he said. “We’re able to identify potential issues with products from a compliance perspective. We have a smart AI crawler that looks at what the app actually does. It can play games, it can log into apps if you give it login credentials, but it’s a smart AI crawler.”

Hurley pointed out that co-founder [Nia Cross Castelly](https://www.linkedin.com/in/niacastelly/) is a lawyer, though Hurley reminded that AI does not provide legal advice.

“She was responsible for [Google Play](https://play.google.com/store/games?hl=en_US) policies, which developers have to strictly adhere to in order to get access to billions of users,” he said. “So we do have a lawyer overseeing things, but we don’t provide legal guidance. That’s important.”

Instead, the AI simply provides [insights and tools to bridge the gap between development](https://thenewstack.io/6-development-insights-to-empower-it-teams/) teams and compliance teams, he added.

## Code Compliance
Code Compliance is in closed beta and allows developers to address regulatory issues before an app is released. It can be integrated into IDEs so developers receive alerts about issues directly in their IDE, integrated into their build systems, Hurley said.
代码合规性提供有关关键问题的的信息，其中可能包括安全问题，但也可能检测到例如过时的 SDK。

“我们还帮助人们在 Google Play 上创建、管理和维护他们的安全标签，”他说。“那是圣杯，能够成为人们需要去的地方，以获得所有合规性见解。”

## AI 安全

第三个产品正在封闭测试中，是 AI 安全。

Hurley 说，开发人员在 AI 和 [AI 驱动的应用程序](https://thenewstack.io/5-best-practices-for-building-reliable-genai-apps/) 中需要解决三个主要问题。首先，他们需要能够设置自己的策略，他称之为“对齐阶段”。在此阶段，他们确定哪些策略与他们及其网站或应用程序相关。

其次，他们需要进行评估，以确保这些策略符合他们最初的模型发布，反之亦然。第三，在实际发布 GenAI 产品后，开发人员需要确保它在野外正常运行。

“我们构建了一个产品来帮助解决这些部分中的每一个，作为这个 AI 安全产品的一部分，所以实际上，它试图在这里建立治理指挥中心，”他说。“在第一阶段，对齐，人们希望能够配置他们的策略，而现在，我们支持每个通用产品真正需要的核心策略，围绕暴力、仇恨言论和敏感数据——例如 PII（个人身份信息）。”

他说，评估阶段帮助开发人员确定策略是否符合他们最初的模型发布，反之亦然。他说，在这个阶段，该产品使用 Google 内部开发的提示进行红队攻击和副词测试。

![显示 Google 检查框架中的三个问题：应用程序需要做什么；应用程序说它在做什么；以及应用程序实际在做什么。](https://cdn.thenewstack.io/media/2024/10/c1fd99cc-checksbygoogleframework.jpg)
Google 检查框架的屏幕截图

红队攻击是一种 [安全测试技术](https://thenewstack.io/security-testing-must-be-part-of-software-development-life-cycle/)，它涉及模拟对系统或组织的恶意攻击，以识别漏洞并评估弹性。这个名字来自一个受控的战争游戏，其中一个红色 [团队试图突破目标的安全性](https://thenewstack.io/what-can-incident-teams-learn-from-crisis-management/)，而一个蓝色团队则进行防御。对抗性测试是一种软件测试，它涉及故意尝试通过引入意外或恶意输入来破坏应用程序或系统。它有助于发现可能被恶意行为者利用的弱点。

“开发人员在构建完模型后会遇到一个难题，那就是想出这些对抗性提示，而我们拥有庞大的对抗性提示库，这非常有价值，这也是我们利用 Gemini 和 Gemma 以及其他 Google 团队所做的大量工作的地方，”他说，并补充说它还包含了这些团队开发的最佳实践。“我们将这些提示针对开发人员模型运行，并确保形成该模型的响应是开发人员想要的。”

这一步不容小觑。AI 模型不仅会产生可能在公众面前令人尴尬的陈述，而且还会提供错误的信息，从而给公司造成经济损失。

“人们有时会试图让模型做一些它们不应该做的事情，”他说。“最公开的案例之一是加拿大航空公司的一个案例，他们的代理人回复说这个人可以获得退款。最终发生的事情是加拿大航空公司说，‘不，根据这些条件，你不能获得退款。’”

他说，这导致了一场诉讼，最终 [加拿大航空公司不得不提供退款](https://www.cbsnews.com/news/aircanada-chatbot-discount-customer/)。

“现在已经设定了规则，公司对其 GenAI 代理所说和所做的事情负责，他们确实有这种责任，”他说。“确保代理人遵守公司的政策至关重要，但这是防止模型根据公司的政策进行微调以仅谈论公司实际提供的服务的公开示例之一。”

“开发人员在构建完模型后会遇到一个难题，那就是想出这些对抗性提示，而我们拥有庞大的对抗性提示库，这非常有价值，这也是我们利用 Gemini 和 Gemma 以及其他 Google 团队所做的大量工作的地方。”

— Fergus Hurley
第三，一旦 GenAI 产品发布，[开发人员需要能够监控](https://thenewstack.io/monitoring-developer-metrics-team-approach-is-best/)它在实际环境中的行为是否正确。例如，曾经有一家公司发布了一个通用 AI 代理来满足特定用例，但人们发现他们可以“破解”它并免费访问实际上使用起来非常昂贵的模型。

“最重要的是确保事情不会偏离轨道，并制定相应的保障措施，”他说。“我们有一个护栏产品，它会监控输入提示和输出提示，并检测问题，例如不应该到达模型的输入提示，比如有人试图破解模型，然后在输出方面，模型不应该暴露任何 PII，并且应该有许多保障措施来防止这种情况发生。”

他指出，如果开发人员不想自己进行微调，他们可以使用护栏来自动创建监控和保障措施。

“他们可以进入并选择输入护栏，[例如]我想开启破解预防，”他说。“假设他们已经用不同的敏感度阈值配置了这些不同的护栏，那么他们就可以配置输出阈值，然后将其作为模型的一部分部署到生产环境中。”

护栏充当模型的过滤器，而不是直接对其进行微调。他补充说，过滤器不会显着影响性能。

## 可根据行业和重点定制
他补充说，谷歌提供的检查也可以根据行业进行定制。例如，如果一个应用程序处理儿童数据，那么该应用程序必须遵循非常具体的规则。

“我们与一些最大的儿童游戏公司合作，”他说。“你可以想象医疗保健和金融或其他受严格监管的主要行业都有自己非常具体的需求，而目标是随着时间的推移建立起这个检查生态系统，让人们能够开启与他们的业务最相关的检查。”

Hurley 说，谷歌产品的检查涵盖了所有类型的开发人员；他们看到[前端开发人员](https://roadmap.sh/frontend)，以及[后端](https://roadmap.sh/backend)和[全栈开发人员](https://roadmap.sh/full-stack)都在使用这些工具。

目前，开始使用是免费的，尽管一些企业比较复杂，确实需要付费服务来帮助他们进行合规性，他说。

[YOUTUBE.COM/THENEWSTACK
科技发展迅速，不要错过任何一集。订阅我们的 YouTube
频道，观看我们所有的播客、访谈、演示等。
](https://youtube.com/thenewstack?sub_confirmation=1)