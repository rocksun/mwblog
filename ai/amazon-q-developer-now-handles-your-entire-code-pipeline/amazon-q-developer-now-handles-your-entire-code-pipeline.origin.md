# Amazon Q Developer Now Handles Your Entire Code Pipeline
![Featued image for: Amazon Q Developer Now Handles Your Entire Code Pipeline](https://cdn.thenewstack.io/media/2024/12/43e1cea7-rose-galloway-green-mzpnzk3prtu-unsplash-1-1024x602.jpg)
Today at [AWS re:Invent](https://reinvent.awsevents.com/), [AWS](https://aws.amazon.com/?utm_content=inline+mention) delivered new enhancements to its [Amazon Q Developer](https://thenewstack.io/amazon-revamps-developer-ai-with-code-conversion-security/) generative AI-based ([GenAI](https://thenewstack.io/generative-ai-in-2023-genai-tools-became-table-stakes/)) software development platform to address the entire software development lifecycle.

New features include agents thatf automate [unit testing](https://thenewstack.io/unit-tests-are-overrated-rethinking-testing-strategies/), [documentation](https://thenewstack.io/poor-documentation-is-costly-heres-how-to-fix-it/), and [code reviews](https://thenewstack.io/how-to-find-success-with-code-reviews/) to help developers build faster across the full software development process. AWS also has introduced a new capability to help users address operational issues in a fraction of the time — DevOps, if you will.

[Adnan Ijaz](https://www.linkedin.com/in/adnanijaz/), director of product management for Amazon Q Developer, told The New Stack, “Amazon Q developer is the most capable generative AI-powered assistant for software development… it works across all aspects of software development life cycle, whether you’re building a new application, re-writing applications, debugging, testing or operating the application in production or transforming an existing application.”
Amazon Q Developer is available through the AWS Management Console, through a new integrated offering with [GitLab](https://about.gitlab.com/?utm_content=inline+mention), as well as integrated development environments (IDEs), and more.

Specifically, Amazon Q Developer is available across IDEs such as [Visual Studio](https://marketplace.visualstudio.com/items?itemName=AmazonWebServices.AWSToolkitforVisualStudio2022), [Visual Studio Code](https://marketplace.visualstudio.com/items?itemName=AmazonWebServices.amazon-q-vscode), [JetBrains IDEs](https://plugins.jetbrains.com/plugin/24267-amazon-q/), [Eclipse](https://marketplace.eclipse.org/content/amazon-q), [JupyterLab](https://docs.aws.amazon.com/amazonq/latest/qdeveloper-ug/jupyterlab-setup.html), [Amazon EMR Studio](https://docs.aws.amazon.com/amazonq/latest/qdeveloper-ug/emr-setup.html), or [AWS Glue Studio](https://docs.aws.amazon.com/amazonq/latest/qdeveloper-ug/glue-setup.html). And in addition to being able to use [Amazon Q Developer](https://aws.amazon.com/q/developer/) in the [AWS Management Console](https://console.aws.amazon.com/), it is available through [AWS Console Mobile Application](https://aws.amazon.com/console/mobile/), [Amazon CodeCatalyst](https://docs.aws.amazon.com/codecatalyst/latest/adminguide/managing-generative-ai-features.html), [AWS Support](https://docs.aws.amazon.com/amazonq/latest/qdeveloper-ug/support-chat.html), [AWS website](https://aws.amazon.com/), or through Slack and Microsoft Teams with [AWS Chatbot](https://docs.aws.amazon.com/amazonq/latest/qdeveloper-ug/q-in-chatbot.html).

## Saving Time and Money
The enhancements to Amazon Q Developer will drastically reduce the time developers spend doing tedious tasks like writing documentation and unit tests or doing code reviews.

“Most developers spend on average an hour writing code each day,” Ijaz told The New Stack. “So where are they spending the rest of their time? They are spending the rest of their time on other aspects of software development lifecycle… those aspects are time-consuming, tedious jobs that they have to perform.”

Even prior to the use of these new capabilities, [Amazon was able to save considerable time and cost using Q Developer internally](https://thenewstack.io/devs-slash-years-of-work-to-days-with-genai-magic/).

“Amazon saved 4,500 developer years in manual work and $260 million in performance improvement annually by transforming 30,000 Java applications to a new version,” Ijaz said.

The new features will enable even more savings, he noted.

“Today, we’re expanding Amazon Q Developer agent capabilities for: 1) enhanced documentation in codebases (`/doc`
), 2) supporting code reviews to detect and resolve security and code quality issues (`/review`
), and 3) generating unit tests automatically and improving test coverage (`/test`
) across the software development lifecycle in your preferred IDE or [GitLab Duo with Amazon Q](https://aws.amazon.com/blogs/aws/introducing-gitlab-duo-with-amazon-q) (in preview), which is one of the most popular enterprise DevOps platforms,” wrote [Channy Yun](https://www.linkedin.com/in/channy/?originalSubdomain=kr), a principal developer advocate for AWS cloud, in a [blog post](https://aws.amazon.com/blogs/aws/new-amazon-q-developer-agent-capabilities-include-generating-documentation-code-reviews-and-unit-tests/).

“Unit test generation, documentation generation and code review are key activities that have to be done, but consume time and therefore any automation help from Q Developer, will increase developer velocity, but also satisfaction as they can spend more time doing what they love — coding,” [Holger Mueller](https://www.linkedin.com/in/holgermueller/), an analyst at Constellation Research, told The New Stack.

## Automatic AI-Driven Test Generation
Amazon Q Developer automates the process of identifying and generating unit tests.

“From the IDE, developers just type ‘/test’ in the Amazon Q Developer chat window or highlight the relevant block of code, right-click, and select ‘test,’ the company said in a statement. “Amazon Q Developer then uses its knowledge of the entire project to autonomously identify and generate tests and add those tests to the project, helping developers quickly verify that the code is working as expected. In GitLab, developers can use Amazon Q Developer with the ‘/q test’ quick action on a merge request to automatically generate tests for the code, saving time and improving test coverage across the organization.”

IDC predicts GenAI will reinvent refactoring of legacy apps, with enterprises utilizing GenAI tools and cloud service provider platforms to initiate and execute 75% of code conversion and development tasks by 2027, [Dave McCarthy](https://www.linkedin.com/in/davemccarthymba/), an analyst at IDC, told The New Stack.

“It’s amazing how much progress AWS has made with Amazon Q over the last 12 months. In addition to generating new code, it can also be used to transform legacy applications,” he said. “I also like that Amazon Q can now help customers make better usage of the AWS console for security scans and debugging.”

In addition to using the new features in Q Developer internally, AWS allowed several partners to test drive the technology.

For instance, by equipping its developers with Amazon Q Developer’s agent for automated unit testing, [Boomi](https://boomi.com/?utm_content=inline+mention) said it expects that the company will reduce manual testing time by 25%, achieve complete test coverage on projects 20% faster, and fix significantly more bugs early in the development cycle — accelerating the final, human-led reviews. With Amazon Q Developer, Boomi is proactively enhancing development efficiency and code quality, saving 15% in development costs, the company said.

Meanwhile, Deloitte is cutting manual testing time by using Amazon Q Developer to automatically identify and generate unit tests. Overall, developers at Deloitte are increasing their development speed by 30% while maintaining security standards.

![](https://cdn.thenewstack.io/media/2024/12/34a7b33c-aws-unit-test-1.jpg)
To start the code reviews with your IDE, open the chat panel and type /review.

## Easy AI-Generated Documentation
Also, Amazon Q Developer now automates the process of producing and updating documentation, making it easy for developers to maintain accurate, detailed information on their projects.

“It’s important because as your code base grows, you have to keep the documentation in sync,” Ijaz said. “Often today, either the documentation doesn’t exist or if it exists, it gets stale pretty quickly. And what’s worse than having no documentation is having stale documentation. So, what we are doing, we’re launching a new agent that automates the process of producing and updating high-quality and accurate documentation.”

The documentation generation agent automatically produces and updates documentation, keeps documentation accurate and in sync with code changes and helps new team members understand code faster. It also can update existing docs and answer questions about them.

## GenAI-Driven Code Reviews
According to AWS, the new Q Developer code review agent automates the code review process to provide quick feedback, identifies issues like security vulnerabilities and performance problems and finds best practice violations early in development.

In short, it reduces review time from days to minutes, Ijaz said.

By acting as a first reviewer, Amazon Q helps developers detect and resolve code-quality issues earlier, saving them time on future reviews.

AWS, in a statement, said the code review agent will flag suspicious code patterns, identify open source package risks, and assess the potential impact of releasing changes to production, the company said. Also, Amazon Q will use the context from the developer’s merge request to adjust its recommendations, ensuring code suggestions are consistent with their style and preferences.

## GenAI-Driven Operations (GenAIOps?)
Finally, AWS has tapped into its more than 17 years of extensive operational experience running the world’s largest and most reliable cloud, to provide users with automated AI capabilities.

Amazon Q Developer now helps operators and developers investigate and resolve operational issues across their AWS environment in a fraction of the time, Ijaz said.

In a statement, AWS explained how it works: “As soon as an Amazon CloudWatch alarm goes off, Amazon Q Developer can automatically start investigating. Utilizing its deep knowledge of an organization’s AWS resources — including information across Amazon CloudWatch, AWS CloudTrail, AWS Health, and AWS X-Ray — it can quickly sift through hundreds of thousands of data points to discover relationships between services and develop an understanding of how they work together to identify anomalies across related signals.

“After analyzing its findings, Amazon Q presents users with potential hypotheses for the root cause of the issue and guides users through how to fix it — a combination of capabilities that no other major cloud provider offers.”

Moreover, AWS said users can also initiate an investigation when checking system signals, like a latency spike or logs showing users running into an error, across the AWS Management Console by selecting “Investigate” or from the Amazon Q chat by asking about their AWS resources, such as, “My AWS Lambda function is running slow. What is wrong with it?”

![](https://cdn.thenewstack.io/media/2024/12/4b7fddfa-aws-operations-1.png)
A look at how you can now use Amazon Q Developer for operational investigations.

## A Big Deal, a Very Big Deal
Overall, this is a big release for AWS, bringing GenAI assistance throughout the entire development lifecycle. This strategy is a differentiator for the company that not many others, if any, can provide.

“It’s a very big release for sure, [Jason Andersen](https://www.linkedin.com/in/jasontandersen/), an analyst with Moor Insights and Strategy, told The New Stack. “To me, the focus on the entire SDLC [Software Development Lifecycle] stands out in terms of the overall marketplace. Traditionally, the development environment centered on the coding, but Q Developer’s taking this more holistic approach really fits into how the developer role is changing. But honestly, these capabilities are the underpinning for what is my favorite part.”

Andersen’s favorite part is how the Q Developer transformation capabilities take the whole lifecycle focus and point it at some very big IT challenges.

“For example, a lot of apps are just left as they are because refactoring them is just too scary from a technology or staffing perspective,” he said. “But Q Developer has the ability to inspect and document apps and provide insight to the project. It’s a process that is inherently more in line with how things are done in real life.”

Undeniably, Amazon’s focus at re:Invent is on helping not only developers with coding but also with making adjacent use cases of the software development value chain more productive, Mueller told The New Stack.

“The environment troubleshooting is also a welcome new capability, as nothing stalls developer productivity more than environment issues — often even on a grander scale as it affects the full developer force working in that environment,” he said.

Ijaz said the core differentiators separating AWS with Amazon Q Developer from competitors include:

- Comprehensive Lifecycle Support, which covers building, operating, and transforming applications as it goes beyond just code writing assistance.
- Security and Compliance — as it is built with responsible AI practices, meets strict privacy standards, is built on Bedrock (which is HIPAA eligible and GDPR compliant), and customer data remains private and isn’t used to train underlying models
- Enterprise Focus — as it is designed for highly regulated industries, making it suitable for healthcare, financial, and intelligence sectors because it built on AWS’s secure cloud architecture
Indeed, the new capabilities in Q Developer represent AWS’s strategy to support the entire software development lifecycle while maintaining enterprise-grade security and compliance standards. The focus is on automating routine tasks to enable developers to concentrate on more creative work that adds more value.

“The intent is to really help developers save time from things that they don’t enjoy and let them use that time to build things that really are different, are innovative and they really enjoy doing,” Ijaz said.

[
YOUTUBE.COM/THENEWSTACK
Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.
](https://youtube.com/thenewstack?sub_confirmation=1)