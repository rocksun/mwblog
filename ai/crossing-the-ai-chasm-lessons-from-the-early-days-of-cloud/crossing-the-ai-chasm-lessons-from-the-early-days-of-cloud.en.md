AI is surely one of the most transformative technologies of the last 50 years, touching all aspects of the IT stack from top to bottom. Although we are still early days in the hype cycle, we are witnessing broad adoption and some early wins.

OpenAI and others have had incredible [growth](https://www.cnbc.com/2025/08/04/openai-chatgpt-700-million-users.html), largely due to adoption by white collar knowledge workers in areas such as development and marketing. However, enterprises are struggling to adopt AI agents for business-specific use cases, [with failure rates as high as 95%](https://fortune.com/2025/08/18/mit-report-95-percent-generative-ai-pilots-at-companies-failing-cfo/), according to MIT.

While new “AI native” startups are putting AI and agentic workflows to work, enterprises are still trying to cross the chasm. This reminds me of the early challenges in adoption of cloud computing services.

## The Rise of Early Cloud Adoption and AWS EC2

In the earliest days of cloud computing we spent a massive amount of time trying to determine what the new architecture meant. “Cloud native” as an architectural pattern hadn’t really come of age in 2009 and 2010, about two years into the [AWS](https://aws.amazon.com/?utm_content=inline+mention) EC2 experience. Many of the early “clouderati” were [experimenting actively with](https://cloudscaling.com/blog/cloud-computing/cloud-innovators-netflix-strategy-reflects-google-philosophy/) and helping to [define this architectural pattern](https://www.slideshare.net/slideshow/pets-vs-cattle-the-elastic-cloud-story/31735707).

We saw the same pattern at the time, with enterprises struggling to understand the new architecture and initially trying to lift and shift “brownfield” workloads directly to the cloud, rather than re-factoring, re-platforming or re-architecting them. Their early successes were largely with new greenfield applications.

Crossing the chasm took some time and although EC2 removed its beta label in 2008, it was really more like 2015 before there was significant and broad enterprise adoption.

I expect we will see a similar pattern with crossing the AI chasm.

## How the Enterprise Adopts New Technologies

Large enterprises are rarely the first to adopt new technologies. Many of the challenges are structural, such as adding new vendors into procurement systems. Some are due to a talent gap, where high tech companies have sucked a lot of the oxygen out of the room in terms of the labor pool. Other issues include risk aversion, a lack of understanding new architectural changes, security and compliance gaps, and a need for packaged solutions. This is why SaaS has been so wildly successful across enterprises. It lifts and shifts entire sets of back-office solutions outside of the business and makes them someone else’s problem, so enterprises can ride the innovation curve of others.

## How the Enterprise Will Adopt AI

While there are parallels to the adoption of cloud native computing architectures, there are also some interesting differences that will affect enterprise adoption. First, because AI can be applied anywhere, it is easily applied to brownfield applications and work. This is why we see so many development, marketing and sales teams simply integrating AI into existing workflows. This usually is dealing with non-sensitive data that can be sent beyond the four walls of the business with the right contractual guarantees.

This brings us to the second point, which is that, like cloud native apps, there is a strong need for net-new greenfield applications that are AI native and agentic. Early enterprise cloud adoption was largely new greenfield applications that brought an immediate benefit to the business and increased their competitiveness. For AI, this is a no-brainer, yet most of these use cases will require access to highly sensitive data. A healthcare business, for example, will want to use its exhaustive hoard of patient data and apply AI agents to electronic healthcare records (EHR). The risk of data leakage if the EHR is sent outside the organization is unacceptable for most healthcare companies.

The upshot is that enterprises will adopt AI via the existing low-hanging fruit. But the biggest value to the enterprise will come with successfully crossing the chasm on agentic AI applications tied closer to the highest sensitivity data. Adoption of these agentic AI applications will be slow – and early failure rates will be high – largely because we don’t know yet what the right patterns are. “AI native” right now is ill-defined. We are all collectively on a mission to solve this.

## What We Know About AI-Native Today

So what is [AI native](https://thenewstack.io/what-is-an-ai-native-developer/) about? While much is unclear, we do know some things right away. [Model Context Protocol (MCP)](https://thenewstack.io/model-context-protocol-a-primer-for-the-developers/) is already the lingua franca for agentic workflows, much like [REST](https://thenewstack.io/rest-vs-graphql-solving-api-challenges-in-modern-data-transfers/) became the lingua franca of the web. We know that agents are good at what they do and that regular old discrete non-agentic code still has a place. Meaning that agents, by definition, rely on [large language models (LLMs)](https://thenewstack.io/7-guiding-principles-for-working-with-llms/)  for their non-deterministic “business logic,” while regular code gives us deterministic procedural execution. We call these “tools” now in the new AI lingo and MCP is the de facto standard that glues it all together.

We know that AI native apps are largely cloud native apps as well. They have the same attributes, the scale-out nature and the need to handle drift detection, etc. Most will probably run on [Kubernetes for this reason and all the deployments](https://thenewstack.io/a-look-at-kubernetes-deployment/) I see today reinforce this notion. AI native appears to be an evolution of cloud native.

We also know that the testing of AI-powered applications, because of their non-deterministic business logic, will be particularly tricky. In the past, you might roll out a new feature or fix a bug, then run a standard test suite against your app or website to make sure key metrics were still achieved. Much of what needs to be tested for regressions in agentic AI apps are things like accuracy and hallucinations, which we haven’t needed to worry about before. This is where “[evaluations](https://www.ibm.com/think/topics/ai-agent-evaluation)” come in.

Observability of AI-powered applications will also be tricky. Most larger scale multiagent workflows will have several agents in the path, each calling one or more LLMs, possibly for different purposes. Instrumenting all of that and being able to perform root cause analysis to troubleshoot issues will be particularly challenging.

Lastly, we know that AI native ultimately has to have robust guardrails, and new solutions to their unique security and data privacy challenges. Right now, much of the security practices are an afterthought, but for broad enterprise adoption, we will have to go back to the drawing board and bring new thinking to the way we solve data leakage, hallucinations, data access, transitive identity and much more.

## Crossing the AI Chasm

As with cloud native, enterprises will need help with crossing the chasm. They need well understood patterns, open solutions, education on MCP and agentic workflows, strong security and data privacy tools. Most importantly, they need the brave early adopters who will work on real-world agentic solutions to learn from these efforts. In my mind that means three clear things:

* Enable internal developers with a “bottoms up” approach,just as Netflix did when adopting AWS and pioneering “cloud.native.”
* Partnering with the companies and thought leaders at the bleeding edge of agentic AI apps.
* Willingness to learn, frequently through bold moves, accepting risk and embracing failures.

Once again, we are at the crossroads and those we adopt early will gain a competitive advantage over those who do not. “Adapt or die” are once again key words to live by in our ever-changing world of technology.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://cdn.thenewstack.io/media/2024/10/79390449-cropped-2934c701-randy-bias-head-shot.jpg)

Randy Bias is a pioneering advocate for cloud, DevOps, and open source technology, recognized for driving successful open sourcing efforts in enterprises of all sizes and significantly influencing the industry’s transition from proprietary models. He has played a critical role...

Read more from Randy Bias](https://thenewstack.io/author/randy-bias1/)