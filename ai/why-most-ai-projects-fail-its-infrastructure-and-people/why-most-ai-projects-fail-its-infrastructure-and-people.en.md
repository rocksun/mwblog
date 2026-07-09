AI trash-talkers love to rip on the technology for failing to produce meaningful business results, often pointing to studies like that from [MIT NANDA](https://mlq.ai/media/quarterly_decks/v0.1_State_of_AI_in_Business_2025_Report.pdf), which reveals a 95% failure rate for enterprise AI solutions, or that from [IDC](https://www.idc.com/resource-center/blog/most-ai-investments-dont-deliver-value-heres-what-emea-leaders-are-missing/), which states “only 9% of [Europe, Middle East, and Africa] organizations have been able to deliver measurable business outcomes from most of their AI-related projects over the past two years.”

What many AI skeptics fail to account for is the experiential nature of AI prototypes; not all these projects are actually meant to move beyond the testing phase. Still, a 5% success rate is embarrassing.

What’s the holdup?

Two things. First, most organizations build AI prototypes on sand; that is, the data infrastructure on which they build early applications can’t support later moves to production. Meanwhile, the operational teams responsible for managing those applications in production often lack the human power to keep up with engineering’s growing output.

## 4 reasons prototyping infrastructure  ≠ production infrastructure

When asked why so many AI prototypes don’t make it to production, [Phillip Merrick](https://www.linkedin.com/in/phillipmerrick), co-founder, CPO, and chairman, [pgEdge](https://www.pgedge.com/), tells *The New Stack* that data infrastructure is largely to blame.

Specifically, he explains that prototype environments don’t meet the requirements of large enterprises for production, naming four main ways they fall flat.

First, Merrick says prototyping environments lack the deployment flexibility organizations need to move from prototype to production.

Vendor-managed cloud platforms, he acknowledges, may seem like an obvious choice for prototyping, as they allow teams to get up and running quickly. Still, he warns they lack the technical chops to support AI applications in production, especially in security, compliance, and governance. Particularly for organizations in healthcare, finance, or other regulated industries, vendor-managed cloud platforms often lack the stringent controls found in self-managed cloud or on-prem environments.

> “You’ve got to be able to choose where that AI prototype is ultimately going to be put into production.”

In this way, flexibility and security go hand in hand. Merrick asserts. “You’ve got to be able to choose where that AI prototype is ultimately going to be put into production.”

Similarly, when it comes time to shift to production, Merrick says vendor-managed cloud platforms can introduce data sovereignty challenges at both the enterprise and regional levels.

“Your data layer is obviously where you enforce this,” notes Merrick. But he says the environments most teams use for prototyping muddy the waters: “If it’s on a vendor-managed platform in who knows what cloud, what region, then you’ve lost data sovereignty.”

Lastly, Merrick brings attention to reliability, explaining that AI prototypes can’t move into production without assurance of high availability. For example, when it comes time to upgrade the database or swap hardware, can it be done without downtime?

“In the vendor-managed cloud world, the answer to that is almost always no,” says Merrick, reiterating his point that [moving AI apps from prototype to production requires enterprise-grade infrastructure](https://thenewstack.io/ai-prototype-to-production-postgres/).

## So why are developers prototyping where they can’t productionize?

If data infrastructure selection is what’s holding developers back from moving AI prototypes into production, then why do they keep starting on the wrong foot?

As Merrick explains, many are attracted to the ease of use of vendor-managed cloud platforms. “These prototyping environments admittedly make it very easy to get started,” he says. But prototyping shortcuts, it seems, don’t pay off in the long run, as someone else is ultimately on the hook for making those prototypes production-ready.

Still, Merrick doesn’t blame developers for looking for the easy way out. Rather, he says there’s a disconnect between the prototyping playground and the production battleground that prevents developers from understanding what it will take to productionize prototypes down the pike.

---

### More pgEdge articles in *The New Stack*

---

Years ago, he says, tooling decisions were primarily made top-down without developer input: “Then, starting 15–20 years ago, the developers won back, quite rightly, the power in being able to choose their own tools.”

The problem now, Merrick claims, is that developers make tooling decisions exclusively for prototyping environments, without anticipating production needs. Internal divisions mean developers are often only responsible for building prototypes before passing the baton to an entirely separate operations team for production:

“The upshot is you really don’t have, in some organizations, this throughline of understanding [of] what the production requirements are all the way back to the developer making the initial choices.”

For Merrick, this disconnect is where AI projects start to fall apart, as teams are left trying to move AI prototypes from accessible-but-inadequate vendor-managed cloud platforms to enterprise-grade data infrastructure that meets requirements for deployment flexibility, security, data sovereignty, and high availability.

“But if you make the right data infrastructure choice, you won’t have that disconnect,” he says, “because you’ll have this throughline from prototype to production.”

He names Postgres as [the data infrastructure that best helps developers bridge this divide](https://thenewstack.io/postgres-ai-ground-truth/), calling it “the Swiss army knife of databases” due to its extensibility, fully open-source nature, and ability to address diverse data management problems, from unstructured data to vector embeddings to geospatial data.

Where and how Postgres is run matters too, Merrick points out, again drawing attention to the limits of many vendor-managed cloud environments that often lack the governance controls to meet data requirements and/or the deployment flexibility to shift to compliant on-premises or BYO cloud environments.

## But picking the right data infrastructure only solves half the problem

Merrick says there’s another part of the equation most organizations are overlooking: people, or more precisely, database administrators (DBAs) and their growing workloads.

Per [Stack Overflow’s 2025 Developer Survey](https://survey.stackoverflow.co/2025), 84% of respondents use AI tools, up from 76% the year prior. Meanwhile, Supabase [says](https://techcrunch.com/2026/06/05/supabase-doubles-valuation-to-10b-in-8-months/?utm_source=chatgpt.com) over 60% of databases on its platform have been launched “by some sort of AI tool.” As Merrick points out, this explosion of productivity comes with a catch: there aren’t enough DBAs to keep up.

“You’ve had this massive, massive step shift in developer productivity,” he explains. “But you have to have some way of managing that on the production side; these databases can’t go unmonitored.” Operations and administration teams were already struggling to keep track of existing Postgres databases before agentic engineering added even more, he says: “Who’s going to manage them?”

He says it’s time for agentic operations to catch up with agentic engineering.

## AI DBA agents can give humans “superpowers”

If it seems Merrick is proposing organizations look to fully autonomous DBA agents to take over, he says the industry isn’t there yet:

“The world is not ready for fully autonomous databases administered by AI DBA agents. But there is a massive resource shortage and productivity problem, and DBAs can only manage so many databases,” he explains. Meanwhile, new “AI applications require so many more databases to put in production.”

> “The world is not ready for fully autonomous databases administered by AI DBA agents.”

So how can organizations increase their operational capacity?

Merrick says DBAs should look to new AI DBA agents, not to take over but to give them “superpowers” to monitor and manage more databases with less manual slog.

pgEdge’s Ellie is one example. Part of the [pgEdge AI DBA Workbench](https://www.pgedge.com/products/ai-dba-workbench), Ellie is an AI agent that has 21 MCP tools and can run EXPLAIN ANALYZE, inspect schemas, query historical metrics, and walk through multi-step diagnostic workflows. When a database falters, Ellie finds the problem, diagnoses it, and provides a solution in the form of working SQL code for the human DBA to review. “When you’ve reviewed it and agree that it’s the right course of action, you literally press the play button, and the agent plays that SQL code into the database, and you solve your problem,” explains Merrick.

In this way, Ellie should bring more capacity to operations teams, where Merrick insists organizations are starved for DBA expertise. To his point, some [industry predictions](https://www.dbta.com/DBTA-Downloads/ResearchReports/The-Vanishing-Database-Administrator-Survey-Of-Data-Professionals-Career-Aspirations-4791.aspx) say 41% of today’s database professionals intend to leave the industry in the next decade, half moving into retirement and the rest seeking other work.

> “An agent … can actually respond to those alerts far more quickly and productively than a human can.”

Without AI agents, Merrick argues, DBA work is tedious, laborious, and time-consuming. As he explains it, a database may have been humming along just fine, but when there’s a snag, trouble can manifest across multiple applications; it’s then up to the DBA to comb through monitoring data to observe and diagnose the problem, essentially scouring for a needle in a haystack.

“An agent,” he says, “can actually respond to those alerts far more quickly and productively than a human can.”

## Better infrastructure AND people: It takes two to improve AI prototype success rates

In nearly any context, AI raises questions about quality over quantity, and enterprise AI projects are no exception. Agentic engineering means developers can now produce more, but all those prototypes don’t just fly directly into production. Limitations in both infrastructure and operational human power are creating obstacles that cause many AI prototypes to fail.

For Merrick, easing the transition from prototype to production requires not only great AI tooling but production-ready data infrastructure, paired with agentic operations that can keep up with the agentic engineering boom.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://thenewstack.io/wp-content/uploads/2025/09/53f49f49-cropped-35fc143f-meredith-shubel-2-600x600.jpg)

Meredith Shubel is a technical writer covering cloud infrastructure and enterprise software. She has contributed to The New Stack since 2022, profiling startups and exploring how organizations adopt emerging technologies. Beyond The New Stack, she ghostwrites white papers, executive bylines,...

Read more from Meredith Shubel](https://thenewstack.io/author/mshubel/)