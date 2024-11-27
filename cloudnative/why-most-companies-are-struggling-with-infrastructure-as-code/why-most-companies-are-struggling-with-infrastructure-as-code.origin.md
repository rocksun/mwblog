# Why Most Companies Are Struggling With Infrastructure as Code
![Featued image for: Why Most Companies Are Struggling With Infrastructure as Code](https://cdn.thenewstack.io/media/2024/11/7e6ecf4c-olumuyiwa-sobowale-kqidjlbcgha-unsplash-1024x683.jpg)
[Olumuyiwa Sobowale](https://unsplash.com/@holumuyiwa?utm_content=creditCopyText&utm_medium=referral&utm_source=unsplash)on
[Unsplash](https://unsplash.com/photos/a-man-sitting-in-front-of-a-computer-wearing-headphones-kQIdjLbCghA?utm_content=creditCopyText&utm_medium=referral&utm_source=unsplash).
[Infrastructure as Code](https://thenewstack.io/infrastructure-as-code-the-ultimate-guide/) (IaC) is a fundamental practice for cloud-native applications and infrastructure to define, provision, and manage IT infrastructure. Instead of requiring development and operations teams to manually configure systems through ad-hoc scripts, teams can codify their infrastructure requirements in machine-readable configuration files and automate many interim steps. This brings software engineering practices to infrastructure management, enabling organizations to provision infrastructure more efficiently for IaC to improve modern IT operations is significant: it promised to increase consistency, reduce human error, and significantly improve the speed and reliability of infrastructure deployments, but [it hasn’t entirely panned](https://thenewstack.io/infrastructure-as-code-is-dead-long-live-infrastructure-from-code/) out that way.
Automating infrastructure provisioning and management *could* enable organizations to scale their environments rapidly, maintain version control over infrastructure changes, and ensure that development, testing, and production environments remain consistent. This is more important than ever in today’s cloud-native and [microservices](https://thenewstack.io/microservices/)-based architectures, where infrastructure needs to be flexible, reproducible, and easily managed at scale. Despite all the potential benefits, IaC remains a thorny challenge for most organizations. The gated, contextless processes leading up to IaC creation and deployments are slowing engineering teams and adding costly overheads to businesses in a GenAI world.

## Current State of IaC Adoption
According to [Stacked Up: The IaC Maturity Report](https://stackgen.com/stackedup-infographic-2024), only 13% of organizations have achieved IaC maturity. However, the majority (51%) indicated that only some of their infrastructure was represented in code, and 10% were still in the early stages, having only a small portion of infrastructure stored in code in pilot projects. These numbers scarcely paint a picture of IaC maturity in organizations. Given the many promised benefits of IaC, what’s holding organizations back from complete and mature adoption?

## Achieving IaC Maturity Is *Hard*
Simply put, achieving IaC maturity is more complicated than it sounds. Indeed, 60% of respondents agreed, “IaC is a powerful concept, but in practice, it hasn’t delivered all the benefits we had hoped for.” Nearly all respondents (97%) reported difficulties with IaC, sharing the following as the most pressing concerns:

- 56% had trouble enforcing consistent configurations despite extensive tooling
- 54% faced
[challenges related to managing](https://thenewstack.io/platform-engineering-overcoming-data-management-challenges/)multiple tools - 45% had difficulty determining ownership of IaC, unsure who was responsible for building templates, deploying them, and maintenance of the infrastructure
While [IaC aims to make infrastructure management](https://thenewstack.io/amid-licensing-uncertainty-how-should-iac-management-adapt/) and deployment faster and easier, 51% of developers shared that they dedicate more than 20% of their time to IaC. This has significant cost implications for organizations. It’s hardly an ideal outcome for developers, who are supposed to be building new apps and services or increasing business differentiation for existing ones. Just 17% of respondents shared that their dev team had achieved the goal of spending less than 10% of their time on IaC.

“99% of infrastructure professionals report that switching between IaC tools causes mental task disruption.”

Faced with these challenges, 75% of infrastructure stakeholders agreed with the statement, “It’s frustrating to be responsible for chasing down IaC configuration errors when anyone can make changes.” Those untracked changes to IaC increase the potential for security vulnerabilities and governance risks, putting the organization at risk. Organizations must increase their IaC maturity to eliminate the possibility of untracked changes and related increased risk.

## 6 Key Areas to Improve
The research identified multiple areas for process improvement across roles to increase IaC maturity, primarily in these six areas:

- 43% lacked the skills to write effective IaC
- 32% were concerned about ensuring governance and security in IaC
- 31% faced challenges with documentation
- 28% worried about ensuring consistency in IaC
- 28% faced difficulties with managing IaC
- 25% wished for better support in IaC for specific application needs
Only 2% of respondents didn’t feel the need to improve their current IaC processes, further emphasizing the challenges most organizations face with IaC maturity.

## Improving IaC Maturity
To address these challenges, 93% of respondents agreed that innovation was needed to make IaC faster and more streamlined. Right now, the responsibility for writing and maintaining IaC is widely distributed, which makes it more challenging to ensure that IaC is and remains secure and compliant, both during creation and while being maintained. Maturing technologies could help manage those distributed responsibilities and increase alignment with best practices without adding more cognitive load.

One specific technology that could help with current struggles is generative Infrastructure from Code (IfC), where the IaC itself is automatically generated from the application code and built with guardrails that align with best practices. 46% of survey respondents indicated that generating IaC directly from the application code would be advantageous. IfC addresses many challenges teams face, eliminating the IaC ownership, time, and skill issues that many organizations struggle with. Recently, Gartner recognized IfC as an emerging paradigm in their annual Hype Cycle, indicating that the future belongs to seamless, automated, and context-aware methods of creating IaC.

Managing cloud systems is a constantly evolving ecosystem, requiring development, infrastructure, and executive teams to learn new technologies and skills to continuously deliver customer applications. While IaC has enabled more streamlined and scalable deployment opportunities compared to manual processes, new technologies are necessary to increase overall IaC maturity and deliver the value organizations require. Organizations looking to increase their IaC maturity and simplify infrastructure provisioning should investigate IfC as a solution that achieves both goals.

*This article is part of The New Stack’s contributor network. Have insights on the latest challenges and innovations affecting developers? We’d love to hear from you. Become a contributor and share your expertise by filling out this form or emailing Matt Burns at mattburns@thenewstack.io.*
[
YOUTUBE.COM/THENEWSTACK
Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.
](https://youtube.com/thenewstack?sub_confirmation=1)