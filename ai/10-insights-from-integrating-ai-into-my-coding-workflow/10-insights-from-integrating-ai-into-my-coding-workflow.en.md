Software development is full of competing pressures: We’re expected to move quickly, innovate constantly and still ship high-quality, maintainable code. That’s a tall order on the best of days — and that’s where AI tools can help.

Over the past few months, I’ve been [integrating AI into my daily workflow](https://thenewstack.io/ai-agents-are-finally-starting-to-revolutionize-the-software-development-lifecycle/) as a senior software engineer at [DataStax](https://www.datastax.com/?utm_content=inline+mention). What started as a bit of curiosity has turned into a steady partnership: I rely on AI not just to save time, but to think differently, reduce friction and strengthen the systems I’m working in.

As developers, we’ve all seen hype come and go, but this is something different. These tools are [reshaping how we interact with codebases](https://thenewstack.io/keeping-up-with-ai-the-painful-new-mandate-for-software-engineers/), how we debug, how we test and how we grow. The journey hasn’t been without missteps, but it’s been illuminating. Below are 10 of the most insightful, helpful or surprising lessons I’ve learned along the way.

## 1. Using AI to Write Tests

I’ve never loved writing tests, and that’s one reason I use AI to help. But more importantly, when I write the code and the tests myself, any blind spots I have tend to carry over into both.

AI offers a second perspective — it’s like having another set of eyes. I’ve caught more than a few bugs this way, especially ones I wouldn’t have even thought to test for. It turns the [testing process](https://thenewstack.io/ai-testing-more-coverage-fewer-bugs-new-risks/) into a kind of early peer review and makes the tests better, which makes the code better.

## 2. AI Cementing Patterns vs. Driving Innovation

One of the risks with AI development tools is that they often reinforce what already exists in your codebase — good or bad. That predictability is useful, but it can also preserve flawed architectures and missed opportunities.

Sometimes, AI suggesting the “old way” is exactly what you want for consistency. But sometimes, it’s a prompt to pause and ask: Is this still the right way? True innovation still requires us to challenge the default and push toward better patterns.

## 3. Windsurf vs. Cursor: First Impressions

I’ve been using [Windsurf](https://thenewstack.io/windsurf-an-agentic-ide-that-thinks-and-codes-with-you/) extensively, and only just started experimenting with [Cursor](https://thenewstack.io/using-cursor-ai-as-part-of-your-development-workflow/). Both tools are impressive in their own right, but they feel different. Windsurf tends to be more conservative and grounded in the patterns already present in your codebase. Cursor feels faster and more experimental — more likely to guess-and-go.

If you’re looking for predictable suggestions that follow established conventions, Windsurf is great. If you want quick iteration and don’t mind more surprises, Cursor might suit you.

## 4. Building Trust in the AI Workflow

When I first started coding with AI, I was skeptical. Could I really trust a suggestion from a machine? But trust builds slowly — a well-caught bug here, a cleverly rewritten test there — and now I find myself actively relying on it.

I’ve found it helps to begin with a well-articulated problem (a solid Jira ticket helps) and then ask ChatGPT for pseudocode. I paste that into Windsurf and let it build from there. That workflow means I stay in control while still benefiting from AI’s strengths.

## 5. Debug Panels as AI Accelerators

Windsurf has a powerful feature I use often: temporary debug panels. Instead of relying solely on `console.log` or browser network tabs, I ask Windsurf to generate a panel that shows specific state values in the UI. I can even take a screenshot, including the browser console, paste it into the Windsurf chat and get tailored feedback.

The visual context helps tremendously, and the debug panel becomes a mini-lab for figuring out what’s going wrong. Just don’t forget to clean up after yourself when you’re done.

## 6. Refactoring with AI as a Partner

AI shines when it comes to tedious but important work like refactoring legacy code. What might take hours by hand can be condensed into minutes — provided I stay in the driver’s seat.

I usually ask AI to walk me through what it’s planning to do, then review the changes carefully. It’s saved me time, yes, but it also helps me reason about the code as I go. It’s like pairing with someone who’s fast on the keyboard but still needs architectural guidance.

## 7. Maintaining Ownership for the Code

I’ve had moments when AI produced something elegant — on paper — that ended up breaking things in subtle ways. In one case, I asked for an optimization, and it introduced a `useMemo` that cached the wrong values. It took me hours to trace the issue.

That experience reminded me that even when the AI writes the code, it’s still *my* responsibility. The bug was mine. I’ve learned to slow down and make sure I understand every change, even when it looks clever.

## 8. Prompting Yourself Before Prompting AI

Before I type anything into the AI chat, I take a moment to sketch out what I think the solution should be. Then, I tell the AI what I think and ask it what it would do. This kind of “metaprompt” — asking it to respond to my own thinking — helps sharpen my ideas and ensures that I’m not just outsourcing the hard work. The result is usually a stronger answer, and one that I feel more connected to.

## 9. When to Use the Force

Sometimes, the best thing I can do is shut the AI off. When suggestions get noisy or feel off-base, I take a step back and go manual for a bit. It clears my head. It reminds me of the moment in “Star Wars” when Luke turns off the targeting computer and trusts the Force.

AI is an amazing tool, but it’s still just a tool. I find it helpful to check in with myself: Is this still helping or is it time to re-center?

## 10. The Myth of AI Replacing Engineers

There’s a lot of talk about [AI replacing developers](https://thenewstack.io/ai-will-steal-developer-jobs-but-not-how-you-think/). I don’t buy it. What I hope happens, and what I’ve seen so far, is that AI enhances the productivity of good engineers. But it doesn’t replace judgment, communication skills or an understanding of what matters to the business. In fact, those skills are becoming even more critical. The keyboard work might shrink, but the thinking? That’s still all on us.

These 10 insights are just a snapshot of an ongoing conversation. The way we work is changing fast, but so is the way we think, collaborate and define what it means to “write code.” AI is powerful, but the future of development still depends on human creativity, responsibility and collaboration.

We’re just beginning to scratch the surface of what AI can do for software development. Some days, it’s a brilliant partner; others, it needs a firm hand. But every day, it’s changing the shape of our work. My hope is that by sharing these stories, we’ll keep pushing the conversation forward — not just about what AI can do, but about what we want our jobs to be like in the future.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://cdn.thenewstack.io/media/2025/07/907853a3-cropped-ea4245bc-dieterrandolph.jpeg)

Dieter Randolph is a senior software engineer at DataStax, based in St. Petersburg, Florida. With over a decade of experience across startups and large enterprises, he’s passionate about using AI tools to enhance creativity, collaboration and developer impact. Dieter is also...

Read more from Dieter Randolph](https://thenewstack.io/author/dieter-randolph/)