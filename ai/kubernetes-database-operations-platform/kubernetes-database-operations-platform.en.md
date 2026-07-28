The DevOps movement, set in motion nearly 20 years ago, broke down the traditional divide between software developers and IT operations and adopted the [maxim](https://queue.acm.org/detail.cfm?id=1142065#:~:text=You%20build%20it%2C%20you%20run%20it.) of “you build it, you run it” as its own. However, in [Kubernetes environments](https://thenewstack.io/kubernetes/), that model can become unrealistic when application teams are also expected to operate databases and data services. In practice, DevOps database operations still require much more structure than many teams expect.

In my role as senior cloud platform engineer at the cloud-native services provider [**anynines**](https://anynines.com/), I’ve seen this time and time again: developers who are highly skilled and highly effective at building software have to deal with databases that sit in a completely different realm and require a different kind of operational expertise.

> Developers who are highly skilled and highly effective at building software have to deal with databases that sit in a completely different realm

That’s especially true in platform engineering database management, where the goal should be to reduce operational burden, not shift it onto application teams. A strong [internal developer platform](https://thenewstack.io/7-core-elements-of-an-internal-developer-platform/ "internal developer platform") should make platform engineering databases easier to consume, rather than harder to run.

Tools like the [**a9s Hub**](https://anynines.com/products/hub/?utm_campaign=434127036-a9s%20Hub&utm_source=thenewstack&utm_medium=referral&utm_content=your-dev-teams-should-not-need-to-be-experts-in-database-operations) demonstrate this model in practice: by enabling developers to request databases through Kubernetes-native workflows while a centralized control plane handles provisioning, backups, patching, and governance.  
  
It’s easy enough to deploy Postgres, Redis, or OpenSearch with a few steps. Run a Helm install command, for example, and the service is up and running, provided everything works. The challenge comes when something falters, and those services need to remain reliable, which means patching, monitoring, backing up, and properly recovering them. That’s not something most product teams were ever meant to build deep expertise in.  
  
Modern applications rarely depend on a single data service. A software-as-a-service application might need Postgres on Kubernetes for core data, Redis on Kubernetes for caching, and OpenSearch or Elasticsearch for search and indexing, all running in a highly available setup. That’s why I think “you build it, you run it” only works when developers can request the services they need through automation, while the complex operational work happens behind the scenes.

## Where teams get stuck

More often than not, the first failure points appear when you have to update the database. Imagine Postgres is deployed on a specific version, and a few weeks later, a critical security vulnerability is discovered, requiring you to update the system. Depending on the upgrade, you might need to read through the change logs, decide whether it’s safe to run, or prepare for several steps before you can proceed. Here’s where database automation and Kubernetes become essential, because upgrades are part of database lifecycle management. It can never be a one-time setup.  
  
With Postgres running on a single node, it’s easy to handle and update. To avoid downtime, though, you need a Postgres cluster, often made up of three nodes, so that when one goes down, the other can take over. That setup boosts resilience, but also introduces problems and can create the downtime it was intended to prevent. It’s why Postgres, Kubernetes, and other databases need careful ownership

## When failover goes wrong

Upgrading the three-node cluster has to happen one node at a time, and so failover can get messy. If the election that determines which node takes over fails, two nodes can end up thinking they’re in charge, leading to inconsistent writes and, in the worst case, data corruption. Sometimes the issue is resolved in minutes by restarting the cluster and re-establishing the leader. But if the data is genuinely corrupted, or you can’t work out what went wrong, that outage can stretch into hours.

> If the election that determines which node takes over fails, two nodes can end up thinking they’re in charge, leading to inconsistent writes and, in the worst case, data corruption.

The business impact becomes hard to ignore. Say I’m running a booking platform for a large hotel chain, and the database goes down; none of those hotels can take room reservations. If backups haven’t worked properly, the recovery problem worsens: you might not just lose uptime; you might lose actual bookings, with no clue who’s arriving tomorrow or next week.

For me, that’s the central issue. Developers end up spending time understanding database failure modes, recovery procedures, and backup issues, instead of building the application itself. That slows them down as they’re forced to troubleshoot constantly and pulls them away from the work they’re best at.

## You can’t just hire out

The deeper problem is that you can’t solve this by simply hiring your way out. First, you have to find the right people, and that’s easier said than done — specialists in database operations are hard to come by. The U.S. Bureau of Labor Statistics projects [just 4% growth](https://www.bls.gov/ooh/computer-and-information-technology/database-administrators.htm) for database administrators and architects from 2024 to 2034, with most openings coming from replacement rather than an explosive new supply.

Even when you do find them, they can’t cover everything on their own. These problems don’t just appear when you’re at your laptop; they often happen at night, so you need a proper on-call schedule, and one expert is rarely enough. Let’s remember that people get sick, take vacations, or might leave the company. Dependency on individual specialists is problematic.

The other challenge is breadth. Different databases need different specialists, and it’s difficult to find someone who can operate all of them equally well. That means you’re not just building one on-call schedule; you’re building several, each tied to a different technology stack. It might work in a small team with a fixed number of data services, but as your teams grow, your application count increases, and your database estate expands, making the whole model much harder to manage.

## Operations, made invisible

Good database operations should be invisible *most* of the time. Security patches are applied automatically, backups run on schedule, and those backups are actually usable when needed. In other words, the developer should wake up to find the database already in a safer state, without having to chase it themselves.

> Good database operations should be invisible most of the time… the developer should wake up to find the database already in a safer state, without having to chase it themselves.

That’s why I believe the split between application teams and platform teams matters so much. There are only a few moments in the database lifecycle where developers really need to get involved. When they want a new database, need credentials, or want to trigger a backup before a risky release. Everything else should be handled by automation and the platform behind it. Just because developers deploy applications on Kubernetes doesn’t mean they should be expected to become database ops experts. My ideal, always, is that developers stay focused on what they’re good at — delivering the application itself.

The “you build it, you run it” tenet introduced all those years ago did a brilliant job of solving deployment, but not operations. It can, though, be made realistic at scale through centralized automation. A centralized control plane is especially useful as an organization grows. The more databases you have, the more important it is to know which ones need patching, which ones are compliant, and which ones need action now, not next week. In larger companies, that sort of governance can’t rely on teams coordinating manually. It has to be visible and manageable from one place.

That’s the real promise of a9s Hub: it gives developers the experience of working with a database as if it were running locally in their Kubernetes cluster, while the actual provisioning, patching, backups, and governance are handled centrally. It supports on-prem environments, where the same level of managed database service is often missing. It also works across different stacks, from Kubernetes to VMs and AWS-backed services, without losing that central layer of control. The result is faster delivery and better efficiency, enabling developers to spend more time innovating and less time firefighting.  
  
[***Explore the a9s Hub***](https://anynines.com/products/hub/?utm_campaign=434127036-a9s%20Hub&utm_source=thenewstack&utm_medium=referral&utm_content=your-dev-teams-should-not-need-to-be-experts-in-database-operations)

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://cdn.thenewstack.io/media/2026/07/e5b40542-cropped-563c9ed3-1711467030075.jpeg)

Oliver Wolf is a Platform Engineer at anynines. He specializes in Kubernetes, Cloud Foundry, platform engineering, and cloud-native infrastructure, with a particular interest in database automation, Internal Developer Platforms, and improving the developer experience for application teams.

Read more from Oliver Wolf](https://thenewstack.io/author/oliver-wolf/)