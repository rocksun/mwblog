# Harness Kubernetes Costs With OpenCost
The major conversations (read: complaints) at every event I attend are about managing Kubernetes’ complexity and cost. A recent survey [found](https://www.infoq.com/news/2024/03/cncf-finops-kubernetes-overspend/) that nearly half of the companies saw Kubernetes increasing cloud spending. The ubiquity of Kubernetes is becoming evident, and the demand for help managing it better is growing daily.

[To manage Kubernetes’ complexity](https://thenewstack.io/managing-kubernetes-complexity-in-multicloud-environments/), we can pick a substrate meant for abstracting it. For this, let’s use open source Cloud Foundry [Korifi](https://github.com/cloudfoundry/korifi), an abstraction built on Kubernetes that simplifies application deployment and management. To manage costs, let’s adopt the [Cloud Native Computing Foundation](https://cncf.io/?utm_content=inline+mention) (CNCF) incubating project [OpenCost](https://github.com/opencost/opencost), which provides comprehensive cost visibility and optimization capabilities.
## A Brief Overview of Korifi and OpenCost
The prerequisites for the tutorial that follows require knowledge of the tools. Cloud Foundry Korifi aims to bring the best of the Cloud Foundry experience to Kubernetes. It provides a higher-level abstraction over Kubernetes, [simplifying application deployment and management for developers](https://thenewstack.io/simplifying-cloud-native-application-development-with-ballerina/).

**Here’s a breakdown of its key features:**
- Simplified application deployment: Korifi allows developers to deploy applications to Kubernetes using familiar Cloud Foundry commands, such as cf push. This abstracts away the complexities of
[Kubernetes YAML configurations](https://thenewstack.io/tutorial-configure-storage-volumes-for-kubeflow-notebook-servers/), making deployments easier and faster. - Language and framework agnostic: Developers can deploy applications built with various languages and frameworks without worrying about underlying Kubernetes configurations.
- Automated networking and security: Korifi automates networking and security tasks, such as service discovery, routing, and security policies, enhancing application reliability and security.
- Enhanced developer experience: By providing a streamlined and user-friendly experience, Korifi empowers developers to focus on
[building applications rather than wrestling with complex Kubernetes](https://thenewstack.io/build-vs-buy-compare-your-kubernetes-platform-options/)configurations.
## What Is OpenCost?
OpenCost is an open source platform that provides comprehensive [cost visibility across your entire cloud infrastructure](https://thenewstack.io/it-leaders-brace-for-tariff-fallout-on-infrastructure-and-cloud-costs/). OpenCost is a powerful tool for any [DevOps team looking to gain control of their cloud](https://thenewstack.io/chaos-under-control-addressing-cloud-infrastructure-drift/) costs. By providing granular visibility, insightful analytics, and a flexible platform, OpenCost empowers you to optimize your cloud spending and maximize the return on your cloud investments.

In today’s cloud native world, understanding and optimizing cloud spending is crucial for any organization, regardless of size. Here is a short list of OpenCost’s many benefits.

- Open source and customizable: Built on open source principles, OpenCost offers flexibility, the ability to tailor it to your specific needs, and the ability to integrate it seamlessly into your existing infrastructure.
- Supports multiple cloud providers: Whether using AWS, Azure, GCP, or a combination, OpenCost can provide a unified view of your cloud spending across all platforms.
- Data-driven decision-making: OpenCost provides a wealth of data and visualizations to help you understand your cloud costs in depth and make informed decisions about your cloud strategy.
- Community-driven development: Benefit from the active community of developers and users who contribute to the ongoing development and improvement of the platform.
### How To Install Cloud Foundry Korifi and OpenCost
This guide will demonstrate how to install Cloud Foundry Korifi and OpenCost on a local Kubernetes cluster (KiND).

**Prerequisites:**
- Ensure you have Helm 3 installed and configured on your system.
- Install KiND using the official instructions.
- Install kubectl to manage your cluster.
**Installing Korifi:**
- Create a Kubernetes cluster using KiND by applying the following configuration inline:
12345678910111213141516171819202122232425 |
cat <<EOF | kind create cluster --name korifi --config=-kind: ClusterapiVersion: kind.x-k8s.io/v1alpha4containerdConfigPatches:- |- [plugins."io.containerd.grpc.v1.cri".registry] [plugins."io.containerd.grpc.v1.cri".registry.mirrors] [plugins."io.containerd.grpc.v1.cri".registry.mirrors."localregistry-docker-registry.default.svc.cluster.local:30050"] endpoint = ["http://127.0.0.1:30050"] [plugins."io.containerd.grpc.v1.cri".registry.configs] [plugins."io.containerd.grpc.v1.cri".registry.configs."127.0.0.1:30050".tls] insecure_skip_verify = truenodes:- role: control-plane extraPortMappings: - containerPort: 32080 hostPort: 80 protocol: TCP - containerPort: 32443 hostPort: 443 protocol: TCP - containerPort: 30050 hostPort: 30050 protocol: TCPEOF |
- Install the Korifi substrate using the following installer:
1 |
kubectl apply -f https://github.com/cloudfoundry/korifi/releases/latest/download/install-korifi-kind.yaml |
- Next, use Helm to install OpenCost:
1 |
helm repo add opencost https://charts.opencost.io |
- Make sure to update Helm:
1 |
helm repo update |
- Next, use Helm to install:
1 |
helm install opencost opencost/opencost |
- Verify the installation using:
1 |
kubectl get pods -n opencost |
- Once OpenCost has finished installing, wait for all the OpenCost pods to reach a “Ready” state. Then, establish a local port-forwarding connection using the following command:
1 |
kubectl port-forward --namespace opencost service/opencost 9003 9090 |
- Access the OpenCost UI from a browser by visiting localhost:9090.
This figure shows how OpenCost provides useful information on a per-pod basis. In the case of Korifi, a pod represents a build. Therefore, we can now see costs per build, which would otherwise never be available.

Checking costs per namespace can be useful for deriving accountability, driving optimization, and identifying anomalies. Here’s an example of what that visualization looks like with OpenCost.

## Summary
There you have it. Now, you have visibility to understand and optimize your costs — best of all, by leveraging open source software.

OpenCost deployed with Korifi makes it possible to monitor the costs of a “build,” a “deployment,” and other primitives that make up the whole cluster. OpenCost can break down costs into atomic components, which helps synthesize an understanding of Kubernetes clusters in an entirely new dimension.

Why do this in the first place, though? To extract the most mileage out of cloud computing, [engineering teams must begin to develop](https://thenewstack.io/4-north-star-metrics-for-platform-engineering-teams/) an understanding of the infrastructure costs involved. This does not mean keeping tabs on AWS bills. This also means expanding the transparency into app deployments, CI/CD costs, observability costs, and more. With this information, engineering teams can make much more transformative decisions about allocating the right resources for their stacks.

[
YOUTUBE.COM/THENEWSTACK
Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.
](https://youtube.com/thenewstack?sub_confirmation=1)