# Perses Closes the Observability Gap with Declarative Dashboards
![Featued image for: Perses Closes the Observability Gap with Declarative Dashboards](https://cdn.thenewstack.io/media/2025/03/4e879205-perses-1024x570.png)
In the evolving landscape of Kubernetes, microservices and GitOps, observability is critical. While tools like [OpenTelemetry](https://thenewstack.io/what-is-opentelemetry-the-ultimate-guide/), Prometheus and Jaeger have standardized the collection and storage of telemetry data, visualization tools remain fragmented. Infrastructure and applications are managed declaratively, yet [dashboards](https://thenewstack.io/kubernetes/kubernetes-dashboards/) often remain manual, inconsistent and disconnected from [DevOps workflows](https://thenewstack.io/devops/). This misalignment creates friction among developers, site reliability engineers (SREs) and business leaders who rely on consistent metrics.

## The State of Observability Dashboard Tooling
Established tools like Grafana and Kibana excel in visualization and have paved the way for many observability vendors. However, they often struggle to align with modern DevOps workflows. Let’s explore some of the known challenges.

**Manual Workflows and Inconsistency**
Many dashboard tools depend on UI editors or unstructured JSON files. While this approach offers flexibility, it also:

**Creates configuration drift:**Teams duplicate dashboards with slight variations (such as “prod-latency” vs. “production-latency”), leading to confusion during incidents.**Lacks collaboration:**Without codified standards, developers, SREs and business teams may interpret metrics differently.**Ignores GitOps principles:**Changes are rarely tracked in git, making audits and rollbacks cumbersome.
**Partial Automation, Full Complexity**
Some tools offer “as code” workflows via Terraform providers or Kubernetes operators. However, these are often:

**Opaque:**JSON-based dashboards lack human readability and validation safeguards.**Fragile:**Migrating dashboards between environments (dev/staging/prod) often breaks queries or data sources.**Tool specific:**Proprietary formats lock teams into vendors, complicating multicloud strategies.
**The Missing Standard**
The industry lacks a portable, vendor-neutral dashboard specification. This forces teams to:

- Reinvent templates for every tool (e.g., Grafana,
[Datadog](https://www.datadoghq.com/?utm_content=inline+mention)or[New Relic](http://newrelic.com/?utm_content=inline+mention)). - Maintain brittle migration scripts when switching vendors.
- Sacrifice innovation to avoid rework.
**Why Dashboard as Code (DAC) Remains Elusive**
The “as code” paradigm transformed infrastructure (Infrastructure as Code, or IaC), policies (Policy as Code, or PaC) and even documentation (Docs as Code). Dashboards, however, lag because existing solutions:

**Prioritize visualization over governance:**Tools focus on rendering graphs, not managing dashboards as collaborative artifacts.**Neglect cloud native patterns:**Few integrate with custom resource definitions (CRDs), operators or GitOps workflows.**Underestimate scale:**Manual workflows collapse under 100-plus microservices, where consistency and automation are non-negotiable.
Given all these challenges, I would like to introduce you to [Perses](https://perses.dev/), a Cloud Native Computing Foundation (CNCF) Sandbox project designed to simplify dashboard creation and management in cloud native environments. Let’s explore how it addresses these challenges.

## Perses: A Cloud Native Approach to Visualization
Perses rethinks dashboards as declarative artifacts, integrating seamlessly with modern DevOps practices. Designed for the cloud native ecosystem, it offers:

**Declarative Dashboard Definitions**
Perses stores dashboard configurations as code using Kubernetes CRDs. This ensures dashboards are version-controlled, auditable and managed alongside application manifests in git. For teams already using GitOps tools like Argo CD, Perses seamlessly integrates into existing workflows.

**Portability and Flexibility**
Unlike proprietary dashboard tools, Perses prioritizes open standards. Its lightweight architecture integrates with popular data sources like Prometheus and Grafana Tempo, avoiding vendor lock-in. Developers can embed dashboards into internal tools via npm packages while platform teams enforce consistency across environments.

**Collaboration at Scale**
Perses’ programmatic SDKs (Go, Cuelang) empower teams to make dashboard templates, reuse components and automate repetitive tasks. This is especially valuable for enterprises managing hundreds of dashboards, where manual dashboard maintenance quickly becomes unsustainable.

**Security and Governance**
By storing dashboards in Kubernetes namespaces, Perses aligns with role-based access control (RBAC) policies, ensuring visibility is scoped to relevant teams. Compliance audits become simpler as all changes are tracked in git history, providing transparency and accountability.

## Why Perses Stands Out in the CNCF Ecosystem
The CNCF has long supported projects like Prometheus and Grafana, but Perses fills a critical gap. It’s a Kubernetes-native dashboard framework purpose-built for declarative management and portability. Its approach aligns with key industry shifts:

**GitOps adoption:**Treating dashboards as code ensures consistency, version control and seamless integration with existing workflows.**Shift-left observability:**Embedding dashboards earlier in the development cycle improves visibility and collaboration across teams.**Enterprise-ready scalability:**As organizations scale, they need solutions that enforce governance without adding operational overhead.
With sandbox status under CNCF, Perses is on track to become a community-driven standard, much like how OpenTelemetry unified telemetry collection across the ecosystem.

## Learn More at KubeCon
Perses represents a paradigm shift in the way teams approach observability visualization. Embracing cloud native principles and declarative practices removes the friction of traditional dashboard tools, ensuring consistency, scalability and automation.

To see Perses in action and learn how it can streamline your observability strategy, join us at KubeCon + CloudNativeCon Europe for our session, “[Limitless Possibilities, Consistent Design: Crafting Dashboards With Perses DAC](https://kccnceu2025.sched.com/event/1txHy/limitless-possibilities-consistent-design-crafting-dashboards-with-perses-dac-nicolas-takashi-coralogix-antoine-thebaud-amadeus?iframe=no&w=100%25&sidebar=yes&bg=no).”

*To learn more about Kubernetes and the cloud native ecosystem, join us at *[KubeCon + CloudNativeCon Europe](https://events.linuxfoundation.org/kubecon-cloudnativecon-europe/)* in London from April 1–4.*
[
YOUTUBE.COM/THENEWSTACK
Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.
](https://youtube.com/thenewstack?sub_confirmation=1)