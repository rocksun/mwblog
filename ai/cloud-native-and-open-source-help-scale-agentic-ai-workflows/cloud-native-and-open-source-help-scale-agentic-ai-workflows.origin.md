# Cloud Native and Open Source Help Scale Agentic AI Workflows
![Featued image for: Cloud Native and Open Source Help Scale Agentic AI Workflows](https://cdn.thenewstack.io/media/2025/06/43fddf20-business-1024x575.png)
Enterprise automation is increasingly leveraging intelligent agent workflows driven by AI, typically relying on large language models (LLMs) for these applications. While LLMs can address many general-purpose use cases, the deployment and orchestration of these models can add significant complexity and high operational costs.

To tackle enterprise-specific use cases, organizations have begun seeing the benefit of smaller models. As a result, [small language models (SLMs)](https://thenewstack.io/the-rise-of-small-language-models/) paired with contemporary cloud native platforms such as [Kubernetes](https://thenewstack.io/kubernetes/) and [Function as a Service (FaaS)](https://thenewstack.io/serverless/) have emerged as an alternative to address [agentic AI](https://thenewstack.io/agentic-ai-the-next-frontier-of-ai-power/) use cases.

Let’s explore how to effectively use cloud native paradigms to deploy and scale SLM-based agentic workflows. Specifically, how to use Kubernetes, Knative and serverless platforms to help dynamically manage inference workloads, optimize resource utilization and accelerate innovation in agent-driven AI applications.

## Why Small Language Models?
While LLMs have gained popularity for their impressive capabilities, their high computational requirements and significant infrastructure overhead often limit their practical deployment at scale. SLMs, typically with fewer parameters and leaner computational demands, can offer substantial advantages in scenarios where responsiveness, scalability and cost-efficiency are critical.

An example of an SLM is [Microsoft’s](https://news.microsoft.com/?utm_content=inline+mention) [Phi-3-mini](https://thenewstack.io/how-to-get-started-running-small-language-models-at-the-edge/). Its relatively small number of parameters (3.8 billion) translates to a smaller memory footprint and faster processing times. Other examples of SLMs include [Mistral 7B](https://thenewstack.io/gemma-google-takes-on-small-open-models-llama-2-and-mistral/), [Llama 3.2](https://thenewstack.io/llama-stack-released-to-help-developers-build-agentic-apps/) and [Google](https://cloud.google.com/?utm_content=inline+mention) [Gemma 2B](https://thenewstack.io/gemma-google-takes-on-small-open-models-llama-2-and-mistral/), which are well suited for running on smaller GPUs and CPUs. These models are designed for efficiency and can all be deployed in various settings, including edge devices like laptops.

For many agentic workflows, such as real-time customer interactions, DevOps automation, anomaly detection and data enrichment, SLMs tend to deliver sufficient accuracy and significantly lower latency. Their smaller footprint makes them ideal candidates for cloud native architectures, emphasizing agility and cost-effectiveness.

## Cloud Native Architectures: Kubernetes and FaaS
The Cloud Native Computing Foundation (CNCF) ecosystem provides robust tools that enable efficient and scalable AI deployments. At the core is Kubernetes, a container orchestration platform renowned for automating application deployment, scaling and management. Kubernetes facilitates containerized deployments, enabling efficient resource allocation and seamless scalability.

A rich ecosystem of CNCF projects complements Kubernetes, including Knative. This FaaS platform provides developers and MLOps teams with critical building blocks for deploying serverless workloads on Kubernetes, enabling automatic scaling based on demand and helping reduce operational overhead by dynamically managing container life cycles.

Using these technologies together can help organizations deploy SLM-based agents rapidly, scale seamlessly under varying workloads and maintain cost efficiency.

## Practical Implementation
To create the following implementation, we are using [OCI Kubernetes Engine](https://www.oracle.com/cloud/cloud-native/kubernetes-engine/?source=:ex:pw:::::TNS_ScalingSLMS_May25&SC=:ex:pw:::::TNS_ScalingSLMS_May25&pcode=) (OKE) on [Oracle Cloud Infrastructure](https://www.oracle.com/cloud/?source=:ex:pw:::::TNS_ScalingSLMs_May25_B&SC=:ex:pw:::::TNS_ScalingSLMs_May25_B&pcode=) (OCI). OKE provides a fully managed Kubernetes environment, simplifying the setup and operation of production-grade Kubernetes clusters. It is conformant with the CNCF’s open source Kubernetes, and the example below should also work using that. In addition, integrating Knative into OKE creates a robust serverless infrastructure for SLM deployment.

**Architectural Blueprint**
An effective cloud native architecture leveraging OCI, Kubernetes and FaaS for SLM deployment consists of several key components like those listed below:

**Oracle Kubernetes Engine (OKE)**: Manages Kubernetes clusters, automating orchestration, security and scaling.**Knative Serving**: Provides serverless capabilities, automatically scaling SLM containers up and down based on inference requests.**OCI object storage**: Stores model artifacts and configuration files, facilitating easy deployment and updates.**Prometheus and Grafana**: Integrate via CNCF tools; they monitor performance metrics, resource utilization and scaling behavior.**Istio service mesh**: Offers advanced traffic management, security and observability.
**Step-by-Step Deployment Guide**
**Prepare Your Kubernetes Cluster**
Provision a Kubernetes cluster using OCI’s managed Kubernetes service. This simplifies cluster management, leaving you free to focus on deployment specifics:

1 |
oci ce cluster create --name my-oke-cluster --kubernetes-version v1.29.0 |
**Install Knative Serving**
Deploy Knative Serving using YAML manifests, enabling serverless functionality:

12 |
kubectl apply -f https://github.com/knative/serving/releases/download/knative-v1.14.3/serving-crds.yamlkubectl apply -f https://github.com/knative/serving/releases/download/knative-v1.14.3/serving-core.yaml |
**Containerize the Small Language Model**
Use Docker or an OCI-compliant container registry to package your SLM with lightweight runtime environments such as FastAPI or Flask:

12345 |
FROM python:3.11-slimCOPY ./model ./modelCOPY requirements.txt ./RUN pip install -r requirements.txtCMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8080"] |
**Deploy the Serverless SLM via Knative**
Create a Knative Service YAML manifest:

12345678910111213 |
apiVersion: serving.knative.dev/v1kind: Servicemetadata: name: slm-agentspec: template: spec: containers: - image: oci-container-registry/my-slm-agent:v1.0 resources: requests: cpu: 500m memory: 512Mi |
Apply the manifest to deploy your model as a Knative service:
1 |
kubectl apply -f slm-agent.yaml |
Knative automatically scales your SLM agent based on incoming requests, spinning up and tearing down containers as needed, optimizing resource use and cost.
**Monitoring and Optimization**
Using tools such as Prometheus and Grafana deployed through Helm charts, monitor SLM agent performance, latency and resource utilization:

1 |
helm install prometheus prometheus-community/kube-prometheus-stack |
Configure Istio service mesh for detailed traffic management and security.
## Addressing Industry-Specific Use-Cases
**Real-Time Customer Support**
Deploying SLM agents for real-time chat support can help enhance customer interaction efficiency by significantly reducing response latency. Cloud native agents can dynamically scale to meet fluctuating demand, reducing delays during peak usage periods. Organizations benefit from operational cost reductions, as the serverless infrastructure eliminates the need for always-on provisioning, seamlessly scaling resources to match demand precisely.

**DevOps Automation**
Integrating SLM agents into CI/CD pipelines with Kubernetes and Knative enables highly effective automated troubleshooting and proactive anomaly detection. Agents can swiftly interpret build logs and test outputs, monitor alerts, diagnose issues and suggest immediate fixes. This helps improve operational efficiency, reduce downtime and streamline DevOps processes by helping to rapidly identify and resolve pipeline bottlenecks.

**Financial Services**
Financial institutions can deploy lightweight SLM agents to more quickly analyze real-time market data, enabling rapid and informed decision-making without the heavy computational overhead typical of larger models. These agile, scalable deployments can more efficiently help handle substantial volumes of concurrent queries, providing traders and financial analysts with immediate insights, trend forecasts and risk assessments, which are crucial for informed trading strategies and to address regulatory compliance.

## Conclusion
Organizations are striving to understand the new paradigm that agentic AI offers to improve operational efficiencies. By integrating SLMs with Kubernetes and FaaS, enterprises can use scalable, efficient and responsive agent-based solutions to help address their use cases. Cloud native solutions like Oracle’s OKE, complemented by CNCF tools such as Knative, Prometheus and Istio, can help streamline operations, be applied to reduce overhead and enable organizations to deliver innovative AI-driven solutions swiftly and economically. Embracing this [cloud native approach](https://thenewstack.io/cloud-native/10-key-attributes-of-cloud-native-applications/) positions businesses to thrive in increasingly agile and competitive environments.

*Experiment with Oracle’s **cloud native services** using the **Oracle Cloud Free Tier**, or quickly build new generative AI solutions with the **AI Solutions Hub**.*
[
YOUTUBE.COM/THENEWSTACK
Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.
](https://youtube.com/thenewstack?sub_confirmation=1)