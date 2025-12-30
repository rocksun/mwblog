As AI systems move from experimentation to production, developers are starting to discover a new problem: The tools that [large language models (LLMs)](https://thenewstack.io/what-is-a-large-language-model/) depend on do not scale well when they run on a single laptop. Early agent prototypes usually start with a simple local [Model Context Protocol (MCP)](https://thenewstack.io/how-to-set-up-a-model-context-protocol-server/) server, which is perfect when you are exploring ideas, but these setups break quickly once multiple teams or real workloads enter the picture.

I ran into this firsthand while building LLM-driven automation inside enterprise environments. Our early MCP tools worked flawlessly during demos, but the moment we connected them to real workflows, everything became fragile. Local processes crashed without logs, multiple engineers could not share the same tool instance, version updates broke workflows, and we had no clean way to roll out new tool capabilities. It became obvious that if MCP was going to power production systems, the servers needed to run remotely, at scale, with proper isolation and observability.

This is the architecture that grew out of those experiences. It outlines a practical and production-ready way to run MCP servers remotely on [Kubernetes](https://thenewstack.io/kubernetes/). The approach uses Amazon Elastic Kubernetes Service (EKS), Elastic Container Registry (ECR), Docker and an [ingress application load balancer](https://thenewstack.io/deploy-a-multicluster-ingress-on-google-kubernetes-engine/) (ALB) to create a scalable pattern that separates the LLM client from the MCP server. This separation makes it possible to deploy, update, debug and scale MCP tools independently from the core LLM workflow, which is essential for real production AI systems.

## Architecture Overview

[![Architecture overview](https://cdn.thenewstack.io/media/2025/12/d3aae05e-image1-905x1024.png)](https://cdn.thenewstack.io/media/2025/12/d3aae05e-image1-905x1024.png)

The diagram illustrates the end-to-end flow of a remote MCP setup. The LLM communicates with an MCP client, which then interacts with a remote MCP server running inside a Kubernetes cluster. The MCP server is packaged as a container image stored in ECR and deployed on EKS, while an application load balancer provides a stable and secure entry point for external traffic.

In practice, this separation was one of the biggest improvements we saw when moving MCP tools off local machines. Once the server ran remotely, teams could update tools without breaking each other’s workflows, logs were no longer tied to a single laptop and we finally had a controlled, observable environment for debugging real production issues. By isolating the LLM from the tools it uses, the architecture becomes significantly easier to operate, maintain and scale.

## **Why MCP Needs a Remote Architecture**

MCP is gaining traction as a standard interface for tools that LLMs can call. In my own early experiments and in team environments, the first instinct was always to run the MCP server process locally. This worked fine during proofs of concept, but the moment multiple engineers or real workloads relied on the same tools, the limitations became obvious. The issues below showed up quickly and repeatedly.

* **Local execution does not scale** — If many users or many LLM invocations hit the tool, a local process cannot handle the load.
* **Difficult to share across multiple environments** — Local tools live only on a single developer machine. They cannot serve workloads from staging, testing or production systems.
* **Limited observability and operational control** — Teams cannot easily monitor logs, metrics or resource use without moving MCP servers into a managed platform.
* **Security and isolation concerns** — Local tools may mix responsibilities and allow unintended access to sensitive systems.

In our case, these pain points were the reason we began shifting MCP tools into Kubernetes. Remote deployment solved the scaling, observability and collaboration challenges that held back local setups and allowed the architecture to grow with the application.

## Why Kubernetes Is a Natural Fit for MCP Servers

When we first moved MCP tools off local machines, Kubernetes quickly became the obvious platform. The moment we containerized the tools and deployed them into a cluster, many of the earlier pain points disappeared. Teams could finally share tools across environments, we gained proper observability, and new versions could be rolled out without breaking existing workflows. Kubernetes provided the operational foundation that local MCP processes were missing.

Kubernetes offers several advantages that make it ideal for MCP workloads:

* **Scalability** — Horizontal pod autoscaling allows MCP servers to grow with demand.
* **Clear separation of concerns** — The LLM stays focused on reasoning and language tasks. MCP servers handle tool execution in isolated containers.
* **Rolling updates** — Teams can deploy new tools or update existing ones without downtime.
* **Network access control** —Ingress rules, security groups and private networking give teams better control of traffic.
* **Observability** —Kubernetes integrates directly with logging, tracing, and monitoring stacks, which helps diagnose issues quickly.
* **Container-based packaging** — Each MCP tool becomes a versioned, tested, and deployable container image.

These capabilities aligned closely with what we needed when scaling AI tooling in production and made Kubernetes the most practical choice for hosting MCP servers at scale.

These capabilities align well with the way modern AI infrastructure is evolving.

## How the Remote MCP Architecture Works

One of the biggest advantages we saw when shifting MCP tools into Kubernetes was the clarity of the request flow. Once everything was remote and observable, it became much easier to understand where latency occurred, where failures happened and how to scale different components independently. The sequence below reflects the pattern that consistently emerged in our production setups.

Below is a simplified explanation of how requests flow through the system.

**1. A user triggers an action —** The user interacts with the application, which prompts the LLM to perform a task.

**2. The LLM creates an MCP tool call —** The LLM sends a tool invocation to the MCP client using the MCP standard.

**3. The MCP client sends the request to the remote server —** The client communicates with the MCP server over HTTP. The server URL is exposed through the Kubernetes ALB.

**4. The ALB routes the request into EKS —** The ALB receives the call and forwards it to the correct Kubernetes service inside the cluster.

**5. The MCP server pod processes the request —** The server runs inside a container built from source code and stored in ECR. It executes the tool logic, handles input output, and returns results.

**6. The result flows back to the LLM —** The response travels back through the same chain: MCP server to ALB to MCP client to the LLM.

**7. The LLM uses the result to continue the workflow —** The LLM integrates the tool output into its reasoning and produces the final response for the user.

In real deployments, this clean separation made troubleshooting far easier and gave teams the ability to observe and scale each stage independently. With proper logs, metrics and routing, we could pinpoint bottlenecks that would have been invisible in a local setup.

## **Sample Kubernetes Deployment for an MCP Server**

Below is a simplified example of how an MCP server might be deployed on EKS.

```
apiVersion: apps/v1
kind: Deployment
metadata:
  name: mcp-server
spec:
  replicas: 2
  selector:
    matchLabels:
      app: mcp-server
  template:
    metadata:
      labels:
        app: mcp-server
    spec:
      containers:
      - name: mcp-server
        image: <aws-account>.dkr.ecr.<region>.amazonaws.com/mcp:latest
        ports:
        - containerPort: 8000
---
apiVersion: v1
kind: Service
metadata:
  name: mcp-service
spec:
  type: NodePort
  selector:
    app: mcp-server
  ports:
  - port: 80
    targetPort: 8000
---
apiVersion: networking.k8s.io/v1
kind: Ingress
metadata:
  name: mcp-ingress
spec:
  ingressClassName: alb
  rules:
  - http:
      paths:
      - path: /
        pathType: Prefix
        backend:
          service:
            name: mcp-service
            port:
              number: 80
```

This is sufficient for a minimal remote MCP setup.

## Key Benefits of a Remote MCP Architecture

One of the biggest realizations we had when scaling MCP-based tooling was that the architecture itself mattered as much as the tools. Running MCP servers on Kubernetes unlocked a set of practical benefits that were impossible to achieve with local processes or ad hoc deployments. These are the advantages that consistently showed up in real engineering use cases.

* **Independent scaling of tool workloads —** Some tools require far more compute than others. By isolating each MCP server in its own pod, the system can scale them independently without affecting the rest of the pipeline.
* **Clear operational boundaries —** The LLM remains focused on reasoning and orchestration, while MCP servers handle the actual tool execution. This separation keeps responsibilities clean and prevents cross-component failures.
* **Easy upgrades and experimentation —** Teams can roll out new versions of MCP tools, upgrade dependencies, or test new capabilities without touching the production LLM workloads. This dramatically reduces the risk of breaking downstream workflows.
* **Support for many tools at once —** An EKS cluster can host dozens or even hundreds of tool containers. Each tool can evolve at its own pace, which is useful when multiple teams contribute different capabilities.
* **Better security posture —** Ingress controls, virtual private cloud boundaries, identity and access management roles and container isolation make it easier to protect sensitive data and ensure that each tool has only the access it needs.
* **Ideal for enterprise AI —** Organizations in financial services, healthcare and other high-trust domains benefit from predictable, auditable and scalable architectures. Kubernetes brings the structure and observability required to meet those standards.

In practice, these benefits are what turned this architecture from an experiment into something that could support real production AI systems at scale.

## Conclusion

The Model Context Protocol is opening the door to a new class of tool-based AI workflows, but most early implementations still live on individual laptops or ad hoc local servers. In my experience working with production AI systems, that gap between experimentation and real deployment becomes obvious very quickly. The more teams rely on MCP tools, the more they need predictable environments, audit trails, scaling capabilities and clean operational boundaries.

Running MCP servers on Kubernetes provides a practical way to meet those needs. By separating the LLM client from the tool implementation, teams gain the ability to deploy and update tools independently, track behavior through centralized logging and scale individual tools based on workload. This also gives engineers a safer space to experiment with new MCP capabilities without disrupting production LLM pipelines.

As MCP adoption grows, I expect these cloud native patterns to become the default for AI engineering teams. The organizations that succeed with AI at scale will be the ones who treat tooling as first-class infrastructure, not as local scripts. Kubernetes offers the reliability and structure needed to support that shift, and the architecture I’ve outlined reflects what I have seen work effectively in real enterprise environments.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://thenewstack.io/wp-content/uploads/2025/12/5499d6b6-cropped-92882add-nikhil-kassetty-600x600.jpg)

Nikhil Kassetty is an engineer and architect with deep experience in AI-powered systems, payments and cloud native platforms. His work focuses on designing scalable, reliable technologies that drive real-world impact across financial and digital ecosystems. He is also a speaker,...

Read more from Nikhil Kassetty](https://thenewstack.io/author/nikhil-kassetty/)