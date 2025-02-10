# The Metamorphosis of Open Source: An Industry in Transition
![Featued image for: The Metamorphosis of Open Source: An Industry in Transition](https://cdn.thenewstack.io/media/2025/02/96724193-pawel-czerwinski-hu6kulsi5dm-unsplash-1024x683.jpg)
[Pawel Czerwinski](https://unsplash.com/@pawel_czerwinski?utm_content=creditCopyText&utm_medium=referral&utm_source=unsplash)on
[Unsplash](https://unsplash.com/photos/blue-and-pink-painting-Hu6kULsI5dM?utm_content=creditCopyText&utm_medium=referral&utm_source=unsplash)
Twenty years ago, declaring your project “open source” was a statement of principle, philosophy, and community. Today, it’s more likely to be a business decision, a marketing strategy, or a talent acquisition tool. This shift is not a failure of open source; it’s a sign of its success.

The numbers don’t lie:[ GitHub’s 2024 Octoverse report](https://github.blog/news-insights/octoverse/octoverse-2024/#the-state-of-open-source) found that developers made nearly 1 billion contributions to open source and public repositories this year, more devs than ever are consuming open source packages, and the number of first-time contributors continues to grow.

According to many surveys and reports, including[ contributions from the OSI,](https://opensource.org/blog/announcing-the-2024-state-of-open-source-report) we are reasonably sure that more than 90% of companies worldwide are using open source and even have at least one open source component in their codebases. And those numbers are growing.

Open source won.

## From Revolution to Convention
The [open source movement](https://thenewstack.io/open-source-movement-emerging-in-ai-to-counter-greed/) began as a pragmatic response to free software ideology. While the[ Free Software Foundation](https://www.fsf.org/) emphasized ethical imperatives (*“promote computer user freedom”*), open source focused on practical benefits: unlimited collaboration, permissionless innovation, and broader adoption. This strategic shift worked remarkably well. [Open source became the default choice for infrastructure software](https://thenewstack.io/is-community-backed-open-source-software-worth-the-risk/), developer tools, and critical business applications.

But success brought its challenges.

## The Cloud Changed Everything
When open source was first conceptualized, software typically ran on-premise. The rise of cloud computing fundamentally changed this landscape. Suddenly, the ability to modify and redistribute code became less important than the ability to run and operate it at scale.

A prime example of this metamorphosis is the journey of Elastic. By 2019, Amazon’s Elasticsearch service was generating more revenue than Elastic itself, even though Elastic was the primary maintainer of the Elasticsearch codebase. This led to a[ well-known conflict](https://www.nytimes.com/2019/12/15/technology/amazon-aws-cloud-competition.html): Amazon forked Elasticsearch after Elastic changed its license, creating OpenSearch. This case exemplified the fight between cloud providers and[ single-vendor open source projects](https://opensource.net/why-single-vendor-is-the-new-proprietary/), leading to fundamental questions about the sustainability of open source business models in the cloud era.

This wasn’t the first time [open source companies sought to protect their interests from cloud](https://thenewstack.io/what-do-cloud-native-and-kubernetes-even-mean/) providers. Before that, new licensing approaches were emerging. MariaDB created the [Business Source License (BSL)](https://mariadb.com/bsl-faq-adopting/) in 2016, pioneering a time-delayed open source conversion model in which code becomes fully open source (typically under the GPL v2.0 or compatible) after a certain period. This middle ground between proprietary and [open source models](https://thenewstack.io/large-language-models-open-source-llms-in-2023/) has been called source available, to distinguish it from open source.

Similar concerns led MongoDB to create the [Server Side Public License (SSPL)](https://opensource.org/blog/the-sspl-is-not-an-open-source-license) in 2018, followed by Redis’s licensing changes. These companies sought to address their challenges with cloud providers. While[ not approved by OSI](https://opensource.org/licenses), the SSPL represented another attempt to balance commercial viability with open-source principles.

To everyone’s surprise, Elastic[ returned to open source](https://www.elastic.co/blog/elasticsearch-is-open-source-again) a few months ago, adopting the AGPL as an optional license for Elasticsearch. This proves that a SaaS business is possible with open source.

## The Corporate Influence
The enterprise open source landscape has evolved dramatically. What began as cautious participation has evolved into strategic investment and leadership. Consider these facts:

- Google’s
[Kubernetes has become the de facto standard for container](https://thenewstack.io/kubernetes-gets-back-to-scaling-with-virtual-clusters/)orchestration, with thousands of contributors from hundreds of companies. - Meta’s React/Vercel’s Next.js dominate frontend development, used by millions of developers and powering millions of websites.
- Microsoft’s VS Code has won a significant market share with its
[open source core.](https://thenewstack.io/the-future-of-open-source-or-why-open-core-is-dead/) - Intel, Red Hat, Oracle, Google, and other big corporations employ
[most Linux kernel developers](https://kernelnewbies.org/DevelopmentStatistics). - Google’s Chrome team drives the development of V8, the JavaScript engine that powers Node.js.
- Microsoft and Google are the
[most significant contributors](https://opensourceindex.io/)to open source projects on GitHub.
And the governance of open source is fundamentally foundation-based. The Linux Foundation[ hosts over 800 projects](https://www.linuxfoundation.org/resources/case-studies) with millions in annual funding, the Eclipse Foundation[ hosts more than 400 projects](https://projects.eclipse.org/), currently[ 296 projects and other initiatives](https://projects.apache.org/) are managed by the Apache Software Foundation, not to mention dozens of projects hosted or supported by the[ Python Software Foundation](https://www.python.org/psf-landing/), the[ OpenInfra Foundation](https://openinfra.dev/), the[ OpenJS Foundation](https://openjsf.org/), and others, and the[ Cloud Native Computing Foundation](https://www.cncf.io/) also manages millions in funding and organizes the biggest conferences in the open source space. Again, major companies like Google, Microsoft, and Amazon collectively contribute hundreds of millions to [open source foundations](https://thenewstack.io/nivenly-foundation-seeks-equity-for-open-source-maintainers/).

This corporate involvement has brought unprecedented resources and stability to many projects, but it’s also changing the power dynamics in the ecosystem. Decisions are often made in corporate boardrooms rather than in community forums. While this has professionalized project management and[ improved security practices](https://openssf.org/), it has also raised concerns about the independence of open source development.

Corporate involvement has also led to significant challenges. Oracle’s acquisition of Sun Microsystems led to concerns about the future of Java and MySQL’s future, ultimately leading its creator Michael “Monty” Widenius, to launch [MariaDB as a community fork](https://mariadb.org/en/). Docker’s struggles with monetization led to the [sale of its enterprise business](https://thenewstack.io/mirantis-acquires-docker-enterprise/) and dramatic changes to Docker Hub’s pricing model. More recently, HashiCorp’s [switch from Terraform to BSL](https://thenewstack.io/hashicorp-abandons-open-source-for-business-source-license/) led to the creation of OpenTofu, highlighting how corporate decisions can fragment communities.

Despite these challenges, corporate involvement remains essential to [open source sustainability](https://thenewstack.io/can-open-source-sustain-itself-without-losing-its-soul/). The key is to establish governance models that balance corporate resources with community interests, as demonstrated by the positive examples that we listed.

## The Quest for Sustainable Funding
The sustainability crisis in open source has sparked various funding experiments. Traditional models like corporate sponsorship and donations have proven insufficient for many projects, leading to new approaches:

- GitHub Sponsors transformed individual funding by enabling direct support of maintainers. Notable success stories include
[Evan You](https://github.com/sponsors/yyx990803)of Vue.js, with his sponsorship tiers offering various benefits to supporters, and[Sindre Sorhus](https://github.com/sponsors/sindresorhus), maintaining hundreds of npm packages through community support - Open Collective pioneered transparent fiscal hosting, managing millions in funds for projects. For instance,
[webpack](https://opencollective.com/webpack)has raised over $1.5 million, with a current balance of approximately $79,000, all tracked transparently on their Open Collective page - Tidelift introduced a
[subscription-based model](https://tidelift.com/)where organizations pay for maintenance guarantees across multiple dependencies. This approach has helped sustain lesser-known but critical infrastructure projects.
However, these models aren’t perfect. Many critical projects still struggle to secure stable funding. The[ Log4j incident](https://www.csoonline.com/article/404962/log4j-one-year-later-the-log4shell-vulnerability-still-has-lessons-to-teach.html) highlighted how even widely used projects can be severely underfunded and maintained by volunteers despite being essential to global infrastructure.

This funding gap has led some projects to explore hybrid models, combining:

- Commercial services and support
- Premium features under different licenses
- Development contracts with major users
- Grant programs from tech giants and foundations
Finding funding mechanisms that preserve project independence while ensuring sustainable development is challenging. The industry needs new models to support high-profile projects and the long tail of more minor but crucial dependencies.

## The AI Licensing Dilemma
The rise of artificial intelligence has introduced a new topic to the open source conversation. Unlike traditional software, AI systems include both code and models, data, and training methods, [creating complexities that existing open source](https://thenewstack.io/how-american-express-created-an-open-source-program-office/) licenses were not designed to address. Recognizing this gap, the OSI launched the [Open Source AI Definition (OSAID)](https://opensource.org/ai/open-source-ai-definition) in 2024, marking a pivotal moment in the evolution of open source principles. OSAID v1.0 defines the essential freedoms for AI systems: the rights to use, study, modify, and share AI technologies without restriction. This framework aims to ensure that [AI systems labeled as “open source”](https://thenewstack.io/a-nue-ux-web-framework-plus-anthropic-openai-boost-ai-apis/) align with the core values of transparency and collaboration underpinning the movement.

However, the journey has not been without challenges. The OSI’s definition has sparked debates, particularly around the [legal ambiguities of model weights and data licensing](https://thenewstack.io/osis-definition-of-open-source-ai-raises-critical-legal-concerns-for-developers-and-businesses/). For instance, while OSAID emphasizes transparency in data sources and methodologies, it does not resolve whether [model weights derived from unlicensed data](https://thenewstack.io/data-modeling-part-2-method-for-time-series-databases/) can be freely shared or used commercially. This has left businesses and developers navigating a gray area, where the practical adoption of open source AI models requires careful legal scrutiny.

Despite these challenges, this effort underscores the adaptability of open source principles. It proves that they can evolve to meet the demands of emerging technologies while preserving their core values, as they have in the past.

So, what comes next?

The transformation of open source is already visible through several clear trends:

- Rise of
*source-available*licenses and hybrid models, from BSL to Elastic approach. - Increasing corporate guidance on significant projects, balanced with foundations.
- The ongoing search for sustainable funding, with experiments like GitHub Sponsors or Open Collective.
- AI-driven
[development tools](https://thenewstack.io/tiddlywiki-an-open-source-alternative-to-notion-or-obsidian/)and models introduce new questions about the meaning of “open source” itself.
We are moving toward a new model that transcends the traditional [definition of open source](https://thenewstack.io/the-open-source-ai-definition-what-the-critics-say/). The stories we’ve seen suggest that the future lies in more explicit value exchanges between stakeholders. We will likely see more tiered licensing systems and hybrid models that balance commercial interests with community benefits.

I also see the need for a new funding mechanism beyond donations and corporate sponsorship. First, corporate funding means corporate involvement, directly or indirectly, which doesn’t guarantee the freedom or independence of [open source maintainers](https://thenewstack.io/security-needs-create-more-work-for-open-source-maintainers/). Second, it does not guarantee the financial stability needed to succeed or maintain a project in the long term. We have recently witnessed the[ potential disaster](https://www.sonatype.com/blog/cve-2024-3094-the-targeted-backdoor-supply-chain-attack-against-xz-and-liblzma) of unmaintained OSS.

## Evolution, Not Death
This doesn’t mean we are about to witness the death of open source, but rather its evolution. Just as open source emerged from *free software* as a more pragmatic approach, new models are emerging to address today’s challenges. The principles of collaboration, transparency, and shared innovation remain valuable. Still, their implementation adapts to a changed technology landscape, and the definition itself could even live outside the [Open Source Initiative](https://thenewstack.io/open-source/).

I could even say the next phase might not be called “open source”! The question isn’t whether this model will survive but how it will transform to meet the needs of a changed industry.

The real challenge for the community is ensuring that this evolution preserves open source’s core benefits while adapting to new realities. We need to be active participants in shaping this future, not just observers of the change. The next chapter of open source will be written by those who can successfully navigate these challenges while staying true to the fundamental values that made it revolutionary in the first place.

[
YOUTUBE.COM/THENEWSTACK
Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.
](https://youtube.com/thenewstack?sub_confirmation=1)