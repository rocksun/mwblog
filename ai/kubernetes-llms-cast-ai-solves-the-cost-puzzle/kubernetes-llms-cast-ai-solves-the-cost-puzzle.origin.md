# Kubernetes + LLMs: Cast AI Solves the Cost Puzzle
![Featued image for: Kubernetes + LLMs: Cast AI Solves the Cost Puzzle](https://cdn.thenewstack.io/media/2024/11/f651b0cb-alex-shuper-4kexemmkesw-unsplash-1-1024x683.jpg)
[Cast AI](https://thenewstack.io/devfinops-and-ai-to-provision-exactly-the-right-cloud-spend/) came onto the scene several years ago with an automation platform for managing the operations and costs of [Kubernetes](https://thenewstack.io/kubernetes/). Given the symbiotic relationship between Kubernetes and AI, it’s not surprising that the five-year-old startup is also helping organizations and their developers manage the costs of their AI operations.
The Miami, Florida-based company wasn’t a newbie to AI; its Kubernetes platform is powered by machine learning algorithms. The rapid emergence of generative open up another avenue for Cast AI. The vendor in April launched its AI Optimizer service that automatically cuts the cost of deploying [large language models (LLMs)](https://thenewstack.io/llm/) by integrating with any OpenAI-compatible API endpoint and identifying the LLM — commercial and open source — that provides the best performance for the lowest inference cost.

Cast AI also has its Playground interactive testingtool, which lets developers compare the performance and cost of LLMs and then customize configurations without having to adjust the code.

At the recent [KubeCon + CloudNative North America](https://events.linuxfoundation.org/kubecon-cloudnativecon-north-america/) show, Cast AI rolled out AI Enabler, the productization of Playground that leverages [the vendor’s Kubernetes infrastructure optimization capabilities](https://thenewstack.io/automating-the-security-of-kubernetes-clusters-in-the-cloud/) to intelligently routes queries from organizations and DevOps folks to the optimal most cost-efficient LLM — again, commercial or open source — for the task that they’re running.

[Laurent Gil](https://www.linkedin.com/in/laurentgil/), co-founder and chief product officer at Cast AI, told The New Stack, using the tool’s initial name, that “Playground gives teams the power to demystify LLM performance and costs. It’s no longer about guesswork. Users can directly benchmark models, understand their trade-offs, and make data-driven decisions for their specific workloads, all without writing a single line of code.”
## Costly LLMs
Cast AI’s various tools — including AI Optimizer and now AI Enabler (nee Playground) — are aimed at helping developers get their arms around a generative AI space that is seeing the number of LLMs and the costs to run them grow rapidly. In a [blog post](https://cast.ai/blog/llm-cost-optimization-how-to-run-gen-ai-apps-cost-efficiently/), [Giri Radhakrishnan](https://www.linkedin.com/in/giriradhakrishnan/), the company’s director of product marketing, noted that the [pricing page](https://openai.com/api/pricing/) for OpenAI’s LLM models is 10 pages long, with at least 20 different models for varying use cases and pricing models.

Given that, it makes sense that developers and [AIOps](https://thenewstack.io/supercharge-aiops-efficiency-with-llms/) teams that already are pinched for time struggle to determine which model is best for their specific needs, which typically has been a manual job, Radhakrishnan wrote in a blog post. Then there’s the cost of running the LLMs, which need expensive components like Nvidia GPUs and eat a lot of energy. According to [International Energy Agency](https://www.iea.org/), a ChatGPT query [consumes 10 times more electricity](https://www.goldmansachs.com/insights/articles/AI-poised-to-drive-160-increase-in-power-demand) than a Google search.

The costs can mount. [Gad Benram](https://www.linkedin.com/in/gad-benram/), founder of two-year-old AI consultancy [TensorOps](https://www.tensorops.ai/), wrote in a blog post about how quickly the costs surrounding LLMs can grow. Benram noted that while LLMs have been foundational to generative AI since [ChatGPT was released two years ago](https://thenewstack.io/how-to-create-software-diagrams-with-chatgpt-and-claude/), cost has been a barrier to organizations realizing their potential.

“The expense of incorporating LLMs into your applications can range from a few cents for on-demand use cases to upwards of $20,000 per month for hosting a single instance of an LLM in your cloud environment,” Benram wrote. “Additionally, there are substantial costs associated with fine-tuning, training, vector search, and scaling.”

## Getting a Hold on Costs
Reining in these costs can make it possible for DevOps teams to take full advantage of what LLMs can do, according to Cast AI’s Radhakrishnan.

“Some teams may not realize that using the default LLM or relying on a single provider might not be the best choice for all of their use cases,” he wrote. “As a result, they often use more resource-intensive and expensive models than necessary. They miss out on more efficient, cost-effective solutions without exploring other options or tailoring models to specific needs. This can lead to unnecessary spending and inefficient resource use.”

While DevOps and MLOps teams responsible for building and maintaining the infrastructure for generative AI workloads don’t have the transparency they need into the costs in compute resources, API calls, or data use, going to the cloud isn’t any better, with hundreds of compute instances — with different configurations, performance, and pricing — to consider. Automation is key, according to Radhakrishnan.

## Dashboards and Playground
AI Enabler includes a dashboard for monitoring costs and creates a report comparing the expenses of using a default LLM with those for leveraging other models. The dashboard aggregates data from a range of LLM providers to give a clearer picture of the cost of each LLM. The tool also automatically selects the optimal LLMs without requiring additional configuration.

“The LLM proxy intelligently selects the most optimal LLM model for user queries, ensuring that organizations get the best performance at the lowest cost,” he wrote. “This approach delivers maximum savings by choosing and executing an optimized LLM with lower inference expenses.”

It fits well with the vendor’s AI Enabler, which compares LLMs and creates benchmarks that developers can use to develop the best configuration for their needs and make better decisions that will optimize the LLM best suited for performance and cost.

Using AI Enabler, DevOps teams can explore their options by creating scenarios that compare the LLMs, providers, and responses, test routing behavior and visualize routing decisions, and configure and tune routing parameters.

“With the Cast AI Playground, we’re putting control back in the hands of businesses,” Gil said. “By allowing teams to compare LLMs side-by-side for both performance and cost, we’re helping them unlock the full potential of AI while ensuring every dollar is well spent.”

## Migrating Workloads in Kubernetes
Also at the show, Cast AI launched its Commercially Supported Container Live Migration feature that enables automatic and uninterrupted migration of stateful and uninterruptible workloads — think databases like MySQL, [PostgreSQL](https://thenewstack.io/charles-schwab-adopts-postgresql-with-vmware-tanzu/), or NoSQL databases such as MongoDB, and AI applications — in Kubernetes. The tool will enable organizations to ensure continuous uptime, create more efficient operations, and reduce infrastructure costs.

“Stateful workloads can’t simply be stopped and restarted without risking data loss or interruption,” Radhakrishnan wrote. “This is why Kubernetes’ initial promise to simplify infrastructure for all workloads [failed to meet the needs](https://cast.ai/blog/how-to-migrate-stateful-workloads-on-kubernetes-with-zero-downtime/?_gl=1*1eacdrj*_up*MQ..*_ga*ODkxMTI4Njg4LjE3MzE5NTAxNDU.*_ga_YLDVPHF0WD*MTczMTk1MDE0NC4xLjAuMTczMTk1MDE0NC4wLjAuMA..) of complex, data-driven applications.”

Cast AI is integrating the new feature with its other automation tools, including Bin-Packing and Eviction, Cluster and Node Rebalancing, Spot Fallback, Spot Interruption ML Prediction, and Spot Instance Price Drift Rebalancing.

“Organizations running resource-intensive, stateful applications cannot afford downtime,” he wrote. “Since there is no widely adopted, commercial solution to move these sensitive workloads to cost-efficient resources, they end up running in underutilized and expensive nodes.”

With Container Live Migration, organizations can automatically move these workloads into fewer optimized nodes. This ensures the maximum utilization of resources and the selection of instances that best suit their needs, all of which reduce costs.

[
YOUTUBE.COM/THENEWSTACK
Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.
](https://youtube.com/thenewstack?sub_confirmation=1)