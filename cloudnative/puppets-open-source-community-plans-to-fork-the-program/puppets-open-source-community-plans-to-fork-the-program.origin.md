# Puppet’s Open Source Community Plans to Fork the Program
![Featued image for: Puppet’s Open Source Community Plans to Fork the Program](https://cdn.thenewstack.io/media/2024/12/db89c722-puppet-fork-2-1024x576.jpg)
The community around [Puppet](https://puppet.com/?utm_content=inline+mention), a popular Infrastructure as Code (IaC) tool, is forking the program.

Or, as community activists would have it, Perforce forked Puppet, and the community is just restoring the open source project.

When [Luke Kanies](https://www.linkedin.com/in/lukekanies/) created Puppet in 2005, a server configuration and management tool, no one knew what [DevOps](https://roadmap.sh/devops) was because the term hadn’t been defined yet. [Infrastructure as Code](https://thenewstack.io/infrastructure-as-code/) was still years away. Puppet would become a leader in both. However, [Puppet would miss the Kubernetes boat,](https://thenewstack.io/puppet-missed-the-kubernetes-boat-then-perforce-came-along/) and [ Perforce](https://www.perforce.com/) acquired Puppet in 2022.

From the point of view of open source Puppet developers, things started to go wrong. Now, the community has had enough, and [it has decided to fork Puppet](https://github.com/OpenPuppetProject/planning/discussions/11).

According to a [GitHub Ideas forum post](https://github.com/OpenPuppetProject/planning/discussions/11) by [Antoine Beaupré](https://gitlab.com/anarcat), a Puppet programmer, the Puppet developers hadn’t decided to fork the code. No, it was Perforce.

“What Perforce is doing right now is taking the open source code that we have collaboratively used, debugged, written, collaborated, stared at and deployed on thousands of machines, and closing access to it to paying customers,” Beaupré wrote. “Therefore, we are not forking Puppet, Perforce is forking Puppet,”

What he was referencing was Perforce’s announcement on Nov. 7 that “in early 2025, [Puppet will begin to ship any new binaries and packages developed by our team to a private, hardened, and controlled location.](https://www.puppet.com/blog/open-source-puppet-updates-2025) Community contributors will have free access to this private repo under the terms of an End-User License Agreement (EULA) for development use. There will be no license changes for the open source version of Puppet.”

The community has found that unacceptable. “They claim to not change the license of the software, but that’s really an insignificant detail because, effectively, the source code for Puppet, as produced by Perforce, will no longer be publicly available.”

## OpenPuppetProject Is Live
If it comes to pass, the Puppet fork would be the latest in a recent series of instances when an open source community forks a popular project after the company that created it announces plans for more restrictive licensing. In August 2023, a fork of [HashiCorp’s](https://www.hashicorp.com/?utm_content=inline+mention) [Terraform was created and eventually named OpenTofu](https://thenewstack.io/will-opentofu-dethrone-terraform-in-iac/). In March, the [Valkey fork was created](https://thenewstack.io/valkey-whats-new-and-whats-next/) in response to licensing changes by [Redis](https://redis.com/?utm_content=inline+mention).

For the record, Puppet has long existed in two forms: An open source version under the [Apache license](https://thenewstack.io/how-do-open-source-licenses-work-the-ultimate-guide/) and Puppet Enterprise, a commercial version built on top of the open source core.

In addition, the community doesn’t like that going forward, Perforce will require community contributors to agree to an end-user license agreement for development use.

“I am here because I manage a fleet of 100 machines for the Tor Project,” Beaupré wrote in his GitHub forum post. “The Debian Project, Riseup, Koumbit, and so many other organisations are in the same boat. We can’t just get off this Puppet ship.”

Some users are also complaining that Perforce has not been receptive to their concerns. As a community member who goes by the handle GeneBean on Mastodon wrote on Dec. 16, “There was a ‘town hall’ today in which Perforce made it quite clear they are going to claim they want to work with the community while not actually doing so.” Therefore, although “none of us in the[ #Puppet](https://fosstodon.org/tags/Puppet) community wanted to take the fork route. [Our hand has been forced by the actions of Perforce.](https://fosstodon.org/@genebean/113664863697232378)”

Thus far, community activists have created an [OpenPuppetProject repository](https://github.com/OpenPuppetProject) on GitHub, but it does not yet include a fork of the Puppet source code. Organizational discussions are ongoing. [Overlook InfraTech](https://overlookinfratech.com/), a public benefit company, is “sponsoring and stewarding” the OpenPuppetProject, according to the project repo’s README file.

No name has been picked yet for the fork. Some [suggestions](https://github.com/OpenPuppetProject/planning/discussions/9) include Manikin, Dolly, and my favorite, Muppet.

## Perforce’s Response
In response to the community’s plans for forking Puppet, a Perforce representative told The New Stack via email:

“Over the last few years, we’ve seen various changes happening within the infrastructure automation space that have required Perforce to rethink how we, as an organization, should be contributing to open source Puppet. Major factors include an increased need for compliance, downstream priorities of our enterprise customers, and the rising tax to directly manage open source Puppet in parallel.

“Given these factors, we are committed to keeping our same license but will start to ship new binaries and packages developed by our team to a hardened, enterprise-facing repository. Previously, we made these available to all open source users as well. Establishing a hardened repository for releases allows us to provide consistent enterprise-grade security and support, which many of our largest companies running Puppet have been asking for.

“This new repository and subsequent releases will be available under the terms of an End-User License Agreement (EULA). It allows developers free access to our hardened Puppet releases (up to 25 nodes) and is intended to support ongoing use by the broader ecosystem. Upstream repositories will remain where they are and under Apache 2.0 license, with the community retaining co-authorship of that code base, funded by Perforce.

“Perforce Puppet will continue to look for and drive points of collaboration and ongoing communication with the community, including town hall sessions, as we recognize the important contributions of so many over the years. We see our investment in enterprise as creating longer-term demand and confidence in the Puppet ecosystem from which the community will benefit.”

If that sounds to you like just a rewording of Perforce’s recent policy change, you’re right. It does, and it is just a rephrasing of its position. No matter who you want to credit — or blame — the Puppet fork on, it is coming.

Perforce’s statement also makes it clear that given a choice between honoring Puppet’s open source roots and, theoretically, making Puppet more attractive to business customers, Perforce is putting profits first. Whether the company’s assumption will make it more profitable remains to be seen.

Back when Perforce acquired Puppet, Kaines, who then sat on Puppet’s board but was no longer a manager, tweeted, “[I’m frankly not a huge fan of acquisitions.](https://x.com/lkanies/status/1513552978371772419)” Nonetheless, he added, “But this was the right outcome for Puppet and its people.”

Kaines hasn’t commented publicly about these latest developments, and he has not yet responded to requests from The New Stack for comment.

[
YOUTUBE.COM/THENEWSTACK
Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.
](https://youtube.com/thenewstack?sub_confirmation=1)