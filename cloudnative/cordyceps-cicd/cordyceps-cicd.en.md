On June 24, research from Novee Security was [released](https://thehackernews.com/2026/06/cordyceps-cicd-flaws-expose-300-github.html), reporting a CI/CD weakness that could enable anyone with an unauthenticated free GitHub account to hijack trusted workflows and compromise open-source supply chains.

Dubbed “Cordyceps” after the parasitic fungus, the weakness allegedly appeared across dozens of organizations, both small and large, including Microsoft, Google, Apache, Python, and Cloudflare. After scanning roughly 30,000 high-impact repositories, the penetration-testing company says it flagged 654 repositories as potentially exploitable and confirmed 300 as fully exploitable.

Though locking down workflows is a wise first step to reducing exposure, it doesn’t address the deeper issue: Many developers don’t consider the CI/CD pipeline a critical supply chain risk.

That needs to change. As [Peyton Kennedy](https://www.linkedin.com/in/peytonkennedyappsec/), senior security researcher at Endor Labs, tells *The New Stack*: “The damage from a single mistake tends to be large since pipelines hold the keys to source code, secrets, and the ability to ship software, so one foothold can reach far downstream.”

## Why does normal code review miss CI/CD risks

When asked why Cordyceps was able to slip by normal code review, [Elad Meged,](https://www.linkedin.com/in/eladmeged/) founding engineer and security researcher at Novee Security, tells *The New Stack* that most development teams still don’t treat CI/CD workflow YAML as security-critical code:

“These workflows are ‘just configuration’ in many developers’ minds, but in practice they run commands, handle credentials, publish packages, and make release decisions,” he says. “A bug in workflow logic can be as dangerous as a bug in application code.”

[Sonu Kapoor](https://www.linkedin.com/in/sonu-kapoor/), senior angular consultant, SOLID Software Solutions LTD, agrees that the main reason flaws like Cordyceps can evade normal code review is that they lurk where most developers aren’t looking.

> “A bug in workflow logic can be as dangerous as a bug in application code.”

While teams may check whether workflows build, test, and deploy properly, they often overlook key security questions about those workflows: “Who can trigger this workflow, what permissions does it receive, are secrets available, and can untrusted pull request data influence a privileged step? This is where the real risk hides,” he says.

It’s not just developers, though. Security scanners can miss these attack paths, too, as they typically only look for known-bad patterns, e.g., a specific dangerous string or setting. But as Kennedy explains for *The New Stack*, weaknesses like Cordyceps take a different shape: “They are a path that untrusted input travels to reach a powerful action, and whether that path is dangerous depends on context the scanner has to understand rather than match.”

In other words, rather than simply identifying and flagging a keyword, scanners need to go a step further to trace and understand where outside input enters the workflow, what permissions that workflow has, and what an input could impact downstream.

## What this means for devs: start thinking of CI/CD as part of the supply chain

Cordyceps isn’t the only warning of late. In March, threat actor [TeamPCP turned Aqua Security’s own Trivy scanner into a weapon against millions of developers](https://thenewstack.io/teampcp-trivy-supply-chain-attack/).

Both incidents are warnings that the CI/CD pipeline is no longer just configuration but a [key part of the software supply chain front line](https://thenewstack.io/cicd-pipeline-front-line/) — and a surface developers need to start giving more attention.

> The key question is not only ‘is this workflow safe?’ It is: ‘Can untrusted input move from a low-privilege place into a high-privilege action?’”

As Kennedy tells *The New Stack*, it starts with changing the way developers review CI/CD workflows:

“Treat pipelines as production systems that hold real credentials and real reach, with the same seriousness you give any production surface.”

Specifically, he advises anchoring each review in three questions: What triggered the workflow? What permissions did it have when it ran? And what can an outside input reach using those permissions?

Meged, for his part, suggests developers think of CI/CD workflows the way an attacker would, i.e., starting from the end goal and working backward. As he describes it for *The New Stack*, “The key question is not only ‘is this workflow safe?’ It is: ‘Can untrusted input move from a low-privilege place into a high-privilege action?’”

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://thenewstack.io/wp-content/uploads/2025/09/53f49f49-cropped-35fc143f-meredith-shubel-2-600x600.jpg)

Meredith Shubel is a technical writer covering cloud infrastructure and enterprise software. She has contributed to The New Stack since 2022, profiling startups and exploring how organizations adopt emerging technologies. Beyond The New Stack, she ghostwrites white papers, executive bylines,...

Read more from Meredith Shubel](https://thenewstack.io/author/mshubel/)