# Tetrate, Bloomberg Collaborate on Envoy-Based AI Gateways
![Featued image for: Tetrate, Bloomberg Collaborate on Envoy-Based AI Gateways](https://cdn.thenewstack.io/media/2024/10/7d62fd5a-tetrate-1024x683.png)
[Tetrate](https://tetrate.io/) and [Bloomberg](https://www.bloomberg.com/) have announced a collaborative effort to create an open standard for AI Gateways. This initiative will build upon the [Cloud Native Computing Foundation](https://cncf.io/?utm_content=inline+mention)‘s (CNCF) [Envoy Gateway](https://gateway.envoyproxy.io/) project, which is an implementation of the [Kubernetes Gateway](https://gateway-api.sigs.k8s.io/) application programming interface (API).
Specifically, [Envoy Gateway](https://thenewstack.io/envoy-gateway-offers-to-standardize-kubernetes-ingress/) builds on the Envoy reverse proxy to act as a network gateway, allowing it to direct internal [microservices](https://thenewstack.io/category/microservices/) traffic and manage external traffic coming into the network. The Gateway can handle millions of requests per second, making it well-suited for high-traffic scenarios. It also supports custom filters and has a flexible architecture. This enables developers to extend its functionality, and that’s exactly what Tetrate and Bloomberg are doing.

Their collaboration addresses the growing demand for efficiently integrating [large language models (LLMs)](https://thenewstack.io/what-is-a-large-language-model/) into enterprise applications. By expanding Envoy Gateway’s capabilities, the project will provide a community-led, open source solution for AI integration without vendor lock-in or commercial licensing restrictions.

The initial idea for this project arose when Dan Sun, engineering team lead for Bloomberg’s Cloud Native Compute Services and co-founder of the [KServe](https://github.com/kserve/kserve) project, came to the Envoy community and outlined his views of the problem space and a potential path forward for solving it. Tetrate, a major Envoy upstream contributor, stepped forward to express interest in helping Sun and Bloomberg turn their vision for the Envoy AI Gateway API into reality.

KServe provides a Kubernetes [Custom Resource Definition](https://kubernetes.io/docs/concepts/extend-kubernetes/api-extension/custom-resources/) for serving predictive and generative machine learning (ML) models. It aims to solve production model serving use cases by providing high abstraction interfaces for TensorFlow, XGBoost, ScikitLearn, PyTorch, and Huggingface Transformer/LLM models using standardized data plane protocols.

The key features of the new AI Gateway will include:

- Application traffic management for LLM providers with high-availability routing.
- LLM usage monitoring and control at various organizational levels.
- A unified interface for LLM requests with backend connectivity to multiple providers.
Envoy Gateway and KServe can be used together to allow traffic routing to both self-hosted and vendor-hosted LLMs. In this case, the AI gateway sits on top and routes open source LLM model traffic to self-hosted endpoints using KServe, while vendor-hosted model traffic is routed to AWS Bedrock or similar cloud-based services.

Varun Talwar, founder of Tetrate, added in a statement, “Our collaboration with Bloomberg and the CNCF aims to design and deliver a community-led, fully open-source AI gateway, powered by the leading contender to replace legacy models for Kubernetes ingress. It’s a solution the market is asking for, and we’re excited to be part of the team of maintainers and contributors creating it.”

Bloomberg’s Cloud Native Compute Services’ engineering lead, Steven Bower, said, “As an ‘open source first’ company, Bloomberg believes in the power and collaborative nature of the open source community to develop webscale solutions, and that important difference makes this project a valuable alternative to other ongoing efforts.”

Chris Aniszczyk, CNCF’s CTO, praised the initiative as a testament to Envoy’s flexibility and the power of community collaboration in the cloud native ecosystem. “Bloomberg and Tetrate have done exactly what our community is designed to do: bring people and organizations together to solve a common problem. That they’re doing it with Envoy Gateway only validates the power and extensibility of the project.”

To learn more about the[ Envoy AI Gateway project, interested parties can join an upcoming webinar](https://community.cncf.io/events/details/cncf-cncf-online-programs-presents-cloud-native-live-enabling-ai-adoption-at-scale-the-ai-platform-with-envoy-ai-gateway/) hosted by the CNCF on Oct. 17, 2024. The panel discussion will feature engineers from Bloomberg and Tetrate. It will cover the project and topics such as enterprise AI adoption and the role of AI platforms.

Thus, it’s clear that Envoy Gateway will play a major role as companies integrate AI into their applications.

[
YOUTUBE.COM/THENEWSTACK
Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.
](https://youtube.com/thenewstack?sub_confirmation=1)