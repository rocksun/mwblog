For [OpenAI](https://thenewstack.io/openai-recovers-30000-cpu-cores-with-fluent-bit-tweak/) employees, asking a question even as seemingly simple as how many ChatGPT Pro users it has in one particular country can be surprisingly difficult, given that the needed data may be stretched be across multiple data sources, each of which is accessible in a slightly different way.

Overall, OpenAI has 70,000 different data sets, amassing 600PBs of new data daily. About 3,500 employees can access this data, using any 1 of 15 tools. The company has always kept close count of its users, but as it adds more regions and plans and features, tallying numbers becomes more difficult.

But each new query brought its own challenges. So analysts frequently found themselves in extended Slack conversations or even meetings with their peers just to figure out how to access the data.

“Simple questions shouldn’t be this difficult, or time consuming,” said [Bonnie Xu](https://www.linkedin.com/in/xubonnie/), OpenAI technical staff member on the data productivity team, [during a talk](https://ai.qconferences.com/presentation/newyork2025/ai-agents-make-sense-data-openai) at [QCON AI conference](https://ai.qconferences.com/schedule/newyork2025), held in New York last month.

Xu was there to discuss a tool the company created, called Kepler, to streamline this process.

Kepler is a helpful agent designed to answers questions for OpenAI employees, hiding the sometimes-many tasks it must undertake to find the answer.

Originally, Kepler was designed primarily for the data scientists at the company, but since its launch the user base has expanded to other personal in finance, human resources and other departments.

One Kepler user, according to Xu, actually said it was the closest they’ve experienced an AI system come to AGI.

## OpenAI’s Challenges in Internal Data Retrieval

For the business analyst, many of the database tables might appear very similar. One database may include logged-out users, while another does not. Some tables included encrypted users, while others do not and must have that data joined into the resulting dataset. Which one to use?

Writing the correct SQL code to extract the data can be difficult as well, especially if they involve joins across different tables.

“Missing one nuance can lead to an answer that is wrong by an order of magnitude, and this can be catastrophic when making important business decisions,” Xu said.

![SQL query](https://cdn.thenewstack.io/media/2026/01/e6807422-qcon-xu-01-1024x768.jpg)

Is this SQL query correct? Many managers would not be able to tell.

## Kepler in Action

Built in-house, Kepler is a data analyst, one that can tap all of OpenAI’s internal data stores to answer questions. OpenAI employees can interface with Kepler through Slack or through an IDE, such as [Cursor](https://thenewstack.io/cursor-2-0-ide-is-now-supercharged-with-ai-and-im-impressed/), or by integration with a specific workflow, or by mobile or other remote clients. In the background, Kepler uses GPT-5 to parse the request.

To provide an example of how Kepler works, Xu walked through a question about New York taxi travels times, She wanted to know which times during the day have the most variance in travel times, as well as which journeys are the “most unreliable,” meaning location pairs (origin and destination) where the variance between the shortest and longest travel times is the greatest.

The demo showed the “chain of thought,” or a series of evaluations and actions, that Kepler executed to answer this question.

First, it does an internal knowledge search, identifying two potentially relevant datasets, including a 2016 collection of NYC travel time data for taxis, which included pick up and drop off times, and the zip codes of both the destination and departure locations.

The agent then calculated the median time for each zip code, identifying the 95th and 99th percentiles.  The agent makes educated guesses on how to write the appropriate queries to get the needed information, testing each one, and soon finds one that works.

“You can imagine, doing this manually yourself takes a lot of time, but the agent is just going through these query and result steps on your behalf,” Xu said. When the queries appear to be correct, it sorts the results, then does some light formatting and even prepares a chart to present the data to the user. (The answers showed that rush hours and late nights are the most unreliable times.)

Another demo Xu provided showed Kepler working through a question of why there was a big spike in ChatGPT users in March 2025. It consulted a dashboard and a mission document to find the table that displayed this data. Kepler wrote different queries to try to pinpoint the sudden increase in usage, such as querying by region. It looked for errors, such as log data duplication.

The chain-of-thought identified a possible reason, namely the launch of a new generative image feature. They did a web search to cross-reference the hypothesis, finding the release notes and news articles on the launch.

Kepler stores all the questions, so you can pick up follow-up threads later on. When asked a follow-up question about taxi rides on February 14, Valentine’s Day, shows that the agent knows which tables and queries to use.

You can also interrupt Kepler if you see from its chain of thought that it is going in the wrong direction.

And since analysts tend to ask the same type of questions, such as product analysis and data validation, Kepler keeps sets of custom workflows for these sorts of questions

## How Kepler Works

At its core, Kepler is a set of APIs that communicate directly with ChatGPT (currently version 5).  Kepler also has direct connections to a set of pre-processed information, including an internal data knowledge base and an internal documents service. It can also make calls to data warehouses and other data services running on [Apache Spark](https://thenewstack.io/enhancing-the-flexibility-of-sparks-physical-plan-to-enable-execution-on-various-native-engines/), [Airflow](https://thenewstack.io/apache-airflow-3-0-from-data-pipelines-to-ai-inference/) and other platforms.

Using the [Model Control Protocol](https://thenewstack.io/model-context-protocol-bridges-llms-to-the-apps-they-need/) (MCP), invented by Anthropic, has been “so helpful” for Kepler, Xu said. Kepler uses the internal documents to understand how to query databases or perform other tasks on MCP. If the results didn’t come out as expected, it can then rerun the query with slight modifications. In effect, the Kepler agent is reasoning by itself.

“So instead of you giving the feedback, Kepler is running tools, then using the right tools to take the next set of steps, depending on whatever feedback that’s given,” Xu said.

Typically, agents running on their own can return wildly inaccurate results, but with additional context in hand, they can understand when something is wrong and try to vary their approach.

“So the really lovely thing is that Kepler can interactively explore the data itself, and content is carried over the whole time,” she said.

## The Importance of Metadata

Also helping build out the context is the metadata.

“It’s not enough to look at the table by itself, just as it is. You need to understand how the table was created and where it came from,” Xu said. This is the secret to the agent really understanding the differences between tables.

An offline job is run to compile this information about each table.

Much of this data has already been compiled by the company. Rich metadata about each database table has been captured, such as why it was created and what it is being used for, and even what its primary keys are.

![OpenAI metadata generation.](https://cdn.thenewstack.io/media/2026/01/983e792d-kepler-04-1024x768.jpg)

How OpenAI generates additional metadata from its own documentation.

It also uses [codex generation](https://thenewstack.io/openai-says-its-new-codex-max-model-is-better-faster-and-cheaper/) to build out metadata from the code itself.

“Since this is all refreshed periodically by an offline job, the context stays fresh without any manual involvement.”

If Kepler, or a user, finds an error, it saves the correction in memory.

“For us, memory is really the mechanism that helps the agent continuously learn and improve,” Xu said. “Contacts will get you maybe 80 – 90% of the way there. But sometimes you need those final little corrections that are really hard to just infer.”

![Kepler code](https://cdn.thenewstack.io/media/2026/01/daff4413-qcon-kepler-03-1024x768.jpg)

How Kepler saves corrections in memory.

To evaluate the quality of the answers, OpenAI runs an Eval Grader, which offers a score for each answer tested. It looks at how the delivered results differ from the expected or correct results.

In many cases, a correct answer may have a slightly different SQL query than what was expected, but the development team plans for this.

“When we compare resolve tests, we actually give a little wiggle room with things that don’t meaningfully impact the answer,” Xu said.

Users bring their own credentials to Kepler, thus ensuring they don’t see any data that they don’t have permission to see.

## Future Steps for Kepler

At present, OpenAI has no plans to open source Kepler or offer it as an enterprise product, Xu said, noting that she isn’t in the position to make these decisions.

Nonetheless, running an agent-based internal data analysis tool seems to bring a lot of value to the company.

“I think at least from what we’ve heard from our users, directly using Kepler is a lot faster. It’s more productive, just because when you’re looking at different sources, that’s a lot of stuff you have to do, and you have to connect the dots,” Xu said. “Kepler is really that layer on top, that abstraction that does it for you.”

*Videos of all the QCON AI talks will be available via a [Video Conference](https://ai.qconferences.com/video-only) pass, starting January 15.*

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://thenewstack.io/wp-content/uploads/2017/05/327440bd-joab-jackson_avatar_1495152980.-600x600.jpeg)

Joab Jackson is a senior editor for The New Stack, covering cloud native computing and system operations. He has reported on IT infrastructure and development for over 30 years, including stints at IDG and Government Computer News. Before that, he...

Read more from Joab Jackson](https://thenewstack.io/author/joab/)