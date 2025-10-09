*This excerpt from the first chapter of the Manning book [Platform Engineering on Kubernetes](https://chronosphere.io/resource/platform-engineering-on-kubernetes/?utm_source=sponsored-content&utm_id=TNS) walks through a Kubernetes environment, installing an example conference app with a single command, verifying health and learning core primitives — deployments, ReplicaSets, services and service discovery — while confronting real-world issues like zero downtime, resilience, state/data consistency, security/identity and understanding application behavior. To read the full chapter, you can [download the book](https://chronosphere.io/resource/platform-engineering-on-kubernetes/?utm_source=sponsored-content&utm_id=TNS).*

---

Distributed systems are complex beasts and fully understanding how they work from Day 1 can help you save time when things go wrong. This has pushed the monitoring, tracing and telemetry communities hard to [develop solutions that help explain](https://www.youtube.com/watch?v=4iBU7YpG0Dw&utm_source=sponsored-content&utm_id=TNS) how things are working at any given time.

The [OpenTelemetry (OTel)](https://thenewstack.io/what-is-opentelemetry-the-ultimate-guide) community has evolved alongside Kubernetes, and it can now provide most of the tools you will need to monitor how your services are working. As stated on [its website](https://opentelemetry.io/), “You can use it to instrument, generate, collect and export telemetry data (metrics, logs and traces) for analysis to understand your software’s performance and behavior.”

## Metrics, Logs and Traces

Figure 1 shows a common use case where services [push metrics, traces and logs to a centralized place](https://dev.to/siddhantkcode/the-mechanics-of-distributed-tracing-in-opentelemetry-1ohk) that stores and aggregates the information so that it can be displayed in dashboards or used by other tools.

[![Fig. 1. Aggregating observability from all services in a single place reduces the cognitive load on the teams responsible for keeping the application up and running.](https://cdn.thenewstack.io/media/2025/10/0d0b88b1-aggregating-observability_fig1.png)](https://cdn.thenewstack.io/media/2025/10/0d0b88b1-aggregating-observability_fig1.png)

Figure 1. Aggregating observability from all services in a single place reduces the cognitive load on the teams responsible for keeping the application up and running. (Source: “Platform Engineering on Kubernetes.”)

## OpenTelemetry on Kubernetes: Core Concepts for Platform Engineers

It is important to note that OpenTelemetry focuses on your software’s behavior and performance, because they will affect your users and their user experience. From the behavior point of view, you want to make sure that the application is doing what it is supposed to do. Therefore, you will need to understand which services are calling which other services or infrastructure to perform tasks.

Using Prometheus and Grafana allows us to see the service telemetry and build domain-specific dashboards to highlight certain application-level metrics (for example, the number of approved or rejected conference proposals over time, as shown in Figure 2).

[![Fig. 2. Monitoring telemetry data with Prometheus and Grafana.](https://cdn.thenewstack.io/media/2025/10/40b6f656-monitoring-telemetry_fig2.png)](https://cdn.thenewstack.io/media/2025/10/40b6f656-monitoring-telemetry_fig2.png)

Figure 2. Monitoring telemetry data with Prometheus and Grafana. (Source: “Platform Engineering on Kubernetes.”)

From the performance point of view, you need to ensure that services are respecting their service-level agreements (SLAs), which means they are answering requests promptly. If one of your services misbehaves and takes more time than usual, you want to know.

## The OpenTelemetry Collector: Ingestion, Processing and Export Patterns

[For tracing](https://chronosphere.io/platform/distributed-tracing/?utm_source=sponsored-content&utm_id=TNS), you must modify your services to understand the internal operations and their performance. OpenTelemetry provides drop-in instrumentation libraries in most languages to externalize service metrics and traces.

Figure 3 shows the OpenTelemetry architecture, including [the OpenTelemetry collector receiving information](https://docs.chronosphere.io/ingest/metrics-traces/otel/otel-ingest?utm_source=sponsored-content&utm_id=TNS) from each application agent, as well as shared infrastructure components.

[![Fig. 3. OpenTelemetry architecture and library (Source: https://opentelemetry.io/docs/)](https://cdn.thenewstack.io/media/2025/10/4627f7a7-otel-architecture_fig3.png)](https://cdn.thenewstack.io/media/2025/10/4627f7a7-otel-architecture_fig3.png)

Figure 3. OpenTelemetry architecture and library. (Source: OpenTelemetry docs.)

If you are creating [a walking skeleton](https://www.youtube.com/watch?v=EY13z1XFVmg&t=2s), ensure it has OpenTelemetry built in. If you push monitoring to later stages of the project, it will be too late — things will go wrong, and finding out who is responsible will take too much time.

### Application Security and Identity Management

If you have ever built a web application, you know that providing identity management (user accounts and user identity) plus authentication and authorization is quite an endeavor. A simple way to break any application (cloud native or not) is to perform actions you are not supposed to do, such as (using the conference proposals example above) deleting all the proposed presentations unless you are a conference organizer.

### Propagating Identity in Distributed Systems and OAuth2 at the Edge

Propagating identity becomes challenging in distributed systems because authorization and user identity must be propagated across different services. In distributed architectures, it is quite common to have a component that generates requests on behalf of a user instead of exposing all the services for the user to interact with directly.

In our example, the frontend service where people submit presentation proposals is this component. Most of the time, you can use this external-facing component as the barrier between external and internal services. For this reason, it is quite common to configure the frontend service to connect with an authorization and authentication provider using the OAuth2 protocol.

The figure below shows the frontend service interacting with an identity management service, which is responsible for connecting to an identity provider (e.g., Google, GitHub, your internal LDAP server) to validate user credentials, as well as to provide roles or group memberships that define what the user can and can’t do in different services. The frontend service handles the login flow (authentication and authorization), but only the context is propagated to the backend services once that is done.

[![Fig. 4. Identity management: The Role/Group is propagated to the backend services.](https://cdn.thenewstack.io/media/2025/10/661990a1-identity-management_fig4.png)](https://cdn.thenewstack.io/media/2025/10/661990a1-identity-management_fig4.png)

Figure 4. Identity management: The Role/Group is propagated to the backend services. (Source: “Platform Engineering on Kubernetes.”)

### Privacy, Social Logins and SSO/Identity Providers

An application that doesn’t handle users or their data is good for complying with regulations such as GDPR. But you might want to allow users to use their social media accounts to log into an application without having to create separate accounts. This is usually known as a social login.

Some popular solutions, such as [Keycloak](https://www.keycloak.org/) and [Zitadel](https://zitadel.com/opensource), bring [OAuth2 and identity management](https://blog.gravatar.com/2024/05/10/oauth-2-0-simplified-unraveling-authorization-protocols/) together. These open source projects provide a one-stop shop for single sign-on (SSO) solutions and advanced identity management. Zitadel also provides a managed service that you can use if you don’t want to install and maintain an SSO and identity management component inside your infrastructure.

The same is true with tracing and monitoring. Planning to have users, including SSO and identity management, in the walking skeleton will push you to think about the specifics of “who will be able to do what,” refining your use case even more.

## Learn More

With OTel wired into your Kubernetes “walking skeleton,” you have the foundation to spot regressions fast, prove SLOs and cut mean time to resolution (MTTR) — before the pager goes off.

If you want the end-to-end playbook, including deploying into Kubernetes clusters, CI/CD, collector patterns, identity, delivery pipelines and multicloud infrastructure, [download the full Manning ebook](https://chronosphere.io/resource/platform-engineering-on-kubernetes/?utm_source=sponsored-content&utm_id=TNS) and keep building.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://cdn.thenewstack.io/media/2024/03/ea0dc3f4-cropped-48da2e2e-1709755541792.jpeg)

Mauricio Salatino as the author of Platform Engineering on Kubernetes, he is a software engineer with Diagrid and previously worked at VMware and Red Hat. As an open source enthusiast, Mauricio Salatino has been a program committee member, track chair,...

Read more from Mauricio Salatino](https://thenewstack.io/author/mauriciosalatino/)