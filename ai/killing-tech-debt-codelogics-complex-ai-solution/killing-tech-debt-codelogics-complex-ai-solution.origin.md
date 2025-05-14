# Killing Tech Debt: CodeLogic’s Complex AI Solution
![Featued image for: Killing Tech Debt: CodeLogic’s Complex AI Solution](https://cdn.thenewstack.io/media/2025/05/ef6452b5-tech-debt-mud-2-1024x576.jpg)
MIAMI — [Edwin Gnichtel](https://www.linkedin.com/in/ned-gnichtel-12039965/) has seen some big balls of mud in his time — and by balls of mud, he means legacy applications and IT systems.

Gnichtel is the CEO of [CodeLogic](https://codelogic.com/), a software intelligence automation platform that’s deploying AI to resolve technical debt. Previously, he was CodeLogic’s chief technology officer and has also worked in [low-level software engineering](https://www.technologyandstrategy.com/news/what-is-a-low-level-software-engineer).

It’s so bad, it’s difficult to graph, he told the audience at Tuesday’s [Infobip Shift Miami](https://shift.infobip.com/us/#hero), a developer conference focused on AI.

“Why do we have 75,000 classes?” He asked. “That’s a real number out of a real system. It was just one system, by the way, that was part of much larger ecosystem of systems.”

## Development Causes of Technical Debt
There are many causes of [technical debt](https://thenewstack.io/technical-debt-continues-to-mount-heres-how-to-solve-it/) in development work. He blamed [Agile](https://thenewstack.io/agile-reinvented-a-look-into-the-future/) for adding to debt through its endless push to production, adding that while he’s a proponent of Agile, its focus on rapid delivery accelerates technical debt by prioritizing features over code quality.

Additionally, he pointed to systems built on outdated frameworks. Plus, nobody really does system architecture any more, he added. He also blamed [misinterpretation of microservices](https://thenewstack.io/how-to-fail-at-microservices/).

“How many organizations think that like taking the existing thing that they have and just shutting it into a container suddenly, magically made that a microservice?” he asked rhetorically.

He showed a knowledge graph of a smaller application with a “mere” 5000 classes, 34,000 methods, 300 tables, 4700 SQL functions and countless edge connections in the form of class derivation and method-to-method calls.

![A blob of pastel colors that represents an IT application.](https://cdn.thenewstack.io/media/2025/05/3c9d92e6-code_debt_visualization.jpg)
A graph of a small application’s many dependencies.

“When you get to a bigger application, there’s no way I can even visually represent it,” he said. “[It] would just be a blob of color on the screen.”

## AI’s Role in Technical Debt
Into this muddy mess, we’re adding AI-generated code.

“AI has potential to make this spectacularly worse,” he said. “It’s written on top of a whole bunch of garbage [which] does not make for a great outcome, ultimately. So we’re driving a technical debt.”

Organizations are dealing with endless code maintenance. Put simply, it’s no longer a problem humans can solve, he argued.

But maybe AI can.

CodeLogic’s approach is to first map the complexity of a system by using an AI agent to create a large knowledge graph.

“In many cases, tons of dependencies really only become visible when the code is executed — things like, for example, procedurally generated connection objects, certain types of constructed database queries, all sorts of things like that,” he said.

Execution environments, interpreters and build environments that includes compilers love to inject things, he added. For instance, [Java](https://thenewstack.io/java-modernizes-new-tools-for-ai-and-quantum-age/) uses lambdas. Lambdas don’t really exist, he said. When you look at the byte code, it’s just converted into classes and methods, he explained.

“It’s a figment of Java’s imagination,” he said.

All these dependencies have to be captured, he added. CodeLogic’s data model, which sits underneath the product, offers a differential analysis and provides impact information to help the company understand how everything is connected.

## Complex Solutions With AI
CodeLogic’s use of multiple models shows how complex systems can be built with AI.

CodeLogic had always planned to use machine learning and other AI technologies, but what they hadn’t anticipated is how quickly the models would improve once they stacked models, deployed an MCP server, and used other techniques for improving [large language models](https://thenewstack.io/what-is-a-large-language-model/).

“It allowed us to really fast forward on this problem,” he said.

[Retrieval Augmented Generation](https://thenewstack.io/retrieval-augmented-generation-for-llms/) with an MCP server allowed them to “talk” to the LLMs, to point to the code that has to be reviewed. An impact analysis reveals all the parts that a rewrite could potentially impact, including pieces that are multiple “hops” away, such as REST endpoints, API boundaries and databases.
The process is not always straightforward and can involve re-prompting and checks against the CodeLogic system to understand what the AI knows. It should be tracked to ensure it doesn’t break dependencies, he said. A human in the loop is also needed to approve the changes.

CodeLogic creates a multigraph differential analysis that can start generating all the necessary disk sets. That gets interpreted by a model, which then generates a differential set. The differential set is interpreted by yet another model, which generates sets of prompts and tickets.

Those can be placed into [JIRA](https://thenewstack.io/why-developers-hate-jira-and-what-atlassian-is-doing-about-it/) so that the AI can be held accountable for closing tickets.

“At the end of the day, the key piece is it writes the prompts as well,” he said. “Those prompts can get pretty sophisticated, and then that gets shoved right back into the augmented AI on the generation side, the code generation side, which then allows you to have all that get done.”

The final piece is helping developers to [stop creating technical debt](https://thenewstack.io/stop-technical-debt-before-it-damages-your-company/). For instance, a developer can ask the CodeLogic system what happens if a particular version of the library is introduced.

“We have functionality around our annotation language where, if you make a change, people get notified [and] slaps on the hand occur,” he said.

[
YOUTUBE.COM/THENEWSTACK
Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.
](https://youtube.com/thenewstack?sub_confirmation=1)