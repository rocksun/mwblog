# Why AI Can’t Fix Your Production Issues
![Featued image for: Why AI Can’t Fix Your Production Issues](https://cdn.thenewstack.io/media/2024/08/82de452a-technology-7111804_1280-1024x559.jpg)
[Generative AI](https://thenewstack.io/ebooks/generative-ai/how-generative-ai-transforms-software-development/) and LLMs have significantly increased productivity across industries and domains, from marketing to engineering. As an early-stage founder, I have personally found them helpful in multiple day-to-day workflows from creating admin document templates to assisting with code syntax.
There has been [much discussion](https://thenewstack.io/5-creative-ways-developers-are-using-ai/) about how AI can replace an engineer, including an editorial [StackOverFlow](https://stackoverflow.blog/2024/06/10/generative-ai-is-not-going-to-build-your-engineering-team-for-you/) blog about why AI can’t replace engineering teams. In this blog, I make my case for why AI is a great productivity enhancer but cannot debug production issues for on-call engineers and SREs today.

### Practical Implementations of LLMs:
AI tools that [act as assistants](https://thenewstack.io/a-coder-perspective-what-its-like-to-develop-an-ai-app/) have been quite helpful across the lifecycle. Here are a couple of examples where I have used them:

**Code Generation/Instrumentation:**LLMs are a great way to get a boilerplate code for a function or task. While I often end up re-writing a significant portion of the code, I do like the experience of not having to do everything from scratch but starting at a certain point (say 30%)
- Github CoPilot
- Terraform generator —
[https://github.com/gofireflyio/aiac](https://github.com/gofireflyio/aiac)Here’s a
[recent blog](https://terrateam.io/blog/using-llms-to-generate-terraform-code)about users’ experiences using LLMs for Terraform generation/update.
**Natural Language to commands**Instead of using chatGPT to find new commands, I find Warp’s natural language to command generator quite relevant. But for use cases that I am not doing for the first time or if I know a command, I am highly reluctant to use the natural language mode. It’s helping me naturalize and accelerate the learning curve to pick up syntax/language.
### My Background
My experiences with machine learning began before I even called my work machine learning. As a young developer in 2015, I spent a summer working on an application that leveraged OpenCV to digitize and parse millions of offline documents. Since then, I have dabbled with supervised/unsupervised learning, constraint optimization problems, forecasting, and NLP in various roles.

For the past couple of years, I have been a co-founder at Doctor Droid, a company focused on solving challenges in the life of an on-call engineer.

**The aspirations of engineers for AI/ML in Production Incident monitoring:**
As a founder, I pitch to fellow developers with different prototypes to solve some part of their problem in the “Observability” lifecycle. While pitching to users, I’ve often found that the excitement for engineers takes an extra high whenever any of these use cases are mentioned:

- Prediction/Forecasting an incident before it happens
- Anomaly Detection to get alerts without having to configure them
- Automated investigation of an incident using AI
Naturally, I built prototypes and tools attempting to solve one or more of these use cases.

Before I dive deeper into the prototypes, I’m sharing a short note on how I think about debugging.

**CAGE Framework for Debugging and Production Investigation**
This framework has been inspired by my engineering experiences in my previous jobs and from interacting with developers at Doctor Droid. I realized that debugging is often down to four things:

- Context:
This refers to tribal knowledge about what your product does, how customers interact with it, how the infrastructure is mapped to the services, to the features, and so on. Your customer complaint might not objectively translate into a specific infrastructure component. Without being able to translate the problem/use case into its right context, it is non-trivial even for existing developers on the team to navigate a production issue.

- Analytical Thinking
Engineers are expected to create hypotheses and validate/disprove them using correlation and causation. Correlating timelines and anomalies (often caught by eyeballing) are skills that require a portion of analytical thinking on behalf of an engineer — be it watching a metric and evaluating whether it’s an anomaly or be it looking at an anomaly and thinking about what else could be impacted (using their tribal knowledge)

- Goal Definition:
Operations for an engineering team are highly dependent on the organization’s business commitments and requirements. Just having analytical thinking isn’t enough, either. Last year, we were building an [analytics platform](https://github.com/DrDroidLab/kenobi) — even with four services when it was deployed, we had 2000+ metrics generated across our infrastructure and application (more about this application in the next section).

If we apply our analytical thinking to evaluate all of these metrics for alerts, it makes sense for none of us on the team. Accordingly, **we defined SLOs and a trickle-down of metrics in order of the priority with which we need to care for it**. This was essential to help the on-call engineer understand when and what needs to be escalated/investigated/deprioritized.

- Entropy Estimation:
Issues in production often have a cascading lifecycle, both pre and post-issue:

- Pre-issue: The issue could have been caused by a series of “unanticipated” changes in the behavior of one component (e.g.,
[this loom incident](https://www.loom.com/blog/march-7-incident-update)), cascading downstream into more components. - Post-issue: While trying to apply a fix/patch, a minor glitch or inaccurate attempt (
[e.g., this AWS incident](https://aws.amazon.com/message/41926/)) could further escalate the issue.
An engineer is expected to be completely active even after stabilization in anticipation of a potential increase in their system’s entropy.

## Experiments and Learnings:
The below-mentioned experiments were carried out on Kenobi’s production systems, a real-time analytics platform that Doctor Droid built in 2023. Below is the architecture of the platform:

The platform (in its current shape) has four microservices, and it took five developers about six months to build it out. The platform processes 20-30M events/day, sent to it from different sources, and makes them available in less than 10 seconds for querying from the UI and alert evaluations. You can read more about the platform[ here](https://notes.drdroid.io/building-an-events-lakehouse-with-dynamic-schema).

### Experiment 1: AI Investigation Assistant
Defining the objective of this experiment:

**Input:**An alert is triggered in the system**Output:**An investigation runbook for an on-call engineer to use as a way to investigate/fix the issue**Problems the tool attacks:**Lack of runbooks/guidelines, leading to delayed investigations.
**Solution:**
**The prototype works as follows:** it receives a webhook from Slack for every alert. Then, the prototype analyses the alert’s context and tries to recommend the most relevant steps by leveraging contextual information available to the user.
Here are the data sources that were used for “context”:

- Team’s internal on-call SOPs (subject to availability)
- Added context of metrics & data sources available to debug in the specific platform.
![](https://cdn.thenewstack.io/media/2024/07/be686e75-picture1.png)
Mental models on how to debug issues in micro-services applications

**Results**:
Prima facie, the output quality from the experiment looks good. But once you test it on production or give it to someone who’s trying to investigate, here are the issues that the on-call engineer ended up facing:

**Generic recommendations:**- “Check metrics of related infrastructure on CloudWatch” is a generic recommendation that could mean many metrics unless the developer knows exactly which components are the most related.
**Faulty suggestions:**- In one of the steps, it is recommended to check logs in ELK / Kibana, but Kibana is not part of the team’s stack.
**Remediation actions with low confidence:**- Remediation actions typically require the backing of correlated data, which the approach cannot currently do. Given the number of generic checks suggested, it also becomes impractical to run ML models for anomaly detection on a wide range of metrics.
While these suggestions felt like an exciting start, we realized that an on-call engineer typically preferred the following approach to keep the time to debug an issue low:

- Follow steps “to the T” as per a document/runbook
- Raise it to an engineer/team that might be closely related to this issue
With this learning, we decided to work on reducing the emphasis on intelligence and more on enabling a framework for automation.

### Experiment 2: Open Source Framework to Automation Production Investigation (With an Optional Layer of AI)
**Objective:**
**Input:**User to configure their observability tools and their investigation runbooks**Output:**The playbook will get auto-triggered when it receives an alert, and then the team will receive the analysis as an enrichment to the alert in the original source (Pagerduty/Slack/Teams/etc.).**The tool attacks the problems:**The Need for an on-call engineer to manually debug issues, which often leads to escalations to other engineers.
**Results:**
This [framework](https://github.com/DrDroidLab/playbooks) improved developer productivity by up to ~70% with some of the participating users. Apart from the data, here’s what we’re additional learnings:

**Preference for Deterministic Outcomes:**Given that issues raised on-call are critical and risk escalation or business loss, engineers prefer deterministic outcomes instead of probabilistic outcomes.**Resistance to Manual Configuration:**Given that the framework depends on the user’s debugging steps/procedure, some teams have challenges manually configuring runbooks due to concerns that it’s time-consuming and that repeated issues are typically automated.**Only sometimes applicable:**Exploratory issues require users to go beyond the framework.
**Use of AI in Experiment 2:**
(a) Generate PlayBooks from Documents: We wrote a small agent that reads an existing doc and maps it to integrated tools. The objective of this tool is to reduce the effort to configure playbooks.

This output is similar to the previously mentioned blog on Terraform Generator — it is still not in auto-mode and requires user reviews and iteration.

(b) Generate Summary from Data

This summariser helps users read the most relevant point first instead of manually going through all the data.

*As you can see, these are assistive implementations and highly dependent on the central framework.*
## Practical Use Cases of Leveraging AI/ML in Observability
AI/ML brings in a lot of opportunities within the observability domain, but **they will be designed for particular/narrow contexts**. “Production Debugging” has a vast scope, but here are three examples with narrower scopes where AI / ML are being used today:

- Summarization and Classification of Investigations:
- Creating an AI layer that analyses the data extracted by the Automation framework and sends a summary back to the engineer can reduce their time investigating an issue.
- Multiple enterprises have implemented this internally. Microsoft has a
[paper](https://yinfangchen.github.io/assets/pdf/rcacopilot_paper.pdf)on this discussing their product RCACoPilot (while the name says CoPilot, the tool is quite deterministic in its approach to debugging/investigation and relies on LLMs only for summarisation and incident classification).(The “handlers” in the Collection Stage are user-written runbooks for every alert/incident.)

- Deployment Monitoring and Auto-rollbacks:
- Alert Grouping and Noise Reduction:
- Reducing the context to just Alerts helps implement intelligence within the platform. Here are a couple of intelligent insights that AIOps platforms can provide (today) on top of a user’s alerts data:
- Grouping and correlation of alerts based on tags, timing, and history.
- Analyzing the frequency of alerts to understand if it’s a noisy alert.
- Reducing the context to just Alerts helps implement intelligence within the platform. Here are a couple of intelligent insights that AIOps platforms can provide (today) on top of a user’s alerts data:
## Conclusion
After all of these experiments and prototyping, I have two key learnings:

- Even minuscule adoption requires significantly less noise than the status quo of custom-configured systems.
- Continuing from the first learning, reaching these low-noise thresholds out-of-the-box has not been common. Optimizing them typically required significant custom work for every team/use case.
Hence, you will see many tools and platforms leveraging AI/ML in their observability stack, but it will likely be restricted to specific scopes, assisting engineers in those scopes instead of being an overarching “replacement for engineers.”

[
YOUTUBE.COM/THENEWSTACK
Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.
](https://youtube.com/thenewstack?sub_confirmation=1)