Modern software development has evolved fast, and static analysis-based security tools haven’t. Today’s engineering teams are building cloud native apps using microservices, containers, serverless functions, and dynamic infrastructure that changes by the minute. Meanwhile, generative AI is accelerating how and when we write code. Developers now use LLMs to scaffold out APIs, generate config files, and even handle business logic. The result? Code is shipping faster than ever, but the complexity — and the risk — are stacking up.

And yet, most static analysis tools are stuck in the past. They were designed to take snapshots for monoliths, single-language stacks, and linear build pipelines, with code that was written manually. In 2025, that’s just not how software works anymore.

To keep pace, security tools must evolve in tandem with software development. They need to operate at runtime, leverage machine learning to detect abnormal behavior, and adapt to ever-changing environments. Static analysis alone simply can’t see enough or move fast enough.

## **Microservices Break Traditional Scanners**

In cloud native environments, your “codebase” isn’t one repo — it’s many. You’ve written services in Go, Python, Node, and possibly some Rust for performance-critical paths. They’re deployed via Kubernetes, communicating over gRPC or message queues, and managed through GitOps workflows. Static tools usually analyze one codebase at a time. They don’t understand distributed systems. If a vulnerability lives at the intersection of two services — say, insecure auth flow between an API and a worker — a scanner probably won’t catch it. They can’t follow calls across repos, languages, or service meshes. That’s a major blind spot.

Runtime security tools, enhanced by machine learning, can. By [observing live interactions between services](https://thenewstack.io/trend-report-merging-observability-and-it-service-management/), they detect suspicious behavior, misconfigurations, or privilege escalations in real-time, even if those vulnerabilities are invisible in the code. Machine learning can learn normal service-to-service interactions and flag anomalies that traditional tools miss.

## **AI Is Writing Code Faster Than We Can Audit It**

Let’s be honest: AI-assisted coding is here to stay. [According to Y Combinator](https://leaddev.com/hiring/95-ai-written-code-unpacking-the-y-combinator-ceos-developer-jobs-bombshell#:~:text=The%20CEO%20of%20famed%20Silicon,%2C), a quarter of its startups report using AI to generate 95% or more of their code. Whether it’s GitHub Copilot or a custom LLM workflow, [developers are using generative tools to move faster](https://thenewstack.io/ebooks/generative-ai/how-generative-ai-transforms-software-development/). That means more code, more dependencies, and a larger surface area — much of it written without thorough review. Even when the output of an LLM “looks good,” on the surface, it might be missing important context: secure defaults, rate limits, proper error handling, or compliance constraints. In fact, AI-driven [coding may introduce new compliance](https://thenewstack.io/checks-by-google-ai-powered-compliance-for-apps-and-code/) issues or vulnerabilities, such as overly permissive access to APIs or storage.

Legacy scan-based [security tools might discover the same overly permissive AI-driven code](https://thenewstack.io/level-up-your-software-quality-with-static-code-analysis/) hours — or even days — after deployment, leaving your organization exposed, and that just isn’t a risk that can be accepted.

That’s where runtime security becomes essential. It validates behavior in the wild by observing how components behave once deployed. Machine learning enables these systems to detect unusual access patterns, misused privileges, and other signs of AI-generated risk.

## **Noise Still Drowns Out Signal**

If you’ve worked with static scanners, you’ve seen this: Pages of alerts, most of which don’t matter. A string that *might* be a secret (but isn’t); an unused variable flagged as a potential bug; a theoretical injection vector behind a hardcoded value. Cloud native teams don’t have time to sift through all that noise, especially when deploying 10+ times a day. False positives erode trust. They are made even worse by AI-driven development, which increases velocity. If your tool cries wolf often enough, engineers will stop listening. At that point, the tool is not helping security; it’s harming it.

Runtime-based tools change the game. Instead of relying on static guesses, they base alerts on what is happening in production. Is it a service accessing a database it has never accessed before? Is a lambda making unexpected outbound requests? With machine learning, security tools can continuously improve — learning what’s normal, reducing false positives, and flagging real issues before they escalate.

## **Attackers Know How Static Tools Work — and How to Evade Them**

Modern attackers aren’t writing simple exploits into code. They use dynamic payloads, obfuscation, and runtime logic that static tools can’t see. If your scanner only looks at code at rest, it’s going to miss malware that’s injected via runtime environment variables or assembled on the fly. This isn’t theoretical — it’s happening today, especially in supply chain attacks. Static [analysis must work](https://thenewstack.io/dont-mess-with-the-master-working-with-branches-in-git-and-github/) in conjunction with runtime monitoring and behavioral tools. Otherwise, it’s just checking the locks on an open window.

Static tools will never see runtime payloads. But runtime security tools will, especially those powered by machine learning. By analyzing live execution patterns, machine learning models can detect suspicious behavior: lateral movement, credential misuse, or data exfiltration. Runtime protection doesn’t just find problems — it stops active threats in progress.

In a world where supply chain attacks are increasingly common, this real-time defense is no longer optional. It’s critical.

## **CI/CD Can’t Wait**

Cloud native teams live in CI/CD pipelines. Code gets built, tested, and deployed automatically, sometimes several times an hour. Security tooling that can’t keep up will get ignored or removed. Long scan times? Excessive false alarms? Lack of container or IaC support? That’s a dealbreaker. To work in DevSecOps workflows, static tools need to be fast, accurate, and built for automation. They have to scan containers, Kubernetes manifests, Terraform files, and Helm charts, not just application code. And they need to do it without blocking the team.

Runtime tools are designed to operate post-deploy, running continuously alongside your applications. They don’t need to block builds — they protect what’s live. Even better, when combined with machine learning, runtime tools get smarter with every deployment. They recognize normal behavior across releases, reduce noise, and adapt as your stack evolves. That’s security built for velocity.

## **Static Isn’t Dead, But It’s Not Enough**

Security can’t be bolted on — it has to flow with your stack. If your tooling isn’t built for cloud native and AI-native code, it’s already outdated. Static analysis still has a role, especially within sensitive workloads. But on its own, it’s nowhere near enough for modern, [cloud native development](https://thenewstack.io/cloud-native/ "cloud native development"): it doesn’t see across services, it struggles with high-velocity AI-generated code, it drowns teams in noise, and it slows down pipelines.

Instead of relying solely on static analysis, we need security tools built for runtime that monitor live environments and use machine learning to adapt, while still offering the benefits of static scanning. This shift to dynamic, intelligent runtime monitoring will help manage complexity, decrease irrelevant alerts, and lower security risks, all while not hindering DevSecOps workflows, by extending protection across the entire software development lifecycle.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://thenewstack.io/wp-content/uploads/2025/06/e2d8407c-1711049732493-600x600.jpeg)

Chris Lentricchia is a versatile B2B SaaS product marketing professional with nearly a decade of experience across open and closed source technologies, from Linux to Kubernetes. He's passionate about making complex tech easy to understand, specializing in content, messaging, and...

Read more from Chris Lentricchia](https://thenewstack.io/author/chris-lentricchia/)