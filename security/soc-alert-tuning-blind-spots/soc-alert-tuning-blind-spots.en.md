The number of incoming IT security alerts arriving at enterprise security operations centers (SOCs) today is staggering, with one IT security industry study estimating that a typical SOC can be hit by some [3,000 or more security alerts each day](https://www.prnewswire.com/news-releases/new-vectra-ai-research-finds-cyber-resilience-lagging-in-the-ai-era-302681983.html).

Another report, a [survey conducted by the security-focused SANS Institute](https://sansorg.egnyte.com/dl/mq6DfGwdgJKC), found that 73% of those alerts are false positives, leading to alert fatigue for security analysts as they actively chase potential threats.

## The cost of false positives

This cat-and-mouse battle is costly for enterprises, racking up an estimated $3.3 billion annually in U.S. costs to manually triage these alerts.

With such a high number of benign alerts reported, it shows how tough it is for teams to sort the real threats from the noise.

For SOC team members, directing their attention towards the valid alerts is the toughest part of their fight. The sheer number of false-positive alerts can lead security analysts to focus on them, become desensitized, and miss actual threats.

In an attempt to dampen the noise of false-positive alerts, alert tuning is one of the biggest requirements and challenges for SOC teams, but it can have unexpected and unwanted consequences.

Ultimately, every tuning decision is essentially a bet that the signal you’re dampening isn’t the one an attacker will exploit next. For security teams, this is a maddening ballet that plays out every day in the SOC.

[Mika Ayenson](https://www.linkedin.com/in/mika-ayenson/), threat research and detection engineering team lead at [Elastic](https://www.elastic.co/), tells *The New Stack* it’s a constant challenge.

“These are the things that SOC analysts struggle with on a daily basis,” Ayenson says*.* “People think that you can keep tossing more tools and more rules at this problem, but fundamentally, the questions here get to what the engineers must do to address the root causes.”

## When tuning creates blind spots

That means not just suppressing alerts, but making every single tuning measurable from performance and efficacy standpoints that are contextual and tied deeply to the threats, says Ayenson. The tuning steps must also be reversible in case they are found to be wrong, he added. “We must do all these things to ensure that we’re reducing that fatigue without also creating blind spots along the way.”

## **Why less mature security teams tune aggressively**

Aggressive tuning and rule exceptions arise from operational pressures as SOC analysts monitor hundreds or thousands of incoming alerts.

“Fatigue is a real thing,” says Ayenson. “And for them, alert suppression traditionally may feel like it’s the only way to stay functional. It solves that queue management piece of the pie, but it does not necessarily address the risk management piece.”

Adding new alert exceptions and raising their thresholds reduces the number of alerts, but they lead to security trade-offs that don’t deliver operational fixes and can introduce new conflicts.

**How over-tuning can inadvertently cause missed threats**

Every single tuning, every reduction in the alert threshold, is an opportunity to lose visibility into incoming threats, says Ayenson. “You’re wagering your bets that a weak threat signal you’re tuning out no longer matters. And along the way, you might create these coverage gaps that you don’t know exist.”

What that does is desensitize analysts to threats, especially quiet threats operating in a low-signal space where they often hide and thrive.

> “The biggest risk is not the alerts you see. It’s really the one that you tuned away.”

“Unfortunately, what can happen is that less mature security teams are optimizing for what’s visible in the alerts, rather than optimizing for what can be missed,” says Ayenson. “The biggest risk is not the alerts you see. It’s really the one that you tuned away.”

This is how attackers try to do subtle things that look normal and benign. For instance, masquerading sensitive file access beneath normal activity that you see from GenAI capabilities like Claude, Cursor, Copilot, or Codex. Often, these cases are only discovered when small anomalies are connected by an insightful security analyst into a malicious incident.

“Attackers are going to try to operate without triggering any alerts,” says Ayenson. “And with AI, they’re moving faster. In some of the latest supply chain attacks, they’re not worried about being stealthy. Instead, they’re making it clear that they are there, that they did what they needed to do, and that they are going to be loud and noisy about it because they can do it.”

## **A better approach than blunt suppression**

So, how can these problems be effectively addressed to bring tuning issues to their knees?

The thing to remember is that tunings are not just about reducing noise, says Ayenson.

“Sometimes tunings are about increasing coverage and efficacy, and you have to do that in a way that isn’t risky to the point where you’ve expanded the scope of a rule, and now it’s being flooded. The problem is that as you increase the scope of a rule, it might also increase the risk of false positives. So, you have to weigh the change, collect that data, perhaps make another subsequent tune, roll it back altogether, and make a more tactical change.”

This is Elastic’s tactical approach, by focusing on critical behavioral baselines to detect threats.

“We try to fundamentally replace alert suppression with better understanding, focusing on correlation and connecting all those weak signals, instead of just removing them,,” says Ayenson. ” It’s about keeping the right signals in the detection process.”

For example, that means observing unusual behaviors across systems and bringing them together for further analysis, says Ayenson. “You identify a user credential that’s being accessed from an endpoint in the cloud at 3:00 a.m. that looks suspicious. The security team has never seen that user do this before or attempt to access that resource. These are the types of questions that we can answer as we start to bring together different multi-domain analytics.”

## **Reduce alert fatigue without reducing visibility**

In a world of increasing threats from cunning AI-driven cyberattacks, SOC teams must start viewing alert tuning as a risk decision rather than just a way to counter alert fatigue.

> “The goal isn’t creating more alerts. It’s having fewer regrets.”

“The goal isn’t creating more alerts,” says Ayenson. “It’s having fewer regrets. You want to reduce fatigue without reducing visibility. You want higher confidence alerts. You want to preserve coverage across different attack stages. You want to talk with analysts to know when they see alerts that they’re actually looking at an impending attack and real threat, not just noise.”

To accomplish this, security analysts must ask which coverages are being weakened before they suppress alerts, and thoroughly document, review, and test the changes they make against earlier attack simulations or incidents.

“Humans have the instincts and the right mindset to question if things look normal, while AI can look at volumes of data across time,” says Ayenson. “That human insight can be used to second-guess and question and come up with a hypothesis that can then be validated and tested empirically to analyze if the threat signals are valid or not. That’s the name of the game, finding the right signals and using them to corroborate a bigger attack chain.”

## **Achieving security alert tuning success**

To help enterprises solve these vexing alert-tuning challenges in response to increasingly stealthy criminal attacks, they need technology that enables SOC teams to improve precision without introducing new blind spots.

That’s where [Elastic Security](https://www.elastic.co/security/ai) can be a critical tool for SOC teams because it focuses on the alerts, rules, and [automated threat protection capabilities](https://www.elastic.co/security/automated-threat-protection) that are central to their enterprise security  responsibilities.

At the heart of Elastic Security is [Elastic Workflows](https://www.elastic.co/security/soar), which automates the full alert lifecycle from triage and enrichment to response, with no stand-alone Security Orchestration, Automation, and Response (SOAR) platform required. When investigations call for judgment beyond scripted steps, AI agents step in to reason through the complexity, giving teams both reliable execution and intelligent analysis in a single platform.

“We’re writing rules based on the actual behaviors that are happening below the surface,” Ayenson says. “With the new agents and workflows, people can take the expertise of their teams and codify them into workflows using and backed by AI agents. It’s not enough just to maintain rules and create more rules. You must understand the threat piece as well so you’re not creating a bunch of weak protections. You must do both things together.”

Ultimately, alert tuning needs to be approached as a risk management exercise, he says.

For teams looking to improve their cybersecurity posture in the age of AI, Elastic’s expertise in enterprise security, search, and observability can help deliver the missing pieces they need to bolster their defenses.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://thenewstack.io/wp-content/uploads/2024/07/00ef81b0-cropped-0a249176-todd-r.-weiss-headshot-2-600x600.jpg)

Todd R. Weiss has been covering technology beats since 2000, first as a staff writer for Computerworld and eWEEK, and later as a freelancer for The New Stack, MSSP Alert, Computerworld, TechRepublic, CIO.com, eWEEK, Data Center Knowledge, IT Pro Today,...

Read more from Todd R. Weiss](https://thenewstack.io/author/todd-r-weiss/)