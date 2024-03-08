# appCD Lifts Developer Load by Automating Infrastructure from Code
![Featued image for: appCD Lifts Developer Load by Automating Infrastructure from Code](https://cdn.thenewstack.io/media/2024/03/a6a369fe-appcdlogo-1024x407.png)
Maintaining that Infrastructure as Code (IaC) has failed to live up to its hype, San Francisco-based startup
[appCD](https://appcd.com/) has opened early access to what it’s calling its generative Infrastructure *from* Code (IfC) software.
The eponymous software auto-generates infrastructure from the application code and automatically applies operations and security policies.
Its creators,
[Sachin Aggarwal](https://www.linkedin.com/in/sachinyaggarwal/) and [Asif Awan,](https://www.linkedin.com/in/asifawan/) are both serial entrepreneurs, having created and sold companies in cloud, cybersecurity and [MLOps](https://thenewstack.io/what-is-mlops/).
Aggarwal says this company is based on what they’ve learned in their previous ventures, for him most recently at Accurics (acquired by Tenable), which detects and resolves security risks in IaC.
From talking with customers, he said, it became clear the underlying
[problem with IaC](https://thenewstack.io/a-brief-devops-history-the-roots-of-infrastructure-as-code/) is because it’s written manually.
“It requires expertise, it’s error-prone and it’s time-consuming,” Aggarwal said. “So the idea was born: Is there a way, especially now, given that we are all moving from a declarative world to a generative world; in the new world, is there a way to for us to generate Infrastructure as Code from the code [itself]?”
“I think there’s a problem to be solved here. I don’t think
[[Infrastructure as Code](https://thenewstack.io/infrastructure-as-code-evolution-and-practice/)] has done its job. Now it’s time to move on to the next wave of provisioning infrastructure.”
## No Changes to Code
“[Infrastructure as Code] enables the deployment, management and scaling of infrastructure through machine or direct-to-machine code. This contrasts with traditional methods that involve working through interfaces and additional software layers,” B. Cameron Gain wrote in his “
[Ultimate Guide](https://thenewstack.io/infrastructure-as-code-the-ultimate-guide/)” to IaC on The New Stack.
He added: “The use of IaC to provision and deploy infrastructure consistently and efficiently across various environments through a command line lends itself well to CI/CD.”
That manual process is what Aggarwal believes doesn’t work. And that existing IaC solutions still require too much from developers.
In a post at InfoQ, MLOps engineer
[Claudio Masolo](https://www.linkedin.com/in/cmasolo/) outlines [four primary approaches to Infrastructure from Code](https://www.infoq.com/news/2023/02/infrastructure-code-cloud-manage/): SDK-based, such as [Ampt](https://getampt.com/) and [Nitric](https://nitric.io?utm_content=inline-mention); annotation based ( [Klotho](https://klo.dev/)); a combination of the two ( [Encore](https://encore.dev/) and [Shuttle](https://www.shuttle.rs/) or AWS [Chalice](https://github.com/aws/chalice), which deploys applications that use AWS Lambda in Python); and introducing a new programming language such as [Winglang](https://www.winglang.io/) and [DarkLang](https://darklang.com/). Meanwhile, [Pulumi](https://www.pulumi.com?utm_content=inline-mention) and [AWS](https://aws.amazon.com/?utm_content=inline-mention) Cloud Development Kit ( [CDK](https://github.com/aws/aws-cdk)) are based on the idea of using existing languages.
“Our approach is pretty simple,” Aggarwal said. “We are saying that we do not want you to make any single line of changes in your code. No, there’s no SDK, there’s no annotation. … We are not giving you a new configuration language or a new descriptive language. …If you’re using Terraform, or if you’re using Helm charts or [AWS] CloudFormation, we will give you Infrastructure as Code in the languages or in the codebase that your teams are used to seeing.”
## Right Size and Right Permissions
Though the company calls its software “generative IfC,” its engine is machine-learning based rather than
[relying on generative AI](https://thenewstack.io/generative-ai-tools-for-infrastructure-as-code/).
You check your Java or Python code, the two languages it supports at this point, into a repo, and appCD does an analysis of that code, which then presents the user with what it considers the optimal infrastructure for this code. It supports Terraform,
[OpenTofu](https://thenewstack.io/opentofu-1-6-general-availability-open-source-infrastructure-as-code/) and [Helm](https://thenewstack.io/applying-kubernetes-security-best-practices-to-helm-charts/) on AWS, with support for [Microsoft](https://news.microsoft.com/?utm_content=inline-mention) Azure coming soon.
“It gives us two things,” Aggarwal said. “It allows us to do a right-sized infrastructure, because when you have different teams writing Terraform code, a context is sometimes lost, and there tends to be overprovisioning of those resources. … But more importantly, we also give you the right size permissions.”
With full context of what this application is supposed to do and the resources or other microservices it should — and should not — be communicating with, appropriate permissions are established.
Existing tools require developers to master not just application development, but also cloud infrastructure and IaC. Then there’s compliance, security and operation policies where platform engineering and security teams also weigh in. appCD maintains that developers shouldn’t have to learn anything new.
The appCD tool can:
**Analyze**code to infer API, service configuration, ingress/egress and environment variables. **Visualize**the deployment architecture, enabling users to make changes with drag-and-drop functionality. This diagram or topology, which Aggarwal describes as a “Figma meets HashiCorp kind of a thing,” enables changes, but still doesn’t require users to learn the underlying language unless they want to. **Generate**Terraform/OpenTofu or Helm charts based on the application’s inferred cloud dependencies and automatically apply standards for regulations such as HIPAA, NIST-CSF, PCI and GDPR. Company-specific policies can be added as well.
“The holy grail of accelerating deployment of applications in the cloud requires the ability to create the Infrastructure as Code in an automated, secure way with least privileges, and aligned to architectural best practices,” said
[Vishal Gupta](https://www.linkedin.com/in/vishal-gupta-046149/), CIO and CTO of Lexmark International. “appCD is closest to making this vision happen right from application code itself and bringing stellar value to platform teams.”
In addition to early access, the company announced it has $6 million in seed funding. It’s offering a
[playground environment](https://docs.appcd.io/getting-started/playground) if you want to try it out. [
YOUTUBE.COM/THENEWSTACK
Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.
](https://youtube.com/thenewstack?sub_confirmation=1)