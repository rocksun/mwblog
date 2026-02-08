When HashiCorp changed the licenses of Terraform and many of its other products from open source MPL 2.0 to the Business Source License (BSL), the [backlash was intense](https://thenewstack.io/hashicorp-abandons-open-source-for-business-source-license/). So intense that the community forked Terraform to create OpenTofu under a fully open source license. [OpenTofu continues to gain ground](https://thenewstack.io/opentofu-joins-cncf-new-home-for-open-source-iac-project/), and HashiCorp (part of IBM since February 2024) has shown signs of stabilization, but the echoes of resistance still ring through the technology industry today.

What this, and other high-profile examples, started was a serious conversation around how we protect greenfield open source technologies from (often poor) replication and commercialization by popular cloud providers. Commonly, with a limited or indirect contribution back to the originating project. HashiCorp took the heat as one of the most public examples of the switch to the BSL, but arguably, it set a blueprint for open source projects to [better protect investments and secure future monetization](https://thenewstack.io/open-source-licenses-who-holds-the-power/).

Let’s look at the impact commercial forking has on open source maintainers and explore how the BSL works. We’ll consider what it means in practical terms for both open source startups and enterprise users. We’ll cover what teams can (and can’t) do with the BSL, when to look at a commercial subscription and why this hybrid model reflects how open source really works inside modern enterprises.

## The Cost of Cloud Commercialization

In 2025, 96% of organizations either maintained or increased their use of open source software (OSS), according to the Perforce OpenLogic “[State of Open Source 2025](https://www.perforce.com/resources/opl/2025-state-of-open-source-report)” report. It’s this widespread adoption of open source technologies, and the innovation that happens around them, that has inspired the big cloud providers to capitalize. And capitalize they have. Marketplaces are full of highly profitable commercial versions of open source projects. It’s not illegal to fork open source code, but when it’s clearly at the expense of community creators and maintainers, the practice raises persistent ethical and economic concerns within the open source community.

### Profit Siphoning

The most obvious cost to maintainers is revenue loss. Cloud-hosted OSS services, even “lite” versions, rank among the highest-margin products for cloud providers. Profit that upstream maintainers never see. Amazon Relational Database Service (RDS) (PostgreSQL, MySQL) is widely considered one of AWS’s most profitable offerings. Azure Cache for Redis and Google Memorystore are extremely high-margin managed Redis offerings that raise revenue far higher than those of the companies that built those databases. And, let’s not forget OpenSearch, AWS’s forking of Elasticsearch, a fork so successful that it is widely seen as contributing to Elastic’s decision to [reintroduce open source licensing](https://thenewstack.io/whats-behind-elastics-unexpected-return-to-open-source/) for Elasticsearch and Kibana under the 2024 AGPLv3 license.

### Increased Maintenance Burden

As well as lost profits, [research](https://arxiv.org/pdf/2411.04739) shows that commercial forks create long-term divergence and extra coordination work. Refactorings and reorganizations make patch propagation difficult from one fork to another and back upstream. Added to this, empirical studies of project fragmentation show that when a cloud provider forks a project, others tend to align with the most powerful distribution. Contributors migrate toward the fork because that’s where their work has a real-world impact. Even neutral contributors often follow the fork without ideological alignment.

### Fragmentation and User Confusion

Forks often split developer activity and focus, especially if commercial incentives pull contributors toward the fork. Some maintainers see core contributors shift allegiances or duplicate efforts across repositories; this really hurts original community momentum. Added to this, forking can lead to knowledge dilution. If contributors move to a fork, institutional knowledge and domain expertise about the original codebase can dissipate, potentially reducing the overall quality and long-term resilience of the original project.

## Community Momentum Grows

Despite all this, there’s no arguing with the popularity of [Valkey](https://thenewstack.io/valkey-a-redis-fork-with-a-future/) (the Linux Foundation-backed fork of Redis), OpenTofu, [Opensearch](https://thenewstack.io/opensearch-how-the-project-went-from-fork-to-foundation/) and others. We might then ask whether the potential losses outweigh the perceived protection that the BSL brings. Will adopting the BSL framework automatically mean developers will be put off? Will it allow teams proper open source access, while protecting IP?

All signs point to the positive. In our experience, the SurrealDB community hasn’t reacted negatively; it continues to grow alongside our customer base.

## What Is the Business Source License (BSL)?

The BSL is a fairly new kind of source-available software license, designed to strike a balance between the freedoms of open source and the realities of commercial sustainability. In simple terms, here’s how it works:

* **Use of the software is free of charge for developers and engineering teams in most scenarios.** Internal projects, prototypes, testing and most non-commercial uses are covered. Teams can modify, extend and redistribute it within their organization.
* **The BSL includes a restriction that restricts commercial competition.** This is the critical clause for many vendors and project owners. It is included to restrict commercial use that directly competes with the vendor. The common example is hosting the software as a paid Software as a Service product without a commercial license.
* **After a set period, it becomes fully open source.** Each project defines a “change date.” After that, the BSL version converts to an [Open Source Initiative](https://thenewstack.io/open-source/ "Open Source Initiative") (OSI)-approved open source license like Apache 2.0 or MIT, becoming fully open source for everyone. In [SurrealDB’s case](https://github.com/surrealdb/surrealdb/blob/main/LICENSE) the change date comes four years after launching each version. For instance, the current version 3.0 converts to Apache 2 on Jan.1, 2030.

Under the BSL, individuals and teams are free to use, explore and deploy a solution in nearly any context, as long as they aren’t offering it commercially as a database service. This means developers at enterprises can evaluate and integrate a solution in projects and products with no red tape or procurement overhead. But, when those systems become mission-critical and need commercial guarantees, support or advanced functionalities such as compliance and security features, that’s when the commercial model comes in.

## What the BSL Does for Enterprises

For business leaders, the BSL licensing model offers a pragmatic middle ground. Firstly, it offers developers and engineers free access with no upfront licensing fees or negotiations. Teams can use it for any purpose — testing, learning, internal build and deployment —provided it’s not being used for commercial purposes.

The license terms are clear: internal use is fine, commercial re-hosting isn’t. This transparency reduces compliance uncertainty. This brings clarity for legal and procurement teams.

Finally, the BSL brings long-term sustainability for project owners and vendors. The BSL ensures that companies can invest in ongoing development, support and enterprise-grade features without fully closing off access for the community.

It’s a model built for the modern enterprise: fast-moving, developer-driven, but also accountable. Most enterprise use begins with motivated teams solving real problems. At SurrealDB, our goal is to make the rules simple: Here’s what you can do with SurrealDB under BSL, and here’s when to talk to us about support or a commercial license.

## When Teams Move From Free to Paid

At what point should an enterprise consider a commercial license or subscription? There are three common triggers:

1. **Production dependency.** When an internal system becomes critical to operations, the business typically seeks commercial support for assurance, uptime guarantees and expert help.
2. **Scale and performance.** Enterprises scaling the database across departments or regions benefit from the subscription model’s advanced features such as clustering, observability or extended integration support.
3. **Governance and compliance.** For organizations with an open source program office (OSPO) or compliance teams, a subscription simplifies audit processes and ensures legal clarity.

As well as the commercial license, most vendors offer an enterprise tier. This is usually a managed cloud service that brings additional benefits such as enhanced security and compliance, essential in highly regulated industries. In many cases, this can significantly reduce operating overheads.

The shift from community to commercial isn’t a change of mindset, it’s a formalization of success. It recognises that open source was the right tool to get started, and enterprise-grade assurance is the right tool to keep going.

## BSL in Context: An Industry Trend

MariaDB pioneered the BSL to protect its database from commercial re-hosting while keeping it open for users. CockroachDB and Sentry followed similar source-available paths, ensuring that innovation remains accessible to the community while safeguarding the vendors’ ability to build viable businesses. This isn’t a retreat from open source; it’s an evolution. The open development model remains intact; the BSL simply introduces fair use boundaries that align with enterprise realities. And, because BSL-licensed software is still publicly available, transparent and auditable, developers continue to learn, experiment and contribute.

## Is the Hard Fork Still a Risk?

What happens when the software becomes completely open? Does the BSL really protect us from the risk of third-party commercialization? In practical terms, the BSL’s real protection is time-bound control, not permanent exclusivity. Within the four-year license term, companies cannot legally offer the software as a competing managed service. This gives companies a protected period to monetize adoption, build the brand, establish an API ecosystem and hasten innovation to outrun alternatives.

Of course, the BSL doesn’t completely remove the ability to fork after conversion but, given how outdated the original toolset would be by then, it’s very unlikely. In this way, the BSL protects vendors from immediate commercial forks and removes the incentive to fork later.

## A Partnership Model for the Modern Enterprise

The BSL reflects a broader truth about modern enterprise IT. Software adoption is no longer a top-down decision. Developers discover, teams prototype, organizations scale and vendors step in to help enterprises turn grassroots innovation into production reliability. That’s why open source adoption isn’t just a community story; it’s a business one.

Many large organizations find new solutions through engineers experimenting with open source versions. When early pilots prove valuable, leaders engage directly for enterprise support, performance optimization and roadmap collaboration. This bottom-up adoption model is now standard across the industry, and the BSL provides the legal and operational framework to make it sustainable.

## Considerations for Business Leaders

* **Encourage responsible exploration.** Empower your teams to test open source tools, but ensure they understand your company’s policies around licensing and usage.
* **Formalize what works.** When open source solutions prove valuable, consider formalizing them through enterprise agreements for security, governance and continuity.
* **View the BSL as an enabler, not a restriction.** It protects both sides: your freedom to innovate and the vendor’s ability to sustain development.
* **Remember the shared goal.** Open source and enterprise subscriptions aren’t opposites; they’re partners in innovation.

## **Open Innovation Meets Sustainability**

The Business Source License represents how open source has grown. It keeps the door open for innovation while defining clear boundaries for commercial use. For enterprises, that means developers can keep building with the tools they love safely, responsibly, and with a clear path to support when it matters most. And for companies like SurrealDB, it ensures that open innovation and sustainable business can thrive together.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://thenewstack.io/wp-content/uploads/2026/01/21e1bd51-cropped-7445b261-tobie-morgan-hitchcock-600x600.jpg)

Tobie Morgan Hitchcock is CEO and cofounder of SurrealDB. He is an experienced tech entrepreneur, developer and software engineer, with 18 years’ experience in the software and cloud computing industries. In 2021 he founded SurrealDB, with the aim of building...

Read more from Tobie Morgan Hitchcock](https://thenewstack.io/author/tobie-morgan-hitchcock/)