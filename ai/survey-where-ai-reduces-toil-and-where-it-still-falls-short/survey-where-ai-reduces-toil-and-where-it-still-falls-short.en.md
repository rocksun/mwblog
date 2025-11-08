DevOps teams spend nearly a third of their time on manual work, according to a [DevOps report](https://duplocloud.com/ebooks/state-of-devops-2026) from DuploCloud. If you have 50 engineers making an average salary of $200,000, that translates into $3 million wasted each year, assuming that all of the manual work can be automated.

A new survey of 135 engineering and DevOps leaders across North America and Europe reveals where AI is helping teams reclaim time and where it still struggles. The respondents come from startups and mid-market Software as a Service companies. This includes technical founders, platform engineers and compliance leads.

The report found a 67% increase in AI investment last year, which can address priorities like [reducing manual toil](https://thenewstack.io/let-ai-hustle-so-employees-can-lead/). But the results are mixed.

AI does improve some targeted workflows. At the same time, it often adds noise and integration overhead.

Here’s a look at the survey findings combined with industry research. With this data, you can clarify where AI delivers measurable value and where the technology still falls short.

## **Key Takeaways**

* AI can reduce manual DevOps work, which accounts for 30% of DevOps teams’ time, by automating targeted workflows. These include incident response, drift detection and compliance evidence collection.
* Strong [automation maturity](https://thenewstack.io/the-engineers-guide-to-automation-maturity/) is a must-have prerequisite. AI can amplify your existing processes, good or bad.
* It’s important to put guardrails and measurements in place to avoid alert fatigue, false positives and costly integration sprawl.

## Too Much DevOps Is Still Too Manual

The point of DevOps is to [accelerate software delivery](https://thenewstack.io/2025-brings-pressure-for-devops-teams-to-showcase-new-values/). And yet it still manages to slow teams down. Thirty percent of engineers’ time still goes toward manual, repetitive infrastructure tasks, audits and tool maintenance.

We’ve found that the biggest pain points include:

* **Security and compliance:** This has been identified by over 60% of respondents as one of their top challenges.
* **Tool sprawl:** Many teams are using up to 20 tools. Even worse, they’ve got limited visibility across them.
* **Manual Infrastructure as Code (IaC) upkeep:** It’s just too much. In fact, it adds overhead instead of removing it.

[![From compliance to burnout: Top DevOps pain points](https://cdn.thenewstack.io/media/2025/11/9b4aae3b-image3-1024x621.png)](https://cdn.thenewstack.io/media/2025/11/9b4aae3b-image3-1024x621.png)

One platform lead noted, “Everything feels duct-taped together. One script breaks, and it’s all hands on deck.”

The result is slower releases, mounting audit fatigue and burnout. Almost half of the respondents report that their exhaustion is directly tied to DevOps workloads. This echoes [Google’s 2024 “DORA Report”](https://dora.dev/research/2024/dora-report/) that links unstable priorities to lower productivity and higher stress.

## **AI Has Become a Core Priority**

Of course, teams aren’t waiting for ideal conditions to get started with automating. Sixty-seven percent of those surveyed said they’ve increased AI investment in the past year.

Here are their stated top goals:

1. Boost developer productivity
2. Adopt automation and AI
3. Cut infrastructure and operational costs

[![Top DevOps priorities for the next 12 months](https://cdn.thenewstack.io/media/2025/11/535e3491-image1-1024x591.png)](https://cdn.thenewstack.io/media/2025/11/535e3491-image1-1024x591.png)

As one senior engineer put it, “Half my job is copy-pasting scripts and hoping nothing breaks.” For many leaders, AI isn’t an experiment anymore. It’s a matter of survival.

Speed has become the north star. Fifty-four percent of teams ranked deployment frequency and lead time to change as top priorities.

This signals a clear shift toward faster, more reliable delivery.

## **From Scripts to Agents**

2025 marked the rise of AI agents. These are systems that observe, decide and act in real time.

These agents can execute infrastructure tasks safely through built-in controls, like:

* Role-based access
* Approvals
* Audit logs

Nearly 80% of leaders said they’re open to using AI agents. But they need the tools to integrate well and maintain transparency.

[![Openness to using AI agents for DevOps tasks.](https://cdn.thenewstack.io/media/2025/11/b0287620-image4-1024x457.png)](https://cdn.thenewstack.io/media/2025/11/b0287620-image4-1024x457.png)

Of course, context will continue to be the difference between helpful and harmful AI.

Without access to an organization’s real, live infrastructure data, AI systems lack the much-needed context and simply can’t act effectively. In fact, the survey notes that “without infrastructure context, responses can be vague and inactionable.” Teams that connect AI to live systems, from IaC and CI/CD to observability, see better accuracy and faster resolution.

## **AI Can Deliver**

### **Incident Response Leads To Faster MTTR**

AI correlation across logs and metrics can reduce mean time to resolution (MTTR) by 20% to 40% in well-instrumented environments. It identifies related incidents and recommends proven runbooks, saving engineers from manual searches.

Teams with inconsistent telemetry typically see smaller gains, usually maxing out at 25% reduction of MTTR.

Clean, labeled data remains the key constraint.

### **Compliance Automation Can Happen in Days, Not Weeks**

Sixty-two percent of respondents said the complexity of [compliance and security is one of their top operational burdens](https://thenewstack.io/want-to-mitigate-risk-invest-in-automation/). Automated evidence collection can map infrastructure to frameworks. These include SOC 2. Plus, they can generate audit-ready reports. This often cuts preparation from weeks to days.

Auditors still require human review for access controls and data-handling practices. So automation simplifies proof gathering but does not replace attestation.

### **You Can Get Immediate ROI From Drift Detection**

Drift detection remains one of the most reliable AI use cases. Teams that adopted automated configuration-comparison tools reported finding drift within minutes. It’s much better than doing daily manual checks.

Why it works:

* Binary success criteria (configuration matches or not)
* Minimal business context required
* Direct link to uptime and reliability

This use case consistently delivers measurable returns and rapid adoption.

## **AI Also Still Falls Short**

### **False Positives and Alert Fatigue Are Problems … Big Ones**

Anomaly-detection systems often produce 15% to 25% false positives during early deployment. Each one requires manual triage and slowly undermines confidence.

How to limit false positives:

1. Run new models in shadow mode for several weeks before production.
2. Require human approval for any automated remediation.
3. Set suppression budgets to cap alert volume.
4. Retune models quarterly using labeled data.

Without these guardrails, teams revert to ignoring alerts altogether.

### **Cost Optimization … Without the Context**

More than half of teams target cost reduction through AI, yet recommendations frequently miss the business context. Algorithms may suggest deleting “idle” disaster-recovery resources or downsizing burst-capacity services.

AI can highlight trends but cannot fully understand risk, redundancy or seasonality. Pair every cost recommendation with human validation to [avoid unplanned outages or compliance](https://thenewstack.io/3-steps-cloud-governance-steps-to-avoid-the-next-hack/) gaps.

### Fragmented Implementation

The survey found that most organizations are still script-driven. That, or they’re partially automated. AI tends to magnify your existing inefficiencies in these environments.

If you can get your team to a higher level of DevOps maturity with proactive monitoring and Policy as Code foundations, you’ll see the strongest ROI.

## Budgets Show the Shift

The evidence is in, and engineering leaders are voting with their budgets.

[![DevOps Budget and Investment Trends](https://cdn.thenewstack.io/media/2025/11/c5a47a47-image2-1024x531.png)](https://cdn.thenewstack.io/media/2025/11/c5a47a47-image2-1024x531.png)

Meanwhile, DevOps engineers are moving from manual execution to automation architecture and AI-assisted operations.

One CTO summarized it thus: “We’re not replacing people. We’re upgrading their impact.”

## Teams That Let AI Execute See the Biggest Impact

The survey highlights four consistent habits among top-performing teams:

1. **Automate first.** These teams strengthen their pipelines before layering in AI.
2. **Keep humans for oversight.** Every AI action includes audit trails and approvals by humans with expertise.
3. **Measure impact.** Successful teams track MTTR, deployment frequency and manual toil weekly.
4. **Scale gradually.** They expand AI to new workflows only after they’ve effectively proven real ROI.

Teams that integrate AI directly into CI/CD, policy engines and observability systems report the highest efficiency gains. They treat AI as an execution layer, not just a recommendation engine.

## **Where To Get Started**

1. **Measure your reality.** Log every manual action for one week and estimate the cost of each category.
2. **Choose one workflow.** Start with the area creating the most friction: compliance, drift or incident response.
3. **Run a short pilot.** Define success criteria such as MTTR reduction or hours saved.
4. **Compare results.** Share before-and-after data across teams.
5. **Scale carefully.** Expand to additional workflows only after success is proven.

## **Wrapping Up**

AI is changing DevOps incrementally, not radically. Reducing manual work from 30% to 20% is a realistic and valuable goal, roughly equivalent to adding one engineer for every 10 on staff without increasing headcount.

As one leader noted, “If you’re not using AI for DevOps yet, you’re already falling behind.”

Teams that achieve success share four habits:

* They reach a higher level of DevOps maturity in automation before adding AI.
* They treat AI as an assistive layer, not an autonomous one.
* They measure and iterate continuously.
* They maintain human oversight with clear audit trails.

AI’s greatest value in DevOps lies in amplification, helping people focus on design, reliability and judgment rather than repetitive tasks.

The insights we’ve included here come from our “State of AI in DevOps 2026 Report,” published by DuploCloud.

Read the full report: [“State of AI in DevOps 2026](https://duplocloud.com/ebooks/state-of-devops-2026).” It reveals a field shifting from scripts to agents and from manual firefighting to automation-first operations.

In short, teams need to combine automation maturity, contextual AI and strong governance. That way, you’ll build faster, operate more safely and scale with confidence.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://cdn.thenewstack.io/media/2025/11/311ffaca-cropped-be78f843-fahmid-kabir.jpeg)

Fahmid Kabir leads product and go to market at DuploCloud, an AI-powered DevOps platform. He has worked with deep AI technologies, cloud infrastructure and compliance for the past 18 years.

Read more from Fahmid Kabir](https://thenewstack.io/author/fahmid-kabir/)