**Mergers, acquisitions, and the steady churn** of business and technology initiatives are creating something nobody asked for: Duplicate infrastructure and expertise.

Here’s the typical split: A platform engineering team that owns cloud-native and Kubernetes workloads. Meanwhile, traditional IT holds the keys to virtual machine (VM) workloads. Two teams. Two domains. One budget. And the costs keep going up.

Even organizations that talk about standardizing on Kubernetes still have a substantial VM footprint. For many teams, this coexistence isn’t a temporary transition state. It’s the operating model.

On-premises, this split forces two separate environments. Each environment includes networking, servers, and storage. Such duplication can be structurally less cost-efficient than consolidation. VM-based mission-critical workloads aren’t going away anytime soon.

It’s not like teams don’t want to modernize. They absolutely do. But it’s not as simple as just picking between old-school VMs or diving into Kubernetes. What’s really happened is these two worlds have grown up on their own.

That kind of split often leads to extra infrastructure, more people doing the same jobs, slower projects, mixed-up governance, and budgets that keep ballooning. And when you’re on-prem or working at the edge, running two separate setups for networking, compute, storage, and playbooks just doesn’t make sense anymore.

To make matters worse, “just rewrite” bares its fangs on the modernization initiative. Finance and executive leadership see two teams running two tech stacks. It’s only natural that they reach for the obvious fix: Pick one team’s platform, with no technology consideration, migrate everything to it, and watch the added cost disappear from the executive briefing slide and move to the CFO’s budget spreadsheet.

## Rewrites are rarely the shortest path to business value

Over time, we learned from our customers that “rewrite it” isn’t a modernization strategy. Rather, it’s a budget, risk, and timeline strategy all at once. In many cases, rewrite it doesn’t make sense financially. The tech industry loves the idea of re-platforming and re-architecting legacy applications. Even then, such a move only returns your enterprise to square one and functional parity. The more realistic path is to keep mission-critical applications as-is when scaling out cloud-native platforms to deliver new value.

Moving everything to Kubernetes/cloud initiatives won’t prevent two platforms either. Such initiatives often stall because some workloads don’t fit or take far longer than planned.

The economics of rewrites don’t disappear just because AI accelerates software delivery. AI can compress the time it takes to write code. However, writing code was never the expensive part of a rewrite. The costs that dominate many rewrite budgets are judgment costs, and those remain stubbornly human.

Start with architecture. Organizations still need software engineering expertise to design the target system. That design problem has gotten harder, not easier. Cloud-native applications built on microservices for horizontal scaling bear little structural resemblance to the traditional enterprise applications they replace. Someone has to make those translation decisions and then spend the time directing the AI on what to build. That direction time is a real line item.

Validation is the next cost that survives. When customers or employees depend on a piece of software, even small behavioral changes are disruptive, making it non-negotiable to prove feature parity. Testing and validating that parity remains heavily human work. AI can generate test cases. It can’t tell you which broken workflow will cost you a customer.

Then comes the data. Teams must migrate and adapt data to the new system, and that work almost always surfaces complexities nobody scoped, including undocumented dependencies and format assumptions baked into decades of records. No amount of generation speed on the code side makes the data side move faster.

> The rewrite math changes shape with AI. It doesn’t shrink to zero. The spend shifts from writing software to decision-making, verification, and migration.

The rewrite math changes shape with AI. It doesn’t shrink to zero. The spend shifts from writing software to decision-making, verification, and migration.

We see the same pattern repeat with rewrites among our customers. They keep mission-critical systems running as they are. Then they build new value with cloud-native applications in parallel. Modernizing selectively only when it’s truly worth it.

## The real gap is operational

The gap we see isn’t philosophical — VMs versus containers — it’s operational. The tooling, workflows, and skills that define VM and cloud-native operations differ. If platform teams can’t deliver these services at the expected velocity, developers will blame the platform. When developers are accustomed to provisioning core services in minutes, any friction in on-prem or edge environments is perceived as the platform adding friction or slowing delivery.

> The gap we see isn’t philosophical — VMs versus containers — it’s operational.

Historically, day-to-day operations in VM environments are UI-driven. Cloud-native environments are much more command-line interface (CLI) driven, where APIs, config files, and the terminal are the center of gravity. That gap becomes both an organizational and technical constraint. Moving from UI-driven operations to deep command-line interface (CLI)/config workflows isn’t a natural step without a significant shift in the team’s capabilities.

The operational gap shows up quickly in data services. Cloud-native workloads don’t just need compute. They need databases, object storage, file, and block services delivered at cloud-like speed. And despite the myth that containers are stateless, the reality is that most meaningful workloads have state somewhere as data, logs, metrics, or dependencies that must be handled consistently.

Another notable gap is that storage consumption differs:

* Cloud-native apps often need multiple storage types simultaneously
* VM workloads historically rely on straightforward block storage

The public cloud, by shaping cloud-native expectations, further contributes to the gap. Developers can click to get a database, such as Amazon Relational Database Service (RDS), and object storage, such as Amazon Simple Storage Service (S3), is just there. Developers expect this level of self-service simplicity when these platforms are extended beyond the public cloud, which isn’t always something platform teams are prepared for.

