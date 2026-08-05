Cloud platform company [Nscale](https://www.nscale.com/) announced this week a definitive agreement to acquire AI workload scaling specialist [Anyscale](https://www.anyscale.com/), in a move that signals a new test of whether cloud-neutral AI software can stay neutral once it is paired with a GPU neocloud.

The purchase coalesces Nscale’s infrastructure capabilities, which span control systems that oversee GPUs, datacenters, power consumption, and the application layer where AI services themselves are executed, with [Anyscale’s software layer](https://thenewstack.io/anyscale-new-optimized-runtime-for-ray-kubernetes-operator/) for scaling AI workloads across data processing, training, inference, and reinforcement learning.

Argued by Nscale to be the coming together of “[two highly complementary companies](https://www.nscale.com/press-releases/nscale-acquires-anyscale)”, Nscale scooping up Anyscale could be a fundamental change in the resulting business model.

## Is this the start of GPU neocloud lock-in?

It’s important to remember that [Nscale is a GPU neocloud](https://www.reuters.com/business/ai-cloud-provider-nscale-buy-software-startup-anyscale-2026-07-30/) (a specialized cloud provider running bare-metal GPUs and infrastructure optimized for AI and machine learning workloads), meaning that it runs its own GPU-rich datacenters and its own software ​stack. At the same time, Anyscale is an independent cloud-neutral software orchestration multi-cloud control plane that works with any cloud hyperscaler… but now owned by a single neocloud.

That doesn’t sound quite so much like [cloud-neutrality](https://thenewstack.io/the-next-stages-of-ai-conformance-in-the-cloud-native-open-source-world/) and agnosticism; it sounds more like a vertically integrated AI cloud provider proposition.

Chief product officer at Nscale, [Dan Bathurst](https://www.linkedin.com/in/danielbathurst/), tells *The New Stack* that the Anyscale platform “continues to be its own brand and product,” and that includes working with bring-your-own-cloud deployments on AWS, GCP, Azure, and the other clouds.

> “Where we want to win is on performance, not on any sort of vendor lock-in or forcing of someone to choose Nscale as the infrastructure provider.”

“But what really changes — or how it’s changing — is that customers now also get this first-party option, where they can have Anyscale running on Nscale fleet as a full-stack, highly-optimized solution. Where we want to win is on performance, not on any sort of vendor lock-in or forcing of someone to choose Nscale as the infrastructure provider,” Bathurst says.

He insists that it is in Nscale’s interest to ensure that it is making it easy for software engineering teams to get the outcomes they want with the workloads that they’re trying to run.

“For us, the existing commitments will carry forward, so Anyscale’s value really is meeting instances where the compute already lives,” he says. “Where we want to win is on performance, not on any sort of vendor lock-in or forcing of someone to choose Anyscale as the infrastructure provider.”

## Neutrality on the platform layer, differentiation on the infrastructure layer

Bathurst invites users to think of it as “neutrality on the platform layer, but differentiation on the infrastructure layer” because the combination of the two organizations is a full-stack play.

“The differentiation comes from the fact that Nscale is fully vertically integrated with Anyscale. Therefore, if users want that first-party option, they can choose Anyscale and get the most optimized solution because, obviously, we’re designing, optimizing, and co-engineering every layer of that stack from power to the datacenter through to the application. It’s quite a unique proposition, but it’s not something we are going to force upon any customer,” confirms Bathurst.

Not everyone is convinced by the company’s pledge to maintain an agnostic and neutral open house. [Sanjeev Mohan](https://www.linkedin.com/in/sanjmo/), principal analyst, SanjMo and former Gartner research VP for data and analytics, tells *The New Stack* that Anyscale “stops being a neutral player” the moment its best features and most optimal pricing land on Nscale first.

> “The software will still run anywhere, but ‘runs anywhere’ and ‘runs best somewhere’ are different things, and buyers will feel the gap in performance and cost. At that point, neutrality is a label.”

## Runs anywhere, but… runs best somewhere

“The software will still run anywhere, but ‘runs anywhere’ and ‘runs best somewhere’ are different things, and buyers will feel the gap in performance and cost. At that point, neutrality is a label,” says Mohan.

He agrees that integrating software and compute will produce measurable cost, performance and reliability gains. Defining this as “the strongest part of the deal”, Mohan explains that with Nscale controlling both the silicon and Anyscale’s control plane, it can tune scheduling, memory, and networking together in ways the compute-neutral Anyscale never could.

## Anyscale commercial support for Ray

Anyscale was founded by the creators of [Ray](https://www.anyscale.com/product/open-source/ray?utm_source=the%20new%20stack&utm_medium=referral&utm_content=inline-mention&utm_campaign=tns%20platform), an open source project that provides a distributed computing framework designed to scale Python workloads across any infrastructure into live production application jobs and services.

[Ray was donated to the PyTorch Foundation](https://thenewstack.io/ray-comes-to-the-pytorch-foundation/) in 2025. Anyscale continues to provide its commercially supported services for Ray, which include a “no DevOps” route to 100% managed cloud infrastructure and serverless autoscaling, making it simpler to create, deploy, and monitor machine learning workflows in production.

Anyscale supports data processing, model training, batch inference, and LLMs across public and private cloud environments. As open source as this all feels, are we still edging towards narrower proprietary channels, or the possible threat of deeper application and data service dependencies that developers will ultimately have to wrangle around?

“I don’t think so, primarily because the way that the platform works, it’s designed to orchestrate across various different clouds and different infrastructure. It’s like a heterogeneous distributed compute platform. So the platform’s always gonna remain multi-cloud,” confirms Nscale’s Bathurst.

## Pricing permutations and hyperscalers hearsay

Pressed on any forthcoming pricing changes or likely reactions from the major cloud hyperscalers in relation to Nscale now being a credible alternative, Bathurst and team were (perhaps understandably one day after an acquisition deal announcement) politely tight-lipped.

More voluble is always-affable analyst Mohan, who says that, “Every optimization that only shows up on Nscale hardware is a dependency. So, an argument can be made either way. Standalone orchestration software and independent tooling vendors are getting absorbed into whoever owns the GPUs, because the economics only work when you control both. Expect more of it,” Mohan underlines.

He explains that Nscale “now becomes a real specialist cloud services provider alternative,” i.e., not a general-purpose one like AWS, Azure and Google Cloud with their plethora of managed services, from databases and data warehousing to container orchestration through to AI/ML pipeline technology.  However, he does see space for Nscale to become a strong player in raw training and inference at scale.

## From cryptocurrency to cloud contender

London, UK-based Nscale was established in 2024 from what was originally a cryptocurrency mining business.

As suggested, Anyscale will retain its brand name as part of the Nscale family, and the company has restated its stance that customers are “free to choose the cloud infrastructure on which they run their AI workloads” today.

The company’s initial press statement said that “over time” users will gain the additional option of running the Anyscale software layer on Nscale’s full-stack AI platform.

## The first full-stack AI hyperscaler?

“Companies are moving beyond simply using AI to actually building their own. Doing that well requires the software and the infrastructure it runs on to be designed together,” says [Keerti Melkote](https://www.linkedin.com/in/keertimelkote/), CEO of Anyscale in the press release announcing the acquisition.

Melkote has defined the combination of Anyscale’s platform — built on Ray — with Nscale’s datacenter, compute and AI cloud services as the “first full-stack AI hyperscaler,” i.e., one that runs any AI workload at greater scale, so more software engineering teams can build and own their AI applications and services.

With this acquisition and the fusion of Nscale with Anyscale’s software layer, the organization will aim to widen its customer base. Existing work sees the company working in verticals from healthcare to e-commerce to robotics. It says its full stack offering will help companies speed up image and document processing, fine-tune LLMs on their proprietary data, and deploy AI agents in-house using open-source models.

The transaction is subject to closing conditions and regulatory approvals and is expected to close in the second half of 2026. Financial terms of the transaction were not disclosed, although [Reuters reports](https://www.bloomberg.com/news/articles/2026-07-30/nscale-to-buy-ai-software-startup-anyscale-for-1-65-billion?accessToken=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzb3VyY2UiOiJTdWJzY3JpYmVyR2lmdGVkQXJ0aWNsZSIsImlhdCI6MTc4NTQxMDIyNywiZXhwIjoxNzg2MDE1MDI3LCJhcnRpY2xlSWQiOiJUSVhaU0hLSkg2VkUwMCIsImJjb25uZWN0SWQiOiJEQ0FGMjNFM0YyMkE0Qzk5OTM0RUMyRDEwNkM0ODc0NyJ9.1hChskM6Twv1RarQXZnJwXh8vZCjp_93Gr18w86cZ1I&leadSource=article-gifting) a source stating that the deal price is “about $1.65 billion”, according to a person familiar with the deal.

AWS, Google Cloud and Microsoft Azure representatives were all contacted and invited to comment on this story.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://cdn.thenewstack.io/media/2026/02/684dae45-cropped-e991646b-06_rpa_inline_01_bridgwater-1-1-300x234-1.jpg)

Adrian Bridgwater is a technology journalist with three decades of press experience. He has an extensive background in communications, starting in print media, newspapers and also television. Primarily working as an analysis writer dedicated to a software application development ‘beat’,...

Read more from Adrian Bridgwater](https://thenewstack.io/author/adrian-bridgwater/)