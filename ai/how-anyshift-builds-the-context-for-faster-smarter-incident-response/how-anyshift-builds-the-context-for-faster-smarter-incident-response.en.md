Most modern companies have a sprawling footprint, comprising international teams and huge, multicloud architectures held together by Kubernetes, CI/CD pipelines, Infrastructure as Code (IaC) and many other interconnected tools.

These jigsaw-puzzled environments have made it easier for teams to move fast and deploy globally — but it’s making incident response an enormous headache for [site reliability engineers](https://thenewstack.io/practical-guidance-for-first-time-site-reliability-engineers/) (SREs).

[Roxane Fischer](https://www.linkedin.com/in/roxane-fischer-92a52414b/), CEO and co-founder of [Anyshift](https://www.anyshift.io/sre-experts), was tuned into this reality when she and [Stephane Jourdan](https://www.linkedin.com/in/stephanejourdan/), fellow co-founder and CTO, decided to launch Anyshift: “From the first day of the company, we always understood that one of the big issues in the domain right now is that you have different silos in your infrastructure … that don’t respond to each other when you have an issue, particularly in production for your engineers.”

She’s not alone in that observation. And all those silos, it seems, might be impacting incident response time. In a [2023 survey](https://devops.com/it-service-incidents-are-becoming-more-frequent-survey-says/?utm_source=chatgpt.com) of 1,000 IT operations, [DevOps](https://thenewstack.io/multipass-fast-scriptable-ubuntu-vms-for-modern-devops/), SRE and platform engineering professionals, 62% said they’d seen an increase in the time it takes to resolve incidents over the last year.

What’s slowing them down? Fischer says it’s the chaos and lack of context that comes from managing fragmented, sprawling infrastructure.

## Too Many Tools, Not Enough Context

Many organizations juggle a mix of [AWS](https://aws.amazon.com/?utm_content=inline+mention), GCP and Azure, along with Kubernetes clusters, CI/CD pipelines, IaC tooling and more. While architecting multicloud or hybrid infrastructure has obvious advantages in the way of flexibility, speed and redundancy, it also means there’s a lot to weed through when it comes time for incident response and root cause analysis.

As Fischer puts it: “When you have a latency issue for a customer, it’s super hard to know [if] it comes from a mixed configuration in your Kubernetes cluster or … a change that created a snowball effect.”

Even just one alert could have been triggered by a dozen different factors, creating dizzying rabbit holes for SREs to pursue — an especially chaotic task when working under duress in an aptly named “war room.”

Fischer calls this root cause analysis goose chase one of the biggest pain points in the industry. And the current tools in use, she claims, are inadequate support: “Traditional monitoring tools will tell you what has changed, but not why. They will not give you the context of the issue.”

Anyshift aims to provide that context.

## Meet Annie: SREs’ Shortcut Through the Root Cause Rabbit Hole

The context comes from a continuously updated infrastructure graph and a smart assistant named Annie.

Anyshift ingests and structures data from multiple sources to create a live map of a company’s infrastructure and production, establishing a single source of truth that maps the relationships between services, cloud resources, configurations and code.

When an incident hits, all SRE teams have to do is tag Annie, who then gets to work investigating the issue. She uses the alert as an entry point, follows the dependency path from frontend to backend and queries live logs and metrics from integrated tools like Datadog or Grafana.

“She will behave similarly to … an SRE,” proclaims Fischer. “She will go through the different paths of investigation, query what she needs, and at the end, create a [root cause analysis] report in the incident channel.”

Notably, Annie doesn’t just present her findings; she shows her work, too.

“[She] then explain[s], in a very structured way, how she did that, where she went, and what path she explored,” adds Fischer. This is a noteworthy step beyond the capabilities of many [AIOps](https://thenewstack.io/sre-report-retrospectives-have-aiops-predictions-held-up/) or AI SRE tools, which typically fetch large volumes of data to surface potential root causes, sans explanation.

## Experts Can Come and Go — But an Assistant Never Logs Off

It’s not just the shortcomings of traditional monitoring tools that impede incident response. The institutional nature of many SRE teams creates room for risks, too.

Some incidents are a breeze to fix if you’re working with veteran SREs who have been there, done that — and know how to trace the problem without eating up a lot of time.

But if your team lacks this kind of hands-on experience, then even routine investigations can suddenly become a lot more laborious. “It’s kind of like finding a needle in a haystack,” says Fischer. “How do I go through these different paths of exploration and try to understand why this issue has been caused?”

Experienced SREs are often the first to get pinged when something goes sideways. But while their years of experience may seem like an asset, it’s actually a liability that could spell disaster very quickly.

“If these people leave, it’s going to be a catastrophe,” Fischer cautions. “If they’re not here, the junior person will be very often lost because they don’t get the information.”

## More Context = Faster Fixes + Less Toil

The impact of drawn-out incident response goes beyond wasted time, though that’s a significant downside. According to one [Google SRE Book](https://sre.google/sre-book/eliminating-toil/#:~:text=Quarterly%20surveys%20of%20Google's%20SREs,to%20find%20satisfying%20engineering%20projects.), “Quarterly surveys of Google’s SREs show that the average time spent toiling is about 33%,” with some outliers claiming 80% toil time.

Cost is, of course, another troubling side effect. Per [a survey](https://www.pagerduty.com/newsroom/study-cost-of-incidents/?utm_source=chatgpt.com) from [PagerDuty](https://www.pagerduty.com/?utm_content=inline+mention), the average incident takes 175 minutes to resolve and costs almost $794,000.

Besides lost minutes and dollars, lengthy incident response hurts companies by pulling SREs away from higher-value work. This is of particular concern for Fischer, who says one of the primary focuses of Anyshift is to help get that time back:

“How do we actually help those SREs, [so they’re] not fixing incidents that [were] caused by past modification — but free some time for those on-call engineers to focus on tasks … [that] actually improve and creat[e] something for the company?”

## Building the Map for a Context-Driven Future

Right now, Anyshift is focused on on-call scenarios — what Fischer calls the first “fire” to put out. But down the line, she envisions the startup’s infrastructure graph as the foundation for the next iteration of AI SREs that don’t just respond to incidents but help teams continuously improve and optimize infrastructure for cost, latency and reliability.

Getting there will mean adding more context by layering application data on the infrastructure graph to map the entire production system. Only then does Fischer believe Anyshift can achieve its ultimate goal “to close the gap between the developer and the DevOps team, between the infrastructure and the application world.”

This end-to-end visibility shouldn’t just improve incident response; it should also eliminate the finger-pointing that often arises during cross-team incident response.

For Fischer, it all comes back to one question: “How do you actually make the entire system better?”

They’re not there yet, but if the future of AI SRE is context-driven, then Anyshift is certainly building the “map” to get there.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://thenewstack.io/wp-content/uploads/2025/09/53f49f49-cropped-35fc143f-meredith-shubel-2-600x600.jpg)

Meredith Shubel is a technical writer covering cloud infrastructure and enterprise software. She has contributed to The New Stack since 2022, profiling startups and exploring how organizations adopt emerging technologies. Beyond The New Stack, she ghostwrites white papers, executive bylines,...

Read more from Meredith Shubel](https://thenewstack.io/author/mshubel/)