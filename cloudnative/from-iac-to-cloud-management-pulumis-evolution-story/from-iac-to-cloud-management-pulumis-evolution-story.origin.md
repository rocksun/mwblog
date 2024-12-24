# From IaC to Cloud Management: Pulumi’s Evolution Story
![Featued image for: From IaC to Cloud Management: Pulumi’s Evolution Story](https://cdn.thenewstack.io/media/2024/10/0aaf99a0-chuttersnap-tsgwbumanue-unsplash-1024x684.jpg)
[Pulumi](https://thenewstack.io/pulumi-templates-for-genai-stacks-pinecone-langchain-first/) for seven years has been building out its flagship [Infrastructure as Code](https://thenewstack.io/infrastructure-as-code-in-any-programming-language/) (IaC) offering to give developers and [DevOps](https://thenewstack.io/devops/) teams an easier and open source way to automate the creation and management of their cloud infrastructure.
They can do so with whatever programming language they want, from C# and YAML to Python, [Go](https://thenewstack.io/russ-cox-steps-down-as-tech-lead-of-go-programming-language/), and Java. They can deploy their creations to any of more than 170 cloud providers that make sense to them, including the giants like [Amazon Web Services (AWS)](https://aws.amazon.com/?utm_content=inline+mention), Microsoft’s Azure, and [Google Cloud](https://cloud.google.com/?utm_content=inline+mention) Platform.

It’s been working for the company, with co-founder and CEO [Joe Duffy](https://www.linkedin.com/in/joejduffy/) noting in a recent blog post that Pulumi had [more than 100 million downloads](https://www.pulumi.com/blog/pulumi-up-2024/) of Pulumi IaC and had gotten 167% the contributions of [HashiCorp](https://thenewstack.io/hashicorps-radar-scans-repos-commits-and-pulls-for-leaks/)’s [Terraform](https://thenewstack.io/terraform-isnt-dead/) in previous weeks and 300% of [OpenTofu](https://thenewstack.io/opentofu-amiable-to-a-terraform-reconciliation/).

“Not only is Pulumi the most powerful IaC technology, it is becoming more popular and vibrant too,” Duffy wrote.

Now the company finds itself in an IaC market that is undergoing an upheaval of sorts as HashiCorp, which in recent years has become a dominant player, prepares to be folded into the massive IBM universe, with [Big Blue buying the company](https://thenewstack.io/ibm-buying-hashicorp-what-devs-analysts-and-competitors-are-saying/) for [$6.4 billion in a deal](https://thenewstack.io/ibm-purchases-hashicorp-for-multicloud-it-automation/) expected to close by the end of the year. The acquisition will open even more room in an already competitive and evolving market to vendors like Pulumi.

And it’s a big and growing space to be in on. According to analysts with Fortune Business Insights, the global IaC market will jump from $908.7 million in last year to [more than $3.3 billion by 2030](https://www.fortunebusinessinsights.com/infrastructure-as-code-market-108777).

The company will move forward not only with Pulumi IaC but now also with a security management offering in [Pulumi ESC](https://www.pulumi.com/product/secrets-management/) and [Pulumi Insights](https://www.pulumi.com/product/pulumi-insights/) for cloud management. Duffy and other executives have talked about these products in the past, but at its recent PulumiUP virtual event, they brought them all together to create a unified platform they said will address all of developers’ infrastructure needs.

“This is the first time that Pulumi has really come out as a multiproduct platform,” Duffy told The New Stack. “We’re known for our Infrastructure as Code product, which is open source. That’s still powering everything we’re doing here. Insights wouldn’t have been possible without the Pulumi IaC foundation. Now we have these three independent products that are better together, but that can be adopted independently. We’re really trying to be a trusted partner. If you’re a VP of infrastructure, we’re trying to solve every mission-critical problem that you have.”

## More Than a Year in the Making
The Seattle-based company [gave the industry a first look](https://thenewstack.io/pulumi-intros-new-secrets-management-platform-engineering-tools/) at Pulumi ESC — for “environments, secrets, and configuration” — last year and hundreds of organizations participated in a public beta. It’s now generally available. For developers, Pulumi ESC is a central spot for managing all of those environments, secrets, and configurations, sitting squarely between their sources, such stores as HashiCorp’s Vault, AWS Secrets Manager, Azure Key Vault, [Google Cloud](https://thenewstack.io/google-cloud-adds-genai-core-enhancements-across-data-platform/) Secrets Manager, Password1, and Pulumi Cloud Secrets, and target environments such as those same major cloud providers as well as GitLab, Docker containers, [Kubernetes](https://thenewstack.io/kubernetes/), Cloudflare Workers, and Pulumi itself.

“It’s fully automated. You define in a central location all your secrets, all of your environments, and then developers can consume them and compose them,” he said. “It integrates with existing secret stores. … We give them one standard interface into all of it and then on the other side so developers can easily consume, but the infrastructure and the security team can audit all the access and control all the access and revoke access if they have to from one place. You don’t have to stay on top of a dozen different places where we might see secrets. Just go to one central location.”

## Pulumi Bulks Up Security
Within the platform, it’s Pulumi’s security offering, which becomes increasingly important as more enterprise data and applications migrate into the cloud. This tool is important for all companies big and small, Duffy said.

“A lot of a lot of the most critical data companies have and the most critical assets companies have are now in the cloud, which means potentially open to the internet,” he said. “People are no longer able to rely on the illusion of physical security with data centers. Now they have to think about software-based security.”

It’s been this way for a while, but accelerated during the COVID-19 pandemic, when organizations emptied their offices and business became highly distributed and cloud-based. Still, in a lot of ways, security is still an afterthought, even in these [shift-left days](https://thenewstack.io/shifting-left-is-now-mainstream-for-developers-or-is-it/), he said.

“The way people develop and ship the software, security is often an afterthought in the sense that developers write code, infrastructure teams put that code in the cloud, and then security teams are now chasing down all the issues that are being found, whether those are CVEs and unpatched containers or VMs that are accessible to the internet, misconfigurations in the in the cloud infrastructure itself,” Duffy said. “A lot of the tools and software today is geared towards assuming the chaos already exists and ‘Let’s go find and fix problems.’”

However, with the push to shift left and the accelerated pace driven by continuous integration and continuous delivery, businesses want their developers to be in the driver’s seat and iterating quickly, shipping code to the cloud with few roadblocks and little friction. Shipping code is done multiple times a day, not once a quarter. Managing secrets is the key to that.

“One of the vectors of mistakes is secrets and making sure that your most sensitive information, whether it’s database passwords or tokens or application keys to go access your [accounts] are handled safely and securely,” Duffy said. “To be able to shift left, your developers need to have a solution where they know all of those things are going to be secure at all times. It needs to be baked in. It can’t be something you basically layer on afterwards.”

## Getting Insights into Cloud Infrastructure
[Pulumi](https://www.pulumi.com) started with Insights early in 2023, giving organizations visibility, intelligence, and control over their multiple cloud environments. Like ESC, the goal with Insights is to make security and more by default, but via a cloud asset and compliance management service. It’s not just helping developers and others know what they have where, but now also gives them compliance remediation capabilities, search, resource visualization, and AI-based insights. It was a step beyond what Pulumi had been doing.
“That wasn’t directly in our wheelhouse, but we … understand the entirety of all these clouds because of our infrastructure is good product,” he said. “What we said is, ‘If we had a way to discover all of the resources you’ve got, wherever they are, and bring them into that data model that we kind of already had with search and AI and all these great things over it, then we would be able to deliver better visibility.’ That combined with our policies code engine, which is already doing compliance for infrastructure-as-code workloads, we figured out a way to actually leverage all that work we’ve done and just apply it to any infrastructure wherever you’re running it.”

## A Bigger, Better Insights
The first iteration of Insights included search and dashboards for IaC infrastructure and the ability to export it to Snowflake. Pulumi bulked up Insights 2.0, enabling organizations bring its capabilities to all of their cloud infrastructure wherever it is. It supports almost 200 clouds and gives an instant inventory of all cloud assets. There are full pivot tables, customizable reports and dashboards inside Pulumi, search and Pulumi Copilot for discovering cloud resources and interactively ask questions.

The feature also leverages Pulumi’s CrossGuard Policy as Code feature, which includes the ability to automate remediations so that Insights can not only alert to security or compliance issues but also helps teams fix them by clicking on a button.

It addresses the ability to use AI to fix a problem but also the desire as well to have some level of human intervention, something that Pulumi wrestled with.

“We debated for a while because a lot of us would like it to be the case that everything is in a CI/CD pipeline and there’s a software development lifecycle process around it and we’d always follow that,” Duffy said. “You’d never go click a button to fix it an issue. But if you’re sitting there staring at a security violation, you probably want the button that just says, ‘Go fix it,’ even though you’re going to have some workflow afterward to make sure it’s fixed permanently, and there are Jira tickets involved in that and all of these things. I do think it’s going to be a key differentiator for us.”

## Pulumi Kubernetes Operator 2.0
Meanwhile, earlier this month, the company released the Pulumi Kubernetes Operator 2.0 beta, which enables users to deploy and manage cloud infrastructure from within their Kubernetes environment. With the 2.0 release, Pulumi solved the scalability and isolation limitations that affected early adopters.

The Pulumi Kubernetes Operator defines a Kubernetes Custom Resource called `pulumi.com/v1/Stack`
, which represents a Pulumi [stack](https://www.pulumi.com/docs/concepts/stack/), [Eron Wright](https://www.linkedin.com/in/eronwright), a software engineer at Pulumi, wrote in a [blog post](https://www.pulumi.com/blog/pulumi-kubernetes-operator-2-0/). The Pulumi stack can be authored in any supported Pulumi language (TypeScript, Python, Go, .NET, Java, YAML) and can deploy and manage cloud infrastructure in any supported cloud (AWS, Azure, GCP, Kubernetes and 60+ additional cloud and SaaS providers). The Pulumi Kubernetes Operator triggers cloud deployments based on changes to the `Stack`
Custom Resource or the resources it uses, Wright said.

As a result, the Pulumi Kubernetes Operator enables users to specify the desired state of their cloud infrastructure by using resources managed directly in their Kubernetes cluster. Modifying those Kubernetes resources will trigger creation, updates, and deletion of the underlying cloud infrastructure that they manage, the company said.

## PulumiUP Europe
Pulumi will showcase this and other key products at the upcoming PulumiUP Europe conference, being held virtually on Nov. 20.

In addition to product information, Pulumi will sponsor sessions on topics ranging from platform engineering to DevOps and security.

For instance, by 2026, 80% of development companies are expected to have internal platform services and teams to improve development efficiency, according to Gartner. As platform engineering continues to reshape how organizations manage infrastructure, integrating DevOps and security becomes essential for building scalable, secure platforms. This includes challenges and opportunities when integrating DevSecOps into platforms of scale to ensure developer autonomy while maintaining governance and compliance.

## Shortcomings of IaC
[StackGen](https://stackgen.com/), a generative [Infrastructure from Code (IfC)](https://blog.stackgen.com/what-is-infrastructure-from-code) company, released research on Oct. 30 that highlights significant challenges with IaC adoption. Key findings from their survey of 315 participants include that 97% of IaC users report difficulties and only 13% of organizations have achieved IaC maturity. In addition, 56% of developers said they spend over 20% of their time on infrastructure management.
Moreover, some of the main challenges include security and reliability concerns (56% struggle with consistent configurations). However, according to StackGen, IfC is emerging as a potential solution, though only 22% are currently familiar with it.

StackGen positions its IfC solution as addressing these challenges by automatically generating infrastructure configurations from application source code, with built-in security and compliance standards.

[
YOUTUBE.COM/THENEWSTACK
Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.
](https://youtube.com/thenewstack?sub_confirmation=1)