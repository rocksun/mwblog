LAS VEGAS — [Amazon Web Services](https://aws.amazon.com/?utm_content=inline+mention) CEO [Matt Garman](https://www.linkedin.com/in/mattgarman/) had a story to tell about [Kiro](https://thenewstack.io/aws-kiro-brings-automated-reasoning-to-agentic-development/), its new agentic IDE, in his keynote at AWS re:Invent.

A distinguished engineer at his company, Anthony, led a team that rearchitected a project in 76 days with six developers. They had initially expected it to take 18 months with 30 people. Eye-opening stuff, enough to make an engineering lead run to the agent vending machine.

Garman shared his story this fall with customers, who asked how Anthony’s team did it. That kind of question will be asked for a long time, which in itself reveals how little people know about the infrastructure, the model and how to use the agents that power what AWS needed a distinguished engineer and team to accomplish.

Welcome to the messy middle.

We are in the middle ages of AI workload development, deployment and management. It’s the messy middle, or the fun times, as one leading engineer said to me. It just depends on how you look at it.

The cloud took 10 or more years to mature. AI’s maturity might take half that time or even less. In the product announcements at re:Invent, Garman showed how fast the pace is moving.

But strikingly, these are innovations without established practices. It’s still more about how you achieve these fascinating results than about [standardizing best practices](https://thenewstack.io/the-production-generative-ai-stack-architecture-and-components/), so you don’t have to build from scratch with GPUs, a dizzying number of models and agentic workflows that are brand new to everyone.

Garman highlighted AWS’ massive scale. Yes, it generates $132 billion in annual revenue and has deployed 1 million Trainium chips, but that comes with trade-offs.

Tech companies are inventing new architectures that are very cool. But at the same time, users are trying to use this new hardware with little understanding of how the infrastructure fits into their enterprise operations. Rapid development is exciting, but the quest for optimal architecture will take time and require significant adaptation, which is very new to most customers.

## Rapid Infrastructure Development

Garman announced that Trainium is now generally available and previewed Trainium 4. AWS also launched both P6 GB200 and GB300 instances.

Map these announcements to the issues that companies like [Uber](https://thenewstack.io/inside-ubers-multicloud-ai-reality-the-gap-between-data-and-compute/) face, and you get a sense that the challenges with moving from cloud native to AI native will only get tougher.

At [KubeCon + CloudNativeCon North America](https://thenewstack.io/event/kubecon-cloudnativecon-na-2025/) last month, Uber talked a lot about how it uses multiple clouds, and what it takes to optimize AI workloads across them. Customers need these choices, but the reality has caught up to Uber, and it will for more and more customers as well.

And what will it take to train the models? The people with capital and engineering talent will thrive. It’s a time of disruption, but how polarized will it get for the [haves and have-nots](https://thenewstack.io/how-cios-can-battle-gpu-poverty-in-the-age-of-ai/)?

Case in point: Garman talked about an entire AWS campus dedicated to training [Project Rainier](https://www.aboutamazon.com/news/aws/aws-project-rainier-ai-trainium-chips-compute-cluster) for [Claude](https://thenewstack.io/anthropics-new-claude-opus-4-5-reclaims-the-coding-crown-from-gemini-3/), Anthropic’s [large language model (LLM)](https://thenewstack.io/introduction-to-llms/). That’s a whole campus for one project, a scenario that is outside what most companies can afford to do — or even have the talent to consider.

Garman said AWS will offer AI factories, but inside enterprises. Why is that? The [repatriation trend](https://thenewstack.io/why-companies-are-ditching-the-cloud-the-rise-of-cloud-repatriation/) signals that customers want their data on their own infrastructure.

It’s a significant shift. Cloud is still king, but there’s another constraint to consider: Power is the bottleneck. AWS will build what it compares to AWS regions. These are vertically integrated capabilities with [Bedrock and other AWS services](https://thenewstack.io/aws-makes-it-easier-to-customize-ai-models-in-bedrock-and-sagemaker-without-a-phd/) built in. But here’s the catch: The customer is responsible for providing the power and all the data center requirements to run AI workloads.

## Models, Models, Everywhere

AWS announced [four new Nova models](https://thenewstack.io/aws-updates-its-nova-models-to-compete-with-google-anthropic-and-openai/):

* **Amazon Nova Micro** is text-only, helping with latency issues.
* **Amazon Nova Lite** is a multimodal model.
* **Amazon Nova Pro** is also a multimodal model with enhancements for accuracy, speed and cost.
* **Amazon Nova Premier** is the company’s most sophisticated model.

Garman also discussed supporting models from Anthropic, OpenAI, Cohere and others. And Nova Forge is used to create versions of the AWS models, which they call novellas. The goal: Make it more affordable to build a model from scratch.

In every technology era, proliferation is the rule, not the exception. After more than a decade of cloud native distributed workloads, convergence is now an aspiration with the proliferation of GPUs. We are in the age of specialization, not general workloads.

At KubeCon, Uber’s [Andrew Leung](https://www.linkedin.com/in/anwleung) pointed to his company’s own struggle to get convergence — and it’s a leader in using AI workloads. Garman, for his part, stated, “We’ve never believed that there was going to be one model to rule them all.”

But the proliferation does impact convergence, allowing enterprises to maintain vast, distributed workloads. At re:Invent, Gaman talked about the extensive choice in models. But he did not address the big challenge engineers face: CPUs and GPUs are comparable but not interchangeable in practice.

The best example comes from AWS. Garman talked about Kiro, the platform AWS developed.

“Now I want to take a quick moment and dive deeper into one of the stories we heard,” he told the re:Invent audience. “The details are pretty high. This was a quote from Anthony, one of our distinguished engineers. Anthony was working on a rearchitecture project … ”

But where are the details of the case study? Who is Anthony? And for a company like AWS, why did it take weeks?

AWS sits in a great place. The Kiro team, being an AWS team, knows what infrastructure and which models to use. The team can adapt as it controls all aspects of the product development.

But it still took weeks for those team members to reach the point where they could devise a real plan. They needed to figure out what the agents could and could not do. And this is one team.

It raises questions about how AWS is faring in building out agentic architectures and managing state — all the sorts of issues that customers have limited resources to address.

And then there’s why we are hearing about Anthony. His team succeeded dramatically. That says a lot in itself.

What followed? How that team’s grand success led to AWS’ big news.

“In fact, we’ve been so blown away that last week, all of Amazon decided to standardize on Kiro as our official AI development environment,” Garman said.

## How AI Agents Are Like Teenagers

AWS is just starting its journey. It’s terrific how deeply its CEO’s excitement runs for AI workloads. The fact that people are asking how to follow its lead shows the approach is just starting to be used.

The “messy middle” theme became evident throughout the keynote. Garman compared agents to raising teenagers. They need ground rules; agents need supervision. They’re young — there’s a lot to learn.

The excitement at re:Invent is palpable. The keynote told about a grand new world where infrastructure and models serve as the foundation for agentic AI, and maybe even the wonders of a new world that can change so much.

But these are new times. It’s really cool, but the knowledge is not that transferable. Not quite yet.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://cdn.thenewstack.io/media/2022/09/13c3d9d6-cropped-0fe18b69-ef774ac85213a6506cf973dc6380cd57.jpeg)

Alex Williams is founder and publisher of The New Stack. He's a longtime technology journalist who did stints at TechCrunch, SiliconAngle and what is now known as ReadWrite. Alex has been a journalist since the late 1980s, starting at the...

Read more from Alex Williams](https://thenewstack.io/author/alex/)