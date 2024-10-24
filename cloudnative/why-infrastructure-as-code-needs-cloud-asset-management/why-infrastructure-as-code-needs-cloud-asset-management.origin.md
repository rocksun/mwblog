# Why Infrastructure as Code Needs Cloud Asset Management
![Featued image for: Why Infrastructure as Code Needs Cloud Asset Management](https://cdn.thenewstack.io/media/2024/10/a7d5ed3d-iac-needs-cloud-asset-management-1024x576.jpg)
The Infrastructure as Code (IaC) landscape drama continues. If we thought everything would calm down following the [HashiCorp](https://www.hashicorp.com/?utm_content=inline+mention) license change, consequent forking of the project and [establishing OpenTofu](https://thenewstack.io/how-opentofu-happened-and-whats-next/), and then the [IBM](https://www.ibm.com?utm_content=inline+mention) acquisition of HashiCorp… well, think again.

While some pundits will claim: “* Terraform is DEAD — long live [ENTER FAVORITE IaC TOOL HERE]*,” I think what is actually happening is quite a bit different and much more compelling. Recently, my co-founder

[Eran Bibi](https://thenewstack.io/author/eran-bibi/)was on a
[KubeCon 24 Paris](https://thenewstack.io/kubecon-europe-webassembly-ebpf-are-huge-for-cloud-native/)panel discussing the “
*,” and I’d like to dig a little further into what I see unfolding.*
[Evolution of IaC — On Open Source & Everything Else](https://www.youtube.com/watch?v=zaJK1YtsfrQ)One of my major takeaways from recent announcements and trends is: If you’ve been thinking of [Pulumi](https://www.pulumi.com?utm_content=inline+mention) primarily as an orchestration tool, [its latest announcement](https://www.pulumi.com/blog/pulumi-up-2024/) suggests you may want to take a closer look.

We’ve been beating the “it’s not just IaC — it’s a whole world of cloud asset management, too!” drum for quite a while now. It’s exciting when we see major industry players validating our positions. Enter Pulumi into the cloud asset management arena. Welcome!

With its positioning newly focused on automation, security and management, I posit that Pulumi’s redirection is evidence of a shift we’ll be seeing among many (if not all) IaC players in the near future. Cloud inventory, compliance and remediation matter just as much as orchestration, and they’re all inherently connected.

Pulumi’s announcement isn’t just news. It’s an indicator of where our industry is headed, and it’s an exciting direction. The future of Infrastructure as Code and cloud asset management is actually quite tightly coupled — and it will likely change the way we think about future cloud operations at today’s cloud fleet scale.

## What Pulumi Said Between the Lines
Is HashiCorp dead?

Embedded in Pulumi’s new vision is taking on competitor HashiCorp following the latter’s license change and [acquisition by IBM](https://thenewstack.io/ibm-buying-hashicorp-what-devs-analysts-and-competitors-are-saying/). Pulumi’s platform now includes three core products:

- Pulumi IaC, for Infrastructure as Code in any programming language.
- Pulumi ESC, for security automation and secrets management.
- Pulumi Insights, for visibility and an analytical view of cloud resources and assets.
Only time will tell if the market is ripe for a new take from an established vendor or for a HashiCorp Vault alternative, but Pulumi’s move suggests a clear focus on integrating cloud governance and visibility capabilities, as well as AI, directly into Infrastructure as Code platforms, while also doubling down on open source commitments (which some consider abandoned by the likes of HashiCorp).

Pulumi’s move underscores a few important truths we’ve known for a long time:

**Cloud asset management is making waves.** When a big player like Pulumi starts moving in this direction, it’s like a huge billboard saying, “Hey, this cloud asset management thing? It’s a big deal.”
**The value of IaC beyond provisioning is being recognized.** Infrastructure as code and the codifying of cloud resources is a largely solved problem. We’re now moving to higher order problems, which is more than just deploying new infrastructure, to actually manage infrastructure that’s already out there (like finally realizing you need to clean out your garage after years of just shoving new stuff in).
**Growing complexity is surfacing longstanding issues with traditional cloud tools.** This move substantiates that cloud environments are becoming increasingly more complex. The ecosystem is saturated with tools, and cloud operations engineers, overwhelmed by choice and understanding, will truly move the needle in reducing manual toil and cognitive load. This complexity creates an opportunity for innovators and fast movers to deliver better, more flexible cloud management tools.
## What IaC Vendors Are Still Getting Wrong
To know how to prepare for change and keep your teams agile in a quickly changing DevOps landscape, you need to recognize what you’re up against — and, importantly, what you may be overlooking:

### 1. Multicloud Environments Are Growing and Underserved
According to our [2024 State of Infrastructure as Code Report](https://www.firefly.ai/state-of-iac-2024), 89% of organizations are using a multicloud approach. Thirty-six percent are even considering expanding their multicloud infrastructure. Over 50% of organizations have 10+ cloud accounts, while another quarter have over 100 cloud accounts, and 12% have over 500. That includes major cloud platforms like [AWS](https://aws.amazon.com/?utm_content=inline+mention), [Google](https://cloud.google.com/?utm_content=inline+mention) Cloud Platform (GCP), [Microsoft](https://news.microsoft.com/?utm_content=inline+mention) Azure and others.

Despite Pulumi’s pivot indicating a positive shift in the right direction, IaC solution vendors are still overlooking cloud practitioners’ multicloud reality and continuing to think about cloud asset management in silos, buckets and languages. As companies continue to spread their assets across multiple clouds, tools that can manage resources across different providers will become crucial.

### 2. Cloud Governance Requires an Active, not Reactive, Approach
Just because governance-related insights are accessible to you doesn’t guarantee that you can act on them proactively and efficiently to take control of your cloud. That’s part of why cloud governance remains one of the top challenges and objectives of using IaC. True governance is about proactive cloud control and safeguarding, not passive insight gathering.

By considering governance at every stage, you can often prevent issues before they happen. And when an incident does happen, leaning on AI to automatically offer the solution saves time by quickly fixing it.

So, what does proactive governance look like?

**End-to-end (or code-to-cloud) policy enforcement:**Implementing “code-to-cloud” governance, enforcing policies at every stage of the process: code, CI/CD*and*cloud.**Active prevention:**Implementing guardrails in place ahead of time to catch violations before they happen.**Automated remediation:**Auto-remediation comes in two forms. In active prevention, guardrails notify the user of code violations and offer remediation solutions before it goes live. The second form of auto-remediation focuses on existing cloud resources. When you add policies, the solution shows you which resources violate which policies and then offers you the right fix.- In 2024,
[any CI/CD can beat TACOS](https://thenewstack.io/for-infrastructure-as-code-ci-cd-can-beat-terraform).
When Terraform automation and collaboration software ([TACOS](https://www.firefly.ai/blog/lets-get-spicy----do-we-still-need-tacos-to-shave-the-iac)) first came onto the scene, these tools offered a compelling proposition, but they can also become a single point of failure for cloud teams. Today, TACOS’s relevance in the modern [DevOps stack](https://thenewstack.io/2-open-source-ai-tools-that-reduce-devops-friction) is increasingly being questioned, especially by organizations that already have robust CI/CD pipelines in place.

The real focus should be on empowering your current platforms with the capabilities they need to handle IaC effectively. In short: We don’t need more tools or more fragmentation. And with the death of TACOS, consolidation is how you truly simplify cloud management.

Pulumi’s expanded offerings will integrate more seamlessly with existing CI/CD pipelines. Plus, the introduction of Pulumi ESC will enhance security practices within CI/CD pipelines, particularly in managing secrets and configurations. This will only serve to further the move away from TACOS.

## What’s Next for Cloud Infrastructure Management?
Since creating the category, Firefly continues to lead and educate on cloud asset management. Now, Pulumi’s recent strategic move shows that Firefly is setting a standard that vendors are poised to follow as the ecosystem matures.

As we continue to see more (seismic) shifts, more players and more innovation in the space, we’ll also see other changes in the market — the most notable being increasingly tight competition. Large and small players alike are looking to be the next Vault, the next Terraform and, by the looks of it, even the next [Firefly](https://www.firefly.ai/).

May we continue to evolve toward the future of cloud-everything management, and may the best cloud tools win.

[
YOUTUBE.COM/THENEWSTACK
Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.
](https://youtube.com/thenewstack?sub_confirmation=1)