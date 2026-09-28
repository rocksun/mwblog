**Enterprise [Java](https://thenewstack.io/introduction-to-java-programming-language/) company Azul** announced its Azul Intelligence Cloud AI Assistant on Wednesday. The technology arrives in response to industry-wide alerts that AI has become a force multiplier for threat actors today.

The [Azul](https://www.azul.com/) service is a natural-language query interface that allows software engineering teams to see where [security risk](https://thenewstack.io/building-with-mcp-mind-the-security-gaps/) and licensing infringements are hiding in their live production Java estate. The assistant provides answers that are “grounded in live runtime data”, so it replaces static reports that grow less accurate after the day they’re generated.

## How fast do code-scanning reports go stale?

Azul said that “most IT and engineering teams” still manage Java risk with static IT and software asset management (ITAM/SAM) reports and code-scanning tools that describe a moment in time. The company has insisted that these reports are “accurate on the day they’re generated, and increasingly wrong after that”, typically because Java Virtual Machines (JVMs) are spun up, patched, drifted and retired underneath the report’s scope.

“For years, enterprises have built dashboards and reports to understand what’s actually running in their Java estate, but by the time a report gets properly summarized and reviewed, the risk it describes has often already changed,” said [Scott Sellers](https://www.azul.com/leadership/scott-sellers/), co-founder and CEO of Azul. “That used to be a productivity problem. Now that AI can find and weaponize a vulnerability in hours instead of weeks, it’s a business risk – for security, for compliance and for the licensing exposure that shows up in an audit.”

> “Now that AI can find and weaponize a vulnerability in hours instead of weeks, it’s a business risk…”

The Azul Intelligence Cloud AI Assistant lets software teams ask a direct question, in plain language, and get an answer grounded in what’s actually running in production right at that moment in time, as well as query historical information for further analysis.

## The weaponization gap is closing

Where enterprises run business-critical workloads on Java alongside AI services, Azul said the practical effect is that the gap between a [Common Vulnerabilities and Exposures](https://thenewstack.io/how-linux-kernel-deals-with-tracking-cve-security-issues/) (CVE) entry being disclosed and it being weaponized is getting shorter.

Citing AI models such as Anthropic’s Mythos and OpenAI’s Aardvark, which have autonomously discovered real-world vulnerabilities, the company pointed to an April 2026 Cloud Security Alliance [white paper](https://labs.cloudsecurityalliance.org/wp-content/uploads/2026/04/CSA_whitepaper_collapsing-exploit-window-ai-mtte_20260411-csa-styled.pdf) (listed as unofficial AI-assisted research), which suggested that, “While organizations historically took a median of 32 days to apply patches to known vulnerabilities – a window that once roughly corresponded to the time available before exploitation began – that window has collapsed to approximately 5 days for median time-to-exploit in 2025.”

Azul highlighted its Intelligence Cloud service, which gives engineers two “continuously updated” records of their Java estate: [JVM Inventory](https://www.azul.com/products/components/jvm-inventory/), a live catalog of every JVM instance running anywhere (on-premises, cloud or container) and [Code Inventory](https://www.azul.com/products/components/code-inventory/), a runtime record of which code actually executes in production versus what is merely provisioned. The new AI Assistant puts in a conversational layer using LLM models on top of both.

Software engineers can ask questions such as:

* “Which JVMs are running Java versions which are not the latest updates?”
* “Where is Oracle Java running in production right now?”
* “What code hasn’t run in the past four quarters and is safe to remove?”

In the [FAQ](https://www.azul.com/newsroom/azul-launches-ai-assistant-that-tells-it-and-security-teams-where-java-licensing-and-security-risk-is-hiding/) section of its announcement, Azul suggested that post-migration JVM “drift is common”, often due to a rollback, a forgotten node, a shadow deployment or various scripts and processes that haven’t been updated, which can reintroduce an Oracle Java runtime, exposing compliance and licensing risk, if not security risk also.

## The shape of the Java runtime security market

In terms of which other vendors operate in the Java runtime analytics and security market, there are more than a handful of usual suspects. [Contrast Security](https://www.contrastsecurity.com/solutionbrief/contrast-agent-deployment) is known for its [JVM agent](https://docs.contrastsecurity.com/en/agents.html) and in-app bytecode instrumentation. [Dynatrace](https://docs.dynatrace.com/docs/secure/application-security/vulnerability-analytics) offers Runtime Vulnerability Analytics as an extension of its core observability platform, which ships with OneAgent monitoring for Java vulnerable functions and JVM-level bytecode instrumentation agents.

Through its acquisitions by HP, Micro Focus, and now [OpenText](https://www.opentext.com/products/cybersecurity-cloud), [Fortify](https://www.microfocus.com/en-gb/media/data-sheet/security-fortify-software-security-center-ds-a4.pdf) remains known for its static and dynamic application testing services, including Fortify Application Defender, a runtime application self-protection (RASP) agent built to monitor Java workloads during execution. Part of Thales, [Imperva](https://www.imperva.com/learn/application-security/runtime-security/)’s runtime security for Java and .NET applications spans simple access control up to complex anomaly detection algorithms, though Imperva has reportedly put its standalone RASP product on an end-of-sale path. Then there’s [Datadog](https://www.datadoghq.com/product/apm/), with its Application Performance Monitoring (APM), built to power code-level distributed tracing from browser and mobile applications to backend services and databases.

> “Runtime context is absolutely critical for understanding the real risk in the production environment.”

A busy market for sure, so just how much of a problem are now-anachronistic static reports?

Head of security advocacy at Datadog, [Andrew Krug](https://www.linkedin.com/in/andrewkrug/), tells *The New Stack* that the downside of most point-in-time inventory scans is that they are “not always representative” of the runtime environment.

“Runtime context is absolutely critical for understanding the real risk in the production environment,” Krug says. “Even in the most mature software development lifecycle (SDLC) flows, tooling that generates static software bill of materials (SBOMs) may be bypassable [i.e. circumventable or subvertible] to get a feature deployed. Moreover, traditional vulnerability management flows outside of SDLC can bump versions outside of CI/CD process, accidentally compounding the problem and introducing added risk by bypassing known good guardrails like dependency cooldowns.”

> “Even in the most mature software development lifecycle (SDLC) flows, tooling that generates static software bill of materials (SBOMs) may be bypassable… to get a feature deployed.”

Krug further advises that Datadog now sees “an increasing rise” in automated drive-by attacks on known vulnerabilities, “particularly Java” in many cases.

“Attacks used to be added to scanners, either specifically or generically, and scans are indiscriminately against targets,” Krug clarifies. “LLMs make it cheaper to add support for new vulnerabilities. However, it also makes it easier for individual researchers/hackers to have their own custom rulesets.”

> “LLMs make it cheaper to add support for new vulnerabilities.”

He advises that this fact makes trends much harder to read than “oh, someone added support to CVE-2026-whatever in FFUF”, so today the goal of many attacks is unchanged.  Attackers are looking to move laterally, establish persistence, and often automations will look for credentials to leverage to do just that.

**NOTE:** ([Fuzz Faster U Fool](https://hackviser.com/tactics/tools/ffuf)) is an extremely fast web application fuzzer (written in the Go language), which is used by security testers to discover hidden files, directories and endpoints.

## Dead code; it’s really a ‘thing’

The above-noted list of competitors that work in Azul’s marketplace is (arguably) substantial evidence of the real commercial licensing and security risks that exist where Java code, redundant JVMs and chunks of unsubstantiated (or more likely just untracked) Java components have been left to roam free. Azul itself noted that there’s a real maintenance overhead here that needs to be addressed because “unused and dead code that still gets tuned, tested and carried through every migration”, usually because no one can assess it’s safe to remove.

The larger the Java estate, the larger the exposures get, obviously. But that also means that the less a point-in-time report can be trusted to catch these exposures before they become an incident, an audit finding or a breach.

Dedicated compliance officers will likely enjoy wider deployment of these tools, although that role itself may now reside within a DevSecOps or platform engineering team, or both.

Azul Intelligence Cloud AI Assistant works regardless of which JVMs are deployed, from which vendor, or how old or large the applications running on them are. JVM Inventory and Code Inventory retain component and code-use history over time, so the AI Assistant can reason over which code, JVMs and applications have actually run in production, now and in the past.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://cdn.thenewstack.io/media/2026/02/684dae45-cropped-e991646b-06_rpa_inline_01_bridgwater-1-1-300x234-1.jpg)

Adrian Bridgwater is a technology journalist with three decades of press experience. He has an extensive background in communications, starting in print media, newspapers and also television. Primarily working as an analysis writer dedicated to a software application development ‘beat’,...

Read more from Adrian Bridgwater](https://thenewstack.io/author/adrian-bridgwater/)