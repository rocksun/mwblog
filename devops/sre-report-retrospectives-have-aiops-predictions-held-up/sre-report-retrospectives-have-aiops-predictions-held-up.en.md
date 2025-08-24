Each year, Catchpoint attempts to capture the pulse of the global reliability community in its [SRE Report](https://www.catchpoint.com/asset/2025-sre-report). It surveys hundreds of site reliability engineers (SREs), reliability engineers and operations leaders worldwide [to understand the current state of the profession:](https://www.catchpoint.com/sresurvey2025?&utm_source=alert_banner&utm_medium=referral&utm_campaign=Content-2025-07-hosted-SRE-Survey&utm_content=survey) the challenges faced, the tools used and the trends shaping the practice. The reports serve as both a snapshot of where the industry stands and a compass for where it’s heading.

But here’s the thing about predictions: They have this pesky habit of aging poorly. Technology evolves, markets shift and what seemed revolutionary three years ago might be gathering dust in the corner of someone’s Kubernetes cluster today.

So, as authors of the SRE Report, we thought it would be fascinating — and perhaps a little humbling — to revisit our past claims and see how they’ve held up against the brutal reality of production environments.

While the SRE Report covers a broad spectrum of topics, from chaos engineering to monitoring best practices, we’re focusing on [AIOps](https://thenewstack.io/what-is-aiops-and-why-you-should-care/) in this piece, a topic first explored in the 2021 report. It has become one of the most discussed, debated and some would argue, transformative concepts in IT operations. So how did those early predictions hold up?

## **AIOps: The Promise That Wouldn’t Die**

Let’s start with a bit of history. Garner coined the term “AIOps” in 2017, defining it as the application of artificial intelligence and machine learning (ML) to [enhance IT operations](https://thenewstack.io/why-aiops-failed-and-event-intelligence-solutions-are-different/) through big data, analytics and automation. Gartner positioned it as the future of IT operations — a way to handle the exponential growth in data volume, velocity and variety that traditional monitoring tools simply couldn’t manage.

The promise was intoxicating: Imagine AI systems that could automatically detect anomalies, correlate events [across your entire stack](https://thenewstack.io/devops-embraces-observability-across-stacks-for-llm-era/), predict failures before they happened and even remediate issues without human intervention. It sounded like the holy grail of operations. Finally, we could move from reactive firefighting to proactive, intelligent infrastructure management.

## **What We Said Then: The SRE Report Take on AIOps**

### **2021: Cautious Optimism Meets Cold Reality**

The [2021 SRE Report](https://pages.catchpoint.com/hubfs/Report/Catchpoint-2021-SRE-Report.pdf?_gl=1*jj0tkv*_gcl_au*MzE4OTA3NDc5LjE3NTE0NTAzNDk.) gave AIOps significant attention, reflecting the industry enthusiasm we were seeing everywhere. The potential was undeniable — AIOps promised to help SREs manage increasing data volumes and extract actionable insights that could transform the way we approached monitoring and incident response.

But here’s where it got interesting: While the industry was buzzing with excitement, survey respondents told a different story. Real-world adoption among SREs was surprisingly slow. The gap between promise and practice was significant.

[![Monitoring tool usage: The SRE Report 2021](https://cdn.thenewstack.io/media/2025/08/ca61e7a0-image2a-1016x1024.png)](https://cdn.thenewstack.io/media/2025/08/ca61e7a0-image2a-1016x1024.png)

Monitoring tool usage: The 2021 SRE Report.

The report’s recommendation then was pragmatic: Break down AIOps into individual components rather than chasing the buzzword. Don’t buy into the hype wholesale; instead, evaluate specific capabilities like anomaly detection, event correlation or automated remediation on their own merits. The report also emphasized the need for AI and ML training within SRE teams, positioning this as a long-term investment rather than a quick fix.

### **2023: The Plot Thickens**

[![The SRE Report 2023](https://cdn.thenewstack.io/media/2025/08/7c196688-image3-1024x561.png)](https://cdn.thenewstack.io/media/2025/08/7c196688-image3-1024x561.png)

By the time the [2023 SRE Report](https://resources.catchpoint.com/hubfs/eBooks/SRE%20Report%202023%20Catchpoint.pdf?_gl=1*2gzok6*_gcl_au*MzE4OTA3NDc5LjE3NTE0NTAzNDk.) rolled around, we had additional data to work with. We asked respondents to rate the “value received” from AIOps for a second year running, and the results were illuminating.

The majority of reliability practitioners continued to report that the value they received from AIOps was low or nonexistent. But here’s where it got really interesting: When we broke down responses by organizational level, a fascinating pattern emerged. Fifty-nine percent of executives said they received moderate or high value from AIOps, while only 20% of individual practitioners said the same.

Read that again. Let it sink in.

[![Value received from AIOps: The SRE Report 2023](https://cdn.thenewstack.io/media/2025/08/356c15bd-image4a-1024x781.png)](https://cdn.thenewstack.io/media/2025/08/356c15bd-image4a-1024x781.png)

Value received from AIOps: The 2023 SRE Report.

We had a classic case of the people making the purchasing decisions seeing tremendous value, while the people actually using the tools in production were largely unimpressed. The [gap in perception between leadership and practitioners](https://www.catchpoint.com/blog/sre-report-2023-are-we-aligned-yes-no-maybe) was stark.

The report’s advice remained consistent: Don’t ignore AIOps entirely, but decompose it into specific capabilities that meaningfully support your observability and reliability operations. Focus on pragmatic use cases, not vendor promises.

### **2024-2025: The Pivot**

By 2024, something interesting happened. We broadened our survey questions from AIOps specifically to AI in general, adding qualifiers about expectations “within the next two years.” This shift reflected the rapidly evolving AI landscape and the rise of generative AI (GenAI).

As one of our field contributors noted: “It’s hard to know whether this is another AI hype cycle or an intensification of the previous one, but it feels like there is something genuinely different between the (rather short on detail) promotion of AIOps, and what’s happening with GenAI.”

The distinction was crucial: Traditional AIOps remained narrowly focused on anomaly detection and analysis within existing command-and-control frameworks — essentially “business-as-usual, with go-faster stripes.” GenAI, however, represented something fundamentally different: “More like dealing with a very early-stage co-worker, who needs training and investment and constant review, but can occasionally be really valuable.”

## **That Was Then, This Is Now: Google Trends Reality Check**

So that was the take from the SRE trenches. But how do you actually measure adoption of something like AIOps in the broader market? It’s crude, but you could do worse than looking at [Google](https://cloud.google.com/?utm_content=inline+mention) search trend data.

Why Google Trends? Two compelling reasons:

* First, it tracks real search interest, not just hype. Google Trends shows how many people are actively searching for information on a topic — a direct window into what the market, professionals and the curious that want to learn or evaluate.
* Second, it’s unbiased and vendor-neutral. Unlike vendor surveys or analyst reports, Trends is independent. It’s not produced by a stakeholder seeking to sell or promote something. It reflects organic search behaviors from [millions of users](https://thenewstack.io/how-to-support-a-million-users-on-your-website-a-success-story/) across the world.

And here’s where things get very interesting.

## **AIOps: What We Learn From Google Search Trend Data**

### The ‘AIOps’ Search Interest Explosion (2024-2025)

The most striking finding is the dramatic spike in “AIOps” searches starting in late 2023/early 2024, reaching peak interest by 2025.

[![Global Google search interest over time for the term "AIOps" (August 2021 – August 2025)](https://cdn.thenewstack.io/media/2025/08/70885b4f-image5a-1024x564.png)](https://cdn.thenewstack.io/media/2025/08/70885b4f-image5a-1024x564.png)

Global Google search interest over time for the term “AIOps” (August 2021-August 2025).

Remember, this is happening after our SRE community had already concluded that AIOps delivered limited practical value.

### Regional Concentration in Asia-Pacific

[![Regional interest in "AIOps" based on global Google search volume (August 2021 – August 2025)](https://cdn.thenewstack.io/media/2025/08/75c68404-image6-1024x484.png)](https://cdn.thenewstack.io/media/2025/08/75c68404-image6-1024x484.png)

Regional interest in “AIOps” based on global Google search volume (August 2021-August 2025).

The geographic data reveals AIOps’ interest is heavily concentrated in:

* China (100% relative interest)
* Singapore, South Korea and Hong Kong (13-21% relative interest)

This suggests either different IT infrastructure challenges in APAC markets, varying technology adoption patterns or perhaps different expectations around AI-driven operations.

### The Educational Curve

[![Global Google search interest over time for the phrase "What is AIOps" (August 2021 – August 2025)](https://cdn.thenewstack.io/media/2025/08/558d1c8b-image7-1024x556.png)](https://cdn.thenewstack.io/media/2025/08/558d1c8b-image7-1024x556.png)

Global Google search interest over time for the phrase “what is AIOps” (August 2021-August 2025).

The “what is AIOps” search trend shows cyclical spikes rather than sustained growth, suggesting periodic waves of discovery rather than consistent adoption. People are still learning about AIOps rather than implementing it. The concept remains nascent despite years of industry discussion.

### **The October 2024 Inflection Point**

But here’s where the story gets really fascinating. Search interest for AIOps absolutely exploded in October 2024.

[![Inflection point in global search interest for "AIOps"—October 2024](https://cdn.thenewstack.io/media/2025/08/f7df4874-image8-1024x381.png)](https://cdn.thenewstack.io/media/2025/08/f7df4874-image8-1024x381.png)

Inflection point in global search interest for “AIOps” (October 2024).

What happened?

### **The Perfect Storm**

October 2024 created a perfect storm for AIOps interest:

* **Gartner Magic Quadrant for Digital Experience Monitoring report (Oct. 21, 2024):** For the first time, Gartner published a Magic Quadrant for Digital Experience Monitoring, which includes AIOps capabilities as evaluated criteria. Companies like Dynatrace and Catchpoint were named Leaders (yes, shameless plug, but we earned it), generating significant industry attention and validating the AIOps space.
* **IBM Cloud Pak for AIOps v4.7 release (Oct. 11, 2024):** IBM announced a major update with production-ready Linux deployment capabilities, signaling enterprise readiness.
* **Nokia’s AIOps integration (Oct. 18, 2024):** Nokia integrated AI-driven operations into its Altiplano Access Controller, showing AIOps expanding beyond traditional IT into network infrastructure.
* **ServiceNow educational push:** Dedicated AIOps workshops and training, indicating vendors were investing heavily in market education.
* **Multiple vendor milestones:** From Motadata’s next-gen platform to Keep raising $2.7M for its open source AIOps platform, the entire ecosystem seemed to mature simultaneously.

This convergence explains why Google Trends shows such a dramatic spike. October 2024 represented the moment when AIOps moved from “emerging technology” to “mainstream enterprise solution” with multiple validation points occurring simultaneously.

## And What Does the Market Actually Say?

The numbers are impressive: The [global AIOps market is expanding](https://www.gminsights.com/industry-analysis/aiops-market) at a compound annual growth rate of more than 25%, projected to grow from $11.16 billion in 2025 to over $32 billion by 2029. Around 40% of enterprises now employ AIOps to some extent, with adoption rates especially high in regulated and data-intensive industries.

But here’s the million-dollar question: Are we seeing hype cycles that don’t align with practitioner reality, or is the early promise of AIOps finally materializing?

## **What We Got Right (And What We Missed)**

Our 2021 and 2023 recommendations still hold water:

* **Break down AIOps into discrete components:** The market has largely validated this approach. Successful AIOps implementations focus on specific capabilities — anomaly detection, event correlation, automated remediation — rather than trying to solve everything at once.
* **Focus on pragmatic use cases:** Organizations seeing value from AIOps are those that identified clear, measurable problems and applied AI/ML tools strategically to solve them.
* **Invest in training:** The most successful teams we’ve observed have invested in AI and ML literacy for their SRE teams, treating it as a long-term capability rather than a silver bullet.

What we perhaps underestimated was the patience required for the market to mature and the role that broader AI developments (particularly GenAI) would play in legitimizing and advancing AIOps capabilities.

## **Write the Next Chapter**

The story of AIOps — and SRE in general — is still being written. That’s why your voice matters in the 2025 SRE survey. Each response helps us benchmark trends, surface emerging best practices and highlight the realities of reliability work across organizations of all sizes.

This year, we’re diving deeper into performance and reliability modeling, chaos engineering, observability practices, learning and upskilling and tooling strategy. The survey is voluntary, anonymous and takes about 10 minutes, yet the impact of your participation is profound.

Because the only way we can accurately reflect on today’s predictions is if we capture the ground truth of what’s actually happening in production environments around the world.

[Take the SRE Survey](https://www.catchpoint.com/sresurvey2025?&utm_source=thenewstack&utm_medium=referral&utm_campaign=Content-2025-07-hosted-SRE-Survey&utm_content=survey) and help us write the next chapter of this story.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://cdn.thenewstack.io/media/2025/01/c2903fbf-leo-vasiliou.jpg)

Leo Vasiliou is Director, Product Marketing, at Catchpoint. Leo grew up in technology operations where web performance, IT operations, and information security activities were part of his charter. Since transitioning to evangelizing DevOps activities in product marketing, Leo currently applies...

Read more from Leo Vasiliou](https://thenewstack.io/author/leo-vasiliou/)

[![](https://cdn.thenewstack.io/media/2025/07/361b4f6e-cropped-223b041a-image2.jpg)

Denton Chikura is an observability advocate focused on helping site reliability engineers and engineering teams discover the tools and capabilities that strengthen internet resilience. With a background at the intersection of monitoring, performance and infrastructure, he works to make complex...

Read more from Denton Chikura](https://thenewstack.io/author/denton-chikura/)