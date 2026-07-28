**Nvidia CEO Jensen Huang used his first post on X** to share a public letter backing frontier open-weight models. Signed by Microsoft, Meta, Hugging Face, and 22 other organizations, the letter argues that open models improve security, encourage faster innovation, and give countries and enterprises more control over their AI infrastructure. The timing of the Friday post is notable, with more organizations choosing to run open-weight models inside their own environments rather than relying entirely on hosted services.

> “Open weights let every organization match the right model to the right job at the right cost, reserving frontier-scale capability for genuine frontier problems and running efficient, specialized models everywhere else.”

## A case for hybrid stacks

The letter draws a comparison between open-weight AI and open-source software, arguing that broad access has driven decades of software innovation. It says the same principle applies to AI. Instead of sending every request to a hosted model, organizations can download an open-weight model, run it on their own infrastructure, customize it for a specific workload, and keep sensitive data behind their own firewall.

Nvidia has already been moving in this direction — [its leaders have described a future where local and frontier models split the work by cost, speed, and control](https://thenewstack.io/nvidia-local-frontier-models/). As the coalition argues, “Open weights let every organization match the right model to the right job at the right cost, reserving frontier-scale capability for genuine frontier problems and running efficient, specialized models everywhere else.”

One isn’t necessarily replacing the other, and many enterprise teams already use both, choosing between them based on cost, performance, compliance requirements, and where the workload needs to run.

The letter underscores this reality for infrastructure teams, noting, “As organizations invest in AI, they want to know that they will not become locked into a single provider or lose the knowledge and capabilities they build over time.” That vendor lock-in concern is already reshaping deals — [Anaconda’s recent acquisition of Kilo was framed explicitly around enterprises’ reluctance to depend on a single AI provider](https://thenewstack.io/anaconda-kilo-open-source-acquisition/).

## Washington weighs new restrictions

The timing is notable. Washington is weighing new restrictions on some Chinese AI models, including [Moonshot AI’s Kimi K3](https://thenewstack.io/kimi-k3-open-weight-coding/), even though the Trump administration’s AI Action Plan described open models as a strategic advantage for the United States.

That split extends to the AI industry itself, though critics differ in their specific concerns. OpenAI’s Dean Ball has publicly warned about the broad economic and regulatory risks associated with Chinese open-weight models. Anthropic’s Sarah Heck, meanwhile, has specifically backed the White House’s allegations regarding intellectual property theft through distillation.

> “Relying solely on closed models is not inherently safe: they can be breached, misused, or fail in ways that outsiders cannot detect. And concentrating advanced AI capabilities behind a small number of closed models compounds that risk.”

The companies that signed the letter argue that continuing to develop frontier open models is part of maintaining U.S. leadership in AI. They argue that security through obscurity is fundamentally flawed, stating: “Relying solely on closed models is not inherently safe: they can be breached, misused, or fail in ways that outsiders cannot detect. And concentrating advanced AI capabilities behind a small number of closed models compounds that risk.”

[Palantir and Nvidia have already operationalized this argument](https://thenewstack.io/palantir-nvidia-sovereign-ai/), building an engine that runs open Nemotron models inside air-gapped government networks.

## Distillation meets trade policy

Distillation, one of AI’s most contentious topics, was also addressed. Widely used by researchers and model builders to create systems that are cheaper to run and easier to deploy, the letter states that it should be treated as a legitimate research technique rather than intellectual property theft.

The issue has taken on new significance after the [White House accused China’s Moonshot AI of specifically distilling Anthropic’s Fable model to build Kimi K3](https://thenewstack.io/moonshot-fable5-distillation-accusations/) — an allegation the company has denied.

Distillation is one way teams build smaller models that can run on private infrastructure, edge devices, or lower-cost GPU clusters. [Kimi K3’s launch showed just how much GPU capacity these deployments demand](https://thenewstack.io/kimi-k3-inference-bottleneck/) — Moonshot had to freeze new subscriptions within 48 hours after demand overwhelmed its available inference capacity. Any new restrictions on that process could affect how enterprise AI systems are built and deployed.

> “As organizations invest in AI, they want to know that they will not become locked into a single provider or lose the knowledge and capabilities they build over time.”

## Nvidia’s infrastructure incentive

Every enterprise that chooses to self-host, fine-tune, or customize an open-weight model needs infrastructure to run it. Nvidia also has clear business reasons for supporting a future in which both proprietary and open-weight models thrive.

The company supplies the hardware powering both hosted frontier models and enterprise-owned deployments. Organizations that use a mix of commercial APIs and self-hosted open models ultimately expand demand for AI infrastructure across the board — a dynamic that is already [redirecting enterprise IT budgets toward AI hardware at the expense of traditional software spending](https://thenewstack.io/ibm-earnings-ai-infrastructure/).

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://thenewstack.io/wp-content/uploads/2026/06/c176528b-cropped-54a705ce-amandacaswellheadshot_4-600x600.jpeg)

Amanda Caswell is an AI journalist, certified prompt engineer, and technology commentator whose work and expertise have been featured on Fox News and CBS News. She covers artificial intelligence, developer tools, foundation models, and emerging technologies, with a particular focus...

Read more from Amanda Caswell](https://thenewstack.io/author/amanda-caswell/)