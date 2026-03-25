The marriage of Kubernetes and AI has arrived in llm‑d, a replicable Kubernetes blueprint to deploy inference stacks for any model, on any accelerator, in any cloud.

On Tuesday at [KubeCon Europe 2026](https://events.linuxfoundation.org/kubecon-cloudnativecon-europe/) in Amsterdam, IBM Research, Red Hat, and Google Cloud announced the donation of [llm‑d](https://llm-d.ai/), their open‑source distributed inference framework, to the [Cloud Native Computing Foundation (CNCF)](https://www.cncf.io/) as a sandbox project.

The move, supported by founding collaborators NVIDIA and CoreWeave along with AMD, Cisco, Hugging Face, Intel, Lambda, and Mistral AI, establishes llm‑d as a community‑governed blueprint for scalable, vendor‑neutral large language model (LLM) inference.

Launched in 2025, [llm‑d was built to make serving foundation models at scale predictable, portable, and cloud‑native](https://www.redhat.com/en/blog/what-llm-d-and-why-do-we-need-it). It transforms [inference from an improvised, model‑by‑model challenge into a replicable, production‑grade Kubernetes-based system](https://thenewstack.io/kubernetes-glorified-ai-host/). Llm-d was created by [Neural Magic, which Red Hat acquired in 2025](https://thenewstack.io/red-hats-ai-platform-now-has-an-ai-inference-server/). IBM’s goal, says [Carlos Costa](https://www.linkedin.com/in/carlos-costa-9b9b1a1/), IBM Research Distinguished Engineer at KubeCon in his keynote, is to “make a large‑scale model serving a first‑class cloud‑native workload.”

Specifically, llm-d is an open‑source, Kubernetes‑native framework for running large language model (LLM) inference as a distributed, production‑grade workload. What that means in practice is:

* Llm-d turns LLM serving into a distributed system: it splits inference into prefill and decode phases (disaggregation) and runs them on different pods. That means you can scale and tune each phase independently.
* It adds an LLM‑aware routing and scheduling layer. This is done via a gateway extension that routes requests based on [KV‑cache](https://huggingface.co/blog/not-lain/kv-caching) state, pod load, and hardware characteristics to improve latency and throughput.
* Finally, it provides a modular stack on top of Kubernetes using  [vLLM](https://vllm.ai/) as an inference gateway, and related components to give you a reusable blueprint for “any model, any accelerator, any cloud.”

Conceptually, while vLLM acts as the fast inference engine, llm‑d provides the operating layer that lets you run that engine across clusters of GPUs/TPUs with intelligent scheduling, cache‑aware routing, and autoscaling tuned for LLM traffic rather than generic HTTP workloads.

In a press conference, [Brian Stevens](https://www.linkedin.com/in/brianmarkstevens/), former Neural Magic CEO and now Red Hat SVP and AI CTO, says, “We do a lot of work bringing in new accelerators. TPUs, AMD, Nvidia, and a long tail of other accelerators. We really want to see them have ways of getting in. So that way, just like Linux, you can run any hardware, any application, with BLM, any model, any accelerator.”

This is both faster and cheaper than older ways of running inference. Early testing by Google Cloud showed “[2x improvements in time-to-first-token](https://cloud.google.com/blog/products/ai-machine-learning/enhancing-vllm-for-distributed-inference-with-llm-d) for use cases like code completion, enabling more responsive applications. That’s because traditional autoscalers, generic APIs, and request routing weren’t designed for stateful inference workloads that depend on efficient KV cache management, prefill/decode orchestration, and heterogeneous accelerators.

Llm‑d tackles these problems head‑on. It introduces prefix‑cache‑aware routing and prefill/decode disaggregation, allowing inference phases to scale independently. It supports hierarchical cache offloading across GPU, CPU, and storage tiers, enabling larger context windows without overloading accelerator memory.

Its traffic‑ and hardware‑aware autoscaler adapts dynamically to workload patterns rather than relying on basic utilization metrics. It’s also designed to work in tandem with emerging Kubernetes APIs such as the [Gateway API Inference Extension (GAIE)](https://gateway-api-inference-extension.sigs.k8s.io/) and [LeaderWorkerSet (LWS)](https://lws.sigs.k8s.io/). Together, this trio is designed to make distributed inference a first‑class Kubernetes workload.

The project’s contributors describe llm‑d as a “well‑lit path” for organizations moving from experimentation to production. “We tested this for you. We benchmarked it. We went through the pain,” Costa said. The framework offers reproducible benchmarks, validated deployment patterns, and compatibility across major accelerator families from Nvidia GPUs to Google TPUs to AMD and Intel hardware.

[Priya Nagpurkar](https://www.linkedin.com/in/priya-nagpurkar/), IBM Research’s VP of AI Platform, said during the llm-d keynote, emphasized that inference now demands the same operational maturity that Kubernetes brought to microservices. “You need the scale, distribution, and reliability of what Kubernetes provided for the previous era, while recognizing that this is a very different workload.”

By contributing llm‑d to the CNCF, IBM and partners are betting that AI inference will soon become as foundational to the cloud‑native stack as Prometheus or Envoy.

IBM sees the donation as pivotal to standardizing the deployment and management of distributed inference. “CNCF is becoming the home for AI infrastructure,” Costa said. “It’s where common patterns, APIs, and governance converge so that everyone builds on the same playbook.”

Looking ahead, llm-d’s next development cycle will focus on expanding llm‑d’s capabilities around multi‑modal workloads, HuggingFace [multi‑LoRA](https://huggingface.co/blog/multi-lora-serving) optimization, and deeper integration with vLLM. Specifically, [Mistral AI](https://mistral.ai/) is already contributing code to advance open standards around disaggregated serving.

IBM Research will continue exploring the intersection of inference and training, including reinforcement learning and self‑optimizing AI infrastructure. As Costa put it, “Creating a common foundation stack lets the ecosystem focus on pushing AI forward instead of rebuilding the basics.” With the CNCF as its new home, llm‑d is poised to become a cornerstone of the cloud‑native AI era.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://cdn.thenewstack.io/media/2023/03/cee63948-cropped-8a0b5c52-steven-vaughan-nichols.jpg)

Steven J. Vaughan-Nichols, aka sjvn, has been writing about technology and the business of technology since CP/M-80 was the cutting-edge PC operating system, 300bps was a fast internet connection, WordStar was the state-of-the-art word processor, and we liked it.

Read more from Steven J. Vaughan-Nichols](https://thenewstack.io/author/sjvn/)