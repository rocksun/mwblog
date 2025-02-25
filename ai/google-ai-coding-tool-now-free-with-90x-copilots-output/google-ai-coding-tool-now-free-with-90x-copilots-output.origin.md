# Google AI Coding Tool Now Free, With 90x Copilot’s Output
![Featued image for: Google AI Coding Tool Now Free, With 90x Copilot’s Output](https://cdn.thenewstack.io/media/2025/02/9760d8c8-steve-johnson-ugie9ddsmpu-unsplashb-1024x576.jpg)
Google has just released a free version of [Gemini Code Assist](https://codeassist.google/), its AI coding tool that up till now had primarily been available on paid business plans starting at $19 per month. Not only is Google opening up the tool to individuals for free, but it’s offering up to 180,000 code completions per month — a massive increase on the 2,000 code completions it main competitor GitHub Copilot offers.

I spoke to [Ryan J. Salva](https://www.linkedin.com/in/ryanjsalva/), a senior director of product management at Google Cloud, about the news. Prior to joining Google last year, Salva worked as a VP of product at GitHub for over four years. So he’s well placed to make comparisons with GitHub’s market-leading tool.

The 180,000 code completions per month is reminiscent of when [Google launched Gmail in 2004](https://cybercultural.com/p/002-the-early-years-of-readwriteweb/). Gmail’s most newsworthy feature at the time was the one gigabyte of storage space it offered — more than 100 times what Yahoo and Microsoft had. Google has almost matched that with the re-launched Gemini Code Assist, which offers 90 times more code completions than Microsoft’s equivalent GitHub product.

I asked Salva why they chose 180,000 code completions, a figure significantly higher than its competitors?

“We wanted to effectively offer a service that met the needs of 98-99% of developers who were banging on it all day.”

– Ryan J. Salva, Google Cloud
“Basically what we did is we looked at current usage of some of our professional engineers and how much they’re using it,” he replied. “We wanted to effectively offer a service that met the needs of 98-99% of developers who were banging on it all day. And so we set the cap at something that, where if you were exceeding that, you would have to be the most insanely dedicated engineer cranking into your code editor for many, many hours a day. And so the idea here is, make it so that it’s practically unlimited.”

Clearly this will put a fair amount of burden on Google’s AI compute infrastructure, but Salva pointed out that Google is “world renowned for being able to handle massive scale.” Who can argue with that, given Google’s experience scaling Gmail (not to mention search!).

## How Else Is It Different From GitHub Copilot?
Gemini Code Assist for individuals is globally available and is powered by [Gemini 2.0](https://deepmind.google/technologies/gemini/), Google’s latest LLM that is “built for the agentic era.” The tool “supports all programming languages in the public domain” and has been optimized for coding. From an LLM power perspective, this puts Gemini Code Assist on par with GitHub Copilot (the free version of Copilot is powered by OpenAI’s flagship model, GPT-4o).

Also like GitHub Copilot, Gemini Code Assist is available as an extension within VS Code and the JetBrains collection of IDEs.

But are there any key differences with GitHub Copilot, aside from the number of code completions?

Salva first pointed to the 128,000 token limit for chat in its free tier. According to [Google’s blog post](https://blog.google/technology/developers/gemini-code-assist-free/), “this large context window lets developers use large files and ground Gemini Code Assist with a broader understanding of their local codebases.” By comparison, GitHub Copilot offers a [64,000 token window](https://github.blog/changelog/2024-12-06-copilot-chat-now-has-a-64k-context-window-with-openai-gpt-4o/) when working with GPT-4o.

Second, Salva mentioned another new feature Google is announcing today: a code review agent available as a GitHub app, called [Gemini Code Assist for GitHub](https://github.com/apps/gemini-code-assist).

Those are the main differences on the free plan, but Salva noted there were more differences on the paid plans. One is the ability to pull data from remote repositories.

“GitHub is effectively incentivized to get people on GitHub,” said Salva. “You know, that makes sense — it’s their business. But there are a lot of organizations [that] are on more than just GitHub. Maybe they’re using GitLab, or they’re using Bitbucket, or they’re using an on-premise, that is to say a self managed, version of version control. […] We don’t have a source control management solution in the game, and so we will connect out to remote repositories.”

## Agentic IDEs and Other AI Dev Tools
I noted that a bunch of new [AI coding tools](https://thenewstack.io/self-driving-software-solver-launches-autonomous-ai-coder/) have come onto the market recently, with some claiming to be [agentic IDEs](https://thenewstack.io/beyond-dx-developers-must-now-learn-agent-experience-ax/) capable of creating an entire app from scratch. Three of the more intriguing examples: [Bolt](https://bolt.new/) was spun out of StackBlitz last October, [Windsurf](https://codeium.com/windsurf) was released in November, and [Lovable](https://lovable.dev/) launched in its current iteration in December (it was previously an open source project called GPT Engineer).

In response, Salva teased some further announcements coming in April and made this observation:

“What the industry is generally, you know, pursuing here is: how do we make batch changes across many files and reason not just over a single component, but entire systems? And that’s kind of when you get to agentic workflows.”

What all the latest AI coding tools have in common is that they’re targeted at individual developers, many of whom aren’t necessarily professional developers. [Bolt’s user base is 60-70% non-professionals](https://thenewstack.io/how-developers-are-using-bolt-a-fast-growing-ai-coding-tool/), Bolt CEO Eric Simons told me earlier this month. Google is clearly trying to muscle in on that same mainstream user base — its announcement post specifically mentions “students, hobbyists, freelancers and startups.”

“…our general approach is to think about the requirement doc and natural language as being the foundation.”

– Salva
There’s been a lot of talk about [English becoming the new default programming language](https://thenewstack.io/can-english-dethrone-python-as-top-programming-language/), and Google’s Ryan Salva seems to buy into this.

“I think our general approach is to think about the requirement doc and natural language as being the foundation,” he told me. “So that developers aren’t necessarily needing to come to it [Gemini Code Assistant] just with a knowledge of Python, or a knowledge of Java, or a knowledge of C#. They can think about what systems do I want to create, express that through natural language intent, and then *through that* produce outcomes or produce software.”

## A Foundation For More Agentic Features
Salva made clear that this is just the beginning for Google when it comes to AI-assisted coding tools for the masses.

“We’re laying the foundation for, how do we get just the basic tools and the IDEs out to as many people as possible, with really generous usage limits, and with effectively no requirement other than an email address.”

He hinted that its plans beyond today’s announcement will include “new agentic capabilities, as well as, frankly, AI not just in IDEs — but in a wide variety of other surfaces beyond the IDE.”

What those “other surfaces” are for AI-assisted coding remains to be seen. But for now, professional and amateur developers alike should go check out the new [Gemini Code Assist for individuals](https://codeassist.google/) and knock themselves out with those tens of thousands of code completions.

[
YOUTUBE.COM/THENEWSTACK
Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.
](https://youtube.com/thenewstack?sub_confirmation=1)