Developer-focused cybersecurity platform [Aikido Security](https://www.aikido.dev/) has announced that it has acquired [Root](https://www.root.io/), a company that patches known vulnerabilities directly into the open source package version a team is already running, instead of forcing them to upgrade to a newer release.

The $70 million deal folds Root’s patching technology into a new product dubbed Aikido Libraries. It also comes with a commitment to backport fixes for critical, actively exploited vulnerabilities to the open source community for free, across every ecosystem the [company supports](https://www.npmjs.com/package/@aikidosec/safe-chain), such as [npm](https://www.aikido.dev/protect/safe-chain), PyPI, and Maven.

Founded in 2022, Aikido offers a single platform covering code scanning, cloud security, supply chain malware detection, and [AI-powered penetration testing](https://thenewstack.io/aikido-self-securing-software/). The Belgian company hit unicorn status back in January, raising [$60 million at a $1 billion valuation](https://www.aikido.dev/blog/aikido-funding-series-b), and now it’s looking to its fourth [acquisition](https://www.aikido.dev/blog/trag-is-now-part-of-aikido-secure-code-at-ai-speed) in [just over a year](https://www.aikido.dev/blog/allseek-and-haicker-are-joining-aikido) to close the gap between finding and fixing vulnerabilities.

Root, for its part, started out as Slim.AI, founded in 2021 and built on the open source DockerSlim project. The company [raised a $31 million Series A in 2022](https://www.insightpartners.com/ideas/slim-ai-closes-31-million-series-a-to-automate-best-practices-in-software-supply-chain-security-for-cloud-native-applications/), before rebranding to Root and pivoting from container optimization to automated vulnerability remediation.

## A fix for urgent flaws

Aikido’s free backporting commitment applies specifically to vulnerabilities on [CISA](https://www.cisa.gov/)‘s Known Exploited Vulnerabilities ([KEV](https://www.cisa.gov/known-exploited-vulnerabilities-catalog)) catalog — the relatively short list of flaws confirmed to have been exploited in the wild. It’s a small slice of all disclosed vulnerabilities, but the ones most likely to cause real damage.

It’s also the kind of commitment that could disappear once an acquisition’s costs need justifying. [Madeline Lawrence](https://www.linkedin.com/in/madelinelawren/), co-founder and chief growth officer at Aikido Security, tells *The New Stack* tells that won’t happen here, since CISA, not Aikido, decides what makes the list. The free fixes sit next to Aikido’s existing paid product, which the company is betting on a separate trend to grow: companies are under mounting compliance pressure to clear Common Vulnerabilities and Exposures (CVEs) generally, regardless of whether any given flaw has actually been weaponized yet.

“This sits apart from our paid capability, which covers the long tail of CVEs that regulators now require companies to remediate, not just the actively exploited ones, and demand there is exploding,” Lawrence says. “Both come out of the same factory. There’s no separate budget line for the free fixes to cut, because the work that produces them is the same work our paying customers rely on.”

> “The industry is still stuck on triage, taking a giant list of CVEs and arguing over which ones to fix first.”

Root CEO [Ian Riopel](https://www.linkedin.com/in/ianriopel/) frames the choice the industry has been avoiding as one between locking fixes behind a vendor’s own ecosystem, or putting them back into the hands of the projects that need them.

“The industry is still stuck on triage, taking a giant list of CVEs and arguing over which ones to fix first. Or worse, telling teams to throw out their images and start over with someone else’s,” Riopel says in a statement. “We built Root to skip the argument and just fix the problem in place. This is a choice between walled gardens and real support for open source. We chose open source.”

> “This is a choice between walled gardens and real support for open source. We chose open source.”

## Security scramble

The acquisition lands at a turbulent time for AI and cybersecurity more broadly. On Friday, the [Linux Foundation launched Akrites](https://thenewstack.io/akrites-open-source-vulnerability-coordination/), a coordinated vulnerability disclosure body backed by Anthropic, Google, Microsoft, and roughly 20 organizations, formed largely in response to how quickly AI tools can now surface flaws in open source code. This, in turn, followed [a tense few weeks](https://thenewstack.io/anthropic-fable-mess-explained/) for Anthropic specifically: the US government [suspended access](https://thenewstack.io/us-gov-orders-anthropic-to-pull-fable-5-and-mythos-5-three-days-after-launch/) to its [Fable 5 and Mythos 5 models](https://thenewstack.io/anthropic-claude-mythos-fable-5/) in June after researchers said they’d found ways to use them to assist cyberattacks, before restoring access for critical infrastructure organizations late in the month.

Lawrence says the timing is coincidental. The Root deal, she says, has been a long time coming, building on an existing partnership the two companies [forged in mid-2025](https://www.aikido.dev/blog/aikido-x-root-io-harden-your-containers-without-the-headaches), bringing Root’s hardened container images into Aikido’s existing Autofix product.

Still, Lawrence doesn’t dismiss the broader pressure AI is putting on both sides of the fight.

“The industry got very good at finding vulnerabilities and stayed stuck on fixing them, and AI is the first thing that makes moving the fixing side at the same pace actually achievable,” Lawrence says. “Advanced models are also making it easier and cheaper to find and exploit weaknesses in open source, which is part of what’s driving the urgency now. The same capability that reads code to fix a flaw can read it to exploit one, which is exactly why every patch is human-verified before it ships.”

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://thenewstack.io/wp-content/uploads/2026/02/bd93adde-cropped-9c2ecfc5-a-600x600.jpg)

Paul is an experienced technology journalist covering some of the biggest stories from Europe and beyond, most recently at TechCrunch where he covered startups, enterprise, Big Tech, infrastructure, open source, AI, regulation, and more. Based in London, these days Paul...

Read more from Paul Sawers](https://thenewstack.io/author/paul-sawers/)