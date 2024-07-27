# Jumpstart AI Workflows With Kubernetes AI Toolchain Operator
![Featued image for: Jumpstart AI Workflows With Kubernetes AI Toolchain Operator](https://cdn.thenewstack.io/media/2024/07/c4574198-tools-1024x576.jpg)
Generative AI is booming as industries and innovators look for ways to transform digital experiences. From AI chatbots to language translation tools, people are interacting with a common set of AI/ML models, known as language models in everyday scenarios. As a result, new language models have developed rapidly in size, performance and use cases in recent years.

As an application developer, you may want to integrate a high-performance model by simply making a REST call and pointing your app to an inferencing endpoint for options like Falcon, Mistral, Phi and other models. Just like that, you’ve unlocked the doors to the AI kingdom and all kinds of intelligent applications.

Open source language models are a cost-effective way to [experiment with AI](https://thenewstack.io/ai/), and [Kubernetes](https://thenewstack.io/primer-how-kubernetes-came-to-be-what-it-is-and-why-you-should-care/) has emerged as the open source platform best suited for scaling and automating AI/ML applications without compromising the security of user and company data.

“Let’s make Kubernetes the engine of AI transformation,” said Jorge Palma, Microsoft principal product manager lead. He gave the keynote at KubeCon Europe 2024, where AI use cases were discussed everywhere. Palma talked about the number of developers he’s met who are deploying models locally in their own infrastructure, putting them in containers and using Kubernetes clusters to host them.

“Container images are a great format for models. They’re easy to distribute,” Palma told KubeCon. “Then you can deploy them to Kubernetes and leverage all the nice primitives and abstractions that it gives you — for example, managing that heterogeneous infrastructure, and at scale.”

[Containers](https://thenewstack.io/containers/) also help you avoid the annoying “but it runs fine on my machine” issue. They’re portable, so your models run consistently across environments. They simplify version control to better maintain iterations of your model as you fine-tune for performance improvements. Containers provide resource isolation, so you can run different AI projects without mixing up components. And, of course, running containers in Kubernetes clusters makes it easy to scale out — a crucial factor when working with large models.
“If you aren’t going to use Kubernetes, what are you going to do?” asked Ishaan Sehgal, a Microsoft software engineer. He is a contributor to the Kubernetes AI Toolchain Operator (KAITO) project and has helped develop its major components to simplify AI deployment on a given cluster. KAITO is a Kubernetes operator and open source project developed at Microsoft that runs in your cluster and automates the deployment of large AI models.

As Sehgal pointed out, [Kubernetes gives you the scale and resiliency you need](https://thenewstack.io/why-kubernetes-needs-to-be-dumbed-down-for-devops/) when running AI workloads. Otherwise, if a virtual machine (VM) fails or your inferencing endpoint goes down, you must attach another node and set everything up again. “The resiliency aspect, the data management — Kubernetes is great for running AI workloads, for those reasons,” he said.

## Kubernetes Makes It Easier, KAITO Takes It Further
Kubernetes makes it easier to scale out AI models, but it’s not exactly easy. In my article “[Bring your AI/ML workloads to Kubernetes and leverage KAITO](https://vmblog.com/archive/2024/03/05/bring-your-ai-ml-workloads-to-kubernetes-and-leverage-the-kubernetes-ai-toolchain-operator-kaito.aspx),” I highlight some of the hurdles that developers face with this process. For example, just getting started is complicated. Without prior experience, you might need several weeks to correctly set up your environment. Downloading and storing the large model weights, upwards of 200 GB in size, is just the beginning. There are storage and loading time requirements for model files. Then you need to efficiently containerize your models and host them — choosing the right GPU size for your model while keeping costs in mind. And there are troubleshooting pesky quota limits on compute hardware.

Using KAITO, a workflow that previously could span weeks now takes only minutes. This tool streamlines the tedious details of deploying, scaling, and managing AI workloads on Kubernetes, so you can focus on other aspects of the ML life cycle. You can choose from a range of popular open source models or onboard your custom option, and KAITO tunes the deployment parameters and automatically provisions GPU nodes for you. Today, KAITO supports [five model families and over 10 containerized models](https://github.com/Azure/kaito/tree/main/presets), ranging from small to large language models.

For an ML engineer like Sehgal, KAITO overcomes the hassle of managing different tools, add-ons and versions. You get a simple, declarative interface “that encapsulates all the requirements you need for running your inferencing model. Everything gets set up,” he explained.

## How KAITO Works
Using KAITO is a two-step process. First, install KAITO on your cluster, and then select a preset that encapsulates all the requirements needed for inference with your model. Within the associated workspace custom resource definition (CRD), a minimum GPU size is recommended so you don’t have to search for the ideal hardware. You can always customize the CRD to your needs. After deploying the workspace, KAITO uses the node provisioner controller to automate the rest.

“KAITO is basically going to provision GPU nodes and add them to your cluster on your behalf,” explained Microsoft senior cloud evangelist Paul Yu. “As a user, I just have to deploy my workspace into the AKS cluster, and that creates the additional CR.”

As shown in the following KAITO architecture, the workspace invokes a provisioner to create and configure the right-sized infrastructure for you, and it even distributes your workload across smaller GPU nodes to reduce costs. The project uses open source [Karpenter](https://karpenter.sh/) APIs for the VM configuration based on your requested size, installing the right drivers and device plug-ins for Kubernetes.

For applications with compliance requirements, KAITO provides granular control over data security and privacy. You can ensure that models are ring-fenced within your organization’s network and that your data never leaves the Kubernetes cluster.

Check out this tutorial on how to [bring your own AI models to intelligent apps on Azure Kubernetes Service](https://aka.ms/kaito-live), where Sehgal and Yu integrate KAITO in a common e-commerce application in a matter of minutes.

## Working With Managed Kubernetes
Currently, you can use KAITO to provision GPUs on Azure, but the project is evolving quickly. The [roadmap](https://github.com/orgs/Azure/projects/669) includes support for other managed Kubernetes providers. When you use a managed Kubernetes service, you can interact with other services from that cloud platform more easily to add capabilities to your workflow or applications.

Earlier this year, [at Microsoft Build 2024, BMW talked about its use of generative AI](https://build.microsoft.com/sessions/812d376f-56fe-411b-a10c-1faa3c1d80c9?source=sessions) and Azure OpenAI Service in the company’s connected car app, My BMW, which runs on AKS.

Brendan Burns, co-founder of the Kubernetes [open source project](https://thenewstack.io/open-source-project-momentum-what-it-takes/), introduced the demo. “What we’re seeing is, as people are using Azure OpenAI Service, they’re building the rest of the application on top of AKS,” he told the audience. “But, of course, just using OpenAI Service isn’t the only thing you might want to use. There are a lot of reasons why you might want to use open source large language models, including situations like data and security compliance, and fine-tuning what you want to do. Maybe there’s just a model out there that’s better suited to your task. But doing this inside of AKS can be tricky so we integrated the Kubernetes AI Toolchain Operator as an open source project.”

## Make Your Language Models Smarter with KAITO
Open-source language models are trained on extensive amounts of text from a variety of sources, so the output for domain-specific prompts may not always meet your needs. Take the pet store application, for example. If a customer asks the integrated pre-trained model for dog food recommendations, it might give different pricing options across a few popular dog breeds. This is informative but not necessarily useful as the customer shops. After fine-tuning the [model on historical data](https://thenewstack.io/automating-context-in-structured-data-for-llms/) from the pet store, the recommendations can instead be tailored to well-reviewed, affordable options available in the store.

As a step in your ML lifecycle, fine-tuning helps customize open source models to your own data and use cases. The latest release of KAITO, v0.3.0, supports fine-tuning, and inference with adapters and a broader range of models. You can simply define your tuning method and data source in a KAITO workspace CR and see your intelligent app become more context-aware while maintaining data security and compliance requirements in your cluster.

To stay up to date on the project roadmap and test these new features, check out [KAITO on GitHub](https://github.com/Azure/kaito).

[
YOUTUBE.COM/THENEWSTACK
Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.
](https://youtube.com/thenewstack?sub_confirmation=1)