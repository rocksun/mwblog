Open source is under attack with a new wave of supply chain attacks.

It has been a bad, bad few weeks for open-source security.  It all started on March 19, 2026, when a severe supply chain attack on the [Aqua Security](https://www.aquasec.com/) [Trivy vulnerability scanner](https://trivy.dev/) occurred, as [hackers, TeamPCP, compromised the project’s continuous integration and delivery (CI/CD) pipeline](https://www.aquasec.com/blog/trivy-supply-chain-attack-what-you-need-to-know/) and GitHub repositories repeatedly. Once in,  the attackers trojanized Trivy binaries and actions to steal sensitive credentials from CI/CD pipelines.

This was not a good look for a security company.

That was bad. You want to know what’s worse? It was only the beginning of a wave of such attacks on other open-source projects. Since [Trivy](https://trivy.dev/) was assaulted, [TeamPCP compromised several dozen NPM JavaScript packages](https://www.aikido.dev/blog/teampcp-deploys-worm-npm-trivy-compromise) with a new three-stage attack called CanisterWorm. Then, the same group successfully used stolen credentials from the Trivy attack to wreak havoc on the popular Python proxy package LiteLLM. While TeamPCP hasn’t claimed credit for the attack, someone used the same methods to [break into the Agentic security company Checkmarx.](https://checkmarx.com/blog/checkmarx-security-update/)

TeamPCP, according to *Internation**al Cyber Digest*, [claims to have “obtained 300 GB of compressed credentials.”](https://x.com/IntCyberDigest/status/2036526495254876418) In case there was any doubt about how they managed their attack, they’re also quoted as saying, “TeamPCP is here to stay. Long live the supply chain.”

It’s not boasting if they can do it. Altogether, the group has compiled open-source projects that are downloaded more than 100 million times a month.

It also appears that TeamPCP is up to mischief for a few weeks before its current successful run of attacks. According to the cloud-security company [Upwind](https://www.upwind.io/), it all started when  “an autonomous AI bot called hackerbot-claw exploited a pull\_request\_target [misconfiguration in Trivy’s GitHub Actions workflows](https://www.upwind.io/feed/trivy-supply-chain-incident-github-actions-compromise-breakdown) to steal a Personal Access Token, ultimately achieving a full repository takeover.”

Aqua Security fixed that problem, but they didn’t do a good enough job. Credentials that survived the incomplete repair were used to compromise the company’s GitHub Aqua Bot service account.

The data company [DreamFactory](https://dreamfactory.nl/) CTO Kevin McGahey wrote in a blog post that [TeamPCP is conducting “a coordinated supply chain campaign](https://blog.dreamfactory.com/the-litellm-supply-chain-attack-a-complete-technical-breakdown-of-what-happened-who-is-affected-and-what-comes-next) that methodically escalated from security tooling to AI infrastructure… The progression is deliberate and strategic: Compromise security scanners first (tools that run with elevated permissions in CI/CD pipelines), harvest credentials, then use those credentials to poison downstream infrastructure.

By attacking Trivy, a security tool that many organizations trust implicitly and run with broad access, TeamPCP obtained the PyPI publishing token and GitHub personal access token needed to publish malicious LiteLLM releases.”

## How the attack unfolded

[Palo Alto Networks](https://www.paloaltonetworks.com/) analysts [described the Trivy attack run](https://www.paloaltonetworks.com/blog/cloud-security/trivy-supply-chain-attack/) and all subsequent assaults as part of a five-part attack chain.

### Phase 1: Credential Reuse and Repository Takeover

Armed with credentials from the initial breach, TeamPCP hijacked the Aqua Bot service account and began committing as trusted maintainers. They then pushed a malicious v0.69.4 tag to the Trivy repository. This kicked off an automated release process that propagated backdoored binaries to GitHub Releases, Docker Hub, GHCR, and Amazon ECR.

### Phase 2: GitHub Actions Tag Poisoning

The attackers force‑updated 75 of 76 version tags in aquasecurity/trivy-action so they now referenced malicious commits. Any GitHub Actions workflow pinned to a version tag, such as @v0.28.0, silently pulled in attacker‑controlled code without any visible change to the workflow definition. To avoid suspicion in Git history, the malicious commits copied the original author metadata and timestamps, and the same technique was used to poison seven setup-trivy tags.

### Phase 3: Three-Stage Credential Theft

The tainted actions ran a three‑stage data theft sequence:

* Collection: The malware read directly from GitHub Actions runner memory, sidestepping log masking, and captured SSH keys, cloud credentials (AWS, GCP, Azure), Kubernetes tokens, Docker registry logins, database passwords, TLS private keys, and cryptocurrency wallet data.
* Encryption: All captured information was encrypted using AES‑256‑CBC and then wrapped with RSA‑4096, defeating most network‑level inspection.
* Exfiltration: The encrypted payload was sent to a typosquatted domain (scan.aquasecurtiy[.]org); if that failed, the malware used the victim’s GitHub PAT to create a public repo named tpcp-docs and stored the data there, piggybacking on GitHub’s trusted infrastructure.

### Phase 4: Persistent Backdoor on Developer Machines

When a compromised Trivy binary was executed on a developer’s machine, it installed a persistent backdoor as a systemd service (sysmon.py). This service regularly contacted a canister on the Internet Computer (ICP) blockchain—about every 50 minutes—to fetch command‑and‑control instructions, using decentralized infrastructure that is difficult to disrupt.

### Phase 5: CanisterWorm — Self‑Spreading npm Supply Chain Attack

With the harvested credentials, TeamPCP launched CanisterWorm, compromising more than 47 npm packages across several scopes. Later iterations added token theft and automatic malicious publishing to the postinstall hook, so any developer workstation or CI pipeline that installed an affected package became an unintentional propagation node. In one burst, 28 packages were backdoored in under 60 seconds.

The end result? The Trivy open source supply chain was silently weaponized.

## GitHub shares the blame

Before you blame Trivy, though, other security professionals put the onus on this security breakdown on GitHub. In an e-mail interview, [Dan Lorenc](https://www.linkedin.com/in/danlorenc), CEO and cofounder of secure image company [Chainguard](https://www.chainguard.dev/), told The New Stack, the attack was “exploiting a weakness in the way their GitHub Actions were configured. They basically took untrusted inputs, in this case, branch names, and passed them into the scripts inside the actions without properly escaping them. The attackers were able to send a pull request with unsafe content in the branch name. This enabled the bad guys to exploit the action pipelines themselves. Once, the assailants were able to push  malicious commits to the repositories or steal credentials from CI Systems.”

Lorenc continues, “A lot of the defaults are bad, and they can be exploited in subtle ways. This affected both the initial attack on Trivy and the way malware propagated across everyone’s CI systems that used the Trivy GitHub Action. So there’s another wave of attacks happening now with all the credentials that were stolen from those Trivy users.”

In short, “this entire wave of attacks isn’t really new, but it’s definitely the biggest by far. It’s hitting multiple ecosystems, including new ones like GitHub Actions (think [Shai-Hulud](https://unit42.paloaltonetworks.com/npm-supply-chain-attack/) [the infamous npm malware attack] on steroids).

## Rotate credentials, pin actions

What can you do about it? Lorenc suggests, “Anyone who had the Trivy action in their pipeline or was running it themselves on their systems likely had credentials stolen and needs to rotate them.” These include cloud keys, GitHub tokens, SSH keys, Kubernetes tokens, Docker registry creds, database passwords, TLS keys, and any exposed wallets. You should also rebuild affected CI runners and images from clean, trusted baselines rather than trying to “clean” them in place.

To prevent this kind of attack from happening again, you should pin GitHub Actions to commit SHAs, not tags. That way, you’re locking an action to a specific commit hash instead of moving a version tag. You should also lock down your GitHub tokens and other runner tokens with explicit permissions. For example, no write access unless absolutely required.”

Beyond that, this is a painful reminder that even our security tools can be used against us. We must start treating security tools like any other dependency. E.g., track their exact versions, verify checksums, and do not auto‑track “latest” for scanners.

This is not over yet. You can expect more such attacks soon. Hey, no one ever said software development security was easy. We wish it weren’t so miserable, especially now that we cannot even trust our own security programs.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://cdn.thenewstack.io/media/2023/03/cee63948-cropped-8a0b5c52-steven-vaughan-nichols.jpg)

Steven J. Vaughan-Nichols, aka sjvn, has been writing about technology and the business of technology since CP/M-80 was the cutting-edge PC operating system, 300bps was a fast internet connection, WordStar was the state-of-the-art word processor, and we liked it.

Read more from Steven J. Vaughan-Nichols](https://thenewstack.io/author/sjvn/)