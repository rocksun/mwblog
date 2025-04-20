# Agentic AI for the Whole SLDC With Atlassian Rovo Dev Agents
![Featued image for: Agentic AI for the Whole SLDC With Atlassian Rovo Dev Agents](https://cdn.thenewstack.io/media/2025/04/001746cd-anu-bharadwaj-teams-25-1024x576.jpg)
ANAHEIM, CALIF. — So much of [generative AI (GenAI) for engineers](https://thenewstack.io/ai-engineering/) is focused on the inner loop, especially AI-generated code. Despite that, [developers want to spend more time writing code](https://thenewstack.io/why-do-developers-lose-1-day-a-week-to-inefficiencies/) — and AI isn’t exactly great at that (yet, anyway).

What really [slows down developer productivity](https://thenewstack.io/the-interrupt-tax-why-developer-productivity-is-measured-in-silences/) is that outer loop, which has engineers waiting on other teams and systems. This is especially true with knowledge sharing and discovery, as poor or missing documentation continues to top developers’ complaint lists.

True innovation in [GenAI](https://thenewstack.io/ai/) comes when organizations [measure the entire software development lifecycle](https://thenewstack.io/a-guide-to-measuring-developer-productivity/), and then apply AI to both major bottlenecks and [smaller paper cuts](https://thenewstack.io/boost-developer-productivity-by-reducing-their-paper-cuts/).

Six months ago, Atlassian, which produces enterprise and developer productivity tools, [released its GenAI suite of products, known as Rovo](https://thenewstack.io/atlassians-new-ai-product-gives-developers-access-to-agents/). Now phasing into general availability, Rovo, with already more than 1 million users per month, centers on three cross-organizational functions:

- Search: With more than 300,000 organizations already using it, Search combats the average
[25% of time knowledge workers spend looking for answers](https://www.atlassian.com/blog/state-of-teams-2025). - Chat: Built on top of all major large language models (LLMs) plus the
[Atlassian Teamwork Graph](https://thenewstack.io/atlassian-intelligence-saas-co-gets-generative-ai-makeover/)and third-party tools, with zero-day retention. - Studio: Out-of-the-box and build-your-own
[AI agents](https://thenewstack.io/ai-agents/)and agent swarm workflows.
According to the Atlassian team, early adopters are now 60% more successful with the Rovo app than leading open source equivalents. For the company’s own engineers, this includes a 45% reduction in pull request cycle time from the implementation of just one AI dev agent.

At last week’s [Atlassian Team](https://events.atlassian.com/team-digital/) event, Rovo, which previously cost $20 a month per person, was announced as included within any Atlassian plan, and costs $5 for colleagues who don’t have a Jira, Confluence or Loom subscription. This, the company said, will increase the “brainpower” behind Rovo, its Teamwork Graph, which maps out the interconnectedness of teams, data, goals and knowledge.

The New Stack learned from Atlassian’s leadership about the impact of Rovo on the developer experience, tightening that chasm between tech and business.

## Go Where Your Developers Are
Atlassian is all in on AI, grounded in the belief that AI is only valuable if it’s easy to adopt — and that early adopters will have the advantage.

This includes, as [Jamil Valliani](https://www.linkedin.com/in/jamil-valliani-b131881/), head of AI product for Atlassian, said in a press briefing at Teams ’25, “All the people who are early on the train as the world is to be rebuilt to AI plus human collaborators.”

Across its core products, Atlassian is looking to balance out-of-the-box common use cases with the ability to tailor any solutions, because, as he put it, “AI is not one-size-fits-all. No team is the same.”

According to the [Atlassian State of Teams 2025 report](https://www.atlassian.com/blog/state-of-teams-2025), 71% of teams surveyed responded that they aren’t maximizing the use of AI to help them manage and discover information. This is in part because so much of early AI adoption is focused on code generation, which, on its best days, tops 30% of the developer experience. Valliani adds that AI adoption falters when rollout is slow and so much of AI is not integrated into the workflow.

One of the reasons [GitHub Copilot](https://thenewstack.io/microsoft-makes-github-copilot-free-in-vs-code/) took off is because it reduces context switching by putting its searchable GenAI right alongside the codebase. Atlassian echoes this sentiment by not only embedding Rovo into its own products’ workflow but within GitHub as well, “at the right time and right place,” as Valliani said, “almost without them having to actively think about it.”

The Teamwork Graph natively understands the relationships between Jira Issues and Confluence Pages. Rovo Search integrates into [Slack](https://api.slack.com/?utm_content=inline+mention) with file preview — no need to download or open in a separate window to preview — as well as with an array of applications like [Google](https://cloud.google.com/?utm_content=inline+mention) Drive, [ServiceNow](https://www.servicenow.com/products/observability.html?utm_content=inline+mention), Sharepoint, Workday and Outlook.

Each Teamwork Graph result will be different for each user. It trains on and pulls from all integrated tools, given role-based access control (RBAC) for each, driving a more personalized search experience.

Rovo Search provides a curated summary with relevant timeline and references, enhanced with semantic search, which Valliani contends is “one of the first companies to offer our customers semantic search out of the box at this scale.”

Rovo Chat is already popular both across Atlassian — again, not just technical roles — as well as with other early adopting customers. Atlassian has a relationship with each major LLM, he said, each with its own no-data-retention agreement. Not only does this protect user data, but it also allows Rovo to have its own mix of GenAI capable of “switching behind the scenes” when new models are released.

Valliani boasted a 90% internal usage success rate for Rovo Chat to perform the actions required. For more complex topics, soon Chat users can also use Deep Research, which executes a research plan including different relevant colleagues, an expanded search and a list of sources, producing a report that includes videos, diagrams, tables and, optionally, web results.

These Rovo features are also now available across all Atlassian products, including Goals, which enables a conversational overlay that connects work to outcomes — something that’s always challenging with [OKRs](https://thenewstack.io/a-guide-to-okrs-and-overcoming-the-pain-of-them/) and can help connect organizational objectives with Jira issues.

## AI Agents Made for Developers
One of the biggest announcements of Team ’25 was the launch of the Studio app within Rovo, which uses natural language to automate the creation of AI agents and the curation of swarms of agents. Of course, The New Stack has its eye on the [Rovo dev agents](http://atlassian.com/rovo-dev).

The overall aim of these agents is to “rescue humans from the drudgery,” Valliani said. For software that translates to building on the [goals of platform engineering](https://thenewstack.io/how-to-foster-a-good-internal-developer-platform-experience/), aiming to take on what he called “time-consuming but important tasks,” or that 80% of the developer experience that’s caught up in toil.

Around 20 out-of-the-box dev agents were released last week. Code Planner reads a Jira issue and all associated information from Teamwork Graph, like requirements, Confluence documentation and any third-party information, according to [Josh Devenny](https://www.linkedin.com/in/jjdevenny/), Atlassian’s head of product, AI, agile and DevOps.

“The Code Planner will then write a technical plan on the Jira issue to help developers be more productive, get faster at getting straight to implementation at the individual or at the team level,” he told The New Stack.

“A good use case is a developer who’s new to a repository, which happens reasonably often across a big organization. You might have to go and contribute code somewhere else. We can help you write a plan of, ‘here’s where we think you should make those changes, we give you the files and the changes that we think need to be made.”

The Code Planner dev agent is also a good first stop for junior engineers before asking their seniors for help.

![The Rovo Code Planner dev agent workflow process within Jira.](https://cdn.thenewstack.io/media/2025/04/a5660a61-rovo-dashboard-2-1024x566.png)
The Rovo Code Planner dev agent workflow process within Jira.

The new Implementor Agent can then take that technical plan and write the code for it.

“The developer can choose an agent to implement the code that it will come back with before a pull request is raised,” Devenny said. The dev agent notifies the developer, shares the diff, and “the developer gets to review it and make any changes.” This often involves a conversation between the developer and the agent.

## Use Cases for Custom Dev Agents
While there are those 20 or so out-of-the-box AI agents, Valliani said early adopters demanded a blank canvas to build their own, each dedicated to a singular purpose.

With that in mind, Atlassian added the no-code ability to build your own agent, which even nontechnical departments at Atlassian have used. Internally, Atlassian created its own Onboarding Buddy agent that, within the first month, was answering 2,000 questions from 70% of Atlassian new hires.

One Atlassian engineering team built and then internally shared its own Pull Request Generator that team members said automated 80% of developer tasks — like adding feature flags and test automation — cutting the average pull request down to 30 minutes.

This ability to create custom dev agents also allows customers to enforce organizational and industry standards, often pulling from existing Confluence documentation.

“Then you can tailor these agents, can specify knowledge sources and constrain the agent, then run agents automatically,” Valliani said.

Facing a time where more AI-generated code means more demand for code reviews, a third early agentic AI developer use case is addressed internally at Atlassian with its Code Reviewer, which combines a pull request with a Jira issue, Devenny said, to “deduce the acceptance criteria in the Jira issue, and we show whether the code actually matches that acceptance criteria or not.”

Code Reviewer also checks for syntax errors and typos. If it’s a code change to a more sensitive or crucial piece of the codebase, it can be flagged for review by two reviewers.

Last week, Code Reviewer suggested Devenny reduce the complexity of this function and provided a code example of how to do it. With this in mind, in the coming months, Bitbucket will be introducing an “apply suggestion” button.

Since the adoption of this particular dev agent in late October, Atlassian engineering has experienced a 45% improvement in PR cycle time for any pull request when Code Reviewer is being used, versus when it is not.

“The reason it’s such an aggressive jump decrease,” Devenny said, “is because you don’t have to wait for hours or days for a peer to jump in, you immediately have feedback.”

“At the moment, the tasks that we’re doing for developers are like repetitive tasks, ones that developers are like not enthused about doing in the first place. Being able to remove that from their things that they have to do means that they get to spend more time focused on the tasks that they love implementing.”

— Josh Devenny, Atlassian
Ops Guide is another dev agent that helps out with on-call duties, seeking to reduce time to detect, respond to and recover from incidents.

Each of these dev agents helps decrease overall issue cycle time, but does not automate out the essential human in the loop.

Devenny also mentioned that Pipeline Fixer and Deployment Summarizer dev agents are coming soon.

The Feedback Decoder AI agent creates and analyzes transcripts from customer feedback from the Loom video messaging platform and other sources, which then can be used to automatically create Jira tickets. The Jira Product Discovery (JPD) AI agent can then connect Jira tickets with customer data, which are in turn tied to stated Goals. The Feedback Decoder can also update teams in Slack, log activity in HubSpot and more.

“JPD makes it really simple to see how your product idea moves the needle on important goals and metrics, so you can explain how your great product idea impacts your business, and you get to decide who has access to your own maps,” said [Anu Bharadwaj](https://www.linkedin.com/in/anutthara/), president of Atlassian, in a Teams ‘25 keynote. “It could be departments, teams or the entire company.”

Atlassian has even used it to share product roadmaps with partners and customers. Bharadwaj also cited the early adopter Doodle online scheduling platform, and how it used JPD to “build a system that converts customer insights into ideas, and the results are staggering — 25% faster delivery and 93% drop in time spent planning.”

These dev agents accomplish all this without data retention, Devenny said: “We are not training on your data. We are simply providing that context to the agent at runtime.”

## Orchestrate a Swarm of AI Agent Teammates
Teams can then orchestrate swarms of AI agents that perform interconnected tasks, scaffolding a swarm of multiple AI agents.

“An [AI native approach to software development](https://thenewstack.io/what-is-an-ai-native-developer/) really changes the game. It breaks down traditional silos between roles and gets rid of repetitive tasks,” Bharadwaj said. “Imagine a world where every team member can do more than their traditionally assigned role. Powered by our Rovo agents, this creates a team of powerful generalists ready for an AI native world.”

Studio also allows teams to implement multiple issues at the same time, such as “generate unit tests for these four things,” and the agent will create four implementations, one for each issue, and move it to review, or even set up an automation.

Recently, Atlassian engineering had to update an API across 200 services. A custom dev agent raised 200 pull requests in one hour.

“People have ‘aha’ moments or ‘wow’ moments where they’re like, ‘Oh, I won’t need to do this type of task anymore.’ And that’s a huge mind shift. I have seen it in a positive light in every single case, because, as the capability of LLMs increases, we will be able to do more and more tasks,” Devenny said.

“At the moment, the tasks that we’re doing for developers are like repetitive tasks, ones that developers are not enthused about doing in the first place. Being able to remove that from their things that they have to do means that they get to spend more time focused on the tasks that they love implementing.”

Rovo dev agents are now in open beta for Atlassian customers on GitHub and Bitbucket. While in beta, there is no cost to the customer.

**Disclosure:** Atlassian paid airfare and lodging for the reporter to attend this conference.
[
YOUTUBE.COM/THENEWSTACK
Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.
](https://youtube.com/thenewstack?sub_confirmation=1)