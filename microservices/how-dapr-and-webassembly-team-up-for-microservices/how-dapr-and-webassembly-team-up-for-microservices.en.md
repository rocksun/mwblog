[Dapr](https://dapr.io/)’s distributed application runtime concept is simple, but enabling it is enormously complex (although its usage is simple).

According to the project’s documentation, Dapr is designed to be portable and an event-driven runtime that’s geared for developers who are building stateless and stateful applications for the cloud edge, while using the languages and frameworks of their choice. It is designed to codify the best practices for building [microservice applications](https://thenewstack.io/introduction-to-microservices/) into open, independent [APIs](https://thenewstack.io/what-is-api-management/) called building blocks.

## Dapr 1.16

The [Dapr 1.16](https://blog.dapr.io/posts/2025/09/16/dapr-v1.16-is-now-available/) release’s best bits are the multi-app workflow feature. It allows developers to specify which applications should execute specific workflow activities, [Marc Duiker](https://www.linkedin.com/in/mduiker/?originalSubdomain=nl), senior developer advocate at [Diagrid](https://www.diagrid.io/) told me. This is important in case an activity requires specific hardware, like a GPU, or when it should be run in a specific geolocation, he said.

“In addition, I believe the federated identity support for Dapr is very important in building secure applications,” Duiker, “Using a robust open source standard as [SPIFFE](https://spiffe.io/) [Secure Production Identity Framework For Everyone] is a great addition that many enterprises will welcome, since it’s compatible with all major cloud service providers.”

Dapr has become a favorite among operations teams due to its proven feasibility for distributed systems, including Kubernetes. Among its most appreciated features are robust security mechanisms for enforcing zero-trust policies and its ability to integrate seamlessly across entire infrastructures. Development teams, in particular, often highlight its simple and user-friendly APIs, which are especially helpful in [Kubernetes](https://thenewstack.io/kubernetes/) environments. Instead of requiring developers to master complex Kubernetes concepts, commands, and infrastructure setup, Dapr allows them to focus on creating problem-solving logic while the runtime handles infrastructure concerns.

## CNCF Graduation

Recently, the Microsoft-led Dapr project achieved several significant milestones, including its graduation from the [CNCF](https://cncf.io/?utm_content=inline+mention) (Cloud Native Computing Foundation). This announcement was made during [KubeCon Europe](https://events.linuxfoundation.org/kubecon-cloudnativecon-europe/) earlier this year. At the event, talks highlighted Dapr’s adaptation to the growing use of [WebAssembly (Wasm)](https://thenewstack.io/webassembly/). In Kubernetes environments, this enables organizations to leverage Wasm’s extended security features, ultra-low latency, and other attributes that contribute to its increasing adoption.

The [CNCF graduation](https://thenewstack.io/dapr-graduates-cncf-and-connects-to-webassembly/) is a significant milestone in its own right, underpinned by recent statistics showing the growing acceptance and usage of Dapr across the developer and operations communities. (The specific stats were not provided but would underscore this progress.)

The project was first released in 2019 at Microsoft and was accepted into the CNCF Incubator in November 2021. Since then, Dapr has grown to over 3,700 individual contributors from more than 400 organizations. It is used by tens of thousands of organizations, including Grafana, FICO, HDFC Bank, SharperImage and Zeiss and more. Today, it is maintained by 21 individuals affiliated with eight organizations who have released regular versions every quarter with many new developer APIs, including workflows, secrets, cryptography, configuration management, and LLMs. Together, the Dapr SDKs have over 70 million downloads, with 50 million image pulls, the CNCF said in a statement.

## Delivering the Best Developer Experience

Projects in which Dapr integrates include [OpenTelemetry](https://thenewstack.io/what-is-opentelemetry/) for [observability](https://thenewstack.io/introduction-to-observability/) data, Prometheus for metrics, SPIFFE for identifying and securing services, [gRPC](https://thenewstack.io/grpc-a-deep-dive-into-the-communication-pattern/) and Cloud Events for sending communications between application services. The Dapr control plane, which, among other capabilities, deploys Dapr sidecars for each application, is hosted on Kubernetes and is deployed with Helm charts.

During the demo talk at KubeCon+CloudNativeCon “Next-Level Powers: Enhance Your IDP with the WASM and Dapr Hero Team-Up!,” [Engin Diri,](https://github.com/dirien) senior solutions architect, Pulumi, showed how using WebAssembly provider Fermyon’s open source SpinKube and Dapr, with KEDA (Kubernetes Event-driven Autoscaling), can be used to deliver “the best developer experience and possibilities,” Diri said. “Let’s take SpinKube to the next level and ask ourselves: how can we help developers be even more productive and think less about everything surrounding them?” Diri said. “If you’re not familiar, this concept is inspired by the French Revolution’s ‘Triumvirate.’ In our case, I’ve created the SpinKube Triumvirate: Dapr, KEDA, and SpinKube. Here’s why I think Dapr, KEDA, and SpinKube form the perfect trio.”

As described above, Dapr provides an abstraction for infrastructure so developers can focus entirely on creating applications. With Dapr, a sidecar mechanism is automatically injected into a deployment by the Dapr operator, Diri explained during his talk. He showed how developers only need to know that there is a component of type Pub/Sub. They do not need to know if it’s Kafka, RabbitMQ, or something else, Diri said. Dapr provides an SDK or API to communicate within the application, eliminating unnecessary complexity, Diri said.

Dapr is built on the actor model, which makes it easier to structure code based on communication patterns (i.e., who communicates with whom), Diri said. This abstraction is extremely helpful. Dapr also consists of multiple building blocks, such as state management, Pub/Sub, security and observability. Developers don’t need to worry about the underlying implementation of these components — it could be RabbitMQ, Kafka or another service. The modular components can be easily implemented, with examples like Key Vault, [AWS](https://aws.amazon.com/?utm_content=inline+mention) Secret Manager, or HashiCorp Vault for secret management. “As a developer, I don’t need to think about these complexities,” Diri said.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://cdn.thenewstack.io/media/2020/04/4d3b9442-bruce-gain.jpg)

BC Gain is founder and principal analyst for ReveCom Media. His obsession with computers began when he hacked a Space Invaders console to play all day for 25 cents at the local video arcade in the early 1980s. He then...

Read more from B. Cameron Gain](https://thenewstack.io/author/bruce-gain/)