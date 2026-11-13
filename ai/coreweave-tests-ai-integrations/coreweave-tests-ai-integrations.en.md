![Futuristic digital visualization of global trade data.](https://cdn.thenewstack.io/media/2025/12/8d3fb16d-network-1024x576.jpg)

**Moving an AI workload to another cloud** means bringing more than a model and its data. Your serving layer, observability dashboards, security controls, and [storage systems](https://www.coreweave.com/products/storage?utm_source=coreweave.com&utm_medium=site#object-storage) have to work together on the new infrastructure. For platform teams, proving those connections under real traffic can become the slowest and riskiest part of the move.

As a stack grows across vendors and clouds, each project adds more integration questions. A compatible specification is a starting point. It doesn’t guarantee a tool will behave as expected in production, or that the runbooks and security workflows built around it will carry over.

## Make production validation visible

An integration needs to work on the infrastructure where you plan to run it, under production traffic. The tools should also be ones your team already uses or has asked for.

> “A compatible specification is a starting point. It doesn’t guarantee a tool will behave as expected in production, or that the runbooks and security workflows built around it will carry over.”

We built the [CoreWeave Partner Network](https://www.coreweave.com/coreweave-partner-network?utm_source=coreweave.com&utm_medium=site) to make that validation visible. It brings relationships with CrowdStrike, VAST Data, Reflection, IBM, and other technology vendors into a curated network of integrations tested under real-world production conditions on [CoreWeave Cloud](https://www.coreweave.com/platform?utm_source=coreweave.com&utm_medium=site).

The network covers four parts of the AI stack, from [training](https://www.coreweave.com/solutions/ai-model-training?utm_source=coreweave.com&utm_medium=site) and inference to data movement, security, and the next iteration:

* Infrastructure: compute, storage, networking, servers, and interconnects, with partners including VAST Data, Dell, AMD, IBM, BackBlaze, and Pulumi.
* Data services: storing, processing, moving, and accessing AI data throughout its lifecycle, with ClickHouse, Encord, LanceDB, and Datology.
* Independent software vendors (ISVs): orchestration, observability, and model development, including Grafana, Datadog, Union, SkyPilot, IBM, Pinecone, Redis, LlamaIndex, and Clockwork. A dedicated security segment includes CrowdStrike, Zscaler, and Cranium.
* Models, agents, and inference: foundational software and services for building, training, serving, and scaling applications, with Reflection, RadixArk, Inferact, OpenRouter, and Red Hat.

Together, these integrations support running and observing models, curating data, improving behavior, and evaluating the next release. Every partner must meet the same requirement: an integration that works on CoreWeave infrastructure under production conditions. Partners enter the network because customers run them or ask for them.

## Read the workload evidence

[IBM trained its Granite models on CoreWeave](https://www.coreweave.com/resources/case-studies/ibm?utm_source=coreweave.com&utm_medium=site) around one of the first deployments of Nvidia GB200 NVL72 clusters. [Cohere built North](https://www.coreweave.com/resources/case-studies/cohere-accelerates-training-of-north-agentic-ai-for-enterprise?utm_source=coreweave.com&utm_medium=site), its [agentic AI platform](https://thenewstack.io/agentic-ai-the-next-frontier-of-ai-power/), on one of the industry’s first production GB200 NVL72 clusters and reported training three times faster than on Nvidia Hopper.

[Mistral AI trains its models entirely on CoreWeave](https://www.coreweave.com/resources/case-studies/mistral-ai?utm_source=coreweave.com&utm_medium=site) and cites training 2.5 times faster on Nvidia GB200 NVL72 systems. [Decart uses Nvidia HGX B200 at production scale](https://www.coreweave.com/resources/videos/creating-realtime-ai-experiences?utm_source=coreweave.com&utm_medium=site) through its CoreWeave collaboration, on a platform that includes [Weights & Biases](https://www.coreweave.com/companies/weights-and-biases?utm_source=coreweave.com&utm_medium=site).

The underlying relationships predate the network announcement. CoreWeave and Weights & Biases have run production integrations with Encord, Pinecone, and other partners since the early wave of open-source large language models (LLMs) and frontier-model training.

[Jon Jones](https://www.linkedin.com/in/jonjones1/), CoreWeave’s Chief Revenue Officer, describes the change as making existing partner work visible before customers build. The network also provides a repeatable way to pursue deeper integrations, joint go-to-market work, and shared innovation.

The partners emphasize different parts of that system. VAST Data co-founder and chief technology officer Alon Horev describes combining CoreWeave’s AI cloud with the VAST AI Operating System across large-scale training, fine-tuning, production inference, and continuous [agentic workloads](https://thenewstack.io/ai-cloud-taxonomy-2026/). CrowdStrike CEO and founder [George Kurtz](https://www.linkedin.com/in/georgekurtz/) emphasizes security built into the infrastructure running AI. [Adam Lawrence](https://www.linkedin.com/in/adamelawrence/), general manager of IBM Americas, points to IBM and Red Hat technologies as a way to expand choice and reduce integration work when deploying and scaling AI.

## Carry over the operations you already use

Your team has already built runbooks around its observability tools. Grafana and Datadog integrations let you carry that work over. CrowdStrike, Zscaler, and Cranium provide security integrations, bringing existing threat visibility and response tooling.

[Inference integrations](https://www.coreweave.com/solutions/ai-inference?utm_source=coreweave.com&utm_medium=site) serve a similar purpose: keeping the models available as teams expand onto CoreWeave, without [rebuilding the serving layer](https://thenewstack.io/5-tech-predictions-for-2026-from-ai-inference-to-kubernetes/). The goal is to add capacity while retaining the parts of the stack that already work.

> “A marketplace listing still leaves your team to validate the integration. An LLM can suggest what’s popular without telling you what works on your infrastructure.”

A marketplace listing still leaves your team to validate the integration. An LLM can suggest what’s popular without telling you what works on your infrastructure. We select partners based on customer demand and test their integrations across all four segments.

The integration problem also reaches inside agent execution. Most closed models include web search, while most open-weight models do not. Teams choosing open weights for cost, control, or customization have often had to connect a search provider separately.

CoreWeave is extending its partner approach to these tools, beginning with Exa, Parallel Web Systems, and You.com. The announced search layer provides access through one integration instead of a separate contract for each provider.

Teams can enable it through a single setting on a standard inference request or access it from inside a [CoreWeave Sandbox](https://www.coreweave.com/products/coreweave-sandboxes?utm_source=coreweave.com&utm_medium=site), without setting up a separate software development kit (SDK) or account. The arrangement is nonexclusive, so using the integration does not restrict future provider choices.

We announced the search partnerships at Fully Connected, with the remaining integration work planned for the following weeks. As those integrations become available, they will meet the same production-validation standard as the rest of the network.

## Start with the connections your workload needs

Before adding another cloud, check the serving, data, observability, and security connections your workload depends on. Ask which integrations have been tested under production conditions and what your team will still need to validate.

> “Before adding another cloud, check the serving, data, observability, and security connections your workload depends on.”

The CoreWeave Partner Network lists validated partners. CoreWeave account teams can discuss a specific integration and workload, and partner sessions from [Fully Connected 2026](https://www.coreweave.com/fully-connected-2026?utm_source=coreweave.com&utm_medium=site) offer another way to see the integrations in use. Teams interested in new collaborations can explore the [partner program](https://www.coreweave.com/coreweave-partner-network?utm_source=coreweave.com&utm_medium=site#partner-with-coreweave).

The post [CoreWeave tests AI integrations on its cloud before you migrate](https://thenewstack.io/coreweave-tests-ai-integrations/) appeared first on [The New Stack](https://thenewstack.io).