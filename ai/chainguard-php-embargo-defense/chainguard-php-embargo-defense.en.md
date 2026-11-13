![The Chainguard booth at KubeCon + CloudNativeCon North America in Salt Lake City in November 2026. (Credit: The New Stack)](https://cdn.thenewstack.io/media/2026/11/f70453f4-chainguard-kube-con-booth-na-2026-1024x586.png)

**At KubeCon + [CloudNativeCon North America](https://events.linuxfoundation.org/kubecon-cloudnativecon-north-america/) 2026 this week**, Chainguard co-founder and CTO Matt Moore defended the company’s decision to release patched PHP images before an agreed-upon embargo with other partners had lifted.

When Chainguard shipped [patched PHP container images](https://thenewstack.io/php2shell-chainguard-embargo-dispute/) more than six hours ahead of an October 21 coordinated security release, PHP’s maintainers accused the company of giving attackers a head start. Chainguard argues attackers already had one.

![](https://cdn.thenewstack.io/media/2026/11/0285dd07-chainguard-cto-matt-moore.jpeg)

*Chainguard founder and CTO Matt Moore*

In an interview with *The New Stack*, [Moore](https://www.linkedin.com/in/mattmoor/) said, “We own the decision that we chose to do it. Nobody could force us to do it — but we did not do it in a vacuum.” He also described, in discussions with TNS, other participants in the embargo and security vendors’ reports of activity targeting the vulnerabilities before Chainguard released its images.

Chainguard was not saying that they patched it faster so they shipped it first. According to Moore, Chainguard believed attackers could already exploit the bugs, or were at least close to figuring out how — or were trying to figure it out.

The two vulnerabilities, [CVE-2026-109618 (out-of-memory corruption)](https://nvd.nist.gov/vuln/detail/cve-2026-109618) and [CVE-2026-109619 (stale global state)](https://nvd.nist.gov/vuln/detail/cve-2026-109619), collectively known as PHP2Shell, were serious memory-management and error-handling flaws. Under the right conditions, an unauthenticated attacker could execute code on a PHP server.

The two bugs involved PHP’s handling of memory exhaustion and its failure to clear references to freed memory between requests. In the first, reaching a memory limit at the wrong moment could interrupt PHP before it finished setting up internal data. Later processing could mistake that unfinished data for valid information. In the second vulnerability, an error could leave PHP holding a reference to memory from an earlier request that had already been freed. A subsequent request could then access that invalid memory. Under exploitable conditions, these failures could let an attacker run code inside the server’s PHP process.

Researchers demonstrated remote code execution through both Apache/mod\_php and application-level PHP-FPM paths for the first vulnerability, and against a real-world Apache/mod\_php application for the second.

These were problems in PHP itself, not something an administrator could fix by simply updating a WordPress plugin. It was a fundamental and nasty security hole.

## How bad were the flaws?

PHP’s advisories rate both vulnerabilities 9.2, or critical, under the [Common Vulnerability Scoring System](https://github.com/php/php-src/security/advisories/GHSA-w8hw-w9fx-j79w) (CVSS) v4.0. Exploitability depends on the PHP build, server configuration, extensions, and application behavior. The advisories do *not* establish that every PHP installation can be compromised. PHP released fixes in versions 8.2.35, 8.3.36, 8.4.27, and 8.5.12. The potential exposure is substantial: As of November 11, W3Techs reported that PHP powered [68.8% of websites](https://w3techs.com/technologies/comparison/pl-php) whose server-side programming language it could identify.

According to the [PHP Foundation’s account](https://thephp.foundation/blog/2026/10/21/todays-php-security-release-and-how-were-strengthening-php-security/), a developer investigating issues from a 2024 security audit spotted the out-of-memory problem, but no concrete attack path was established then. Proposed fixes risked compatibility breaks, new denial-of-service problems, or changes across PHP extensions.

On August 11, [Calif](https://calif.io/) researcher Ryan A. reported remote code execution from the same underlying problem. From that date, fixing it became the PHP Foundation security team’s top priority. OpenAI independently reported the same underlying flaw. Wiz supplied additional attack vectors on August 24, and OpenAI reported more on September 18.

## How the PHP security patch came apart

In response, PHP’s maintainers coordinated fixes with researchers and distributors. Then details about the release process began leaking.

On October 20, the [CVE identifiers circulated publicly](https://thephp.foundation/blog/2026/10/21/todays-php-security-release-and-how-were-strengthening-php-security/), accompanied by an incorrect release time and severity score. PHP responded by issuing a warning and moving the release forward a day, to October 21 at 14:00 UTC. Calif, one of the reporting security companies, then mistakenly published a video demonstrating its proof of concept. Although the video was deleted, copies circulated. PHP also acknowledged that mitigation advice given to critical infrastructure providers might have leaked.

In short, the information environment was already a mess before Chainguard published anything.

But the PHP Foundation maintained that its remaining coordination window still served a purpose: specifically that distributors were packaging the fixes, and releasing immediately would leave many users without a straightforward update path. At 07:41 UTC on October 21, Chainguard published its patched images anyway — six hours and 19 minutes before the agreed-upon time.

The PHP Foundation [criticized](https://thephp.foundation/blog/2026/10/21/todays-php-security-release-and-how-were-strengthening-php-security/#:~:text=the%20coordinated%20release%2C-,Chainguard%20unilaterally%20broke%20the%20embargo%20and%20published%20built%20images%20containing%20the%20fix.,-Like%20other%20distributors) this move: “Chainguard unilaterally broke the embargo and published built images containing the fix.” That meant, it argued, that “any attacker could now study the fix in binary form while every other PHP user was still waiting for the release.”

> A patched binary protects the person who installs it. It can also tell an attacker where to look.

That was the PHP Foundation’s central objection. A patched binary protects the person who installs it. It can also tell an attacker where to look.

## Moore’s defense: The advantage had already shifted to the attackers

Moore doesn’t dispute that releasing patched binaries can help attackers. He argues that, by then, the advantage an embargo was supposed to preserve had already eroded.

While defenders alone know about a vulnerability, he told *The New Stack*, confidentiality gives them time to prepare. Once attackers have enough information to exploit it, withholding available fixes can reverse that advantage: attackers can act, while users outside the embargo cannot protect themselves.

“If we see exploitation in the wild, it’s incumbent upon us to release it,” Moore said. In his account, reports from other security vendors were what pushed Chainguard toward that conclusion.

Moore said Chainguard learned on the Friday before the release that PHP had a vulnerability, pointed its vulnerability-hunting harness at the software, and found the vulnerability or produced a proof of concept within hours. That is Chainguard’s account of its own research. But it helps explain the company’s thinking in breaking the embargo: If your tools can find the bug quickly, you have to consider whether attackers’ tools can too.

He also disputed the implication that Chainguard simply went off on its own. According to Moore, other embargo participants woke [Chainguard CEO Dan Lorenc](https://www.linkedin.com/in/danlorenc) to discuss the situation while PHP maintainers in Europe were asleep. Moore declined to identify those participants.

Moore accepted that Chainguard made the final decision. It does, however, distinguish the company’s account of a disputed emergency decision from an account in which it ignored everyone else without discussion.

## The evidence supports concern, not certainty

Public evidence supports Chainguard’s concern that attackers were already targeting the flaws. For example, Amazon Threat Intelligence reported a [PHP2Shell exploitation attempt](https://aws.amazon.com/blogs/security/amazon-threat-intelligence-identifies-php2shell-exploitation-prior-to-public-disclosure-in-madpot/) against its MadPot honeypot network on October 17, four days before public disclosure. It also reported proof-of-concept exploits beginning around 02:00 UTC on October 21, followed by additional attempts from anonymized infrastructure over the next six hours. Some of that activity clearly preceded Chainguard’s 07:41 release.

Cloudflare likewise reported observing attack traffic targeting its customers before the official release. It said its free and paid [web application firewall protections](https://blog.cloudflare.com/php-vulnerabilities-waf-protection) were enabled by default starting at 03:02 UTC on October 21.

So, no, Chainguard was not imagining hostile interest in these bugs.

But Amazon included an important qualification: “Technical analysis is ongoing, and it’s unclear if any of these attempts would have succeeded in real-world systems.” The PHP security team, meanwhile, said it examined the circulating proofs of concept and “did not identify any functional exploits at the time of release/public disclosure.”

Those statements are not necessarily contradictory. A honeypot can record a request intended to exploit a vulnerability without establishing that it can achieve remote code execution against a real application. Likewise, PHP’s failure to find a functional public exploit does not prove that no attacker privately possessed one.

Subsequent evidence should not be confused with what was known that morning. On October 26, CISA added both vulnerabilities to its [Known Exploited Vulnerabilities catalog](https://content.govdelivery.com/accounts/USDHSCISA/bulletins/4309083). That confirms exploitation was known by then; it does not establish when the first successful compromise occurred or whether Chainguard’s early release enabled it.

Welcome to security incident response. The evidence rarely arrives neatly labeled.

## Did the binaries give attackers something they lacked?

Moore’s second argument is narrower. Attackers were already probing the relevant code, so publishing patched binaries might not have helped much.

“I don’t see any evidence that what we did helped the attackers in ways that they didn’t already have,” he told TNS. He acknowledged that comparing patched and unpatched binaries can identify vulnerable code, including with AI-assisted disassembly. But identifying the code, he argued, isn’t necessarily the same as building a working exploit.

Fair enough. Locating a memory-corruption bug and reliably turning it into remote code execution are different engineering problems.

Still, this defense has limits. Evidence that some attackers knew where to look does not establish that every prospective attacker did. Nor does it establish that the patch contained no useful clues beyond the vulnerability’s location. Chainguard’s argument depends on how much actionable information was already available and how reliable it was.

The same restraint applies to the accusation against Chainguard. Publishing the binaries created an opportunity to study the changes. It does not, by itself, demonstrate that a particular compromise happened because Chainguard released early.

The two sides were assessing different risks. Chainguard emphasized the danger of withholding a ready patch from users while hostile activity was visible. PHP emphasized the danger of distributing new information before the wider ecosystem could update. Both risks were real.

## AI makes the timing problem worse

The broader concern is that [AI-assisted vulnerability research](https://thenewstack.io/php2shell-ai-vulnerabilities-maintainers/) could shorten the time defenders have to respond. The public reports cited here do not establish whether the pre-release PHP2Shell attempts used AI, or that this was the first incident of its kind.

For Moore, the PHP dispute fits a larger problem: attackers’ ability to turn vulnerability information into an exploit may outrun defenders’ ability to build and distribute a fix.

He described a scenario in which a Chromium patch becomes public, and an attacker develops an exploit faster than it takes to compile the browser. That was a warning about where the industry is heading, not a claim that this exact scenario had occurred.

“You literally cannot produce builds fast enough,” he said. And the build is only the beginning. Even if Chainguard produces an updated image quickly, customers still have to incorporate it, rebuild their applications, test them, and deploy.

> Faster does not mean instantaneous, and a supplier’s release time is not a customer’s remediation time.

That is the uncomfortable part of the “patch faster” answer. Faster is useful. Faster does not mean instantaneous, and a supplier’s release time is not a customer’s remediation time.

Moore’s proposed longer-term response is to reduce the number of vulnerabilities that require this race in the first place. He discussed with TNS the work toward ABI-compatible replacements for foundational [software components in Rust](https://thenewstack.io/white-house-warns-against-using-memory-unsafe-languages/), along with formal verification techniques intended to rule out particular classes of defects. These remain engineering ambitions to evaluate.

They also do not settle, in the eyes of Chainguard’s critics, what the company should have done on October 21. A future with fewer memory-corruption bugs would be welcome, but administrators dealing with the current bugs still need a workable disclosure process, they would argue.

## The lesson is bigger than Chainguard

It would be easy to see this incident as only a story about one vendor breaking the rules. It would be equally easy to see it as a story about an agile security company rescuing users from a slow-moving upstream project. It’s not that simple.

PHP’s own postmortem acknowledges a deeper failure. The foundation calls that delay “a structural failure,” involving both decision-making and insufficient resources.

Finding bugs faster doesn’t automatically provide the [engineers needed to fix](https://thenewstack.io/open-source-paid-maintainers-keep-code-safer-survey-says/) them safely. And getting a patch ready at one company doesn’t mean an ecosystem of distributions, hosting providers, extensions, and applications is ready to deploy it.

Many people jumped to attack Chainguard for its call. For instance, [Jay Gazlay](http://linkedin.com/in/jay-gazlay-58535), CISA’s acting associate director for vulnerability management, said at an October 28 Red Hat conference in Washington: “that type of behavior is dangerous, and we’ve got to be [careful about holding embargoes](https://federalnewsnetwork.com/cybersecurity/2026/10/dangerous-cisa-official-criticizes-companys-decision-to-release-php-bug-early/).”

There may still be room to repair the relationship. [*Federal News Network*](https://federalnewsnetwork.com/cybersecurity/2026/10/dangerous-cisa-official-criticizes-companys-decision-to-release-php-bug-early/), citing [*Politico*](https://www.politico.eu/article/the-cyber-flaw-scramble-that-brought-the-ai-threat-to-life/), reported that PHP Foundation Executive Director Elizabeth Barron expressed disappointment with Chainguard but hoped to restore trust and continue collaborating.

Moore called it “a really tough call” between “two really, really bad choices.” He’s right.

Maintainers and distributors need to agree in advance on when to lift an embargo early, who makes that decision, and how other distributors will get fixes to their users.

We need to do this as soon as possible. Otherwise, the next incident will end the same way, with vendors arguing about who broke the embargo. At the same time, administrators try to work out whether they can patch before somebody breaks their servers.

The post [Chainguard defends its choice to break the PHP security embargo: “We own the decision.”](https://thenewstack.io/chainguard-php-embargo-defense/) appeared first on [The New Stack](https://thenewstack.io).