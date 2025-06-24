The AI security market is having its “emperor has no clothes” moment. According to Latio’s [Q2 2025 AI Security Market Report](https://pulse.latio.tech/p/2025-latio-ai-security-report), 93% of security professionals recognize [AI’s potential to enhance cybersecurity](https://thenewstack.io/navigating-the-turbulent-waters-of-ai-security/), but a staggering 77% of organizations feel unprepared to defend against AI-driven threats. More tellingly, when surveyed about their immediate AI security priorities, practitioners revealed a troubling disconnect between vendor messaging and real-world needs.

I’ve witnessed this disconnect firsthand through conversations with enterprise customers rushing to [deploy AI workloads](https://thenewstack.io/developers-are-embracing-ai-to-streamline-threat-detection-and-stay-ahead/). The patterns mirror what we saw during container adoption — [excitement trumping security](https://thenewstack.io/ai-is-changing-cybersecurity-fast-and-most-analysts-arent-ready/), with painful lessons learned only after incidents occur.

## The Great AI Security Misdirection

Most AI security vendors are solving yesterday’s problems while tomorrow’s threats are already materializing. The report reveals that the majority of AI security solutions started by focusing on employee data loss prevention (DLP), essentially building fancy monitoring tools to watch what employees paste into ChatGPT. Others focus on AI “firewalls” that filter inputs and outputs of LLMs, which are useful but limited in scope. Meanwhile, the real risk is rapidly shifting toward AI applications that can access sensitive data and take actions on behalf of users.

This misdirection isn’t accidental. DLP-style solutions are easier to build and tap into CISOs’ familiar fear patterns. But as [Microsoft](https://news.microsoft.com/?utm_content=inline+mention) Copilot and [Google](https://cloud.google.com/?utm_content=inline+mention)‘s Gemini mature with built-in guardrails, these monitoring solutions are becoming commoditized.

The fundamental issue isn’t just about AI security tools; it’s about whether the underlying infrastructure can support secure AI workloads at scale. Many organizations are building AI applications on container foundations that were never designed for the isolation requirements that sensitive AI workloads demand.

## Where Infrastructure Meets AI Security Risk

The report’s most crucial insight centers on “application runtime protection” — the [security challenges](https://thenewstack.io/ai-agents-are-a-security-ticking-time-bomb/) that emerge when AI systems move beyond simple chatbots to become autonomous agents. Consider the risk evolution: A basic ChatGPT session carries minimal risk, but AI agents present entirely different threat landscapes. For example, AI coding assistants that can execute arbitrary code during development, or agents that query internal databases and trigger financial transactions. These scenarios demand infrastructure-level security controls.

Here’s where infrastructure decisions become critical. AI workloads processing sensitive data require the same kernel-level isolation that enterprises depend on for their most critical applications. The shared kernel model that many container-based AI deployments rely on creates attack vectors that simply can’t be adequately secured with application-layer protections alone.

According to [Microsoft’s 2024 container security overview](https://techcommunity.microsoft.com/blog/microsoftdefendercloudblog/new-innovations-in-container-security-with-unified-visibility-investigations-and/4298593), container-based workloads face growing security threats, with security teams often unable to track which containers are running or vulnerable at any given time. For AI workloads handling sensitive data, these visibility gaps become critical vulnerabilities.

## Infrastructure Requirements AI Workloads Actually Need

AI applications demand three infrastructure characteristics that traditional container deployments struggle to provide:

* **True isolation:** AI models processing proprietary data need kernel-level separation, not just namespace isolation. When an AI system can access customer records or financial data, shared kernel vulnerabilities become business-critical risks.
* **Performance without compromise:** AI inference workloads are latency-sensitive. The networking and I/O overhead inherent in many container architectures can make real-time AI applications unusable.
* **Dynamic resource allocation:** Unlike traditional applications, AI workloads have highly variable resource needs. Infrastructure that can dynamically allocate GPU and memory resources based on actual demand eliminates the massive overprovisioning waste that plagues standard container deployments.

## The Build vs. Buy vs. Wait Decision

The investment landscape tells a revealing story. While organizations are spending over [$320 billion on AI infrastructure](https://www.cnbc.com/2025/02/08/tech-megacaps-to-spend-more-than-300-billion-in-2025-to-win-in-ai.html) in 2025, the AI security market represents just $25 billion — a fraction focused on securing these massive infrastructure investments. This disparity highlights the gap between infrastructure spending and security preparation.

The answer to whether organizations should invest in dedicated AI security tools depends on your AI adoption velocity and infrastructure maturity. If you’re building AI applications that handle sensitive data, dedicated tools offer specialization that incumbents can’t match. But architecture decisions matter more than vendor selection. Organizations that build AI infrastructure with hypervisor-level isolation and secure multitenancy from the ground up have significant advantages over those trying to retrofit security into existing container deployments.

Traditional security vendors are rapidly adding AI capabilities, but they’re playing catch-up to solutions designed from the ground up for this threat landscape. The most effective approaches combine proven security principles, like hypervisor-based isolation, with modern implementations optimized for AI workload characteristics.

## Looking Into the Crystal Ball

Based on the report’s findings, three trends are emerging:

First, DLP-focused AI security will consolidate rapidly as platforms build native protections. Second, runtime application protection will drive the majority of market growth, with infrastructure security becoming a key differentiator. Third, “security by design” versus “security as afterthought” will separate market leaders from followers.

## What Organizations Should Do Now

The AI security market’s growing pains [mirror past technology adoption cycles](https://thenewstack.io/future-proofing-ai-repeating-mistakes-or-learning-from-the-past/). Organizations that will thrive are those that focus on their actual risk profile and infrastructure foundation rather than chasing security trends.

Start by asking these questions: Where is AI actually deployed in your organization? What data can it access? Can your current infrastructure provide adequate isolation for these workloads? The answers should drive your AI security strategy, not vendor marketing.

Apply time-tested infrastructure principles while adapting to AI’s unique requirements. Those who build secure, efficient foundations will outperform those who bolt security onto inadequate infrastructure.

The emperor may not have clothes, but recognizing that reality is the first step toward building AI security that actually works.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://thenewstack.io/wp-content/uploads/2025/06/3cbe6c56-cropped-297f9c4a-kaylin-trychon-600x600.jpg)

Kaylin Trychon is chief marketing officer at Edera and a seasoned cybersecurity executive specializing in cloud native security, threat intelligence and Kubernetes development. Prior to joining Edera, she held leadership positions at Chainguard and Google.

Read more from Kaylin Trychon](https://thenewstack.io/author/kaylin-trychon/)