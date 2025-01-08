# How Supply-Chain Attackers Maximize Their Blast Radius
![Featued image for: How Supply-Chain Attackers Maximize Their Blast Radius](https://cdn.thenewstack.io/media/2025/01/4b6a195d-supplychainattackersmaximizeblastradius-1024x576.jpg)
Modern software development heavily relies on open source packages. Platforms like npm, PyPI and GitHub collectively host millions of packages and facilitate billions of downloads monthly.

While the interconnected, collaborative nature of open source software (OSS) enables innovation, it also [exposes the ecosystem to malicious activity](https://thenewstack.io/what-developers-can-grok-from-the-latest-pypi-package-attack/). Attackers are increasingly exploiting these trusted supply chains to propagate malware, including cryptominers, information stealers and backdoors [Sonatype](https://www.sonatype.com/?utm_content=inline+mention)‘s 2024 report highlighted a [156% increase in malicious packages](https://www.sonatype.com/state-of-the-software-supply-chain/introduction) compared to the previous year, signaling a growing and urgent threat to software supply chains.

## Minimal Barriers, Maximum Risk
The simplicity of publishing open source packages has inadvertently created an environment with low barriers for entry but substantial rewards for malicious actors of all levels. With minimal effort, adversaries generate and distribute an alarming volume of malicious packages using throwaway identities, complicating tracking and mitigation.

At the advanced end of the threat landscape, nation-state actors, particularly those [affiliated with the North Korean government](https://www.darkreading.com/application-security/japan-blames-north-korea-for-pypi-supply-chain-cyberattack), have progressively turned to npm and PyPI packages. They use these platforms as part of campaigns aimed at infiltrating organizations and stealing cryptocurrency.

These threats force package registries and security researchers into a reactive “whack-a-mole” scenario, identifying and removing these threats, often after extended periods of undetected activity.

## Expanding Attack Surface
Modern development’s reliance on intertwined dependency chains amplifies the potential impact of a single compromised package. While a project may have a handful of direct dependencies, transitive dependencies in npm regularly exceed 1,000 per package.

The explosion in use of AI-based code-generation tools compounds these risks. Code generation models “[hallucinate” almost 20% of generated packages](https://arxiv.org/abs/2406.10279v1), suggesting non-existent or even malicious libraries. As developers adopt large language model (LLM) tools to speed development, the potential for supply chain compromise grows.

## Key Categories of OSS Supply Chain Attacks
Open source package ecosystem attacks can be divided into two main categories: hijacking trusted packages and imitating trusted packages.

### Hijacked Packages
Attackers aiming to maximize their blast radius might endeavor to hijack a high-profile package, one used by many applications or developers. The effectiveness of these attacks relies on the project’s existing user base and reputation. Unlike disposable malicious packages, these incidents tend to be more complex, making them harder to detect and prevent.

However, since popular packages are naturally subject to greater scrutiny, many OSS supply chain attacks have been uncovered thanks to the vigilance of the community.

To execute a package hijacking attack, adversaries typically need to possess maintainer or owner rights to the target project. They gain access through account compromise or gradual reputation-building within the community.

#### Maintainer Takeover
Threat actors can compromise maintainer accounts in various ways — weak passwords, targeted phishing attacks, stealing session cookies or API tokens or registering an expired email domain. Attackers may also seize the opportunity to take control of abandoned projects.

Project owners can mitigate such attacks by strengthening authentication and security mechanisms for maintainers and contributors. Tools like [Sigstore](https://thenewstack.io/need-to-sign-your-code-and-havent-a-clue-sigstore-can-help/) enable maintainers to cryptographically sign artifacts and provide provenance attestations.

#### Malicious New Contributors
Instead of compromising an existing maintainer, sophisticated attackers might opt to infiltrate projects by patiently building trust and reputation over time — organically or otherwise — before requesting elevated privileges.

Organic trust-building involves [“low and slow” social engineering](https://thenewstack.io/the-xz-hack-reveals-a-looming-8-8-trillion-infrastructure-disaster-hidden-in-plain-sight/), which can span months or even years. Such activity will approximate normal patterns within open source development, making it hard to distinguish from benign contributions.

Some will attempt to skip ahead by using “[sock puppet”](https://en.wikipedia.org/wiki/Sock_puppet_account) accounts to bolster credibility, or manipulating metrics with bought stars and followers on GitHub. These tactics gamify the trust-building process, creating a false sense of legitimacy to support their case as a maintainer.

Once attackers gain project access, they need to trigger execution of their payload to propagate it to all downstream users. The most obvious method involves committing some malicious code, possibly across multiple files and stages to avoid detection by other contributors and users.

Another option is exploiting the CI/CD pipeline. For example, the recent [Ultralytics PyPI compromise](https://blog.pypi.org/posts/2024-12-11-ultralytics-attack-analysis/) hinged on GitHub Actions cache poisoning.

Teams should rigorously review all pull requests and monitor CI/CD processes. Tools like [Minder](https://thenewstack.io/stacklok-donates-minder-security-project-to-openssf/) and [Stacklok Insight](https://thenewstack.io/codegate-open-source-tool-secures-ai-coding-assistants/) can identify suspicious code additions, deprecated dependencies or unusual patterns.

### Imitating Packages
Most threat actors will take a simpler approach of creating counterfeit packages that mimic legitimate ones, rather than attempting to hijack the originals directly. Such attacks, including typosquatting and starjacking, rely on deceiving users into trusting and downloading their packages. With this approach, the attacker retains full control over all aspects of the package’s delivery, source code and appearance.

This method not only simplifies execution but also makes such attacks easier to detect. However, their reach is often limited — a deliberate choice by some attackers seeking to avoid widespread scrutiny.

#### Typosquatting
Typosquatting has long been a favored technique in malware and spam campaigns. Attackers register domain names with slight misspellings or substitutions to trick users into visiting malicious websites. For example, a fraudulent [Microsoft](https://news.microsoft.com/?utm_content=inline+mention) login page might use a domain like microsoft-auth.xyz/login.

The same strategy applies to packages; attackers will choose names nearly identical to legitimate packages, using slight mistypes, extra tokens or character substitutions. For example, they might use [eth-gasreportr](https://www.insight.stacklok.com/report/npm/eth-gasreportr) rather than [eth-gas-reporter](https://www.insight.stacklok.com/report/npm/eth-gas-reporter).

#### Starjacking
Starjacking often accompanies typosquatting. Since most package registries allow unverified user-declared repository links, attackers can hijack the popularity statistics for a high-reputation package. Displaying the star count and contributor list from the legitimate package on the malicious package lends it undue credibility.

![A "starjacked" package - the only difference is that the main title is misspelled "eth-gasreportr" rather than eth-gas-reporter](https://cdn.thenewstack.io/media/2025/01/5c8f6c64-eth-gasreportr-typosquat-1024x742.png)
A “starjacked” package uses typosquatting to present itself as a legitimate website.

![A legitimate repository](https://cdn.thenewstack.io/media/2025/01/b42a280a-eth-gas-reporter-legit-1024x744.png)
The legitimate repository for eth-gas-reporter

Teams should avoid relying solely on displayed popularity metrics for trust, as these are not reliable indicators of legitimacy. Verified package provenance can give assurance that the package code originates from the repository it claims a link to.

## Conclusion
These malicious strategies, from targeted maintainer takeovers to deceptive package imitations, illustrate the vulnerabilities inherent in the open source ecosystem.

While these methods are among the most common, they represent only a fraction of the ever-evolving threat landscape.

New attack vectors, such as leveraging AI-generated code or exploiting novel vulnerabilities in CI/CD pipelines, continue to emerge. Addressing these challenges requires ongoing vigilance, [innovation in security tools](https://thenewstack.io/stacklok-builds-on-sigstore-to-identify-safe-open-source-libraries/) and collective effort from the OSS community to [protect the software supply chain](https://thenewstack.io/who-should-be-responsible-for-software-security/).

[
YOUTUBE.COM/THENEWSTACK
Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.
](https://youtube.com/thenewstack?sub_confirmation=1)