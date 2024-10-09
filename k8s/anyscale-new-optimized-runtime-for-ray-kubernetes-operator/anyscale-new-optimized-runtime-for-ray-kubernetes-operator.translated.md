# Anyscale: A New Optimized Runtime for Ray and Kubernetes Operator

![Anyscale: A New Optimized Runtime for Ray and Kubernetes Operator](https://cdn.thenewstack.io/media/2024/10/786be763-anyscale-new-optimized-runtime-for-ray-kubernetes-operator-2-1024x576.png)

[Anyscale](https://www.anyscale.com/), the company behind the rapid rise of the open-source AI computing engine [Ray](https://thenewstack.io/how-ray-a-distributed-ai-framework-helps-power-chatgpt/), announced a slew of new products and services at its annual user conference in San Francisco earlier this week.

Among them: an optimized Ray runtime and Kubernetes operator created in response to customer feedback.

The three-day [Ray Summit](https://raysummit.anyscale.com/flow/anyscale/raysummit2024/landing/page/eventsite) event, which concluded Thursday, drew nearly 1,500 developers and featured representatives from leading experts, including [OpenAI](https://thenewstack.io/openais-realtime-api-takes-a-bow/), [a16z](https://a16z.com/), [Meta](https://about.meta.com/?utm_content=inline+mention), and [Runway](https://runwayml.com/), who discussed the latest innovations in large-scale AI development.

[Ray](https://www.anyscale.com/ray-open-source) is a unified AI development platform that enterprises can deploy to scale their [AI and machine learning workloads](https://thenewstack.io/ai-engineering/) to any infrastructure. The company claims Ray enables developers to instantly scale applications from laptops to the cloud without the cost or expertise of building complex infrastructure.

Existing users of Anyscale’s Ray AI platform include [Airbnb](https://thenewstack.io/airbnb-builds-a-second-neural-network-to-diversify-listings/), [Instacart](https://thenewstack.io/instacart-speeds-ml-deployments-with-hybrid-mlops-platform/), [OpenAI](https://thenewstack.io/how-ray-a-distributed-ai-framework-helps-power-chatgpt/), Netflix, [Uber](https://thenewstack.io/how-uber-eats-uses-machine-learning-to-estimate-delivery-times/), [Canva](https://thenewstack.io/canva-launches-developer-platform-eyes-generative-ai-apps/), Pinterest, and Spotify.

Anyscale announced a series of platform improvements, including an architectural rebuild that makes Ray GPU-native. This means it is now capable of achieving high-performance inter-GPU communication in workloads such as distributed training and model serving.

The five-year-old San Francisco company also announced [RayTurbo](https://www.anyscale.com/blog/announcing-anyscale-rayturbo), an optimized Ray runtime designed to improve the performance and efficiency of AI workloads. The company launched the [Anyscale Kubernetes Operator](https://www.anyscale.com/blog/announcing-anyscale-on-kubernetes-k8s), which enables users to optimize their AI workloads and [Kuberay API server](https://ray-project.github.io/kuberay/components/apiserver/) investments on their controlled infrastructure.

Anyscale also updated its [Anyscale Governance Suite](https://www.anyscale.com/blog/enterprise-governance-observability), a suite of observability tools designed to manage compute resources and control AI sprawl.

## Ray “Supports Any AI Workload”

“From day one, we designed Ray to be used for building and scaling AI applications,” Anyscale co-founder [Ion Stoica](https://www.linkedin.com/in/ionstoica/) told The New Stack. “By unifying infrastructure with a single, flexible framework, Ray makes any AI workload possible, from multi-modal data processing to model training to model serving and beyond.”

Stoica said RayTurbo was created in response to feedback from Ray users.

“One of the pieces of feedback we’ve been hearing is that our users need to maximize their resource utilization and minimize their costs,” Stoica said. “Now, with RayTurbo, we’ve built on top of the industry’s de facto standard AI computing engine to make it faster, more cost-effective, and more reliable. RayTurbo is now available to all users on the Anyscale platform.”

Other announcements at the conference included [Ray Data](https://docs.ray.io/en/latest/data/data.html), a library for large-scale processing of unstructured data, [a new direct integration connecting the Anyscale platform to Kubernetes](https://www.anyscale.com/blog/announcing-anyscale-on-kubernetes-k8s) for AI/ML development, and tools for enterprise governance and [observability](https://thenewstack.io/observability/).

## Access to New Supported Data Formats

The company said that with the general availability of Ray Data, all users will be able to access newly supported data formats, including data lake formats such as [Hudi](https://hudi.apache.org/), [Iceberg](https://thenewstack.io/apache-iceberg-a-different-table-design-for-big-data/), and [Delta Lake](https://thenewstack.io/delta-lake-a-layer-to-ensure-data-quality/).
“Ray 的灵活性使其成为开发人员扩展任何 AI/ML 工作负载的理想平台，无论其多么复杂和精妙，”Stoica 说。“这就是为什么大多数主要的 AI 公司都在使用 Ray。现在我们已经重新架构了 Ray 以使其成为 GPU 原生，我们能够为分布式训练和模型服务等工作负载提供更好的性能。”

Stoica 将 Anyscale 放入了商业环境中，Anyscale 与 [AWS](https://aws.amazon.com/?utm_content=inline+mention) [CodeWhisperer](https://thenewstack.io/developer-tool-integrations-with-ai-the-aws-approach/), ChatGPT, [Github Copilot](https://thenewstack.io/go-big-or-go-home-what-github-learned-building-copilot/) 和 [MetaGPT](https://www.deepwisdom.ai/) 等产品竞争。

“我不确定人们是否意识到 Ray 为世界上一些最大、最知名的科技公司提供支持，”他说。

“例如，如果您在 Airbnb 上预订住宿，Ray 支持这些 AI 推荐。或者在 Instacart 上订购您的杂货以便在手机上取货，Ray 支持这一点。AI 基础设施对于支持这些公司改善用户体验至关重要，从而在过程中积极影响数百万人的生活。”

[YOUTUBE.COM/THENEWSTACK](https://youtube.com/thenewstack?sub_confirmation=1)
科技发展迅速，不要错过任何一集。订阅我们的 YouTube 频道以收看我们所有的播客、访谈、演示等。