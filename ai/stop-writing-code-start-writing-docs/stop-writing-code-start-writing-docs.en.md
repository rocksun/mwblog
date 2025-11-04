For this episode of The New Stack Agents, TNS Publisher Alex Williams and I talked to [Keith Ballinger](https://www.linkedin.com/in/keithba/), the vice president and general manager of the Google Cloud Platform Developer Experience group.

Ballinger is one of those rare executives who still frequently codes and who is also deep into building and using the latest [agentic coding tools](https://thenewstack.io/expectations-for-agentic-coding-tools-testing-gemini-cli/). Unsurprisingly, we spent some time talking about [Gemini CLI](https://thenewstack.io/gemini-cli-googles-challenge-to-ai-terminal-apps-like-warp/), Google’s direct competitor to products like Claude Code and Gemini’s Codex, and one of the key products Ballinger is currently responsible for.

VIDEO

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

But what’s maybe even more interesting is his take on how to get the most out of these agentic tools, which Ballinger believes are still in “their first inning.” In his view, it’s important to slow down to speed up the process: developers should write clear guides for the agents, focus on architecture (and document it) and create a project plan.

Too often, he said, developers still try a one-shot approach, but that doesn’t provide the models with enough information about the developer’s intent and the overall context of the problem they are meant to solve.

Ballinger also believes that in the long run, we may get to a place where the majority of developers won’t need to look at the code at all. The history of programming languages has been one of increased abstraction. The next abstraction layer, he told us, “is essentially my intent — what I want, and how that comes together to make an experience, to make an application.”

He acknowledged that this is a bit controversial and that he generally has a “very optimistic opinion that’s probably in the minority.”

Check out the full conversation above, including a discussion of Keith’s career at Microsoft, Xamarin and GitHub, his Conductor framework for guiding agents, and why great programmers are also great writers. You can also see more episodes of Agents by subscribing to our podcast on YouTube or other podcast platforms.

What follows are some of the highlights of our conversation, lightly edited for clarity.

## The Early Days of AI Coding

**Alex Williams:** I was asking about how Keith, you really started to use AI. You were saying before our recording, that a lot of people just don’t know how to use it, and they’re using it in a very single-shot kind of way. What have you learned about that now, and tell us about those early days when you were first getting started?

**Keith Ballinger:** Yeah, it’s interesting. While I’ve always been involved in developer tools and technologies, as a teenager I was an email penpal of Marvin Minsky. So I had the AI bug very early in my life. I put together a hack team in 2012 or something for Bayes Hack, which did machine learning for nonprofits. So I’ve always been really interested in that world. [*Editors note*: *Bayes Hack was the hackathon of [Bayes Impact](https://www.bayesimpact.org/en).*]

Then at GitHub, we started building Copilot. The idea there was that OpenAI had come along and finally had a pretty good model that, funny enough, they called Codex at the time, and it could do coding tasks pretty well if you managed it carefully. The very first thing we did was purely code completion. There was chat soon after. And interestingly, I think starting with code completion, starting with something very interactive, was very useful in understanding how people would use AI and getting them comfortable a little bit with it.

Then people started using the chat. Some people go to ChatGPT or Gemini, even today, to do AI coding. Then, of course, agents came along, right? Where all of a sudden, the model was doing things on your behalf with tool usage. That was a really interesting growth in our industry.

I kind of followed along on it. I remember maybe mid-last year, tool-using models started really taking off. You think about people like Cursor, all of a sudden they were able to make a dent because they weren’t just code completion and they weren’t just chat. All of a sudden, they were doing these semi-autonomous tasks for you with tools.

It was funny, because up until then, for like a year prior to that, I would just use chat. So I would go to Gemini — we called it Bard at the time— and I would tell it what I wanted to do, and then it would come back and give me code, and I would take that code and I would paste it into my project.

But it would also tell me to do other things, like run a test and give it the output of the test. I was basically acting as the tool for Gemini, for the model itself. And then once that was automated, all of a sudden you could do things so much more quickly, and it really expanded what you could do.

## Best Practices for Working With Agentic Coding Tools

**Ballinger:** One of the things I’m seeing in the industry right now is there’s a big variance in people understanding what the best practices are, and even maybe what the best practices should be. That’s something I think we have to do more education on, to help people understand how to use AI for coding assistance.

Because if you just single-shot stuff, you’re not going to really be successful. You have to treat the AI kind of like a coworker. And if you follow best practices from development in general — things like writing a user guide or a spec, things like writing a technical design, creating a project plan — just those three things, if you do that when you interact with AI, which you should do anyway on anything complex, you actually have really great results with AI.

**Frederic Lardinois:** I was thinking about this: it’s still all very verbose, and we see similar projects right where we get `agents.md` files. Do you think that is just an intermediate step right now in a different direction, where we don’t have to do that anymore?

**Ballinger:** I’m not sure of that. I hope not. I think I like creating things. I like being a craftsman and creating things, and I want to be involved with that. I don’t necessarily want to write every line of code and debug every test failure or whatnot, but I like the act of creation.

And for me, the act of creation is thinking of a problem I want to solve and then thinking about how I want to solve it. I think AI could probably do that as well, but you still have the problem of, “How do I as the AI, or how do I as a human, give you enough of what I want without the AI?”

You have to do that somehow. It can’t read your mind, at least not yet. And if it doesn’t read your mind, then you can’t get that. And I want to be involved in that part.

## On Keeping the Agent on Track

**Williams:** How do you then make sure that it’s working correctly? Often, when you put in a prompt and then the output that you get from the prompt, and then you apply it to your dev environment, it doesn’t really work very well. So how are you verifying everything?

**Ballinger:** The way I do that is I use the AI to help me with that. So I don’t look at every line of code. With something like Aether [*Editors note*: A*ether is a programming language for LLMs Ballinger created as an experiment.*], I created that architecture doc.

I did collaborate a lot with it. The task plan was very minute, and after each task, I basically had it do like test-driven development — it was like TDD. It would write tests, and then it would implement the feature until the test passed.

I did spend time looking at that. I would look a lot at the tests, but I also spent probably most of my time looking at the examples. I had to create a bunch of examples covering all kinds of scenarios — file I/O, HTTP, simple memory management things — and those examples, I made sure always ran.

So after any task that was done, I would make sure the examples ran, all the tests passed, and I would make sure the AI was doing those things too. In some sense, it’s a black box to me.

All I really care about is, in the end, did it work? At times, I’d go casually inspect things as well.

## The CLI Resurgence

**Lardinois:** Why do you think the CLI has become so popular again lately? Pretty much all of these agents have some kind of CLI version at this point. Why is that?

**Ballinger:** I think, honestly, we never abandoned the terminal. I think that’s part of it. We didn’t think about the terminal as a primary interface. More and more, people would go to the terminal to run things like npm or just other commands like ls or whatever. But we didn’t think about it as our primary interface.

More and more, there used to be a rich ecosystem of TUIs—terminal user interfaces—like Midnight Commander, right?

**Williams:** I’m old enough to remember.

**Ballinger:** Yeah, right. And it’s interesting — we just kind of stopped thinking about those and just had command-line scripts. But we always use the terminal, and especially in modern development, especially where there’s so much [open source software], people use the terminal for git.

So it was really natural to use the terminal as a way to do these things. It gives you a lot of control. It focuses on the job to be done versus lots of UI. It focuses you in on what you need to do. And it just kind of follows along with what you’re already doing or what you have been doing.

**Williams:** The CLI is an interesting topic now in the world of AI, as Frederic is noting. I’m curious about how you see the terminal itself evolving. I mean, the Gemini CLI brings AI directly into it, doesn’t it?

**Ballinger:** Yeah, I think it’s a really interesting question: Will the terminal evolve to be more AI-capable itself, or will there just be more and more AI-capable or influenced command tools within it?

A year ago, I built a prototype of kubectl. I built an extension for it called kubectl AI. The team rewrote it — my code was awful — but it’s now part of kubectl core. You can give it a natural language query, and then kubectl can do things with it, like “what nodes are failing right now,” or whatever. That’s one place we could see things happening—more and more tools do that.

The other thing we could see is terminals becoming more AI and agentic themselves. Warp is an example of that. And then also, the most common shells today, absent the terminal, are BASH and zsh. One of the things I’ve been thinking a lot about—I did a prototype a while back, and my team’s done another prototype that was even better—which is, could we create an AI-aware shell?

Each of these are ways of interacting, right? Just like you could have a desktop app that understands things and you interact with, or a web page. Likely all of these things will happen, is my guess, because they all have interesting use cases.

## The Future of Programming Languages

**Williams:** Makes sense. I’m curious again about programming languages. Are you seeing — if we’re talking about the evolution of the terminal, there’s the evolution of lots of other things that are associated with the terminal. With generative AI, you can use the machine to help you generate the right code. But is there a shift in how we’re thinking about code itself? And with that, how do you see the evolution of new programming languages?

**Ballinger:** This is a fascinating question, because I think there’s a wide variety of opinions on this, and no one knows for sure. I generally have a very optimistic opinion that’s probably in the minority. But Aether was, of course, an example of that.

I think we should be building programming languages that are designed for LLMs, where we never look at them, so to speak. I think we can get to a place where, as a developer, I’m no longer dealing with lines of code. I’m dealing with the system design, the architecture, the user interfaces, all those kinds of things. I’m crafting it together, but the actual language underneath is just a black box to me.

This, to me, feels like a natural progression of abstractions. We originally started with punch cards, essentially machine code. Then we had languages like C, which were thinly on top of things like assembler. Then we went to more and more abstract languages like Java or C#, which continued up the abstraction level.

The next abstraction level is essentially my intent, what I want, and how that composes together to make an experience, to make an application. In those cases, I don’t think you’ll necessarily need to have the code.

Now, I always think there’ll be people whose craft is the code, who love writing code line by line. And honestly, they’ll probably have a competitive advantage for certain areas of code writing for a long time. That’s what they enjoy. I want them to enjoy it. But I think we’re going to get to a place where we don’t see that as much. Again, controversial opinion, I’m sure.

There was a paper I read not too long ago about someone who put two agents in communication with each other, and over time, they started sending gibberish to each other because they negotiated a highly compact language that they invented on the fly to talk. That kind of thing is fascinating to me. I’d love to see where that goes.

**Lardinois:** Is that abstraction layer, by default, natural language though, or is it kind of a meta-programming language? Because you want some degree of precision, right? Which natural language isn’t — at least English isn’t always good at.

**Ballinger:** Yeah, I mean, this is a question I ultimately don’t know the answer to. I used to be kind of anti-natural language. I felt like there were going to be other metaphors for interacting with AI that were more precise than natural language.

But as I’ve worked in this field longer and longer, I kind of feel like, when you look at a textbook or any nonfiction novel, we don’t worry about the precision of what’s been written. No one ever says, “Well, that textbook on calculus was imprecise.” We feel like it was pretty precise. And of course, there’s bad writing that’s vague, but I think there’s so many examples of people in natural language writing precision and documentation.

I think you have to kind of meet people where they are, right? People could learn some other syntax, something that is formal, that allows them to talk to an AI, or something that’s visual, that allows them to communicate with an AI. But then we’re asking people to learn something new and do something new. I think you have more and more evidence that — [people should] just have really good writing skills and have the ability to decompose problems well and understand designs, right?

Design patterns have existed for a long time now, and they’ve always turned out to be incredibly useful, and not just in coding. Architects do design patterns. I think that’s kind of where we want to go—let’s just help people be better and better writers and better and better problem solvers, which, again, it’s about decomposition of the problem.

**Lardinois:** Yeah, a different kind of skill, though, from sometimes the skill that programmers have today.

**Ballinger:** I would argue, I don’t think that’s true. I think that a great programmer is a great writer. They write down what they’re going to do. They document the problem, the solution, options for the solutions, the design, all of that stuff. I think great programmers do that.

And they certainly understand — they’re able to go from business problem to technical solution really well. Understanding what requirements are, understanding what’s possible, decomposing it into small pieces so that they can iterate and pivot as they need to. I think those are the exact skills needed in this agentic coding world. And maybe, or maybe not, the ability to write lines of code is the one that is not as needed in the future.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://thenewstack.io/wp-content/uploads/2025/03/15a7eb12-cropped-4e88ac40-frederic-profile-2-600x600.jpg)

Before joining The New Stack as its senior editor for AI, Frederic was the enterprise editor at TechCrunch, where he covered everything from the rise of the cloud and the earliest days of Kubernetes to the advent of quantum computing....

Read more from Frederic Lardinois](https://thenewstack.io/author/frederic-lardinois/)