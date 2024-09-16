# Protect Your Codebase: The Importance of Provenance
![Featued image for: Protect Your Codebase: The Importance of Provenance](https://cdn.thenewstack.io/media/2023/04/c9a67e42-secrets-management-lockbox-2-1024x576.jpg)
Anyone who has watched a crime drama has heard about the chain of custody for evidence. The prosecution must be able to show who handled evidence and how they handled it from when it was collected to when it was presented at trial. The judge can reject the evidence if there’s a broken link in the chain. This is a vital protection against malicious prosecution.

While it doesn’t make for compelling television, software has the same concept: provenance.

## The Importance of Provenance
Modern software isn’t just the code you write; it includes a [collection of dependencies](https://thenewstack.io/a-guide-to-software-dependencies/) that you bring in from vendors and open source projects. This supply chain has a direct impact on the security of your software. Just like a physical chain is only as strong as the weakest link, your software is only as secure as the most insecure dependency. The applications affected by [Log4Shell](https://thenewstack.io/log4shell-lives/) weren’t vulnerable because the application code was insecure; they were vulnerable because the [log4j library](https://thenewstack.io/log4j-why-organizations-are-failing-to-remediate-this-risk/) they used was vulnerable.

Of course, the Log4Shell vulnerability was accidental, as most are. However, some vulnerabilities are inserted intentionally. Someone may insert obfuscated malicious code to the source repo (as with the [xz backdoor](https://thenewstack.io/the-xz-hack-reveals-a-looming-8-8-trillion-infrastructure-disaster-hidden-in-plain-sight/) earlier this year), or they may add a dependency designed to attack certain users (as with the anti-Russian [peacenotwar](https://en.wikipedia.org/wiki/Peacenotwar) dependency added to node-ipc in March 2022), or they may compromise a software repository or update mechanism (as with [NotPetya](https://www.wired.com/story/notpetya-cyberattack-ukraine-russia-code-crashed-the-world/) in 2017).

When you know who developed the software and how it was tested, built and shipped — its provenance — you know how much you can trust it.

## How Provenance Can Be Attacked
Because provenance is essential to securing the software supply chain, manipulating provenance is integral to a successful supply chain attack.

Some attacks happen before or as the provenance is generated. For example, an attacker may falsely assert that they reviewed code when they did not, or deliberately ignore issues that came up in a review. An attacker may also compromise another account and use that account to impersonate a trusted person. The impostor can commit code, perform a review or trigger a build in a way that wouldn’t raise alarms among the rest of the team. An attacker who has compromised the build system could cause it to generate false records in the build’s software bill of materials (SBOM).

Other attacks happen after the fact. An attacker accessing a git repository can edit the commits to change the author or timestamp. Or they could even alter an old commit to insert malicious code well in the past, which few would think to notice. Attackers with server access can alter file contents and timestamps to cover their tracks.

In both cases, attackers don’t necessarily need to take direct action. Using social engineering approaches, they can trick others into making these changes on their behalf.

## Ensuring Trustworthy Provenance
When you know that provenance is a vector for a software supply chain attack, you can take action to protect it. The first step is to collect the provenance data for your dependencies, where it exists; projects that meet [SLSA level 1](https://thenewstack.io/securing-the-software-supply-chain-with-slsa/) or higher produce provenance data you can inspect and verify.

Ensure that trusted identities generate provenance. If you can prove that provenance data came from a system you own and secured or from a known good actor, it’s easier to trust. Cryptographic signing of provenance records provides assurance that the record was produced by a verifiable entity — either a person or a system with the appropriate cryptographic key.

Store provenance data in a write-once repository. This allows you to verify later if any provenance data was modified. Modification, whether malicious or accidental, is a warning sign that your dependencies have been tampered with somehow.

It’s also important to protect the provenance you produce for yourself and any downstream users. Implement strict access and authentication controls to ensure only authorized users can modify provenance records. Use multifactor authentication for any access to systems that produce provenance data, which reduces the risk of unauthorized access. Log access to a separate write-once logging system so that you can audit who accessed what systems and when.

## Toward a More Secure Supply Chain
There’s no one magic solution to [supply chain security](https://thenewstack.io/fortifying-the-software-supply-chain/), but every step you take is in the right direction. When you know what’s in your dependency graph, how it was produced and what known vulnerabilities it includes, you’ve made your supply chain more secure.

The more secure your supply chain, the more secure your users are.

[
YOUTUBE.COM/THENEWSTACK
Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.
](https://youtube.com/thenewstack?sub_confirmation=1)