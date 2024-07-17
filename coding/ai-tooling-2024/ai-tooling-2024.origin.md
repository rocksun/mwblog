# AI Tooling for Software Engineers in 2024: Reality Check (Part 1)
### How do software engineers utilize GenAI tools in their software development workflow? We sidestep the hype, and look to the reality of tech professionals using LLMs for coding and other tasks.
In April last year we published [The Productivity Impact of AI Coding Tools](https://newsletter.pragmaticengineer.com/p/ai-coding-tools) based on a survey of subscribers to this newsletter, about how new AI tools were helping developers with coding. Back then, ChatGPT and GitHub Copilot were the dominant tools and more [were on the way](https://blog.pragmaticengineer.com/github-copilot-alternatives/) during that time of experimentation.

Based on readers’ feedback at the time, the article advised playing around with AI coding tools to find out what worked or not, and predicted: “AI coding tools will move the industry forward.”

Fast forward to 2024, and AI coding tools are more widespread than ever. GitHub Copilot has passed 1 million paying customers (safe to assume mostly developers,) and there’s been a surge in startups building AI software engineering tools, along with no shortage of hype.

A recent peak of the AI hype cycle saw some startups raise funding to [“replace developers](https://newsletter.pragmaticengineer.com/i/142616988/is-the-ai-developera-threat-to-jobs-or-a-marketing-stunt) with AI engineers.” *This publication’s take on that “mission” and similar ones is that they’re overheated marketing slogans in response to the popularity of GitHub Copilot, and aren’t the reality.*

**But how are engineers ****really**** using these tools in 2024? **
In order to sidestep the hype and tackle that question, we recently launched a new survey asking software engineers and engineering managers about your hands-on experience with AI tooling; which tools are being used this year, what parts of the development workflow are AI-augmented, what works well, and what doesn’t?

As far as we know, this is the biggest survey yet on how tech professionals are using AI tools, and this publication’s business model means we’re free from bias on the subject. The volume of responses was such that it’s taken a couple of months to compile the data, but today we present it!

We analyze input from subscribers to this newsletter and seek to offer a balanced, pragmatic, and detailed view of where LLM-powered development tooling is today.

This article covers:

**Survey overview**. Most of the data in this survey is from software engineers, with a roughly even split between people working with AI tools for less than 6 months, between 6-12 months, or for more than a year.**Popular software engineering AI tools.**ChatGPT and GitHub Copilot remain the standouts in popularity. Google’s Gemini, Antrophic’s Claude, Jetbrains AI, Codeium, and others follow.**AI-assisted software engineering workflows.**Some of the most common workflows use Copilot in the IDE, chatting with AI bots instead of googling, AI-assisted debugging, and picking up unfamiliar languages and frameworks. There’s a long tail of helpful, innovative use cases.**The good.**When AI tools work well, they’re a massive help in completing projects, increasing test coverage, and making experimentation easier.**The bad.**Poor output, hallucinations, and devs over-trusting these tools, top the list of complaints.**What’s changed since last year?**Surprisingly, not too much! Interactive rubber-ducking is more common, and teams are experimenting more with AI agents.
*The bottom of this article could be cut off in some email clients. Read the full article uninterrupted, online.*
## 1. Overview
A total of 211 tech professionals took part in the survey, an increase on the 175 responses to [last year’s AI tooling questionnaire](https://newsletter.pragmaticengineer.com/p/ai-coding-tools).

**Positions: **most respondents are individual contributors (circa 62%.) The remainder occupy various levels of engineering management:
We asked engineering leaders additional questions because these people are in a great position to see the impact of AI tooling on teams. *We’ll cover the engineering leaderships’ views in a follow-up issue.*

**Experience: **The lengths of respondents’ careers is segmented into five-year periods, up to 20+ years of experience (YOE) in the tech industry:
Fun fact: one respondent had 60 years of professional development experience (!!) This developer is now semi-retired. His outlook on these tools – which he plans to use in the future – is positive, writing:

“I have seen many other technologies over the past 60 years that were touted as software developer eliminators. All of them failed to live up to the hype. This is a new age and AI looks like it may be a promising opportunity to push the boundaries in software design and development. Exciting time to be alive and see the future blossom before our eyes.”

**Time spent using AI tools: **again, a pretty even split between professionals who are new to using AI tools (6 months or less,) people who have used them for 6-12 months, and those who have done so for over a year.
Responses from people who don’t use AI tooling may seem a bit out of place in a survey about these tools, but we wanted to reach such developers and ask specific questions, in order to find out why some folks do not, will not, or cannot employ them. *We’ll dive into this in a future article.*

**Size of company:** a roughly even split in size from tiny businesses, all the way to mega-corporations. Companies with between 1-50 people are the majority.
## 2. Popular software engineering AI tools
ChatGPT and GitHub Copliot need little introduction as the market leaders in the software engineering sector. But exactly how popular are they, and which other tools do developers use?

#### The Tools
As just mentioned, ChatGPT and GitHub Copilot are heavily represented in the survey. The surprise was the degree of their popularity:

The responses reveal that as many professionals are using *both* ChatGPT and GitHub Copilot as all other tools combined! Below is a breakdown of this “other” category; note, the next most popular tool, Google’s Gemini, has only 14% of the mentions garnered by GitHub Copilot:

The difference in mindshare across respondents is significant, as becomes clear by visualizing all mentions together:

This chart lists all tools with at least two mentions in the survey. Those mentioned only once include Microsoft Teams AI, Amazon Q, Meta AI, Vercel’s v0.dev (UI generation from prompts,) Databricks AI assistant, Replit Ghostwriter, Ellipsis.dev (AI code reviews & bugfixes,) Mutable.ai (creating living documentation,) CodeRabbit AI (AI-powered code reviews,) StartCoder (code completion,) and Aider (AI pair programming in a terminal.) It’s great that so many tools are being tried out!

#### Favorite AI coding tools
We asked developers which tools are their favorites.

**GitHub Copilot and ChatGPT. **As the charts show, these got the most mentions. Here’s a selection:
“Github Copilot chat is the real deal.” – engineer at a dev tools startup

“I use GitHub Copilot because it also has built-in chat” – Ruby on Rails developer at a quality control software vendor

“I use GitHub Coliplot for daily coding and ChatGPT 4 for complex, open-ended design discussions” – a data engineer

“GitHub Copilot autocomplete is nice [but] I’ve found its chat function chat useless. It’s the same with the “generate code from description” functionality. When I need a leetcode function such as “partition array X based on Y”, I like using chatGPT, because it works fine. But ChatGPT gets stuck on harder problems. For example, building complex typescript generics is too much to handle.” – engineer at a scaleup

“I only use Copilot currently. I did use the free ChatGPT, and every so often I come back to it for something specific.” – software engineer at a cybersecurity startup

GitHub Copilot Chat is mentioned quite a lot, mostly positively. A big plus is that it offers an alternative to opening a browser to use ChatGTP. Still, not everyone is blown away by what the market-leading AI can do, including a senior software engineer who’s saltiness is hard to miss:

“My favorite is GitHub Copilot. It’s the least bad of all the AI tools I have access to.”

Another respondent shares that their company evaluated 8 AI coding tools and settled on GitHub Copilot, which seems to have an advantage with companies buying department-wide licenses, and developers moving over to it from other tools:

“I started off with Tab9. After that, my company supplied me with a free GitHub Copilot option, so I started to use Copilot!” – Ruby on Rails developer at a quality control software vendor

Several respondents say ChatGPT is the only tool they use, and that they like it. A software engineer at an eSports company shares:

“ChatGPT is where I go if I want to reason about something and I don’t have colleagues around me available.”

**Other tools** earned honorable mentions as some devs’ favorite tools:
– the Opus model – was mentioned several times as the best coding model. This was before the Claude 3.5 Sonnet model was released, which is much more proficient with coding tasks,[Claude](https://claude.ai/)[according to](https://www.anthropic.com/news/claude-3-5-sonnet)the Anthropic team, who uses this model to develop their own product; meaning we can expect Claude’s popularity to increase.The most mentioned after ChatGPT and Copilot. Several respondents reckon Gemini is better for coding tasks than ChatGPT, and prefer to use it over OpenAI’s chatbot. One respondent says they alternate between Gemini and Claude to gauge which one works better for each use case.[Gemini](https://gemini.google.com/).has several mentions as a favorite IDE, thanks to its code-aware autocomplete.[Codieum](https://codeium.com/)also gets several mentions, with one respondent calling it a “game-changer.”[Cursor](https://www.cursor.com/)and[Perplexity](https://www.perplexity.ai/?__cf_chl_tk=APpQg437C4fCJZbe8j8GXHNAuOXSZV7maVZal8F3Dfw-1720786519-0.0.1.1-8062)[Phind](https://www.phind.com/)**Other tools:**[Aider](https://aider.chat/)(pair programming in the terminal),[JetBrains AI](https://www.jetbrains.com/ai/),[AWS CodeWhisperer](https://aws.amazon.com/blogs/aws/amazon-codewhisperer-free-for-individual-use-is-now-generally-available/)and[Rewatch](https://rewatch.com/)(meeting notes) each had one mention
## 3. AI-assisted software engineering workflows
We asked respondents who have used AI tools for more than six months what an AI-assisted workflow looks like for them and/or their team. Some trends can be observed: