Tabletop exercises answer one question: when something breaks, will the people responsible for fixing it do the right thing, in the right order, fast enough? For years, the answer depended almost entirely on humans: their training, runbooks, and their judgment under pressure. We assumed the tooling around us was static. We have always tested the people because the people were the variable.

That assumption doesn’t hold anymore.

At [Webflow](https://webflow.com/), we’ve spent a year building AI into the parts of incident response that used to be purely human: triaging alerts, pulling the right playbook, proposing responses, and even drafting PIA (Post Incident Analysis) and its follow-up items.

We’ve written before about how this multiplied our security team rather than replacing it, but there’s a consequence of that shift we don’t see many teams grappling with yet. If AI is now doing real work during an incident, AI is now part of what a tabletop has to test. Not just whether your responders know the runbooks, but whether the system that’s supposed to hand them the runbook actually does, and does so correctly, under the same pressure that used to only apply to humans.

This isn’t just a security team problem. Any team that has quietly let an AI system become part of its response (support routing customer escalations, SRE triaging outages, IT auto-resolving access requests) has the same untested dependency sitting in its process. If your tabletop exercise formats haven’t changed since you injected AI into your systems, you’re testing a team that no longer exists, and that leaves you blind to gaps.

## Tabletops used to test people. Now it has to test a system.

Classic tabletop design assumed a fixed set of tools and a variable set of humans. The scenario changes, but the injects are built around decision points: who gets paged, who has authority to make the call, and whether the runbook gets followed under stress. The tooling is scenery; it doesn’t fail or mislead, and it doesn’t need its own line item in the after-action report.

> “If your triage system is summarizing alerts, an AI failure during a live incident doesn’t look like a server going down. It looks like a summary that’s confidently wrong.”

That’s no longer true once AI sits between your team and the information they act on. If your triage system is summarizing alerts, an AI failure during a live incident doesn’t look like a server going down. It looks like a summary that’s confidently wrong, a document retrieval that pulls a deprecated playbook because it matches keywords better than the current one, or a suggested response action that sounds reasonable but is quietly unsafe. Those failures are quiet. They don’t throw an error. They just make your responders slower or potentially wrong without anyone noticing until later. A tabletop that never injects one of these failures tests only half the system that will actually run during a real incident.

## What actually needs to be in the exercise now

A few categories of failure are new enough that most existing tabletop libraries don’t have injections for them yet. Worth building in:

**AI [gives a wrong or incomplete answer with total confidence.](https://thenewstack.io/rag-retrieval-scaling-architecture/)** This is the most important one and the easiest to skip, because it’s uncomfortable to design against your own tooling. Run a scenario where the AI-assisted triage step hallucinates the root cause, or the playbook lookup returns a document that’s close but outdated. The test isn’t whether the AI is right. It will eventually hallucinate; that’s a given. The test is whether your responders notice, and whether they have a habit of checking rather than trusting.

**AI System Availability.** This is the sharpest version of the problem for security teams specifically: what happens when the thing you’d normally lean on to investigate a compromise is the thing that’s compromised, or is offline because the incident took it down with it? Most teams have a fallback plan for “the SIEM is down.” Fewer have rehearsed “the AI system we use to triage is unavailable, and half the team has never actually run triage without it.” That gap doesn’t show up until you look for it.

**Guardrails get tested under actual pressure, not in a demo.** Guardrails that hold up in a calm design review often get quietly worked around when someone is three hours into an incident and just wants the AI to take the action instead of drafting a suggestion for a human to approve. A good tabletop inject puts a responder in exactly that position and watches what they do, not what the policy says they should do.

> “Guardrails that hold up in a calm design review often get quietly worked around when someone is three hours into an incident.”

**Nobody remembers how to do it the old way.** The flip side of AI doing triage and document retrieval well is that the muscle memory for doing it manually atrophies. If your team has spent a year with AI reliably surfacing the right playbook in seconds, most of them have not personally searched your documentation under time pressure in a long time. Test that skill directly, on purpose, before an incident forces you to find out if it’s gone.

**The handoff point is unclear.** AI-assisted response works because there’s a boundary: AI surfaces and suggests, a human in the loop decides and acts. Tabletops are a good place to find out whether the people operating on it actually understand that boundary, or whether it’s just written down somewhere. Build an inject where the “obviously correct” AI suggestion is subtly wrong, and see who catches it and who doesn’t.

## What this means for how you run the exercise

None of this requires throwing out your existing tabletop program. It requires adding a layer. A few practical changes:

Write injections that target the AI layer specifically, not just the human layer. If your scenario document only ever describes what happens to systems and people, and never what happens to the AI tooling sitting between them, you’re missing a category of failure that’s now [part of your real attack surface](https://thenewstack.io/cordyceps-cicd/) for response quality.

Include the people who build and maintain the AI tooling in the exercise, not just the responders who use it. They’re often the only ones who actually understand the failure modes worth injecting, and the exercise is a good forcing function for them to think about it too.

Debrief on your trusted AI Tooling, not just process compliance. The traditional after-action question is “did the team follow the runbook?” The new question sitting alongside it is “did the team trust the AI system the right amount,” not too little, which wastes the investment, and not too much, which is how a wrong answer becomes an incident on its own.

Treat “we tested this once” as insufficient. AI systems change: models get updated, retrieval sources get added, guardrails get adjusted, in ways your static documentation doesn’t. A tabletop that tested your AI-assisted response process a year ago is testing a system that no longer exists.

## The uncomfortable part

The teams most likely to skip this are the ones that’ve had the most success with AI-assisted response, because it’s working, and testing it feels like looking for problems that aren’t there. That’s exactly backward. The more load-bearing the AI system becomes, the more expensive it is to discover its failure modes for the first time during a [real incident](https://thenewstack.io/ai-devops-vs-sre-agents-compare-ai-incident-response-tools/) instead of a rehearsed one. We didn’t build AI into our response process to make it fragile. Tabletops are how we make sure we haven’t.

> “The more load-bearing the AI system becomes, the more expensive it is to discover its failure modes for the first time during a real incident instead of a rehearsed one.”

If your team is leaning on AI for triage, retrieval, or response, in security or anywhere else, the question worth asking this quarter isn’t whether your people are ready for the next incident. It’s whether you’ve actually tested the system they’ll rely on to get them there.

Test the system before the incident does it for you.

This article was o*riginally published on October 6, 2026, on* [*webflow.com*](https://webflow.com/blog/ai-incident-response-tabletops)*.*

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://cdn.thenewstack.io/media/2026/07/5f5aae47-andygombar.png)

Andy is a Staff Detection & Response Engineer at Webflow, where he founded and leads the detection and response program. With nearly six years at Webflow and a background spanning IT and military service, he brings a pragmatic, systems oriented...

Read more from Andy Gombar](https://thenewstack.io/author/andy-gombar/)