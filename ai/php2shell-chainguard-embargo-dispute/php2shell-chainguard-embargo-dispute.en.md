**Did one of your favorite websites go dark on Wednesday?** Some did, as operators took services offline while they waited for fixes to [two critical flaws in PHP](https://thenewstack.io/ai-php2shell-disclosure-framework/), the language behind much of the web.

The precaution didn’t mean those sites were hacked. The holes themselves were bad news with a capital B. But the bigger long-term concern might be how the embargo on the patches was handled.

PHP powers roughly 70% of websites, but that figure describes PHP’s reach, not the number of vulnerable or compromised sites.

WordPress told site owners to update PHP; these flaws don’t require a WordPress update.

The flaws are CVE-2026-109618 and CVE-2026-109619. The PHP project’s fixed releases are 8.2.35, 8.3.36, 8.4.27 and 8.5.12; users of older PHP branches need a supported upgrade or a distributor’s backport.

The PHP security emergency, aka PHP2Shell, exposed more than dangerous bugs in a widely used language. The release also set off a dispute over coordinated disclosure and underscored the pressure on [open-source maintainers](https://thenewstack.io/php2shell-ai-vulnerabilities-maintainers/) as [AI-assisted researchers](https://thenewstack.io/anthropic-oss-scanner-vulnerabilities/) find and develop exploits faster.

The road to this emergency ran through OpenAI’s [Patch the Planet](https://openai.com/index/coordinated-disclosure-of-critical-vulnerabilities/) initiative. Working in that program, security firm Calif used GPT-5.6 Sol to find a route to remote code execution and reported it to PHP on August 11. OpenAI independently reported the same underlying issue that day; Wiz reported its findings on August 24. PHP’s maintainers led the fixes. They had spotted signs of the underlying out-of-memory problem in 2024, but its full impact became clear only this August.

> “This is about as broad as a critical vulnerability gets.”

“This is about as broad as a critical vulnerability gets,” [Moshe Siman Tov Bustan](https://il.linkedin.com/in/hexploit) of OX Security said in a statement. “If you have a publicly accessible PHP instance and haven’t patched it, start from the assumption that you’re exposed. If you find evidence of exploitation, assume compromise, not just exposure.”

OX Security CEO [Neatsun Ziv](https://www.linkedin.com/in/neatsun-ziv-ab7394) added: “This is what an internet-scale vulnerability looks like. When a flaw hits technology this ubiquitous, the blast radius isn’t one product or one industry. It’s the web itself.”

Behind those warnings, [open-source leaders](https://thenewstack.io/there-is-just-one-way-to-do-open-source-security-together/) are debating how the industry should respond when discovery outpaces remediation. *The New Stack* has reported on the flood of [AI-generated vulnerability reports](https://thenewstack.io/akrites-ai-vulnerability-reports/) facing maintainers; PHP’s case adds a dispute over whether an embargo still protected users once details began to leak.

## A disclosure dispute and an admission of failure

Before the patches were released, details of PHP2Shell began to leak. The PHP Foundation says two CVE IDs circulated on October 20, followed by an accidentally published proof-of-concept video.

Chainguard CEO and co-founder [Dan Lorenc](https://www.linkedin.com/in/danlorenc) then released patched container images more than six hours before the October 21 coordinated release. He says he believed reports of active exploitation justified the decision to break the embargo.

The speed concern is real: After WordPress released version 7.1.2 on September 22 to fix CVE-2026-87902, Patchstack observed probes against WordPress sites that same day and attempts to write files the next day.

That, by the way, is bad enough. But the WordPress episode doesn’t establish whether attackers successfully exploited these PHP flaws when Chainguard published its images.

## Why Lorenc jumped the clock

In an email to *The New Stack*, later reflected in his LinkedIn post, Lorenc said Chainguard independently discovered the same issue with its [testing harness](https://thenewstack.io/chainguard-mythos-security-harness/) and a frontier AI model prompted to “find bad vulnerabilities in PHP.”

Lorenc said Chainguard first heard on Friday, October 16, that a PHP issue was coming. It independently found the issue that night, received a full briefing on Saturday, October 17, and helped test fixes.

He said news began leaking Monday, October 19, and discussion intensified Tuesday night, when several vendors reported what they believed were exploits in the wild.

Lorenc wites that, after a video call with other researchers, he decided to ship the fixes and immediately notified the disclosure group. He said he believed the coordinated disclosure guidelines allowed early release when there was evidence of exploitation in the wild.

Lorenc said three considerations drove the decision. These were how easily Chainguard had independently discovered the vulnerability and built an exploit, how much information was already circulating about the vulnerabilities and fixes, and the evidence shared about active exploitation.

Chainguard made its patched images publicly accessible, rather than restricting them to customers. Lorenc acknowledged that the PHP Foundation disagreed with his decision.

They certainly didn’t agree. The [PHP Foundation’s account](https://thephp.foundation/blog/2026/10/21/todays-php-security-release-and-how-were-strengthening-php-security/) was blunter: “Chainguard unilaterally broke the embargo and published built images containing the fix.” It said Chainguard had received the patch early so customers could update at the agreed disclosure time.

In the foundation’s view, publishing the built images gave attackers a chance to study the fix while other PHP users were still waiting for patches.

> “We’re not always going to get it right, and not everyone is going to agree with our decisions.”

Lorenc wrote that he was sorry his decision added stress for PHP’s maintainers. “We’re not always going to get it right, and not everyone is going to agree with our decisions,” he said, adding that Chainguard’s goal was to protect the most people.

## What counts as an exploit?

The disagreement centered on what counted as evidence of active exploitation. Lorenc said other vendors had seen exploits in the wild. The PHP Foundation said its security team had not identified a functional exploit among the circulating proofs of concept at the time of release.

Amazon Threat Intelligence later reported an apparent exploit attempt against one of its honeypots on October 17 and more attempts early on October 21. Still, it said it was unclear whether those attempts would have succeeded on real systems.

The competing risks are clear. Yes, [holding an embargo](https://thenewstack.io/ai-php2shell-disclosure-framework/) gives distributors time to prepare updates together. And, true, releasing a fix early may protect users who can obtain it. But it also gives attackers clues while other PHP users are still waiting for patches.

## The capital-B problem underneath

The PHP Foundation also acknowledged a separate failure in its response. Developers noticed signs of the out-of-memory problem behind one CVE during a 2024 audit, but had not found a concrete route to remote code execution.

The foundation said competing fixes carried difficult compatibility and security trade-offs, and work repeatedly stalled. It called the delay “a structural failure” caused by its decision process and lack of resources.

*The New Stack* has previously reported on the link between [paid maintenance](https://thenewstack.io/open-source-paid-maintainers-keep-code-safer-survey-says/) and security practices. The foundation is now seeking more support from companies, hosts and governments that depend on PHP.

[Canonical](https://canonical.com/), [Ubuntu Linux](https://ubuntu.com/)‘s parent company, offers a less critical assessment of the overall response. In an e-mail, [Luci Stanescu](https://ro.linkedin.com/in/lucistanescu), Canonical’s security engineering manager, says, “Canonical supports and recommends coordinated vulnerability disclosure according to best practices. The early embargo leak by a third-party was unfortunate, but we believe the disclosure process worked well.”

That assessment differs in emphasis from the PHP Foundation’s criticism: a leak can undermine part of the process without necessarily invalidating the broader coordination effort.

For CIQ Chief Technology Officer [Peter Nelson](https://www.linkedin.com/in/peter-nelson-774a6), whose company is Rocky Linux’s founding sponsor, the PHP episode fits a broader change already underway in Linux security.

“We have seen AI used in exploiting vulnerabilities in the kernel space for the past six months,” Nelson says. “This represents more research going into other widely used software programs like PHP. We expect to see more of it as open-source projects continue to use AI and other means to harden the code and provide a greater defense against vulnerabilities like this.”

> “Today, such vulnerability exploitation requires a frontier model. Tomorrow that won’t be the case.”

Nelson expects that pressure to continue as advanced vulnerability-research capabilities become more accessible. “Today, such vulnerability exploitation requires a frontier model. Tomorrow that won’t be the case.”

Lorenc also frames the challenge as an industry-wide problem rather than one confined to PHP. “This is unfortunately the new normal for the industry, and we’re going to need to work together as one team to have a chance at securing our critical infrastructure fast enough to stop attackers from causing real harm.”

## Patching cannot wait for the usual maintenance window.

For enterprise users, the immediate consequences are operational. [Gunnar Hellekson](https://www.linkedin.com/in/gunnarhellekson), Red Hat’s vice president and general manager for Lightwell, a joint Red Hat–IBM effort to address vulnerable [open-source dependencies](https://thenewstack.io/aikido-acquires-root-security/), tells *The New Stack* in an email that the PHP flaws illustrate the risk in dependable software that organizations may rarely think about.

Hellekson said that stable production software can be easy to overlook even as AI-driven discovery increases the volume and speed of vulnerability findings. The PHP issues, he said, remind us how deeply open source is woven into the systems that run businesses.

He emphasized getting tested updates from trusted suppliers, especially when vulnerabilities affect vital programs like PHP. “Given the potential impact of these vulnerabilities, Red Hat recommends that customers deploy validated, tested patches as soon as they are available from trusted sources including Red Hat, even outside of normal patching windows.”

> “Software that supports millions of websites cannot depend on a handful of maintainers to manage increasingly sophisticated threats alone.”

Beyond that, we need more resources, in general, for [open-source software maintenance](https://thenewstack.io/security-needs-create-more-work-for-open-source-maintainers/) and security. As [Kara Sprague](https://www.linkedin.com/in/ksprague08), CEO of [HackerOne](https://www.hackerone.com/), says in a statement sent to the media, “The PHP discoveries are also a reminder that open-source security is everyone’s responsibility. Software that supports millions of websites cannot depend on a handful of maintainers to manage increasingly sophisticated threats alone.”

No, no it can’t.

For organizations running affected PHP systems, the “patch it right now!” problem remains: deploy a fixed build and review systems for signs of attempted exploitation, including activity dating back to October 17.

This is where the competing assessments converge. Better-funded maintainers, more resilient disclosure procedures, and broader access to defensive tools could address the longer-term problem. And that’s the capital-B problem underneath this week’s patch.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://cdn.thenewstack.io/media/2023/03/cee63948-cropped-8a0b5c52-steven-vaughan-nichols.jpg)

Steven J. Vaughan-Nichols, aka sjvn, has been writing about technology and the business of technology since CP/M-80 was the cutting-edge PC operating system, 300bps was a fast internet connection, WordStar was the state-of-the-art word processor, and we liked it.

Read more from Steven J. Vaughan-Nichols](https://thenewstack.io/author/sjvn/)