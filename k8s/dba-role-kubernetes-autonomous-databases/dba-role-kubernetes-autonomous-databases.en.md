The promise of fully autonomous systems — databases that manage, heal, and optimize themselves amid rapidly increasing data stores — is tantalizing to CTOs. But as [Percona](https://www.percona.com/) co-founder [Vadim Tkachenko](https://www.linkedin.com/in/vadimtk) explained to *The New Stack* last week, the reality is far more nuanced: While automation is indeed transforming the data landscape, the human element remains not only relevant but essential.

“I think a human still will need to run databases,” Tkachenko told *The New Stack*. “However, the growth of data is not slowing down. The transformation is not in the disappearance of the (DBA) role, but in its redefinition.”

![](https://cdn.thenewstack.io/media/2026/06/4ac4d0e3-vadim-tkachenko.jpg)

*Percona CTO and co-founder Vadim Tkachenko. Credit: Percona*

Speaking during his company’s [Percona Live 2026 conference](https://thenewstack.io/percona-20-oursql-foundation-rebrand/) here at the [Computer History Museum](https://computerhistory.org/) in Mountain View, California, Tkachenko predicted, “The database administrator of the future will evolve from a mechanic focused on operational upkeep to an architect specializing in the structure of the data itself.”

The Durham, North Carolina-based Percona, which makes popular open-source database software with a set of optional services, celebrated its 20th anniversary at the CHM event. Practical solutions for current workload issues were highlighted over three days of seminars, with experts from AWS, VMware, NEXTGRES, and others contributing their expertise to the discussions.

> “The database administrator of the future will evolve from a mechanic focused on operational upkeep to an architect specializing in the structure of the data itself.”

The day-to-day drudgery — the patching, scaling, and maintenance that currently consume human time — will increasingly be handled by machine learning and AI agents. Tkachenko envisions a future in which these agents communicate with the database – not through the venerable, human-readable SQL standard, but through their own optimized internal language.

This change means human expertise pivots to strategic, higher-level concerns: ensuring data integrity, defining access patterns, and architecting systems. The human role transforms from management to governance.

This vision of autonomy is intimately tied to the rise of cloud-native infrastructure, particularly involving the open-source data distributor Kubernetes. The need for a standardized, portable control plane is the technical foundation for achieving true database autonomy and flexibility. Kubernetes abstracts the underlying infrastructure, allowing automation tools to manage databases across any environment — public cloud, private cloud, or hybrid — with a consistent set of APIs and best practices.

**The Percona-Kubernetes relationship**

Kubernetes and Percona (specifically Percona Operator and the Percona Monitoring and Management app) enhance each other by blending container orchestration with enterprise database management. Kubernetes provides scalable, self-healing infrastructure for databases, while Percona optimizes database performance and automates lifecycle management to ensure reliable, high-speed operations.

How Kubernetes benefits Percona:

* **Automated scaling and orchestration:** Kubernetes dynamically allocates CPU, memory, and storage resources, allowing Percona databases (such as [Percona XtraDB Cluster](https://docs.percona.com/percona-xtradb-cluster/8.0/index.html)) to instantly scale to meet traffic spikes.
* **Self-healing failover:** If a database node fails, Kubernetes automatically reschedules the pod to a healthy node. Percona’s [Operators](https://docs.percona.com/percona-operator-for-mysql/pxc/index.html) handle the database rejoining process natively, preventing downtime and maintaining continuous high performance.
* **Consistent deployments:** Using [Kubernetes StatefulSets](https://kubernetes.io/docs/concepts/workloads/controllers/statefulset/) and declarative APIs, Percona databases can be deployed identically across on-premises, hybrid, or multi-cloud setups without performance configuration drift.

How Percona benefits Kubernetes:

* **Database-aware lifecycle management:** Standard [Kubernetes](https://kubernetes.io) struggles to manage stateful databases natively. Percona Operators bridge this gap, automating specialized tasks like point-in-time recovery, rolling upgrades, and cluster backups within the Kubernetes ecosystem.
* **Deep observability:** With [Percona Monitoring and Management (PMM)](https://docs.percona.com/percona-monitoring-and-management/3/index.html), database performance bottlenecks can be directly linked to Kubernetes container metrics. PMM provides granular visibility into query execution times, allowing DBAs to pinpoint whether a performance lag is due to database tuning or Kubernetes cluster resource contention.
* **High-performance open source tuning:** Percona distributions are highly optimized for demanding, resource-intensive operations. By tuning settings such as caching and memory management within the Pod, Percona extracts near-bare-metal speeds from the Kubernetes environment.

## **Portability guards against vendor lock-in**

The imperative for the portability enabled by Kubernetes and Percona is driven by Tkachenko’s stark warning against vendor lock-in.

> “You’re going to need to make choices if you want to continue to pay for a public database at cost, or how much it will cost you to migrate, or how much it will cost you to run your own database.”

For many companies, the public cloud database is a convenience that functions like a water or electricity utility. However, this convenience comes at the cost of control. If a public cloud provider continues to raise costs, users are trapped, Tkachenko says.

“You’re going to need to make choices if you want to continue to pay for a public database at cost, or how much it will cost you to migrate, or how much it will cost you to run your own database,” he says.

This is where open source infrastructure becomes crucial. Running databases on a portable platform offers a way out of the high-cost, high-control trap of proprietary cloud solutions. The ability to deploy, manage, and move autonomous database workflows via Kubernetes operators ensures that the business retains leverage and independence.

## **How security enters the conversation**

The conversation on automation also necessitates a discussion on security. Tkachenko cautions that increased automation is not automatically synonymous with increased security. If automated processes are not robust, he says, they can inadvertently create new attack surfaces by missing necessary controls. The complexity of non-robust, automated access controls can pose far more risk than a well-managed human process.

For Percona, its commitment to independence and robust systems is fundamental. Tkachenko says Percona has always been bootstrapped and independent, never accepting external VC capital. This independence allows the company to provide unbiased advice that isn’t geared toward locking customers into a single, proprietary solution.

Ultimately, the goal is not to eliminate humans but to equip them with better tools and an independent foundation. This approach, supported by community efforts such as the newly formed [OurSQL Foundation](https://www.globenewswire.com/news-release/2026/05/27/3302305/0/en/oursql-foundation-launches-to-support-mysql-users-developers-and-companies.html), which Tkachenko sees as a necessary complement to guide the ecosystem independently of any single vendor’s shifting direction, aims to ensure the long-term health and stability of the open-source data world.

For the record, OurSQL Foundation’s key function is to provide a venue for those involved in the MySQL community to build and deploy applications that use MySQL or a broad range of compatible software, and to share them with their peers. It also aims to access knowledge and provide feedback on future development consistently and transparently. This community non-profit supports the growth and use of MySQL as an open-source database and collaborates with all players in the market, including [Oracle](https://oracle.com), to see MySQL succeed with the next generation of developers and applications, Tkachenko told Percona Live conference goers last week.

Autonomous databases will continue to handle the nuts and bolts of production, but humans, leveraging standardized platforms like Kubernetes, will always be needed to design the data structure and maintain the workflow’s ethical and economic independence.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://thenewstack.io/wp-content/uploads/2024/09/314a85cc-cropped-89f126f8-chrisp-600x600.png)

Chris J. Preimesberger, a contributing writer/editor at several publications since June 2021, is former editor in chief of eWEEK. He was responsible for the publication's coverage for a decade (2011-2021). In his 16 years and more than 5,000 articles at...

Read more from Chris J. Preimesberger](https://thenewstack.io/author/chris-j-preimesberger/)