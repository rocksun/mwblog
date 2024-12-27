# Infrastructure as Code in 2024: Why It’s Still So Terrible
![Featued image for: Infrastructure as Code in 2024: Why It’s Still So Terrible](https://cdn.thenewstack.io/media/2023/12/aec929b1-year-wrapup-1-1024x576.png)
From deep within the Looker traffic reports of The New Stack, we have unearthed the most viewed posts from 2024 about the subject of [Infrastructure as Code (IaC)](https://thenewstack.io/infrastructure-as-code/). Collectively, what they show is that, despite IaC’s promise in scaling IT systems, it still has many issues that drive DevOps folks crazy.

“Having used Terraform extensively, I genuinely appreciate the magic of Infrastructure as Code as an accelerant. However, refactoring is a reality of ‘Day 2’ operations and doing this with Terraform is still extremely painful to get right,” [Matt Moore](https://www.linkedin.com/in/mattmoor/), founder and CTO of security company [Chainguard](https://www.chainguard.dev/?utm_content=inline+mention), told TNS.

Cloud services created the need for the practice of “Infrastructure as Code*,” *as organizations set up their operations on [Amazon Web Services](https://aws.amazon.com/?utm_content=inline+mention) and other providers. Declarative, domain specific languages were created by [Puppet](https://thenewstack.io/puppets-open-source-community-plans-to-fork-the-program/) and [Chef](https://www.chef.io?utm_content=inline+mention) and as a way to automate configuration and provisioning work in setting up and maintaining these systems.

And [Kubernetes](https://roadmap.sh/kubernetes), with its ability to orchestrate microservices, put this practice into overdrive. And so [HashiCorp’s](https://www.hashicorp.com/?utm_content=inline+mention) [Terraform](https://thenewstack.io/new-terraform-features-manage-migrations-modules/) surfaced to manage this next level of cloud provisioning.

But despite the great value Terraform and associated IaC tools have brought, [DevOps teams](https://thenewstack.io/DevOps/) are feeling more frustrated than ever.

The New Stack’s’ 10 most popular IaC stories from 2024 show the frustrations they are feeling, and some possible paths going forward.

**1.** [Infrastructure as Code Is Dead: Long Live Infrastructure from Code](https://thenewstack.io/infrastructure-as-code-is-dead-long-live-infrastructure-from-code/)
[Infrastructure as Code Is Dead: Long Live Infrastructure from Code](https://thenewstack.io/infrastructure-as-code-is-dead-long-live-infrastructure-from-code/)
In this contributed post, [Asif Awan](https://www.linkedin.com/in/asifawan/), co-founder and chief product officer at a company then called [appCD](https://thenewstack.io/appcd-lifts-developer-load-by-automating-infrastructure-from-code/) but now known as [StackGen](https://stackgen.com/), noted that managing, maintaining and deploying applications and infrastructure securely and consistently remains an incredibly complicated challenge.

“Just as IaC expanded the ability to deploy to the cloud, it added complexity to that deployment by combining teams with different experiences and expertise and requiring them to find new ways to work together,” Awan noted.

The solution, he suggested was to “generate the infrastructure your application needs based on the version of your application being deployed.”

This approach he called “Infrastructure from Code.”

**2.** [How We Evolved from IaC to Environments as Code](https://thenewstack.io/how-we-evolved-from-iac-to-environments-as-code/)
[How We Evolved from IaC to Environments as Code](https://thenewstack.io/how-we-evolved-from-iac-to-environments-as-code/)
[Edan Evantal](https://www.linkedin.com/in/edan-evantal-2153764), CTO of [Quali](https://www.quali.com/?utm_content=inline+mention) noted that IaC tools were designed for velocity and automation, not as the source of truth for environments. Great for deploying cloud services, they are pretty terrible as a tool for predicting how code changes can change app performance
Also, IaC tools don’t play nicely together.

He noted that Quali rethinks the IaC process, defining everything a developer needs to launch an environment, in such a way that it is easy for machines and humans to understand. Then, teams can use [GitOps](https://thenewstack.io/4-core-principles-of-gitops/) as a base to launch applications.

**3.** [Terraform Isn’t Dead](https://thenewstack.io/terraform-isnt-dead/)
[Terraform Isn’t Dead](https://thenewstack.io/terraform-isnt-dead/)
[Nitric](https://nitric.io?utm_content=inline+mention)‘s [Rak Siva](https://www.linkedin.com/in/rak-siva-b9360816a/) is also a proponent of Infrastructure *from *Code (IfC).
The problem, Siva wrote, is”when a developer decides to replace a manually managed storage bucket with a third-party service alternative, the corresponding IaC scripts must also be manually updated, which becomes cumbersome and error-prone as projects scale. The desync that occurs between the application and its runtime can lead to serious security implications, where resources are granted far more permissions than they require or are left rogue and forgotten.”

He added, “Infrastructure from Code automates the bits that were previously manual in nature. Whenever an application changes, IfC can help provision resources and configurations that accurately reflect its runtime requirements, eliminating much of the manual work typically involved.”

Siva noted that the the developer doesn’t write the low-level configuration code, for tasks like setting up IAM roles and permissions, but rather, they just need to know its available.

Nitric offers an open source IfC framework for building in your language of choice and deploying to all the major clouds.


Infrastructure as Code is unidirectional and has an asymmetric experience where changes (writes) and observations (reads) are performed through different tools. What are some consequences of that? Is it really necessary?

[https://t.co/O1WJX6yhic][#infrastructureascode]— Brian Grant (@bgrant0607)

[December 23, 2024]

**4.** [OpenTofu Project Denies HashiCorp’s Allegations of Code Theft](https://thenewstack.io/opentofu-project-denies-hashicorps-allegations-of-code-theft/)
[OpenTofu Project Denies HashiCorp’s Allegations of Code Theft](https://thenewstack.io/opentofu-project-denies-hashicorps-allegations-of-code-theft/)
On top of all the manual work that Terraform causes developers, there has been a lot of uncertainty floating around this toolset itself in the past year. In August 2023, [HashiCorp moved the software from an open source license to a more restrictive Business Source License (BSL)](https://thenewstack.io/hashicorp-abandons-open-source-for-business-source-license/), in an effort to thwart competing service providers.

As a result, a group of these companies, such as [Spacelift](https://spacelift.io/),[ forked the last version](https://thenewstack.io/linux-foundation-joins-opentf-to-fork-for-terraform-into-opentofu/) of the open source code into its own project, which would be called [OpenTofu,](https://thenewstack.io/how-opentofu-happened-and-whats-next/) and [quickly backed by the Linux Foundation](https://thenewstack.io/linux-foundation-joins-opentf-to-fork-for-terraform-into-opentofu/), which needed an open source IaC tool as part of its [Cloud Native Computing Foundation](https://cncf.io/?utm_content=inline+mention) stack.

And licensing wasn’t the only issue either; power users of Terraform complained of HashiCorp being slow at accepting outside bug fixes. A more receptive model of software management was needed, they argued.

Naturally, HashiCorp was not pleased with the fork, and in April, tried to cast the doubt on the effort, by charging the open source collective had stolen code from the now-BSL licensed Terraform. The OpenTofu team quickly debunked the charges and continued on its journey of [modernizing](https://thenewstack.io/new-opentofu-release-challenges-terraforms-dominance/) OpenTofu.

**5.** **Why Most Companies Are Struggling With Infrastructure as Code**
**Why Most Companies Are Struggling With Infrastructure as Code**
According to a recent survey from StackGen, “[Stacked Up: The IaC Maturity Report](https://stackgen.com/stackedup-infographic-2024),” only 13% of organizations have thus far achieved IaC maturity. Most assert that only some of their infrastructure was represented in code, but only 10% have embarked on pilot projects.,

Achieving IaC maturity is hard, noted [Arshad Sayyad](https://www.linkedin.com/in/arshadsayyad/), co-founder and chief business officer of StackGen, in this post.

Most companies surveyed were still in the early stages, having only a small portion of infrastructure stored in code in pilot projects. Sayyad also recommends IfC, where “the IaC itself is automatically generated from the application code and built with guardrails that align with best practices,” he wrote.

**6.** [Beyond Infrastructure as Code: System Initiative Goes Live](https://thenewstack.io/system-initiative-goes-live-beyond-infrastructure-as-code/)
[Beyond Infrastructure as Code: System Initiative Goes Live](https://thenewstack.io/system-initiative-goes-live-beyond-infrastructure-as-code/)
Other companies looked beyond Terraform for answers. This year, [Adam Jacob](https://www.linkedin.com/in/adamjacob/), the former CTO of Chef, launched his own company, [System Initiative](https://www.systeminit.com/), with an automation platform where, with a graphical grid-based workspace, an admin can stitch together a system with small, reactive functions, allowing the system to be managed as “living architecture.”

Managing Infrastructure as Code may seem like a good idea but it causes “all sorts of downstream problems,” Jacob told TNS.

“It’s not a single technology problem, but it is the shape, the foundation, the primitives that we’re being asked to use that cause these [negative] outcomes in the vast majority of cases.”

**7. **[Generative AI Tools for Infrastructure as Code](https://thenewstack.io/generative-ai-tools-for-infrastructure-as-code/)
[Generative AI Tools for Infrastructure as Code](https://thenewstack.io/generative-ai-tools-for-infrastructure-as-code/)
But wait, perhaps AI could help! [Dell Technologies](https://www.delltechnologies.com/en-us/index.htm?utm_content=inline+mention)‘ [Parasar Kodati](https://www.linkedin.com/in/parasarkodati) notes that [large language models](https://thenewstack.io/why-large-language-models-wont-replace-human-coders/) (LLMs) are great for analyzing error messages and logs to identify the root causes of frequently occurring issues. This approach could apply to any platform too, including [Red Hat ](https://www.openshift.com/try?utm_content=inline+mention)[Ansible Playbooks](https://thenewstack.io/red-hat-brings-ansible-automation-to-amazon-web-services/) and Terraform.

In addition to checking errant code, generative AI can also be used to set up your own personalized chatbot for answering questions.

“You can train GPT models with anything, such as a policy document or coding guidelines or an IT infrastructure-size calculator, and have chatbots use these backend models to answer queries from customers or internal stakeholders,” Kodati wrote.

**8.** **For Terraform Deployment, Any CI/CD Can Beat TACOS**
**For Terraform Deployment, Any CI/CD Can Beat TACOS**
One of the first solutions to IaC fragmentation problem was [Terraform Automation and Collaboration Software](https://spacelift.io/terraform-automation) (TACOS), which sought a way to bring IaC under the same governance and collaborative workflows that we use for application code. But admins did not see the hidden cost of TACO implementations, which came in the form of integration challenges, configuration confusion and potential system fragmentation, noted [Eran Bibi](https://www.linkedin.com/in/eran-bibi), co-founder and chief product officer at [Firefly](https://www.firefly.ai?utm_content=inline+mention) in this post.

The answer comes, Bibi argued, in improving tools on the [CI/CD](https://thenewstack.io/ci-cd/) pipeline instead. This approach can integrate easily with Policy as Code and Governance as Code initiatives, to provide “a more holistic approach to managing infrastructure, without the need for an additional layer of tools.”

**9.** [OpenTofu Amiable to a Terraform Reconciliation](https://thenewstack.io/opentofu-amiable-to-a-terraform-reconciliation/)
Meanwhile, here was some potentially good news on the Terraform fragmentation front. In April, [IBM](https://www.ibm.com?utm_content=inline+mention) [announced](https://thenewstack.io/ibm-purchases-hashicorp-for-multicloud-it-automation/) that it would be acquiring HashiCorp, along with its IaC portfolio built around Terraform.

One of the chief reasons of putting Terraform under a BSL license was financial in nature, and many soon started [speculating](https://thenewstack.io/with-ibms-open-source-roots-terraform-could-be-free-again/) that IBM, which has been historically friendly to open source, may revert the BSL decision and place the software back under open source. And, in an interview with The New Stack, the maintainers of OpenTofu said they would be glad to fold their work back into Terraform, should be it placed back under open source.

To date, IBM has given no indication whatsoever that it plans to do anything of this nature, though once the deal closes, which should happen any day now, we may hear more.

And, as of press time, yet another source IaC tool is [being forked](https://thenewstack.io/puppets-open-source-community-plans-to-fork-the-program/), namely [Puppet](https://puppet.com/?utm_content=inline+mention), from its current owner [Perforce](https://www.perforce.com/), due to objections to the company's revamped [distribution](https://www.puppet.com/blog/open-source-puppet-updates-2025) method. So the IaC community should brace for more tool fragmentation.

**10.** **Can OpenTofu Become the HTTP of Infrastructure as Code**?
**Can OpenTofu Become the HTTP of Infrastructure as Code**?
The open source work around OpenTofu may point the way forward out of this mess. Or at least that is the view of industry observer [Kelsey Hightower](https://thenewstack.io/kelsey-hightower-on-whats-next-for-developers-after-genai/), who likened the open sourcing of Terraform to the opening of technologies that made the Internet possible, making OpenTofu to be the "HTTP of the cloud," wrote [Ohad Maislish](https://www.linkedin.com/in/ohadmaislish/), CEO and co-founder of [env0](https://thenewstack.io/env0-self-service-for-infrastructure-as-code-plus-cost-visibility/).

"For Terraform technology to achieve universal HTTP-like adoption, it had to outgrow its commercial origins," Maislish wrote. "In other words: Before it could belong to everyone, it needed to be owned by no one."

*TNS analyst Lawrence E. Hecht contributed to this report. *
[
YOUTUBE.COM/THENEWSTACK
Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.
](https://youtube.com/thenewstack?sub_confirmation=1)