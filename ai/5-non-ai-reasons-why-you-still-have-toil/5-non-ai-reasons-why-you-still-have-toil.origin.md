# 5 Non-AI Reasons Why You Still Have Toil
![Featued image for: 5 Non-AI Reasons Why You Still Have Toil](https://cdn.thenewstack.io/media/2025/03/c3176c8c-wheel3-1024x576.png)
Toil — manual, repetitive tasks and sometimes dubbed “busy work” — had been steadily declining since 2020, thanks to automation and streamlined workflows. But [our annual SRE Report](https://www.catchpoint.com/asset/2025-sre-report) revealed a surprising reversal, as the median of time spent on toil has stopped improving in 2025 and actually rose back to 2023 levels.

![The SRE Report 2025: Toil levels rise](https://cdn.thenewstack.io/media/2025/03/edba79df-image1-3-1024x351.png)
The SRE Report 2025 Insight: Toil levels stopped improving. Is AI adding new demands?

With AI adoption accelerating, it’s easy to wonder if there is a cause-and-effect relationship. Headlines scream about automation replacing jobs, but engineers quietly grumble about the new toil it introduces — wrangling prompt chains, distracting us from the [technical debt that’s accruing or debugging hallucinated code](https://thenewstack.io/how-frontend-devs-can-take-technical-debt-out-of-code/). As one DevOps engineer put it, “I spend more time fixing AI’s ‘creative’ infrastructure templates than I ever did writing my own.”

However, the report offers a different perspective. Citing findings from the [2024 DORA Report](https://dora.dev/research/2024/dora-report/), it suggests that while AI accelerates value delivery, organizations often fill newfound capacity with more tasks. Convenient, perhaps, but let’s not ignore the elephant in the server room: toil predates ChatGPT.

Think back to the 2010s when *“*cloud migration*”* meant manually rebooting servers at 2 a.m. Or the Excel jockeys of the pre-automation era, endlessly updating spreadsheets. Toil has always been a shape-shnifter, thriving on organizational inertia.

Before blaming AI, let’s examine five credible, non-AI reasons for toil’s resurgence and what you can do about them.

## 1. The ‘Always-On’ Collaboration Trap
Modern work is a circus of fragmented tools. Slack pings! Teams alerts! Calendar pop-ups! We spend hours context-switching, chasing approvals or reconciling conflicting updates across platforms. What’s [automated in theory becomes manual in practice](https://thenewstack.io/how-to-mature-your-devops-automation-practices/) — toil disguised as productivity. According to [Asana’s Anatomy of Work Index](https://www.inc.com/rebecca-deczynski/asana-anatomy-of-work-index-meetings-remote-work-efficiency.html), employees spend nearly 60% of their time on “work about work,” leaving only 27% for skilled work and 13% for strategic planning.

What you can do:

**Streamline collaboration tools**: Declare war on “work about work.” Audit tools — do you really need 14 Slack channels for “urgent-urgent”? Enforce “quiet hours” for deep work.**Automate coordination**: If a Jira ticket moves to “done,” let Zapier tell Slack. Humans have better things to do.
## 2. The Rise of ‘Shadow IT’
Teams often adopt unauthorized tools and SaaS applications without central oversight, leading to siloed systems that require manual data transfers and reconciliation. Marketing uses Airtable. Sales swears by Notion. Engineers are wed to Coda. None speak the same language. Suddenly, you’re playing data janitor, copy-pasting like it’s 1999.

Worse, some of these tools aren’t just unsanctioned — they aren’t even known to IT until they cause a disruptive [manual] hullabaloo. A study by Software AG revealed that half of all employees are using unauthorized AI tools, commonly referred to as “[shadow IT](https://thefutureofwork.pro/study-finds-half-of-employees-using-unauthorised-ai-tools/).”

**What you can do:**
**Ensure the shadows of shadow IT are not hallucinations:**Identify and evaluate all unauthorized apps currently in use, removing redundant tools. Be prepared to find tools that actually provide value that IT never considered.**Build a self-serve platform:**Offer teams pre-approved and integrated solutions to reduce rogue SaaS adoption. This has platform engineering vibes — creating a structured environment where teams can move fast without creating integration chaos.
## 3. Fear-Driven Bureaucracy Creep
Risk-averse organizations layer on approvals, audits, and documentation to mitigate IT DevOps incidents. A code deployment now requires five sign-offs, a manual log and a post-mortem for a typo fix — toil masquerading as governance.

**What you can do:**
**Embed**[Internet Performance Monitoring](https://www.catchpoint.com/internet-performance-monitoring)**(IPM) into your life cycle:**Gain full visibility into external dependencies, detect issues before they escalate and resolve incidents faster, reducing the need for excessive approvals and manual oversight.**Adopt blameless post-mortems**: Foster a culture that learns from incidents rather than assigning blame, allowing for streamlined processes.
## 4. Technical Debt Continues To Accrue Interest
Many organizations still rely on outdated legacy infrastructure, creating friction with modern cloud native tools. This misalignment often leads to manual interventions to bridge technological gaps.

**What you can do: **
**Prioritize “strangler fig” modernization**: Gradually replace legacy components with microservices while keeping core systems running.**Embed a center of excellence for monitoring.**Depending on where your organization is on the digital transformation or modernization curve, you’ll want a center of excellence focused on monitoring or observing the[end-user experience](https://www.catchpoint.com/blog/mastering-ipm-monitor-what-matters-from-where-it-matters)to minimize impact while going through these changes.**Invest in Interoperability**: Use APIs or middleware (such as MuleSoft) to bridge old and new systems, reducing manual glue work.
## 5. The ‘Quick Fix’ Culture
Under pressure to deliver immediate results, teams often take shortcuts — choosing manual workarounds instead of long-term automation. A study by [Stripe](https://www.pullrequest.com/blog/cost-of-bad-code/#:~:text=A%20recent%20study%20from%20Stripe,code%20that's%20difficult%20to%20maintain.) found that developers spend approximately 42% of their time on maintenance activities**,** reducing their ability to focus on innovation.

**What you can do: **
**Incentivize reliability.**Set team and leadership[goals tied to measurable reductions in manual tasks](https://thenewstack.io/set-goals-and-measure-progress-for-effective-ai-deployment/).**Allocate “shift-wide” automation sprints.**Instead of debating “shift left” or “shift right,” adopt a “shift-wide” approach, dedicating at least 10% of engineering cycles to automating manual tasks across the entire CI/CD life cycle. A[shift-wide approach](https://thenewstack.io/monitoring-developer-metrics-team-approach-is-best/)forces teams to work together, aligning efforts across the pipeline rather than optimizing in silos. The result is a system that becomes more efficient as a whole, rather than just improving individual pieces*.*
## Is AI the Villain — Or Just a Mirror?
The data is clear: Toil is rising. But why? Is AI the culprit, or is it simply holding up a mirror to habits we’ve ignored for years — quick fixes, bureaucratic bloat and legacy systems held together by digital duct tape?

The SRE Report 2025 doesn’t settle the debate. It does, however, remind us that toil thrives in ambiguity. Whether AI amplifies existing inefficiencies or creates entirely new ones depends on how we wield it. Fix the culture. Automate ruthlessly. And for the love of productivity, delete half your Slack channels.

For those craving fewer metaphors and more data, [download the full report.](https://resources.catchpoint.com/hubfs/Website%20Assets%20-%20Briefs%2c%20EBooks%2c%20etc/The%20SRE%20Report%202025%20Catchpoint.pdf?_gl=1*174s7pu*_gcl_au*MTcyMzc5MzIwMC4xNzM5NTUwMzk2)

[
YOUTUBE.COM/THENEWSTACK
Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.
](https://youtube.com/thenewstack?sub_confirmation=1)