# How Developers Can Head Off Open Source Licensing Problems
![Featued image for: How Developers Can Head Off Open Source Licensing Problems](https://cdn.thenewstack.io/media/2024/06/6153560b-problems-with-open-source-1024x683.jpg)
Using open source can go south, and the frontend is not immune to the dangers. From corrupted software to license changes, open source software can “turn” against developers.

“The frontend is no different than any other piece of software. Definitely, it’s an exposure,” said [Dotan Horovits](https://www.linkedin.com/in/horovits/?originalSubdomain=il), chief evangelist at [Logz.io](https://logz.io/). Horovits is an open source advocate as a Cloud Native Computing Foundation (CNCF) ambassador, but he also speaks on the down side of open source.

## Open Source Gone Bad
He pointed to the [2022 incident with Marak Squires](https://thenewstack.io/is-open-source-really-free-if-we-arent-allowed-to-break-it/), who corrupted the libraries faker.js (with 2.5 million downloads at the time) and colors.js (with 22.4 million downloads when the incident occurred).

“It was massive, until [npm](https://thenewstack.io/npm-security-woes-continue-amidst-a-series-of-cdn-attacks/) reverted and stopped the ripple effect from spreading further,” Horovits said. “So yes, frontend is exposed, just like any of us. It’s not about the domain. It’s about software.”

There are other examples, such as [HashiCorp’s change of the Terraform license](https://thenewstack.io/opentofu-vs-hashicorp-takes-center-stage-at-open-source-summit/). Originally under the Mozilla open source Mozilla Public License v2.0 (MPL 2.0), Terraform’s license was changed to the Business Source License (BSL) v1.1, which is not open source but considered “source-available.” That led to the the Terraform community forking Terraform to create OpenTF and the [Linux Foundation taking it up as OpenTofu](https://thenewstack.io/linux-foundation-joins-opentf-to-fork-for-terraform-into-opentofu/).

“It wasn’t just relicensing,” Horovits told The New Stack. “It was also taking the Terraform registry, which was an authoritative place, the hub, if you will, for placing all the Terraform modules and making it closed for other utilities.”

[Elasticsearch is another example](https://www.elastic.co/blog/licensing-change). Elastic moved Elasticsearch and its data analytics tool, Kibana, from the Apache 2.0 license to be dual licensed under Server Side Public License (SSPL) and the Elastic License. But it was more than a license change, Horovits said.
“They had shippers that collect telemetry locally from the application, then send it to a backend Elasticsearch cluster for storage, indexing and so on; and for over a decade, it’s been open source,” he said. “Now they’ve changed the backend — that everyone knows. The thing that people maybe are less aware of is that even the shippers that remained Apache to license —which is an open source license for all purposes, OSI [Open Source Initiative] approved — they made changes so that they check that the backend cluster to which they send, that’s not part of the open source. If the target cluster, remote cluster, is not … authorized, then it won’t work. It will break.”

Linkerd provides another problematic example. There the source code remained under an open source license, but [Linkerd is no longer releasing deployable artifacts](https://linkerd.io/releases/).

**“**There’s something beyond just the license, and it is the contract, let’s say the agreement, with the community. Now for a long time, the community has been in agreement that the project releases artifacts that you can then take and deploy and use that in your production environment, and suddenly it’s no longer the case,” he said.
“The reason it’s no longer the case is not a mutual decision by a governance committee of all the [people] representing the whole community. It was primarily, chiefly driven by a single vendor to steer organizations wishing to deploy Linkerd for production usage to their commercial offering.”

## Warning Signs Your Open Source Project is Turning
Licensing is just the beginning of the story, Horovits said. Developers and organizations that use [open source software need to take a more mature](https://thenewstack.io/3-ways-to-drive-open-source-software-maturity/) approach to it use.

“People need to look at open source more maturely, understand and ask more questions, beyond which license. Also ask who’s behind the open source? Is that a single vendor, or is that a sustainable diversity of entities, maybe even a mix of vendors and end users, that will guarantee better sustainability and lower odds of such thing happening?” He said. “Is there a clear governance policy behind the [open source to clearly define](https://thenewstack.io/open-source-initiative-hits-the-road-to-define-open-source-ai/) the ways in which modifications can be made — certainly licensing, but even smaller ones — and who can join?”

One early sign of trouble could be that the suddenly external contributions are blocked or the project maintainers are not being responsive to suggestions from the community, he said.

“Why would that be? Probably because it, in a way, conflicts with their commercial offering that they developed around the open source or think [it is] just not their priority,” he said. “These things should not happen in open source.”

The governance policy can also provide a warning sign, as can a mix of open source and proprietary code, he added.

## Check the License
There’s not a lot developers can do if someone decides to change the license, except to possibly fork the project from an earlier version. The license change won’t be retroactive to early versions, Horovits said.

What developers can do is work with legal or an [open source program office](https://thenewstack.io/does-your-organization-need-an-open-source-program-office/) on licensing issues. That’s because even with an open source license, there can be clauses that create repercussions for developers and their organizations.

Developers should also perform license checks any time they have to update [open source code](https://thenewstack.io/how-donating-open-source-code-can-advance-your-career/) to ensure the license hasn’t changed.

“If you automatically update to the next release, if the next release has been relicensed, then you’re automatically becoming exposed without anyone having any judgment in the matter, just because you pulled the latest version, and that’s it,” he said.

## Review the Source Code
He also suggested going into the code to understand how it works and to check for unusual code that might indicate a future problem.

“While you’re going in there, keep your eyes and ears open, and if you see something that might indicate these sorts of non-open source patterns,” he said. “When Elasticsearch changed the license and the community forked the project to create OpenSearch, the vision is you just click the fork button and you have your own fork, right? But it actually was very, very [much] a very tedious process, to the extent that some developers needed to go line by line to separate the proprietary code. In [the] Elastic case, it’s called [XPack](https://www.elastic.co/guide/en/elasticsearch/reference/7.17/setup-xpack.html), licensed from the open source code.”

## Understand the Governance
There are proactive steps developers can take as well. For instance, developers can opt for code that isn’t controlled by a single vendor.

“The other side, beyond the licensing, is to look and to understand who’s behind the license, the governance, policy,” he said.

Another option to provide some cushion of protection is to use a vendor that specializes in distributing a particular open source solution. A distro vendor can provide indemnification against exposure, he said. They also provide other benefits, such as support and certification to run on specific hardware set-ups.

Developers can also look for [open source solutions that are under a foundation](https://thenewstack.io/value-investing-open-source-foundations/), rather than a single company, he suggested, although he cautioned that even that isn’t a failsafe measure.

“Even foundations are not bulletproof,” he said. “Foundations provide some oversight, some governance and some other means to reduce the risk. But if ultimately, down the path, it ends up again being backed up by a single vendor, then it’s an issue even under a foundation.”

Foundations also need to learn how to better steer and govern a project with transparency, he added.

“Within the CNCF, we’re revisiting the more rigorous understanding in terms of what is expected, or at least for the project to very clearly state what the expectation is,” he said.

[
YOUTUBE.COM/THENEWSTACK
Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.
](https://youtube.com/thenewstack?sub_confirmation=1)