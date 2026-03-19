As [AI coding assistants](https://thenewstack.io/ai-coding-assistants-are-reshaping-engineering-not-replacing-engineers/) and autonomous agents dramatically [accelerate software development](https://thenewstack.io/think-like-a-developer-to-help-dev-teams-ship-faster/), they’re introducing a security problem that most organizations aren’t prepared for: dependency sprawl at machine speed.

Chainguard CEO [Dan Lorenc](https://www.linkedin.com/in/danlorenc/) tells *The New Stack* that coding agents have a blind spot. Their training data is typically a year or more out of date, which means when they reach for a library, they default to older, often insecure versions — not because they’re careless, but because that’s what they know. And as more and more production code gets written by agents, that pattern compounds fast.

“When you ask an agent to generate code, its training window is usually a year old,” says Lorenc. “So, it defaults to older versions of all these libraries, because that’s what it’s trained on. You can have agents update code, but it takes a lot more time and care than people trying to go faster.”

## Attackers are using AI too

Meanwhile, Lorenc says attackers are increasingly using AI themselves — not to accidentally write vulnerable packages, but to find and exploit misconfigurations at a scale and speed that would take a human researcher days.

A recent breach of the [Trivy project](https://trivy.dev/), a [vulnerability scanner](https://thenewstack.io/aqua-securitys-trivy-security-scanner-can-scan-anything-now/) from [Aqua](https://thenewstack.io/aqua-security-uncovers-major-kubernetes-attacks/), illustrated the threat, he said. Attackers deployed agents to systematically identify known misconfigurations across dozens of GitHub organizations, automating what would otherwise have been hours of manual digging.

“There was a big breach of the Trivy project a few weeks ago,” Lorenc says. “Attackers compromised dozens of other GitHub organizations just by having agents go and find these known misconfigurations. It takes a human maybe seven hours of working and digging. We’re seeing a lot more AI-enabled attacks.”

Nearly 455,000 malicious packages flooded npm, PyPI, and Maven Central in 2025 alone, according to Sonatype’s annual software supply chain report. The average container carries more than 600 known CVEs, and 89% of container images in production contain known vulnerabilities, Chainguard says.

## A single front door for open source

To address the problem, Chainguard on Tuesday announced Chainguard Repository, a unified, secure-by-default repository for open source artifacts. The product gives developers — and the AI agents writing code alongside them — a single, governed endpoint for pulling open-source libraries, containers, OS packages, and virtual machines, with configurable security policies enforced at the point of consumption. Lorenc said.

Starting today, Chainguard Repository is available in production for JavaScript, giving customers access to more than 70,000 Chainguard-built npm packages. Those libraries are built in an SLSA Level 3-compliant environment and eliminate 99.7% of malware by design. For packages served from the upstream npm registry as a fallback, a seven-day cooldown policy filters out malware that the broader research community identifies during that window.

## The cooldown dilemma

However, the cooldown policy has its limits, Lorenc says. The approach, which originally surfaced in [Snyk](https://thenewstack.io/security-firm-snyk-tackles-ai-codings-perfect-storm/) research showing that waiting a week sidesteps most malware, faces a structural problem. That is, if everybody adopts it, attackers simply adjust their timelines.

“If everyone does that, then it becomes less effective, and you have to wait even longer,” Lorenc tells The New Stack. “And sometimes you need software before that. If there’s a critical CVE in something, you can’t be waiting seven days for a new version. You’re being chased by one bear while trying to catch another one.”

Organizations dealing with a critical CVE in a production dependency can’t always wait a week for a patched version. Chainguard’s answer is configurable exceptions that let security teams bypass the cooldown for critical fixes while maintaining the default posture everywhere else.

## Governance beyond security

The governance use case extends beyond security. Lorenc notes that as Chainguard’s library coverage has grown, some customers are now using policy controls simply to manage the sheer volume of available packages — not for security reasons, but for engineering discipline.

“We have a lot of customers where we now have so many libraries that it’s actually too many, and they want to be able to control which ones developers are getting,” Lorenc says. “Maybe you don’t need 17 different database clients or 32 different date-time parsers.”

Chainguard is looking ahead to an era when neither developers nor their AI tools can be expected to make safe dependency choices on their own. Chainguard Repository can replace or integrate with existing artifact managers like [Artifactory](https://thenewstack.io/jfrog-brings-artifactory-on-prem-for-aws-with-eks-anywhere/), [Cloudsmith](https://cloudsmith.com/), and [Nexus](https://www.sonatype.com/products/sonatype-nexus-repository), and complement [SCA scanning tools](https://thenewstack.io/sca-should-be-in-your-toolbox-to-address-supply-chain-risk/) like Snyk and [Sonatype](https://thenewstack.io/sonatype-offers-its-malicious-source-code-blocker-as-a-service/) that identify vulnerabilities but don’t provide clean versions.

“This is a single point where you can point all of your clients directly, and we’ll control what’s going in there,” Lorenc says. “You can set whatever policies you need.”

## Security that improves on its own

As [Chainguard’s AI-powered Factory](https://thenewstack.io/chainguard-500-million-builds/) rebuilds more packages from source, the security posture of organizations using the repository improves automatically with no configuration changes or code updates required. Lorenc says he sees this as the key architectural shift: rather than scanning for problems after the fact, security is enforced at the point of consumption.

Lorenc also called out AI skill hijacking as an emerging threat vector that the industry is only beginning to see. While MCP hijacking remains early-stage, attacks on AI skill ecosystems — platforms like skills.sh where agents pull tools dynamically at runtime — are already happening at scale.

“We see a lot of skill hijacking with AI skills now,” Lorenc says. “These tools pull down whatever tools they feel like at runtime if you’re deploying them insecurely. There was a [big attack on the skills ecosystem a few weeks ago for OpenClaw](https://thenewstack.io/openclaw-moltbot-security-concerns/). That’s how people share OpenClaw workflows.”

## What’s next

Later this year, Chainguard Repository will expand to Python and Java libraries, container images, OS packages, and virtual machines. Additional policy controls planned for release include CVE blocking to prevent artifacts with known critical vulnerabilities from being pulled, license enforcement to restrict artifacts to approved licenses, and end-of-life prevention to reject unmaintained dependencies before they enter production. [Chainguard Repository](https://chainguard.dev/libraries/javascript) is available now.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://thenewstack.io/wp-content/uploads/2021/06/a95bb5bc-image-576x600.png)

Darryl K. Taft covers DevOps, software development tools and developer-related issues from his office in the Baltimore area. He has more than 25 years of experience in the business and is always looking for the next scoop. He has worked...

Read more from Darryl K. Taft](https://thenewstack.io/author/darryl-taft/)