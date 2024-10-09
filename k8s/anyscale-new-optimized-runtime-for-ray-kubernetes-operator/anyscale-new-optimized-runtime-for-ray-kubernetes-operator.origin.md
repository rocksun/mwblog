# Anyscale: New Optimized Runtime for Ray, Kubernetes Operator
![Featued image for: Anyscale: New Optimized Runtime for Ray, Kubernetes Operator](https://cdn.thenewstack.io/media/2024/10/786be763-anyscale-new-optimized-runtime-for-ray-kubernetes-operator-2-1024x576.png)
[Anyscale](https://www.anyscale.com/), the fast-emerging company behind the open source AI compute engine [Ray](https://thenewstack.io/how-ray-a-distributed-ai-framework-helps-power-chatgpt/), revealed a list of new products and services at its annual user conference in San Francisco earlier this week.
Among them: An optimized Ray runtime, created in response to customer feedback, and a Kubernetes operator.

The three-day [Ray Summit](https://raysummit.anyscale.com/flow/anyscale/raysummit2024/landing/page/eventsite) event, which ended Thursday and attracted nearly 1,500 developers, also brought together leading experts from [OpenAI](https://thenewstack.io/openais-realtime-api-takes-a-bow/), [a16z](https://a16z.com/), [Meta](https://about.meta.com/?utm_content=inline+mention), and [Runway](https://runwayml.com/), among others, to discuss the latest innovations in the development of AI at scale.

[Ray](https://www.anyscale.com/ray-open-source) is a unified AI development platform that enterprises deploy to scale their [AI and machine learning workloads](https://thenewstack.io/ai-engineering/) across any infrastructure. The company claims that Ray enables developers to instantly scale applications from a laptop to the cloud without the cost or expertise of building complex infrastructure.
Current users of Anyscale’s Ray AI platform include [Airbnb](https://thenewstack.io/airbnb-builds-a-second-neural-network-to-diversify-listings/), [Instacart](https://thenewstack.io/instacart-speeds-ml-deployments-with-hybrid-mlops-platform/), [OpenAI](https://thenewstack.io/how-ray-a-distributed-ai-framework-helps-power-chatgpt/), Netflix, [Uber](https://thenewstack.io/how-uber-eats-uses-machine-learning-to-estimate-delivery-times/), [Canva](https://thenewstack.io/canva-launches-developer-platform-eyes-generative-ai-apps/), Pinterest, and Spotify.

Anyscale announced a slew of platform advancements, including an architectural rebuild that makes Ray GPU-native. This means it now enables high performance in inter-GPU communication for workloads such as distributed training and model serving.

The 5-year-old, San Francisco-based company also announced [RayTurbo](https://www.anyscale.com/blog/announcing-anyscale-rayturbo), an optimized Ray runtime meant to improve performance and efficiency for AI workloads. The company introduced the [Anyscale Operator for Kubernetes](https://www.anyscale.com/blog/announcing-anyscale-on-kubernetes-k8s), which enables users to optimize their AI workloads and [Kuberay API server](https://ray-project.github.io/kuberay/components/apiserver/) investments on the infrastructure they control.

Anyscale also updated its [Anyscale Governance Suite](https://www.anyscale.com/blog/enterprise-governance-observability), a set of observability tools designed to manage compute resources and control AI sprawl.

## Ray ‘Enables Any AI Workload’
“From Day One, we designed Ray for building and scaling AI applications,” [Ion Stoica](https://www.linkedin.com/in/ionstoica/), co-founder of Anyscale, told The New Stack. “By unifying infrastructure via a single, flexible framework, Ray has enabled any AI workload, from multimodal data processing to model training to model serving and beyond.”

RayTurbo, Stoica said, was created in response to comments from Ray users.

“One piece of feedback we’ve heard consistently is that our users need to maximize their resource utilization and minimize cost,” Stoica said. “Now, with RayTurbo, we’ve built on top of the industry’s de-facto standard AI compute engine to make it faster, more cost-effective and more reliable. RayTurbo is now available on the Anyscale platform to all our users.”

Other items unveiled at the conference included [Ray Data](https://docs.ray.io/en/latest/data/data.html), a library for processing unstructured data at scale, [new direct integrations connecting the Anyscale platform to Kubernetes](https://www.anyscale.com/blog/announcing-anyscale-on-kubernetes-k8s) for AI/ML development, and tools for enterprise governance and [observability](https://thenewstack.io/observability/).

## Access to Newly Supported Data Formats
With the general availability of Ray Data, the company said, all users will have access to newly supported data formats, including data lakehouse formats such as [Hudi](https://hudi.apache.org/), [Iceberg](https://thenewstack.io/apache-iceberg-a-different-table-design-for-big-data/) and [Delta Lake](https://thenewstack.io/delta-lake-a-layer-to-ensure-data-quality/).

“The flexibility of Ray makes it an ideal platform for developers to scale any AI/ML workload, no matter how complex and sophisticated it is,” Stoica said. “That’s why most major AI companies are using Ray. Now that we’ve rearchitected Ray to make it GPU-native, we’re able to provide even better performance for workloads like distributed training and model serving.”

Stoica put Anyscale, which competes with products such as [AWS](https://aws.amazon.com/?utm_content=inline+mention) [CodeWhisperer](https://thenewstack.io/developer-tool-integrations-with-ai-the-aws-approach/), ChatGPT, [Github Copilot](https://thenewstack.io/go-big-or-go-home-what-github-learned-building-copilot/) and [MetaGPT](https://www.deepwisdom.ai/), into a business context.

“I’m not sure people realize that Ray powers some of the largest and best-known tech companies in the world,” he said.

“For example, if you’re booking a stay on Airbnb, Ray supports those AI recommendations. Or ordering your groceries for mobile pick up on Instacart, Ray supports that. AI infrastructure is crucial to supporting these companies in improving their user experience, positively impacting millions of lives in the process.”

[
YOUTUBE.COM/THENEWSTACK
Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.
](https://youtube.com/thenewstack?sub_confirmation=1)