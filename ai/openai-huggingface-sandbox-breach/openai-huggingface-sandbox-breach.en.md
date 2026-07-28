According to [OpenAI](https://openai.com/), the [Hugging Face](https://huggingface.co/) [security breach was an “unprecedented cyber incident,](https://openai.com/index/hugging-face-model-evaluation-security-incident/) involving state-of-the-art cyber capabilities.” Critics may disagree.

Back in 2018, for example, academics predicted that new [attacks might “arise that would be impractical for humans alone to develop](https://jp.reuters.com/article/artificial-intelligence-poses-risks-of-misuse-by-hackers-researchers-say-idUSL8N1QA7Z3/) or which exploit the vulnerabilities of AI systems themselves.”  Well, here we are.

## **What escaped the sandbox**

So, what really happened? OpenAI reports an autonomous security-evaluation run of [GPT‑5.6 Sol](https://thenewstack.io/openai-gpt-56-live/) and a pre-release model broke out of a sandbox, reached the internet, and then targeted Hugging Face to try to solve the [ExploitGym benchmark](https://kenhuangus.substack.com/p/when-the-model-cheats-by-hacking).

By OpenAI’s account, “an internal evaluation which prompts models to pursue advanced exploitation using complex attack paths … [with] maximal cyber capabilities by running this evaluation without production classifiers used to prevent models from pursuing high-risk cyber activity.”

OpenAI continues, “Our benchmarks run in a highly isolated environment, with network access constrained to the ability to install packages through an internally hosted third-party software that acts as a proxy and cache for package registries.”

> “All evidence suggests that the models were hyperfocused on finding a solution for ExploitGym, going to extreme lengths to achieve a rather narrow testing goal.”

The AI models, however, cracked their sandbox. Once out, they “identified and chained vulnerabilities across OpenAI’s research environment and Hugging Face’s production infrastructure to obtain test solutions directly from Hugging Face’s production database. All evidence suggests that the models were hyperfocused on finding a solution for ExploitGym, going to extreme lengths to achieve a rather narrow testing goal.”

AI expert [Ken Huang](https://www.linkedin.com/in/kenhuang8) describes the process in a [blog post](https://kenhuangus.substack.com/p/when-the-model-cheats-by-hacking): “The model spent enormous inference budget probing the sandbox, then found a zero-day in the third-party software OpenAI used as a package-registry proxy and cache.

“It used that bug to gain unrestricted internet access. It then reasoned that Hugging Face probably hosted the ExploitGym datasets, chained stolen credentials with several more vulnerabilities into a remote code execution path, and pulled the benchmark answers straight out of Hugging Face’s production database.”

## **Why intent no longer matters**

This was not, as [John W. Larson](https://www.linkedin.com/in/johnwlarson/), president and chief AI officer of the AI security company [Babel Street](https://www.babelstreet.com/), tells *The New Stack*, a “*Terminator*” moment. OpenAI models and agents “[were not] acting out of malice or trying to attack Hugging Face. It encountered obstacles, developed an unexpected strategy, bypassed safeguards, and pursued its assigned goal in a way its creators never anticipated. The incident demonstrates that harmful cyber incidents no longer require malicious intent: Only highly capable autonomous AI optimizing for an objective.

> Harmful cyber incidents no longer require malicious intent: Only highly capable autonomous AI optimizing for an objective.

That’s the first issue we must be aware of. Software attacks no longer require a hacker. All it needs is an LLM freed of guardrails with a mission to accomplish, and it will take whatever steps are needed to reach its goal.

In addition, [Adam Boynton](https://www.linkedin.com/in/adamboynton), senior enterprise security manager of EMEIA at the Apple Identity and Access Management company [Jamf](https://www.jamf.com/), tells *The New Stack*, “This happened inside a frontier lab deliberately stress-testing its most capable models, in conditions no enterprise would ever run.”

Boynton also notes that this episode confirmed that “AI tools are no longer just applications people open. They act on the user’s behalf, with the user’s access. So every organization needs a clear view of which AI tools its people are running, and how those tools are configured and used.”

An agent given too much power is far more capable than a user armed with a superuser password of causing havoc both to your systems and to ones far outside your control.

## **Where container isolation failed**

As for the attack itself, [Edera](https://edera.dev/) CMO [Kaylin Trychon](https://www.linkedin.com/in/kaylintrychon) writes in a [blog post](https://edera.dev/stories/cya-contain-your-architecture-mitigating-the-hugging-face-breach#), “This incident deserves more attention than ‘an AI did the hacking now.’ The interesting part isn’t who was driving, or even that it was a model instead of a person. It’s where the walls gave way, twice, in two different companies’ infrastructure — and that part is entirely familiar to anyone who’s spent time securing container infrastructure.”

Exactly so. Trychon continues, “Strip away the framing and this is a story about two escalation chains, back to back.” The first consisted of “The model found and exploited a zero-day in that proxy, then used privilege escalation and lateral movement inside OpenAI’s own ‘highly isolated’ testing environment until it reached a node with open internet access.”

Next, OpenAI’s models inferred, correctly,  that “Hugging Face likely hosted the datasets, models, and reference solutions for the benchmark it was trying to solve. It chained stolen credentials with a remote-code-execution path into Hugging Face’s servers, harvested more credentials, and moved laterally into several internal clusters over a weekend, all in pursuit of one narrow goal: Finding the answer key.”

> “The failure that actually matters is what a single code-execution event is allowed to become — and notably, that failure happened the same way twice, at two different companies, in the same incident.”

The serious issue, from Trychon’s perspective, is that “both companies’ blast radius was a cluster instead of a container.”

That’s because “the failure that actually matters is what a single code-execution event is allowed to become – and notably, that failure happened the same way twice, at two different companies, in the same incident. In a typical container fleet, workloads [share a kernel](https://edera.dev/stories/the-shared-kernel-is-the-real-problem-in-container-security).

“A process that gets popped, or a model that gets a shell, is one syscall boundary away from the node it’s running on, and the node is one set of mounted credentials away from the rest of the cluster. Namespaces and cgroups are process-isolation primitives, [not security boundaries](https://edera.dev/stories/kubernetes-finally-has-user-namespace-support-the-shared-kernel-problem-remains) — they were never designed to hold against an attacker (human or model) that already has code execution and time.”

People might not have been able to do this easily. But as Bloomberg succinctly put it, [“OpenAI Models Spent Hours on Hack That Usually Takes Weeks.](https://www.bloomberg.com/news/articles/2026-07-23/openai-models-lurked-in-hugging-face-system-for-hours-undetected)” Exactly so. We can expect to see more such successful attacks.

## **Beyond the sandbox paradigm**

Edera’s CTO and co-founder [Alex Zenla](https://www.linkedin.com/in/azenla/) tells *The New Stack*, “The sandbox escape here isn’t really the surprising part of this attack. An entire market of AI sandboxing tools has exploded over the past couple of months, and this is the reality they’re all built on top of: containers, VMs via namespaces — whatever the branding — most of them still share a kernel with the host or with each other.

“That’s a boundary enforced in software, and software boundaries are exactly the kind of thing an agent that can try ten thousand escape paths over a weekend is going to find a way through. We shouldn’t be shocked that this happened; we should be shocked at how many teams are still betting their infrastructure on technology that was never designed to withstand such a persistent adversary. The fix isn’t a better sandbox; it’s getting out of the sandbox paradigm entirely.”

Zenla continues, “Teams should adopt secure execution environments that are hardware-enforced and eliminate the shared kernel flaw. This technology exists today and would have made this specific escalation chain structurally impossible, not just harder. Teams running agents with real permissions and real access need to stop treating this as a someday problem, because the next version of this week is already being tested somewhere right now.”

That underlines the most important issue of all. Thanks to AI, security attackers are coming harder and faster than ever. Security can no longer be an afterthought.

As [Jim Zemlin](https://www.linkedin.com/in/zemlin), the Linux Foundation CEO, said at the 2026 Open Source Summit North America, “[the exploit time for a zero-day vulnerability being exploited has shrunk from 63 days to -7 days](https://www.linkedin.com/posts/the-linux-foundation_the-bill-for-open-source-cybersecurity-is-activity-7468361250796711936-V3Tj/).”

You literally no longer have time to wait for security fixes. You must bake in as much security as you can as fast as you can, or your systems will be broken into. It’s as simple as that.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://cdn.thenewstack.io/media/2023/03/cee63948-cropped-8a0b5c52-steven-vaughan-nichols.jpg)

Steven J. Vaughan-Nichols, aka sjvn, has been writing about technology and the business of technology since CP/M-80 was the cutting-edge PC operating system, 300bps was a fast internet connection, WordStar was the state-of-the-art word processor, and we liked it.

Read more from Steven J. Vaughan-Nichols](https://thenewstack.io/author/sjvn/)