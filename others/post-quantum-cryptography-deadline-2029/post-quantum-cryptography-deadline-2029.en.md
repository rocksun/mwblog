The inevitable path to access to [quantum computing](https://thenewstack.io/quantum-computing-use-cases/) brings an equal and opposite responsibility to address post-quantum cryptography.

Government directives from nations including the [United States](https://www.whitehouse.gov/presidential-actions/2026/06/securing-the-nation-against-advanced-cryptographic-attacks/) and [France](https://www.reuters.com/legal/litigation/france-stop-certifying-products-without-quantum-safe-encryption-2026-06-16/) have previously set an end-of-decade timeline, stipulating that public sector bodies and “critical operators” should procure and deploy exclusively [quantum-safe technologies](https://thenewstack.io/nist-secures-encryption-for-a-time-after-classical-computing/) by 2030.

That timeline has now changed.

Technology vendors, including [Microsoft](https://www.microsoft.com/en-us/security/blog/2026/06/30/microsoft-advances-quantum-safe-security-as-the-risk-timeline-shifts/), [Google](https://blog.google/innovation-and-ai/technology/safety-security/cryptography-migration-timeline/#:~:text=Mar%2025%2C%202026,to%20encryption%20and%20digital%20signatures.) and [Cloudflare](https://blog.cloudflare.com/post-quantum-roadmap/), have publicly stated that they will bring their quantum-safe deadline date forward to 2029.

> “We believe cryptographically relevant quantum computers could arrive sooner than previously expected, and the work required to prepare is significant so organizations need to start now.”

## A new risk horizon

According to [Mark Russinovich](https://www.linkedin.com/in/markrussinovich/), Microsoft Azure chief technology officer, advances in quantum research and development have now “shifted the risk horizon” for everyone.

“We believe cryptographically relevant quantum computers could arrive sooner than previously expected – and the work required to prepare is significant so organizations need to start now,” writes Russinovich in a recent blog post.

Russinovich noted that there has been growing recognition that the transition to quantum-safe cryptography is a “multi-year engineering effort” that benefits from early planning and action, so delaying work increases both cost and risk.

The Microsoft Quantum Safe Program (QSP) timeline and the goal of transitioning products and services to PQC by 2029 mean Redmond is also incorporating PQC requirements into its [Secure Future Initiative](https://www.microsoft.com/en-us/trust-center/security/secure-future-initiative) (SFI).

“This brings quantum-safe readiness into the same disciplined engineering framework we use for other critical security outcomes: clear ownership, measurable milestones, and transparent progress. Embedding these capabilities into our platforms empowers customers to move sooner and more confidently,” added Russinovich.

> “Cryptographically relevant quantum computers don’t exist yet, but many labs across the world are pursuing different approaches to building one.” – Bas Westerbaan, Cloudflare.

## What changes with post-quantum cryptography?

PQC is only possible on a cryptographically relevant quantum computer, [which doesn’t yet exist](https://quantumsequrity.com/blog/pqc-state-2026#:~:text=As%20of%20early%202026%2C%20the,quantum%22%20(NISQ)%20devices.). The closest we have in 2026 are “noisy intermediate-scale quantum” (NISQ) devices that run the [IBM Heron](https://www.ibm.com/quantum/hardware#processors) or  [Google Willow](https://blog.google/innovation-and-ai/technology/research/google-willow-quantum-chip/) chips to process approximately 1,000 to 1,500 physical qubits.

Underlining the looming threat, Cloudflare post-quantum specialist [Bas Westerbaan](https://www.linkedin.com/in/baswesterbaan/) has called Q-Day the day when sufficiently capable quantum computers can break essential cryptography used to protect data and access across systems today.

“Cryptographically relevant quantum computers don’t exist yet, but many labs across the world are pursuing different approaches to building one. Google’s motivation behind its recent announcement to also [pursue neutral atoms](https://blog.google/innovation-and-ai/technology/research/neutral-atom-quantum-computers/) alongside superconducting quantum computers becomes clear now,” stated Westerbaan.

Today’s public-key cryptography standards, such as RSA and ECC (Elliptic Curve Cryptography), are built on the difficulty of factoring large integers or computing discrete logarithms. These are defense systems that a quantum computer could quickly undermine with [Shor’s algorithm](https://en.wikipedia.org/wiki/Shor%27s_algorithm), which uses quantum superposition and interference to compute the period of a related function.

A cryptographically relevant quantum computer archives post-quantum cryptography using alternative mathematical problems over large integers, including lattice-based or hash-based structures, both of which are said to remain computationally hard even against quantum threats.

According to Google’s [Heather Adkins](https://www.linkedin.com/in/argvee/), VP for security engineering, and the company’s head of cryptography, [Sophie Schmieg](https://www.linkedin.com/in/sophie-schmieg-14367499/), work has already started. “As an example of our ongoing PQC commitments, Android 17 is integrating PQC digital signature protection using ML-DSA in alignment with the National Institute of Standards and Technology (NIST),” wrote the pair on Google’s innovation blog.

> “Most organizations have no clear picture of where cryptography exists across their applications, infrastructure, legacy systems and data flows,” Simon Pamplin, Certes.

## The threat of harvest now, decrypt later

[Simon Pamplin](https://www.linkedin.com/in/simonpamplin/), CTO at quantum-safe data protection company [Certes](https://certes.ai/), tells *The New Stack* that the “direction of travel” from governments and the world’s largest technology platforms is now unambiguous, and the pace is accelerating.

“What is worth examining is why,” Pamplin says. “The standard explanation points to advances in quantum hardware. That is part of it. But the more immediate driver is the threat of ‘[harvest now, decrypt later](https://www.hashicorp.com/en/blog/harvest-now-decrypt-later-why-today-s-encrypted-data-isn-t-safe-forever)’ activities. Adversaries, including state-level actors with long time horizons, are already intercepting and stockpiling encrypted data today. The cryptographic foundations protecting that data do not need to be broken immediately. They need to be broken eventually, and eventually is getting closer.”

Pamplin is fatalistic about this whole discussion and suggests that whether the deadline is 2027, 2029, or 2030 is, in some respects, beside the point. He reminds us that this is because data being harvested today does not wait for compliance timelines.

“Most organizations have no clear picture of where cryptography exists across their applications, infrastructure, legacy systems and data flows,” underlines Pamplin. “Investing in newer versions of the same infrastructure controls deployed for years will not resolve the underlying exposure. Data does not stay within environments an organization controls. It moves across third-party platforms, supplier networks and legacy infrastructure, and that is where protection needs to be applied.”

He says that the organizations creating and deploying genuine resilience are those applying data-centric, quantum-safe protection directly to the data itself, ensuring it remains unreadable and sovereign regardless of which system it passes through or when an adversary attempts to use it.

## Don’t wait until 2026; the time to act is now

Three years from now isn’t long, so 2029 will feel close to the new big (bad) thing for many organizations. Microsoft’s advice is to consider this change today and define ownership, scope, and milestones for a multi-year cryptography transition.

For systems architects and software engineers with any degree of insight into roadmaps, that means designing for change and building crypto-agility into new software and data products so future standards shifts are updates, not emergency situations.

Microsoft’s Russinovich urges companies to begin with an inventory and create and maintain “a living cryptographic inventory” to identify, prioritize, and ultimately modernize application dependencies. Quantum is coming, and it will inevitably intersect with AI; what comes next is something of an unknown.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://cdn.thenewstack.io/media/2026/02/684dae45-cropped-e991646b-06_rpa_inline_01_bridgwater-1-1-300x234-1.jpg)

Adrian Bridgwater is a technology journalist with three decades of press experience. He has an extensive background in communications, starting in print media, newspapers and also television. Primarily working as an analysis writer dedicated to a software application development ‘beat’,...

Read more from Adrian Bridgwater](https://thenewstack.io/author/adrian-bridgwater/)