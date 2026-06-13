**The promise of [agentic development](https://thenewstack.io/agentic-ai-is-quickly-revolutionizing-ides-and-developer-productivity/) is that anyone** — the finance analyst, the operations manager, the [non-technical founder](https://thenewstack.io/vibe-coding-ceos-executives-ai-agents/) — can [vibe code](https://thenewstack.io/how-to-use-vibe-coding-safely-in-the-enterprise/) a solution into existence without waiting on an engineering team. But the assumption is that the open-source ingredients going into those [AI-generated applications](https://thenewstack.io/ai-coding-tools-create-more-bugs-than-they-fix/) are safe to use.

[Chainguard](https://www.chainguard.dev/), the supply chain security firm, is betting they are not — and says it has the data to prove it.

The company introduced a new [source code scanner](https://thenewstack.io/sonatype-offers-its-malicious-source-code-blocker-as-a-service/) this week that goes beyond traditional malware detection to catch what it is calling “greyware”: Open-source packages that do exactly what they advertise, pass every existing security scan on the market, and still do things no enterprise security team would ever allow, the company says.

> “Frank in finance is not a coder. He’s an FP&A guy. And so along comes a solution that can say, hey, you can vibe code stuff into existence — but don’t just grab random stuff off the internet that could come from anywhere or be manipulated by bad actors.”

“The big promise of agentic code development is that it allows organizations to pivot from a world where they essentially had to pick from what vendors are willing to offer them,” Chainguard CISO [Quincy Castro](https://www.linkedin.com/in/quincy-castro/) tells *The New Stack* in a briefing. “But Frank in finance is not a coder. He’s an FP&A [Financial Planning and Analysis] guy. And so along comes a solution that can say, hey, you can vibe code stuff into existence — but don’t just grab random stuff off the internet that could come from anywhere or be manipulated by bad actors.”

The new Chainguard scanner is now analyzing more than 100,000 packages per day and has already blocked more than 52,000 packages identified as malware or greyware.

## What greyware is

The distinction matters. Traditional malware hides what it does. Greyware, as Chainguard defines it, is transparent about its functionality — it just buries the harmful parts in plain sight.

One of Castro’s examples from the briefing was that of a social media automation package that required access tokens to function. But the package also exported those tokens to a remote command-and-control server — behavior that had no plausible connection to its stated purpose, and was nowhere near disclosed to the developer who installed it.

> “I don’t think a normal person would imagine they were also approving those tokens to be exported off their system and sent somewhere for who knows what purposes.”

“You think you’re giving this thing access to automate what you’re doing,” Castro says. “I don’t think a normal person would imagine they were also approving those tokens to be exported off their system and sent somewhere for who knows what purposes.”

The pattern shows up across credential theft, API key harvesting, command interception, and persistent remote access. Chainguard has already flagged five live examples on npm — packages with names like `chrome-tools` and `@robinpath/cloud-cli` that openly export modules for harvesting Chrome passwords, cookies, and credit card data, or that establish permanent backdoors to third-party servers. All five are still available for download. All have passed the standard seven-day cooldown period that registries use as a trust signal.

Castro says he believes greyware is more prevalent than outright malware in the wild — and harder to catch because it is subtler.

“Greyware packages have functionality that no reasonable developer or enterprise would expect, want, or permit in their applications if it were subject to formal review,” write [Ross Gordon](https://www.linkedin.com/in/rosscgordon/), Staff Product Marketing Manager, and [Evan Gibler](https://www.linkedin.com/in/egibs/), Staff Security Engineer at Chainguard, in a [blog post](https://www.chainguard.dev/unchained/the-expanding-threat-landscape-chainguard-now-scans-source-code-for-traditional-malware-and-greyware) about the launch.

“These packages look identical to everything else you’re downloading from public registries, yet offer concerning security shortcomings. They honestly declare what they do, and what they do is harmful. The examples we’ve found are some combination of credential theft, command interception, API key harvesting, and persistent remote access.”

## Why AI makes this worse

The greyware problem is not new. But agentic development has turned a manageable risk into a structural one, Castro explains.

Manual code review was already becoming impractical before AI coding tools arrived, he says. Now, with non-technical users spinning up applications via natural language prompts and AI agents automatically pulling in dependencies, the surface area for greyware exposure has expanded enormously. And human oversight cannot keep up.

> > “Whether we’re doing it at gargantuan scale against a huge portion of the source, or whether that’s a dev doing it themselves — for anybody, it’s increasingly impractical.”

“Whether we’re doing it at gargantuan scale against a huge portion of the source, or whether that’s a dev doing it themselves — for anybody, it’s increasingly impractical,” Castro says of manual review.

This creates a specific threat model for the enterprise agentic wave. When a knowledge worker vibe codes a workflow automation tool, and their agent pulls in a package that harvests access tokens, there is no SRE team standing between the developer and the damage, Castro explains.

Chainguard’s scanner is designed to sit at that chokepoint. Rather than scanning packages when a developer requests them — creating exposure windows where malicious packages can be cached before detection fires — it analyzes packages before they are added to the Chainguard Libraries catalog at all.

The scanner evaluates maintainer behavior, package contents, publishing signals, and dynamic execution in a sandboxed environment, and decides before the package is ever served.

## The competitive claim

Chainguard’s blog post makes a pointed assertion that alternatives only catch obvious malware. Asked to back that up, Castro stood by it — and offered a possible explanation for why competitors might be behind.

“We literally build an immense amount of open source daily, hourly,” he says. “We have a lot of data on what these packages look like and the telemetry around them when they get built. It may be that we have signal around some of this stuff that other folks just don’t have.”

Socket, Snyk, Sonatype, and Endor Labs have all invested heavily in behavioral analysis of open source packages.

Regarding false positives, Castro says none have been detected so far. The company is also building a policy override layer that would allow customers to whitelist blocked packages, with Chainguard’s product security team overseeing those decisions and monitoring whitelisted packages for behavioral drift over time.

“We’re making an intentional tradeoff here to allow false positives in order to prevent false negatives,” writes Chainguard co-founder and CEO [Dan Lorenc](https://www.linkedin.com/in/danlorenc/) in a post on LinkedIn. “Our early testing shows it performs as well or better than every other malware scanner out there, and you get the added benefits of blocking greyware. If we ever go too far, you can just allow-list individual packages. We won’t judge you.”

## The bigger picture

The greyware positioning calls out a problem that has largely been ignored. [Supply chain security](https://thenewstack.io/are-we-thinking-about-supply-chain-security-all-wrong/) has centered on issues such as typosquatting, dependency confusion attacks, and compromised maintainer accounts — all cases where something is hidden. The harder case is the package that tells you exactly what it does and counts on the fact that you will not read carefully enough to understand it.

Agentic development does not make developers more careful. It makes them faster. And in a world where Frank in finance can vibe code a production workflow in an afternoon, the security review that should happen between “install package” and “ship to prod” has to happen somewhere, Castro says. Chainguard is arguing it should happen before the code ever lands.

Chainguard’s scanner currently protects npm packages served through Chainguard Libraries for [JavaScript](https://thenewstack.io/30-years-of-javascript-10-milestones-that-changed-the-web/). Coverage is expanding to additional ecosystems in the coming weeks, the company says.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://thenewstack.io/wp-content/uploads/2021/06/a95bb5bc-image-576x600.png)

Darryl K. Taft covers DevOps, software development tools and developer-related issues from his office in the Baltimore area. He has more than 25 years of experience in the business and is always looking for the next scoop. He has worked...

Read more from Darryl K. Taft](https://thenewstack.io/author/darryl-taft/)