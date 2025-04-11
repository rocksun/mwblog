# OTel, Elastic Collaborate to Make Observability More Accessible
![Featued image for: OTel, Elastic Collaborate to Make Observability More Accessible](https://cdn.thenewstack.io/media/2025/01/f74f19ca-otel-elastic-collaborate-make-observability-more-accessible-1024x576.jpg)
As it stands today, observability tools aren’t accessible to everyone. Open standards do their part to ease interoperability and reduce vendor lock-in, but taking the time to sufficiently understand and adopt many different standards is its own challenge. Elastic is hoping to accelerate adoption through its work with [OpenTelemetry](https://opentelemetry.io/) (OTel), the open source, vendor-neutral collection of telemetry APIs, software development kits (SDKs) and tools for analyzing software performance and behavior.

Elastic’s collaboration with OpenTelemetry ramped up in 2023 when the company [donated Elastic Common Schema (ECS)](https://thenewstack.io/opentelemetry-and-elastic-common-standard-comes-not-too-soon/) and, in 2024, [Universal Profiling](https://sdtimes.com/softwaredev/elastics-donation-of-universal-profiling-agent-to-opentelemetry-further-solidifies-profiling-as-core-telemetry-signal/) to OTel. “Instead of having another computing standard, by donating we’re helping reduce the number of standards,” explained Miguel Luna, OpenTelemetry product lead, Elastic Observability, in an interview with The New Stack. “Once that happened, we realized that OpenTelemetry is the way forward, and we decided to go all in and start working with the community.”

Go all in, it has. Since the donation of ECS, Elastic has consistently been among OpenTelemetry’s top three contributing companies — but Luna stressed that its real goal is to see OpenTelemetry succeed.

## Standardizing Telemetry Data: Why It Matters
OpenTelemetry gives users a standardized way to instrument, generate, collect, and export traces, metrics and logs. The project made [significant advancements in 2024](https://thenewstack.io/why-the-latest-advances-in-opentelemetry-are-significant/) — and there’s already [a lot to be excited about in 2025](https://thenewstack.io/observability-in-2025-opentelemetry-and-ai-to-fill-in-gaps/).

From Luna’s point of view, it’s semantic conventions and resource attributes that users should be paying attention to: “There are plenty of tools out there that do the work of collecting metrics, logs and traces, but all data is not treated the same way. Now, with semantic conventions, we can all agree on what the metrics, logs or other signals are called, regardless of what mechanisms you use to collect data.”

In this way, semantic conventions unify telemetry data and provide a path forward to unified observability pipelines. Meanwhile, resource attributes enrich this data to more clearly understand which entities emit the telemetry.

Standardizing telemetry data enables using semantic conventions and resource attributes to consolidate fragmented observability pipelines into a unified framework. This, in turn, helps pave the way for simplified telemetry pipelines in diverse and heterogeneous environments.

It’s also a win for organizations that are afraid of vendor lock-in. With consistent, uniform telemetry data, you don’t have to reinstrument your applications every time you want to change vendors. As Luna explained, “Your telemetry becomes more portable. If you decide you want to change to a different vendor, then OpenTelemetry will allow you to do that.”

Additionally, the uniformity provided by semantic conventions and resource attributes holds promise to help teams with debugging and performance monitoring. With signals enriched in a standardized way, teams have a common language to correlate different logs, traces and metrics. Enabling teams to work and diagnose issues from the same vantage point simplifies debugging, monitoring and even maintenance. For a lot of organizations, this is a total 180° from their current approach.

“Today, most companies are collecting some signals using a vendor’s proprietary collection mechanism, but that doesn’t necessarily guarantee a unified way to enrich these signals,” explained Luna. While it’s certainly not impossible to work this way, it makes problem-solving and maintenance much more labor-intensive — especially when dealing with changes down the line, such as artifact upgrades.

## Uniform Telemetry Data Drives Accessibility
Uniformity will simplify pipelines, reduce vendor lock-in and streamline debugging activities, but perhaps most impactful will be its effects on accessibility. According to Luna, this is the issue holding most organizations back — and it’s high time that observability was made more easily accessible for everyone.

“Users shouldn’t have to care about all the specifics of telemetry of the entity they’re observing,” asserted Luna. “Users care about entities; they care about the things they’re observing. But when we force them to care about the logs, traces and metrics that you need to process, transform and export, we make the barrier very high.”

Interoperability issues have been a plague on the observability market, and some speculate it’s [the reason behind observability’s gross undervaluation](https://thenewstack.io/the-looming-crisis-in-the-data-observability-market/). In many ways, the root of the problem is that, up until now, data processing and collection has been very proprietary. Historically, most users have sourced telemetry data from vendors’ proprietary data-collection mechanisms, which means they were on the hook for understanding different standards and different ways of processing data.

When you zoom in and look at the problem close up, Luna said, it’s even more complex than most people realize: “Many people think that when you mention ‘user,’ it’s just one single person who’s collecting telemetry data, and if that person understands the process, then everything is OK. But the reality is very different.”

In practice, more often than not, most organizations have centralized teams working on observability, e.g., providing Observability as a Service (OaaS) to platform engineering teams (Kubernetes as a Service) or [DevOps teams](https://roadmap.sh/devops). This is where things get tricky. Not only does the entire platform engineering team need a single, unified way to collect data, but they need a simple solution to help other teams (in this example, the application team) democratize their telemetry/observability data.

To add to the confusion, infrastructure/platform teams and application teams usually have very different incentives. After all, application teams want to focus on their work — evolving and advancing their applications — not waste time becoming observability experts.

Therein lies the issue. For years, anyone who wanted to observe needed to have a certain level of expertise in order to work with telemetry data. But perhaps the tides are starting to turn. According to Luna, this is where Elastic is helping to make a change.

## OpenTelemetry Adopters Still Face Challenges
If the future of observability is simplification and a smoother user experience, then OpenTelemetry is indeed taking a step in the right direction — and the new [Elastic Distributions of OpenTelemetry (EDOT)](https://www.elastic.co/observability-labs/blog/elastic-distributions-opentelemetry) are helping.

EDOT was developed to enhance the capabilities of standard OpenTelemetry distributions and provide commercial support for OpenTelemetry SDKs and components through Elastic. Luna said the real goal of EDOT is to simplify deployment and configuration to create an out-of-the-box experience so that anyone who wants to work with OpenTelemetry has a consistent experience. Additionally, if they have issues, they can get help from Elastic’s support teams. It’s a notable step forward, but there are still more challenges ahead for OpenTelemetry adoption.

For many, the biggest hurdle is setting up and maintaining OpenTelemetry pipelines. Particularly for users who don’t have a built-in integration with specific receivers (e.g., [Kubernetes](https://roadmap.sh/kubernetes)), they must put in the work to understand how to use OpenTelemetry. As Luna broke it down, “These users might be able to collect telemetries from an endpoint, but since the collector doesn’t know where the data is from, the user will have to get more involved.” In other cases, a receiver may be available, but it may not be technology-specific; once again, users will need to have a deep understanding of OpenTelemetry in order to translate the data into OpenTelemetry-compatible signals.

Luna also pointed out that OpenTelemetry has a mixed maturity state: “The collector is a battle-tested machine, but there are receivers, processors and exporters that have been newly contributed. You need to consider: What is the stability of these components? Are they properly maintained?”

Again, this is where EDOT is supposed to help. Luna said Elastic has carefully curated a stable, widely used set of receivers, processors and exporters. All OTel signals are then stored in Elasticsearch, a unified backend that preserves OTel data natively. Kibana enhances this with dedicated content packages, providing dashboards and assets for seamless analysis. “We are being intentionally selective about which components we’re bringing. We’re also giving users a lot of clarity about how we can support these components and be there for users,” he added.

Still, even with EDOT’s included configurations, Luna cautioned that users will need to consider their specific situation and what level of support best suits their organization. While some teams will be just fine with community-level support, others with higher requirements and more stringent service level agreements (SLAs) will need something more. All of the enhancements and fixes made to EDOT are regularly upstreamed back into OpenTelemetry.

## Start With a Purpose: Understand OpenTelemetry’s Impact
For organizations that want to adopt OpenTelemetry and enhance their observability practices, Luna offered some words of advice.

The first thing to consider is your motivation: Why do you want to adopt OpenTelemetry? Getting clear on this before going in will help you better understand what you might have to give up in the short term in order to align with OpenTelemetry’s data model. Beyond that, he chalked up understanding semantic conventions as the key to smooth OpenTelemetry adoption: “If you’re adopting OpenTelemetry, you should understand why it’s important for you and how you’re going to use it.”

Once again, it all comes back to understanding and accessibility. Observability has typically been a pretty opaque game, where only the players with a deep understanding of the ins and outs of observability get the real advantages. This is problematic because it creates a higher barrier to entry, adds complexity and promotes vendor lock-in. But through its collaboration with OpenTelemetry, Elastic is nudging the industry in a different direction, one where observability is more accessible to a wider range of users.

*Transform your organization’s observability strategy with open standards and simplified data collection. Read “ Realizing the Business Value of OpenTelemetry-Native Observability” to learn how.*
[
YOUTUBE.COM/THENEWSTACK
Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.
](https://youtube.com/thenewstack?sub_confirmation=1)