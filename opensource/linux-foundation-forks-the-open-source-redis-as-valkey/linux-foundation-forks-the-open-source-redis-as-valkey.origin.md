# Linux Foundation Backs ‘Valkey’ Open Source Fork of Redis
![Featued image for: Linux Foundation Backs ‘Valkey’ Open Source Fork of Redis](https://cdn.thenewstack.io/media/2024/03/8bcfdf51-valkey.webp)
We’ve got to stop meeting like this, Linux Foundation.
Thursday, the foundation announced that intends to back a fork of the formerly open source Redis in-memory data store, swiftly following the news that
[Redis](https://redis.com/?utm_content=inline+mention) itself [moved](https://redis.com/blog/redis-adopts-dual-source-available-licensing/) the code base [to a more restrictive license](https://lwn.net/Articles/966133/).
Beginning with version 7.4. Redis will be dual-licensed under the
[Redis Source Available License (RSALv2)](https://redis.com/legal/rsalv2-agreement/) and [Server Side Public License (SSPLv1)](https://redis.com/legal/server-side-public-license-sspl/). Older versions will [remain open source](https://thenewstack.io/new-research-shows-secure-usage-of-open-source-remains-problematic/).
As a result, the Linux Foundation is putting its weight behind a new project named Valkey, as “an open source alternative to the Redis in-memory, NoSQL data store.”
Already, a number of industry players have quickly joined in, including
[Amazon Web Services](https://aws.amazon.com/?utm_content=inline+mention) (AWS), [Google Cloud](https://cloud.withgoogle.com?utm_content=inline+mention), and [Oracle](https://developer.oracle.com/?utm_content=inline+mention).
“By forming Valkey, contributors can pick up where we left off and continue to contribute to a vibrant open source community,” said
[Madelyn Olson](https://www.linkedin.com/in/madelyn-olson-6a5053b6/), an AWS principal engineer and [former longtime Redis maintainer](https://www.linkedin.com/feed/update/urn:li:activity:7176350563071139840/) who co-launched Valkey, in a statement.
“It is nice to see a strong community forming so quickly around Valkey,” chimed in
[Andi Gutmans](https://www.linkedin.com/in/andigutmans/), Google Cloud GM and VP of Engineering for Databases, also in a statement.
At launch,
[ the project](https://github.com/madolson/placeholderkv) has nine contributors — including Olson and two other AWS engineers — and has garnered 1,500 GitHub stars.
Valkey will use Redis v. 7.2.4 as the base, placing it under the open source Berkeley Software Distribution (BSD) three-clause license.
## Redis Cries Foul, Invites the Competition
In an e-mail response to The New Stack, Redis CEO
[Rowan Trollope](https://www.linkedin.com/in/rowant/) all but scoffed at the fork, casting it as the underhanded work of stingy cloud providers to get out of paying licensing fees.
“The major cloud service providers have all benefited commercially from the Redis open-source project so it’s not surprising that they are launching a fork within a foundation,” Trollope wrote.
Redis’ licensing change was a move to establish fair licensing agreements with the cloud providers, Trollope explained. Microsoft
[came to an agreement](https://azure.microsoft.com/en-us/blog/redis-license-update-what-you-need-to-know/), while AWS and GCP have yet to strike a bargain.
Like HashiCorp did before, Redis stressed its commitment to enterprise excellence.
“We remain focused on our role as stewards of the Redis project, and our mission of investing in the Redis source available product, the ecosystem, the developer experience, and serving our customers,” Trollope wrote. “Innovation has been and always will be the differentiating factor between the success of Redis and any alternative solution.”
Naturally, industry observers remain skeptical.
This is the “worst outcome” for Redis labs, wrote
[System Initiative](https://thenewstack.io/system-initiative-a-devops-makeover-by-ex-chef-adam-jacob/) Co-founder [Adam Jacob](https://thenewstack.io/adam-jacob-rebuilding-devops-with-system-initiative/) on X.
“Congratulations! You now have a competitor that’s well funded, ships a trustable product at $0, and will obviously be what cloud providers use to compete,” he
[tweeted](https://twitter.com/adamhjk/status/1773401933073780752).
## What Software Has the Linux Foundation Forked Recently?
In open source terms,
[forking](https://thenewstack.io/may-fork-short-history-open-source-forks/) is the process of [copying a code base](https://thenewstack.io/the-security-risks-of-forking/) and then developing it independently of the originator, often resulting in two separate and soon incompatible code bases.
This is the second time that the non-profit Linux Foundation has backed forkings of commercial software after its (commercially-minded) creator pulled back the licensing terms. In September the foundation
[cloned Terraform](https://thenewstack.io/linux-foundation-joins-opentf-to-fork-for-terraform-into-opentofu/) just a month after HashiCorp moved that Infrastructure as Code (IaC) software to a non-open source, view-only BSL (Business Source License). The software was renamed [OpenTofu](https://thenewstack.io/can-opentofu-become-the-http-of-infrastructure-as-code/).
The
[HashiCorp Vault secrets manager](https://thenewstack.io/hashicorps-releases-hcp-vault-to-combat-secrets-management-fatigue/) was also forked, by engineers at [IBM](https://www.ibm.com?utm_content=inline+mention), [into OpenBao](https://thenewstack.io/meet-openbao-an-open-source-fork-of-hashicorp-vault/), with the aim of becoming a Linux Foundation Edge project.
Following an industry trend, both Redis and HashiCorp have expressed business reasons for moving their respective code bases out of open source licensing, joining other companies
[in the practice](https://www.computerworld.com/article/3714821/software-vendors-dump-open-source-go-for-the-cash-grab.html) such as [Elastic](https://thenewstack.io/this-week-in-programming-aws-completes-elasticsearch-fork-with-opensearch/) and MongoDB.
## What Is Redis?
In its most recent survey, DB_Engines
[ranks Redis](https://db-engines.com/en/ranking) as the sixth most widely-used database worldwide.
The
[Redis project](https://redis.io/) was created in 2009 by [Salvatore Sanfilippo](https://thenewstack.io/redisconf-2020-why-redis-is-more-than-just-a-cache-provider/) as [a high-performance key/value store](https://thenewstack.io/redis-is-not-just-a-cache/) that can be used for caching or as a speedy data store for real-time data analysis, session store, message broker, and many other use cases. Thousands of developers have contributed to the project.
Initially, Valkey (an inverse abbreviation of “key-value”) will run on the Linux, macOS, OpenBSD, NetBSD, and FreeBSD platforms.
The development team plans to continue on the existing Redis roadmap, with planned improvements in slot migration, scalability and stability to the clustering system. Multithreaded performance improvements, triggers, new commands, and vector search support are also on the books.
“Fostering open collaboration that benefits all and not just a single organization is critical in building long-term, sustainable open source communities,” said
[Chris Aniszczyk](https://www.linkedin.com/in/caniszczyk/), CTO of The Linux Foundation, [in a statement](https://www.linuxfoundation.org/press/linux-foundation-launches-open-source-valkey-community). “Having this project in the hands of a foundation, rather than a single company, means Valkey will be community-driven without surprise license changes that break trust and disrupt a level open source playing field.”
A number of
[open source distributions](https://thenewstack.io/distribution-commercialization-and-the-future-of-open-source/), such as [Red Hat](https://www.openshift.com/try?utm_content=inline+mention)‘s Fedora, currently include Redis in their packages, and [would probably be hard-pressed to continue to do so](https://lwn.net/ml/fedora-devel/CAEg-Je_GoiJN6kOj1_K5WqTvA6n0j8r4fi9=C7-WbXLHovM3ow@mail.gmail.com/) given the more restrictive nature of the new Redis license.
The Foundation is not the only one looking to keep the
[Redis open source](https://thenewstack.io/open-source-builders-how-redis-upended-the-database-market/) alive. The [Redict project](https://andrewkelley.me/post/redis-renamed-to-redict.html) was also recently launched with this aim in mind. *David Cassel contributed to this post. * *3/28: This post has been updated with input from Redis.* [
YOUTUBE.COM/THENEWSTACK
Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.
](https://youtube.com/thenewstack?sub_confirmation=1)