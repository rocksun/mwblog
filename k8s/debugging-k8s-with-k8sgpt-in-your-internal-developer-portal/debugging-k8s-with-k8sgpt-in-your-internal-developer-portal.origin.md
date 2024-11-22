# Debugging K8s With K8sGPT in Your Internal Developer Portal
![Featued image for: Debugging K8s With K8sGPT in Your Internal Developer Portal](https://cdn.thenewstack.io/media/2024/11/5ddf2e1f-debugging-kubernetes-ai-1024x576.png)
Quickly identifying and resolving issues is a constant challenge for [DevOps](https://www.getport.io/blog/streamlining-devops-with-workflows) and [site reliability engineering (SRE)](https://thenewstack.io/sre-vs-platform-engineer-cant-we-all-just-get-along/) teams, who often find themselves navigating a complex web of commands, logs and dashboards that is unique to each problem. This fragmented approach delays resolutions, and developers frequently report that they spend nearly 40% of their time just troubleshooting — which also opens software environments to risk of human error.

[Platform engineering](https://www.getport.io/glossary/platform-engineering) emerged as a way to overcome this DevOps complexity, and at the heart of platform engineering is the internal developer portal. An internal developer portal streamlines incident response, reduces manual toil and empowers DevOps teams to resolve issues faster. It offers a unified space for managing infrastructure, code repositories and deployments.
Portals also centralize all the data related to your software development life cycle (SDLC) in one, accessible place. Integrating AI into your portal can help you proactively identify potential system degradations and provide instant guidance on remediation, which can sometimes cut your average incident resolution time by 50%.

In this article, I’ll walk you through how to accelerate issue resolution using AI to enrich portal data and how to display the enriched data within the portal to reduce time-to-resolution.

## Using K8sGPT to Enrich Portal Data
[K8sGPT](https://github.com/k8sgpt-ai/k8sgpt) is an AI agent specifically designed for [Kubernetes](https://www.getport.io/blog/simplify-kubernetes) (K8s) environments. It surfaces actionable insights from historical data, providing quick recommendations that significantly reduce resolution times. By pinpointing anomalies or misconfigurations and offering intelligent solutions, K8sGPT transforms traditionally reactive processes into proactive ones. Plus, by tightly integrating with your portal, these insights are presented in a single pane of glass that is fully aligned with your operational workflows.
While this example will focus on Kubernetes only, AI can assist across multiple domains in more advanced scenarios, such as cloud infrastructure, where issues often span different layers of the stack. Our goal is not just to equip AI to handle multiple domains but to empower it to fully automate the remediation process, resolving issues independently.

In the context of an [internal developer portal](https://thenewstack.io/improve-developer-onboarding-with-an-internal-developer-portal), you can use K8sGPT to gather data from all of your workflows across your entire SDLC and draw insights from them. With that vision in mind, let’s start with small steps and explore how a single-domain workflow can improve efficiency.

## Deploying an Automatic AI Enrichment Process
Say you want to create an automated workflow to enrich your internal developer portal with a real-time view of failing [Kubernetes workloads](https://thenewstack.io/kubernetes/). This workflow involves several key components that, working together, will use AI to create an automated process that helps use your portal to solve observed issues in K8s.

These components are:

**Kubernetes (K8s) cluster**: This represents your workload infrastructure. There are multiple ways to deploy Kubernetes clusters, and the most common are Platform as a Service (PaaS) such as[Amazon](https://aws.amazon.com/?utm_content=inline+mention)EKS,[Microsoft](https://news.microsoft.com/?utm_content=inline+mention)AKS and[Google](https://cloud.google.com/?utm_content=inline+mention)GKE. Whatever you’re using, there should also be an[integration](https://docs.getport.io/integrations-index/#kubernetes)between the cluster and the portal in order to have both the listing of the workloads and their health status.This is where all the data about your Kubernetes cluster is centralized and can be correlated and refined. This will provide easy access to deployments data and AI insights on how to solve unhealthy Kubernetes workloads. I’ll be using[Internal developer portal:](https://www.getport.io/blog/what-is-an-internal-developer-portal)[Port](https://www.getport.io/?utm_content=inline+mention)for this example.**K8sGPT**: This is the main AI “consultant.” It is in charge of issuing commands against the K8s API to both collect data and communicate back and forth with an AI large language model (LLM) that provides insights.- K8sGPT can be deployed both outside and in the cluster. To deploy the K8sGPT REST API server,
[follow the installation guide](https://docs.k8sgpt.ai/getting-started/installation/). - Use this command to serve the REST API:
`k8sgpt serve --http`
. - To deploy the in-cluster K8sGPT,
[follow the installation guide](https://docs.k8sgpt.ai/getting-started/in-cluster-operator/).
- K8sGPT can be deployed both outside and in the cluster. To deploy the K8sGPT REST API server,
**Communication facilitator**: The communication facilitator is crucial for bridging the gap between the portal and K8sGPT. It ensures that commands, queries and insights flow seamlessly between these systems. Depending on your organization’s security and compliance requirements, you can use:[Kafka](https://thenewstack.io/top-10-tools-for-kafka-engineers/)topics, which is what this example uses. This means that when a workload is recognized as failing, a message will be created in a Kafka topic. The communication facilitator (in this case, a[Python](https://thenewstack.io/what-is-python/)script) will handle checking the topics and consuming messages in a`PULL`
-based direction.- Another approach is to just have the script constantly check locally for the health of workloads and enrich that check with AI insights when workloads fail.
**AI LLM**: The core intelligence behind K8sGPT leverages natural language processing to interpret Kubernetes data and provide actionable recommendations.
Note that K8sGPT currently supports [11 different types of AI backends](https://docs.k8sgpt.ai/reference/providers/backend/). I have tested it with [Ollama](https://docs.k8sgpt.ai/reference/providers/backend/#ollama); you can also [download a model](https://ollama.com/library). Check out these guides for [using an OpenAI API token](https://platform.openai.com/docs/quickstart) and [deploying an on-premises LLM using Ollama](https://github.com/ollama/ollama) to help.

Once deployed, you can configure K8sGPT to [use Ollama](https://thenewstack.io/how-to-set-up-and-run-a-local-llm-with-ollama-and-llama-2/) like so:

1 |
k8sgpt serve --http -b openai |
## Understanding the Flow of Events
Take a look at the diagram below to better understand how to enable a fully automated flow of events to serve AI insights. The numbers beside each element in the tech stack correspond with an explanation of how they are involved in the flow:

![Automated event flow described below](https://cdn.thenewstack.io/media/2024/11/515348e9-event-flow-ai-insights-1024x536.png)
(Source: Port)

- A K8s integration updates the portal with the health status of a workload.
- An automated workflow issues a message to a Kafka topic.
[Python](https://roadmap.sh/python)script picks up the topic message data.- Python script polls K8sGPT for insights.
- K8sGPT communicates with the K8s cluster and LLM.
- K8sGPT replies to the Python script with insights.
- Python script leverages the portal API — in this case, Port — to populate the Kubernetes workload entity with insights on how to fix the issue.
## Configuring the Automated Workflow in the Portal
Now it’s time to configure the portal to facilitate the automated workflow. First things first: Make room for AI insights data as part of the Kubernetes workload dashboard. Add a Port Insights property to your workload blueprint:

![A JSON representation of the K8s workload blueprint in data mode](https://cdn.thenewstack.io/media/2024/11/9e9c3096-insights-property-1024x737.png)
A JSON representation of the K8s workload blueprint in data mode (see this [JSON code](https://github.com/dan-amzulescu-port/Port-K8sGPT/blob/main/PortObjects/Blueprints/workload.json) in GitHub).

Next, define a workflow that will automatically notify your communication facilitator of an unhealthy workload. You need to select the data point that will trigger the [workflow automation](https://thenewstack.io/why-internal-developer-portals-need-automations) (reporting on the health of your workloads) and define what will be triggered (workload data will be sent to Kafka):

![JSON representation of the automation workflow](https://cdn.thenewstack.io/media/2024/11/b0125fc5-json-automation-workflow-980x1024.png)
JSON representation of the automation workflow (see [this code](https://github.com/dan-amzulescu-port/Port-K8sGPT/blob/main/PortObjects/Automations/K8s-serviceUnHealthy.json) in GitHub).

Last but not least, you need to create the facilitator that will:

- Continuously listen to Kafka topics.
- Consume relevant messages (with the right type) to poll K8sGPT regarding the identified, unhealthy workloads.
- Populate the portal with insights from K8sGPT for the relevant unhealthy Kubernetes workloads.
Here is an example of what K8s AI insights look like in the portal:

![JSON representation of insights on Kubernetes workflows](https://cdn.thenewstack.io/media/2024/11/b45e7aa4-json-kubernetes-workflows-912x1024.png)
JSON representation of insights on Kubernetes workflows (see [this code](https://github.com/dan-amzulescu-port/Port-K8sGPT) in GitHub).

Now, when this workflow is implemented, you can receive regular, real-time updates on the health of your Kubernetes workflows, alongside recommendations for how to resolve them. This can help reduce the time it takes to locate the issues and figure out how to fix them.

## Additional Considerations for Your Workflow
Though this may be a good start to automating your workflow, there are still other ways you can continuously improve it and boost efficiency.

You could simplify the flow of events in your workflow in multiple ways — for example, you can entirely bypass using an event to trigger K8sGPT and instead modify the script to continuously monitor the health of the cluster and distribute insights autonomously.

The command-line outputs and overall refinements in this example are also better than the outputs provided via REST API. Therefore, some additional output modifications were made to improve the overall REST API-generated output.

## Using Alternative GPTs
While K8sGPT offers impressive capabilities, in more advanced scenarios, AI can assist across multiple domains such as cloud infrastructure, where issues often span different layers of the stack. The goal is not just to equip AI to handle multiple domains but to empower it to fully automate the remediation process and resolve issues independently.

I recently came across another emerging open source AI project, [HolmesGPT](https://github.com/robusta-dev/holmesgpt), which I believe complements and even extends K8sGPT’s functionality.

HolmesGPT offers AI-driven insights and supports both Kubernetes and other flexible deployment architectures, along with multiple AI models. However, based on my experiments, HolmesGPT stands out with its advanced capabilities and superior performance.

One of HolmesGPT’s standout features is its ability to understand and respond to natural language queries. Here are two examples that illustrate its prowess:

- Simple question: Identifying Kubernetes pods with issues
- Complex inquiry: Requesting solutions
But HolmesGPT doesn’t stop at Kubernetes. It extends its analytical capabilities to a wide range of platforms and tools, including [PagerDuty](https://www.pagerduty.com/?utm_content=inline+mention), OpsGenie, Prometheus and Jira. This cross-domain functionality is a game-changer, allowing users to set up workflows that analyze and interpret logs and data from many different sources.

Central to this capability is the concept of runbooks, which can be defined in natural language. These runbooks enable users to create cross-domain workflows for comprehensive issue analysis and resolution, making the entire troubleshooting process more coherent and streamlined.

In essence, HolmesGPT isn’t just an AI tool for Kubernetes — it’s a holistic solution for modern DevOps environments, empowering teams to resolve issues more efficiently and effectively.

## Summary
- Debugging and resolving issues often consumes significant time and involves error-prone manual processes for engineers.
- Reducing time-to-resolution is crucial for improving service quality and allowing teams to focus on innovation.
- Internal developer portals represent a significant step towards reducing time-to-resolution by providing refined, contextual information.
- Portals can be further enhanced by leveraging AI insights across various domains.
- The ultimate goal is to achieve cross-domain insights and automated remediation, streamlining problem-solving processes.
Want to see how it could work for you? Check out Port’s [live demo](https://demo.getport.io/organization/home) or read about [driving developer self-service](https://thenewstack.io/drive-developer-self-service-with-crossplane-k8s-and-a-portal/) with Crossplane, Kubernetes and a portal. Discuss all things portal with like-minded individuals by joining [Port’s community on Slack](https://join.slack.com/t/port-community/shared_invite/zt-2n5tu72wi-FEgN6HGFeG9bcRfHtKYdCg).

[
YOUTUBE.COM/THENEWSTACK
Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.
](https://youtube.com/thenewstack?sub_confirmation=1)