Your AI agents are growing up. It’s time your control model did, too.

Over the past two years, much of the AI conversation has focused on risk, and rightly so — jailbreaks, data leakage, and unintended actions. I’ve been the captain of Team Caution since the original publication of the OWASP Top 10 for LLMs, dating back to mid-2023.

The question is no longer “is AI risky?” but “how do we scale AI safely?”

AI agents have matured, and the use cases are broadening. AI reasoning is improving fast. They’re writing code, triaging alerts, resolving tickets, drafting reports — and they’re doing it in production, not just in labs. The pressing question now isn’t *whether* these agents are dangerous.

The pressing question is whether you’ve built the right control model to let them operate safely and productively.

It’s time to move from Human-in-the-Loop (HITL) to Human-on-the-Loop (HOTL).

## The Evolution From Prompt Engineering to AI Agent Supervision

We’ve moved past the copy-paste era of AI. Today, the agents are driving.

Let’s look at the evolution of AI actions over the past couple of years. We started with ChatGPT. It could generate ideas, draft emails, or write code snippets. But the human drove the entire automation loop. You copied, pasted, ran the code, and handled execution. The AI was reactive. You were in charge because you were doing all the work.

Then came tools like Cursor. Cursor gave the AI more power within coding workflows.  It could read and write files, execute commands, and modify your codebase directly. However, in typical usage, it often paused, looking to the human developer for guidance or permission before taking most actions. Even if the human interaction were as simple as repeatedly pressing the Tab key, the human was still fully engaged from minute to minute. This was Human-in-the-Loop in practice: The AI works, but the human drives.

Now we’re seeing a different pattern emerge, especially in tools like Claude Code, which have leaned into operational modes that allow for more autonomy.

You can still run Claude Code conservatively, but many developers are now allowing it to run more autonomously. Instead of checking in constantly, it presents a plan, gets approval once, and then executes across multiple steps — writing, testing, debugging, and iterating. These unsupervised workflow steps, which used to be seconds between human approval checks, can now often range into the 10s of minutes, or more.

You’re still involved. You’re monitoring. But you’re not micromanaging.

That’s Human-on-the-Loop — and it’s quickly becoming the only viable path to scale.

And it’s not just a software story. In the defense world, the same debate is playing out, with military leaders weighing whether autonomous drones should be allowed to take lethal action without a human in the loop. That’s not sci-fi. It’s systems architecture at a national scale.

## SIDEBAR: Autonomy in the Air

The HITL vs. HOTL debate isn’t just a software issue — it’s playing out right now inside the world’s leading defense programs.

Multiple governments are exploring fully autonomous fighter jets, capable of identifying threats and executing lethal force without real-time human input.

In parallel, there’s heavy investment in “loyal wingman” systems — semi-autonomous drones that fly alongside human pilots, executing delegated tasks while keeping a human firmly on the loop.

It’s a hotly contested design choice. Full autonomy promises speed and reach. But HOTL designs offer better accountability, coordination, and human judgment.

For now, the loyal wingman model has the edge. It captures many of the benefits of autonomy — without severing the link to human decision-making.

This isn’t a philosophical footnote. It’s a practical design decision that determines how — and whether — autonomy works in your system.

## Building Secure Autonomy: HOTL Implementation Framework

HOTL isn’t just about developer workflows. It’s about scaling autonomy *anywhere* machines are acting on our behalf.

The most mature examples today are in software development — but the same pattern is showing up across domains:

* Productivity agents managing calendars, documents, and outreach.
* Customer support bots resolving issues and routing tickets.
* Autonomous systems in logistics, finance, and infrastructure.

And beyond the enterprise, the implications are even more significant. The question of when a machine should act independently vs. when it should defer to a human isn’t just about code. It’s about policy, safety, and ethics.

## **What Secure Autonomy Actually Looks Like**

Human-on-the-Loop doesn’t mean removing safeguards. It means building systems that don’t *depend* on constant interruption to stay safe.

If you want your agents to act productively and responsibly without burning out their human handlers, you need:

* **Least-Privilege Tooling**
  + Don’t give your agent blanket permissions. Limit what it can access and what tools it can use. Smaller trust surface = smaller risk.
* **Runtime Observability**
  + Track what your agent is doing in real-time. This includes commands, file edits, tool use, and external calls. Not just logs — telemetry.
* **Triggerable Interventions**
  + Design for escalation. Agents should pause, notify, or route to a human when they hit unexpected conditions or high-risk actions.
* **Verification Pipelines**
  + Outputs from agents — especially those that affect systems or users — should pass through validation pipelines, just like human code in CI/CD.
* **Postmortem-Ready Logging**
  + When things go wrong, you should be able to see what happened and why. Traceability isn’t optional — it’s foundational.

## Cross-Functional Governance for AI Agent Control Systems

If you’re leading an AI transformation effort — as a Chief AI Officer, product exec, or functional leader — this shift affects you directly.

You can’t rely on your engineering team alone to set the boundaries for agent behavior. This is a cross-functional governance issue.

* Legal and compliance need to weigh in on acceptable autonomy.
* Product and UX teams need to define where the handoff happens between agent and user.
* Security needs to be designed for runtime monitoring and containment.
* Without cross-functional governance, AI agents become productivity mirages — or worse, security liabilities.

The move to HOTL changes your operating model. Ignoring it doesn’t delay the change — it just ensures your organization won’t be ready when it arrives.

## **You Can’t Sit This One Out**

The most effective agents today are the ones that operate under structured autonomy. Not clamped down. Not free-for-all. Just fast, capable, and supervised.

That’s Human-on-the-Loop.

It’s not a compromise. It’s a blueprint.

If you still require human approval at every step, you’re bottling yourself up. If you’re handing full control to the model without oversight, you’re taking a risk.

But if you structure your agents with guardrails, observability, and well-designed autonomy boundaries, you unlock the real value of agentic AI — at scale.

So stop waiting for permission.

Redesign your systems. Define your boundaries. And put the human on the loop instead of micromanaging.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://thenewstack.io/wp-content/uploads/2025/07/16f91268-steve-wilson-600x600.jpg)

Steve Wilson is a pioneer in generative AI and cybersecurity, driving advancements in AI-powered cyber defense and securing AI systems. As the Chief AI and Product Officer at Exabeam, the leader in AI-driven security operations, Steve spearheaded the launch of...

Read more from Steve Wilson](https://thenewstack.io/author/steve-wilson/)