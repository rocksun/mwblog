# The 4 Evolutions of Your Observability Journey
![Featued image for: The 4 Evolutions of Your Observability Journey](https://cdn.thenewstack.io/media/2024/10/0e0f5407-known-unknown-1024x576.jpg)
When going on an [observability](https://thenewstack.io/observability/) journey, there tends to be a few concrete phases that every company goes through. Understanding how those unfold and take shape as you mature your observability practices can help you identify when you’ll run into certain types of challenges, and when you’ll start really wanting certain tools and practices to help address those challenges.

That said, when you’re communicating about this to others, you might often find that it’s difficult to explain how you know where you are in the journey, or articulate the issues you’re running into. Often, people express difficulty getting a shared understanding around this, which is where mnemonics and mental models can come in handy.

The [known/unknown matrix](https://en.wikipedia.org/wiki/There_are_unknown_unknowns) in particular can be incredibly helpful in understanding where you are on your observability journey.

In the known/unknown matrix, we have four stages: known knowns, known unknowns, unknown knowns and unknown unknowns. Each one corresponds to a different way of approaching three very crucial tasks in operating a system: asking questions, learning about the system and explaining what you learned.

Those three tasks, in a nutshell, are what almost everything we do in [platform engineering](https://thenewstack.io/platform-engineering/), observability, site reliability engineering (SRE) work, [DevOps](https://thenewstack.io/devops/) and more can be boiled down to. So let’s go over them and see how we can use the matrix to help understand where you’re at and share that understanding with others.

## Known Knowns
Known knowns, when used to describe where you are on your observability journey, are the first stage. You know what question you’re asking and what you’re looking at. Here, you want to be able to look into the past and ask, “What happened?”

Some examples:

- The website had a spike in errors. Where, how, why?
- The mobile app is experiencing more crashes in the latest version.
[Is it only buggy in the latest version?](https://get.embrace.io/mobile-devops-sre/?utm_source=the-new-stack&utm_medium=paid&utm_campaign=four-quadrants) - Our auth service is completely down, but only in one geographical area. What does that mean?
Even though this is the first stage, this is actually one of the hardest ones. Most companies and most engineers never progress past this stage, and almost every tool and vendor you’ll encounter is primarily interested in this stage. That’s because this stage is all about the ability to ask meaningful questions about the past, and it turns out that “meaningful” is a tricky concept to nail down.

If that wasn’t enough, figuring out how to get your tooling and systems to let you ask those questions is even harder. It’s no wonder most people get stuck here and can find themselves having a difficult time explaining why this is just the beginning of the journey.

After all, if so many companies can be wildly successful without achieving this, you might wonder whether it’s even necessary to start this observability journey in the first place.

Known knowns are about investigation.

Truth be told, if you can’t sufficiently articulate why the observability journey is critical for the company, you’re never going to finish the journey. Human understanding and shared motivation have to come first.

**You know you’re here if:**
- You ask investigative questions, like “Hey, what happened during … ?”
- You mostly learn by inferring and exploring the system, not by predicting and anticipating.
- You build narratives with historical records.
Let’s break those down.

Investigative questions are the main types of analysis you do with these systems. You’re in that exploration phase, that learning part where the most important thing is figuring out why, how, what and where. It turns out that basic questions can be really, really hard to answer. You can’t always just say it was DNS and leave it at that; you have to be able to figure out *what* and *how*.

That means you’re going to spend a lot of time inferring and exploring the system. You won’t really get a predictive sense of the system, but this is where engineers build a deep intuition of the system and its behaviors. Learn it! Play with it! Poke things! This is the land of experimenting and finding out. The types of tools that are right at home here are ones where you get instant and incremental feedback.

How do you share the results of what you learned? By writing a narrative. Particularly with historical records. Incident retrospectives should feel right at home here, especially things with timestamps.

## Known Unknowns
Known unknowns can be used to describe the second stage. They fit because we’re looking at things we know we don’t know, but we’re trying to see how well we can develop the understanding of those unknowns, whereas if these were unknown unknowns, we wouldn’t even know where to start.

If the first stage is where most of your observability tooling lies, then this is the era of service-level objectives (SLOs); this is also the stage where observability starts being phrased in a “yes, and” manner. Observability? Yes, and performance monitoring and SLOs and developer experience and user experience and …

Having developed the ability to figure out that you can ask questions about what happened in a system in the past, you’re probably now primarily concerned with statistical questions and developing more comprehensive correlations.

Examples include:

- Our endpoints are usually fast (responding within 200ms), but how slow is too slow?
- We updated some dependencies and now our website is suddenly 60% faster. Is that … fine?
- Our initial response time distribution is different enough between platforms that all of our alerts broke when we added mobile SLOs.
[How do we account for that?](https://get.embrace.io/mobile-slos-guide/?utm_source=the-new-stack&utm_medium=paid&utm_campaign=four-quadrants)
It’s not enough to know whether something happened, but you now want to find out how abnormal it was. This is where you learn that abnormally good can be just as dangerous to a system as abnormally bad.

Known unknowns are about analyzing.

**You know you’re here if:**
- You ask statistical questions, like “How unusual is … ?”
- You mostly learn by predicting and anticipating, not by experimenting or playing.
- You build narratives around emotions of surprise and novelty.
Let’s break those down.

Statistical questions are the main types of analysis here, not investigative ones, because you’re trying to figure out how the system behaves over time so you can start to anticipate and predict its behavior. Sure, you’re still mucking about and poking things, but when you start having statistical insight to back up a hypothesis about what will happen to the system after a change occurs, you’re in this second stage. Which is why a tool that allows you to correlate very different streams of data, do some number crunching and then annotate it with human notes ends up being so valuable here.

Additionally, one of the most interesting developments here is when your incident reports change: They stop becoming concerned about what happened and start becoming concerned with how unusual or surprising it was.

You’re seeing first hand this stage of the observability journey in action if you’ve ever read a retrospective that said something like, “We were surprised by the behavior, so we dug in. Even though our alerts were telling us that this other thing was the problem, we investigated the surprising thing first.”

## Unknown Knowns
We’re stepping into fun territory here. This is the first stage of the observability journey, where we start with “we have no idea.” This stage, unknown knowns, is the ability to predict how a system will behave if certain events occur. This is where fault injection and user experiments come into play.

Examples:

- What happens if we turn off an availability zone?
- Our app supports failover, but does it work?
- How effective are our user satisfaction programs? Can we introduce faults and see how customer support is affected?
- In our mobile app,
[do over-the-air (OTA) updates beyond a certain size affect conversion rates?](https://blog.pragmaticengineer.com/uber-app-rewrite-yolo/#the-app-release-strategy-yolo)
We know what we’re going to do to the system, but we have no idea what the system did or will do. Exciting!

Unknown knowns are about experimentation.

**You know you’re here if:**
- You ask experimental questions, like “What happens if we … ?”
- You mostly learn by experimenting and playing, not by modeling or sensemaking.
- You build narratives around experiments and learnings.
Because experimentation is the main method of analysis here, what we’re doing is testing the boundaries of the system and figuring out where they are and how it behaves. You can think of this as slowly developing expertise in all the prerequisites for understanding emergent behavior and being able to reckon with it (insert foreshadowing).

As you mature here, developers won’t do all the experimentation; feature flags can be used for A/B testing, content personalization and marketing funnels too. You should involve everyone in the company at this stage, because experiments are all about learning, and learning has to be shared in a cross-disciplinary manner to be maximally effective.

## Unknown Unknowns
This is where you start trying to understand the necessary future shape of your system and how to trade off effectively between humans and computers. Error budgets come into play, data-driven “good enough” targets materialize and the connection between SLOs and service-level agreements (SLAs) graduate from vibes-driven to prediction-driven.

The examples get fascinating here:

- What codebases are the biggest business continuity risks? What do our SLAs need to be, accordingly?
- Which sales funnel is the most effective, and how does system resilience factor into that?
- Which has more return on investment (ROI) in two quarters: building more public features or investing in internal tooling for the customer success team?
- Which aspect of our mobile
[app’s performance affects](https://thenewstack.io/does-garbage-collection-logging-affect-app-performance/)daily active user (DAU) rates the most?
In the words of [Donella Meadows](https://en.wikipedia.org/wiki/Donella_Meadows), who was a pioneer in sustainability and systems thinking: You’re [dancing with systems](https://donellameadows.org/archives/dancing-with-systems/).

Unknown unknowns are about dancing.

**You know you’re here if:**
- You ask modeling questions, like “What does our system need to look like in order to achieve … ?”
- You learn by modeling, sensemaking and cross-disciplinary knowledge sharing.
- You build narratives around the interactions of sociotechnical dynamics.
When you arrive here, it’s going to feel weird, because it’s going to feel like you’re not doing observability at all. Indeed, observability, developer experience, platform engineering, product-led growth and many other things all sort of end up here. It turns out that when the market is complex and your system is complex, you need to develop an expertise in understanding emergent behavior. Secretly, that’s what the entire observability journey is about: understanding the systems beyond the limiting paradigms of command-and-control or predict-and-control.

## The Journey Awaits
There you have it. Four phases, and a way to tie them together into a narrative for everyone at your company, not just engineers, to understand the types of challenges you’ll run into and the tools you’ll want as you work together to address those challenges.

A recap:

**Known knowns:**Investigation-
- You’re here if you want to ask, “What happened during … ?”
- You’ll want tools that let you query data rapidly and interactively.
**Known unknowns:**Analyzing- You’re here if you want to ask, “How weird is … ?”
- You’ll want tools that let you correlate lots of different sources.
**Unknown knowns:**Experimentation- You’re here if you want to ask, “What happens if we do … ?”
- You’ll want tools that let everyone in the company conduct experiments and share results.
**Unknown unknowns:**Dancing- You’re here if you want to ask “What does the system need to look like to achieve … ?”
- You’ll want a culture of systems thinking here (sorry, no tools here).
One important thing that’s missing is understanding the motivation for being on the journey, tying that to understanding where you’re at and where you need to go. It’s missing for an important reason: It has to be written by you. Your story and your motivations are going to be the critical energy that fuels you along the journey toward understanding your system holistically across the entire company.

[
YOUTUBE.COM/THENEWSTACK
Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.
](https://youtube.com/thenewstack?sub_confirmation=1)