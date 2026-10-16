**Every time an AI agent has to trawl Slack threads**, Jira tickets and old pull requests to piece together something a company already knows, the customer pays for that work again. [Uvi](https://www.uvi.io/), an Israeli startup that emerged from stealth on Wednesday with $7.5 million in seed funding from investors including CT Innovations, Cardumen, Mana VC and 91 Ventures, says this repeated context-gathering is quietly inflating the cost of running agents on [frontier models](https://thenewstack.io/open-weight-models-frontier-costs/).

The firm says in-house agents built on frontier models, connected directly to six company systems, cost roughly eight times more than they needed in internal testing, mostly because of repeated context gathering rather than actual reasoning.

## Developers are paying for amnesia

Uvi co-founder and CEO [Gilad Salinger](https://www.linkedin.com/in/gilad-salinger-15650b127/) tells *The New Stack* that models are rented, but context is owned.

“Developers are paying frontier prices for amnesia,” Salinger says. “Every quarter there’s a new model that is faster and cheaper, and every quarter the company’s memory of why it built things the way it did stays exactly where it was: in people’s heads, in old tickets, in Slack threads nobody will read again.”

He explains that Uvi takes that memory out of people and tools and puts it in one place every agent, on every model, can read. If developers need to swap the model tomorrow, they don’t have to relearn anything. Salinger insists that Uvi makes sure that memory information is actually usable.

> “Context is unique to every company and demands a deep understanding of how that company defines its work, from what counts as a feature to how two departments communicate.”

## Working through “both sides” of agent testing

In terms of core mechanics, Uvi champions a semantic layer, a knowledge graph, and a reasoning layer that sits on top of relevant, permissioned, tightly synchronized live data. The Uvi team tested its platform against more than 900 real employee questions, according to the company, using the same frontier model on “both sides” of the test. The tests are internal and not independently verified.

“Both sides” means two different ways of building an AI agent, using the same frontier model to answer the same questions.

“On one side, we had an agent connected directly to six enterprise systems, including [Slack](https://thenewstack.io/slack-code-agent-channels/), [Jira](https://thenewstack.io/atlassian-jira-coding-agents/), and [GitHub](https://thenewstack.io/github-2-9b-monthly-commits/). Every time someone asked a question, it had to dig through those systems, piece the information together, and figure out how it all connected before it could answer. That took 15 to 35 round trips per question,” clarifies Salinger.

On the other side, he explains that his team used an agent with Uvi, so it used the same model and asked the same questions with the same company information.

“Uvi had already connected the dots between the company’s decisions, conversations, code and processes, so the agent got its context in one step,” Salinger says. “The first agent was doing detective work every time someone asked a question. The second already had the case file. And here’s the ridiculous part: The first approach cost roughly eight times more and took more than twice as long. We weren’t comparing a stupid model against a smart one. We were comparing the same brain with and without an understanding of the business it was supposed to work for.”

## How much more expensive is 8x, exactly?

Built the way most enterprises are building today, Uvi claims an answer costs $0.75 to $1.41 and can exceed $2.00. Built on Uvi, the same answer costs $0.10 to $0.16. On open-ended questions where agents got stuck in search loops, Uvi claims to be up to 46 times cheaper.

If Uvi’s claimed results hold water, Salinger thinks the real shame isn’t cost; it’s the lost opportunity to stay at the vanguard of business.

“The real worst case is not waste. It is losing the race,” he says. “Enterprises today compete with other players who can flip an entire market overnight. A software-centric company’s only lasting advantage over AI labs is the information nobody else has. So if it cannot turn that into something agents use quickly, safely, and precisely, the advantage is theoretical. We are at the point where companies understand the cost and energy it takes to build that environment themselves and stay competitive. That is the moment this category exists for.”

## Developers floundering in tokenmaxxing context blindness

All of this raises the question: is the AI industry missing a trick, or is there widespread awareness of a predicament that leaves some developers floundering in tokenmaxxing context blindness?

**“**They [the frontier model companies] know. You do not set up consulting arms for large enterprises unless you understand that context is the whole game,” Salinger says. “Look at the shape of their business: a huge market to serve seamlessly at scale. Context is the opposite. It is unique to every company and demands a deep understanding of how that company defines its work, from what counts as a feature to how two departments communicate. That does not scale the way a model does.”

Salinger explains that Uvi’s approach does two things at once: it works to understand the information and the connections between pieces. This means (for example) that a question about a billing exception pulls the decision, the people, and the dependencies, not every document that mentions billing. Uvi understands each organization and its specific way of working, so the same question gets answered differently inside two different companies.

> “The first agent was doing detective work every time someone asked a question. The second already had the case file.”

That combination is what lets this platform hand the agent the “smallest correct slice”, at the speed, security, and precision an enterprise expects. Of course, diminishing returns exist at this level, Salinger agrees, so he notes that Uvi’s job is to find the point of enough, per question, per company.

## Additional Uvi integrations are in development

Most of what a company knows was never captured in a single document. A decision may begin in a Slack thread, become a Jira ticket, change in a pull request, and end up behind a feature flag, with no individual system holding the full story. Uvi maps how those pieces connect and reconstructs what was decided, why, what changed, and what happened next.

It then makes that context available to whatever models and agents the company chooses to run. Without that history, an AI agent can confidently recommend the same migration a company rejected three years ago for the same reasons.

> “The real worst case is not waste. It is losing the race”

Uvi says that its software runs in production at Lemonade and [monday.com](http://monday.com/), both public companies, and at Melio, now part of Xero. It connects to Slack, codebases, coding sessions, meeting notes, Jira, and Confluence, with additional integrations in development.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://cdn.thenewstack.io/media/2026/02/684dae45-cropped-e991646b-06_rpa_inline_01_bridgwater-1-1-300x234-1.jpg)

Adrian Bridgwater is a technology journalist with three decades of press experience. He has an extensive background in communications, starting in print media, newspapers and also television. Primarily working as an analysis writer dedicated to a software application development ‘beat’,...

Read more from Adrian Bridgwater](https://thenewstack.io/author/adrian-bridgwater/)