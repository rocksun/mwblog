Irish software engineer [Addy Osmani](https://addyosmani.com/) is not opposed to [vibe coding](https://thenewstack.io/vibe-coding-six-months-later-the-honeymoons-over/). And yet this [Google Gemini](https://thenewstack.io/google-launches-gemini-3-pro/) developer (who is also working on Chrome) has a keen sense of AI’s limitations too.

“We use vibe coding at Google as well — I find it great for prototypes, MVPs, really good for learning…” Osmani said on a podcast in early November. “But for the most part, vibe coding is prioritizing speed and exploration over things like correctness and maintainability.”

[![Addy Osmani shares Forrest Brazeal comic on Vibe coding vs rodeo cowboys](https://cdn.thenewstack.io/media/2025/11/21c50c0d-addy-osmani-shares-forrest-brazeal-comic-on-vibe-coding-vs-rodeo-cowboys.png)](https://cdn.thenewstack.io/media/2025/11/21c50c0d-addy-osmani-shares-forrest-brazeal-comic-on-vibe-coding-vs-rodeo-cowboys.png)

Osmani was [speaking on the podcast for Zed Industries](https://youtu.be/kvZGJVAZwr0?si=GBRpJBiB-_8GmxiP) (a company founded in 2022 to build tools for programmers — and to resurrect the popular Atom text editor as “Zed”). And he has a unique vantage point for how AI is impacting the coding world, both from watching Google’s adoption of AI tools, and from reports from around the industry.

Google CEO Sundar Pichai said [in April](https://abc.xyz/investor/events/event-details/2025/2025-Q1-Earnings-Call/) that “well over 30%” of the code that’s checked in at Google is “people accepting AI-suggested solutions.” That same month [CNBC reported](https://www.cnbc.com/2025/04/29/satya-nadella-says-as-much-as-30percent-of-microsoft-code-is-written-by-ai.html) Microsoft CEO Satya Nadella’s estimate that “maybe 20%, 30% of the code that is inside of our repos today and some of our projects are probably all written by software.”

But is AI creating more problems along the way, leaving coders to face longer code reviews and a new set of challenges as they try to solve the remaining bits, “the 70% problem”?

[![Addy Osmani interviewed by Richard Feldman - screenshot from Agentic Engineering (on YouTube)](https://cdn.thenewstack.io/media/2025/11/1d661ed0-addy-osmani-interviewed-by-richard-feldman-screenshot-from-agentic-engineering-on-youtube.png)](https://cdn.thenewstack.io/media/2025/11/1d661ed0-addy-osmani-interviewed-by-richard-feldman-screenshot-from-agentic-engineering-on-youtube.png)

## The Deceptively Convincing Nature of AI-Generated Code

In short, AI can rapidly produce much of the code for an app, for a feature, Osmani said on the podcast, but the scaffolding, the obvious patterns, can be just as time-consuming as it ever was. This includes crucial details like how to integrate with production systems, plus “your auth, your security, your API keys…”, as well as edge cases and things that need additional debugging.

Getting a UI with a few prompts is “deceptively convincing… You can get something that looks like it’s functional. But it can be held together with duct tape behind the scenes, for all you know.”

VIDEO

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

This may be reflected in the latest developer surveys. “While adoption is in a really good place, trust is surprisingly low, and it’s declining…” Osmani added. “There are lots of studies, including [Google’s] [DORA AI report,](https://cloud.google.com/blog/products/ai-machine-learning/announcing-the-2025-dora-report) which showed that while adoption is up, trust is really down… Favorable views about AI coding dropped from 70 to 60 percent within two years. And about 30% of people are reporting little to no trust in AI-generated code at all.

“Which is kind of wild, given how much we’re kind of relying on this now…”

[![Addy Osmani O'Reilly book cover - Beyond Vibe Coding (from Amazon)](https://cdn.thenewstack.io/media/2025/11/14fa5f4b-addy-osmani-oreilly-book-cover-beyond-vibe-coding-from-amazon-229x300.jpg)](https://cdn.thenewstack.io/media/2025/11/14fa5f4b-addy-osmani-oreilly-book-cover-beyond-vibe-coding-from-amazon-229x300.jpg)

In September, Osmani published a new book called “Vibe Coding: The Future of Programming.”

## Solving the ‘70% Problem’ in AI-Assisted Programming

So how should developers tackle that final 70%? Osmani says one fundamental step is “taking the time to go back and understand what was generated.”

Maybe there’s a newly popular software design pattern, Osmani suggests — the “two steps back” pattern. (“You’re feeling good” after using prompts in your favorite tool to generate a minimum viable product, and try “throwing two or three more prompts at it,” Osmani explains…) This typically leads to a point where small changes — say, fixing a bug — somehow make things worse.

“The fix is going to break something else, you’re going to ask AI to fix that issue, and it’s going to create two more problems. Rinse, repeat. Sometimes it’s *five* new problems.”

Besides having variable-validating checkbacks and the ability to rollback to prior states, Osmani thinks developers still also need to be prepared to modify their codebase themselves. “This starts with understanding the generated code.”

This ultimately suggests a larger problem with our workflows. He’s also read articles warning about “using AI as a crutch” — the possibility that we don’t understand more than just our current codebase. “Our fundamental critical thinking skills, our ability to learn from making mistakes, is kind of disappearing or it’s being eroded.”

At September’s [Lead Dev conference](https://leaddev.com/leaddev-new-york/) in New York, Osmani asked whether teams should try AI-free sprint days, “just to keep those skills sharp.”

But another idea is creating a file capturing decisions made along the way and the lessons learned, maybe by asking the agent to “distill insights after every single task”. For your AI agent, this forms a “compounding learning loop” — but it does more than just improve the quality of your next round of AI prompts. It’s become a kind of memory anchor for you, “a file that you can go back to and learn…”

## The Importance of Better Context Engineering

This leads to his next suggestion, which addresses the “70% problem” more directly. “I do find that investing in fully understanding what [context engineering](https://thenewstack.io/context-engineering-the-foundation-for-reliable-ai-agents/) means is really, really useful,” Osmani said. AI tools generate better code if they’re given all the relevant background on a project.

One [Anthropic document](https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents) points out that context includes message history but also system instructions, as well as external data and how tools are connected to external systems.

Osmani says it’s “making sure that your model, your agent, your tools have got all of the information needed to be able to successfully accomplish a task. It’s about going beyond just ‘prompting and praying’ to giving it as much information as you can optimally fit within your context window to increase the chances that things are actually going to work out well…”

“For a lot of the tools people are using these days, I think it is now a little bit easier to be able to pull in that context — so docs, URLs, examples, any of these markdown files that might have additional context about the problems or your codebase or how your team works.

“That is something I think is useful for people to also keep in mind if they’re trying to get beyond that 70% point.”

This also means that writing tests for code can become even more important, since they can double as a feedback loop for AI agents, Osmani said at Lead Dev.

Still, here the same caution applies: A human needs a strong understanding of any tests being generated by AI. “Tests are a safety net. They de-risk AI coding. And I tend to think that if you’re lucky, your team has been investing in tests for quite some time.

“If you don’t have decent test coverage, it’s perhaps not a huge surprise that someone’s going to say, ‘Well, yeah, we can just use AI to write the tests for us.’ And that’s okay, as long as there is still a human in the loop that is reviewing those tests.

“Because if you think you’re going to just prompt yourself out of the problem, I worry.” (He laughs.) “I worry for you, friend…”

## Does AI-Assisted Coding Really Save Time?

So in the end, are coders more productive using AI tools? Osmani has seen estimates based on self-reported productivity gains, an internal Google survey, and even metrics on the lines of code written by AI — but believes the true gain is… less than 2x. “This is a topic I feel very strongly about,” he says.

When someone on Twitter reports wildly higher numbers, “if you zoom in, often those are companies that are doing greenfield development on something completely fresh. They don’t have technical debt, they don’t have all of the baggage that usually comes with traditional software engineering, on something that is *real* and has existed for a while. And if you’re building something from scratch, you’re probably not going to have quite as much inherent complexity from the start.”

## How Code Review Is Becoming the New Bottleneck

How does that play out in the real world? “Maybe they can complete 20% more tasks than they could before. But we’re also starting to see side effects of some of these, too… Using AI to increase velocity means that more code is being thrown over the wall, and someone has to *review* it. We’re actually starting to see that code review is becoming the new bottleneck…. That’s going to be an interesting challenge, because we tend to have finite senior engineers, often, who are reviewing this code. And they’re going to have finite time… I don’t think the patterns for code review have fully evolved for this moment just yet.”

Having said all that, there are some ways AI can be truly useful. Agents are “actually really powerful as just a learning buddy” — maybe chatting with it on a break from coding, seeking fresh perspectives and better approaches. Osmani uses it when returning to an old codebase. “Sometimes you will think that you have a good mental model of how a system works, but there are almost always going to be things that you maybe missed or that other people added over time… Trying to use AI to form more of those connections — more of the nodes — I think can be really, really powerful, just as a learning aid.”

And after talking to different companies developing tools, Osmani says, “Something that is on the horizon is how can we start to offer proactive AI coding suggestions…”

Though he thinks it will take some time before tools like that could mature into something we’re using every day…

VIDEO

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

---

# WebReduce

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://cdn.thenewstack.io/media/2023/11/82081813-7zddypfe_400x400.jpg)

David Cassel is a proud resident of the San Francisco Bay Area, where he's been covering technology news for more than two decades. Over the years his articles have appeared everywhere from CNN, MSNBC, and the Wall Street Journal Interactive...

Read more from David Cassel](https://thenewstack.io/author/destiny/)