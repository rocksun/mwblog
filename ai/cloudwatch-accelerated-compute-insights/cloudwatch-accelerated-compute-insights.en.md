![Abstract monochrome digital terrain with circuit-like fissures representing GPU cluster observability and workload blind spots.](https://cdn.thenewstack.io/media/2026/11/c92a967e-flying-object-jzkpjxphomq-unsplash-1024x576.jpg)

**Accelerator bills have become one of the largest lines in the infrastructure budget.** GPUs have become the most expensive resource in modern computing, and yet most organizations operate them with little visibility. A single training cluster can run for days and cost millions of dollars. Most organizations pool these accelerators across teams on shared clusters to keep them busy. But in these shared environments, platform teams cannot answer basic questions: which team is using which accelerators? Is the inference workload generating tokens efficiently? What is wasting money?

When a workload degrades (a failing accelerator, a thermally throttled node), teams find out only after a run crashes or the bill arrives. The device-level signals needed to find the cause (request traces, kernel logs, memory metrics from the accelerator itself) are not collected or connected. Without a way to isolate the problem to a single accelerator, teams fall back on cycling the entire instance, surrendering seven healthy GPUs to address a fault on one, and often waiting on scarce capacity to get the instance back.

> “GPUs have become the most expensive resource in modern computing, and yet most organizations operate them with little visibility.”

Accelerator observability turns those blind spots into answers. It tells you who is using your accelerators, whether they are healthy, and what the waste is costing you, all the way down to a single device. That way, you fix one bad GPU instead of eight, and spend your accelerator budget on real work instead of idle capacity.

Amazon CloudWatch accelerated compute insights, a new capability launched at KubeCon North America 2026, gives you a single operational view of every accelerator in your fleet. It shows platform and AI teams who are using their GPU and AWS AI Accelerators capacity across Amazon Elastic Kubernetes Service (Amazon EKS). In this post, we walk through what accelerated compute insights does, how it works on Amazon EKS, and how to get started.

## What accelerated compute insights does

Accelerated compute insights gives you a single operational view of every accelerator in your fleet. It shows how each accelerator is being used, detects failures and bottlenecks as they happen, estimates the cost impact of each problem, and connects those findings to the actions that resolve them.

> “Accelerated compute insights holds accelerator telemetry, workload boundaries, and pricing data together, a combination that monitoring tools that only see metrics cannot replicate.”

On Amazon EKS, it supports NVIDIA GPUs and NVIDIA GPUs, AWS Trainium and AWS Inferentia. Metrics from NVIDIA GPUs and Inferentia are normalized into a common schema and presented in a single Accelerator Health view, so teams running mixed fleets manage every accelerator type in one place.

## Fleet visibility with Kubernetes context

Every accelerator in your EKS cluster is enriched with Kubernetes metadata: pod, namespace, node, node group, and custom labels (team, application). You see utilization by team and workload across your entire fleet.

Accelerated Compute Insights auto-detects MIG (Multi-Instance GPU) partitioned GPUs and shows utilization and memory for each MIG instance, along with the pod using it. It also recognizes other partitioning schemes, including Kubernetes DRA ([dynamic Resource allocation](https://thenewstack.io/kubernetes-dra-gpu-scheduling/)) and time-slicing, by reading device labels. No configuration required.

## Cost waste identification

Accelerated compute insights connects real-time accelerator telemetry to workload boundary events and AWS pricing data to surface recoverable waste in three categories:

1. Right-sizing opportunities: workloads running on more powerful instances than the task requires.
2. Training efficiency gaps: low tensor core (MFU) utilization relative to the workload’s own historical baseline, indicating the job is not getting full value from the hardware.
3. Inference below hardware capacity: endpoints serving fewer requests than the hardware supports, based on customer-emitted throughput correlated with device utilization.

For each finding, accelerated compute insights identifies the specific workload or node responsible, helping users troubleshoot and optimize. This works because accelerated compute insights holds accelerator telemetry, workload boundaries, and pricing data together, a combination that monitoring tools that only see metrics cannot replicate.

Note: CloudWatch accelerated compute insights is an operational tool, not a billing or chargeback tool. Cost figures are estimates intended to guide operational decisions. For authoritative cost and usage accounting, continue to use AWS Cost Explorer and the AWS Cost and Usage Report.

When an inference workload experiences performance degradation or inefficient token generation, accelerated compute insights helps identify GPU bottlenecks, inefficient accelerator utilization, and potential resource waste. By automatically collecting and correlating inference performance metrics, request traces, logs, and accelerator telemetry, it provides end-to-end visibility into workload performance and GPU efficiency. With AI-powered insights and troubleshooting capabilities, customers can quickly identify root causes, optimize token throughput, reduce inference latency, and improve accelerator utilization without disrupting healthy workloads.

> “It distinguishes between failure modes that call for different actions. By default, the agent presents a specific, evidence-backed action plan for you to approve.”

You can also route health events to the AWS DevOps Agent for deeper investigation. The agent reasons across accelerator telemetry, CloudWatch logs, recent infrastructure changes, job configuration, and any runbooks you have authored. It distinguishes between failure modes that call for different actions. For example, a node with an accelerating memory-error trend that needs replacement versus a driver issue that clears with a restart. By default, the agent presents a specific, evidence-backed action plan for you to approve. For a faster loop, you can opt in to let it carry out well-understood remediations through AWS APIs on its own.

## How it works on EKS

Collection paths converge at the CloudWatch Metrics API. For NVIDIA GPUs, the CloudWatch agent and NVIDIA Exporter collect device-level metrics. The Unified Accelerator Health Layer normalizes GPU and Inferentia collection paths into a common schema and presents them in a single dashboard.

The diagram below illustrates how Amazon CloudWatch accelerated compute insights provides end-to-end observability for AI inference workloads and accelerator efficiency on Amazon EKS. Customers can install the CloudWatch Observability add-on from the CloudWatch console or CloudWatch Omni to collect NVIDIA GPU metrics and [inference workload performance](https://thenewstack.io/ai-inference-kubernetes-observability/) metrics, logs, and traces. The telemetry data is ingested into CloudWatch’s centralized storage through the CloudWatch OpenTelemetry (OTLP) endpoint. Customers can monitor inference workload performance and GPU utilization directly in the CloudWatch console or leverage CloudWatch Omni and its AI-powered investigation to troubleshoot performance issues, identify accelerator inefficiencies, and optimize resource utilization.

![Diagram illustrating how Amazon CloudWatch accelerated compute insights provides end-to-end observability for AI inference workloads and accelerator efficiency on Amazon EKS.](https://cdn.thenewstack.io/media/2026/11/4ae1026f-image1-1024x317.png)





*Click to enlarge graphic.*

## Getting started on EKS

Install the CloudWatch Observability add-on with OTel Container Insights enabled. The add-on discovers your accelerators and collects everything the dashboard needs. No per-node setup, no agents to manage, no collection pipelines to configure. Your fleet appears in the console within minutes and stays current as nodes join and leave the cluster.

## Step 1: Get your data flowing

If you run self-hosted inference on Amazon EKS, install or upgrade the Amazon CloudWatch Observability EKS add-on to v7.0.1 or above. The add-on discovers every NVIDIA GPU and AWS Inferentia device in your cluster and starts sending OpenTelemetry data, with no per-node setup and no collection pipelines to configure.

You can enable the add-on using eksctl, Helm, or Terraform. Check examples with eksctl and Helm below:

### Using eksctl

```

eksctl create addon \
  --name amazon-cloudwatch-observability \
  --cluster your-cluster-name \
  --region your-region

```

### Using Helm

```

helm repo add aws-observability https://aws-observability.github.io/helm-charts
helm install amazon-cloudwatch-observability \
  aws-observability/amazon-cloudwatch-observability \
  --namespace amazon-cloudwatch --create-namespace

```

## Step 2: Use your data in CloudWatch Omni

Once telemetry is flowing, open CloudWatch Omni. Omni is built for the teams that own the inference code and fix it. Instead of a wall of infrastructure metrics, you get an application-centric view: your [inference workloads](https://thenewstack.io/ai-observability-through-interoperability/) appear next to the services and AI agents that call them, with accelerator health, utilization, and waste tied to each workload.

When an endpoint shows low throughput or a high time to first token, Omni helps you trace the problem to the workload, node, or single accelerator responsible and shows what to change, whether that’s a configuration update or a code fix. You can go from detection to fix without switching tools.

> “Instead of a wall of infrastructure metrics, you get an application-centric view: your inference workloads appear next to the services and AI agents that call them, with accelerator health, utilization, and waste tied to each workload.”

Platform and infrastructure teams who need a fleet-wide view, such as accelerator allocation across many teams, idle capacity, or a cross-account summary, can also see the same data on the accelerated compute insights page in the CloudWatch console.

Ready to see your own fleet? This [documentation](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/Accelerated-Compute-Insights-Get-Started.html) walks you through getting started.

## Where this fits in the Amazon EKS observability stack

Amazon CloudWatch accelerated compute insights builds on the observability foundation we have been shipping for EKS throughout 2025 and 2026: OTel Container Insights for infrastructure metrics, Application Performance Monitoring for application telemetry, and Container Network Observability for the network layer. Accelerated compute insights adds the missing layer, the accelerators themselves. Teams get GPU and Inferentia utilization, cost waste, and device-level health, all enriched with Kubernetes metadata and connected to automated remediation, in the same place they already monitor everything else

## Getting started today

Amazon CloudWatch accelerated compute insights is available today in all [Regions](https://aws.amazon.com/about-aws/whats-new/2026/10/amazon-cloudwatch-omni-8-regions/) where CloudWatch Omni is available. To get started:

1. Install or upgrade to the latest CloudWatch Observability EKS add-on on your cluster.
2. Open CloudWatch Omni to see your inference workloads, with accelerator health and waste for each one.
3. Troubleshoot and optimize from the workload view, from time to first token down to a single device.

Check out the [documentation](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/Accelerated-Compute-Insights.html) for more.

The post [Expensive accelerators, no workload-level visibility: Introducing Amazon CloudWatch accelerated compute insights](https://thenewstack.io/cloudwatch-accelerated-compute-insights/) appeared first on [The New Stack](https://thenewstack.io).