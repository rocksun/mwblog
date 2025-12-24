It has been established that observability is essential to understand how our systems are performing and when something goes wrong with them. Through my work with enterprises adopting observability services for their critical cloud native workloads, I see observability is adopted in silos. The requests are often separated: focusing on application traces or only on Kubernetes metrics/logs or only on CI/CD [pipelines telemetry](https://thenewstack.io/the-case-for-telemetry-pipelines/).

However, my approach is to think about end-to-end observability from Day 1 and not treat it as a bolt-on.

Here’s a demonstrated end-to-end [observability](https://thenewstack.io/introduction-to-observability/) framework using a simple two-microservices application built/deployed on a managed Kubernetes cluster through CI/CD pipelines. It focuses on the telemetry that can be collected from each layer— application, [Kubernetes](https://thenewstack.io/kubernetes/) and [CI/CD](https://thenewstack.io/introduction-to-ci-cd/) — and how each contributes to faster troubleshooting and better system health.

## **Application and Observability Architecture**

Image 1 shows the architecture, including telemetry collection. The demo application includes two microservices — retail-web and retail-api — running on a managed Kubernetes cluster in a cloud environment. For this application, observability is covered through the following strategy:

* Traces from the application are collected using [OpenTelemetry collector](https://opentelemetry.io/docs/collector/), which offers a vendor-agnostic way to receive, process and export telemetry data.
* Logs from Kubernetes cluster are collected using [fluentd](https://www.fluentd.org/) daemonsets (one log collection pod per node).
* Kubernetes infrastructure metrics are collected using the cloud platform’s proprietary agent. This could also be done using a Prometheus Node Exporter.

Because this application runs on a cloud platform, telemetry from cloud native components such as CI/CD pipelines, compute nodes and the Kubernetes control plane is collected through the platform’s observability services.

This demo retail application is focused on one feature: the checkout request. The [user’s checkout request hits the load balancer](https://thenewstack.io/stop-losing-users-the-load-balancing-fix-your-website-needs/), and is processed by the web frontend, which calls the API backend. The API backend then executes the three key operations – checking inventory, charging payment and creating the order, then all three operations hit a database. The API backend uses SQLite for demonstration purposes; in production, this would be a managed database service. The observability patterns remain applicable regardless of the underlying database.

**Note**: A managed Kubernetes environment also includes several other cloud-managed components, such as [networking and load balancing](https://thenewstack.io/zero-trust-for-legacy-apps-load-balancer-layer-can-be-a-solution/). It’s important to enable and monitor their telemetry as well since these services directly affect the reliability of Kubernetes workloads.

[![](https://cdn.thenewstack.io/media/2025/12/5c123218-image8.png)](https://cdn.thenewstack.io/media/2025/12/5c123218-image8.png)

Image 1

## **Capturing Application Traces with OpenTelemetry**

A trace captures the end-to-end journey of a single user request. A single trace is made up of multiple spans depending on how the request traverses the distributed system. In my application, a single user request starts when the user hits the Checkout button on the UI, moving on to the backend and SQLite database. A single trace tracking this request will have multiple spans and, in this example, individual spans will capture every HTTP request and operations such as “verifying inventory,”“executing payment”and “create order” as shown in Image 2.

[![Trace = Collection of Spans](https://cdn.thenewstack.io/media/2025/12/45f35491-image10.png)](https://cdn.thenewstack.io/media/2025/12/45f35491-image10.png)

Image 2

The application uses a mix of OpenTelemetry auto-instrumentation (for Flask and HTTP calls) and manual spans (around the business logic stages), and all spans are exported through the OpenTelemetry (OTel) Collector, which enriches them with Kubernetes metadata before sending them to the cloud native application performance service.

Image 3 shows a code snippet from my telemetry module, where I define a custom `bootstrap()` function. This function configures OpenTelemetry for my service by setting resource attributes such as `service.name`, `service.namespace`, and `deployment.environment`. These attributes become part of every span.

Inside the same function, I initialize an OpenTelemetry TracerProvider and attach an OTLP (OpenTelemetry Protocol) span exporter, which is the component responsible for sending spans to the next destination in the pipeline, which in this case is the OTel Collector.

[![](https://cdn.thenewstack.io/media/2025/12/445f4526-image9.png)](https://cdn.thenewstack.io/media/2025/12/445f4526-image9.png)

Image 3

### **If You’re New to OpenTelemetry**:

OpenTelemetry Protocol (OTLP) is the standard way telemetry signals (traces, logs, metrics) are transmitted between components. The OTLP span exporter sends spans to whichever OTLP endpoint is configured.

Although an OTLP span exporter candirectly send traces to an application performance monitoring (APM) backend, I intentionally send them to the OTel Collector instead. There are two reasons for this:

1. **Vendor neutrality and futureproofing.**  
   When the collector sits between the application and APM backend, I can route the same traces to any backend (Grafana Tempo, Jaeger, [cloud native APM](https://thenewstack.io/streamlined-apm-integration-in-cloud-native-buildpacks/) services, etc.) without modifying application code.
2. **Span enrichment and processing.**  
   I use the collector to inject Kubernetes metadata (pod name, node name, deployment, etc.) into spans. The collector can also perform batching, sampling, transformations and routing, if needed.

Image 4 shows a code snippet with an auto-instrumentation section inside `bootstrap()`. Here, I enable OpenTelemetry’s instrumentation libraries for:

1. **Requests** (Python’s HTTP client) to automatically create client-side spans whenever the application makes outbound HTTP calls (such as `retail-web` calling `retail-api`).
2. **Flask** to automatically create server-side spans whenever the application receives inbound HTTP requests.

Without the RequestsInstrumentor, the downstream API calls would not appear as part of the same trace, and the distributed parent-child relationship would be lost. Flask instrumentation handles inbound traffic, while requests instrumentation handles outbound calls. Because microservices often call each other, both are required to maintain a complete distributed trace.

[![](https://cdn.thenewstack.io/media/2025/12/e15ecf5f-image12.png)](https://cdn.thenewstack.io/media/2025/12/e15ecf5f-image12.png)

Image 4

Image 5 shows a code snippet from the application file (app.py), where the `bootstrap()` function is called immediately after creating the Flask application instance. This is what activates auto-instrumentation for the running service and applies the resource attributes defined earlier.

[![](https://cdn.thenewstack.io/media/2025/12/7212aca8-image11.png)](https://cdn.thenewstack.io/media/2025/12/7212aca8-image11.png)

Image 5

Manual instrumentation means explicitly creating spans in your application code to capture business logic, database operations or any work that auto-instrumentation cannot infer.

In the retail-web service, by the time `/checkout/execute` handler runs, Flask auto-instrumentation has already created a SERVER span for the HTTP request. In the handler, I fetch that span with `trace.get_current_span()` and then I add a manual parent span called `Process_Checkout_Flow` with three child spans: `Verify_Inventory_Status`, `Execute_Payment_Charge` and `Create_Order_Record`. `Process_Checkout_Flow` sits between the HTTP-level SERVER span and these business steps. These spans map directly to my business steps, and I attach attributes like `retail.flow` and `retail.stage` so I can later filter traces by flow and stage if I want to.

Image 6 below is the code showing the manual parent span and business span for the verifying inventory step.

[![](https://cdn.thenewstack.io/media/2025/12/d587aec6-image14.png)](https://cdn.thenewstack.io/media/2025/12/d587aec6-image14.png)

Image 6

Image 7 below shows the full span tree for one checkout request. The first span, `retail-web: POST /checkout/execute`, is the entry-point server span created automatically by the Flask auto-instrumentation. The next span, `retail-web: Process_Checkout_Flow` and the nested spans underneath it (inventory check, payment charge and order creation) are manually instrumented. These manual spans come from the code-level instrumentation as shown in image 6.

[![](https://cdn.thenewstack.io/media/2025/12/e3a92efa-image13.png)](https://cdn.thenewstack.io/media/2025/12/e3a92efa-image13.png)

Image 7

Auto and manually instrumented spans serve different purposes. If the latency comes from auto-instrumented spans, it can be attributed to overhead processes such as network connectivity issues whereas if it’s coming from manually instrumented spans, then it’s mostly because of application logic such as inefficient loops.

OpenTelemetry generates three types of spans:

* **Server spans** — created whenever a service receives an incoming HTTP request (such as retail-web receiving `POST /checkout/execute`, retail-api receiving `GET /inventory/check`).
* **Client spans** — created whenever a service makes an outgoing HTTP call (such as retail-web calling retail-api). These show the outbound portion of the round-trip.
* **Internal spans** — spans created inside the service to represent internal units of work. All manual spans (such as `Process_Checkout_Flow`, `Verify_Inventory_Status` `Execute_Payment_Charge`, DB operations) fall under this category because they represent code-level operations performed within a service, and I didn’t explicitly set the span kind to any other type. Image 8 below shows different types of spans in the span tree.

[![](https://cdn.thenewstack.io/media/2025/12/3a83c00c-image16.png)](https://cdn.thenewstack.io/media/2025/12/3a83c00c-image16.png)

Image 8

I used the OTel Collector to enrich spans with Kubernetes context. Image 9 shows how I configured the OTel Collector to extract Kubernetes metadata.

[![](https://cdn.thenewstack.io/media/2025/12/42f0256a-image15.png)](https://cdn.thenewstack.io/media/2025/12/42f0256a-image15.png)

Image 9

Once this configuration is applied, every span sent through the collector includes Kubernetes attributes as shown in Image 10. This enrichment becomes extremely valuable when troubleshooting performance issues. If a span slows down, I can immediately see which pod and node executed the code.

[![](https://cdn.thenewstack.io/media/2025/12/0a284913-image19.png)](https://cdn.thenewstack.io/media/2025/12/0a284913-image19.png)

Image 10

## **Observability for Managed Kubernetes Environments**

In a managed Kubernetes environment on a cloud platform there is a shared responsibility model. The cloud provider manages the Kubernetes control plane components such as API server, etcd, scheduler, controller manager, node provisioning and exposes only the logs or metrics that the platform chooses to make available for control plane. Everything that runs inside the nodes (pods, containers, application processes) is fully user-managed and the user needs to own their observability setup.

In essence, while all major managed platforms (Oracle, Google, Amazon, Azure) expose control plane metrics for their managed Kubernetes, but a user must generally opt-in or use the provider’s native monitoring solution to consume them. Essential control plane metrics include API server requests, API server request latency and etcd latency to understand how the control plane is performing and raise service tickets with the cloud provider when you see unexpected behavior.

**Node Health** – Understanding node health is important as nodes are the basis where application workloads run. A good starting point is to keep a watch on node-level metrics as they are our early warning system for resource exhaustion. Image 11 shows CPU utilization for 3 nodes belonging to a Kubernetes cluster. Here we see equal distribution across three nodes, and that’s healthy. If one metric line was at 10% while the other was at 95%, that would have shown that one node is overburdened while the other is underutilized.

[![](https://cdn.thenewstack.io/media/2025/12/e5871842-image17.png)](https://cdn.thenewstack.io/media/2025/12/e5871842-image17.png)

Image 11

Logs also can provide insights.Logs can help in troubleshooting, but they also make for a great overview like the node health summary shown in Image 12. Through this widget, I highlight all three pressure values for each node, which contributes to the readiness of a node to host pods. These conditions come directly from kubelet and are surfaced in node status.

[![](https://cdn.thenewstack.io/media/2025/12/dae63044-image18.png)](https://cdn.thenewstack.io/media/2025/12/dae63044-image18.png)

Image 12

The node-pod correlation is important, providing the status of pods running on nodes. Image 13 shows a machine-learning-based visualization that brings multiple dimensions together: node, namespace, pod status and count of pods. This makes it easy to spot patterns such as uneven pod placement, pods stuck in pending/failed states or nodes consistently hosting problematic workloads. That’s the real power of observability: being able to see relationships rather than isolated metrics.

[![](https://cdn.thenewstack.io/media/2025/12/0b75a7d2-image21.png)](https://cdn.thenewstack.io/media/2025/12/0b75a7d2-image21.png)

Image 13

**Pod Health**

Logs from pods can be used to provide snapshots like Image 14 which shows details of all running pods including namespace, placement, controller and controller kind.

[![](https://cdn.thenewstack.io/media/2025/12/106f08fb-image22.png)](https://cdn.thenewstack.io/media/2025/12/106f08fb-image22.png)

Image 14

But for understanding pod health simply knowing pod phase (Running / Pending / Succeeded / Failed / Unknown) is not enough. A pod may show a Running phase while still being unhealthy because the phase only reflects the life cycle state, not whether the container is reachable or functioning correctly.

Image 15 is a good example. The pod phase highlighted is running but when I correlated it with Kubernetes Events, I found “readiness probe failure.” This correlation exposes the actual truth:Pod status does not equal pod health. Health depends on signals such as readiness, liveness, restart counts and probe failures. These rarely show up in the high-level phase alone. This is where observability helps by connecting pod logs, events and metrics together so that the “real” health becomes visible.

[![](https://cdn.thenewstack.io/media/2025/12/4c315567-image23.png)](https://cdn.thenewstack.io/media/2025/12/4c315567-image23.png)

Image 15

## **Gaining Insights from CI/CD Pipeline Observability**

In CI/CD setup, metrics and logs give developers a feedback loop that improves reliability and accelerates shipping code. Here I focused on observability signals from build and deployment pipelines for retail-web and retail-api microservices, using cloud-native DevOps telemetry.

### **Build Pipeline Trends**

Images 16 and 17 show metrics graphs showing successful and failed build trends for both microservices.

For successful builds, we want to see this line maintain a healthy level, but if the successful builds line drops relative to the expected number of builds, it tells us something important about the quality of code being merged or the stability of our testing environment.

[![](https://cdn.thenewstack.io/media/2025/12/cb22aa80-image24.png)](https://cdn.thenewstack.io/media/2025/12/cb22aa80-image24.png)

Image 16

The failed builds chart is a timeline of developer frustration. What immediately stands out is the large spike in the light blue line, representing the retail-api pipeline. This immediately prompts the DevOps engineer to ask: ‘What was committed right before that time? Did we introduce a breaking change, an incompatible dependency or a configuration error?

[![](https://cdn.thenewstack.io/media/2025/12/06cde2c4-image26.png)](https://cdn.thenewstack.io/media/2025/12/06cde2c4-image26.png)

Image 17

### **Build Run Duration (P95)**

Next, we look at the P95 build run duration, which tells us the time it takes for our code to go through the build and test process.

What is P95? P95 build duration tells us how long 95% of builds take, which is much more useful than averages.

In Images 18 and 19 show a consistent pattern that failed builds take significantly longer than successful ones. This signals that failures in this example are happening late, after lengthy test runs.

[![](https://cdn.thenewstack.io/media/2025/12/1f7e2ee3-image27.png)](https://cdn.thenewstack.io/media/2025/12/1f7e2ee3-image27.png)

Image 18

[![](https://cdn.thenewstack.io/media/2025/12/9a795148-image28.png)](https://cdn.thenewstack.io/media/2025/12/9a795148-image28.png)

Image 19

The fix is to “shift left”: Add earlier validation so builds fail fast, saving compute time and improving developer experience.

### **Deployment Pipeline Trend**

Image 20 shows deployment failure counts per hour for both retail-web and retail-api pipelines.

Notice the retail-web pipeline (dark blue) shows a persistent level of failure with distinct spikes. This tells us the problem isn’t necessarily the code itself, which passed the build. This indicates environmental or configuration issues like image pull errors, networking timeouts, missing secrets or Kubernetes API throttling.

[![](https://cdn.thenewstack.io/media/2025/12/9a54c6d0-image29.png)](https://cdn.thenewstack.io/media/2025/12/9a54c6d0-image29.png)

Image 20

Observing deployment failures helps separate code-level issues from cluster-level problems, which keeps [developers focused while DevOps teams debug the actual bottleneck](https://thenewstack.io/2-ways-to-reduce-bottlenecks-with-the-theory-of-constraints/).

### **Deployment Execution Time (P95)**

P95 deployment duration for both services shows high variance with dramatic spikes shown in Images 21 and 22. Instead of a flat, stable line, we see high, dramatic spikes and dips.

The time it takes to deploy our code is highly unpredictable. It might take one minute on one day, and over 11 minutes to deploy on another day.

Investigating logs from the CI/CD system helps identify whether it’s the registry, network, cluster API or rollout strategy causing the slowdowns.

[![](https://cdn.thenewstack.io/media/2025/12/be01c203-image4.png)](https://cdn.thenewstack.io/media/2025/12/be01c203-image4.png)

Image 21

[![](https://cdn.thenewstack.io/media/2025/12/a928e156-image5.png)](https://cdn.thenewstack.io/media/2025/12/a928e156-image5.png)

Image 22

## **From Raw Logs to Intelligent Insights with AI**

We’ve tracked our build and deployment failures but diagnosing them from thousands of log lines is painful. This is where log clustering becomes a real accelerator. The platform applies machine learning-based clustering to automatically group similar log patterns together.

In Image 23 over 3,000 raw log entries from the retail-web build pipeline were reduced into just 52 clusters immediately highlighting recurring issues and outliers.

Now we can focus on the big picture: spotting recurring failure signatures or configuration errors that might otherwise be buried in noise.

[![](https://cdn.thenewstack.io/media/2025/12/dfe7d73c-image6.png)](https://cdn.thenewstack.io/media/2025/12/dfe7d73c-image6.png)

Image 23

Taking it one step further, Image 24 shows how an AI assistant summarizes these clusters in plain language. By correlating logs across 52 clusters, it can surface probable causes behind recurring errors such as why `BUILD_EXECUTION Failed` appears or whether it overlaps with authentication issues, missing dependencies or pull-rate limits

This does not replace an engineer’s expertise. Instead, it acts as a copilot that accelerates reasoning, highlights relationships across log patterns and reduces time-to-root-cause.

[![](https://cdn.thenewstack.io/media/2025/12/65dddd84-image7.png)](https://cdn.thenewstack.io/media/2025/12/65dddd84-image7.png)

Image 24

**Conclusion**

With this article my goal is to give readers a practical, end-to-end view of what observability can look like across your application, your Kubernetes environment and your delivery pipelines. I hope the lessons help you build systems with observability as the first-class design principle.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://thenewstack.io/wp-content/uploads/2025/12/a395c311-cropped-fc7862ca-khushboo-nigam-600x600.jpeg)

Khushboo Nigam is a principal cloud architect at Oracle, where she specializes in holistic observability strategies for enterprise. Her work focuses on helping organization unify telemetry across the entire stack — from cloud infrastructure to modern distributed systems and enterprise...

Read more from Khushboo Nigam](https://thenewstack.io/author/khushboo-nigam/)