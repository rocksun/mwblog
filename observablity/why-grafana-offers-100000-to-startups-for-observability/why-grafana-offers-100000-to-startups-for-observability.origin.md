# Why Grafana Offers $100,000 to Startups for Observability
![Featued image for: Why Grafana Offers $100,000 to Startups for Observability](https://cdn.thenewstack.io/media/2024/09/af5535be-alexander-mils-hyob4ml_yso-unsplash-1-1024x576.jpg)
NEW YORK — During [ObservabilityCON](https://grafana.com/events/observabilitycon/) here this week, [Grafana](https://thenewstack.io/can-grafana-adaptive-metrics-help-slash-observability-costs/) announced it is offering a $100,000 stipend to selected startups. This financial support aims to alleviate the cost barrier and allow startups to focus on growing their business without sacrificing the crucial [observability](https://thenewstack.io/observability/) needed to maintain operations efficiently.

Cost is a quintessential concern for organizations, particularly when it comes to observability, according to a recent Grafana study. This concern is especially critical for startups, which often have limited runway and must ensure every investment either saves costs or generates revenue and profit.

While there is general consensus that observability is necessary for a variety of reasons — ranging from managing infrastructure to enhancing security and streamlining processes like testing and [CI/CD](https://thenewstack.io/ci-cd/) — the cost of implementing observability tools can be a significant concern. Even those backed by venture capital can easily balk at spending on tools that seem to add extra financial burden.


[@grafana]’s[@nopzor]: $100,000 on offer for startups in Grafana costs.. «we don’t require startups to be VC backed or US based.. »[#ObservabilityCon]2024 keynote.[@thenewstack][pic.twitter.com/gsbBStDJFj]— BC Gain (@bcamerongain)

[September 24, 2024]
“Obviously, we have an open source project, so many startups can use our open source software for free, and that’s by design. However, we noticed a gap for startups that are not necessarily VC funded and are going through periods of tremendous growth and scaling — a good problem to have, obviously, but it carries financial risk for these companies,” [Grafana Labs](https://grafana.com/) co-founder and CEO [Raj Dutt](https://www.linkedin.com/in/radutt) said during the keynote. “Particularly for startups with limited funds, they are often caught between reinvesting in their growth and simply keeping the lights on. We believe it doesn’t have to be that way.”

While [Grafana Cloud](https://thenewstack.io/grafana-extends-free-access-for-cloud-managed-observability/) already serves a substantial tier of free use to any user, Grafana’s stipend offer arguably falls under an extended free-use plan as an investment in what Grafana hopes will lead to a successful startup’s scaling needs for observability, underpinned by Grafana’s reach across observability with a predominance of open source. Grafana also hopes to demonstrate how [Prometheus](https://thenewstack.io/creating-a-path-for-prometheus-success/) and a number of other open source alternatives, including Loki for logs, Tempo for tracing, and Mimir for metrics, can be used to help organizations manage their telemetric data and decisions in a way that can reduce costs as cloud prices continue their upward trajectory.

These cost concerns were a major theme during ObservabilityCON. Speakers emphasized how implementing effective observability practices not only improves operational efficiency but can also be used to reduce the costs associated with maintaining observability itself. A study Grafana Labs released this year also noted that the top concern regarding observability was cost, with 56% of respondents ranking it as their biggest issue. Understandably, the complexity of managing systems followed closely behind at 50%, while cardinality came in third place.

One could argue that the challenge of managing cardinality directly contributes to higher costs, as it falls under the broader umbrella of financial concerns. This would position cost as an even more dominant factor in the hierarchy of struggles that organizations face when implementing observability.

Similarly, the signal-to-noise ratio, which is a challenge for those responsible for debugging and filtering through numerous alerts, was cited as a top concern by 34% of respondents. Additionally, at 30%, this issue was tied to the cost in resources, further highlighting how many observability challenges ultimately relate to financial strain.

## Get Adaptive
Central to Grafana’s outreach to help organizations save on their observability costs is “adaptive” metrics, logs, and traces. According to Grafana, customers are seeing a 35% reduction in metrics costs with [Adaptive Metrics](https://thenewstack.io/why-did-grafana-labs-need-to-add-adaptive-metrics/), which lowers bills by identifying and eliminating unused metrics through aggregation. TeleTracking, an integrated healthcare operations platform provider, used Adaptive Metrics to cut its billable metrics series by 50%, reducing costs by up to 33%, Grafana says.

Announced during Grafana, Grafana Labs is extending this “Adaptive” concept to logs and traces, leveraging AI/ML techniques to analyze observability data at a scale that wouldn’t be feasible with manual processes, the company says. With the general availability of Adaptive Logs released this week, Adaptive Logs helps organizations lower their observability costs by reducing the volume of unnecessary logs. Adaptive Logs identifies commonly ingested log patterns and creates a set of customized sampling recommendations based on how frequently those patterns are queried. This gives customers the ability to prune away low-value logs so they only retain the important ones.

For Adaptive Traces, Grafana Labs purchased startup TailCtrl, an early-stage company founded by [Sean Porter](https://github.com/portertech), who co-founded Sensu.

During his talk on adaptive metrics, [Oren Lion](https://www.linkedin.com/in/oren-lion/), director of software engineering at healthcare services platform provider TeleTracking, noted how Grafana Adaptive Metrics serves as a “log level but for metrics.” Adaptive Metrics effectively reduce the verbosity of metrics, Lion said. Since each label in a metric may result in generating many time series, Adaptive Metrics effectively dials back the number of labels in a metric, and fewer time series are produced.

The recommendations published by Adaptive Metrics enable organizations to automate the process of assessing what metrics are needed and where. The organization quickly slashed its metrics costs by using an early iteration of Grafana Cloud’s Adaptive Metrics. Within a few weeks, after addressing all the defects and getting Adaptive Metrics fully operational, they realized a 50% reduction in costs.

With what Lion describes as “custom metrics and dependency metrics,” “we’ve built incredible metrics generators,” Lion said. “Teams will think about design and how to monitor services and dependencies, but fall short of estimating and tracking the cost to monitor a service,” Lion said. “Really, the cost of metrics is not in the plan until you get the bill, and then you scramble.”


[@grafana]’s Jen Villa: Developers can get onboard to lower observability costs..Grafana Explore Metrics and Logs, with AI/ML are now GA[#ObservabilityCon]2024 keynote.[@thenewstack][pic.twitter.com/yXVB3ostSf]— BC Gain (@bcamerongain)

[September 25, 2024]
Meanwhile, during her talk, [Jennifer Villa,](https://www.linkedin.com/in/jevilla/) Grafana’s director of product management for databases, said “The saving money part could also be pretty fun and exciting.” However, “What I’m going to talk to you about is a little more depth on what we went over yesterday. The keynote is about applying AI/ML via our adaptive telemetry strategy to help everyone adopt observability at greater and greater scale because we’re making it more affordable than ever,” Villa said. “Not only do we want to increase the cost-effectiveness of observability, but we also want to empower all engineers at your organization to participate in the mission of improving your costs, right? We don’t just want that responsibility in the hands of a select few.”

[
YOUTUBE.COM/THENEWSTACK
Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.
](https://youtube.com/thenewstack?sub_confirmation=1)