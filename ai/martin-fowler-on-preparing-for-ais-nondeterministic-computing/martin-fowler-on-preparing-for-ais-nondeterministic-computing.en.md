[Martin Fowler](https://www.martinfowler.com/), Thoughtworks chief scientist and long-time expert on object-oriented programming, views AI as the biggest shift in programming he has seen in his entire career.

In an interview on the [Pragmatic Engineer](https://www.youtube.com/@pragmaticengineer) podcast, hosted by [Gergely Orosz](https://www.linkedin.com/in/gergelyorosz/), Fowler admitted about AI that, “We’re still learning how to do this.”

The closest parallel for the industry would be the shift away from assembly language.

Assembly language was tedious to write, as much of the work involved moving memory values across registers. That’s why the move to higher-level programming languages (such as [COBOL](https://thenewstack.io/20-years-in-the-making-gnucobol-is-ready-for-industry/) and [Fortran](https://thenewstack.io/how-john-backus-fortran-beat-machine-codes-priesthood/)) was such a blessing for programmers.

“At least in a relatively poor, high-level language like Fortran, I can write things like conditional statements and loops,” Fowler said.

These new languages were a higher level of abstraction than the hardware itself.

With large language models (LLMs), it’s a “similar degree of mindshift,” he said.

## Deterministic vs. Nondeterministic Computing

But it is not that LLMs are another abstraction, but that they are a different type of computing altogether.

Namely, LLMs are a form of nondeterministic computing, which has different characteristics than everything we consider as “computing” today, which is deterministic computing.

Deterministic computing is strictly binary. A calculation is either correct or it is wrong. If it is incorrect, we can debug the code to see where it went wrong.

Nondeterministic computing is fuzzier. An LLM may produce one answer at one point, and another entirely different answer another time. The answers it builds rely on [statistical reasoning](https://thenewstack.io/how-to-generate-ai-from-a-database-bruce-momjian/), a set of probabilities built on top of binary math, but not as foolproof.

It completely changes how you have to think about computing, he said.

## Where AI Is Working

[Thoughtworks](https://www.thoughtworks.com/about-us) is a technology-driven consulting company, and so it has been keeping an eye on how AI has been used successfully.

One use case, according to Fowler, has been for quickly knocking up prototypes, thanks in part to the emergence of [vibe coding](https://thenewstack.io/why-there-might-be-something-to-vibe-coding-after-all/). Here you can explore an idea “much more rapidly” than you could before.

But the real killer app has been using AI to help [understand legacy systems](https://thenewstack.io/agent-infused-mongodb-tackles-application-modernization/). On the company’s most recent [annual Radar report](https://www.thoughtworks.com/en-us/radar) (#33) of emerging technologies, using generative AI (GenAI) to modernize legacy systems was the single AI technology that got the company’s highest “Adopt” rating.

For its customers trying to modernize old systems, Thoughtworks has created a routine that basically semantically analyzes the codebase, putting the results in a [graph database](https://thenewstack.io/common-uses-cases-for-graph-databases/), which can then be interrogated with a [Retrieval-Augmented Generation (RAG) process](https://thenewstack.io/vector-processing-understand-this-new-revolution-in-search/) to understand how the application runs.

“If you are doing any work on legacy systems, you should be using LLMs in some way to help you,” Fowler said.

## Harder Problems for AI

But while LLMs can help us understand legacy code, whether they can modify that code in a safe way is another question.

Higher-level programming remains dodgy with LLMs, however. Here you have to break AI work into very thin “slices,” and review everything very closely, he said.

“You’ve got to treat every slice as a [pull request] from a rather dodgy collaborator who’s very productive in the lines-of-code sense of productivity, but you know you can’t trust a thing that they’re doing,” Fowler said.

Nonetheless, using AI in this way can save developers time, though maybe not as much time as the [advocates have been claiming](https://thenewstack.io/ai-coding-tools-in-2025-welcome-to-the-agentic-cli-era/).

In particular, he advised us to “come up with a more rigorous way” of speaking to the LLMs, in order [to get better results](https://thenewstack.io/ignore-prior-instructions-ai-still-befuddled-by-basic-reasoning/). [Domain-driven design](https://thenewstack.io/celebrating-20-years-of-domain-driven-design-ddd-and-eip/) (DDD) and [domain-specific languages](https://thenewstack.io/rethinking-data-integrity-why-domain-driven-design-is-crucial/) may offer a way forward.

## AI’s Similarities To Mechanical Engineering

The practice of structural engineering can also be helpful in better gauging where to use AI, Fowler pointed out.

“My wife’s a structural engineer. She always thinks in terms of the tolerances: ‘How much extra stuff do I have to do beyond what the math tells me because I need it for tolerances?'” Fowler said.

Just as we know how much weight a concrete bridge can take, so too should LLMs come with metrics describing the levels of precision they can support.

“What are the tolerances of nondeterminism that we have to deal with?” he asked. Knowing this, software developers will know where “not to skate too close to the edge.”

One book Fowler recommended to software developers to help think about nondeterminism is [“Thinking, Fast and Slow,”](https://www.goodreads.com/book/show/11468377-thinking-fast-and-slow) by Daniel Kahneman.

“He does a really good job of trying to give you an intuition about numbers, and spotting some of the many mistakes and fallacies we make when we’re thinking in terms of probability and statistics,” Fowler said.

As always, Fowler is an eloquent speaker, and had some insights across a variety of subjects in this interview, including refactoring, agile processes, LLMs in the enterprise, patterns of enterprise application, and, of course, every object-oriented programmer’s favorite language, [Smalltalk](https://thenewstack.io/the-big-impact-of-smalltalk-a-50th-anniversary-retrospective/).

Enjoy the entire talk here:

VIDEO

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://thenewstack.io/wp-content/uploads/2017/05/327440bd-joab-jackson_avatar_1495152980.-600x600.jpeg)

Joab Jackson is a senior editor for The New Stack, covering cloud native computing and system operations. He has reported on IT infrastructure and development for over 30 years, including stints at IDG and Government Computer News. Before that, he...

Read more from Joab Jackson](https://thenewstack.io/author/joab/)