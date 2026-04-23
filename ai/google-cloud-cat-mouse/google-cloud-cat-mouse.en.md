The core problem in AI security right now is that attackers are using AI models to find and exploit zero-day vulnerabilities within hours, while defenders are often still manually triaging alerts.

Google Cloud’s response, announced on Wednesday at Next ’26, is to throw new AI-powered security agents at the problem — and, in the long run, its $32 billion Wiz acquisition. The company’s bet is straightforward and something we’ve been hearing for quite a while now: defense has to be as agentic as offense — and it has to work across every cloud.

> Defense has to be as agentic as offense — and it has to work across every cloud.

The window between “vulnerability exists” and “exploit in the wild” is narrowing.  
Anthropic’s Claude Mythos Preview, announced in early April and released to roughly 40 organizations through Project Glasswing, can [autonomously find and exploit zero-day vulnerabilities](https://thenewstack.io/claude-mythos-preview-simulation/). Anthropic considered it too dangerous for public release, but in the long run, AI vendors won’t be holding back models like this.

It’s worth noting that Google is one of the Glasswing partners. The model is available on what was, until Wednesday, called Vertex AI (now the Google Gemini Agent Platform) for defensive use, and security teams can point it at their own infrastructure and find the exploitable flaws before an attacker does. Google isn’t using it for any of its own launches today, though.

## What Google Cloud is adding

Google is adding three new AI agents — all in preview — to Google Security Operations, its cloud-native Security Information and Event Management (SIEM) and Security Orchestration, Automation, and Response (SOAR) platform.

The Threat Hunting agent proactively scans for novel attack patterns and adversary behaviors that bypass traditional rule-based defenses. A Detection Engineering agent identifies gaps in an organization’s detection coverage and automatically creates new detections for threat scenarios — turning what has historically been a manual, analyst-driven craft into something closer to an automated pipeline. A Third-Party Context agent enriches security workflows with contextual data from external sources.

> The window between “vulnerability exists” and “exploit in the wild” is trending toward zero.

The additions build on an existing Triage and Investigation agent that Google says has processed more than 5 million alerts over the past year. The company says that this agent has been reducing what would typically be a 30-minute manual analysis to about 60 seconds.

Together, the four agents cover most of the security operations workflow: the Triage agent handles the initial alert volume and filters out false positives, the Threat Hunting agent goes looking for what the rules missed, the Detection Engineering agent closes the gaps those hunts reveal, and the Third-Party Context agent pulls in the outside intelligence that ties it all together.

## What Wiz is shipping

Google did not spend $32 billion without having a few Wiz announcements at Google Cloud Next, too.

For the most part, Wiz is not launching new products but new features for existing ones, as well as new integrations. Like Google itself, many of these also target the AI-native development lifecycle, which now often includes far more code being pushed to production without extensive reviews.

What’s interesting here is that Wiz is focused not only on Google Cloud but also on third-party clouds and ecosystems. The company launched its AI-Application Protection Platform (AI-APP), its service for securing AI apps from end-to-end, earlier this year. Now, the company is extending its support to Databricks, AWS Agentcore, Gemini Enterprise Agent Platform, Microsoft Azure Copilot Studio, and Salesforce Agentforce.

Wiz’s [own research in 2025](https://www.wiz.io/blog/common-security-risks-in-vibe-coded-apps) found that 20 percent of vibe-coded apps contain security risks. Starting in May, a new integration runs Wiz scanning directly inside the vibe-coding service Lovable, surfacing vulnerabilities and misconfigurations before code ships.

For professional developers, Wiz is adding inline AI security hooks in IDEs and agent workflows, which will also ideally catch problems before the code is every commit.

For situations where Wiz finds a vulnerability, there is now an agent-based remediation feature that lets an agent generate a targeted remediation as a pull request.

The last piece addresses shadow AI. Wiz’s dynamic AI-BOM (AI Bill of Materials) aims to put an end to your unauthorized use of Claude Code and can automatically inventory every AI framework, model, and IDE extension across your environment. Given how fast AI coding tools are proliferating, an automated inventory is more or less a prerequisite for enforcing any coherent security policy around them.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://thenewstack.io/wp-content/uploads/2025/03/15a7eb12-cropped-4e88ac40-frederic-profile-2-600x600.jpg)

Before joining The New Stack as its senior editor for AI, Frederic was the enterprise editor at TechCrunch, where he covered everything from the rise of the cloud and the earliest days of Kubernetes to the advent of quantum computing....

Read more from Frederic Lardinois](https://thenewstack.io/author/frederic-lardinois/)