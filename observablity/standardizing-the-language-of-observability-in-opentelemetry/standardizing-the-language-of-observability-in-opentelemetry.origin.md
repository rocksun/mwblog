# Standardizing the Language of Observability in OpenTelemetry
![Featued image for: Standardizing the Language of Observability in OpenTelemetry](https://cdn.thenewstack.io/media/2025/03/c97cb128-dashboard-1024x576.jpg)
As companies look to more closely track the real-time health of their applications, many are running into a common challenge: too many tools providing different formats, signals and values. With almost 90% of teams using between two to 10 [observability](https://thenewstack.io/observability/) tools, the hard part is getting them all to play nicely together.

Often, different instrumentations will use their own terminology to refer to observability signals or attributes. And there’s no interoperability between them. While one might call an executed prompt a query, others call it an operation or a function. Or one might refer to an operation runtime as duration, while another refers to it as latency. And for teams tasked with monitoring for potential performance issues as well as optimizing cloud spend, these discrepancies are a major headache.

Just like trying to combine two spreadsheets where column names don’t match and values might not align, different naming conventions across systems create unnecessary complexity.

While developers often create scripts or data processors to automate the collection process, a lot of this work is still being done manually, making maintaining these tools and keeping them in sync with evolving naming patterns increasingly challenging. This monopolizes valuable time that could otherwise be spent delivering new products and capabilities. It can affect how quickly organizations are able to detect issues within their applications.

The impact is twofold: Critical [metrics](https://thenewstack.io/observability-working-with-metrics-logs-and-traces/) might be overlooked because they’re stored under an unexpected name, and seemingly functional dashboards can suddenly break when someone changes a metric name somewhere in the pipeline, leaving teams confused about what went wrong.

As application environments grow more complex, demands on budgets more intense and delays in troubleshooting more financially devastating, companies must be able to instantly understand the activity of all their applications, regardless of which tools or instrumentation they’re using.

Clear, consistent semantic conventions for telemetry signals unlocks more sophisticated approaches to observability across the open source software ecosystem focused on interoperability and avoiding vendor lock-in. With [OpenTelemetry’s ever-growing list of common naming schemas](https://thenewstack.io/opentelemetry-and-elastic-common-standard-comes-not-too-soon/), enterprises now have a set of standardized conventions to help streamline their workflows.

No longer is observability handled in silos. Increasingly, users can simply specify the metric they want to track, and the supporting platform should work across underlying tools and programming languages to produce the uniform intelligence that enterprises need to get better control over their IT landscape.

Here’s how the rise of semantic conventions for telemetry signals is poised to upend observability.

## A Gradual Solution
Creating standard naming conventions is difficult work. It can take months, if not longer. Once initial terminology is agreed upon and prototypes are released to the public, OTel developers then consolidate feedback across many users, spanning all the major programming languages and can tweak the naming convention, add clarification or completely scrap parts of the convention.

During this time, the conventions are considered “in development,” and users can expect some disruption. But this community-driven approach helps ensure that once the conventions are eventually stabilized, they are actually adopted in the real world across a wide and varied user base. In fact, a large amount of feedback often signals huge demand among developers.

It’s a constant effort to improve proposed conventions, as well as add new terminology. But once schemas are listed as “stable,” the term becomes the de facto standard, giving developers the confidence to now cement their workflows around.

## Better Dashboards, Faster
Because of the wide array of existing terminology, vendors providing the underlying observability platforms struggle to build uniform templates that could be easily adopted by end users. Without standard naming conventions across different instrumentations, platform operators can’t be sure the dashboards will work across every customer. Instead, it falls to [developers to manually build these dashboards every time](https://thenewstack.io/why-traditional-logging-and-observability-waste-developer-time/), pulling them away from actually delivering the innovations that end customers are demanding.

If observability software providers have a set of common terminology to reference, they could begin to release pre-built dashboards designed around outcomes, not metrics. Right now, most dashboards track insights like CPU usage or memory utilization. But with a set of standardized semantic signals spanning metrics across profiles, logs, traces and spans, platform providers can unify all the metrics needed to, for example, optimize cloud spend, making it easy and quick for organizations to adopt and get value.

And, it creates a more interoperable ecosystem that can help individual developers optimize their own — and their teams’ — environments. Often, they might not even be aware they could collect certain metrics until the semantic conventions are instrumented in their libraries. A shared vocabulary improves cross-team collaboration that literally democratizes access to data across various areas of the business.

The best part: The list of conventions is only going to get longer and better. The more users that begin to adopt these definitions, the more feedback that OTel receives, the faster that standards move from experimental to stable. The more companies can confidently [integrate these standard names and signals into their observability ecosystem](https://thenewstack.io/continuous-integration-observability-explained/), the quicker they can create the interoperability needed to run high-performance applications in the most cost-effective way.

*To learn more about Kubernetes and the cloud native ecosystem, join us at *[KubeCon + CloudNativeCon Europe](https://events.linuxfoundation.org/kubecon-cloudnativecon-europe/)* in London on April 1–4.*
[
YOUTUBE.COM/THENEWSTACK
Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.
](https://youtube.com/thenewstack?sub_confirmation=1)