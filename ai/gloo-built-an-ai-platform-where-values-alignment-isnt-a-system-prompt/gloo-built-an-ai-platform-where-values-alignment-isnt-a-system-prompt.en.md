AI models have gotten a lot better at avoiding hallucinations, and the frontier labs tend to put strict guardrails around their services to avoid harmful content. But for faith-based organizations, that is not always enough. They want models that [align](https://thenewstack.io/ai-alignment-in-practice-what-it-means-and-how-to-get-it/) directly with their values.

This is the target audience for [Gloo](https://gloo.com/). On Thursday, the company announced [Gloo AI Studio](https://studio.ai.gloo.com/). The company calls this “a production-grade AI development platform for faith-based and mission-driven developers” that embeds values alignment and governance directly into the infrastructure layer.

Instead of relying on default system prompts and ad hoc content policies, Gloo AI Studio applies a configurable harness around every model call. And since it’s model-agnostic, it can do this for models from OpenAI, Anthropic, and Google, as well as for open-source models.

This has always been part of Gloo’s mission and roadmap, Steele Billings, the president of Gloo AI, says in an interview with *The New Stack*.

“We built Gloo AI Studio so governance and values alignment are foundational, not optional,” he says. Like many businesses, churches, nonprofits, and faith-based universities want to use AI and offer services based on large language models, but those models have to be aligned with their values.

To some degree, that’s also true for any secular enterprise, and in our conversation, Billings hinted that Gloo was also working with some large enterprises that, just like faith-based organizations, are looking for technologies to ensure that their chatbots, for example, stay on track.

![](https://cdn.thenewstack.io/media/2026/03/2b0ff677-dashboard.png)

Gloo AI Studio dashboard (credit: Gloo).

## AI Studio

For developers, using Gloo Studio isn’t all that different from using Google AI Studio or a similar platform. At its core, after all, Gloo AI Studio is a multi-model AI gateway with similar core components to what you’d find from other AI startups or a hyperscaler.

What is different, of course, is that Gloo puts its own guardrails around these models (and allows its users to modify those as necessary). But to call those models on Gloo is no different from using any other platform.

The challenge for Gloo is adding the alignment harness while keeping the overhead to a minimum. “Our job is to be as small of a bump in latency as we possibly can be, while still providing things like grounding and the harnessing that lead to the values-aligned outputs that we’re measuring,” Billings says.

The platform also supports model routing, dynamically selecting the appropriate model per request while maintaining consistent policy controls.

The organizations Gloo works with want to bring their own data to these models as well, of course. Gloo AI Studio uses retrieval augmented generation (RAG) for this as the core technology, allowing a church, for example, to upload doctrinal texts, or a university to upload a curriculum and articles. Gloo manages the data enrichment, vector embeddings, grounding, and live syncing with external content sources.

![](https://cdn.thenewstack.io/media/2026/03/549fdc2a-explore-models.png)

Model choice on Gloo AI Studio (credit: Gloo).

Developers can manage all of this through Gloo’s API, but there is also the Studio interface itself. That’s where developers can manage their API keys and find starter recipes. There is also a playground for side-by-side model comparison. The playground lets developers toggle between denominational perspectives (currently Catholic, Evangelical, and Mainline Protestant) and see how the same prompt will offer different responses.

Nick Skytland, vice president of Gloo Developers and AI Research, said the team can typically harness a new frontier model within hours of its release, bring in their own data, and evaluate it against Gloo’s human flourishing benchmarks.

“Every developer we talk to, they want to ingest their data, ground the model in their data, and then build agents to be deployed using the infrastructure,” Skytland says. “That literally is the script of the ask of everyone we talk to.”

## Alignment as infrastructure

Gloo’s focus here to bring alignment into the infrastructure. To do this, the company set up a “constitution,” a set of principles that gets applied to all API calls. That constitution, similar to what Anthropic is doing with its models, establishes a baseline for safety, accuracy and compliance. Each organization can then add its own layer on top of this to steer outputs toward its specific values or doctrines. From there, the data layer can add another degree of customization.

As we reported last year, Gloo developed the FAI ([Flourishing AI](https://thenewstack.io/former-intel-ceos-new-ai-benchmark-focuses-on-human-flourishing/)) benchmark to evaluate how frontier models do on human flourishing criteria rather than the usual metrics of speed and cost. Gloo claims its values-aligned model variants show a 13 to 22 percent improvement on FAI scores compared with out-of-the-box models.

![](https://cdn.thenewstack.io/media/2026/03/54461608-glooaiexample.jpg)

An example of Gloo AI Studio’s alignment (credit: Gloo).

## What developers are building

As Billings noted, scripture turns out to be an interesting test case for AI accuracy. “If you’re using an LLM to quote scripture, and you’re using its probabilistic nature, you actually fall sort of victim to those hallucinations,” Billings says. “We believe it should be safe, we believe it should be accurate, and we believe it should be compliant. And in the faith-based world, compliance means aligning with doctrine and theology — and so that’s an area that we spend a lot of time in.”

Billings notes that a devotional assistant grounded in specific biblical texts through the data engine, for example, is far less likely to hallucinate. Other use cases range from theological study tools at Christian universities to content moderation for faith-based community apps.

But it is not just faith-based organizations that are interested. Billings said one of the largest organizations in the country — he declined to name it but noted they are in the food industry — is in conversations with Gloo, and its interest has nothing to do with religion.

“They’re choosing us simply because we really stand on a values-aligned, trusted approach to AI,” he says. “People pay them for their given food product, and therefore, the technology they implement and adopt is *only* in pursuit of helping them fulfill their mission. And that’s something that we hear a lot from the organizations that we serve.

“They don’t get into the technology business for the sake of playing or even in the name of innovation. They get in it solely for the purpose of advancing their mission. They take a really disciplined approach.”

There’s an opportunity here for Gloo to go well beyond its faith-based roots, and one that the team seems to be well aware of. AI values matter across industries, and the company is betting that alignment will become a standard infrastructure expectation, not a niche concern.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://thenewstack.io/wp-content/uploads/2025/03/15a7eb12-cropped-4e88ac40-frederic-profile-2-600x600.jpg)

Before joining The New Stack as its senior editor for AI, Frederic was the enterprise editor at TechCrunch, where he covered everything from the rise of the cloud and the earliest days of Kubernetes to the advent of quantum computing....

Read more from Frederic Lardinois](https://thenewstack.io/author/frederic-lardinois/)