## Edge + AI is turning fragmentation into a business risk

Today, edge and disconnected environments, such as air-gapped computing, have moved from niche use cases to mainstream constraints. When connectivity is intermittent or when latency matters, platform assumptions change. In these environments, reliability isn’t an IT metric. It’s a business outcome. Even minutes of downtime can cause major financial loss. It’s also a sign that data gravity is driving more pragmatic architectural conversations about the growing need to locate compute and data services closer to where data is generated.

AI raises the stakes further. If you’re collecting data at the edge, shipping it away for processing and pulling results back can be too slow and too expensive.

## Our platform demands before betting on it

Before we’d bet on any platform, we’d ask a basic question: Can a single team operate both VM and Kubernetes environments without duplicating the entire organization? We’d insist on consistent governance: security controls and role-based access control (RBAC) should not fracture just because workloads are deployed differently.

We’d also look for cloud-like data services — object, file, block, and database capabilities — delivered quickly enough to keep developers moving toward their delivery targets, and designed to scale easily as application usage expands.

Then we would evaluate whether the platform helps reduce on-prem duplication. If it forces parallel networking, storage, and operational runbooks, the cost structure won’t improve.

Finally, we’d scrutinize lifecycle operations, including patching, upgrades, and maintenance, because “heroic” weekend work isn’t a sustainable strategy.

## Dual native architecture is the pragmatic model

We use “dual native” to reject the binary choice. Enterprises need platforms that are both VM-native and container-native. Some workloads benefit from the operational efficiency of virtualization. Others are sensitive to latency or specialized hardware and are better served on bare metal. A one-size-fits-all mandate creates friction on both sides.

Dual native platform architecture isn’t just integration. It’s the one operational model that treats VMs and containers as first-class citizens. Teams no longer have to pick one architecture or stitch together separate stacks. In this model, organizations can keep mission-critical VM workloads running while building and scaling new cloud-native applications. Teams can maintain consistent management, governance, lifecycle operations, and cloud-like data services across VMs and bare metal servers across globally distributed infrastructure.

Nutanix Kubernetes Platform (NKP) solution with NKP Metal, which extends the Nutanix operating model and the NKP solution, supports Kubernetes deployments directly on bare-metal infrastructure. This solution provides unified Kubernetes operations, shared data services, centralized visibility, and automated bare-metal lifecycle management to support a dual native platform architecture.

Our approach with NKP starts with the premise that VM and bare-metal Kubernetes should operate under a consistent model rather than be split into separate toolchains and teams. To that end, a major focus has been on unified data services across deployment targets so the storage layer doesn’t become the breaking point when workloads span VMs and bare metal. We also purposefully centralize day-to-day operations and visibility across VMs and Containers in NKP so teams aren’t forced to manage two worlds with two separate management planes.

NKP Metal addresses lifecycle management, one of the biggest challenges of running bare metal at scale, including host OS setup, patching, and upgrades without resorting to late-night or holiday/weekend manual maintenance windows.

## What’s next

Some things we know with confidence. VM workloads aren’t disappearing — the coexistence of VMs and containers will remain the operating model for many enterprises well into the next decade. Edge and AI workloads will likely continue to pull compute toward where data is generated, and budget pressure on duplicated infrastructure will likely only intensify.

What we don’t know is the pace. How quickly enterprises consolidate two platform teams into one depends on skills, internal politics, and licensing decisions, which vary widely from one enterprise to the next. Nobody can credibly predict a timeline there.

What we think is coming: AI inference at the edge will make bare metal a first-class deployment target rather than a special case, and platform teams will be judged less on which architecture they picked and more on whether developers can self-serve their own infrastructure, including data services, without opening a ticket.

> The path forward is about building an operational foundation that accepts reality where VMs, containers, and bare metal coexist under a unified model.

The path forward is about building an operational foundation that accepts reality where VMs, containers, and bare metal coexist under a unified model. Enterprises that will thrive in this future are those adopting dual-native approaches that are ready for whatever comes next.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://cdn.thenewstack.io/media/2025/11/e00a72d5-aarthi-mahesh.jpg)

Aarthi drives product and solutions marketing at Nutanix, specializing in the Nutanix Kubernetes Platform (NKP) and its full-stack cloud native solution. With a background in computer science and customer success engineering, she brings deep expertise in enterprise technology and Kubernetes...

Read more from Aarthi Mahesh](https://thenewstack.io/author/aarthi-mahesh/)

[![](https://thenewstack.io/wp-content/uploads/2026/08/70002758-cropped-dba1a1f0-steve-headshot-2024-600x600.jpg)

Steve Carter has dedicated over a decade to pioneering modern cloud architectures and making them accessible to Enterprise IT organizations. Steve joined Nutanix as a software developer in 2011 before turning his attention to educating the market on transformational IT...

Read more from Steve Carter](https://thenewstack.io/author/steve-carter/)