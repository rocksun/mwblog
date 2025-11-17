ATLANTA — [Knative](https://knative.dev/), the open source [Kubernetes](https://thenewstack.io/kubernetes/)-native platform for building, deploying and running serverless and event-driven applications, has [officially graduated](https://www.cncf.io/announcements/2025/10/08/cloud-native-computing-foundation-announces-knatives-graduation/) from the [Cloud Native Computing Foundation (CNCF)](https://cncf.io/?utm_content=inline+mention). It took over seven years, but it’s finally here.

Everyone agrees that Knative’s goal — to simplify the deployment and management of modern workloads on Kubernetes by abstracting away infrastructure complexities such as autoscaling, routing and event delivery — is a good one. This allows developers to focus on business logic and application architecture, rather than getting lost in the weeds of Kubernetes’ intricacies.

As [Evan Anderson](https://www.linkedin.com/in/evankanderson/), Knative’s co-founder, said in the press release when Knative was released, “Knative fills several gaps in the cloud native ecosystem as an easy on-ramp to Kubernetes, with Knative’s eventing acting as the missing skeleton for connecting events to reactions.”

## Serving and Eventing

Specifically, Knative’s core components, Serving and Eventing, enable developers to deploy containerized applications that automatically scale to zero when not in use, reducing infrastructure costs and improving efficiency. Eventing provides a unified way to connect applications through events, making it easier to build event-driven architectures. Knative integrates with the [CloudEvents specification](https://cloudevents.io/) and supports cloud native [Buildpacks](https://buildpacks.io/) and [Tekton](https://tekton.dev/), the open source framework for creating [CI/CD](https://thenewstack.io/introduction-to-ci-cd/) pipelines.

In addition, Eventing now integrates with [Apache Camel Kamelets](https://camel.apache.org/camel-k/2.8.x/kamelets/kamelets.html) — bringing new event sources into the ecosystem. For Serving, Knative is adopting the [Kubernetes Gateway API](https://gateway-api.sigs.k8s.io/) to simplify the networking stack and is introducing safer container settings as a default to increase security posture. The project has also switched from [OpenCensus](https://opencensus.io/) to the far more popular [OpenTelemetry](https://opentelemetry.io/) for metrics and tracing.

Major cloud providers and enterprises, including Alibaba Cloud, Scaleway and Gojek, have already adopted Knative to power their serverless functions, AI inference models and scalable automation platforms. The platform’s ability to handle diverse workloads, from AI to finance, has also made it an attractive choice.

As [Chris Aniszczyk](https://www.linkedin.com/in/caniszczyk/), CNCF’s CTO, said at KubeCon here that “Knative’s graduation reflects the maturity of serverless technology in the Kubernetes and CNCF ecosystem. Knative has built a strong contributor base, gained trust from end users, and continues to evolve with integrations that address needs, from newer AI workloads to interoperability.”

Thinking of AI, [Red Hat](https://www.openshift.com/try?utm_content=inline+mention) in particular has been working on how to use [Knative Functions](https://knative.dev/docs/functions/) with [Llama Stack](https://github.com/llamastack/llama-stack), an open source framework for [building generative AI (GenAI) applications](https://knative.dev/blog/articles/ai_functions_llama_stack/). Red Hat has also had its hands in integrating [large language models (LLMs) as agents with Knative](https://knative.dev/blog/articles/llm-agents-overview/). Finally, Red Hat is also developing [sophisticated systems of AI agents using Knative](https://knative.dev/blog/articles/knative-eventing-eda-agents/).

## More Serious Competition

Several people at KubeCon, who didn’t want to be quoted, told me that they expect, with CNCF’s blessing, for Knative to be seen as a much more serious rival to [AWS](https://aws.amazon.com/?utm_content=inline+mention) [Lambda](https://aws.amazon.com/lambda/) and [Azure Functions](https://azure.microsoft.com/en-us/products/functions). While there are [significant differences in architecture, use cases and operational philosophy](https://developers.redhat.com/articles/2023/10/19/knative-versus-aws-lambda-and-azure-functions), they all provide serverless and event-driven capabilities that allow developers to run code with automatic scaling and without managing underlying server resources.

And, of course, [AWS](https://aws.amazon.com/?utm_content=inline+mention) Lambda and Azure Functions are closely tied to their respective cloud infrastructures, while Knative is an open source project that runs on top of Kubernetes. This means companies using Knative can be vendor-neutral. It also gives them the ability to run serverless workloads anywhere Kubernetes runs, including multicloud or on-premises environments.

Will this be enough to propel Knative to what [Market Intelo](https://marketintelo.com/) predicts will be a [$3.2 billion market by 2033](https://marketintelo.com/report/managed-knative-services-market), while growing at a robust compound annual growth rate (CAGR) of 24.8%? Stay tuned. We’ll soon see.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://cdn.thenewstack.io/media/2023/03/cee63948-cropped-8a0b5c52-steven-vaughan-nichols.jpg)

Steven J. Vaughan-Nichols, aka sjvn, has been writing about technology and the business of technology since CP/M-80 was the cutting-edge PC operating system, 300bps was a fast internet connection, WordStar was the state-of-the-art word processor, and we liked it.

Read more from Steven J. Vaughan-Nichols](https://thenewstack.io/author/sjvn/)