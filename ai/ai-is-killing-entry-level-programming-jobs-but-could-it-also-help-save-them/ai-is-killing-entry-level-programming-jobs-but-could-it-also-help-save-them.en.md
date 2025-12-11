TOKYO — Standing between the audience and their lunch, [Stefania Druga](https://www.linkedin.com/in/drugastefania/), research scientist at [Sakana AI](https://sakana.ai/ai-scientist/) and former AI research scientist at [Google](https://cloud.google.com/?utm_content=inline+mention) [DeepMind](https://thenewstack.io/qa-how-google-itself-uses-its-gemini-large-language-model/), made the room stretch before delivering one of [Open Source Summit Japan](https://events.linuxfoundation.org/open-source-summit-japan/)‘s most sobering talks: a clear-eyed assessment of how AI is undermining the apprenticeship, mentorship and shared knowledge systems that have sustained computing education for decades.

“We’re currently seeing the loss of epistemic agents,” Druga warned during her keynote. For those of you who aren’t familiar with the term, it refers to people who form, evaluate, revise and act on what they’ve learned, rather than just passively receiving information.

Or, as Druga explained later in an interview, “With AI, too many people want to be in the passenger seats and not fly the plane.”

That is, rather than think about how to get an answer, they want to unquestioningly accept the answer the AI gives them. This is bad news.

You see, her message was not about AI replacing programmers. It was about something deeper and more dangerous: AI eroding the structures that teach humans how to think, question and build technical mastery.

## ‘The Vanishing Ladder of Technical Apprenticeship’

This transformation of work had led to what Druga called “the vanishing ladder of technical apprenticeship.” She cited a stark number that hung in the air long after she said it: [Entry-level tech hiring in the U.K. has dropped 46%](https://www.theregister.com/2025/10/16/uk_tech_grad_jobs/).

At the same time, AI tools are [automating many of the junior tasks](https://thenewstack.io/ai-will-steal-developer-jobs-but-not-how-you-think/) that once served as stepping stones for newcomers. “We need experience to get a job, and a job to get that experience,” she said. “If AI is going to automate these entry-level tasks, how are real people supposed to learn these skills?”

In addition, open source communities, historically a training ground for early career developers, are overwhelmed, Druga said. Maintainers report a surge in low-quality pull requests, many of which are likely AI-generated. For [open source maintainers, AI spam is a real problem](https://thenewstack.io/ai-is-spamming-open-source-repos-with-fake-issues/). Just ask [Curl maintainer Daniel Stenberg](https://thenewstack.io/curl-fights-a-flood-of-ai-generated-bug-reports-from-hackerone/). According to Druga, “they’re actually not more productive with AI right now.”

The ur-problem, she argued, is not that AI writes code, but that humans increasingly don’t know how to read, verify or challenge it.

That’s especially bad, because of, as Druga pointed out, AI’s [jagged intelligence](https://x.com/karpathy/status/1816531576228053133?lang=en): This new phrase, coined by [Eureka Labs](https://eurekalabs.ai/) Founder and former Director of Tesla AI, [Andrej Karpathy](https://thenewstack.io/openai-co-founder-ai-agents-are-still-10-years-away/), refers to the simple fact that while AI systems appear superhuman at some tasks, they also fail at surprisingly simple ones.

Wrapping developers’ minds around this concept, Druga said, is “very hard … particularly for beginners. You might expect [an AI] that is powerful at writing math proofs, but it might not be able to count the number of R’s in ‘strawberry.’”

## Why Devs Must Cultivate New Skills

This unpredictability requires developers, especially novices, to cultivate skills AI cannot replace: verification, debugging, critical questioning and systems reasoning. These competencies, Druga noted, are now at the top of curriculum reform discussions at major computer science programs worldwide.

Unfortunately, those are precisely the same skills senior management often neglects in their rush to replace junior-level programmers with chatbots and agents. The only way to master those skills is to start with learning the simple, fundamental work that leads to expertise.

“Traditionally, we had a pipeline,” Druga observed. “We would have junior devs who come in and learn the ropes, mid-level people who mentor them and understand the trade-offs in the code, and then seniors who can oversee the architecture and processes. Where does this expertise come from now?”

We don’t know yet.

Druga thinks AI can help. She showcased research on AI-assisted learning systems designed to promote [Socratic Method learning](https://tilt.colostate.edu/the-socratic-method/) rather than simply marking answers right or wrong. Instead, the teacher or an AI uses questions to guide students toward a deeper understanding of a subject.

Such programs, she said, “should help them debug. It should give them affirmations, but not do all the work for them.”

For example, Druga said, with her collaborator, [Nancy Otero](https://www.linkedin.com/in/nancy-otero-8003492/), she “[built this benchmark of 55 most common math misconceptions in algebra](https://arxiv.org/pdf/2412.03765v1). We used this misconception benchmark to create a math tutor that doesn’t tell students this is the right or wrong answer, because that’s not helpful for learning. It helps them debug their thinking.

“If you get the wrong answer, why is that? Maybe you don’t know the order of operations yet, right, or maybe you don’t understand negative numbers or fractions. Maybe you want to practice that concept until you get it right.

“This is much more motivating than telling you you got this score or this is right, or this is wrong, and it’s helpful for teachers, too, to know which concepts they need to go over more and which concepts the kids already have.”

Druga believes in this same approach to create AI programs that can help entry-level programmers get up to speed. To help with this, she believes AI programs should be more open, so students can try to break them and gain a deeper understanding, rather than just accept an answer.

To make this effective, pen code and open weights are not enough. Open data is needed as well.

## ‘We Are Burning the Furniture To Warm the House’

In an interview with The New Stack, Druga expanded on several themes from her keynote. She pointed to a worrying trend: the collapse of the online commons on which modern AI depends.

“Since the launch of ChatGPT, [contributions to Stack Overflow have declined by more than 50%](https://observablehq.com/@ayhanfuat/the-fall-of-stack-overflow),” she said. “We are burning the furniture to warm the house.”

As inexperienced developers outsource thinking to code generators, the communal knowledge base thins, and the AI systems trained on that knowledge degrade. Druga agreed with me that we may be witnessing early signs of [AI model collapse](https://www.theregister.com/2025/05/27/opinion_column_ai_model_collapse/) as recursively generated “slop” feeds back into new models.

She also critiqued the popular notion of vibe coding, building applications by typing natural-language prompts into AI tools. “It’s not really vibes,” she said. “It’s like peeling layers of an onion.”

Many tasks work. Until suddenly they don’t. Something trivial for a human, like placing a custom logo, becomes a half-hour ordeal when mediated through a [large language model (LLM)](https://thenewstack.io/introduction-to-llms/). At that point, she said, users must “not be afraid to look into the code.”

This is where she advocates for progressive disclosure in tool design: gradually exposing power users to deeper technical concepts as their confidence grows. Thus, she believes in AI tools that incorporate hands-on learning for everyone, not just kids. Too many leaders, she said, assume AI lets them eliminate junior ranks. They’re wrong.

She encouraged companies to replace expensive AI briefings with half-day internal hackathons that enable staff to collaboratively test, break and evaluate tools in authentic contexts. Senior management may resist, she acknowledged, but the startups that embrace this hands-on culture will be the ones that understand both AI’s limitations and its potential.

Druga concluded both her keynote and interview with the same message: AI may be getting smarter, but humans must not become less so. If the communities that underpin shared technical knowledge collapse — open source, mentoring networks, Q&A sites, classrooms — we will lose not only future developers, but the collective ability to understand and shape our tools.

As she asked the Tokyo audience: “AI is getting smarter. But we must answer the question of ‘How do we ensure our shared knowledge remains?’”

That’s a darn good question, and we want to answer it as soon as possible.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://cdn.thenewstack.io/media/2023/03/cee63948-cropped-8a0b5c52-steven-vaughan-nichols.jpg)

Steven J. Vaughan-Nichols, aka sjvn, has been writing about technology and the business of technology since CP/M-80 was the cutting-edge PC operating system, 300bps was a fast internet connection, WordStar was the state-of-the-art word processor, and we liked it.

Read more from Steven J. Vaughan-Nichols](https://thenewstack.io/author/sjvn/)