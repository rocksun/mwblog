Bug bounty programs have been a cornerstone of cybersecurity for years, serving as conduits for hackers and security researchers to responsibly disclose vulnerabilities before malicious actors can exploit them.

And so it should come as little surprise that Anthropic has formally launched its own public bug bounty program, opening its security reporting pipeline to the wider research community after previously running tightly controlled safety-testing initiatives.

However, the launch comes exactly one month after [Anthropic unveiled Claude Mythos and Project Glasswing](https://thenewstack.io/anthropic-claude-mythos-cybersecurity/), a restricted-access cybersecurity initiative centered around a more advanced frontier model that the company claims can identify and chain together software vulnerabilities far more effectively than its current public systems.

Rather than releasing Mythos broadly, Anthropic instead limited access to a small group of security and infrastructure partners — including Amazon, Microsoft, Cisco, CrowdStrike, and the Linux Foundation — framing the project as an effort to strengthen defensive cybersecurity capabilities before more powerful offensive AI tooling becomes widespread.

Yet Anthropic’s decision to simultaneously expand public human-led vulnerability research also subtly undermines some of the broader hype surrounding Mythos itself – the company, after all, has gone to great lengths to highlight Mythos’s dangerous cybersecurity capabilities.

> The new bug bounty program is a tacit acknowledgment that conventional security research — carried out by external human researchers rather than frontier models alone — remains central to finding and fixing real-world vulnerabilities.

The new bug bounty program is a tacit acknowledgment that conventional security research — carried out by external human researchers rather than frontier models alone — remains central to finding and fixing real-world vulnerabilities.

In Anthropic’s case, parts of the security community have questioned the difficulty of verifying some of the company’s broader claims about Mythos’ vulnerability-discovery capabilities and real-world impact.

Still, if Mythos truly represents the future of AI-driven cybersecurity, Anthropic’s decision to simultaneously launch a very traditional human-powered bug bounty program introduces an obvious tension into that narrative.

## Crowdsourcing security for Claude

[Hosted on HackerOne](https://hackerone.com/anthropic/?type=team), the new bug bounty program allows external researchers to report vulnerabilities in Anthropic-developed software and systems, with rewards determined using the Common Vulnerability Scoring System ([CVSS](https://en.wikipedia.org/wiki/Common_Vulnerability_Scoring_System)), an industry-standard framework for ranking software security flaws by severity.

The move, in fact, marks an evolution of Anthropic’s earlier vulnerability disclosure efforts. In August 2024, the company [launched a more conventional](https://hackerone.com/anthropic-vdp/policy_versions?change=3737764&type=team) Vulnerability Disclosure Program (VDP), which primarily acted as a reporting and triage channel for security findings. That earlier VDP page now redirects researchers to the new bug bounty program, with Anthropic noting that future reports should be submitted through the updated system.

The new program spans a broad range of Anthropic-owned assets, including Claude.ai, the Anthropic API, Claude Code, official desktop and mobile clients, internal infrastructure, SDKs, and Anthropic-developed MCP integrations and Chrome extensions. Certain categories remain excluded, including vulnerabilities affecting third-party MCP servers, archived open source repositories, social engineering attacks, and low-severity informational findings.

Notably, Anthropic has also placed Claude Code within scope for critical vulnerabilities involving unauthorized command execution, invisible tool usage, and permission bypasses — precisely the kinds of risks that have become increasingly central to the rise of autonomous coding agents.

It’s also far from Anthropic’s first efforts to involve external researchers in probing the safety boundaries of its AI systems. In addition to its public VDP in 2024, [the company launched](https://www.anthropic.com/news/model-safety-bug-bounty) an invite-only “model safety” bounty program to uncover universal jailbreaks and methods to bypass Claude’s safeguards. Anthropic [later expanded those efforts](https://www.anthropic.com/news/testing-our-safety-defenses-with-a-new-bug-bounty-program) with a second HackerOne initiative designed to stress-test its Constitutional Classifiers against prompts related to chemical, biological, radiological, and nuclear (CBRN) misuse scenarios.

Those earlier programs focused more on probing the behavioral and safety boundaries of frontier AI systems themselves.

Announcing [the new program on X](https://x.com/AnthropicAI/status/2052466175540629965) on Thursday, Anthropic said it had been testing the initiative for some time ahead of its formal launch.

“We’ve run the program privately within the security research community, and their findings have strengthened our products,” the company writes. “Now anyone can report vulnerabilities and get rewarded.”

## The Mythos skepticism grows

In the wake of the launch, not everyone appears convinced by Anthropic’s broader Mythos narrative.

Some users on social media openly questioned the tension between Anthropic’s claims around advanced AI-driven vulnerability discovery and the simultaneous launch of a very traditional human-led bug bounty program. “*So, Mythos is a myth*,” one user [writes](https://x.com/glinsec_com/status/2052617943410753941), while another [asked](https://x.com/quantumaidev/status/2052466625044263213): “*I thought you had Mythos doing all these things*?”

While reactions from random online commenters should hardly be treated as authoritative security analysis, the remarks nonetheless tap into a broader undercurrent of skepticism that has built around Mythos.

## Benchmarking transparency under fire

Shortly after Mythos was unveiled to the world, [Dr. Heidy Khlaaf](https://www.linkedin.com/in/heidy-khlaaf/), chief AI scientist at the AI Now Institute, [publicly questioned](https://x.com/HeidyKhlaaf/status/2041591737563394442?s=20) several aspects of Anthropic’s Mythos rollout, particularly around benchmarking transparency and evaluation methodology.

Khlaaf argued that Anthropic had not disclosed sufficient comparisons against established static analysis and security tooling already widely used inside enterprise and critical infrastructure environments. She also pointed to the absence of detailed false-positive metrics, which many security researchers consider one of the most important indicators when assessing whether vulnerability discovery tools are genuinely useful in practice.

She further questioned how much of Mythos’ apparent success may still depend on significant amounts of human expert validation behind the scenes.

“This is not to say AI tools cannot augment security engineering,” Khlaaf [writes](https://x.com/HeidyKhlaaf/status/2041591751891177486?s=20). “It can, but the claims that attempt to render existing tooling and engineers obsolete are dishonest.”

[David Ottenheimer](https://www.flyingpenguin.com/about/), president of the security consultancy [FlyingPenguin](https://www.flyingpenguin.com/), raised similar concerns in a [separate analysis](https://www.flyingpenguin.com/the-boy-that-cried-mythos-verification-is-collapsing-trust-in-anthropic/), arguing that parts of Anthropic’s Mythos narrative blurred important distinctions between vulnerability discovery, exploitability, benchmarking, and real-world security impact.

Ottenheimer also criticized what he described as a closed verification loop surrounding Project Glasswing and Mythos, where Anthropic’s technical documents and launch materials largely pointed back to one another without substantial independent validation from outside partners.

> “The security story is ALL marketing and basically no evidence.”

“The security story is ALL marketing and basically no evidence,” Ottenheimer writes.

Ottenheimer also pointed to a [report from AISLE](https://aisle.com/blog/ai-cybersecurity-after-mythos-the-jagged-frontier), an AI security startup, which found that small, cheap, open-weights models could replicate much of Mythos’s flagship vulnerability analysis — including one with just 3.6 billion active parameters costing $0.11 per million tokens.

## Human researchers are still essential

On the flip side, there is evidence suggesting Mythos’ capabilities may extend beyond marketing hype. The UK AI Security Institute (ASI) [released an evaluation](https://thenewstack.io/claude-mythos-preview-simulation/) of Claude Mythos Preview, showing that the model could autonomously complete multi-stage cyberattack simulations and solve expert-level capture-the-flag (CTF) challenges at rates that previous frontier models struggled to approach.

In one controlled evaluation, ASI said Mythos became the first model to successfully complete a 32-step simulated corporate network takeover from reconnaissance through exploitation and lateral movement. Across 10 attempts, the model completed an average of 22 of the 32 required steps, substantially outperforming Anthropic’s previous flagship systems.

At the same time, ASI also cautioned against overinterpreting the results, noting that the tests occurred inside controlled environments without many of the defensive measures, active monitoring systems, and real-world constraints found in hardened enterprise networks.

“We cannot say for sure whether Mythos Preview would be able to attack well-defended systems,” the institute writes.

However one chooses to interpret Mythos and Project Glasswing, Anthropic’s new HackerOne rollout perhaps reveals something more grounded beneath the mythology: even in an era of increasingly capable AI cyber systems, the company still sees value in ordinary human researchers poking holes in its products the good old-fashioned way.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://thenewstack.io/wp-content/uploads/2026/02/bd93adde-cropped-9c2ecfc5-a-600x600.jpg)

Paul is an experienced technology journalist covering some of the biggest stories from Europe and beyond, most recently at TechCrunch where he covered startups, enterprise, Big Tech, infrastructure, open source, AI, regulation, and more. Based in London, these days Paul...

Read more from Paul Sawers](https://thenewstack.io/author/paul-sawers/)