[Atlassian](https://www.atlassian.com) wants the autonomous, long-running agents that developers use in tools like Claude Code to work for everyone else.

At its Team ’26 conference in Anaheim on Wednesday, the company is rolling out Max, a new mode in Rovo Chat that Atlassian’s head of product for AI, [Jamil Valliani](https://www.linkedin.com/in/jamil-valliani-b131881/), describes as a “mini Claude Code” running “in the cloud with Teamwork Graph context built in.”

For Atlassian — as for many of its competitors — the data it has and the context it can provide to agents is becoming increasingly important as the core of the emerging agentic layer that is, at least for now, still very much in flux.

![](https://cdn.thenewstack.io/media/2026/05/7e02cc03-twg-mcp-vignette-final.gif)

For Atlassian, this specifically means opening its Teamwork Graph, its map of more than 150 billion objects and relationships across Jira, Confluence, Jira Service Management, and dozens of connected SaaS tools, to any MCP-compliant agent. There is also a new Teamwork Graph command-line tool and a set of MCP servers, both in open beta, that let Claude Code, IDE copilots, and other third-party agents query the same context substrate that powers Atlassian’s own Rovo platform.

> Atlassian’s bet is that the context an agent can access within a customer’s data fabric determines whether it’s useful in the enterprise.

Atlassian’s bet is that the context an agent can access within a customer’s data fabric determines whether it’s useful in the enterprise. The company is willing to make that bet even at the cost of letting outside agents into its own graph.

## How the graph works

The Teamwork Graph has been in development for years, Valliani told *The New Stack* in a briefing ahead of the announcement. He calls it “system of record level quality,” and he believes this is what distinguishes it from competitors (though those competitors, too, are often taking a very similar approach as they look at their internal graphs as moats in this agentic age)

For an enterprise, this graph includes years of Jira ticket history, Confluence pages, and Jira Service Management incidents, along with signals from connected SaaS tools. These are then all mapped with relationships between people, projects, decisions, and documents.

[](https://cdn.thenewstack.io/media/2026/05/9e1a79a2-twg-mcp-vignette-final.mp4)

Atlassian exposes the graph to agents through an internal query language it calls Cipher. The tools shipping at Team ’26 allow an agent to perform these Cipher queries to traverse relationships across the graph in what Valliani describes as multi-hop traversal.

The pitch over standard retrieval-augmented generation is that an agent reasoning over relationships can find what it needs without dumping raw text into the context window. “The context window is not stuffed anymore,” Valliani says. “You can actually use reasoning power where it belongs, not just to sit through a bunch of data.”

A new public site at teamworkgraph.com will now, for the first time, also allow customers to visualize their own graph.

Atlassian ran its own internal benchmark comparing Claude Code with Teamwork Graph CLI access and the same agent without it. Atlassian says that the version with graph access used 48 percent fewer tokens and produced 44 percent more accurate results, which Valliani attributes to the agent’s ability to traverse relationships rather than reconstruct context through retrieval.

![](https://cdn.thenewstack.io/media/2026/05/7c4a152b-img_3822-1024x768.jpg)

Atlassian co-founder Mike Cannon-Brooke at Atlassian Team ’26. Credit: *The New Stack*

## Opening the moat

Also new at Team ’26 is the Teamwork Graph CLI, now in open beta, that gives developers, admins, and coding agents a terminal interface to the graph (who thought command-line tools would suddenly be interesting again?). Meanwhile, the Teamwork Graph tools in MCP, also in open beta, let any MCP-compliant agent query the graph the same way Rovo does.

In a press briefing ahead of the conference, Atlassian co-founder and CEO [Mike Cannon-Brookes](https://www.linkedin.com/in/mcannonbrookes/) said that he believes “the Teamwork Graph CLI is probably going to be the number one thing, I suspect, received by customers in terms of — it’s free, which always helps them, and it just unlocks the existing graph they have in all these new ways.”

> “We’ve been an open platform company from day one, so we’ve never wanted to constrain somebody to use only one thing.”   
> —Jamil Valliani, Atlassian

The practical use case Atlassian describes is a developer running Claude Code in their IDE who wants the agent to know which Jira tickets and Confluence decisions are connected to the file they’re editing. Without these new tools, a developer would have to write custom glue code to retrieve this data. But now, the agent can query the graph directly through MCP and obtain the same relational context that Rovo does.

“We’ve been an open platform company from day one, so we’ve never wanted to constrain somebody to use only one thing,” Valliani says and notes that this allows power users to build with the agent of their choice on top of the Teamwork Graph, while knowledge workers can stay in Rovo, where this context has always been the default.

With code intelligence, a developer can ask Rovo to find every place in the codebase where a new button style hasn’t been adopted, for example. Rovo searches across “over a billion lines of code,” says Valliani, and returns the non-conformant repositories in minutes. From there, agents can be assigned to make the changes through the agents-in-Jira workflow.

## Pricing

Today, Rovo actions are entitled per seat. Customers get a number of Rovo credits with their Atlassian plan. Overage charges have not yet been turned on.

Max is moving to a different model. Atlassian plans to bill Max usage on a variable, value-based basis, with rate cards and overage timing to be published “relatively soon,” says Valliani. “You could ask a 5-minute job or a 20-minute job,” and pricing has to follow, he argues.

Cannon-Brookes, when *The New Stack* asked about Atlassian’s overall approach to pricing now that so many companies are moving into consumption-based models, noted that the company wants “to be customer-led on pricing.” He believes in the hybrid model, the company’s current offers, mixing per-seat charges with credits for AI usage.

“Our seat-based model comes with a generous Rovo credit limit as an example, on the AI side of things, generous indexed objects on the storage side of things, generous storage limits, like a bunch of Forge limits, and other things like this. For the vast majority of customers, we want their usage to be inside the kind of envelope of what they pay,” Cannon-Brookes said.

He did acknowledge, of course, that some users will push this to the limit, but then, the user who pushes millions of objects into the TeamWork Graph is also likely to be willing to pay for the value they get out of that.

## The context-layer wars are here

Atlassian is not alone in claiming the context graph as the differentiator, of course. Microsoft is making the same pitch with Microsoft Graph plus Copilot Studio, Salesforce with Data Cloud and Agentforce, and ServiceNow with a number of tools it is announcing at its own event this week.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://thenewstack.io/wp-content/uploads/2025/03/15a7eb12-cropped-4e88ac40-frederic-profile-2-600x600.jpg)

Before joining The New Stack as its senior editor for AI, Frederic was the enterprise editor at TechCrunch, where he covered everything from the rise of the cloud and the earliest days of Kubernetes to the advent of quantum computing....

Read more from Frederic Lardinois](https://thenewstack.io/author/frederic-lardinois/)