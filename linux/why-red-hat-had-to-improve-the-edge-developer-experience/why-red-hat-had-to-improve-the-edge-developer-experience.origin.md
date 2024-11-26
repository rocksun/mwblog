# Why Red Hat Had To Improve the Edge Developer Experience
![Featued image for: Why Red Hat Had To Improve the Edge Developer Experience](https://cdn.thenewstack.io/media/2024/11/cc739340-planet-volumes-bq1nbwrwzwe-unsplash-1024x585.jpg)
SALT LAKE CITY — [Red Hat](https://www.openshift.com/try?utm_content=inline+mention) has recognized the importance of enhancing the developer experience as it advances on multiple fronts for OpenShift and [RHEL](https://thenewstack.io/configure-multiple-websites-on-a-single-rhel-based-apache-host/). Notably, during the recent series of [KubeCon+CloudNativeCon](https://events.linuxfoundation.org/kubecon-cloudnativecon-north-america/) announcements here, the company introduced a new version of Red Hat Device Edge.

OpenShift AI supports Red Hat’s efforts to improve development processes as well.

Red Hat Device Edge began over five years ago. Described as an offshoot of Red Hat Enterprise Linux, it was designed to address the more specific needs of individual customers using [Kubernetes](https://thenewstack.io/kubernetes/).

Initially, the focus was on telcos leveraging Kubernetes for 5G and industrial applications. Over time, this scope has expanded to include deployments across various environments constituting edge deployments.

By using Red Hat Device Edge and running Kubernetes on the Edge, Red Hat provides a solution to reduce latency and deliver other features valued by operations teams for the underlying infrastructure. At the same time, as demonstrated by this release, the company continues to enhance the developer experience.

Red Hat Device Edge initially had the same core components as RHEL but with key differences. Instead of compiling hundreds or thousands of individual packages to form an operating system, a novel approach was adopted: This method involved creating point-in-time images, which are summaries of individual packages, forming the edge-focused operating system base for Red Hat Device Edge, according to Red Hat documentation.

This approach addressed several key requirements from customers and partners that Red Hat communicated:

- Images are immutable, ensuring deployment consistency and preventing unintended changes to deployed systems over time.
- Updates are delivered as deltas, minimizing bandwidth requirements for updates.
- Each image is independently bootable, enabling automatic health checks and standardizing rollback capabilities.
- A reduced base package set offers a compact and portable foundation tailored for low-power devices.
## Get Edgy
[Red Hat Device Edge](https://www.redhat.com/en/technologies/device-edge) combines RHEL with [MicroShift](https://www.redhat.com/en/topics/edge-computing/microshift). MicroShift acts as a lightweight Kubernetes-based solution derived from OpenShift, designed for minimal hardware typically found in edge environments, [Shobhan Lakkapragada,](https://www.linkedin.com/in/shobhan) Red Hat’s senior director of product management, said during a briefing. Low CPU and memory requirements characterize MicroShift, which still retains many benefits associated with OpenShift. [Ansible](https://thenewstack.io/red-hat-ansible-lightspeed-uses-ai-to-automate-infrastructure-management/) was also included in this solution to facilitate the management of edge environments. “This integrated platform is offered at an attractive price point for edge computing,” Lakkapragada said.
The launch of Red Hat Device Edge 4.17 during KubeCon+CloudNativeCon has two principal updates: Enhanced support for low-latency workloads and improvements to edge AI workload support, Lakkapragada said. A new build of Red Hat Device Edge, “pre-tuned and preconfigured for industrial control software,” is also being introduced, Lakkapragada said. This build supports industrial systems undergoing digital transformation, allowing modernization of industrial control stacks through this new configuration, Lakkapragada said.

AI support thus plays a key role in helping to improve Red Hat Device edge, especially for the developer. That said, Red Hat’s OpenShift AI is still “a relatively new product,” as [Jeff DeMoss,](https://www.linkedin.com/in/jeff-demoss/) product manager of AI at Red Hat, explained during the briefing while referencing OpenShift AI 2.15.

“We introduced it last year and are investing heavily in it. At a high level, it’s an AI platform that enables enterprises to create and deploy AI-enabled applications across hybrid cloud environments,” DeMoss said.

OpenShift AI supports both predictive AI and generative AI use cases, providing “a broad set of functionalities across the AI lifecycle,” DeMoss said. These include model development, training, serving, monitoring, and automation for AI workflows.

DeMoss explained that leveraging the capabilities provided by OpenShift AI and other Red Hat AI assets simplifies consumption. A significant aspect involves enabling developers to create applications efficiently. DeMoss highlighted the importance of ensuring developers can locate and utilize necessary assets, such as a corporate [LLM (large language model)](https://thenewstack.io/llm/) serving specific models. A clear process is required to catalog these resources in a centralized repository.

DeMoss described the Developer Hub as a portal that addresses this need. By centralizing documentation and resources, the Developer Hub eliminates the time developers would otherwise spend searching for information. This cataloging approach accelerates the adoption of AI tools within enterprises, aiding in the creation of applications and ensuring developers can efficiently access and use assets.

Looking ahead, DeMoss stated that future releases would integrate additional AI features into the product, enhancing productivity through AI-driven solutions. “With the 2.15 release, first, we are introducing a model registry that bridges model experimentation and production activities. The model registry acts as a central repository to manage versions, metadata, and model artifacts,” DeMoss said. “It enhances the overall MLOps workflow by enabling teams to collaborate on models and deploy them into production more efficiently. Additionally, it supports model governance by offering information on model versions, documentation, origins, datasets used, and evaluation metrics.”

As part of this feature, customers can create multiple registries within their organization, define permissions to control access at the user or group level and deploy models directly from the registry. This feature was developed within the Kubeflow open source project.

For model serving, users have access to the [vLLM](https://github.com/vllm-project/vllm) serving runtime, a popular open source runtime for serving LLMs. vLLM is a highly flexible runtime that supports most popular open source models available on Hugging Face, including Llama, Mixtrol, and Mistrol. It also offers numerous capabilities and optimizations to enhance performance when serving LLMs, according to Red Hat documentation. “In OpenShift AI, we integrate the most up-to-date version of vLLM, which supports the latest model architectures and multimodal models, such as vision-language models,” DeMoss said.

Developers should be able to rely on AI to create applications while the rest of the platform for Red Hat Device Edge or OpenShift abstracts away the infrastructure support.

“Developers are not required to spend time figuring out usage details or searching for documentation. All necessary information can be made available as part of a centralized catalog for AI assets,” Balaji Sivasubramanian said. “This approach accelerates enterprise journeys by enabling not only the creation of new applications but also simplifying the process of making these assets and applications accessible to developers.”

## The Hub
AI-enabled application development constitutes a large part of improvements to Red Hat Developer Hub. Red Hat Developer Hub provides templates and resources for organizations to begin their AI-assisted journey for developing edge applications or apps for other types of deployments on Kubernetes and containers.

Red Hat Developer Hub templates include:

- Audio-to-text application: An AI-enabled audio transcription application that allows users to upload an audio file to be transcribed.
- Chatbot application: An LLM-enabled chat application to create a bot that replies with AI-generated responses.
- Code generation application: An LLM-enabled code generation application for a specialized bot that helps with code-related queries.
- Object detection application: Enables developers to upload an image to identify and locate objects in the image.
- Retrieval-Augmented Generation (RAG) chatbot application: Enables developers to embed files containing relevant information to allow the model to provide more accurate responses.
Red Hat Developer Hub was created to pool together a number of tools and support for developers. If there is a corporate LLM (large language model) serving specific models, a defined process is needed to ensure developers can access and utilize these resources effectively, [Balaji Sivasubramanian,](https://www.linkedin.com/in/balajisiva) senior director of product management and developer tools, said during the briefing. Since all of these assets need to be cataloged in a central repository, “this is where the Developer Hub, a portal for developers, proves to be highly effective,” Sivasubramanian said.

“The Developer Hub eliminates the need for developers to spend time figuring out how to use the assets or searching for documentation. Everything can be consolidated and made easily accessible as part of a centralized catalog for AI assets,” Sivasubramanian said. “This approach significantly accelerates the journey for enterprises, not just in creating new applications but also in ensuring that developers know how to use all these assets and applications effectively. Looking ahead, there is even more to come. Future releases will incorporate additional AI features into the product, further enhancing productivity through AI-driven solutions.”

[
YOUTUBE.COM/THENEWSTACK
Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.
](https://youtube.com/thenewstack?sub_confirmation=1)