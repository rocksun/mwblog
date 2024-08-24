# Building an IDP With Help From the Open Source CNOE Framework
![Featued image for: Building an IDP With Help From the Open Source CNOE Framework](https://cdn.thenewstack.io/media/2024/08/2a48fc20-building-an-idp-with-help-from-the-open-source-cnoe-framework-1024x576.jpg)
NEW YORK — How do you build an [internal developer platform](https://thenewstack.io/7-core-elements-of-an-internal-developer-platform/) for an organization that can expect massive online traffic surges on a regular basis and whose developers have grown used to lots of autonomy?

And how do you sort through the ever-growing pile of options to standardize your organization’s tooling?

Those are the questions facing the platform team at [The New York Times](https://thenewstack.io/new-eleventy-supports-esm-and-ny-times-embraces-react-18/), the more than 170-year-old bastion of global journalism. The once tradition-bound organization has [leaned hard into the digital world](https://thenewstack.io/a-candid-assessment-from-the-new-york-times-cto-with-serverless-and-the-1990s-in-mind/) in recent years, providing not just global news and thought leadership but also a heap of popular features: niche-interest newsletters, a cooking app, the Wirecutter consumer guide and, of course, [Wordle](https://thenewstack.io/programmers-explore-the-secrets-of-wordle/).

As the Times has created new environments, so have its roughly 1,000-strong developers and engineers. And that was becoming a problem.

During a presentation at [Kubernetes Day in New York](https://www.kcdnewyork.com/) in May, [Luke Philips](https://www.linkedin.com/in/lukephilips/), staff software engineer at the Times, described the situation that preceded the company’s journey to getting its own internal developer platform (IDP).

Like other organizations, Philips said, the Times had [lots of Kubernetes clusters](https://thenewstack.io/neglect-kubernetes-resource-management-at-your-peril/), with a chaotic variety of approaches to provisioning infrastructure and delivering and deploying code: [a mix of cloud native tools](https://thenewstack.io/how-to-tackle-tool-sprawl-before-it-becomes-tool-hell/), both single cluster and multicluster environments, developers responsible for the full life cycle of upgrades for their infrastructure, feature teams with embedded [DevOps/site reliability engineers](https://thenewstack.io/platform-engineering/sre-vs-devops-vs-platform-engineering/) managing their own clusters. And so on.

A lot of developers had their own clusters, Philips said, adding to the complexity.

About three years ago, the Times started a [platform engineering initiative](https://thenewstack.io/platform-engineering/), building what it came to call its delivery-shared engineering platform (DSP).

The project was shaped by the Times’ mission and unique needs as an organization, but also by a set of open source guidelines known as [Cloud Native Operational Excellence, or CNOE](https://cnoe.io/) (pronounced “KUH-noo,” like a small boat). This is the story of how the Times is building its DSP with the help of roughly 60 platform team members (which the organization calls its “delivery engineering” team).

It’s a work in progress, but early signs are promising, said Philips and his colleague, [Tiara Sykes](https://www.linkedin.com/in/tiara-sykes/), a Times software engineer who was also a presenter at Kubernetes Day in New York.

“We’re up to, I think, about 25% of the company workloads are in this managed IDP experience,” Philips told The New Stack. “And our goal is for everyone to get over there.”

## Getting Started With Platform Engineering
The Times’ mission, Philips said in the Kubernetes Day presentation, is “to build the essential subscription bundle for every English-speaking curious person who seeks to understand and engage with the world.”

To build its internal platform, the team driving the project needed to show curiosity about what its customers needed most.

“Your platform support is your starting point to get product engineers, product managers and other leadership on board to use it,” said Sykes during the presentation. “Some questions to guide and assess the support model could be, what does a platform developer or product developer want from a platform, and how will they feel supported as they develop new products?”

An ideal development workflow, she said, would let developers focus on the delivery of features, on writing high-quality code, “covering it with tests and implementing it with their bus patterns to keep the codebase maintainable.”

However, she noted, “That’s far from reality.” There’s infrastructure to build, and devs must store and deploy the artifacts from their code.

And once the code is deployed, she added, “there are still routing, DNS [monitoring and observability](https://thenewstack.io/monitoring-vs-observability-whats-the-difference/) — each of these tasks is huge on its own, requiring a lot of time, effort and knowledge, understanding security threats and best practices.”

The Times needed a [“golden path”](https://thenewstack.io/heres-one-golden-path-to-build-an-mvp-enterprise-idp/) for developers, a standardized set of self-service tools, with easy access to [documentation](https://thenewstack.io/poor-documentation-is-costly-heres-how-to-fix-it/), Sykes said. In addition, she said, it needed to provide “centralized code management and deployment pipelines, infrastructure to help run our systems in the cloud, and observability tooling to help teams understand and operate their systems.”

## What’s CNOE?
Parallel to the Times’ platform project, an open source effort to create guidelines for building IDPs gathered momentum. Last October, five companies — Adobe, [Amazon Web Services](https://aws.amazon.com/?utm_content=inline+mention), Autodesk, Salesforce and [Twilio](https://www.twilio.com/?utm_content=inline+mention) — [launched CNOE as a joint initiative](https://aws.amazon.com/blogs/opensource/cloud-native-operational-excellence-cnoe-a-joint-effort-to-share-internal-developer-platform-tools-and-best-practices/); Intuit and Nike have subsequently also signed on to support CNOE.

CNOE is a framework that aims to pool the best practices of enterprises that are on the same platform journey.

The framework, according to the project website, is designed to help organizations of similar scale “navigate their operational technology decisions together, de-risk their tooling bets, coordinate contribution, and offer guidance to large enterprises on which [sponsor_inline_mention slug="cncf" ]Cloud Native Computing Foundation[/sponsor_inline_mention] technologies to use together to achieve the best cloud efficiencies.”

Members of the Times’ delivery engineering team started attending CNOE community meetings. “We just kind of started to listen and learn,” Philips said. As they began building their own project, the team members were able to “tap into the brainpower of these other engineers out there. We don’t have to go hire all those engineers who work for us — we can share collaborative learning from each other’s experiences

The CNOE project includes templates for some of the most common tasks involved in platform engineering, including an [IDP builder](https://github.com/cnoe-io/idpbuilder) — pre-released and still under active development. The tool can help users spin up an IDP using [Kubernetes](https://thenewstack.io/streamline-platform-engineering-with-kubernetes/), [Argo](https://thenewstack.io/gitops-on-kubernetes-deciding-between-argo-cd-and-flux/) and [Backstage](https://thenewstack.io/spotifys-backstage-a-strategic-guide/) (the internal developer portal template created by Spotify engineers), with only [Docker](https://www.docker.com/?utm_content=inline+mention) required as a dependency.

Another repo, [“cnoe-cli,”](https://github.com/cnoe-io/cnoe-cli) Philips told the Kubernetes Day audience, will help create Backstage’s scaffolding [custom resource definitions (CRDs)](https://thenewstack.io/kubernetes-crds-what-they-are-and-why-they-are-useful/) for a user’s own CRDs. The GitHub project also includes repos for the [Backstage plugins for Argo workflows](https://github.com/cnoe-io/plugin-argo-workflows) used by CNOE stack, for [Backstage images used by the stacks](https://github.com/cnoe-io/backstage-app) and for the [reference implementation of CNOE and its toolings on AWS cloud](https://github.com/cnoe-io/reference-implementation-aws).

The CNOE website also includes [“technology radars,”](https://cnoe.io/radars) visualizations of data from community members about various tools they’re using for different tasks — such as service mesh or CI/CD pipelines — and where each tool currently lands on the assess-trial-adopt continuum.

## Getting Started on an Internal Platform
The core of the Times’ DSP is a centrally operated and managed set of Kubernetes clusters, for development, staging and production.

“Teams and developers no longer have to maintain their own infrastructure,” Philips said in the Kubernetes Day presentation.

He added, “We offer distinct multitenant spaces within the clusters. Each team’s operations are separate from each other with our backend security controls.”

Here’s a simplified look at the DSP’s Kubernetes clusters:

The DSP needed to provide certain capabilities to function seamlessly as a self-service platform for the Times’ developers. Here’s what was needed:

“We began to build our platform piece by piece together, bringing to bear the best-of-class CNCF and open source projects, Kubernetes as our base compute platform and a related dedicated team,” Philips said in his presentation.

“Along with Kubernetes, you want to add a declarative configuration management tool, following GitOps best practices and add Argo CD, as well as another dedicated team for application delivery. Finally, we wanted to add a developer portal —Backstage seemed like the right choice — as well as another dedicated team.”

Here’s a visualization from CNOE, used by Philips and Sykes in their presentation, that shows that project’s suggested tooling options.

In her presentation, Sykes referred to this visualization as a “suite of technologies that were chosen because of how seamlessly they work together. And this subset hopefully takes away that pain point of having misplaced bets.

## What the Platform Team Learned
Philips and Sykes shared the lessons they’ve learned from the project.

First among them: It pays to be a good listener. Tool choices will sometimes need to be reconsidered as the platform scales; even within an organization, some tools won’t fit every use case.

The goal when serving developers, Philips told The New Stack is “not to just tell them this is the way it must be, but understanding what they are doing. And if it’s not the tool they’re used to, how do we reach them?”

The Times’ internal platform project remains a work in progress. Various parts of the organization need to scale rapidly at particular times of the year — for instance, the Cooking app sees its heaviest traffic around Thanksgiving. The news division will get a surge in readers leading up to the U.S. presidential election.

“So we’ve done our conversion for the news, we got things ready for where we want to be for November and we wait for that to happen,” Philips told The New Stack. Next, “we’ll work on other things, and other migrations with a different kind of impact can come over.”

He advised organizations that seek to emulate the Times’ effort to move step-wise and handle all the details before moving into production: “There’s a lot of glue in between, like all of your security hardening and multitenancy and all that.”

Philips acknowledged, “We’ve kind of been in the weeds doing the hard security stuff. And our developer experience is a little rough.”

But with 25% of workloads already moved to the DSP, he remains bullish on the prospects for more adoption.

During the presentation, an audience member asked how to persuade developers who are used to managing their own Kubernetes cluster to move to a shared one.

“You just give them the pager,” Philips said. “At 2 a.m., do you want to run this? That’s the right balance of motivation. Can you run this —versus someone, or a group of people, that might optimize it?

He posed the question at the heart of developer productivity: “What is the best way for you to spend the next hour of your time?”

## What’s Next for CNOE?
In the Kubernetes Day presentation, Sykes recommended that organizations seeking to build their own shared, self-service development platforms check out CNOE and its [online roadmap of capabilities](https://cnoe.io/docs/category/technology-capabilities).

“You can learn more about these capabilities in detail, heed their best practices that they recommend as well as some demos, templated out examples,” she said.

Sykes also recommended checking out the project’s bi-weekly community meetings and the CNCF Slack channel devoted to the project: “One of the greatest ways you can also contribute is looking at filing issues on GitHub that relate to how you operate your IDP.”

Overall, CNOE is a blueprint for building an internal platform, but not a one-size-fits-all solution, Sykes told the Kubernetes Day audience.

“Your platform will depend on your product engineers’ needs as well as your business needs,” she said. CNOE, she added, is “a great starting point” for a team’s initial conversations about building its IDP.

“That way, you’re not going down the windy road of encountering problems. Try to figure out a solution from there that provides a holistic overview. Get your GPS navigations on track before you start the journey.”

[
YOUTUBE.COM/THENEWSTACK
Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.
](https://youtube.com/thenewstack?sub_confirmation=1)