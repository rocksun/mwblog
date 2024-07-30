# Platform Teams Win Over Devs With Quick Wins
![Featued image for: Platform Teams Win Over Devs With Quick Wins](https://cdn.thenewstack.io/media/2024/07/e8e8e388-platformteamswinoverdevsquickwins2-1024x576.jpg)
As a product leader in Software as a Service (SaaS) startups for over a decade, I’ve come to love the final day of a company hackathon when everyone demos what they worked on that week and describes how it helped a customer, the company or themselves. It’s fascinating to learn which efforts captured the attention and praise of folks throughout the business.

Let me tell you about the one and only time I’ve seen a full standing ovation (in person and virtually) after a hackathon presentation. The ovation was for a newly formed platform engineering team created to remove the friction of building and deploying software for teams building marketable features.

During the hackathon, this platform team reviewed cycle times and performance metrics and identified consistent delays in our software deployment process. They also created a developer experience (DevEx) survey to collect qualitative feedback from each of our 14 engineering teams. From this data, the team prioritized the top three actions that would improve DevEx and that could also be shipped within five working days.

At the hackathon demo, the team demonstrated the process, the top developer challenges and the quick-win platform changes they implemented — to the audience’s roaring appreciation. In a short week, they demonstrated how quick wins focused on experience could result in meaningful gains in metrics for development productivity and developer happiness. The platform team was truly serving their customers — our company’s engineering organization — in a way that created trust, transparency and results.

The emergence of platform teams is a familiar story in 2024, and industry reports confirm that building a dedicated platform team remains a current priority for software organizations of all sizes, even though adoption and practices have been found to be quite immature across the industry. Gartner predicts that by 2026, approximately [80% of software engineering companies may incorporate platform teams](https://www.gartner.com/en/infrastructure-and-it-operations-leaders/topics/platform-engineering) as internal contributors of reusable services, components and tools for application delivery. In June, the analyst firm released the first edition of the [Hype Cycle for Platform Engineering](https://www.gartner.com/en/documents/5519995).

The platform strategy is benefiting organizations — [HashiCorp](https://www.hashicorp.com/?utm_content=inline+mention)’s [2024 State of Cloud Strategy Survey](https://www.hashicorp.com/state-of-the-cloud) reports a 2x greater likelihood that high-maturity organizations have standardized on platform teams. Modern organizations seeing the highest benefits have embraced self-service developer platforms to continually improve developer experience, productivity, quality and compliance. Automation that frees developers to focus on business logic, which enables faster shipping of work important to their customers, deserves a standing ovation.

Read on for some actionable investments and recommendations for organizations to move forward in realizing the full potential of their platform teams. Taking inspiration from the hackathon ovation, I’ll focus on efforts that can be implemented quickly to spark new wins that lead to prolonged trust and success.

## Look for Opportunities to Spike Adoption
Platforms are only as successful as their adoption and consistent usage. Platform teams can take on a ton of varied responsibilities across the entire development life cycle, from creating internal developer platforms (IDPs), configuring and provisioning resources, centralizing security and compliance, managing deployment pipelines, and simplifying operations and monitoring.

However, investing in quick wins aimed at capturing the minds and hearts of your developers is a remarkably effective way to increase adoption. I’ve seen firsthand how a proof of concept (PoC), [minimum viable product (MVP)](https://thenewstack.io/2-ways-to-accelerate-developer-productivity/) or hackathon creates long-term interest, excitement, recognition and usage.

Here are a few examples of platform investment categories to analyze for quick wins:

### Self-Service
Give developers [freedom](https://thenewstack.io/infrastructure-from-code-gives-ops-needed-freedom) to directly access, provision and manage resources without relying on the platform team. Collaborate on high-value decisions and activities rather than gates that don’t add value. A common starting point is to inventory what developer platform capabilities are available as self-service today and identify what is missing. A more advanced consideration is adding automation software to existing workflows that can extract and document infrastructure runtime requirements every time a modification is made.

### Golden Paths
Provide guardrails around development environments, services and configurations, and best practices around tagging, logging, and identity and access management (IAM) policies to [deliver consistent](https://thenewstack.io/nitric-and-the-rise-of-infrastructure-automation-in-platform-engineering/), high-quality software. Evaluate highly used infrastructure configurations and consider creating [Infrastructure as Code (IaC)](https://thenewstack.io/infrastructure-as-code/) template libraries and developer portals — or go a step further and automate them directly from the developers’ code.

### Automation
Automate routine tasks like setting up environments, configuring API gateways, provisioning cloud resources and deploying applications. Analyze your CI/CD pipeline to identify common delays or manual steps that automation can improve. This allows developers to focus more on writing code for the business needs. Automate deployment processes to create consistent and fast deployments to testing and production environments and remove costly delays and blockers to shipping quality software.

### Local Development
Simulate the approved cloud environments locally to allow developers to debug and test business logic quickly. With cloud development, it’s common to hear developers struggling with long deployment cycles that greatly hinder their ability to code, debug and deploy quickly. Reducing feedback cycles can have a huge impact on productivity and DevEx. The key to this experiment is simplicity: Developers must be able to establish their local environments effortlessly without overly disrupting the rest of the team.

These investments above have a common theme: They contribute to a more productive and satisfying DevEx, which is the key to successful platform adoption. Let’s dig into how you can identify quick DevEx wins by enabling faster innovation and software delivery.

## Try an Infrastructure DevEx PoC
Our hackathon platform team demonstrated how to focus on what developers value. Developers want processes and tooling that allow them to be productive and focused.

In my role at [Nitric](https://nitric.io/), I often hear that cloud and infrastructure complexity is the biggest issue affecting developer productivity. In many organizations, IaC and similar approaches require developers to understand cloud infrastructure providers’ constant evolution, or they rely heavily on communication, separation of duties and coordination with the platform team. This friction can have a big impact on DevEx, and therefore adoption.

Automating infrastructure configuration and provisioning helps developers quickly adopt new tooling and processes. It can be tempting for platform teams to focus on governance, process and monitoring, which are all critical to the platform team’s value. However, consistently checking and improving DevEx is the key to promoting adoption of the platforms you are building.

Try creating a PoC around a common platform monitoring tool to assess the likely impact on DevEx and outcomes. The PoC should be accomplishable within a single sprint.

For example, try an uptime monitoring tool for checking website or service availability. This solution is bite-sized while still somewhat complex to configure correctly in the cloud. It uses resources such API gateways, compute, messaging events, scheduled tasks and a key value store.

This [uptime monitoring guide](https://nitric.io/docs/guides/nodejs/uptime) is a great starting point to accomplish a quick win for your organization. It provides step-by-step instructions on developing the frontend and backend for this application using Node.js.

The tool enables developers to:

- Build new applications quickly in the language they prefer.
- Immediately deploy using resources that the platform team governs.
## Level Up Your DevEx Metrics
How do you know if you’re improving the developer experience if you aren’t measuring the impact of your investments? As the hackathon team did, platform teams should regularly assess a combination of quantitative and qualitative metrics to understand and improve the developers’ effort to deliver.

Qualitative feedback from your developers likely already exists in a few places (e.g., Slack, GitHub, Jira, manager 1:1’s, company surveys). To build trust, analyze the information you already have for any actionable items. To level up, run regular developer feedback surveys to gather qualitative feedback on pain points, tool satisfaction and overall experience.

Alongside your qualitative feedback, pick the most relevant and available quantitative metrics to analyze. Here are a few examples of measurements we’ve seen help teams.

**Developer satisfaction scores:**Collect developer CSAT (Customer Satisfaction), NSAT (Net Satisfaction) or NPS (Net Promoter) scores to measure overall satisfaction with development systems and tools.**Focus time:**Measure the average number of days with sufficient focus time to assess developers’ ability to concentrate on their work without interruptions.**Deployment frequency:**Capture and analyze how often code is deployed to production to measure the efficiency of the development process.**Lead time:**Analyze the time it takes from code commit to code running in production to assess the speed of the development pipeline.**Change failure rate:**Measure the percentage of deployments that result in failures to evaluate code quality and testing effectiveness.**Adoption rate of tools and practices:**Create a historical analysis showing the percentage of targeted developers who actively use specific products, services or best practices.**Return on investment (ROI):**Quantify the benefits (time saved, increased productivity, reduced downtime, faster time to market, etc.) and identify the costs (platform team salaries, training, tooling, overhead, etc.). ROI = ((benefits – costs) / costs) * 100.
Analyze metrics in context to keep the whole picture in mind. The more you can easily measure and analyze, the more comprehensive your view of your DevEx. Then you can start conversations and drive improvements based on the actual and desired conditions of your developer community.

Staying consistent with measurement and iteration will earn the trust required to keep the teams engaged with your efforts, but even taking a small action this week will demonstrate transparency and empathy.

## Show the Way With Focus and Action
I hope this article inspires your next hackathon, PoC or MVP to accelerate your ability to make a positive impact for your developers. Prioritize quick wins that directly align to what developers want to improve or to avoid. Put measurements in place to consistently act on your developer community’s feedback loops. And check out [Nitric’s open source framework](https://nitric.io/docs) and [community](https://nitric.io/chat) to inspire or accelerate the next quick win for your team.

[
YOUTUBE.COM/THENEWSTACK
Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.
](https://youtube.com/thenewstack?sub_confirmation=1)