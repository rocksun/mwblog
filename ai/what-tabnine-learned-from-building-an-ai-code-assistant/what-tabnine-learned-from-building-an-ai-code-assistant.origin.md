# What Tabnine Learned from Building an AI Code Assistant
![Featued image for: What Tabnine Learned from Building an AI Code Assistant](https://cdn.thenewstack.io/media/2024/12/4452e337-boliviainteligente-kecrxz0m42a-unsplashb-1024x576.jpg)
Developers continue to be both [curious and sceptical](https://stackoverflow.co/labs/developer-sentiment-ai-ml/) about AI coding tools, but also ready to use them. Gartner says [14% of enterprise developers](https://www.gartner.com/doc/reprints?id=1-2IKO4MPE&ct=240819&st=sb) are already using AI coding assistants, a third of the developers in [Docker’s AI Trends Report 2024](https://www.docker.com/blog/ai-trends-report-2024/) are using AI for coding, 43% of coders (especially frontend, fullstack and cloud infrastructure developers) in the [Stack Overflow 2023 Developer Survey](https://stackoverflow.co/labs/developer-sentiment-ai-ml/) are already using AI tools.

Many of the developers using AI for coding are [copying and pasting from ChatGPT](https://www.docker.com/blog/docker-2024-state-of-application-development-report/) (which has the advantage of being free). When it comes to integrated code assistants, although [a slew of other assistants](https://redmonk.com/kholterhoff/2024/11/18/top-10-things-developers-want-from-their-ai-code-assistants-in-2024/) have come along since then, GitHub Copilot (the clear [leader in Gartner’s recent magic quadrant](https://github.blog/news-insights/company-news/github-named-a-leader-in-the-gartner-first-ever-magic-quadrant-for-ai-code-assistants/)) was [the most popular](https://survey.stackoverflow.co/2023/#section-most-popular-technologies-ai-developer-tools) tool in last year’s Stack Overflow survey.

The second most popular was what can be considered the original AI code assistant, Tabnine. It predates GitHub Copilot by about four years, has over a million monthly active users, and promises something enterprises say they value: [privacy and confidentiality](https://www.tabnine.com/code-privacy/).

You can deploy Tabnine as a service in your own cloud tenant or on your own infrastructure, train it on your own codebases (Copilot can use those for context, but doesn’t train or fine-tune on them) and have it use information from developers’ IDEs to add context (that includes details like the currently selected code, current and other open files connected repositories, conversation history, Git history, imported libraries, project metadata plus compile, syntax and runtime errors). You can also use it in multiple IDEs and with different source code management platforms.

Organizations can choose which large language model Tabnine uses (an [option ](https://github.com/marketplace/models)that GitHub Copilot has [recently introduced](https://github.com/newsroom/press-releases/github-universe-2024)). This includes a model that the company trained itself using only permissively licensed open source code.

Those are all things that enterprises say they care about, points out [Peter Guagenti](https://www.linkedin.com/in/peterguagenti/), president of Tabnine. “They’re concerned about privacy, because they’re concerned that the access to their systems will be used against them. Or at the very least, they’re allowing vendors to exfiltrate really critical customer and employee insights and their code, and they’re losing control over that when that happens.”

“Business stakeholders are demanding responsible approaches to the use of AI code assistants,” Gartner notes in its [Critical Capabilities for AI Code Assistants research](https://www.tabnine.com/gartner-critical-capabilities-ai-code-assistants/). Similarly, CIOs [say in surveys ](https://www.cisco.com/c/en/us/about/trust-center/data-privacy-benchmark-study.html?CCID=cc004881#~responsible-innovation)that copyright and license infringement are concerns that might even stop them from adopting generative AI code assistants, or at least make them [spend money protecting themselves ](https://www.gartner.com/en/newsroom/press-releases/2024-03-13-gartner-predicts-defensive-spend-to-derisk-ip-loss-and-copyright-infringement-will-slow-genai-adoption-and-diminish-returns)from claims. But in practice, those good intentions seem to take a back seat to performance.

“When we created our LLM, we only trained on permissively licensed open source code,” says Guagenti. “We knew we were doing something that was going to be inferior to the other things, but we figured that was the right thing to do for something we were putting our name on, and we could close the gap in its capability using private access to a customer’s code.”

“Everyone thinks the LLMs are the king, but they

[’]re not. Actually, they[’]re just the foundation of the house.”
— Peter Guagenti, president of Tabnine
Using the customer’s own code base as context, and for fine-tuning the model works well to improve performance, at least for large engineering teams, he claims.

“Everyone thinks the LLMs are the king, but they’re not. Actually, they’re just the foundation of the house. Really, the value in AI code assistants is not what the LLMs themselves do, but it’s in the context that’s applied,” he says.

Providing codebase awareness of what’s open in the developer’s IDE increases the rate at which coders accept the suggestions from the Tabnine assistant by 40%. Typically, customers look at Tabnine because of their privacy concerns, but the protected model is often the first thing they ask about because of those copyright concerns, he notes.

“Our last release of our protected model performs just as well as GPT 3.5 even though it’s trained on a considerably smaller corpus of data, and one that we can actually tell you — it[’](https://www.docker.com/blog/ai-trends-report-2024/)s all allowed.”

But GitHub Copilot now uses [GPT 4](https://github.blog/changelog/2023-11-30-github-copilot-november-30th-update/) (and GPT-4o for [chat and pull request summaries](https://github.blog/changelog/2024-07-31-github-copilot-chat-and-pull-request-summaries-are-now-powered-by-gpt-4o/)). “They look at Tabnine and the protected model performance versus Claude or [Command R+](https://docs.cohere.com/v2/docs/command-r-plus) or one of these others that are very strong, that have been trained on everything they can scrape.”

Guagenti characterizes the protected model performance as “seven out of ten.” “Claude and the others would be eight and a half out of ten, maybe nine out of ten if you really push the boundaries on it, but not a dramatic difference.” However, even the small difference in performance often turns out to be more of a priority than potential ethical issues. “When they see the difference, I will tell you, a surprising number say, ‘Ah, actually, we don[’](https://www.docker.com/blog/ai-trends-report-2024/)t care about license compliance anymore.’”

That pragmatism (which also [shows up in LinearB’s research](https://assets.linearb.io/image/upload/v1705960174/NewGenAI_ImpactReport.pdf?mkt_tok=MzE3LVVYVy00MTgAAAGQ4e6t2V1OWNXSELqVehBZY75w2he4kcnSufs9VBJFEqxyUp3LKVnighfQSSz7M1PLg70dwOoclNf7fQ60QQH42UGGK7LVIpYTJaOIFVG0), especially once organizations have deployed genAI coding tools) isn’t something to blame organizations for, he believes, because these are questions about what society decides is acceptable, while IT teams are asked to deliver high productivity and high performance at the most affordable price possible.

“The motives internally to choose these tools and use these tools are at odds with what we face when we talk about AI ethics, and this is no different than any other technology that came before it.”

The discrepancy doesn’t surprise [Kate Holterhoff](https://www.linkedin.com/in/kateholterhoff/), senior analyst at RedMonk, and it underlines the need to understand how these tools affect developer workflow and the code they produce.

“We

[’]re still at the ‘throw spaghetti at the wall to see what sticks’ phase of product development when it comes to code assistants.”
— Kate Holterhoff, senior analyst at RedMonk
“There is a real disconnect between what AI code assistant vendors anticipate developers wanting, and what practitioners actually use,” she explains. “We[’](https://www.docker.com/blog/ai-trends-report-2024/)re still at the ‘throw spaghetti at the wall to see what sticks’ phase of product development when it comes to code assistants, which is why it[’](https://www.docker.com/blog/ai-trends-report-2024/)s so important to attend to genuine developer sentiments expressed in, for instance, online forums and conference hallway tracks.”

## Making AI Coding Assistants More Successful
There are other paradoxes in working with an AI code assistant that knows more about your own codebase, rather than the aggregate of everyone else’s code, because the code you have may not be what you need to get the results you want. Organizations want to train on their own code to get the most relevant suggestions, but that almost certainly includes legacy coding practices you don’t want to replicate, so you have to select the parts of your codebase that work the way you want new code to work.

“[Imagine] I[’](https://www.docker.com/blog/ai-trends-report-2024/)m an organization, I have 30 million lines of code,” posits [Eran Yahav](https://thenewstack.io/author/eran-yahav/), co-founder and CTO of Tabnine. “7 million of them are legacy code that I don’t want anyone to ever see. I don’t want you to connect to that, I don’t want to train on that; I don’t want [the code assistant] to know that they even exist except maybe as a negative example.”

For most organizations, he warns, there are probably a lot more examples of legacy code, outdated libraries, obsolete artifacts and deprecated coding patterns than there are of the kind of code you want the assistant to suggest. Not only does code outlive multiple generations of employees — “nobody in the company knows what the code of 20 years ago does” — but whether it[’](https://www.docker.com/blog/ai-trends-report-2024/)s employees or generative AI blindly copying what there are the most examples of, it’s easy to end up with what he calls “new legacy.”

“New legacy is people who are new in the company creating new legacy code by looking at legacy code and imitating what appears in it,” Yahav explains. “The architect or the dev engineer manager is trying to eliminate some library or some API or some way of doing things, but because people see it pop up, whether through AI or search, and keep imitating that, they are creating new legacy .”

If a developer doesn’t know which version of a library to use (because the team doesn’t already have policies or a curated artefact repository), they’re likely to pick the one that’s already in other code they work with, and the same is true of training and fine tuning an AI model. “If you take an AI assistant and connect it to all the legacy information, whenever people ask how to do something they always get the old answer because that has the most examples. Unless you're carefully going to be drawn to this Jupiter-level gravity of legacy stuff.”

Even if that doesn’t introduce vulnerabilities that are fixed in newer versions of an artifact or mean that you’re breaching regulations that didn’t exist when the original code was written, you can end up mixing old and new approaches and getting something that’s not consistent with either.

Recency can be a signal, but the safest option is to train on and get AI assistance on relatively recent code that the development team is already familiar with, so they know how to evaluate the suggestions and then move on to what he terms “the shakier territories of legacy and old code”.

Adopting an AI assistant trained on your own code can make it worthwhile to make changes to that code that make it better as training data, because the return on investment is more visible with AI (especially if you track a full set of engineering metrics in tools like [Faros ](https://www.faros.ai/blog/is-github-copilot-worth-it-real-world-data-reveals-the-answer#results)or [LinearB](https://assets.linearb.io/image/upload/v1705960174/NewGenAI_ImpactReport.pdf?mkt_tok=MzE3LVVYVy00MTgAAAGQ4e6t2V1OWNXSELqVehBZY75w2he4kcnSufs9VBJFEqxyUp3LKVnighfQSSz7M1PLg70dwOoclNf7fQ60QQH42UGGK7LVIpYTJaOIFVG0)).

Some Tabnine customers have done non-trivial code refactoring and significant work on documentation to make code assistance work better.

“Getting in order wasn’t a priority, but now it feeds into another process [AI assistants] and it becomes more of a priority.”

— Eran Yahav, co-founder and CTO of Tabnine
“What helps AI also helps humans, so it’s not work just done for Tabnine,” Yahav points out, “It’s work done because by coming in we put up a mirror that reflected the state of the codebase.” Code quality doesn’t just mean fewer bugs: it also [improves developer productivity](https://arxiv.org/abs/2203.04374), because it’s easier to work with, but getting code out the door is often prioritized instead.

He’s clear this isn’t about criticizing existing code or the developers who wrote it, but about priorities, deadlines and available resources. “The reason code is not clean isn’t because people are stupid or lazy, it’s because they had to ship it and it worked. Getting it in order wasn’t a priority but now it feeds into another process and it becomes more of a priority.”

## Finally Prioritizing Documentation
Documentation is one of the areas that’s often under-resourced and usually out of date: developers might complain about it being missing but it’s rarely seen as a priority, and delivering it doesn’t usually get as much credit as writing code or fixing bugs. With AI, you can clearly see the value of adding documentation.

“I[’](https://www.docker.com/blog/ai-trends-report-2024/)ve seen people going in and adding documentation to key components that had zero documentation,” says Yahav. “That helps the AI but it also helps any human venturing into this project and trying to understand what[’](https://www.docker.com/blog/ai-trends-report-2024/)s going on. The universe becomes better [for humans] by adding this documentation, but that’s not the motivation. The retrieval system does a better job if it has this additional explanation of what[’](https://www.docker.com/blog/ai-trends-report-2024/)s going on that is not inferable from the code, that’s only known to the humans who wrote this piece of code.”

The documentation needs to explain the rationale for specific design choices rather than what the code does.

The documentation needs to explain the rationale for specific design choices rather than what the code does. “The AI knows what the code does: but why this design decision was made is some additional information that helps people who are using the AI get the full context of what this thing is or why it looks like it does.”

The information in that documentation becomes more valuable because it will show up, perhaps indirectly, in different contexts, where more people will find it useful than just a developer looking for how to do something, Yahav suggests.

Take JIRA (or any work management system), where issues function as implicit contracts for what work will get done. “The issues that people write [in JIRA] are typically not very elaborate. Developers hate writing them, obviously, and product managers, depending on the size of the org, also hate writing it, because it pins down the feature, and then the dev says, ‘Hey, this is much more than what you told me in the ticket, I'm not doing that.’. Everybody hates that contract of the JIRA issue.”

Tabnine can [automatically generate code to match a JIRA issue](https://www.tabnine.com/blog/introducing-tabnines-ai-agents-for-atlassian-jira/) like a story, bug or task (or validate that code actually captures the requirements in an issue and suggest code improvements if it doesn’t), using the text in the issue as the context for the code generated. “This is the first time that the developer actually has a vested interest in the issue having sufficient information for the AI. The more information they have in the ticket, the more the AI can help you.” That changes the dynamics of how people use the system because there’s now an obvious incentive to make sure it’s accurate and comprehensive.”

“This ‘issue-to-code’ automation isn’t an attempt to replace developers, Guagenti is quick to point out, describing it as suitable for simple use cases like straightforward React apps. “It’s not going to give you DoorDash; it’s not going to give you the really innovative stuff.”

Yes, AI code assistants can already deliver what he calls ‘ridiculous’ improvements with tasks they’re well suited to. “They’re taking 20% of the time they took before; there are 80% automation factors, 90% automation factors on certain tasks if you do it well.” That doesn[’](https://www.docker.com/blog/ai-trends-report-2024/)t mean you need fewer developers; it means developers can spend their time on more important things (and take the time to learn how to get the most out of the AI coding tools they use).

The [benefits Gartner identifies from using code assistants](https://www.gartner.com/en/documents/5298563) are as much about developer experience as basic productivity: reducing task switching and maintaining flow state, improving code quality and maintainability by helping expand unit test coverage, writing more consistent code comments and clearer pull requests — which in turn can reduce technical debt and let developers spend more time on high-value work.

“Anyone who thinks the software developer is just going to go away completely is fooling themselves.”

— Guagenti
AI, Guagenti suggests, “is just pushing the skill set up to allow us to make even bigger, more complex, more interesting applications.” Organizations and teams that get the most out of using AI code assistants will do it by investing in their developers. “We[’](https://www.docker.com/blog/ai-trends-report-2024/)re going to be expecting them to be more creative, to be more innovative, to be more capable and spend less time in hackery.”

“Anyone who thinks the software developer is just going to go away completely is fooling themselves. There are many, many things that we can fully automate, but somebody still has to design the system. Somebody still has to take the user requirement or the business requirement and turn it into a vision for a thing that actually solves that problem.”

[
YOUTUBE.COM/THENEWSTACK
Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.
](https://youtube.com/thenewstack?sub_confirmation=1)