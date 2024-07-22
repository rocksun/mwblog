# 7 Urgent Lessons from the CrowdStrike Disaster
![Featued image for: 7 Urgent Lessons from the CrowdStrike Disaster](https://cdn.thenewstack.io/media/2024/07/5ef24021-the-crowdstrike-disaster-lessons-2-1024x576.jpg)
Sitting here on my [Linux](https://thenewstack.io/linux/) desktop, with my Linux servers humming away in the background, the [CrowdStrike crash ](https://www.crowdstrike.com/blog/statement-on-falcon-content-update-for-windows-hosts/)didn’t affect me directly. Like pretty much everyone else on the planet, indirectly, it was another story.

Work buddies were stuck in airports. Colleagues, 48 hours after the incident, were still repairing one defunct Windows system after another, and friends had to use cash to buy groceries.

None of this had to happen.

“This is a reminder that we live in an increasingly digital world in which software underpins nearly every facet of our lives — from transportation and emergency services to banking, retail and even food services,” noted [Jason Schmitt](https://www.linkedin.com/in/mjasonschmitt/), general manager of the [Synopsys](https://www.synopsys.com/software-integrity.html?utm_content=inline+mention) Software Integrity Group in a statement released to the news media. “Software problems can lead to severe business problems–and, in some cases, problems that impact many of the necessities consumers take for granted.”

Let me repeat: None of this. Let me count the lessons.

## 1. Monocultures Are Dangerous.
Whether it’s potatoes in Ireland during the Great Famine, which brought my ancestors to the U.S., cotton in the American South before boll weevils showed up, or Windows, anytime everyone relies on a single system, you’re asking for trouble.

By [Microsoft’s](https://news.microsoft.com/?utm_content=inline+mention) low count, only [8.5 million Windows devices, or less than one percent of all Windows machines, were affected](https://blogs.microsoft.com/blog/2024/07/20/helping-our-customers-through-the-crowdstrike-outage/). But those numbers don’t tell the whole story.

By the count of [6sense.com](http://6sense.com/), the business data analysis company[,](http://6sense.com/) [CrowdStrike](https://www.crowdstrike.com/?utm_content=inline+mention) is [the No. 1 business endpoint security company](https://6sense.com/tech/endpoint-protection/crowdstrike-market-share) with over 3,500 customers. That may sound small, but it includes one in four companies that use endpoint security. These tend to be major businesses. So, while small in terms of the sheer number of systems stuck in endless reboots, the effects were massive.

“The scale of this outage highlights the risks associated with over-reliance on a single system or provider,” said [Mark Boost](https://www.linkedin.com/in/markboost), CEO of cloud computing company [Civo](https://www.civo.com/), in a statement released to the news media. “It’s a sobering reminder that size and reputation do not guarantee invulnerability to significant technical issues or security breaches. Even the largest and most established companies must be vigilant, continuously updating and securing their systems.”

## 2. Bad Code Is Dangerous Code.
According to one popular theory proposed on X by [Evis Drenova](https://www.linkedin.com/in/evisdrenova/), CEO of [NeoSync](https://www.neosync.dev/), a developer tool company, the root cause of the disastrous security update to its Falcon Sensor program was a [null pointer error ](https://x.com/evisdrenova/status/1814355536152015094)in its [C++ code](https://thenewstack.io/google-spends-1-million-to-make-rust-c-interoperable/). [CrowdStrike appears to deny this.](https://x.com/patrickwardle/status/1814583925223678281/photo/3)

[Tavis Ormandy](https://github.com/taviso), the well-known [Google](https://cloud.google.com/?utm_content=inline+mention) vulnerability researcher also disagrees [ via an X tweet](https://x.com/taviso/status/1814762302337654829). Ormandy and
[Patrick Wardle](https://www.linkedin.com/in/patrick-wardle-34580581/), creator of the Mac security website and tool suite
[Objective-See,](https://objective-see.org/)who also weighed in on X, suspect the
[blame goes to a logic error](https://x.com/patrickwardle/status/1814583573111812304).
Eventually, we’ll find out exactly what went wrong, but there can be no question whatsoever that this lousy code should never, ever should have been shipped to a customer.

## 3. Quality Assurance Is Absolutely Necessary.
This problem started at CrowdStrike. How the company’s quality assurance (QA) team ever let this update out the door is a question that will likely lead to numerous people being fired soon.

They’re not the only ones who should get the blame for this step towards disaster, though.

In a presentation at Open Source Summit North America in Seattle this past April, [Jack Aboutboul](https://www.linkedin.com/in/jackaboutboul/), senior project manager at the Microsoft Linux Platforms Group, discussed the “[lazy sysadmin](https://www.youtube.com/watch?v=ZOUlZ5s8XkI&t=854s)” problem. The stereotypical lazy admin installs software, turns on automatic updates and deals with the latest urgent problem. That’s fine… until one of the updates crashes the system.

They should be testing each new patch when it comes in. In his presentation, Aboutboul was talking about Linux distro updates, but the same idea applies to all mission-critical software.

As [Konstantin Klyagin](https://www.linkedin.com/in/thekonst), a founder of [Redwerk](https://redwerk.com/) and [QAwerk](https://qawerk.com/), both software development and QA agencies, pointed out in a statement released to the news media, “Automated testing ensures that even minor changes don’t introduce new bugs. This is particularly important for large-scale updates, like the one from CrowdStrike, where manual testing alone would be insufficient.”

Who doesn’t do this!? It would appear at least some companies still don’t.

Did that many organizations really fail this basic step? Some suggest that CrowdStrike is to blame because this security data [patch “was a channel update that bypassed client’s staging controls](https://www.resetera.com/threads/windows-blue-screen-of-death-bsod-happening-worldwide-right-now-up-caused-by-crowdstrike-falcon-sensor-see-threadmarks.931566/page-17?post=126020565#post-126020565) and was rolled out to everyone regardless” of whether they wanted it or not.

By bypassing the client’s rollout controls, far more companies were damaged. This strikes me as all too likely since so many businesses were smacked by this failure. Again, the problem remains: “Why would anyone let such a critical patch be deployed without question?”

## 4. Staged Rollouts Avoid Catastrophe.
A related production problem is that many organizations have simultaneously rolled out their updates to all their systems. This is such a basic blunder; it should never happen, but here we are

Yes, there are arguments against staged rollouts — users can be confused when different teams are working with various versions. But when it comes to mission-critical systems where failure is unacceptable, you need to exercise extreme caution with any upgrade.

Besides, there are [many ways to do a staged rollout](https://thenewstack.io/5-deployment-strategies-the-pros-and-cons/). They include rolling updates, [blue/green, canary](https://thenewstack.io/primer-blue-green-deployments-and-canary-releases/), and A/B testing. Pick one. Make it work for your enterprise, just don’t put all your upgrades into one massive basket.

Besides, robust rollback procedures are essential to revert to a stable version if problems arise quickly. Wouldn’t you have liked just to hit a button and roll back to working systems? Tens of thousands of IT staffers must wish for that now.

## 5) Disaster Recovery and Backups Are Must-Haves.
This should go without saying, but you must have a [disaster recovery plan](https://thenewstack.io/supercharge-your-disaster-recovery-plan-in-5-simple-steps/) and trustworthy backups.

“I’ve talked to several CISOs and CSOs who are considering triggering restore-from-backup protocols instead of manually booting each computer into safe mode, finding the offending CrowdStrike file, deleting it, and rebooting into normal Windows,” said [Eric O’Neill](https://www.linkedin.com/in/eric-m-oneill/), a public speaker and security expert in a press statement. “Companies that haven’t invested in rapid backup solutions are stuck in a Catch-22.”

Indeed, they are. True, in these days of [cloud computing, disaster recovery, and backups aren’t as simple as they used to be](https://thenewstack.io/k8s-backup-and-disaster-recovery-is-more-important-than-ever/). But they’re vitally important. And, in this case, old-school disaster recovery methods and backups would have been a major help.

## 6. You Need Enhanced Monitoring and Incident Response.
The outage’s global scale highlights the need for advanced monitoring tools and robust incident response plans. Real-time monitoring and alerting systems should be in place to catch issues as they occur. IT teams should develop detailed incident response plans with clear protocols for quick identification, isolation and resolution of issues. These plans should include root-cause analysis and [post-incident reviews](https://thenewstack.io/top-12-best-practices-for-better-incident-management-postmortems/) to improve response strategies continuously.

That’s easier said than done.

“Navigating the challenges of today’s digital era requires businesses to have proactive and practical strategies to mitigate outages and ensure resilience,” said [Spencer Kimball](https://www.linkedin.com/in/spencerwkimball), [Cockroach Labs](https://www.cockroachlabs.com/)‘ CEO, and co-founder observed, in a statement released to the news media.

He added, “Outages are not a problem we’re going to solve completely. Cloud environments are only growing more complex and interconnected. This complexity at scale will continue to increase risk, particularly for businesses still in the initial stages of cloud adoption. Continuous monitoring and alerting are essential to detect and address issues before they escalate.”

Kimball’s thoughts were echoed by Anthony Falco, vice president at [Hydrolix](https://hydrolix.io/), a company working on real-time query performance in an e-mail to The New Stack.

“The massive outage underscores the new reality companies face: Globally distributed software platforms that drive business today are a complex web of interdependencies, not all under any one actor’s control,” Falco said. “A modest mistake can literally grind global business to a halt.

“We need a new approach to [observability](https://thenewstack.io/observability/) — one that is real-time and can simplify the management of tremendous volumes of data streaming from myriad sources so events can be detected and mitigated before they spread.”

## 7. Get Ready Now for the Next Time.
The CrowdStrike/Windows incident is a stark reminder that even routine maintenance can lead to significant disruptions if not managed properly. It highlights the interconnected nature of modern IT systems and the far-reaching consequences of failures in widely used software.

By learning from this event and implementing robust risk management strategies, IT teams can better prepare for and mitigate the impact of similar incidents in the future.

We need to do better. We must do better. I’m old enough to have fought off the first major, widespread security problem, 1988’s [Morris Worm](https://www.zdnet.com/article/the-day-computer-security-turned-real-the-morris-worm-turns-30/). Then, technology problems only bothered those working in tech. We’ve gone long past those days.

[
YOUTUBE.COM/THENEWSTACK
Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.
](https://youtube.com/thenewstack?sub_confirmation=1)