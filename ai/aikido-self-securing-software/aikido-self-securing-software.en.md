While traditional [penetration testing](https://thenewstack.io/use-pen-testing-to-gauge-software-development-life-cycle-health/) relies on manual or point-in-time assessments, often delivered weeks after software has already shipped, software security solution provider [Aikido](https://www.aikido.dev/) has introduced [Infinite](https://www.aikido.dev/blog/introducing-aikido-infinite), which provides continuous AI penetration testing.

The Brussels-based company is calling Infinite the industry’s first continuous [AI penetration testing](https://thenewstack.io/evil-models-and-exploits-when-ai-becomes-the-attacker/) solution. That is, one that doesn’t just find vulnerabilities, but validates whether they’re actually exploitable and generates patches, all within the same automated workflow.

## Self-securing software

The goal, according to Aikido co-founder and CEO [Willem Delbare](https://www.linkedin.com/in/willemdelbare/?originalSubdomain=be), is software that essentially secures itself.

“For years, organizations have been working around the limitations of traditional testing and [DAST](https://thenewstack.io/devsecops-tools-that-offer-security-efficiency-and-quality/) [Dynamic Application Security Testing] because there was nothing better available,” [Willem Delbare](https://www.linkedin.com/in/willemdelbare/?originalSubdomain=be), co-founder and CEO of Aikido, says in a statement. “Software delivery is now continuous, but security testing isn’t. Infinite completely changes that. This is the beginning of self-securing software.”

In a recent survey of 500 security and engineering leaders, Aikido found that 76% deploy significant production changes weekly or faster — yet only 21% validate security on every release. Meanwhile, 85% report that security findings are outdated by the time final reports land.

Traditional penetration testing, typically an annual or biannual exercise that can cost up to $15,000 per engagement, simply wasn’t built for a world where code ships daily, Delbare tells *The New Stack*.

> “Developers can no longer manually review all this AI-generated code,” he says. “So, it has to be reviewed by AI as well.”

Delbare says the bottleneck in modern software development is rapidly shifting from how fast teams can write code — AI has largely solved that— to how fast they can verify that code is secure. He says AI pen testing now works about two to three times better than human pen testing.

“Developers can no longer manually review all this AI-generated code,” he says. “So, it has to be reviewed by AI as well.”

Infinite addresses this problem by triggering agentic pentesting on every release. Agents explore the full attack surface — including undocumented endpoints, hidden logic paths, and cross-layer architectural interactions that manual testers typically don’t have time to pursue — confirm whether vulnerabilities are actually exploitable, and then open pull requests with fixes. Teams can review and merge, or let the loop run. The system learns from each deployment, building a continuous feedback cycle rather than a periodic snapshot.

Security teams can expand their capacity with elite hacking agents dedicated to finding security holes in every piece of code pushed, 24/7, according to Aikido.

## Near-term goal

Delbare acknowledges that fully autonomous security is still a near-term goal rather than today’s reality. “The only thing that Infinite will do is schedule automated pen tests,” he said in a recent briefing. “It’s more like a scheduling tool,” but one that closes the loop between detection, validation, and remediation in a way existing tools don’t, he says.

“As software delivery cycles shorten and change becomes constant, point-in-time security models no longer reflect how modern systems operate,” [Katie Norton](https://www.linkedin.com/in/katie-d-norton/), research manager, DevSecOps and Software Supply Chain Security at [IDC](https://my.idc.com/getdoc.jsp?containerId=PRF005561), says in a statement. “We are beginning to see early signs of a more autonomous security approach, where exploitability validation and remediation are embedded directly into the software lifecycle. Aikido Infinite reflects this shift by combining continuous testing with remediation capabilities inside a unified platform.”

So, when will we see autonomous self-securing software?

“I think that’s basically where we’re headed very soon, because the amount of code reviews is just too big,” Delbare tells *The New Stack*. “So, it needs to become autonomous, or else it won’t work.”

> “I’m not sure we need or want fully autonomous software operations like that right now.”

[Brad Shimmin](https://www.linkedin.com/in/bradshimmin/), an analyst at the Futurum Group, tells *The New Stack* he believes we are far from seeing fully autonomous self-securing software.

“I’m not sure we need or want fully autonomous software operations like that right now, anyway, especially as we move faster and faster into agentic software development practices,” he says. “I think the best we can hope for right now is to build an understanding of our software and how to secure that software.

“The more we place into the hands of probability-led automation, the less likely we are to even know when we have a security issue that needs addressing. If you don’t believe me, ask any of the hundreds of thousands of [OpenClaw](https://thenewstack.io/openclaw-github-stars-security/) users who were surprised to see their security keys in the open.”

## Aikido in practice

Aikido isn’t just making its case in theory. The company’s AI penetration testing system recently discovered and responsibly [disclosed a high-severity cache deception vulnerability](https://www.aikido.dev/blog/sveltespill-cache-deception-sveltekit-vercel) affecting default [SvelteKit](https://thenewstack.io/rich-harris-talks-sveltekit-and-whats-next-for-svelte/) applications deployed on [Vercel](https://vercel.com/), the framework’s most common hosting platform.

Apps using cookie-based authentication were exposed by default — a single malicious link could cause authenticated responses, including session data and private API output, to be cached publicly and retrieved by an attacker.

The flaw emerged from an interaction between SvelteKit’s rewrite logic and Vercel’s caching behavior, spanning more than 150,000 lines of framework and adapter code. Vercel has since patched the issue across the platform.

“The attacker only needs to be right once,” Delbare tells *The New Stack*, “Whereas on the defender side, you need to be right literally every time. AI gives the attacker the upper hand again. We’re essentially trying to even that playing field.”

## Agentic penetration testing

Each software change triggers agentic penetration testing agents that expose risk, validate exploitability, apply remediation where safe, and retest to confirm risk reduction. Instead of relying on periodic engagements, teams gain a continuous feedback loop that operates alongside deployment, not after it, the company says.

Aikido’s agents autonomously pursue every possible route of attack across the application’s total surface area, identifying undocumented endpoints, hidden logic paths, complex multi-step edge cases, and architectural anomalies that are often unknown by testers today or too time-consuming for manual testers to address, the company says.

Moreover, Aikido Infinite learns from every finding on each deployment, providing a continuous feedback loop that developers can then use to improve code security even before commit.

Infinite builds on [Aikido Attack](https://www.aikido.dev/attack/aipentest), the company’s existing on-demand AI pentesting product, and runs on a model-agnostic architecture. It also connects to a broader platform that spans code, cloud, and runtime, which Aikido says gives its agents an edge over tools that test only from the outside in.

Meanwhile, the Futurum Group’s Shimmin notes: “I would say that we are still quite a ways away from that [self-securing software], even within well-defined areas like security.”

Right now, we have the tools to support intelligent monitoring and human-in-the-loop automation for select tasks, such as applying security patches, all within well-bounded, static software products such as a database management system, he adds.

“But that’s a long way from zero or nearly zero human intervention and control. And honestly, those are the first two steps on the road to autonomous operations,” Shimmin tells *The New Stack*.

Delbare claims Aikido is the fastest European cybersecurity startup to reach unicorn status. It has grown to 200 employees and is targeting $200 million in annual revenue within 18 months.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://thenewstack.io/wp-content/uploads/2021/06/a95bb5bc-image-576x600.png)

Darryl K. Taft covers DevOps, software development tools and developer-related issues from his office in the Baltimore area. He has more than 25 years of experience in the business and is always looking for the next scoop. He has worked...

Read more from Darryl K. Taft](https://thenewstack.io/author/darryl-taft/)