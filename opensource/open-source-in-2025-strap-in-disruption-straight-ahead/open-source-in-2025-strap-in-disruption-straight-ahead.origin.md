# Open Source in 2025: Strap In, Disruption Straight Ahead
![Featued image for: Open Source in 2025: Strap In, Disruption Straight Ahead](https://cdn.thenewstack.io/media/2023/12/95c34a5e-year-forecast-1-1024x576.png)
The open source software world can feel like a bubble at times, one in which people who love to solve problems go and tinker with solutions, share ideas freely and build global communities of contributors. They gather at conferences, meetups and online to praise each other’s hard work and innovation, and remind each other how awesome they are.

But outside forces can sometimes shake that bubble like a snow globe. In March, [Redis](https://redis.com/?utm_content=inline+mention) adjusted the licensing for its open source in-memory data store, which [prompted the creation of a Linux Foundation-supported fork](https://thenewstack.io/linux-foundation-forks-the-open-source-redis-as-valkey/), [Valkey](https://thenewstack.io/valkey-whats-new-and-whats-next/).

In December, the community around [Puppet](https://puppet.com/?utm_content=inline+mention), an Infrastructure as Code tool, [announced plans to fork it](https://thenewstack.io/puppets-open-source-community-plans-to-fork-the-program/) in the wake of [November news](https://www.puppet.com/blog/open-source-puppet-updates-2025) that [Perforce](https://www.perforce.com/), its owner, would “ship any new binaries and packages developed by [its] team to a private, hardened and controlled location. Community contributors will have free access to this private repo under the terms of an end-user license agreement (EULA) for development use.”

In other words, Puppet will now be source-available, not open source.

The trend of widely used [open source software moving to more restrictive licensing isn’t new](https://thenewstack.io/hashicorp-abandons-open-source-for-business-source-license/). But the current wave started, arguably, with [HashiCorp’s](https://www.hashicorp.com/?utm_content=inline+mention) August 2023 decision to pull Terraform (and subsequently other products, like Nomad) back from the open source world, assigning them to [Business Source License v1.1](https://www.hashicorp.com/bsl). A community is growing around the fork of Terraform, OpenTofu. Likewise for [OpenBao, a fork of HashiCorp’s Vault secrets manager](https://thenewstack.io/meet-openbao-an-open-source-fork-of-hashicorp-vault/) created at the end of 2023.

Users are truly experiencing some “turbulation” — a word [Matt Butcher](https://thenewstack.io/author/mattbutcher/), CEO and co-founder of [Fermyon Technologies](https://www.fermyon.com/?utm_content=inline+mention), coined about the [open source licensing](https://thenewstack.io/how-do-open-source-licenses-work-the-ultimate-guide/) dramas of 2023 and 2024 — a mashup of “turbulence” and “tribulation.” His company was hit by turbulation caused by HashiCorp’s decision, since Fermyon uses HashiCorp’s Nomad. Butcher told The New Stack (TNS): “We literally ended up asking them for exceptions to bits and pieces, because we were running a patched version of Nomad.”

But as a startup founder, he is watching the licensing decisions carefully. Fermyon, which focuses on [WebAssembly](https://thenewstack.io/webassembly-in-2024-components-are-and-are-not-the-big-story/), has both open source projects and paid enterprise-level products.

“I’m kind of hoping that that particular approach to things remains still highly tenable, and I think it will,” he told TNS at [KubeCon + CloudNativeCon North America](https://events.linuxfoundation.org/kubecon-cloudnativecon-north-america/), in November. “If we can plan that way from the get-go, we don’t have to yank things back, which is what tends to build up the bad faith in the community, or the assumption of bad faith.”

In addition to the demands of late-stage capitalism and impatient investors in companies built on open source tools, other outside factors are pressuring the open source world. There’s the promise/threat of generative AI, for instance. Or the shifting geopolitical landscape, which brings new security concerns and governance regulations.

And there’s the perennial issue of how to compensate the global army of unpaid, volunteer maintainers that so many projects rely on.

What’s ahead for open source in 2025? Here are some ideas, gleaned from interviews at this past autumn’s tech conferences and also from a [New Stack survey](https://thenewstack.io/programming-languages-coverage-matters-most-say-tns-readers/) of more than 120 industry experts, conducted in November, that asked about the future of open source, developers’ use of AI, and IT infrastructure.

## More Consolidation, More Licensing Changes
Expect more “turbulation” in the coming year, as the sprawling cloud native ecosystem consolidates. [IBM’s](https://www.ibm.com?utm_content=inline+mention) [$6.4 billion purchase of HashiCorp, announced in April](https://thenewstack.io/ibm-purchases-hashicorp-for-multicloud-it-automation/) and now expected to close in Q1 of 2025, may herald a trend.

[Matt Moore](https://www.linkedin.com/in/mattmoor/), CTO of [Chainguard](https://www.chainguard.dev/?utm_content=inline+mention), said in a response to the TNS survey that he hopes the IBM-HashiCorp deal might bear fruit for the open source community. “I kind of hope that with IBM’s acquisition of Hashi that [they might mend fences between Terraform and OpenTofu](https://thenewstack.io/with-ibms-open-source-roots-terraform-could-be-free-again/). There’s already a precedent here, with [Elastic’s](https://www.elastic.co/) reversal of a similar decision.”
Elastic moved [Elasticsearch and Kibana to open source licensing in August](https://thenewstack.io/whats-behind-elastics-unexpected-return-to-open-source/) by adding a [GNU Affero General Public License](https://www.gnu.org/licenses/agpl-3.0.en.html) to them. The move came three years after the company’s decision to move both projects away from Apache 2.0 licenses. Elastic’s search and analytics engine, Elastic, has been seeing competition from [OpenSearch](https://thenewstack.io/opensearch-how-the-project-went-from-fork-to-foundation/), a fork sponsored by [Amazon Web Services](https://aws.amazon.com/?utm_content=inline+mention).

What’s tricky about guessing the future of licensing is that the pressures on open source software sponsors don’t simply push in one direction; [competition](https://thenewstack.io/why-open-source-forking-is-a-hot-button-issue/) could make a company either embrace more restrictive licensing for an open source tool, or create an open source version to speed adoption.

“Predicting what open source projects are moving to a more restrictive model is highly speculative,” said [Scott Wheeler](https://www.linkedin.com/in/dscottwheeler/), cloud practice lead at Asperitas, in response to The New Stack survey of industry experts.

Still, Wheeler pointed to Elasticsearch and Kibana as examples that might feel new licensing pressures down the road. And, based on the HashiCorp example, he thinks the following projects might experience similar pressures in the future:

[Hadoop](https://github.com/apache/hadoop),[Kafka](https://github.com/apache/kafka),[Lucene](https://github.com/apache/lucene)(sponsored by the[Apache Foundation](https://www.apache.org/)).[Kubernetes](https://github.com/kubernetes/kubernetes)and[Prometheus](https://github.com/prometheus/prometheus)(sponsored by the[Cloud Native Computing Foundation](https://cncf.io/?utm_content=inline+mention)).[Ansible](https://github.com/ansible/ansible)(sponsored by[Red Hat](https://www.openshift.com/try?utm_content=inline+mention)).
All but Ansible, which is covered by a [GNU General Public License v3](https://www.gnu.org/licenses/gpl-3.0.en.html), are under [Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0) licenses currently. (And all but Ansible are housed at nonprofit foundations, presumably sheltered from commercial concerns.)

By contrast, [Jason Perlow](https://thenewstack.io/author/jason-perlow/), president of Argonaut Media and former editorial director at [The Linux Foundation](https://training.linuxfoundation.org/training/course-catalog/?utm_content=inline+mention), told TNS that “the reverse of this is going to transpire.”

“I feel it is likely that Chrome and possibly Android are likely to become independently governed open source projects, rather than sold off by [Google](https://cloud.google.com/?utm_content=inline+mention) per antitrust regulation,” Perlow said in response to a TNS survey question about the future of open source. (In August, a US District Court for the District of Columbia found the company had maintained an illegal monopoly in online search.)

[David DeSanto](https://www.linkedin.com/in/ddesanto/), chief product officer at[ GitLab](https://about.gitlab.com/?utm_content=inline+mention), expects to see more formerly open source projects move to more restrictive licensing in 2025. But he’s taking a glass-half-full view of the trend.
“I expect that’ll be open to a whole new breed of what open source can mean,” he told The New Stack at KubeCon in November. He pointed to HashiCorp’s moves as an example.

“They’ve been moving Vault off of a very permissive open source license, but that’s led to OpenBao. And at GitLab we’re building our own native secrets manager. That’s going to generate the next round of future open source.”

## The Open Source AI Debate: Just Getting Started
In October, the Open Source Initiative [released version 1.0 of its definition of open source AI](https://thenewstack.io/the-open-source-ai-definition-is-out/). [Stefano Maffulli](https://thenewstack.io/what-does-open-mean-in-ai/), OSI’s executive director, told The New Stack ahead of its release that [1.0 is a “humble” document](https://thenewstack.io/osi-finalizes-a-humble-first-definition-of-open-source-ai/), a work in progress.

In the wake of the definition’s release, [critics](https://thenewstack.io/the-open-source-ai-definition-what-the-critics-say/) picked it apart, complaining that it gives some vendors cover if they don’t want to reveal their training data, [that the definition fundamentally changes the meaning of open source](https://thenewstack.io/the-case-against-osis-open-source-ai-definition/), and that, given how different AI is from software code, maybe OSI shouldn’t have attempted to define open source AI at all.

“There’s an interesting debate around what constitutes ‘open source’ in AI,” said [Yang Li](https://thenewstack.io/author/yang-li/), COO at [Cosine](https://cosine.sh/), in response to The New Stack’s survey.

“[Meta](https://about.meta.com/?utm_content=inline+mention) and Google just [got called out for claiming they’re open source when they’re not](https://thenewstack.io/why-open-source-ai-has-no-meaning/). The real question is: as we generate more [synthetic data](https://thenewstack.io/the-future-of-ai-and-travel-relies-on-synthetic-data/), where do you draw the line? You can be open about your data sources but keep your synthetic data generation process proprietary. It’s a blurry line between revealing your data set and revealing how you created it.”

Clearly this debate is just getting started. Moves by the big players will likely be part of 2025’s conversation. In a company blog post on Dec. 26, [OpenAI stated its intention](https://openai.com/index/why-our-structure-must-evolve-to-advance-our-mission/) to transform from a for-profit and nonprofit structure to a public benefit corporation — like rivals Anthropic and xAI — that supports a nonprofit.

The big takeaway: AI and its major players are certainly poised to suck a lot of the oxygen out of the open source bubble in 2025.

“The biggest threat will likely be the sustainability and maintainability of existing open source projects,” replied [Christian Posta](https://thenewstack.io/author/christian-posta/), global field CTO at [Solo.io](https://solo.io?utm_content=inline+mention), in response to a survey question about the future of open source.

“As AI continues to dominate technological advancements, there has been a noticeable shift in focus toward AI-related initiatives. This often leaves mature projects, such as CNCF-graduated projects, with fewer maintainers, jeopardizing their ability to remain healthy and sustainable in the long term.”

And it will become harder in 2025 for entities that aren’t Google, Meta, [Microsoft](https://news.microsoft.com/?utm_content=inline+mention) and its ilk to compete in open source AI.

“For AI applications, computation and data is central, but only the giants like Google or Meta can obtain the data easily,” said [James Luan](https://thenewstack.io/author/james-luan/), vice president of engineering at [Zilliz](https://zilliz.com?utm_content=inline+mention), in response to the TNS survey.

“Smaller groups of developers or even individual developers do not have this luxury, and therefore will find it continuously challenging to find open source models.”

In fact, some are concerned that deep learning models could eventually overtake open source development. There’s [pushback on that idea](https://thenewstack.io/genai-wont-replace-open-source-says-aws-exec/). But the threat looms nevertheless.

“GenAI tools, often proprietary, offer developers advanced automation, code generation and observability capabilities that could outpace open source alternatives in convenience and performance,” warned [Eran Kinsbruner](https://www.linkedin.com/in/erankinsbruner/), head of product marketing at [Lightrun](https://lightrun.com/?utm_content=inline+mention), in his response to the TNS survey.

“At the same time, complex architectures demand highly integrated, scalable solutions, which proprietary platforms are better positioned to deliver. This shift risks sidelining open source projects, especially those unable to keep up with AI-driven innovations or the demands of distributed systems, leading to reduced adoption and investment in open-source ecosystems.”

## Security and Compliance Concerns Will Rise
The world, you may have noticed, is not particularly peaceful at the moment. And cyberattackers love to create opportunities out of crises.

“Aside from AI, the other big, huge debate [is] going to be security and compliance,” OSI’s Maffulli told The New Stack. “It’s already there. But in 2025 it is going to be even more, given the geopolitical landscape getting more and more complicated and convoluted. It’s going to be big.”

AI has the potential to supercharge threats, noted [Idan Plotnik](https://www.linkedin.com/in/idanplotnik/), co-founder and CEO of [Apiiro](https://apiiro.com/), in response to the TNS survey.

“In 2025, open source software threats will shift from traditional vulnerabilities to AI-generated backdoors and malware embedded in open source packages,” said Plotnik. “With attackers leveraging AI tools to develop and disguise malware within open source code, addressing these new threats will require a significant advancement in security tools to stay ahead of these quickly evolving challenges.

A bit of good news, however: In 2025, AI automation tools might help find and remediate more unmaintained open source code and technical debt, helping to close some of the potential on-ramps for hackers.

“I believe with the proliferation of AI coding tools we should definitely see some decrease in unmaintained open source components primarily because it would be easier and faster to write code for developers even with limited experience in some highly niched areas,” said [Madhukar Kumar](https://www.linkedin.com/in/madhukarkumar/), chief marketing officer at [SingleStore](https://www.singlestore.com/?utm_content=inline+mention), in response to the TNS survey.

## Paying Maintainers: More Cash, Creativity Needed
Nearly every stack uses open source code but still — *still!* — most open source maintainers essentially get paid in GitHub stars and kissy-face emojis.

Sixty percent of open source maintainers surveyed by [Tidelift](https://tidelift.com/), in a study published in September, said [they aren’t paid for their work](https://thenewstack.io/open-source-paid-maintainers-keep-code-safer-survey-says/). (Perhaps not coincidentally, about the same percentage said they had quit or had considered quitting their project.)

This situation — the continued dependence on an army of [unpaid, underappreciated hobbyists](https://thenewstack.io/what-happens-to-relicensed-open-source-projects-and-their-forks/) to maintain essential codebases — is going to be the biggest threat to open source in 2025, including the security of its tools and platforms, say industry experts.

“Open source is sprawling and often thanklessly maintained by folks in their nights and weekends,” said Moore of Chainguard, in response to the TNS survey. “As the complexity and breadth of open source ecosystems expand, the rate of necessary updates accelerates exponentially.”

“As more organizations integrate open source solutions, the potential for unpatched vulnerabilities and outdated configurations increases, exposing businesses to significant security and performance challenges.”

[Jeff Hollen](https://www.linkedin.com/in/jeffhollan/), director of product for Snowpark, the ecosystem and developer platform at [Snowflake](https://www.snowflake.com/?utm_content=inline+mention), replied to the TNS survey with a comment on the importance of paying the people who build and maintain open source projects.
“Open source depends on sponsors and supporters,” Hollen wrote. “Many maintainers and contributors (myself included) participate in open source in addition to their day-to-day job responsibilities. The biggest threat to open source would be if significant enterprise sponsors stop encouraging, promoting and supporting those efforts to help contributors and maintainers get some value from them.”

In addition to the contributions of sponsors like Tidelift and by large corporations to put productive maintainers on their payrolls, expect some creative attempts to compensate open source developers to emerge in 2025.

[One to watch in the coming year is tea](https://thenewstack.io/is-crypto-the-solution-to-paying-open-source-developers/), a decentralized technology protocol co-founded by Homebrew creator [Max Howell](https://www.linkedin.com/in/mxcl). Howell has launched Chai, which measures open source vitality through package manager data.
Participants who have signed up for a “testnet” of the project are earning tokens; at some point in 2025, when the “mainnet” stage of the project launches, those tokens will be launched on a number of cryptocurrency exchanges, with the intent of having monetary value.

About 16,000 projects signed up for Chai’s testnet, Howell told The New Stack. It’s a mere sliver of the 10.5 million open source projects worldwide, but it’s a clear indication that there’s raging demand for innovative thinking when it comes to compensating open source’s makers.

[Lawrence E. Hecht](https://thenewstack.io/author/lawrence-hecht/) contributed to this post.
[
YOUTUBE.COM/THENEWSTACK
Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.
](https://youtube.com/thenewstack?sub_confirmation=1)