As the cliché goes: Garbage in, garbage out*.* That applies [directly to AI-powered systems](https://thenewstack.io/using-llms-right-leveraging-ai-for-augmented-data-quality/).

If the data going into the system is inaccurate or incomplete, then inferences from that data will be flawed.

It’s the same thing with data diversity. If an AI system only sees a limited subset of the environment, it ends up biased. It won’t make strong inferences about the rest of the system because the examples it’s learning from don’t represent the full picture.

This is especially true in incident management. When you can harvest incident data effectively, you can begin drawing correlations between different attributes while gaining a strong understanding of incident nuance, and this is where AI really becomes valuable.

## **A 360-Degree View of the Incident Landscape**

There are many factors that inform the nature of an incident and how it should be resolved.

For example, the source integration gives you clues about the underlying system that’s affected. The environment tells you how critical it is, whether it’s a test system or a production environment. Even the timing of incidents matters. If an incident occurs right after another one, teams can use it as a signal to determine if it’s part of a pattern or an isolated issue.

Then there’s the resolution side. The [automation used to diagnose or remediate the incident](https://thenewstack.io/5-ways-to-supercharge-incident-remediation-with-automation/) is incredibly instructive. You also have sources such as status updates and incident notes, which often explain why an issue happened or how it was resolved.

When you have both deep and broad data, you can paint a full 360-degree picture of the incident landscape or even the broader tech landscape. There are basically two big buckets of attributes to look at: how incidents occur and how they get resolved.

The more visibility an AI system has across these attributes, the more powerful it becomes. It can flexibly classify [incidents alongside similar ones and identify a much stronger resolution strategy](https://thenewstack.io/bridging-the-gap-between-monitoring-and-incident-resolution/). That kind of flexibility makes the system robust.

## **What Strong Incident Data Looks Like**

Generally, you need two types of data:

* **Incident origination data**: Data that provides insight into which system was affected, the environment it was in, which rule triggered the alert, its timestamp and the affected service.
* **Incident resolution data**: Data that shows which [automation was run](https://thenewstack.io/crawl-walk-run-the-key-to-successful-automation/), user annotations like notes or status updates, Slack conversations and Zoom transcripts.

Together, incident origination and resolution data paint a rich, 360-degree profile of an incident. The full picture helps ensure incidents are categorized correctly. Once categorized, historical resolution strategies can be surfaced, or even executed automatically using agentic AI, to accelerate response.

When AI can confidently cluster a team’s incidents, it often cuts noise and accelerates resolution. Imagine a team’s incidents can be grouped into Type A which can be ignored, Type B that just needs automation and Type C that requires human intervention. Type C becomes the primary focus. [Managing incidents in this manner helps teams scale](https://thenewstack.io/what-can-incident-teams-learn-from-crisis-management/) as their tech stacks grow, without incident volume growing at the same rate.

## **Speed and Confidence Through Automation**

Let’s say a team has created scripts to run diagnostics or remediation actions. When an incident occurs, responders can click a button, run the automation and see the results. But these automations are often written by developers, and new responders might not know which to use, or how.

That’s where AI can be really helpful. The system looks at the available [automations](https://thenewstack.io/fighting-incidents-with-end-to-end-event-driven-automation/) and tags the most useful ones for that specific incident, and within that recommended set, it prioritizes the action the responder should take first. Responders who aren’t familiar with the available automation can then choose the right action more quickly and with more confidence.

## **From Data-Driven to Data-Producing**

Businesses have always used data to inform decisions, but now, and in the near future, there will be a shift to where data won’t just inform decisions. It will produce them.

With the rise of agentic AI, systems are starting to have real autonomy. These agents are already out in the world making decisions, and the decisions they make are completely informed by the data they’re given. Data is moving from being a backseat consultant to sitting in the front seat, driving.

That’s a big shift, and it means that companies will need to make sure the data they’re using to support their customers, as well as power these decision-making systems, is rock solid and high quality.

## **Building the Right Foundation: Data Governance**

The best way to ensure that the right data is producing the right decisions is to build a strong muscle around data governance. There are a few key pillars:

* **Data integrity**: Make sure the data is clean, accurate and standardized. Use consistent formats and naming conventions. Build monitors that can report on data quality scores to have a continuous check-up on data health.
* **Data security**: Build trust slowly, but lose it immediately. Data should be tightly controlled and encrypted wherever possible. Create audit reports that log who accessed the data and when, and set up alerts.
* **Compliance**: Organizations need to comply with regulations in the markets you operate in, but also think ahead. Even if not currently active in the EU, it’s worth preparing for GDPR or the EU AI Act so the organization is ready to expand.
* **Storage**: Data storage costs can balloon fast. In a world where organizations are collecting more and more data, it’s worth being efficient to avoid unnecessary overhead.

Bottom line: The systems making decisions tomorrow are being trained on the data you manage today.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://thenewstack.io/wp-content/uploads/2025/07/6671ce47-cropped-5d756f9e-scott-bastek-600x600.jpeg)

Scott Bastek is senior applied scientist at PagerDuty. He has extensive experience in AI and data analytics. He is currently focused on building customer-facing AI functionality at PagerDuty. Based in Lisbon, Scott splits his time running, sitting at kiosks and...

Read more from Scott Bastek](https://thenewstack.io/author/scott-bastek/)