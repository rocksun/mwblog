# Can You Trust AI To Be Your Data Analyst?
![Featued image for: Can You Trust AI To Be Your Data Analyst?](https://cdn.thenewstack.io/media/2025/03/8e34160a-igor-omilaev-9xtksci9crg-unsplash-1024x576.jpg)
[Igor Omilaev](https://unsplash.com/@omilaev?utm_content=creditCopyText&utm_medium=referral&utm_source=unsplash)on
[Unsplash](https://unsplash.com/photos/a-neon-neon-sign-that-is-on-the-side-of-a-wall-9XtKSci9crg?utm_content=creditCopyText&utm_medium=referral&utm_source=unsplash).
The good news is that deploying AI agents and connecting them to your data is easier than ever. But that alone won’t make AI agents effective for data-driven decision-making. Models like DeepSeek — or any other large LLM — can’t generate meaningful insights if the underlying data is inconsistent. It’s the classic **garbage in, garbage out** problem.

And in most companies, there’s an elephant in the room: organizations often have multiple versions of the same metric, each calculated differently. Take “profit margin” as an example — finance, sales, and operations might all define it differently. With this kind of inconsistency, AI has no chance of delivering the *correct* answer because, in reality, the organization hasn’t yet agreed on the correct answer.

Many think cleaning the [data and removing errors is enough](https://thenewstack.io/observability-isnt-enough-its-time-to-federate-log-data/) to get AI-driven insights. However, even immaculate data can lead to conflicting answers without consistent definitions.

**A Real-World Scenario**
Let’s say an AI agent is asked to find the company’s at-risk customers — the ones most likely to churn. It searches the CRM and sees a field labeled **“at-risk”** attached to a list of customer accounts. The AI pulls the data, generates a report, and presents the results.

*Is that correct?*
Not quite. The customer support team applied that **“at-risk”** tag months ago during a temporary service issue. Risk should be evaluated using metrics like long-term engagement, product usage, and historical churn, not on an obsolete tag. Worse, the actual churn model, officially accepted by management, lives in a workbook buried among other exploratory dashboards in the BI tool.

So what happens next? The AI agent delivers an incomplete or misleading analysis, teams base decisions on the wrong numbers, and trust in AI-driven insights erodes.

**Building a Foundation for AI-Ready Data Assets**
Traditionally, teams [approach AI-driven analytics by first building](https://thenewstack.io/building-ai-driven-applications-with-a-multimodal-approach/) a governed semantic model. Creating a governed foundation for business metrics is crucial for long-term success. It ensures consistent [data interpretation and accurately maps business](https://thenewstack.io/ai-adoption-why-businesses-struggle-to-move-from-development-to-production/) intent to the data. A semantic model is essential for enabling text-to-SQL and ensuring AI agents can accurately interpret and answer natural language queries such as: *What was our CAC (Customer Acquisition Cost) last quarter? *

But if you also want AI agents to pull the right dashboards and reports, they need to differentiate between ad hoc work and trusted data products. Most organizations have thousands of dashboards, many created for quick analysis or one-off reports. If a user asks, *“Show me our sales performance by region,” *AI shouldn’t just surface the first dashboard it finds.

To ensure AI surfaces the right reports, we recommend **labeling reliable dashboards as certified** so AI agents can confidently share them. This will prevent outdated or exploratory reports from being mistaken for trusted data.

**Start Small and Scale**
Building a semantic model and certifying data products doesn’t have to be an all-or-nothing approach. Instead of trying to govern everything at once, start with a limited set of tables (such as company-wide KPIs or tables associated with a specific domain) before expanding to your entire data ecosystem.

**Establish a Governed Semantic Model**
A [semantic model](https://euno.ai/blog/semantic-layers/) acts as the aligned source of truth for your organization’s key metrics. It maps business intent to [data using standardized](https://thenewstack.io/why-we-need-an-inter-cloud-data-standard/) definitions, enabling AI tools to interpret natural language queries accurately, delivering on the classic text-to-SQL scenario.

But here’s the challenge: analysts are constantly creating new metric definitions on the fly in their BI tools. Without visibility into how these metrics are defined and used and whether they conflict with existing definitions, organizations risk building a semantic model that doesn’t align with real business needs. To ensure your semantic [model reflects how data](https://thenewstack.io/data-modeling-part-2-method-for-time-series-databases/) is used, you need a deep understanding of what already exists, how it’s utilized, and where inconsistencies lie.

**How to establish your semantic model:**
**Start with highly utilized metrics**: Begin with metrics that are frequently referenced or queried across teams. These are the ones that will deliver the most value when governed.**Prioritize complex calculations**: Metrics with custom logic are good candidates for inclusion into the semantic model. Governing these ensures accuracy and minimizes errors in downstream reports.**Keep it consistent and clean**: Invest in resolving conflicts, identifying duplicates, and decluttering unused metrics.**Monitor continuously**: The semantic model isn’t static. Keep an eye on which metrics gain traction and evaluate whether they should be incorporated into the semantic model or replace outdated definitions
The goal isn’t just to build the model; it’s to keep it clean, relevant, and aligned with the business as it evolves.

![](https://cdn.thenewstack.io/media/2025/03/12fa9433-conflict-analysis-1024x512.png)
Find conflicting measures, trace their data sources, compare calculations, and assess their utilization and owners to resolve inconsistencies.

**Certify Data Products**
Even with a governed semantic model, AI agents still need to know which dashboards and reports can be trusted. A certification program helps distinguish between reports built on validated, governed [data and those created for exploratory or one-off analysis](https://thenewstack.io/the-rise-of-community-driven-data-analysis-in-the-age-of-ai/). Implementing a certification program can help AI agents navigate dashboard sprawl.

How it works:

**Set certification criteria**: Define what makes a dashboard or report certifiable. For example:[Data should be sourced from production-grade tables](https://thenewstack.io/a-react-based-open-source-tool-for-creating-data-tables/)(e.g., debt marts with production tags).- Ownership and documentation should be clear and up to date.
- Doesn’t include custom logic (e.g., in the form of custom SQL statements).
**Add a “certified” label to dashboards**: Dashboards can be labeled “certified” to indicate that they comply with governance standards. You can manage this process manually or use tools such as Euno automating certification. These tools can identify which dashboards meet certification criteria, highlight gaps in non-certified ones, and provide clear steps for remediation.**Monitor continuously**: If a dashboard’s data source or logic changes, its certification status should be re-evaluated. Regularly update certifications to ensure that AI agents are always working with[reliable data for trusted](https://thenewstack.io/aws-brings-trusted-extension-support-to-managed-postgres/)results.
**Connect AI Agents to Governance Data via API**
AI agents don’t inherently understand governance, they need explicit labels about the trustworthiness of data assets. Connecting them to [governance data via an API](https://thenewstack.io/make-data-governance-automation-suck-less-with-a-supergraph/) ensures that they only surface reliable, certified insights.

**For surfacing dashboards:**
- When a user asks, “Show me our sales performance by region,” the AI agent should:
- Query the governance API to identify certified dashboards.
- Surface the most relevant, trusted dashboard, avoiding outdated or uncertified versions.
**For answering ad-hoc questions:**
- For queries like, “What’s our churn rate for enterprise customers?” AI agents should:
- Pull definitions from the semantic model to ensure consistency.
- Use only governed data sources to calculate and return accurate results.
AI agents can confidently distinguish between high-quality, reliable assets and exploratory or outdated ones by integrating governance metadata into their workflows.

**The Outcome: AI That Works as Expected**
Organizations can transform their AI-powered analytics by establishing a governed semantic model and a robust certification program. Instead of guessing or relying on incomplete data, AI agents will deliver inaccurate, actionable [insights aligned with the business](https://thenewstack.io/data-unleashed-unlocking-powerful-business-insights/).

When your data is AI-ready:

**Decisions happen faster**: Users get instant access to reliable insights.**Trust improves adoption**: Business teams rely on AI tools with confidence.**Data stays clean**: Governance processes reduce clutter and errors.
**Conclusion**
AI-powered analytics is a game-changer only if the data assets are governed. Without governance, AI tools risk amplifying chaos instead of delivering clarity. Standardizing key metrics, certifying trusted dashboards, and connecting AI agents to governance metadata will ensure your AI initiative delivers real, reliable impact.
Generative AI can revolutionize analytics. Just make sure your organization is ready to match the promise.

[
YOUTUBE.COM/THENEWSTACK
Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.
](https://youtube.com/thenewstack?sub_confirmation=1)