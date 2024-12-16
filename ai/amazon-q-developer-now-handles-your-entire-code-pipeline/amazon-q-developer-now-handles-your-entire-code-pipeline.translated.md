# Amazon Q Developer 现已全面掌控您的代码流水线

![Amazon Q Developer 现已全面掌控您的代码流水线特色图片](https://cdn.thenewstack.io/media/2024/12/43e1cea7-rose-galloway-green-mzpnzk3prtu-unsplash-1-1024x602.jpg)

今天在 [AWS re:Invent](https://reinvent.awsevents.com/) 上，[AWS](https://aws.amazon.com/?utm_content=inline+mention) 为其基于生成式 AI 的 [Amazon Q Developer](https://thenewstack.io/amazon-revamps-developer-ai-with-code-conversion-security/) 软件开发平台带来了新的增强功能，以应对整个软件开发生命周期。

新功能包括自动化 [单元测试](https://thenewstack.io/unit-tests-are-overrated-rethinking-testing-strategies/)、[文档](https://thenewstack.io/poor-documentation-is-costly-heres-how-to-fix-it/) 和 [代码审查](https://thenewstack.io/how-to-find-success-with-code-reviews/) 的代理，以帮助开发人员在整个软件开发过程中更快地构建软件。AWS 还引入了一项新功能，帮助用户在极短的时间内解决操作问题——可以说是 DevOps。

Amazon Q Developer 产品管理总监表示：“Amazon Q Developer 是功能最强大的基于生成式 AI 的软件开发助手……它适用于软件开发生命周期的所有方面，无论您是构建新应用程序、重写应用程序、调试、测试还是在生产中操作应用程序，还是转换现有应用程序。”

Amazon Q Developer 可通过 AWS 管理控制台、与 [GitLab](https://about.gitlab.com/?utm_content=inline+mention) 的新集成产品以及集成开发环境 (IDE) 等方式获得。

具体来说，Amazon Q Developer 可在 [Visual Studio](https://marketplace.visualstudio.com/items?itemName=AmazonWebServices.AWSToolkitforVisualStudio2022)、[Visual Studio Code](https://marketplace.visualstudio.com/items?itemName=AmazonWebServices.amazon-q-vscode)、[JetBrains IDEs](https://plugins.jetbrains.com/plugin/24267-amazon-q/)、[Eclipse](https://marketplace.eclipse.org/content/amazon-q)、[JupyterLab](https://docs.aws.amazon.com/amazonq/latest/qdeveloper-ug/jupyterlab-setup.html)、[Amazon EMR Studio](https://docs.aws.amazon.com/amazonq/latest/qdeveloper-ug/emr-setup.html) 或 [AWS Glue Studio](https://docs.aws.amazon.com/amazonq/latest/qdeveloper-ug/glue-setup.html) 等 IDE 中使用。除了能够在 [AWS 管理控制台](https://console.aws.amazon.com/) 中使用 [Amazon Q Developer](https://aws.amazon.com/q/developer/) 之外，还可以通过 [AWS 控制台移动应用程序](https://aws.amazon.com/console/mobile/)、[Amazon CodeCatalyst](https://docs.aws.amazon.com/codecatalyst/latest/adminguide/managing-generative-ai-features.html)、[AWS Support](https://docs.aws.amazon.com/amazonq/latest/qdeveloper-ug/support-chat.html)、[AWS 网站](https://aws.amazon.com/) 或通过 Slack 和 Microsoft Teams 使用 [AWS Chatbot](https://docs.aws.amazon.com/amazonq/latest/qdeveloper-ug/q-in-chatbot.html)。

## 节省时间和金钱

对 Amazon Q Developer 的增强功能将大大减少开发人员花费在编写文档和单元测试或进行代码审查等繁琐任务上的时间。

表示：“大多数开发人员平均每天花一个小时编写代码。”“那么他们剩下的时间都花在哪里呢？他们剩下的时间都花在了软件开发生命周期的其他方面……这些方面是他们必须执行的费时费力的工作。”

即使在使用这些新功能之前，[亚马逊已经能够通过内部使用 Q Developer 节省大量时间和成本](https://thenewstack.io/devs-slash-years-of-work-to-days-with-genai-magic/)。

表示：“亚马逊通过将 30,000 个 Java 应用程序转换为新版本，每年节省了 4,500 个开发人员年的手动工作和 2.6 亿美元的性能改进。”

他指出，新功能将带来更多节省。

“今天，我们正在扩展 Amazon Q Developer 代理的功能，以实现：1) 增强代码库中的文档 (`/doc`)，2) 支持代码审查以检测和解决安全和代码质量问题 (`/review`)，以及 3) 自动生成单元测试并提高测试覆盖率 (`/test`)"
AWS云计算部门首席开发者布道师在博客文章中写道：“在您首选的IDE或（预览版）[GitLab Duo with Amazon Q](https://aws.amazon.com/blogs/aws/introducing-gitlab-duo-with-amazon-q)（这是最受欢迎的企业DevOps平台之一）中，贯穿整个软件开发生命周期。”

Constellation Research的分析师告诉The New Stack：“单元测试生成、文档生成和代码审查是必须完成的关键活动，但它们会消耗时间，因此Q Developer的任何自动化帮助都将提高开发人员的速度，并提高他们的满意度，因为他们可以花更多时间做他们喜欢的事情——编码。”


## 自动化AI驱动的测试生成
Amazon Q Developer自动化了识别和生成单元测试的过程。

公司在一份声明中表示：“在IDE中，开发人员只需在Amazon Q Developer聊天窗口中键入‘/test’，或突出显示相关的代码块，右键单击并选择‘test’。Amazon Q Developer随后利用其对整个项目的了解，自主识别和生成测试，并将这些测试添加到项目中，帮助开发人员快速验证代码是否按预期工作。在GitLab中，开发人员可以使用Amazon Q Developer以及合并请求上的‘/q test’快速操作来自动生成代码测试，从而节省时间并提高整个组织的测试覆盖率。”

IDC分析师告诉The New Stack，IDC预测GenAI将彻底改变遗留应用程序的重构，企业将利用GenAI工具和云服务提供商平台启动和执行75%的代码转换和开发任务。

他表示：“AWS在过去12个月中在Amazon Q方面取得的进展令人惊叹。除了生成新代码外，它还可以用于转换遗留应用程序。”“我也喜欢Amazon Q现在可以帮助客户更好地利用AWS控制台进行安全扫描和调试。”

除了在内部使用Q Developer的新功能外，AWS还允许一些合作伙伴试用这项技术。

例如，通过为其开发人员配备Amazon Q Developer的自动化单元测试代理，表示该公司预计将减少25%的手动测试时间，在项目中以20%的速度实现完整的测试覆盖率，并在开发周期的早期修复更多错误——从而加快最终的人工审查速度。公司表示，借助Amazon Q Developer，正在积极提高开发效率和代码质量，节省了15%的开发成本。

同时，德勤正在通过使用Amazon Q Developer自动识别和生成单元测试来减少手动测试时间。总体而言，德勤的开发人员正在提高30%的开发速度，同时保持安全标准。

![](https://cdn.thenewstack.io/media/2024/12/34a7b33c-aws-unit-test-1.jpg)
要在您的IDE中开始代码审查，请打开聊天面板并键入/review。

## 易于生成的AI文档
此外，Amazon Q Developer现在还自动化了生成和更新文档的过程，使开发人员可以轻松维护项目准确、详细的信息。


文档生成代理会自动生成和更新文档，确保文档准确并与代码更改同步，并帮助新团队成员更快地理解代码。它还可以更新现有文档并回答有关文档的问题。

## GenAI驱动的代码审查
据AWS称，新的Q Developer代码审查代理自动化了代码审查过程，以提供快速反馈，识别安全漏洞和性能问题等问题，并在开发早期发现最佳实践违规行为。

简而言之，它将审查时间从几天缩短到几分钟。

通过充当第一审阅者，Amazon Q帮助开发人员尽早发现和解决代码质量问题，从而节省了未来审查的时间。
AWS在一份声明中表示，代码审查代理将标记可疑的代码模式，识别开源软件包的风险，并评估将更改发布到生产环境的潜在影响。此外，Amazon Q将使用开发人员合并请求中的上下文来调整其建议，确保代码建议与其风格和偏好一致。

## GenAI驱动型运维 (GenAIOps?)
最后，AWS利用其超过17年的丰富运营经验，运营着全球最大、最可靠的云，为用户提供自动化AI功能。

Ijaz表示，Amazon Q Developer现在可以帮助运营人员和开发人员在很短的时间内调查和解决其AWS环境中的运营问题。

在一份声明中，AWS解释了其工作原理：“一旦Amazon CloudWatch警报发出，Amazon Q Developer可以自动开始调查。它利用其对组织AWS资源的深入了解——包括Amazon CloudWatch、AWS CloudTrail、AWS Health和AWS X-Ray中的信息——可以快速筛选数十万个数据点，以发现服务之间的关系，并了解它们如何协同工作以识别相关信号中的异常情况。

“在分析其发现后，Amazon Q会向用户提供问题的根本原因的潜在假设，并指导用户如何解决问题——这是其他任何主要云提供商都不具备的功能组合。”

此外，AWS表示，用户还可以在检查系统信号（例如延迟峰值或显示用户遇到错误的日志）时，通过在AWS管理控制台中选择“调查”或通过询问其AWS资源（例如，“我的AWS Lambda函数运行缓慢。它出了什么问题？”）来启动调查。

![](https://cdn.thenewstack.io/media/2024/12/4b7fddfa-aws-operations-1.png)
如何使用Amazon Q Developer进行运营调查。

## 一件大事，一件非常大的事
总的来说，这对AWS来说是一个重大的发布，它在整个开发生命周期中都提供了GenAI辅助。这种策略是该公司的差异化因素，很少有其他公司（如果有的话）能够提供。

Moor Insights and Strategy分析师Andersen告诉The New Stack：“这绝对是一个非常重大的发布。对我来说，关注整个SDLC（软件开发生命周期）在整个市场中脱颖而出。传统上，开发环境以编码为中心，但Q Developer采取这种更全面的方法，非常符合开发人员角色的变化。但说实话，这些功能是我最喜欢部分的基础。”

Andersen最喜欢的是Q Developer转换功能如何将整个生命周期焦点指向一些非常大的IT挑战。

他说：“例如，许多应用程序都被保留原样，因为从技术或人员配置的角度来看，重构它们太可怕了。”“但是Q Developer能够检查和记录应用程序并为项目提供见解。这是一个与现实生活中做事方式更一致的过程。”

Mueller告诉The New Stack，不可否认的是，亚马逊在re:Invent上的重点是不仅帮助开发人员进行编码，而且还提高软件开发生命周期相邻用例的生产力。

他说：“环境故障排除也是一项受欢迎的新功能，因为没有什么比环境问题更能阻碍开发人员的生产力了——通常规模更大，因为它会影响在该环境中工作的整个开发团队。”

Ijaz表示，将AWS与Amazon Q Developer与竞争对手区分开来的核心差异化因素包括：

- 综合生命周期支持，涵盖构建、运营和转换应用程序，因为它不仅仅是代码编写辅助。
- 安全性和合规性——因为它采用负责任的AI实践构建，符合严格的隐私标准，基于Bedrock（符合HIPAA和GDPR），并且客户数据保持私密，不会用于训练底层模型
- 企业重点——因为它专为高度管制的行业而设计，使其适用于医疗保健、金融和情报部门，因为它构建在AWS的安全云架构之上

事实上，Q Developer中的新功能代表了AWS支持整个软件开发生命周期的战略，同时保持企业级安全性和合规性标准。重点是自动化日常任务，使开发人员能够专注于更有价值的创造性工作。

Ijaz说：“我们的目的是真正帮助开发人员节省他们不喜欢做的事情的时间，让他们利用这段时间来构建真正不同、具有创新性并且他们真正喜欢做的事情。”
[YOUTUBE.COM/THENEWSTACK](https://youtube.com/thenewstack?sub_confirmation=1)

技术发展日新月异，不要错过任何一期节目。订阅我们的YouTube频道，收看我们所有的播客、访谈、演示等等。