Modern cloud native attacks don’t always rely on a single breakthrough exploit. Instead, threat actors chain together small assumptions, overlooked behaviors, and trusted components in ways defenders least expect. The recent React2Shell vulnerability is a perfect example of this, and the EtherRAT malware shows just how creative adversaries are.

For teams that rely on [React](https://thenewstack.io/why-reacts-boring-maturity-is-actually-its-main-strength/), the [React2Shell vulnerability](https://react2shell.com/) was a wake-up call. It doesn’t just affect React as a framework; it breaks assumptions many teams rely on in production. In December, it showed us how quickly attackers can use something subtle like [server-side rendering](https://thenewstack.io/is-server-side-rendering-reacts-holy-grail/) (SSR) behaviors for server-side code execution and how difficult it is to spot once it’s live.

If you run React or Next.js workloads in production, here’s what [CVE-2025-55182](https://nvd.nist.gov/vuln/detail/CVE-2025-55182) and [CVE-2025-66478](https://nvd.nist.gov/vuln/detail/CVE-2025-66478) actually break, what you should check immediately, and how to identify attackers hiding behind legitimate infrastructure.

## **What React2Shell breaks**

If you’re unfamiliar, [React2Shell](https://www.sysdig.com/blog/detecting-react2shell) is not just another vulnerability you can one-click patch away — the flaw is within the framework itself. React2Shell is a class of vulnerabilities that arise when React applications improperly handle user-controlled input during SSR.

Exploitation allows server-side code execution, and the attacks began only hours after the vulnerability was published. Mitigation requires coordinated updates across React server components (RSC), [Next.js](https://thenewstack.io/next-js-deployment-spec-simplifies-frontend-hosting/), and related [frameworks](https://thenewstack.io/javascript-framework-reality-check-whats-actually-working/), in addition to an evaluation of application data flows.

First, once React components render on the server, they no longer execute in a browser sandbox. Instead, they run inside the backend runtime. React is often treated as frontend code and therefore, it’s assumed the server is safe. An attacker can exploit this assumption and inject JavaScript that then runs on the server, not on the browser. At this point, the code runs with the same permissions as the application itself, potentially giving attackers access to cloud credentials, internal APIs, filesystems, and more.

Second, client-side sanitization is not the same when rendering moves to server-side. Client-side input validation cannot be relied on to protect server-rendered execution paths. Patterns that are safe in the browser can become risky when evaluated during SSR. Inputs never intended to be executable can be evaluated as code when handled incorrectly by server-rendered components.

Finally, server-rendered components are usually assumed to be safe because they originate from application logic rather than user input. React2Shell arises from implicit framework behavior and has little to do with obviously unsafe code. Risk increases in large codebases where SSR patterns are abstracted, reused, and left unchecked.

Attackers exploit assumptions because, in this case, they can shift execution from the browser to the server. Once that boundary is crossed, the blast radius expands dramatically. Server-side execution enables credential access, lateral movement, and follow-on payload delivery. Detection requires understanding what the application is doing at runtime and how that behavior can be abused.

## **What you need to check**

If you have React or Next.js workloads running in production, here’s your checklist:

**Inventory your environment**

* Identify all services using RSCs, Next.js server components, or SSR.
* Don’t forget to check the admin panels and dashboards of all internal tools.
* Ensure framework and package versions are updated against advisory guidance.

**Audit data flows**

* Is user-controlled input passed into server-rendered components?
* Are there dynamic rendering paths that evaluate data structures or serialized content?
* Has data from app logic been reviewed, or is it assumed safe?

**Review permissions**

* Does this service need outbound internet access?
* Are credentials and permissions at the minimum requirements?
* Can containers write to disk or spawn child processes?

## **What happens after exploitation**

React2Shell was being actively exploited by nation-state threat actors within hours of public disclosure. In one particular campaign investigated by the Sysdig Threat Research Team (TRT), the damage went far beyond smash-and-grab exploitation and financial motivation. A custom remote access trojan (RAT) dubbed [EtherRAT](https://www.sysdig.com/blog/etherrat-dprk-uses-novel-ethereum-implant-in-react2shell-attacks) was deployed in real-world React2Shell attacks.

Instead of using traditional command-and-control (C2) infrastructure, EtherRAT uses something unconventional but resilient: The Ethereum blockchain. Commands are encoded into blockchain transactions and infected systems monitor the chain for instructions. [EtherRAT payloads](https://www.sysdig.com/blog/etherrat-dissected-how-a-react2shell-implant-delivers-5-payloads-through-blockchain-c2) are delivered in stages, allowing the malware to pull down additional capabilities as needed.

This approach offers several advantages for attackers:

* **Resilience:** Public blockchains are highly available and difficult to disrupt.
* **Stealth:** Blockchain traffic can appear legitimate and is increasingly common in enterprise environments, making it difficult to distinguish.
* **Attribution challenges:** There’s no central server to seize or sinkhole.

This is not commodity malware opportunistically scanning the internet. It’s deliberately crafted and designed to blend into modern operational noise. The takeaway here is: You won’t always see “malware-like” behavior from vulnerability exploitation. EtherRAT indicates subtle runtime deviations in systems that otherwise look healthy, an issue easily overlooked.

## **How to find hidden threats**

Detecting React2Shell abuse or other hidden threats requires observing what workloads are doing at runtime. You don’t need to know about specific threats to detect threats like these. You just need to know how your environment and applications normally behave.

When identified, the following behaviors should be investigated when they’re unexpected or abnormal:

**Process-level**

* Web server or [js](http://node.js) processes spawning shells
* Unexpected child processes
* Executions at runtime that don’t align with normal app startup behavior

**Network**

* Outbound connections to unfamiliar external endpoints.
* Long-lived outbound connections with no relation to the application function.
* Blockchain-related traffic coming from web services that have no business requirement.

**File-system**

* Writes to temporary directories from web-facing processes.
* Creation or execution of new binaries at runtime.

## **What comes next**

* Several broader trends emerge from these recent discoveries:
* **The blurring of client and server boundaries.** When JavaScript runs everywhere, blind assumptions become far more costly. Server-side JavaScript is server code.
* **The weaponization of legitimate infrastructure.** Blockchains, CI/CD systems, and cloud metadata services are all fair game.
* **The limits of static security controls.** You can’t scan your way out of logic flaws that only manifest during execution.

So, what does “operating safely” look like in light of React2Shell and EtherRAT? Production behavior is a new security perimeter. Attackers are already operating comfortably inside it, and with clarity, defenders will catch up.

There’s no blame or need to slow innovation. Treat SSR code paths with the same scrutiny as backend logic and use runtime detections based on normal and irregular behaviors, not just known threats.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://thenewstack.io/wp-content/uploads/2025/08/dfbfb486-i5jnccyk-nxw7aqbydo31zeacz696mlu70ufdwdl9fo-scaled-600x600.jpeg)

Crystal Morin is a senior cybersecurity strategist at Sysdig. She translates complex security concepts and cutting-edge research into clear, actionable guidance for leaders and practitioners alike, helping organizations defend against modern threats. Previously, Crystal served as a linguist and intelligence...

Read more from Crystal Morin](https://thenewstack.io/author/crystal-morin/)