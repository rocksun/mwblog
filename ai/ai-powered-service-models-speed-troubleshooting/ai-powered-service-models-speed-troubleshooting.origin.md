# AI-Powered Service Models Speed Troubleshooting
![Featued image for: AI-Powered Service Models Speed Troubleshooting](https://cdn.thenewstack.io/media/2024/08/87839df0-ai-powered-service-models-speed-troubleshooting-1024x576.jpg)
If you manage a modern distributed IT environment, context is critical for troubleshooting and analyzing the business impact of production issues. But that context can be hard to acquire.

You might have different teams and [observability](https://thenewstack.io/otel-is-the-secret-to-devops-success) solutions managing the different layers that contribute to a business service, or different tools that generate useful [telemetry data](https://thenewstack.io/metrics-traces-logs-and-now-opentelemetry-profile-data/), such as metrics, events, logs, traces and topology, but they operate in silos. Maybe you don’t have a model of the connections in your environment. Or possibly all the knowledge about cause-and-effect relationships, actions and consequences is not documented but locked in someone’s institutional memory.

To pinpoint the root cause of service issues accurately and quickly in complex environments, you need deep understanding of critical paths and dependency levels across the application, API and network layers.

Highly performant graph databases, [dynamic service modeling](https://www.bmc.com/blogs/whats-new-with-bmc-helix-winter-release/) capabilities and causal AI can help you understand and model the cause-and-effect relationships between different applications, APIs and network and infrastructure layers. Modeling your service — building a visualization of services and the relationships between various system and infrastructure components — provides critical context for troubleshooting. A well-defined service gives you an end-to-end view to quickly identify an impacted node for faster root cause analysis.

## How Service Modeling Works
Assuming you have a dynamic and reconciled graph database of your IT landscape where all types of ingested data (metrics, events, logs, traces, topology) are normalized, modeling your service involves the following steps:

**Identify end-user services that you want to model and add service details as inputs to the service modeling tool.**An application performance monitoring (APM) tool can provide application-specific details about software components and their relationships across cloud, mainframe and container topologies. Infrastructure and network monitoring tools and scanning tools can detail the infrastructure’s connectivity to underlying virtual and physical devices, such as servers, databases, switches, routers, firewalls and load balancers.**Use blueprints to dynamically traverse all layers to automatically connect the application topology to the hosts and network devices.**Discovery and monitoring tools can provide service blueprints to simplify creating and maintaining dynamic service models. These service models support modern technologies like microservices,[Kubernetes](https://roadmap.sh/kubernetes), cloud services, application performance tracking and mainframes to keep accurate tabs on all IT resources and relationships. Blueprints make it easy to express a simple rule that identifies all the elements of your service. You define the rule once and apply it to as many services as needed.**Calculate the health score for a service.**Understanding a service’s current and historical health based on indicators, abnormalities and events in the service model’s components helps you identify root causes of health impacts or service performance degradation. Machine learning (ML) algorithms can calculate health scores, so you can quickly understand the scope of an issue.
## How to Incorporate AI for Faster Troubleshooting
AI technologies such as causal AI and generative AI (GenAI) can help accelerate the troubleshooting process by connecting cause to effect and translating root cause insights. True [AIOps](https://thenewstack.io/seeing-the-big-picture-with-aiops/) requires a complete system designed to collect and model data through the lens of end users and business impacts. Service modeling, using the process above, allows you to confidently use AI to generate reliable insights.

Causal AI integrates [knowledge graph](https://thenewstack.io/how-knowledge-graphs-make-data-more-useful-to-organizations/) and transformer-based AI techniques to understand and model relationships across telemetry data variables. Casual AI can reason about casual relations or patterns using topological data. A knowledge graph–based causality analysis analyzes how causal relationships change depending on how the variables influence one another.

Using causal AI in production troubleshooting:

- Helps you understand and explain a problem by providing visual representations of how events were correlated and how the root cause was identified.
- Accelerates troubleshooting by automatically identifying whether a similar situation previously occurred. If you’ve already seen and resolved a problem, you shouldn’t need to go through the entire discovery process again. Causal AI fingerprints recurring situations for future identification to help speed mean time to recovery (MTTR) and reduce incident noise.
GenAI also has a powerful role in the troubleshooting process. It can be used to generate:

- Plain-language summaries, making it quicker and simpler to understand an issue compared to decoding a string of output error codes.
- Best-action recommendations to resolve issues.
- Responses to commonly asked questions during troubleshooting.
For AI algorithms to give results that you trust, the quality of your data matters. Establishing the right foundation with well-defined service models is critical.

## Real-World Applications
Service modeling is already making a significant impact in managing services. It decreases investigation time, helping you see and respond to issues before they impact the business.

Here are examples of how service modeling enables faster root cause analyses, continuous optimization and continuous compliance.

**Root cause analysis:**By modeling service dependencies as a reconciled topology, you can isolate the root cause of an issue, whether it’s:- The application software components: Don’t impact the infrastructure.
- The network: Impacts the infrastructure and application.
- The mainframe database: Impacts distributed applications.
**Capacity optimization:**By analyzing interactions between services, service modeling can provide insights into how to right-size and align IT resources with changing business requirements. When used with AI to analyze bottlenecks and recommend areas to minimize risk and cost, you can continuously optimize your IT environment’s performance.**Continuous compliance:**Collecting and modeling IT assets, services and relationships provides up-to-date information and processes to meet security and regulatory compliance requirements. Instead of chasing down individual developers to document what’s running and where, you can stay ahead of ever-growing risk and complexity with automated discovery and service modeling.
There’s no question that AI will continue to play an important role in observability. It can greatly accelerate the troubleshooting workflow and improve efficiency with the right contextual data.

The [BMC Helix IT Operations Management](https://www.bmc.com/it-solutions/it-operations-management.html) (ITOM) portfolio provides out-of-the-box service blueprints that make it easier to create and maintain dynamic service models. And [BMC Helix Operations Management with AIOps](https://www.bmc.com/it-solutions/bmc-helix-operations-management.html) (BMC Helix AIOps) takes it a step further with a fully integrated, cloud-native, observability and AIOps solution that gives you the right tools and data to significantly reduce the time to isolate root causes and resolve problems.

[
YOUTUBE.COM/THENEWSTACK
Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.
](https://youtube.com/thenewstack?sub_confirmation=1)