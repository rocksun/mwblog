What if there was an AI coding tool that had algorithms as sophisticated as TikTok’s? That thought experiment is now a reality, with today’s launch of a Chinese AI coding tool called [Verdent](https://www.verdent.ai/).

The founding CEO is [Zhijie Chen](https://www.linkedin.com/in/zhijie-chen-bytechen/), previously head of algorithms at ByteDance — where TikTok was created. According to Chen, Verdent aims to “redefine how software gets written.”

I conducted an email interview with Chen, to find out how his experience leading TikTok’s algorithm development helped him create this new AI coding tool. Chen was also previously chief technical architect at Baidu (2010-2019), so it’s no exaggeration to say that he’s one of the top internet technologists in China.

> “We see AI coding as merely the prologue of a much larger software revolution.”  
> **— Zhijie Chen, CEO, Verdent**

Before we get to the interview, a quick introduction to the product. It comes in two flavors: a plugin for Visual Studio Code and a desktop application called Verdent Deck. The plugin is “for developers who want to stay close to the code,” according to the company, while the desktop app is “for developers orchestrating multiple projects or large task batches in parallel.”

Paid plans start at $19 per month. (The New Stack’s [David Eastman](https://thenewstack.io/author/david-eastman/) will have a full tutorial coming shortly.)

## How Does Verdent Differ from Other Tools?

I started by asking Chen how Verdent is different from existing coding agents — such as [Cursor](https://thenewstack.io/install-cursor-and-learn-programming-with-ai-help/), [Claude Code](https://thenewstack.io/claude-opus-4-with-claude-code-a-developer-walkthrough/) and [OpenAI’s Codex](https://thenewstack.io/testing-openai-codex-and-comparing-it-to-claude-code/)?

“Verdent Deck is significantly different from Cursor or other AI-coding products,” Chen replied. “Basically, Verdent is a full-stack AI engine with parallel execution, customizable workflows and bullet-proof delivery — so every engineer works like they have their own elite AI team.”

One of the key features is what Chen calls “an adaptive feature called ‘Orchestration,'” which enables users to build their own workflows.

“Users can configure [Model Context Protocols] and sub-agents in our Orchestration section,” he added. “We also provide some built-in orchestrations for newcomers and they can use them conveniently.”

[![Verdent multitasking](https://cdn.thenewstack.io/media/2025/09/2662be8f-verdent-deck.jpg)](https://cdn.thenewstack.io/media/2025/09/2662be8f-verdent-deck.jpg)

Verdent multitasking.

## Applying Lessons from TikTok’s Algorithm to AI Coding

Now to the billion-dollar question: what lessons from TikTok’s famous algorithm did Chen bring to Verdent?

“Any cutting-edge recommendation system, such as TikTok, Facebook or YouTube, is a massive system engineering project,” he replied. “It doesn’t rely on a single all-in-one unified model, but rather has hundreds of models to model various objectives, such as likes, dislikes, etc.

“The largest models are even bigger than [large language models]. At the same time, there are various complex business logic and strategies inside, and the entire system may include millions of lines of code.”

> “AI-SWE products are also system engineering projects behind the scenes, not just problems that can be solved by wrapping an LLM shell.”  
> **— Chen**

“In fact, recommendation, advertising, and search scenarios are all algorithm-driven,” Chen continued, “and they follow similar system engineering patterns. Therefore, we believe the same applies to AI-software engineering scenarios. How do you quantitatively evaluate whether a task is completed well? How do you quantitatively evaluate product experience?

“This cannot be described by a single metric, nor can it be solved purely by relying on foundation models. Therefore, AI-SWE products are also system engineering projects behind the scenes, not just problems that can be solved by wrapping an LLM shell. There should be multiple models and strategies behind it to achieve the best product results.”

The “quantitatively evaluate” approach that Chen describes above is perhaps exemplified in another feature Chen told me about: real-time testing.

“At the result delivery stage, Verdent Deck gives users a comprehensive summary which includes code diff and verification results,” he said. “Each piece of summary is aligned with code diff, so that users can understand every code change easily. In order to deliver a more precise result, Verdent Deck also verifies code automatically and shows testing results to users.”

## Verdent’s Dual Products: VS Code and Desktop App

As noted, Verdant has two product forms: a VS Code extension and a desktop application. According to Chen, you can use both products simultaneously.

“When you need fine-grained collaboration with AI, you can directly use Verdent for VS Code,” he said. “When you have a task that you want the Agent to handle relatively independently, you can use Verdent Deck.

“Moreover, Verdent Deck and Verdent for VS Code can share agent memory, agent rules and user personalized task-related configurations, providing users with a consistent experience across different scenarios.”

[![Verdent coding](https://cdn.thenewstack.io/media/2025/09/eadb9391-verdent2.jpg)](https://cdn.thenewstack.io/media/2025/09/eadb9391-verdent2.jpg)

Verdent as a VS Code extension.

## The Typical Developer Workflow with Verdent

I asked Chen to describe the typical workflow a developer will have with Verdent — for example, what if they are using it to build a new app for their company?

A developer, he said, would start by providing a natural language description. For example: “Build a customer support ticketing system with user auth, real-time chat, and admin dashboard.”

The Verdent software then analyzes those requirements and proposes a structured task breakdown with architectural decisions. The developer would review this plan and, Chen said, “add constraints, modify priorities, set compliance rules.”

Then comes what he calls the “autonomous development” phase, which he described as follows:

* **Parallel execution:** Multiple Verdent agents work simultaneously on different components.
* **Real-time tracking:** Task dashboard shows progress (completed, in-progress, failed tasks).
* **Context awareness:** Agents maintain consistency across files, following existing patterns and architectural decisions.

[![Verdent in action](https://cdn.thenewstack.io/media/2025/09/d2db20b3-verdent3.jpg)](https://cdn.thenewstack.io/media/2025/09/d2db20b3-verdent3.jpg)

Verdent in action.

Following that is automated testing and code review — along with a “roadmap feature” called “verification loop,” where “failed tests trigger automatic fixes and re-testing until acceptance criteria met.”

The final step is the developer review, where the dev “can approve entire solution or request modifications to specific components.” There is git integration too, giving “clean pull requests with self-documenting commits and test coverage.”

## The Future of AI in Software Engineering

Verdent is pitching its new product as “a powerful new autonomous coding agent that’s built to change the way developers build software.” I asked Chen to expand on that — what is his vision for the future of AI-assisted coding?

> “Current [AI coding] systems are still far from touching the full scope of software engineering.”  
> **— Chen**

“Coding is just one part of the entire software engineering workflow,” he replied. “The entire digital world is built on the foundation of software. If AI only does coding, that only solves a small part of the software industry’s problems.

“At the same time, the significance and value of AI + SWE is not just about agents calling a few more tools. We see AI coding as merely the prologue of a much larger software revolution. Current systems are still far from touching the full scope of software engineering.”

He then talked about two separate “revolutions” in AI+SWE. The first, “AI-SWE as orchestrator,” appears to be what the present version of Verdent aims for.

“AI-SWE agents won’t just autocomplete code; they’ll act as planners and controllers across the entire software life cycle — design, development, testing, build, deployment, operations and upgrades. This turns them into workflow-level orchestrators, reshaping the entire software industry.”

The second revolution he labelled “AI-Native Infrastructure.”

“Software production and maintenance will shift from being human-centric to AI-centric,” he said, comparing it to how trains upgraded to high-speed rail.

> There will be a “future AI native programming language,” Chen predicted, along with programming languages that AI will itself generate.

“Today’s infrastructure — programming languages, frameworks, DevOps pipelines and engineering principles — was built for human comprehension, management and maintainability,” Chen said. “An AGI-level AI-SWE agent doesn’t need those constraints; it can operate through the most direct, high-bandwidth instruction channels.

“What we need is not ‘human tools translated for AI,’ but purpose-built, AI-native infrastructure designed for hyper-speed software creation and iteration.”

He suggested that there will be a “future AI native programming language,” along with programming languages that AI will itself generate. Another question as yet unanswered is: “What new software engineering principles will govern an AI-first industry?”

So Verdent clearly has grand ambitions and a long-term view of how AI will change software engineering. That said, Chen is appropriately humble about the present state of Verdent on its launch.

“Any great product is gradually refined through iteration,” he said. “To be honest, there will be shortcomings in the first version of Verdent, and we will listen to users’ genuine feedback to improve our product, so that Verdent can maximize developers’ efficiency.”

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://cdn.thenewstack.io/media/2020/03/1c7152c0-ricmac_highres_w400_h400.jpg)

Richard MacManus is a Senior Editor at The New Stack and writes about web and application development trends. Previously he founded ReadWriteWeb in 2003 and built it into one of the world’s most influential technology news sites. From the early...

Read more from Richard MacManus](https://thenewstack.io/author/richard/)