Nvidia today launched its latest set of AI models in its open source [Nemotron series](https://www.nvidia.com/en-us/ai-data-science/foundation-models/nemotron/) for powering AI agents: Nemotron 3 Nano, Super and Ultra. For the first time, Nvidia is also releasing not just the models but also three trillion tokens worth of pre-training data and 18 million samples of post-training data. Thanks to Nvidia’s existing training environments, for which the company is also launching 10 new gym environments, and the company’s open source reinforcement learning libraries, developers will also be able to easily take these models and train them for their own use cases.

The Nano model is available now, with the Super and Ultra models expected to be available in the first half of 2026.

### The Nemotron 3 Model Family

As for the models themselves, this is the first of the Nemotron families to use the [mixture of experts](https://www.ibm.com/think/topics/mixture-of-experts) (MoE) technique, which essentially decouples model size from compute cost by only keeping a subset of parameters active at any given time. That, in turn, means these new models are significantly faster, with Nvidia arguing that the 30-billion-parameter Nemotron 3 Nano model (with 3 billion active parameters because of that MoE technique), is up to 4x more performant than the equivalent Nemotron 2 Nano model. It also generates up to 60% fewer reasoning tokens to create its answers, which will bring down the cost of using this model even more. It’s also one of the few open source models to offer a context window of 1 million tokens.

The Nano model, which Nvidia says should work especially well for targeted tasks, is now available on HuggingFace.

The Nemotron 3 Super model is a 100-billion-parameter model with 10 billion active parameters, is meant for multi-agent applications. The Nemotron 3 Ultra model features 500 billion parameters and 50 billion active ones, and while that is going to make the smartest of these new models and great for more complex applications, it’ll also be the most expensive to run.

[![](https://cdn.thenewstack.io/media/2025/12/0e6ceaf2-nemotron-3-press-release-image.png)](https://cdn.thenewstack.io/media/2025/12/0e6ceaf2-nemotron-3-press-release-image.png)

Credit: Nvidia.

Nvidia did not provide the press with detailed benchmarks ahead of the embargo time, all the company has said so far is that “Artificial Analysis, an independent organization that benchmarks AI, ranked the model as the most open and efficient among models of the same size, with leading accuracy.”

You can gather a bit more information about where the Nano model falls from the below Artificial Analysis graph, which puts Nemotron 3 Nano in the same ballpark as OpenAI’s GPT-OSS-20B (high), Qwen 3 30B and Qwen 3 VL 32B, though with much higher tokens per second output speed. ServiceNow’s Apriel Thinking model is significantly slower but a bit ahead of the Nano model in Artificial Analysis’s intelligence index.

[![](https://cdn.thenewstack.io/media/2025/12/35414510-artificial-analysis-intelligence-vs.-output-speed-scaled.png)](https://cdn.thenewstack.io/media/2025/12/35414510-artificial-analysis-intelligence-vs.-output-speed-scaled.png)

Nvidia Nemotron 3 Nano benchmark according to Artificial Analysis. Credit: Nvidia.

## Availability

Given the open source nature and license of these new models, developers will be able to run them themselves if they have the required hardware as an Nvidia NIM microservice, but they will also be available through commercial providers and other platforms, including public clouds like [Amazon](https://aws.amazon.com/?utm_content=inline+mention) Bedrock (serverless) and, soon, on Google Cloud, Coreweave, Nebius, Nscale and Yotta.

Inference services like Baseten, Deepinfra, Fireworks, FriendliAI, OpenRouter and Together AI will also offer it, as well as platforms like [Couchbase](https://www.couchbase.com/products/capella?utm_content=inline+mention), DataRobot, H2O.ai, JFrog, Lambda and UiPath.

### Why Nvidia Builds Its Own Models

While Nvidia is better known for creating the hardware accelerators that the vast majority of large language models have been trained on, the company’s journey in building its own models started in 2019, with the [Megatron-LM model](https://nv-adlr.github.io/MegatronLM). The first models under the Nemotron brand launched in 2024, with a reasoning model based on Meta’s Llama 3.1. Since then, Nvidia has launched quite a few Nemotron models in different sizes and tuned for specific use cases, all with relatively permissive licenses that allowed [companies like ServiceNow](https://thenewstack.io/servicenow-launches-a-control-tower-for-agents/) to tune these models for their own use cases.

When asked why Nvidia is building its own models in a press conference ahead of today’s announcement and if the company is trying to become a frontier model builder, [Kari Briski](https://www.linkedin.com/in/karibriski), the VP of Generative AI for Enterprise at Nvidia, noted that part of the idea here is to push the company’s own hardware to the limit in both training and model inference.

“I wouldn’t have to say ‘is it competing?’ It’s for building it for ourselves and we’re giving it to the ecosystem to trust and develop on top of,” she explained.

This, Briski argued, is also why Nvidia is interested in building this open ecosystem around its models — and model creation in general. “If we believe that generative AI and large language models are — and we do — the development platform of the future, I’m looking at these LLMs as if they’re a library. And what do we do with libraries? We put them out there for [developers] to inspect the code, so that you can understand it, that you can build on it, that we can fix bugs, that we can improve it, and then put that back out there. So the more that we put that out there, the more developer engagement.”

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://thenewstack.io/wp-content/uploads/2025/03/15a7eb12-cropped-4e88ac40-frederic-profile-2-600x600.jpg)

Before joining The New Stack as its senior editor for AI, Frederic was the enterprise editor at TechCrunch, where he covered everything from the rise of the cloud and the earliest days of Kubernetes to the advent of quantum computing....

Read more from Frederic Lardinois](https://thenewstack.io/author/frederic-lardinois/)