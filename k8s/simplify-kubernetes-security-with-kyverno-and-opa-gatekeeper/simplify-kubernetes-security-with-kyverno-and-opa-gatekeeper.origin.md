# Simplify Kubernetes Security With Kyverno and OPA Gatekeeper
![Featued image for: Simplify Kubernetes Security With Kyverno and OPA Gatekeeper](https://cdn.thenewstack.io/media/2025/06/e0086a79-door-1024x682.jpeg)
[Kubernetes ](https://thenewstack.io/securing-kubernetes-with-external-secrets-operator-on-aws/)is hands-down the go-to tool for managing containerized applications, yet it comes with one specific challenge: security! With its complexity, ensuring your [Kubernetes deployment](https://thenewstack.io/kubernetes/) is secure and aligned with best practices can be overwhelming.
But there’s good news. Tools like [Kyverno](https://thenewstack.io/using-the-kyverno-cli-to-write-policy-test-cases/) and [OPA Gatekeeper](https://thenewstack.io/getting-open-policy-agent-up-and-running/) are here to help you protect your clusters. These policy enforcement engines make sure your Kubernetes resources are safe and compliant before they even enter your cluster. Sounds like a game-changer, right?

Here’s how these tools can simplify your Kubernetes security setup and help you avoid common pitfalls, like running containers as root or using images from dubious sources.

**Why Kubernetes Security Matters **
Kubernetes is a powerhouse for orchestration, but without the right controls, you’re leaving the door open to potential security risks. From untrusted images to excessive resource allocation, the risks can pile up fast. That’s where policy engines come in. They act as guardrails, creating a balance between security and developer autonomy.

**Enter Kyverno and OPA Gatekeeper **
Both [Kyverno](https://kyverno.io/) and [OPA Gatekeeper](https://github.com/open-policy-agent/gatekeeper) are designed to lock down your Kubernetes environment without adding unnecessary complexity. Think of them as your Kubernetes security bouncers. They validate your configurations, ensure compliance and stop vulnerabilities in their tracks before they get into your system.

**Spotlight on Kyverno **
Kyverno is built specifically for Kubernetes, and it’s simple to use. Policies are written in [YAML](https://yaml.org), a human-friendly data serialization language, with no extra programming language required. Whether you’re enforcing namespaces, applying cluster-wide rules or testing policies with the CLI tool before deployment, Kyverno has you covered. And the bonus? You get reports on compliance right out of the box. Some key highlights of Kyverno include:

- Easy-to-write YAML policies
- Native integration with Kubernetes tooling
- A CLI tool to preview policies before rolling them out
- Policy enforcement across namespaces and clusters
**Built-In Compliance Reporting**
Kyverno doesn’t just enforce security; it empowers organizations to understand and adapt their policies with clarity and precision.

**How To Install Kyverno in Your Kubernetes Cluster**
You will need to install Helm in your workstation. You will be using [Helm](https://helm.sh/) to install Kyverno.

**Get Started With Kyverno**
Why use Helm to install Kyverno? It’s:

- Better-suited for production
- Easier to install and upgrade packages or software in your cluster
**Step 1: Install Helm (if not already installed)**
**To install brew on macOS (with Homebrew):**
`brew install helm`
**To install brew on Linux:**
`curl https://raw.githubusercontent.com/helm/helm/main/scripts/get-helm-3 | bash`
**To install brew on Windows (with Chocolatey):**
`choco install kubernetes-helm`
**Step 2: Add the Kyverno Helm Repo**
12 |
helm repo add kyverno https://kyverno.github.io/kyverno/helm repo update |
**Step 3: Install Kyverno**
1 |
helm install kyverno kyverno/kyverno --namespace kyverno --create-namespace |
**Step 4: Verify the Kyverno Installation**
`kubectl get pods -n kyverno`
**Example of Kyverno Policy**
**Use case 1**: It prevents users from deploying containers that use `:latest tag`
.
If there is an issue with that piece of code, it is very difficult to track or roll back since you’re not sure all instances of it have the same version. The image also might have other dependencies that are difficult to track down or fix.

Please copy and paste the snippet below into a file with the filename `disallow-latest-tag.yaml`
and use this command to execute it in your cluster. The policy below will prevent users from using image tags `:latest`
in your cluster.

`kubectl apply -f disallow-latest-tag.yaml`
### Applying NGINX With the ‘Latest’ Tag
Please copy and paste the snippet below into a file with the filename `nginx-latest.yaml`
and use this command to execute it in your cluster. The manifest below uses an image with `nginx:latest`
. The Kyverno policy should prevent you from applying the manifest:

`kubectl apply -f nginx-latest-tag.yaml`
You can see below that we are unable to create the NGINX pod with the image tag as the latest. This is the essence of using a policy engine like Kynervo to enforce security best practices.

By enforcing policies such as disallowing mutable image tags (latest), teams can:

- Prevent unintentional deployments of unversioned or unstable images
- Improve traceability and reproducibility
- Strengthen the overall security posture of the cluster
## What Is OPA Gatekeeper?
[Open Policy Agent (OPA) Gatekeeper](https://www.openpolicyagent.org/integrations/gatekeeper/) is a policy enforcement tool tailored to work with Kubernetes. Policies are written in [Rego, OPA’s declarative query language](https://www.openpolicyagent.org/docs/policy-language), to define rules and enforce security policies dynamically. It allows you to write policies that check whether something in your Kubernetes setup breaks a defined rule.
OPA Gatekeeper acts as a Kubernetes admission controller, evaluating policies before the resources are deployed and helping to ensure compliance from the beginning.

Below is an example of a simple Rego rule to ensure that all namespaces in your Kubernetes cluster have a team label:

12345678910 |
package kubernetes.admissionviolation[{"msg": "Namespace must have a 'team' label"}] {api_object.kind == "Namespace"not has_label(api_object.metadata.labels, "team")}has_label(labels, label) {labels[label]} |
**Key Features of OPA Gatekeeper**
- The policy logic is kept separate from the constraints, making it reusable across different policies. The policy logic, written in Rego, defines what should be checked (for example: “Namespace must have team label”), while constraints tells the Gatekeeper where and when to apply the policy logic (for example: “Apply this rule to all namespaces in this cluster”).
- It can scan existing resources for violations.
**Comparing Kyverno and OPA Gatekeeper**
Feature | Kyverno |
OPA Gatekeeper |
Policy language |
YAML | Rego |
Complexity |
Simple | Complex |
Mutation support |
Yes | No |
Custom resource support |
Yes | Limited |
Flexibility |
Moderate | High |
Learning curve |
Low | High |
**Choosing Between Kyverno and OPA Gatekeeper**
The choice between Kyverno and OPA Gatekeeper depends on your specific needs and technical expertise:

**Choose Kyverno if**:
- You prefer a Kubernetes-native approach with policies defined as CRDs using YAML.
- You and your team are familiar with Kubernetes concepts and YAML.
- You need a simpler and more intuitive way to define common Kubernetes security policies.
**Choose OPA Gatekeeper if**:
- You and your organization have an existing expertise in Rego or are willing to invest in learning it.
- You need to express highly complex and custom policy logic.
- You need to use a more mature and widely adopted policy engine with broader community support.
- You require a general-purpose policy engine that can be used across multiple systems. OPA Gatekeeper can be used to enforce policies not only in Kubernetes environments but also across various systems such as microservices, cloud platform and more.
Both Kyverno and OPA Gatekeeper, when implemented, can enforce security best practices such as:

- Enforcing namespace-based resource quotas.
- Restricting privileged container execution.
- Requiring specific labels and annotations.
## Install OPA Gatekeeper in Your Cluster
You will need to have [Helm](https://helm.sh/) running on your workstation.

**Step 1: Add the Gatekeeper Helm Repo:**
12 |
helm repo add gatekeeper https://open-policy-agent.github.io/gatekeeper/chartshelm repo update |
**Step 2: Install Gatekeeper**
123 |
helm install gatekeeper gatekeeper/gatekeeper \--namespace gatekeeper-system \--create-namespace |
**Example of OPA Gatekeeper Policy**
**Use case 1**: It prevents users from deploying containers that use `:latest`
tag.
**Step 1: Create a Constraint Template (It Defines the Logic)**
Please copy and paste the snippet below into a file with the filename `disallow-latest-tag-constraint-template.yaml`
.

`kubectl apply -f disallow-latest-tag-constraint-template.yaml`
**Step 2: Constraint (Activates and Applies the Template)**
Please copy and paste the snippet below into a file with the filename `disallow-latest-tag-gatekeeper.yaml`

`kubectl apply -f disallow-latest-tag-gatekeeper.yaml`
**Step 3: Applying NGINX with the ‘Latest’ Tag**
Please copy and paste the snippet below into a file with the filename `nginx-latest.yamland`
. Use this command to execute it in your cluster. The manifest below uses an image with `nginx:latest`
. The Gatekeeper Rego policy should prevent you from applying the manifest.

`kubectl apply -f nginx-latest-tag.yaml`
![Container with the tag latest.](https://cdn.thenewstack.io/media/2025/06/9aebb6e9-image10a-1024x107.png)
Container with the tag ‘latest’.

**Conclusion**
Kyverno and OPA Gatekeeper are useful tools for keeping your Kubernetes workloads secure. Kyverno stands out with its simple, YAML-based policies and Kubernetes-native design, making it easy to use. On the other hand, OPA Gatekeeper brings serious flexibility with its Rego language, which is adept at handling complex setups or working across multiple platforms. Picking the right one really comes down to what your team needs, your experience level and your security goals. Both tools help developers move quickly and confidently while staying within the rules, making sure security, compliance and best practices are baked into everything without slowing anyone down.

Learn how to create an end-to-end solution to automate the build, test and deployment processes for a Kubernetes-based Node.js REST API in Andela’s guide, “[Make a Scalable CI/CD Pipeline for Kubernetes With GitHub and Argo CD](https://www.andela.com/blog-posts/make-a-scalable-ci-cd-pipeline-for-kubernetes-with-github-and-argo-cd/?utm_medium=contentmarketing&utm_source=blog&utm_campaign=brand-global-the-new-stack&utm_content=kubernetes-gatekeeper&utm_term=writers-room).”

[
YOUTUBE.COM/THENEWSTACK
Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.
](https://youtube.com/thenewstack?sub_confirmation=1)