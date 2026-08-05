“**Raise your hand if** your team is actively using AI to write and review code. Now keep it up if you feel you have the security systems in place to account for that.”

This is how the panel discussion on security kicked off earlier this summer at [PlatformCon London](https://platformcon.com/live-day-london). The not-uncommon response to this question was that the hundreds assembled of platform engineers and engineering leaders raised their hands about using AI to write code. Then all but two of them kept their hands up when asked if they felt comfortable with the security systems they have in place to account for AI-written code.

This contrast begs the question: If we can’t go at the speed of AI securely, should we go that fast at all?

[Liz Rice](https://www.linkedin.com/in/lizrice/), chief open source officer at [Isovalent](https://isovalent.com/) and member of that panel discussion on security, told *The New Stack* last month, “The threat landscape has really changed a lot because finding vulnerabilities is almost wasted work now. What we’re doing in the AI world is non-deterministic, so having guardrails around what systems can do becomes ever more important because we can’t predict what models are going to do next.”

> “What we’re doing in the AI world is non-deterministic, so having guardrails around what systems can do becomes ever more important because we can’t predict what models are going to do next.”

Expanding that risk factor is that many more people in a company than even a few years ago might be able to write code that creates a security risk. So. should everybody in your company be onboarded to your [internal developer platform](https://thenewstack.io/7-core-elements-of-an-internal-developer-platform/ "internal developer platform")?

## AI-BOM: The threat lurking in your office cafeteria

Shadow AI is the uglier cousin of shadow IT, bringing more risks. But it is pushing organizations to really look at their cross-company IT adoption, and to consider what they need and what they really don’t. Because we know more tools and more lines of code are not indicators of anything but complexity.

“AI is going to radically change how we think about the full stack of technology from developers all the way down through platform engineering to the hardware, because there is no such thing as a zero-day anymore,” said panelist [Joe Baguley](https://www.linkedin.com/in/joebaguley/), CTO of EMEA at Broadcom during the group discussion. “I think the biggest concern actually is how we approach engineering because SBOMs [software bills of materials] are going to be really, really important going forward, and understanding what you’re building with your products, what dependencies you have.”

> “There is no such thing as a zero-day anymore.”

This extends to an AI bill of materials (AI-BOM) to track all non-deterministic components like model weights, training datasets, and third-party APIs to prevent gaps in your supply chain map, data poisoning, and regulatory non-compliance.

Baguley also predicted that companies will soon stop adopting wholesale open-source projects, opting instead to fork and keep the parts they use. On the other hand, he argues that the AI-driven ease of building your own systems is turning into Frankenstein’s monster, giving the example of 17 different HR professionals building 17 different AI agents to solve different aspects of their day-to-day.

Rice added during the discussion that this HR scenario becomes even more concerning when you consider the private information posseses about employees.

“I predict we’ll see some horror stories where people write their own whatever, and it will have vulnerabilities in it. However good your model is, it probably is not going to write absolutely secure code any more than a human does,” said Rice, who is also author of *Container Security* and *Learning eBPF*. “And let’s say it’s somebody from a non-technical background; they probably don’t know if it’s a safe thing. So with the ability to create more code more easily, we probably also end up seeing this more.”

> “However good your model is, it probably is not going to write absolutely secure code any more than a human does.”

If Frankenstein’s monster stays locked in the lab, it’s one thing. But what about when someone takes that insecure agentic AI hack off their laptop and shares it with the rest of their less-technical teammates?

“Someone in HR now has software, and it does a thing; you don’t need to pay for Asana. I now have a thing that Asana does, but now it runs locally,” offered panelist [Nigel Douglas](https://www.linkedin.com/in/nigel-douglas-devrel/), head of developer relations at Cloudsmith, to the PlatformCon audience. “We need to start thinking of the consumers of the resources as no longer just developers that have well-trained experience.”

So is the answer that everyone — each human and agent from each department — should be onboarded to the internal developer platform? Or does this call for a more traditional command-and-control IT platform?

## Do we have to change the way we platform… again?

In this post-Mythos era, patching can’t be done quickly enough.

Forget predictions for the future; AI models today can autonomously discover, chain, and exploit software vulnerabilities at scale, which is why Rice told *The New Stack*, “Organizations are going to need runtime shields to protect themselves before they have time to apply patches.”

Runtime shields, often based on eBPF, can safeguard file systems, prevent privilege escalations, and monitor network access. They are dynamic and quicker to implement than traditional reactive measures like caches, which require software rebuilding and redeployment. These shields act as a stopgap, providing immediate protection against known vulnerabilities or unexpected behavior.

“We could be protecting against privilege escalations; we could be checking against network access, all sorts of different conditions that we can build shields for, whether that’s in the form of guardrails to stop a vibe-coded action becoming unexpectedly wild or maybe in the form of CVE-specific runtime shields to detect the particular behavior of an exploit or problem,” Rice said.

This doesn’t mean you won’t re-patch and rebuild, but, at the speed of AI, already burnt-out security and site reliability engineers can’t keep up. In 2025 alone, a record 48,185 common vulnerabilities and exposures (CVEs) were published, with 20% of those deemed critical or high severity. All while the same [EdgeScan Vulnerabilities Statistics Report](https://www.edgescan.com/stats-report/) finds the mean time to patch or resolve was 55 days.

This had the PlatformCon panelists most worried about these *n*-day threats, public, known, patchable threats that nobody’s gotten to yet.

“What we’re looking at is how do we build platforms that are instantly patchable and continue to be updated for this instant *n*-day threat,” Baguley mused during the panel, where, like an iPhone update, the average user isn’t paying attention to what it does.

When it comes down to it, there his no low-level exploitation vulnerability anymore.

“We’re entering a world where it’s not just about how we control agents, but it’s about how you think about rebuilding platforms. We can’t use the processes from 20 years ago around security,” Baguley said.

“This is shift down and shift left at the same time. You’re going to need to think about how you make your platforms leaner, harder, and faster.”

---

*How is your platform team finding a way to securely keep up pace with both AI innovation and innovative AI attacks? [Connect with me on LinkedIn](https://www.linkedin.com/in/jkriggins/), so your lessons, fixes, and human-agentic collaboration can be the next case study in The New Stack.*

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://thenewstack.io/wp-content/uploads/2025/09/220bf6cf-jriggins-2025-600x600.jpeg)

Jennifer Riggins is a tech storyteller and journalist, event and panel host. She bridges the gap between business, culture and technology, with her work grounded in the developer experience. She has been a working writer since 2003, and is based...

Read more from Jennifer Riggins](https://thenewstack.io/author/jennifer-riggins/)