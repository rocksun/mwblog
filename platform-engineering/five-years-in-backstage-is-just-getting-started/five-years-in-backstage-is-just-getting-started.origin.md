# Five Years In, Backstage Is Just Getting Started
![Featued image for: Five Years In, Backstage Is Just Getting Started](https://cdn.thenewstack.io/media/2025/04/2e1cbd5f-chris-tyson-backstage-kubecon25-2-1024x576.jpg)
LONDON — While [Backstage](https://backstage.io/) has only just turned five, it really is the grown-up of the [platform engineering](https://thenewstack.io/platform-engineering/) world, having [set the standard for internal developer portals](https://thenewstack.io/spotifys-backstage-a-strategic-guide/). Not only in popularity but in open source community impact as well.

Backstage started as an open ecosystem within the audio streaming company [Spotify](https://thenewstack.io/how-spotify-achieved-a-voluntary-99-internal-platform-adoption-rate/), where developers inner-sourced more than a hundred plugins to extend its capabilities. Over the last five years, it became a large open source project with more than 3,400 adopters, including [Airbnb](https://thenewstack.io/platform-as-a-product-101/), Booking.com, H&M, HCA Healthcare, [LEGO](https://thenewstack.io/how-data-helps-lego-click-developer-experience-into-place/), OVO Energy, Philips, [Toyota North America](https://thenewstack.io/how-toyota-drove-agile-load-testing-to-the-cloud/) and [SeatGeek](https://thenewstack.io/case-study-how-seatgeek-adopted-hashicorps-nomad/). More than two million developers outside the founding company now use Backstage.

Last year, the [Backstage open framework for building developer portals](https://github.com/backstage/backstage) was one of the [Cloud Native Computing Foundation’s](https://cncf.io/?utm_content=inline+mention) (CNCF) top five projects in terms of velocity. In 2023, it had more commits than any other [CNCF project](https://landscape.cncf.io/). The open source project is already undergoing the security audit needed to join the CNCF’s graduated projects.

The Backstage open source ecosystem now has about 1,600 contributors, with 13,000 developers having earned the [Backstage certification](https://www.cncf.io/training/certification/cba/). There are more than [230 Backstage plugins](https://backstage.io/plugins/), including those integrating with [Argo CD](https://thenewstack.io/make-a-scalable-ci-cd-pipeline-for-kubernetes-with-github-and-argo-cd/), [Datadog](https://www.datadoghq.com/?utm_content=inline+mention), [GitHub Actions](https://thenewstack.io/boost-your-ci-cd-pipeline-automate-docker-with-github-actions/), [Grafana](https://thenewstack.io/grafana-seeks-to-correct-observabilitys-historic-terrible-job/), [Snyk](https://snyk.io/?utm_content=inline+mention) and [Terraform](https://thenewstack.io/new-terraform-features-manage-migrations-modules/). [Spotify Portal](https://thenewstack.io/new-spotify-portal-for-backstage-eases-platform-engineering/) is the pre-build internal developer portal Software as a Service (SaaS) offering released last year.

At [KubeCon + CloudNativeCon Europe](https://thenewstack.io/kubecon-cloudnativecon-eu-2025/), The New Stack sat down with [Tyson Singer](https://www.linkedin.com/in/tysonsinger/), head of platform and technology at Spotify, and [Chris Aniszczyk](https://www.linkedin.com/in/caniszczyk/), CTO of the CNCF, for an exclusive reflection on how Backstage grew from an internal dev portal into the open source framework with [89% market share](https://newsletter.getdx.com/p/backstage-and-the-developer-portal-market). And, of course, they talked about some exciting announcements about Backstage plugins and [the future of platform engineering in the age of AI](https://thenewstack.io/whats-the-future-of-platform-engineering/).

**Open Source Paves the Way**
Spotify engineering aims to be the first to open source its innovations — like its internal developer portal framework — because otherwise, its developers will eventually be forced to move to other tooling.

The company learned that lesson the hard way with [Kubernetes](https://thenewstack.io/kubernetes/), when Spotify first chose a different vendor for its container orchestration. Later, when Spotify had to replatform to K8s when that orchestrator triumphed in the market, Singer said, the move cost the streaming company $10 million. Open source, he said, is just good economic sense.

Once that shift to Kubernetes was complete, Spotify became an early investor in its own developer experience and developer productivity.

“One of the things that Spotify learned early on, quite a long time ago — before the [term] ‘platform engineering’ was actually coined — was that there are a set of pressures that you end up having that really focuses you on improving the developer experience,” Singer said.

“We were competing with the biggest companies in the world. We were growing very fast, and we needed to really focus on fast feature development,” he continued. “As we shifted away from spending as much time on [those] lower-level infrastructure layers, we shifted up the stack to make those feature developers move much faster.”

As the tech industry rides another economic downturn, he only predicts more emphasis on developer experience. Companies have to do more with less.

“A lot of our tech companies [customers] are looking at: How do I get more efficient with my workforce?” Singer said. “Backstage is — and IDPs in general are — a very, very effective way to do that, to make things simpler [and] more similar.”

One focus of his platform and engineering organization is to figure out how to foster more T-shaped developers: those who dive deep into an area of expertise, but also have a good understanding of other domains.

At Spotify, this translates to backend developers being able to do fast data engineering. But to achieve that, everything has to look the same, across the whole data ecosystem, pipelines and endpoints. That’s done via a software catalog that encourages cross-organizational discoverability and reusability.

“I think as we make more types of capabilities available, we see more and more folks be like, ‘That’s our problem as well,’” Singer said. And then, once you solve for the main developer experience problems, like for backend developers, you can replicate those solutions for other parts of an R&D organization, like the data ecosystem.

Currently in the alpha testing stage for existing Portal customers, this [data experience plugin for Backstage](https://backstage.spotify.com/docs/portal/guides/data-experience#overview) will soon be released into the premium Portal offering. This product will:

- Enable organizations to discover, understand and manage business data within Portal.
- Ingest metadata from different data sources, then model it in the Backstage software catalog, providing visibility into the data ecosystem on the same plane as all other software entities.
- Integrate with data warehouse tools BigQuery, Redshift, Snowflake and dbt.
- Integrate with core features of Portal to enable teams to search, catalog and manage datasets in the exact same manner as software.
“Now I can solve all the problems from the chaotic data ecosystem also in there, using the same paradigms,” Singer said, “using the same things like Soundcheck that allow you to drive quality into your ecosystem, defragment the ecosystem and get to the point that every company needs [for] faster development and features.”

Soundcheck is one of the most popular Backstage plugins that focuses on team health and alignment around [DevOps best practices](https://thenewstack.io/devops/).

**Maintainer, Contributor and User, Too**
Backstage makes Spotify an open source business, in addition to its core mission of audio streaming.

“One of the challenges of being a maintainer, contributor and user of a product is that you started with something that maybe was a little bit different than what you released,” said Singer.

This “diamond problem,” as he calls it, emerges when in-house and open source projects diverge. As the open source project starts to dominate, the in-house team works to bring them back together. To be more cost-effective, the Spotify team has been migrating and refactoring its own version of Backstage to be more like the open source version. The two versions are very near convergence, Singer said.

This [business/open source game](https://thenewstack.io/entrepreneurship-for-engineers-from-open-source-to-monetization-profit/) of Jenga comes down to tool and language choices, too. He described Spotify as “primarily a [Google](https://cloud.google.com/?utm_content=inline+mention) shop,” which means his platform team would normally build for data products like [BigQuery](https://thenewstack.io/bigquery-pricing-a-users-guide/) and [Dataflow](https://cloud.google.com/products/dataflow). However, because [Snowflake](https://www.snowflake.com/?utm_content=inline+mention) is also very popular, even though Spotify doesn’t use it, the data experience plugin had to be compatible with it.

“We developed the plugin so that you could integrate with enough data sources that it wasn’t too hard for us to just make a few tweaks,” Singer said.

“That’s a that’s a fairly common pattern, as we take the plugins that we have internally, which we think are valuable, and do sort of 70% of the work that everybody needs to do. And then there’s like a 30% where we have to customize to cases that we don’t use.”

In the end, he added, these seemingly selfless choices are actually a “positive force for quality,” as these choices help Spotify abstract the problem while reinforcing domain boundaries.

In another curb benefit, [PagerDuty](https://www.pagerduty.com/?utm_content=inline+mention) is currently a design partner for Portal. Because PagerDuty “has put a lot of work into making sure that their plugin is one of the most valuable plugins out there,” Singer said, this plugin “instruments the Backstage ecosystem, and provides high-quality signal back to Spotify developers.”

**Metrics Always Matter**
Since an [internal developer platform](https://thenewstack.io/7-core-elements-of-an-internal-developer-platform/) or portal is distinguished by being optional to use, adoption rate is one of the key measures of success. Before looking to external usage, it’s important to look within Spotify.

All of the open source community growth has been achieved while still engaging the Spotify developer teams with Backstage. Spotify’s internal Backstage adoption rate remains at an impressive 96% across all of its research and development workers, not just developers.

“We follow a tremendous number of metrics for our development ecosystem,” Singer said, including the instrumentation of the entire development ecosystem, the integrated development environments and human resources systems within Backstage.

At a time when #RTO — return to office — is trending, Spotify has publicly doubled down on its remote work policy. That decision wasn’t just made on a whim. As Singer said, “We look at: Are our remote developers more or less productive than people who are in our offices? And we really don’t see any difference.”

Being a long-term customer of the [DX](https://getdx.com/?utm_content=inline+mention) [developer insights platform](https://thenewstack.io/4-north-star-metrics-for-platform-engineering-teams/), Spotify and DX partnered and last week released a [DX Backstage plugin](https://backstage.spotify.com/partners/dx/plugin/dx/) so that other organizations can dive into the measurable developer experience.

“They’re really good — maybe not as good as what we have internally at Spotify, but they’re really good,” Singer said. “I think this is going to be a really big value add for folks as they try to figure out how to get value out of the Backstage and get [return on investment] and understand where they should focus.

“DX has one thing that others don’t have, which is they have a lot of information around the industry. So I look at their industry data so that you can compare and contrast how you’re doing, as well.”

Part of the mission of platform engineering teams is to [prove the business value of developers](https://thenewstack.io/the-real-business-value-of-platform-engineering/) and, by extension, why it’s important to dedicate funds to developer productivity. Singer said the Portal enterprise team has been talking with large enterprises, including banks, where finance and procurement teams are definitely decision-makers.

“At Spotify, we got signals that a developer portal can 2x your improvement. But when you’re a bank and you have 30,000 developers, like 5%, 2% improvement, those are massive numbers, and that gets them really excited because they have so many developers,” he said. “We see lots of those signals coming in that large development organizations that are orders of magnitude larger than Spotify see the value proposition of moving forward with this.”

**Riding the Wave of Platform Engineering**
Platform engineering and internal developer portals are the next wave Singer and Aniszczyk witness crashing into the tech industry, making a pivotal change the way the cloud, Kubernetes and now AI have done.

Indeed, while it has a dominant market share, Backstage only being adopted by about 3,400 organizations didn’t sound like that much.

“What ends up happening is, if they do a homegrown version, it’s like a half-assed IDP — maybe they wrote their own service catalog,” Aniszczyk said, but it’s only a matter of time for these companies to adopt Backstage, too.

“In the early days of Kubernetes, people wrote their own little schedulers on top,” he said. “People will do homegrown things for a while, until there’s a better solution out there, which there is now.”

While Backstage was originally conceived as being for mid-size and large companies addressing complexity in the cloud, Singer said he is seeing a lot of adoption in startups as small as 50 engineers.

“You already see this pressure and the problem sets at smaller companies,” he said. “I think that is a reflection of the way that modern software is built — so componentized, so broken down, moving so fast — that small companies realize the value proposition as well. So I think that bodes well to the wave continuing to build.”

Add to this, in the age of AI, more code is being created than ever, faster.

“Using [Cursor AI](https://thenewstack.io/using-cursor-ai-as-part-of-your-development-workflow/), all these amazing things, you can create software super fast,” Singer said. “And that’s been one of the challenges at Spotify: we’re really good at creating software. We’ve got 90 million lines of code, or something like that, and so that creates complexity quickly.

“You see these companies. They’re going fast. They’re creating software. And then reuse already becomes a problem. And that becomes the boat anchor that weighs you down eventually.”

**In the Face of AI**
The emergence of [AI agents](https://thenewstack.io/ai-agents/) doesn’t rattle Singer. “The more you create code with these agentic IDEs,” he said, “the more likely it is to, one, get created fast, and two, be low quality.”

This makes platform engineering, IDP guardrails and visibility even more essential. Backstage works to reel the AI rush back in with features like Soundcheck and templating capabilities that should help standardize and maintain quality. With dashboard, [observability and monitoring](https://thenewstack.io/monitoring-vs-observability-whats-the-difference/) plugins, users can find and flag security violations when things don’t follow the chosen data ecosystem’s policies.

Perhaps Spotify’s biggest announcement at KubeCon Europe is the AiKA plugin for Portal. This “AI knowledge assistant” is an AI chatbot that was first integrated into Spotify’s internal Backstage instance, its IDE, [Slack](https://thenewstack.io/developer-guide-a-new-way-to-build-on-the-slack-platform/) and more. A [retrieval-augmented generation (RAG)-based](https://thenewstack.io/why-rag-is-essential-for-next-gen-ai-development/) chatbot, AiKA understands the organizational and data ecosystem, including referencing its source material.

Ever the dogfooding organization, Spotify is finding colleagues are eager to use AiKA even outside technical roles, with more than 1,000 employees using the chatbot daily.

AiKA should be released into alpha for existing Portal customers by the end of April. Check back at The New Stack to learn more about AiKA later this month.

[
YOUTUBE.COM/THENEWSTACK
Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.
](https://youtube.com/thenewstack?sub_confirmation=1)