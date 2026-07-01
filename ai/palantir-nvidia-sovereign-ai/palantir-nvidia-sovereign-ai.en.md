Building with AI has, until recently, meant calling up someone else’s model. But wiring an app to an API from OpenAI, Anthropic, or Google is a poor fit for government and operators of critical infrastructure. When data legally or operationally cannot leave a secured network, a hosted endpoint in someone else’s cloud is a non-starter, regardless of whether the workload is intelligence analysis, grid operations, or patient records.

> “The most revealing aspect here is that Palantir didn’t ship a model, but the apparatus for deploying and owning one.”

That’s the lens through which to read [Palantir’s announcement](https://www.businesswire.com/news/home/20260629390275/en/Palantir-Launches-Engine-for-Deploying-NVIDIA-Nemotron-Open-Models-in-Sovereign-Environments) on Monday. The company introduced an “intelligent engine,” built on Nvidia AI and [Nemotron open models](https://thenewstack.io/nvidia-launches-nemotron-3-super-a-120b-open-model-for-large-scale-ai-systems/), for running, customizing, and continuously improving AI inside air-gapped and other sovereign environments while keeping data and model weights in the customer’s hands. The most revealing aspect here is that Palantir didn’t ship a model, but the apparatus for deploying and owning one.

## From calling AI to operating it

Most organizations will run a hybrid of hosted and self-hosted models for years, but a second pattern is hardening alongside this workflow. Rather than treating the model as an external service, the application communicates with an internal AI platform that routes requests to one or more models running on the organization’s GPUs. Data never leaves the perimeter, which hands security and compliance teams direct control over governance, auditing, and retention.

So we’re seeing the question shift from *which model we should call t*o *w**hich models we should own and operate ourselves.* And, just as importantly, *what does it cost us to run them?*

## What’s actually in the box

This is where the announcement gets more concrete than the press release lets on, and where it’s worth knowing what Nemotron is.

Nemotron is Nvidia’s family of open-weight models, released in 2026 in three sizes — Nano (~31.6B parameters), Super (120B), and Ultra (550B). All three use a hybrid Mamba-Transformer mixture-of-experts design that activates only about a tenth of their parameters per token, so they run far cheaper than their headline sizes suggest, with context windows up to a million tokens.

Nvidia publishes the weights, training data, and recipes under a permissive license, and the models are deployable via open runtimes such as vLLM, SGLang, and llama.cpp, Ollama — or as Nvidia NIM microservices, the containerized, TensorRT-LLM-optimized path that ships inside the Nvidia AI Enterprise suite. Palantir, notably, was already on Nvidia’s published list of early Nemotron adopters, so this is less a cold start than a formalization.

An important note for builders weighing the move: Nemotron doesn’t top the raw-capability leaderboards; open families like DeepSeek, Qwen, and Kimi K2 generally score higher on absolute benchmarks. Nemotron’s pitch is efficiency on Nvidia silicon and genuine openness, which is exactly the axis that matters when the deployment target is your own hardware behind an air gap rather than a hosted endpoint.

Palantir’s contribution is the layer that turns “download the weights” into “run this in a classified environment and keep improving it.” The company describes three engineering surfaces: *deployment* (getting base and customized models into air-gapped and classified networks), *context* (prompts, workflow structure, and model behavior in production), and *model* (changing the weights themselves on proprietary data and mission outcomes). Underneath sits Palantir’s existing stack — AIP, Ontology, Foundry, and Apollo — handling data authorization, enforced isolation, and auditability.

The “self-improving” claim is a telemetry loop: The engine captures usage and trace data, then uses it to post-train and align the model toward the tasks where it adds value. This is the part that demands the most operational discipline, because a feedback loop with no evaluation harness is a recipe to drift.

## The catch: Owning the stack means owning the stack

The sovereignty pitch is genuinely attractive, and it has a price tag the announcement doesn’t dwell on. Owning your models means owning everything around them. That’s GPU capital expenditure and the power and cooling to match; an inference stack you keep patched and performant; a model lifecycle — fine-tuning, evaluation, rollback — that you staff and run yourself; and a security burden that doesn’t go away just because the box is disconnected.

> “Owning your models means owning everything around them.”

Ultra-class models, in particular, are not modest: running a 550B model, even at ~10% activation, requires multi-GPU server nodes, not a spare rack.

For an agency that legally cannot use a hosted API, that cost is simply the cost of doing the work, and the calculus is easy. For a commercial enterprise that *could* use a hosted endpoint, the math is a real trade — control and data residency on one side, capex and operational headcount on the other. The right answer is workload-specific, and anyone selling it as obvious is selling something.

## Read the announcement for what it is

It’s also worth being clear about what this news is not. It’s a packaging-and-positioning announcement between two companies with aligned incentives: NVIDIA sells more GPUs and more AI Enterprise licenses, Palantir sells more platform, and “sovereign AI” is the banner both have been marching under all year. There’s no named agency customer, no contract value, and no benchmarks. Palantir CEO Alex Karp says many U.S. clients already use these models and frames the appeal as avoiding proprietary insight being baked into the weights of [closed models](https://thenewstack.io/ai-agents-credential-crisis/); NVIDIA’s Jensen Huang calls open source foundational to national security. Both quotes are doing strategic work. The substance here is the integration and the go-to-market, not a technical breakthrough.

## Why it still matters

Strip away the government framing, and the same pattern is spreading through finance, healthcare, manufacturing — anywhere data residency and compliance are design constraints rather than afterthoughts. The reasons it’s newly practical are concrete: open models good enough for production, MoE architectures that cut the compute bill, and an inference tooling layer (NIM, TensorRT-LLM, vLLM) mature enough that air-gapped serving is an engineering project rather than a research one.

> “The model becomes a component. The engine becomes the product.”

The takeaway here for developers is that as open models converge on “good enough,” differentiation shifts to everything around them — deployment, routing, governance, evaluation, security, and lifecycle management. The model becomes a component. The engine becomes the product.

Most organizations will keep calling hosted APIs for plenty of work. But for a growing set of them, the interesting question is how much of the stack they’re prepared to own — and whether they’ve counted the cost of owning it.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://thenewstack.io/wp-content/uploads/2026/06/c176528b-cropped-54a705ce-amandacaswellheadshot_4-600x600.jpeg)

Amanda Caswell is an AI journalist, certified prompt engineer, and technology commentator whose work and expertise have been featured on Fox News and CBS News. She covers artificial intelligence, developer tools, foundation models, and emerging technologies, with a particular focus...

Read more from Amanda Caswell](https://thenewstack.io/author/amanda-caswell/)