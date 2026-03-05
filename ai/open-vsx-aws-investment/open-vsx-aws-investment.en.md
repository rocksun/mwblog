The [Eclipse Foundation](https://www.eclipse.org/) this week announced that [Open VSX,](https://open-vsx.org/) the open source extension registry for tools built on the [VS Code extension API](https://code.visualstudio.com/api), has surpassed 300 million downloads per month, a milestone the organization says underscores its role as “foundational infrastructure” for the global developer ecosystem.

The figure comes as the Eclipse Foundation, a non-profit steward of open-source software and collaboration, continues to strengthen the registry’s security and infrastructure posture amid rising demand from AI-native and cloud-based platforms.

With peak daily traffic exceeding 50 million requests and more than 10,000 extensions from over 6,500 publishers, Open VSX now sits in the operational path of tools such as [Amazon’s Kiro](https://thenewstack.io/kiro-is-awss-specs-centric-answer-to-windsurf-and-cursor/), [Google’s Antigravity](https://thenewstack.io/hands-on-with-antigravity-googles-newest-ai-coding-experiment/), [Cursor](https://thenewstack.io/cursor-2-0-ide-is-now-supercharged-with-ai-and-im-impressed/), and other VS Code–compatible editors.

Financial backing has followed that growth. News emerged [in November](https://eclipse-foundation.blog/2025/11/05/aws-invests-in-strengthening-open-source-infrastructure-at-the-eclipse-foundation/) that Amazon Web Services (AWS) would invest in open infrastructure operated by the Eclipse Foundation, including Open VSX.

The Foundation has now confirmed to *The New Stack* that the AWS commitment is a “multi-year, seven-figure” strategic investment. Cursor, whose AI-focused editor drives significant traffic to the registry, is now also providing financial support.

> “The AWS commitment constitutes ‘infrastructure credits and operational collaboration’ focused on bolstering Open VSX and other critical services under the Eclipse Foundation.”

The AWS commitment constitutes “infrastructure credits and operational collaboration” focused on bolstering Open VSX and other critical services under the Eclipse Foundation.

While AWS is already a member of the Eclipse Foundation, the organization stresses that membership and infrastructure investment are separate. Membership fees support the Foundation’s governance and project services across its broader open-source portfolio and are tiered by company size and class.

Participation in the Open VSX Working Group carries an annual fee of €40,000. The infrastructure support for Open VSX, by contrast, is specifically designed to strengthen the registry’s technical operations as demand scales.

Eclipse maintains that the arrangement does not grant additional decision-making authority over the project, as [Thabang Mashologu](https://www.linkedin.com/in/thabang-mash/), the Eclipse Foundation’s CMO and head of product, tells *The New Stack*:

“This support does not confer any governance rights, veto authority, or special oversight,” Mashologu says. “Open VSX continues to operate under the Eclipse Foundation’s vendor-neutral governance model and the established processes of the Open VSX Working Group.”

## A bazaar is born

To rewind a little, Open VSX was born out of a licensing limitation with Microsoft’s Visual Studio Marketplace, which [stipulates that extensions may only be installed](https://cdn.vsassets.io/v/M264_20251020.18/_content/Microsoft-Visual-Studio-Marketplace-Terms-of-Use.pdf) and used with Microsoft products such as Visual Studio, VS Code, and other “in-scope products,” leaving open source forks and alternative editors unable to access it directly.

Open VSX emerged as an open-source alternative: a registry that implements the same VS Code extension API but is governed independently.

The project was initially developed by [TypeFox](https://www.typefox.io/), with the first public instance of Open VSX going live in 2020. Shortly after, stewardship began transitioning to the Eclipse Foundation, and by early 2021, the [registry was operating](https://thenewstack.io/eclipse-open-vsx-registry-offers-open-access-to-vs-code-extensions/) under the Foundation’s governance, giving it a formal nonprofit home and establishing open source oversight.

Over time, a growing number of browser-based IDEs, cloud development environments, and AI-native coding tools adopted Open VSX as their default or fallback registry. As *The New Stack* reported [in 2023](https://thenewstack.io/alternative-to-visual-studio-marketplace-gains-momentum/), that growth led to the creation of a dedicated Open VSX working group within the Eclipse Foundation, backed by companies including Google and Salesforce, to provide more structured support and funding for the registry’s continued development.

At its core, the registry is a package distribution service for VS Code – compatible extensions that deliver everything from language servers, linters, and debuggers to testing tools and cloud connectors. That function places it at a critical juncture in the software supply chain. A compromised extension can spread quickly across developer machines and hosted workspaces, and impersonation of trusted publishers has been documented in other ecosystems.

Against that backdrop, Eclipse is fortifying the registry with a [new pre-publication verification framework](https://blogs.eclipse.org/post/christopher-guindon/strengthening-supply-chain-security-open-vsx), which scans and vets extensions before publication. It’s designed to catch certain classes of risk earlier in the lifecycle, including namespace impersonation, extension name spoofing, embedded credentials, and known malicious patterns, with suspicious uploads quarantined for review.

While most submissions pass through automated screening, those that raise red flags are escalated for closer scrutiny before they are allowed into the registry.

“Extensions that trigger defined risk signals are automatically quarantined for further review,” Mashologu says. “Manual review is reserved for flagged cases or ambiguous indicators. We have also introduced internal reporting and administrative tooling to support oversight. As with most security systems, certain implementation details are intentionally not disclosed to reduce the risk of circumvention.”

Beyond screening what gets published, Eclipse is also addressing how extensions are consumed. The registry is implementing targeted [rate limiting](https://blogs.eclipse.org/post/christopher-guindon/scaling-open-vsx-registry-responsibly-rate-limiting) and traffic controls aimed at sustained, high-volume automated requests, a pattern more common in AI-assisted and cloud-based development environments where extensions are installed, updated, or provisioned programmatically.

Operationally, Open VSX is also [transitioning to a hybrid model](https://blogs.eclipse.org/post/denis-roy/hardening-open-vsx-registry-keeping-it-reliable-scale). Previously, production workloads were hosted in Canada across a mix of Eclipse Foundation on-premises infrastructure and cloud services. Primary production now runs on AWS infrastructure in Europe, while a fully operational on-premises deployment in Canada will be maintained as an independent secondary environment managed by the Eclipse Foundation.

The shift reduces reliance on a single geographic environment and strengthens resilience as automated and AI-driven workloads generate heavier and more continuous extension traffic.

## “Shared infrastructure”

Amazon’s investment is notable, given that Kiro, Amazon’s [AI-native development environment](https://thenewstack.io/aws-kiro-testing-an-ai-ide-with-a-spec-driven-approach/) built on VS Code, relies heavily on extension distribution to deliver core functionality. When those tools install or update extensions, requests frequently flow through Open VSX.

That dynamic explains why commercial adopters are stepping in to support the registry and, in the case of AWS, hosting the primary production environment for Open VSX in Europe. Cursor’s financial backing, meanwhile, reflects its growing reliance on the same extension pipeline as its AI-focused editor’s usage expands.

> “Open VSX has evolved into foundational infrastructure for the global developer ecosystem… Support from leading commercial adopters reinforces Open VSX as trusted, shared infrastructure.”

And it’s this shared dependency, Eclipse argues, that underpins these investments.

“Open VSX has evolved into foundational infrastructure for the global developer ecosystem,” said Mike Milinkovich, executive director of the Eclipse Foundation, in a statement. “As adoption accelerates across AI-native and cloud-based development platforms, we are investing to ensure the registry remains secure, resilient, and vendor-neutral. Support from leading commercial adopters reinforces Open VSX as a trusted, shared infrastructure.”

For developers building and using AI-native coding tools, most of these changes will be invisible day-to-day. Extensions will continue to install and update in the background.

The more consequential shifts are structural: tighter controls on what gets published, clearer traffic management policies, and a hybrid deployment model intended to withstand heavier demand.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://thenewstack.io/wp-content/uploads/2026/02/bd93adde-cropped-9c2ecfc5-a-600x600.jpg)

Paul is an experienced technology journalist covering some of the biggest stories from Europe and beyond, most recently at TechCrunch where he covered startups, enterprise, Big Tech, infrastructure, open source, AI, regulation, and more. Based in London, these days Paul...

Read more from Paul Sawers](https://thenewstack.io/author/paul-sawers/)