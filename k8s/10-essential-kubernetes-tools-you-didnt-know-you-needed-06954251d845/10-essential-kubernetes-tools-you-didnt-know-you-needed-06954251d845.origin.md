# 10 Essential Kubernetes Tools You Didn’t Know You Needed
# Introduction
As Kubernetes celebrates its 10th anniversary, its adoption and ecosystem have grown exponentially. With over **100,000** stars on GitHub, Kubernetes has become the backbone of the cloud-native ecosystem, enabling scalable and efficient management of containerized applications. The latest version, [Kubernetes 1.30](https://kubernetes.io/blog/2024/04/17/kubernetes-v1-30-release/), introduces several new features and improvements, further solidifying its place as a leading container orchestration platform.

However, to truly harness the power of Kubernetes, it’s essential to utilize the right tools. In this blog, we’ll explore ten lesser-known but incredibly useful tools that can enhance your Kubernetes experience. From configuration issues detection to network observability, these tools will help you manage your clusters more effectively and efficiently. Whether you’re a seasoned Kubernetes user or just getting started, you’ll find valuable insights and practical tips to optimize your Kubernetes workflows.

Let’s dive in and discover the tools that can take your Kubernetes game to the next level!

# Categories of Tools
Each project we are going to talk about belongs to a category. These categories help in setting up, managing, and developing on Kubernetes. I have deliberately tried to avoid well-known and established projects such as Prometheus/Grafana in the observability space or Cilium in networking. Instead, we will focus on tools that may not be as widely known but offer significant benefits to Kubernetes users.

# 1. Popeye
**Repository Link**: [Popeye](https://github.com/derailed/popeye)
**Category**: Configuration Issues Detection
**Description**: Popeye is a Kubernetes cluster sanitizer. It scans your Kubernetes resources and reports potential issues and misconfigurations in your clusters. Designed to be proactive, Popeye ensures your clusters are clean and compliant with Kubernetes best practices by regularly scanning and auditing your deployments, configurations, and resource definitions.
**What Problem Does It Solve**: Kubernetes clusters can become cluttered and misconfigured over time, leading to potential stability and performance issues. Popeye helps identify these misconfigurations, such as deprecated API versions, missing resources, and security vulnerabilities. By addressing these issues, Popeye helps maintain the health and performance of your clusters, ensuring they run smoothly and efficiently.
**Example Usage**: To run a scan on your current Kubernetes context and scan all namespaces, simply use the command:
`popeye -A -s cm`
# 2. KUTTL
**Repository Link**: [KUTTL](https://github.com/kudobuilder/kuttl)
**Category**: Testing
**Description**: `KUTTL`
(Kubernetes Test ToolKit) is a comprehensive toolset designed for testing your Kubernetes applications. It provides a simple and declarative framework to write, run, and manage tests, ensuring your Kubernetes configurations and applications behave as expected.
**What Problem Does It Solve**: Testing Kubernetes configurations and applications can be complex and error-prone. `KUTTL`
simplifies this process by providing a declarative testing framework that integrates seamlessly with Kubernetes. It allows you to define test scenarios and expected outcomes, making it easier to validate your configurations and catch issues early in the development cycle.
**Example Usage**: To create and run tests with `KUTTL`
, you can define your test cases in YAML files. Here’s an example of a simple test case:
Create a test directory structure:

`my-tests/`
├── 00-setup.yaml
├── 01-verify.yaml
├── kuttl-test.yaml
Define a test step in `00-setup.yaml`
:

`apiVersion: v1`
kind: ConfigMap
metadata:
name: my-config
data:
key: value
Define the expected outcome in `01-verify.yaml`
:

`apiVersion: v1`
kind: ConfigMap
metadata:
name: my-config
data:
key: value
Run the tests using the command:

`kuttl test my-tests/`
This command will execute the test steps and verify the outcomes as defined in your YAML files.

# 3. Kubescape
**Repository Link**: [Kubescape](https://github.com/kubescape/kubescape)
**Category**: Security Screening
**Description**: `Kubescape`
is a security scanning tool for Kubernetes clusters. It provides a comprehensive assessment of your cluster’s security posture by scanning for vulnerabilities, misconfigurations, and compliance with security standards. `Kubescape`
leverages industry best practices and frameworks, such as the NSA Kubernetes Hardening Guidance, to ensure your cluster meets stringent security requirements.
**What Problem Does It Solve**: Ensuring the security of Kubernetes clusters is crucial, but can be challenging due to the complexity and dynamic nature of the environment. `Kubescape`
simplifies this task by providing automated security scans that identify vulnerabilities, misconfigurations, and compliance issues. This helps administrators maintain a secure and compliant Kubernetes environment, reducing the risk of security breaches and non-compliance.
**Example Usage**: To perform a security scan on your Kubernetes cluster, use the following command:
`kubescape scan framework nsa --exclude-namespaces kube-system`
This command will scan your cluster against the NSA Kubernetes Hardening Guidance framework, excluding the `kube-system`
namespace.

**Example Output**:
📖 Read more about

[Kubernetes security hardening]
# 4. Mirrord
**Repository Link**: [mirrord](https://github.com/metalbear-co/mirrord)
**Category**: Remote Development
**Description**: `mirrord`
is a remote development tool that allows developers to run local processes in the context of their Kubernetes clusters. This means you can develop and debug your applications locally while they interact with live Kubernetes resources as if they were running in the cluster. `mirrord`
simplifies the development process by providing a seamless bridge between local and remote environments.
**What Problem Does It Solve**: Developing and debugging applications that run on Kubernetes can be challenging due to the differences between local and cluster environments. `mirrord`
solves this problem by allowing developers to run their applications locally while seamlessly interacting with the Kubernetes cluster. This helps in faster debugging, testing, and development, as developers can use their familiar local tools and environments without having to deploy their applications to the cluster for every change.
**Example Usage**: To use `mirrord`
for running a local process in the context of your Kubernetes cluster:
`mirrord exec --target-namespace devops-team \`
--target deployment/foo-app-deployment \
nodemon server.js
For a detailed guide and more examples, you can refer to

[my previous blog post]on using`mirrord`
for remote development.
# 5. Kube-linter
**Repository Link**: [Kube-linter](https://github.com/stackrox/kube-linter)
**Category**: Linting
**Description**: `Kube-linter`
is a static analysis tool that checks Kubernetes YAML files and Helm charts to ensure they comply with best practices and security guidelines. It helps you catch potential issues before deploying your resources, ensuring that your Kubernetes configurations are secure and efficient.
**What Problem Does It Solve**: Writing Kubernetes configurations can be complex, and even small mistakes can lead to significant issues in production. `Kube-linter`
solves this problem by analyzing your YAML files and Helm charts for common errors, security risks, and deviations from best practices. This proactive approach helps you identify and fix issues early in the development cycle, improving the overall quality and security of your Kubernetes deployments.
**Example Usage**: To lint your Kubernetes manifests using `Kube-linter`
, run the following command:
`kube-linter lint 1-create-deployment.yaml`
# 6. k3d
**Repository Link**: [k3d](https://github.com/k3d-io/k3d)
**Category**: Provisioning
**Description**: `k3d`
is a lightweight wrapper to run `k3s`
(a lightweight Kubernetes distribution) in Docker. It allows you to create and manage Kubernetes clusters inside Docker containers, providing an easy way to set up and run `k3s`
clusters for development, testing, and CI/CD purposes.
**What Problem Does It Solve**: Setting up and managing Kubernetes clusters for local development and testing can be cumbersome and resource-intensive. `k3d`
simplifies this process by enabling you to run `k3s`
clusters inside Docker containers. This approach reduces the overhead of setting up full-blown virtual machines or physical servers, making it easier and faster to create and manage Kubernetes clusters on your local machine.
**Example Usage**: To create a new `k3s`
cluster with `k3d`
, use the following command:
`k3d cluster create mycluster`
# 7. Kubeshark
**Repository Link**: [Kubeshark](https://github.com/kubeshark/kubeshark)
**Category**: Network Observability
**Description**: `Kubeshark`
is an API traffic analyzer for Kubernetes, providing deep visibility into your Kubernetes network communications. It captures, parses, and visualizes the network traffic in your clusters, allowing you to monitor and debug the interactions between your microservices.
**What Problem Does It Solve**: Understanding and debugging network communications in a Kubernetes cluster can be challenging, especially in complex microservices environments. `Kubeshark`
addresses this problem by providing a comprehensive view of the API traffic within your cluster. This helps developers and operators gain insights into service interactions, detect anomalies, and troubleshoot network issues more effectively.
**Example Usage**: To start capturing traffic with `Kubeshark`
, run the following command:
`kubeshark tap`
# 8. kubectl-tree
**Repository Link**: [kubectl-tree](https://github.com/ahmetb/kubectl-tree)
**Category**: Plugin
**Description**: `kubectl-tree`
is a `kubectl`
plugin that allows you to visualize Kubernetes object hierarchies as trees. This tool enhances the `kubectl`
experience by providing an easy way to view and navigate the relationships between Kubernetes resources, such as Pods, Deployments, ReplicaSets, and more.
**What Problem Does It Solve**: Navigating and understanding the relationships between Kubernetes resources can be complex, especially in large clusters with many interconnected objects. `kubectl-tree`
simplifies this by displaying resource hierarchies in a tree format, making it easier to visualize and manage dependencies and relationships between resources.
**Example Usage**: To visualize the hierarchy of a `crossplane`
deployment, use the following command:
`✗ kubectl tree deployment crossplane -n crossplane-system`
NAMESPACE NAME READY REASON AGE
crossplane-system Deployment/crossplane - 49m
crossplane-system └─ReplicaSet/crossplane-6dcbf47db4 - 49m
crossplane-system └─Pod/crossplane-6dcbf47db4-gzzwp True 49m
# 9. Flux
**Repository Link**: [Flux](https://github.com/fluxcd/flux)
**Category**: GitOps
**Description**: `Flux`
is a set of continuous and progressive delivery solutions for Kubernetes. It automates the deployment of resources and synchronizes cluster state with configurations stored in Git repositories, following GitOps principles. `Flux`
ensures that the desired state of your Kubernetes cluster, as defined in your version-controlled configuration files, is continuously maintained and updated.
**What Problem Does It Solve**: Managing Kubernetes configurations and deployments manually can be error-prone and difficult to audit. `Flux`
solves this problem by automating the synchronization between your Git repository and your Kubernetes cluster. By treating Git as the source of truth, `Flux`
ensures that your cluster state is consistent with your configuration files, enabling traceability, audibility, and easier rollback of changes. This approach also facilitates collaboration among team members by leveraging version control.
**Example Usage**: To install `Flux`
in your Kubernetes cluster and connect it to your Git repository, follow these steps:
`fluxctl identity --k8s-fwd-ns flux`
`fluxctl sync --k8s-fwd-ns flux`
📖 Read more about [using GitOps with Flux and Crossplane](https://medium.com/itnext/gitopsify-cloud-infrastructure-with-crossplane-and-flux-d605d3043452)

# 10. Kubecost
**Repository Link**: [Kubecost](https://github.com/kubecost/cost-model)
**Category**: Cost Management
**Description**: `Kubecost`
is a cost monitoring and optimization tool for Kubernetes clusters. It provides real-time insights into the cost and resource usage of your Kubernetes workloads. `Kubecost`
helps you allocate costs accurately, optimize resource utilization, and reduce overall cloud spending by identifying inefficiencies and unused resources. Additionally, `Kubecost`
integrates with [OpenCost](https://www.opencost.io/docs/), an open-source cost monitoring and management project for Kubernetes.
**What Problem Does It Solve**: Managing costs in Kubernetes environments can be challenging due to the dynamic nature of containerized workloads and the complexity of cloud billing. `Kubecost`
addresses this problem by providing detailed cost breakdowns, usage reports, and optimization recommendations. This helps organizations gain visibility into their Kubernetes spending, make informed decisions about resource allocation, and identify opportunities for cost savings.
**Example Usage**: After deploying `Kubecost`
in your Kubernetes cluster, you can access the dashboard to view cost reports, allocate costs by namespace, label, and deployment, and receive recommendations for optimizing your resource usage. The integration with `OpenCost`
enhances these capabilities by providing standardized cost monitoring and management features.
# Bonus Round
While I have highlighted ten essential tools for Kubernetes, there are numerous other tools that can greatly enhance your Kubernetes experience. These bonus tools offer a range of functionalities from managing deprecated APIs to facilitating remote development, and much more. Here’s a list of additional tools that you might find invaluable:

# Closing Thoughts
We’ve just celebrated Kubernetes’ 10th anniversary and it’s clear that the ecosystem is stronger and more vibrant than ever. Kubernetes has evolved into a critical component of the cloud-native landscape, enabling organizations to manage their containerized applications at scale with efficiency and reliability.

The tools we’ve reviewed in this blog, from `Popeye`
for configuration issues detection to `Kubecost`
for cost management, showcase the diversity and depth of the Kubernetes ecosystem. Each tool addresses specific challenges, helping to optimize or secure Kubernetes deployments. The proliferation of these tools highlights the dynamic nature of the Kubernetes ecosystem and the absence of well established standards in every area. This variety allows for tailored solutions that cater to the unique needs of different organizations and use cases.

Looking ahead, Kubernetes is poised to power even more of the world’s infrastructure. As new trends like edge computing, serverless architectures, and AI-driven operations emerge, Kubernetes will continue to adapt and evolve. The ecosystem’s ability to foster innovation through a wide range of tools and solutions will be crucial in meeting the demands of future cloud-native environments.

Are any of the projects your favourite? Do you use different tools that you would like to share? Let me know in the comments.

Thanks for taking the time to read this post. I hope you found it interesting and informative.

🔗 **Connect with me on ****LinkedIn**

🌐 **Visit my ****Website**

📺 **Subscribe to my ****YouTube Channel**