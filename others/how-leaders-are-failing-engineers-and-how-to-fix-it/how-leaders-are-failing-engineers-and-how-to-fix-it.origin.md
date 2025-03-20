# How Leaders Are Failing Engineers – and How To Fix It
![Featued image for: How Leaders Are Failing Engineers – and How To Fix It](https://cdn.thenewstack.io/media/2025/03/a85500b8-misalign4-1024x576.png)
Software engineering is undergoing rapid transformation with the rise of platform engineering and AI, yet one challenge remains consistent: the disconnect between software engineers and engineering leaders. This gap is more than just a perception; data confirms it. [The 2025 State of Internal Developer Portals report](https://www.port.io/state-of-internal-developer-portals?utm_campaign=The%20New%20Stack&utm_source=The%20New%20Stack&utm_content=disconnect), conducted by Global Surveyz on behalf of Port, found misalignment on productivity, standards and [data trust](https://thenewstack.io/wp-admin/post.php?post=22780926&action=edit). This disconnect stems across communication, priorities, expectations and technical decision-making.

## Misalignment Between Developers and Leaders
Eighty-one percent of engineers reported losing between six and 15 hours each week because they have to [constantly switch between numerous different tools](https://thenewstack.io/how-to-tackle-tool-sprawl-before-it-becomes-tool-hell/) to do their jobs. However, around a third of engineering leaders (33%) don’t recognize this loss, indicating that many managers may not fully realize how much inefficiency affects their teams daily.

A disconnect on standards was also highlighted in the report. When respondents were asked if software complies with organizational standards, 25% of leaders expressed doubt, compared to just 4% of engineers. This may be because leaders are more focused on overall outcomes and compliance with organizational standards and have a better view of how compliant software is.

However, only 15% of developers stated that they had clarity on the standards required by different domain owners. Without clear standards, engineers may struggle to align with expectations, leading to inconsistencies in software development and increased risks related to regulatory, security and quality requirements.

Additionally, engineering managers tend to trust their data more than engineers do. The report found that 54% of engineers feel that data collected in existing, centralized repositories are not trustworthy, compared to only 44% of engineering leaders. Since engineers are more exposed to the fallout of unreliable data, they tend to be more skeptical. A lack of quality data increases developer and manager overhead; for instance, if service ownership or AppSec data is not up to date, it can lead to inefficient workflows — or worse still, missing a security gap.

The difference in trust itself can cause issues too; when alerts are false positives and leaders are unaware of this, it can lead to disagreements about priorities in alerts or issue triaging, or lead to an unnecessary investigation launched into known issues. Overall, this reflects a broader communication gap between leaders and engineers.

## Why Does This Disconnect Exist?
One key reason for the disconnect is that engineering managers are removed from the day-to-day operations of software development. The reality is that much of their time is spent dealing with escalations, in meetings and on strategic work. This lack of time in the coding trenches means they’re unable to grasp the everyday struggles of their team. Their responsibilities revolve around strategy, team management and translating technical objectives into business outcomes. To fulfill their roles, they rely on metadata from various sources to report to leadership and track progress. They trust this data because they must — without it, they cannot make informed decisions.

Engineers, on the other hand, interact directly with the systems and tools that generate this metadata. They have a more nuanced understanding of their platform’s intricacies and are more likely to recognize false positives in error reporting, misinterpretations in compliance metrics and inefficiencies in workflows. This firsthand experience often makes them more skeptical of data quality and centralized reporting.

Shifting business priorities further widen this gap. While engineering teams aim to optimize efficiency and maintain high-quality code, leadership often has a broader focus on delivering business value.

A business-minded leader may prioritize getting a new feature to market quickly because it addresses customer demand or strengthens the product’s competitive edge. In contrast, the same business-minded leader may struggle to justify the time investment in foundational improvements, such as refactoring code or optimizing developer experience, which have long-term benefits but lack immediate business appeal.

Organizational goals that can quickly shift further exacerbate this tension. For example, while an organization may focus on increasing revenue, the engineering team may be striving to meet [DORA metrics](https://www.port.io/blog/how-to-implement-and-track-dora-metrics-in-your-organization?utm_campaign=The%20New%20Stack&utm_source=The%20New%20Stack&utm_content=disconnect). A sudden shift in business priorities can disrupt engineers’ workflows, leaving managers struggling to translate technical impact into business language.

A recurring theme is that there are communication gaps and transparency issues between engineering leaders and engineers, making it difficult for engineers to know what to prioritize, what expectations of them are and how standards are defined.

## AI Is Adding More Complexity
AI adoption stands to further widen this gap. Leaders tracking AI tool adoption may see positive results in efficiency, but engineers working with AI-generated code are the first to encounter the increased risks, such as security vulnerabilities and unexpected bugs. AI-generated code leads to more microservices, more cloud resources and, ultimately, more complexity. More code means more incidents, more vulnerabilities and a greater need for governance and oversight. As a result, engineers may struggle with the added burden while leaders expect faster delivery times without fully grasping the technical debt being accumulated.

AI adoption often also lacks clear governance, and engineers may struggle to implement AI-generated code within existing standards. Without alignment on how AI tools should be used and measured, the disconnect will continue to grow between leadership expectations and engineering realities.

Additionally, the difficulty in measuring the return on investment of AI tools fuels this divide. In fact, according to Gartner, 49% of AI leaders view estimating and demonstrating AI value as the top barrier to AI adoption.

## How Do You Fix the Disconnect?
### 1. Feedback Loops: Using Surveys To Bridge the Gap
One of the most effective ways to close the gap between engineers and engineering leaders is through structured feedback loops. [Surveys](https://www.port.io/blog/how-to-create-a-developer-experience-survey?utm_campaign=The%20New%20Stack&utm_source=The%20New%20Stack&utm_content=disconnect) can highlight inefficiencies caused by tool sprawl, unclear standards and poor AI implementation. They allow leaders to gauge how engineers feel about their work environment, whether they trust the data they rely on and how productive they believe they are, in a nonconfrontational way that supports meaningful change.

This type of continuous feedback ensures that leadership understands engineers’ pain points and can act accordingly. Using a platform or [portal that has surveys integrated](https://docs.port.io/guides/all/create-surveys/?utm_campaign=The%20New%20Stack&utm_source=The%20New%20Stack&utm_content=disconnect) can help teams improve communication, and more importantly, improve the experience of everyone involved in software engineering.

### 2. Define and Enforce Standards
A major frustration for managers is aligning developers with organizational standards. One method of combating this is to use scorecards. Scorecards provide a structured way to define and [track key metrics across engineering teams](https://thenewstack.io/how-to-track-dora-metrics-in-an-internal-developer-portal/), ensuring best practices are consistently followed. They help leaders measure progress in reliability, security and efficiency while giving engineers a clear framework for improvement. They include tiered levels — such as gold, silver and bronze — to indicate varying levels of compliance or maturity.

Scorecards help assess production readiness, code quality, migration progress, operational performance and more. They improve visibility into standards, ensuring engineers and managers are aligned on expectations without unnecessary friction.

Scorecards also provide a structure for tracking the impact of AI-generated code to ensure it aligns with organizational standards. AI adoption should not just be measured by how many engineers use it; it should be evaluated based on whether it improves or hinders software quality. By integrating AI metrics into scorecards, leaders can ensure AI-generated code meets security and compliance standards, while preventing the creation of additional technical debt.

### 3. A New Playbook for AI Standards
Rather than imposing rigid AI standards from the top down, engineering leaders should involve developers in defining best practices. AI-generated code should be piloted in controlled environments, with human reviews ensuring quality. Organizations must also measure AI’s impact on release frequency, bug count and vulnerabilities to ensure its effectiveness aligns with overall engineering goals.

### 4. Increasing Transparency on Data
A core issue in the engineer-manager disconnect is trust in data. Trust should improve when both engineers and leaders have real-time access to the same data on DORA metrics, standards compliance and workflow inefficiencies. It would also help to unearth any issues with the quality of the data and present opportunities for resolution.

Engineers need to be able to rely on the metadata from a single source of truth, rather than switching between tools for data they can trust or relying on DevOps, site reliability engineers or other colleagues for information. Once they have data they trust — through shared visibility on dashboards and scorecards based on this data — engineers will more easily see the reasoning behind leadership decisions. In turn, managers will gain a fuller view into their software delivery life cycle and a more accurate understanding of on-the-ground realities.

### 5. Measuring Impact of New Tools
One way to bridge the gap is by implementing [better measurement for new tools, including GenAI](https://www.port.io/blog/measure-roi-genai-tools?utm_campaign=The%20New%20Stack&utm_source=The%20New%20Stack&utm_content=disconnect). Engineering leaders should not only track AI tool adoption but also correlate usage with key performance indicators such as code quality, incident frequency and security vulnerabilities.

Instead of just measuring the number of AI-generated suggestions accepted, organizations should assess their impact on mean time to recovery (MTTR), deployment frequency and overall software stability.

## Collaboration Over Control
Closing the gap between engineers and engineering leaders isn’t about forcing alignment. It’s about fostering communication, collaboration and trust. Whether through structured feedback loops, developer portals, AI standardization or shared visibility into data, the key to a stronger engineering culture lies in enabling better conversations and empowering both sides with the right tools.

When engineers have clarity on expectations and the tools to meet them, and leaders have real insight into their teams’ realities, both can focus on what truly matters: building high-quality software without unnecessary friction.

[
YOUTUBE.COM/THENEWSTACK
Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.
](https://youtube.com/thenewstack?sub_confirmation=1)