All those security fears about the OpenClaw AI agent and its social network, [Moltbook](https://thenewstack.io/moltbook-the-singularity-or-hype/), are already proving true, according to security researchers who have been cataloguing and reporting vulnerabilities.

OpenClaw, the hot new personal AI Agent, may run on your local machine. Still, by default, it has full system access, can read files, execute commands, manage credentials, and work with external services via messaging platforms such as Discord, Slack, and Telegram. For the security-conscious, that alone is deeply troubling.

But now it’s become a live-fire security exercise for the entire “personal AI agent” concept. Researchers are cataloging concrete vulnerabilities, ranging from remote code-execution bugs to a wide‑open social‑graph database and a malware‑stuffed plug‑in ecosystem, at a rapid rate.

We knew from the start that OpenClaw, then known as Clawdbot, shipped with a huge attack surface, powerful local privileges, a network‑reachable control interface, and weak or missing authentication in its [Model Context Protocol (MCP)](https://thenewstack.io/model-context-protocol-a-primer-for-the-developers/?mailpoet_page=subscriptions) plumbing. In practice, that meant any process on a user’s machine could reach the agent’s steering wheel and drive it like a remote‑controlled car. 

For example, a technical deep‑dive from the security company [Guardz](https://guardz.com/) describes default deployments in which the Clawdbot gateway is bound to 0.0.0.0 on port 18789 and [exposes the full admin API](https://guardz.com/blog/when-ai-agents-go-wrong-clawdbots-security-failures-active-campaigns-and-defense-playbook/), with hundreds or thousands of such instances indexed in Shodan under the “Clawdbot Control” signature.

They also pointed out that MCP was shipping “without security,” making it easy for attackers and infostealer operators to target Clawdbot’s configuration directories and harvest plaintext credentials and chat histories.

MCP grants direct access to tools, credentials, and action routines. Thus, exposed endpoints let attackers read configuration files, pull stored API keys and OAuth tokens, browse private conversation logs, and even issue commands to the agent as if they were the owner. 

But, wait! There’s more! A separate high‑severity flaw, now tracked as [CVE‑2026‑25253](https://nvd.nist.gov/vuln/detail/CVE-2026-25253), hit OpenClaw. This bug allowed attackers to craft a malicious link that, when opened in a browser where a user had previously authenticated to the OpenClaw Control UI, exfiltrated tokens and handed over “operator‑level” access to the gateway API.

> He “was able to find a one-click account takeover to remote code execution (RCE) in approximately 1 hour and 40 minutes.”

As [Henrique Branquinho](https://www.linkedin.com/in/henrique-branquinho-5495a7123/), an AI Engineer at [Ethiack](https://ethiack.com/), an ethical hacking security startup,  writes,  he “was able to find a [one-click account takeover to remote code execution (RCE)](https://ethiack.com/news/blog/one-click-rce-moltbot) in approximately 1 hour and 40 minutes.

“A victim would simply need to visit an attacker-controlled website that leaks the authentication token from the Gateway Control UI, which is enabled by default, via a WebSocket channel. Then an arbitrary command will run, even if the victim is hosting locally.” Yow!

He warns that because the victim’s browser initiates the outbound WebSocket connection, the exploit works even when the gateway is configured to listen only on the loopback interface, effectively bypassing the usual “localhost is safe” assumption. With stolen tokens, an attacker can change the configuration, execute arbitrary code on the host, and direct the agent to act against any connected service or dataset. 

As for [Moltbook](https://www.moltbook.com/), the Reddit‑like social network built for OpenClaw agents, it has already suffered a critical backend misconfiguration that exposed its primary database. Researchers at the cloud security company [Wiz](https://www.wiz.io/) say a single key embedded in the site’s code was enough to unlock full read access to Moltbook’s internal data store. That doesn’t give me a warm fuzzy feeling. 

This flaw exposed tens of thousands of email addresses, and, according to [Gal Nagli](https://www.linkedin.com/in/galnagli/), the Wiz’s Head of Threat Exposure, about 1.5 million API keys and private messages between agents, while also allowing attackers to impersonate any bot on the platform. With valid authentication tokens in hand, a malicious actor could post, edit, or delete content on behalf of agent identities, potentially poisoning downstream models or launching large‑scale misinformation and spam campaigns. The possibilities for mischief are endless. 

Adding insult to injury, Moltbook relies on OpenClaw. Most Moltbook accounts are OpenClaw agents scripted by their owners to role-play, collaborate, or experiment with autonomous agent‑to‑agent interaction. Thus, Moltbook is also vulnerable to OpenClaw’s security woes. 

Security giant [Palo Alto Networks](https://www.paloaltonetworks.com/) warns that [OpenClaw’s ability to “remember” weeks of interactions means that a hidden instruction](https://www.paloaltonetworks.com/blog/network-security/why-moltbot-may-signal-ai-crisis/) in a website, PDF, or Moltbook post can remain dormant until a future task triggers the agent to execute it. In other words, “With persistent memory, attacks are no longer just point-in-time exploits. They become stateful, delayed-execution attacks.”

Still, as [Jamieson O’Reilly](https://www.linkedin.com/in/theonejvo/), founder of the security company [Dvuln](https://dvuln.com/), observes on LinkedIn, even though ” hundreds of people [have] set up their [Clawdbot control servers exposed to the public](https://www.linkedin.com/pulse/hacking-clawdbot-eating-lobster-souls-jamieson-o-reilly-whhlc/) …  this isn’t the end of the world. It’s not even a particularly sophisticated attack – it’s a misconfiguration/bug that any security review should have caught.” Ah, but they didn’t, did they? Oh, and he found the agent itself couldn’t help users secure it. Ironic, eh?  

Let’s say the most obvious holes are patched, so what? The Moltbot/OpenClaw ecosystem has already become an attractive distribution channel for commodity malware. OpenClaw “skills,” plug‑ins that extend the assistant’s capabilities, are already being abused by attackers. There, they use typical tricks, such as publishing typosquatted or fake packages that masquerade as crypto trading tools, financial utilities, or social media helpers. 

According to [OpenSourceMalware](https://opensourcemalware.com/), a community security site, OpenClaw now has [386 malware-infected skills.](https://opensourcemalware.com/blog/clawdbot-skills-ganked-your-crypto) That’s out of over [3,016 known OpenClaw skills](https://blog.virustotal.com/2026/02/from-automation-to-infection-how.html). I don’t like those odds.

I think O’Reilly sums it up well in a subsequent post, “As recently as 6 months ago I was still skeptical as to the utility & threat of AI when it comes to attack capability.” He’s changed his mind. “If your job has anything to do with the responsibility of data/privacy/security in your organisation, please do not keep telling yourself ‘maybe one day, but not today’ like I did. Invest [in AI defenses] now.” If you don’t, you’ll regret it. 

In the meantime, it may be wise to steer well clear of Moltbot and OpenClaw. The lack of meaningful security may pinch unwary developers and users. 

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://cdn.thenewstack.io/media/2023/03/cee63948-cropped-8a0b5c52-steven-vaughan-nichols.jpg)

Steven J. Vaughan-Nichols, aka sjvn, has been writing about technology and the business of technology since CP/M-80 was the cutting-edge PC operating system, 300bps was a fast internet connection, WordStar was the state-of-the-art word processor, and we liked it.

Read more from Steven J. Vaughan-Nichols](https://thenewstack.io/author/sjvn/)