Four years is a long time in technology. But in AI, it’s more like an eternity.

When [Unleash](https://www.getunleash.io/) last raised funding [in March 2022](https://venturebeat.com/cloud/open-source-feature-management-platform-unleash-nabs-14m), ChatGPT had yet to enter mainstream vernacular, and “AI-assisted coding” was a niche pursuit far from the vaunted, vibe-coding vogue that grips developer culture today. Yet some fundamentals have not changed. Software still has to run reliably in production. Features still need to be tested, measured, and, when necessary, rolled back.

That enduring tension between speed and stability sits at the heart of Unleash’s latest push. On Wednesday, brothers and co-founders [Egil](http://www.linkedin.com/in/egilconr/) and [Ivar Østhus](https://www.linkedin.com/in/ivarconr/) announced a fresh $35 million in funding, alongside a major new product update aimed squarely at the realities of AI-accelerated development.

## Distinguishing features

Feature management sits between writing code and exposing it to users. Rather than deploying a change to everyone at once, teams can wrap new functionality in feature flags — switches that determine who sees what and when. That might mean releasing a new checkout flow to a small segment of users, testing two variations of a recommendation engine, or quietly enabling a backend change before exposing it publicly. If something misfires, the feature can be disabled without redeploying the entire application.

Unleash provides that control layer, allowing engineering teams to define rollout rules based on user segments, geography, device type, or other attributes, and to fine-tune exposure in real time.

![Unleash: Feature Management](https://cdn.thenewstack.io/media/2026/03/bf3e3c45-feature-management.png)

Unleash: Feature management interface

The concept predates the current AI surge for sure, but as code generation accelerates, the volume of changes moving toward production has increased. And that, in turn, raises the stakes of how releases are handled.

Egil Østhus, the company’s CEO, says the shift has been visible inside the company as well. AI tools have increased internal development speed, but they have also forced stricter discipline around what actually ships.

> “When generating code becomes cheaper, discipline about what you write becomes more important. We are more intentional about what we ship and what we keep. Velocity without control just creates noise and long-term complexity which is the opposite of what you want when scaling.”

“Our engineers are a lot more efficient, but at the same time, AI raises the expectations bar,” Østhus tells *The New Stack.*“When generating code becomes cheaper, discipline about what you write becomes more important. We are more intentional about what we ship and what we keep. Velocity without control just creates noise and long-term complexity, which is the opposite of what you want when scaling.”

Moreover, Østhus says that what Unleash is experiencing internally mirrors what it is seeing across its customer base, which includes the likes of Lloyds Banking Group and Lenovo.

“AI dramatically increases code velocity — teams can ship more experiments, more features, more changes,” Østhus said. “But that does not guarantee they are shipping the right things, or that those changes are safe.”

Indeed, research suggests that rapid AI adoption is not a panacea for delivery performance. The [2025 *State of AI-Assisted Software Development* report](https://cloud.google.com/blog/products/ai-machine-learning/announcing-the-2025-dora-report) from DORA — the long-running DevOps Research and Assessment program at Google — found that while AI is now widely integrated into engineering workflows and can boost throughput, it also amplifies strengths and weaknesses in software delivery systems. As a result, teams without mature release practices and controls often see instability remain elevated even as velocity increases.

“In a world where applications change dozens or hundreds of times per day, companies need progressive rollouts, real-time measurement to see what is working, and instant kill switches in case something goes wrong,” Østhus said.

## When CI/CD isn’t enough

There are plenty of development disciplines and toolchains that engineers can lean on to ship software safely. Continuous integration and continuous deployment (CI/CD) pipelines automate the route from commit to production, while observability platforms collect metrics once code is live. But none of these are explicitly designed to control the *behavior* of individual features once they’ve been exposed to users — a gap that becomes more apparent with AI in the picture.

“When AI-assisted development increases the frequency of changes, traditional rollback becomes less practical,” Østhus says. “Rolling back an entire deployment because one feature is misbehaving is too slow and too blunt. In highly distributed systems, redeployments can even introduce new risk.”

> “Rolling back an entire deployment because one feature is misbehaving is too slow and too blunt. In highly distributed systems, redeployments can even introduce new risk.”

This is a layer Unleash, and other industry players refer to as [FeatureOps](https://www.jbillmann.com/introducing-feature-ops) — the practice of managing feature lifecycles independently of deployments.

“It allows teams to control exposure at the feature level — they can release a feature to 1 percent of users, monitor real-time signals, and automatically pause or disable that feature without touching the rest of the system,” Østhus says. “It is surgical control instead of all-or-nothing deployment logic.”

![AI model variant rollout controls](https://cdn.thenewstack.io/media/2026/03/d8a13412-ai-effortless-rollback.gif)

AI model variant rollout controls

And that is a philosophy that underpins Unleash’s latest product update. Version 7.5 introduces “Impact Metrics,” a capability designed to move selected production signals directly into the release logic itself.

Rather than relying solely on dashboards and manual intervention, teams can define which metrics should govern a feature’s exposure — from error rates and latency thresholds to business indicators such as adoption or conversion. If those predefined thresholds are breached, a rollout can be automatically paused or terminated without redeploying the broader system.

The intent, Østhus argues, is to ensure that release decisions reflect more than just technical telemetry. Engineering signals, product performance, and user impact can all be factored into how a feature is evaluated as it rolls out.

“Most enterprises already have monitoring tools, product analytics, and data warehouses,” Østhus says. “The challenge is not the lack of data. It is connecting the right signals to the right feature at the right time. Unlike existing monitoring-driven release guardrails in the market, Impact Metrics allows the organization to bring a full 360 point of view into the conversation.”

![Impact Metrics](https://cdn.thenewstack.io/media/2026/03/7fb33b72-impactmetrics.png)

Impact Metrics

## Open source, auditability, and the enterprise question

At the heart of Unleash’s appeal to large enterprises is its open source credentials.

The project began in 2014, when Ivar Østhus, now the company’s CTO, was a developer at Norway’s largest online marketplace, Finn.no. Frustrated by the friction of shipping unfinished features — and the merge conflicts and delayed feedback that came with feature branches — he built an internal flagging system to decouple code deployments from feature releases.

The tool was open-sourced the following year, and eventually evolved into today’s commercial Unleash platform, with his brother Egil Østhus joining as CEO in 2019.

For regulated industries, Egil Østhus argues, offering transparency and control is critical — particularly as AI-generated code increasingly enters production systems.

“Being open-source and self-hostable is a significant advantage,” he said. “Customers can inspect the code, fork it if needed, and run it entirely inside their own infrastructure.”

Auditability explains why Unleash focuses heavily on enterprise customers, but Østhus rejects the idea that runtime control is solely an enterprise concern.

“Large enterprises have multiple teams, legacy systems, regulatory requirements, and millions of users — the blast radius of a mistake is exponentially larger,” he said. “But even a two-person startup can take down its entire product with one bad change.”

As AI lowers the barrier to generating and shipping code, teams of all sizes are releasing changes more frequently. The difference, Østhus argues, is one of scale and complexity. Larger organisations face greater coordination burdens and regulatory exposure, while smaller teams operate with fewer layers. The underlying challenge — controlling how software behaves once it is live — remains the same.

Unleash’s Series B round was led by One Peak, with participation from existing investors Spark Capital, Frontline Ventures, and Firstminute Capital. With a fresh $35 million in the bank, the company plans to build on the foundation it has established since its last raise in 2022, during which time it says it has surpassed 500 paying customers, passed 13,000 GitHub stars, and recorded more than 40 million total downloads of the open source project.

As AI accelerates software delivery, the mechanics of release management are becoming more consequential. Unleash’s wager is that feature-level oversight becomes routine infrastructure in modern software delivery — a “safety net,” as Østhus puts it, for teams operating at AI speed.

“When AI-generated code is in production, and something breaks, every minute of downtime costs you revenue and customers,” he said.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://thenewstack.io/wp-content/uploads/2026/02/bd93adde-cropped-9c2ecfc5-a-600x600.jpg)

Paul is an experienced technology journalist covering some of the biggest stories from Europe and beyond, most recently at TechCrunch where he covered startups, enterprise, Big Tech, infrastructure, open source, AI, regulation, and more. Based in London, these days Paul...

Read more from Paul Sawers](https://thenewstack.io/author/paul-sawers/)