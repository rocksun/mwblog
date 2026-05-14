On Tuesday, Red Hat announced significant advancements to [Red Hat AI (RHAI) 3.4](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux_ai) at its [Red Hat Summit](https://www.redhat.com/en/summit) in Atlanta.

Red Hat promises to deliver what the company [describes](https://www.redhat.com/en/about/press-releases/red-hat-unites-builders-and-operators-agentic-future-major-advancements-red-hat-ai) as “metal-to-agent capabilities” designed to bridge the gap between AI experimentation and production-grade operational control across hybrid cloud infrastructure.

What that means, according to [Red Hat](https://www.redhat.com/en) VP of AI [Joe Fernandes](https://www.linkedin.com/in/joefernandes1/), is that the company’s AI strategy is “divided into four key pillars. First, helping customers deliver fast, flexible, and efficient inference, serving models in their environment. Second, connecting their enterprise data to those models and agents. Third, helping them accelerate the deployment and management of agents across a hybrid cloud environment. And fourth, bringing that all together on our integrated AI platform, enabling them to run any model in any agent, across any hardware and cloud environment.”

That last one about “bringing that all together” is a new and important part of Red Hat’s latest AI plan. RHAI 3.4 centers on [Model-as-a-Service](https://www.redhat.com/en/topics/ai/what-is-models-as-a-service) (MaaS). This enables you to deliver pre-trained AI and machine learning models as shared resources accessible on demand through API endpoints. In Red Hat’s implementation of this idea, MaaS also provides a single, governed interface for developers to access curated models while enabling administrators to track consumption and enforce policies.

> In Red Hat’s implementation of Model-as-a-Service, it also provides a single, governed interface for developers to access curated models while enabling administrators to track consumption and enforce policies.

In addition, RHAI 3.4 builds on high-performance distributed inference powered by the [vLLM inference server](https://docs.vllm.ai/en/latest/) and the [llm-d distributed inference engine](https://developers.redhat.com/articles/2025/11/21/introduction-distributed-inference-llm-d) to maintain optimized model serving across diverse environments. On top of that, RHAI Inference adds request prioritization to its distributed inference capabilities.

This allows interactive and background traffic to share the same endpoint while latency-sensitive requests are processed first under load. Red Hat also claims that [speculative decoding support](https://docs.vllm.ai/en/latest/features/speculative_decoding/) “improves response speeds by 2x–3x with minimal quality impact while lowering the cost per interaction.”

> “The agentic era represents an evolution of our platform from running traditional applications to powering intelligent, autonomous systems.”

That’s handy because agents, which are becoming increasingly popular, consume a lot of resources. As Fernandes observes, “What’s really going to be driving inference demand exponentially is AI agents.”

To address the operational challenges of autonomous agents, RHAI 3.4 introduces comprehensive AgentOps capabilities, including “integrated tracing, observability, and evaluations, alongside agent identity and lifecycle management to move agents from development to production.” The platform is framework-agnostic, managing agents “regardless of agent framework.”

Fernandes continues, “So, with our new [MCP [Model Context Protocol]](https://thenewstack.io/model-context-protocol-a-primer-for-the-developers/) server catalog and MCP gateway, we provide governed access to MCP server-based tools and secure access at runtime when we make those connections. Enterprise customers need us to help connect their enterprise data to both models and agents.

“We’re introducing a new evaluation hub that provides an integrated control plane and a collection of evaluation frameworks to help evaluate model and agent performance, integrated experiment tracking, and automation for configuring retrieval, augmented generation, and traditional ML models, and then again, this all comes together in our AI platform.”

To secure all this, Red Hat is now using SPIFFE/SPIRE-based cryptographic identity management. This enables organizations to replace static hardcoded keys with short-lived tokens to support “east-privilege operations for autonomous agents across the stack and help confirm that agentic actions are tied to a verified identity.

While that certainly helps, RHAI also integrates automated adversarial scanning directly into the development lifecycle. It’s doing this by leveraging technology from its newly acquired Chatterbox Labs and using [Garak](https://docs.garak.ai/garak), an LLM vulnerability scanner. RHAI uses this to screen models and agentic systems for risks such as jailbreaks, prompt injections, and bias. Red Hat is  pairing with [Nvidia NeMo Guardrails](https://developer.nvidia.com/nemo-guardrails) for run-time safety.”

Red Hat is also introducing integrated prompt management. This treats prompts as first-class data assets. It stores the inputs driving models and agents in a central registry, providing a single source of truth for developers and administrators.

To help ensure all this is working as efficiently as possible, RHAI’s evaluation hub provides a framework-agnostic, unified AI evaluation control plane for evaluating LLMs, AI applications, and agents. This Red Hat claim replaces “fragmented testing methods with a unified approach to benchmarking quality, accuracy, and risk”. These capabilities are powered by [MLflow](https://mlflow.org/), which “provides integrated experiment tracking and artifact management for both generative and predictive AI use cases.”

Strategically, Fernandes says, “The agentic era represents an evolution of our platform from running traditional applications to powering intelligent, autonomous systems. We are defining the open standard for how enterprises execute AI. By providing a hardened, metal-to-agent foundation for AI inference, MaaS and AgentOps, Red Hat provides the operational assurance organizations need to innovate at scale while maintaining rigorous control.”

That all sounds grand. We’ll soon be able to tell if RHAI can deliver on Red Hat’s promises. The program was not ready to be unveiled at the Red Hat Summit. It’s expected to be sometime this quarter. I’m looking forward to seeing it run through its paces, and I know I’m not the only one.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://cdn.thenewstack.io/media/2023/03/cee63948-cropped-8a0b5c52-steven-vaughan-nichols.jpg)

Steven J. Vaughan-Nichols, aka sjvn, has been writing about technology and the business of technology since CP/M-80 was the cutting-edge PC operating system, 300bps was a fast internet connection, WordStar was the state-of-the-art word processor, and we liked it.

Read more from Steven J. Vaughan-Nichols](https://thenewstack.io/author/sjvn/)