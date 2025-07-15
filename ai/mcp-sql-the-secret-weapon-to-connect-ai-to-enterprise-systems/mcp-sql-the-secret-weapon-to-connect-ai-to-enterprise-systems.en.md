“We’ve spent four months and half a million dollars trying to connect our AI to our business systems, and it still can’t reliably pull basic customer data.” The frustration in the CTO’s voice was obvious during our video call. His company, and many others, face the same issues: The data needed to make AI super-powered lives in Enterprise applications, and those enterprise applications are not easily connected to AI processes and agents.

I’d heard this story dozens of times in my role as chief product officer at CData. Companies were racing to implement AI agents, only to hit the same wall: Their data lived in Salesforce, SAP, Oracle, custom databases, and countless other systems. Each required custom integration work, and even then, the security and governance challenges seemed insurmountable.

“What if I told you,” I said, “that your AI already knows how to talk to all these systems? It just needs the right translator.” That conversation led to a pilot project that would transform how they — and eventually dozens of other enterprises — approach AI integration. The secret? Integrating the Model Context Protocol (MCP) with CData connectors aims to establish a standardized communication method between AI and enterprise systems.

## **The Enterprise AI Integration Nightmare**

Let me paint you a picture of what enterprises face when trying to connect AI to their data. They’ve got:

* Customer data in Salesforce.
* Financial records in SAP.
* Inventory in a custom PostgreSQL database.
* Analytics in Snowflake.
* Documents are scattered across Google Drive and SharePoint.

Each system has its own API, authentication method, and quirks. Teaching an AI to speak all these languages is like asking someone to become fluent in 50 different dialects overnight.

Here’s the kicker: even if you manage to build all these integrations, you’ve created a security and maintenance nightmare. How do you ensure the AI only accesses [data the user](https://thenewstack.io/rockset-users-stranded-by-openai-acquisition-now-what/) is authorized to see? How do you track what it’s doing across all these systems? How do you keep up with changes in the API? How do you ensure that all the relevant data available in the API is exposed?

## **MCP + SQL: The Unexpected Power Couple**

We realized we can help deploy AI connected to enterprise data by combining two things:

First, [Large Language Models](https://thenewstack.io/what-is-a-large-language-model/) (LLMs) are surprisingly good at SQL. Why? Because they’ve been trained on millions of SQL examples from documentation, forums, and code repositories. SQL is standardized, logical, and pattern-based — exactly what LLMs excel at.

Second, the Model Context Protocol (MCP) provides a secure, standardized way for LLMs to interact with external tools and data sources. Think of it as a universal adapter that lets AI systems safely connect to your business tools.

Here’s how we make it work for our enterprise customers:

**Step 1: Deploy SQL Connectors.** CData connectors make any business system look like a SQL database. The Salesforce connector, for example, transforms API calls into SQL tables. Suddenly, querying customer data became as simple as:

SELECT \* FROM Customers WHERE Region = ‘Northeast’  
AND LastOrderDate < DATEADD(month, -6, GETDATE())

**Step 2: Implement MCP.** MCP acts as the secure bridge between the LLM and these connectors. When an AI needs data, it:

1. Generates the appropriate SQL query.
2. Sends it through MCP to the right connector.
3. Receives results in a standardized format.
4. Processes and acts on the information.

**Step 3: Enforce Security** This was crucial. MCP ensures that every query runs with the current user’s credentials. If a user can’t see certain customer records in Salesforce, neither can the AI when it’s working on that user’s behalf. No special AI permissions, no security backdoors.

## **Real-World Impact: From Theory to Practice**

Let me share a specific example. Our sales team needed to identify at-risk accounts and create personalized outreach. Previously, this required:

* Manually checking multiple systems.
* Copying data between applications.
* Crafting individual emails.
* Logging activities back into the CRM.

Total time: 2-3 hours per sales rep, daily.

With an MCP-powered AI agent, the same task now works like this:

1. Sales rep asks: “Find my accounts that haven’t engaged in 90 days and draft re-engagement emails.”
2. The AI generates SQL queries for CRM, email, and activity data.
3. MCP securely fetches data from each system using the rep’s credentials.
4. The AI analyzes patterns and drafts personalized emails.
5. Rep reviews and approves the emails.
6. AI updates the CRM with the outreach activity.

Total time: 15 minutes.

But here’s what really excites me — this isn’t just about read operations. The AI can now:

* Update opportunity stages in Salesforce.
* Create tasks in project management tools.
* Modify inventory levels (with approval).
* Generate and store reports.

All while maintaining a complete audit trail of every action.

## **Lessons Learned and Best Practices**

After a few months of experimenting with MCP-powered AI agents, here’s what we’ve learned:

**Start with Read-Only Operations.** Build trust by beginning with data retrieval. Let users see the AI pulling accurate information before enabling write capabilities.

**Implement Query Governance.** We built a simple approval system for certain operations. Deleting records? Updating financial data? These require human confirmation.

**Cache Smartly.** Not every query [needs real-time data](https://thenewstack.io/what-are-time-series-databases-and-why-do-you-need-them/). We cache relatively static information (like product catalogs) while [keeping transactional data](https://thenewstack.io/agentic-ai-is-coming-but-can-your-data-infrastructure-keep-up/) fresh.

**Monitor Everything.** MCP makes it easy to log every query and action. We built dashboards showing which systems the AI accesses most, helping us optimize performance and identify new use cases.

### **The Road Ahead**

The combination of MCP and SQL-based connectors has fundamentally changed how we think about enterprise AI. Instead of building complex, brittle integrations for each system, we now have a standardized, secure approach that scales.

We’re currently expanding our purpose-built connectivity for AI agents to handle more complex workflows:

* Multistep processes that span several systems.
* Predictive analytics using historical [data from multiple sources](https://thenewstack.io/how-open-source-and-time-series-data-fit-together/).
* Automated compliance checks across databases.

The key insight? You don’t need to rebuild your entire tech stack to leverage AI. By speaking the language your AI already knows (SQL) and providing secure access through MCP, you can transform how your organization works with data.

Next time someone tells you that connecting AI to enterprise systems requires months of custom development, tell them about MCP. Better yet, show them what’s possible when you flip the script and build on the foundation that’s already there.

Want to experiment with MCP yourself? Start with read-only queries to a single system. Once you see the [power of AI that can actually access your data](https://thenewstack.io/how-ray-a-distributed-ai-framework-helps-power-chatgpt/), you’ll never go back to copy-paste workflows again.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://cdn.thenewstack.io/media/2025/06/009a938b-manish.jpg)

Manish is responsible for defining CData’s strategic product vision and roadmap. He has over 15 years of product management experience growing packaged software and cloud-based offerings across multiple SaaS companies, including Tier1, Valassis Digital, and Ipreo. Manish holds a Bachelor’s...

Read more from Manish Patel](https://thenewstack.io/author/manish-patel/)