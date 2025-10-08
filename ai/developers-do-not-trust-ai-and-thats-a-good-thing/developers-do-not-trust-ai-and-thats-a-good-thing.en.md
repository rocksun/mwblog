One of my old hobbies was writing for independent music magazines, such as Spill Magazine (distributed free at music venues) and DV8 (distributed free at hair salons). Over the years, I saw hundreds of unsigned bands and learned a crucial lesson: Amplification makes everything you do really loud, but it doesn’t fundamentally change whether what you’re doing is good or bad.

This law of amplification applies equally to software development, according to [DORA’s State of AI-assisted Software Development report](https://dora.dev/research/2025/). AI is an amplifier that will [boost the volume of your software](https://thenewstack.io/openssf-boosts-software-supply-chain-security-with-slsa-1-0/) delivery capability, whether good or bad.

And this is why I find the report’s findings on trust so reassuring.

## We Don’t Trust AI

The report found that AI is being used practically everywhere. Almost everyone (95%) is using AI for their work and believes it increases their productivity (80%) and code quality (59%). But they don’t trust it. In fact, when asked whether they trust AI-generated output, the response was an overwhelmingly subdued “somewhat”.

This has led many people to ponder how we can increase trust in AI. There’s a perception that if we can get technical people to trust it, we’ll get even bigger gains. However, this is not an outcome we should strive for.

One factor contributing to the successful adoption of AI is undoubtedly a healthy level of skepticism regarding the answers it provides. Encouraging people to increase their trust in AI can reduce agency, diminish personal responsibility, and lower vigilance.

## Absolute Trust Not Required

Successful software developers have acquired critical thinking skills that enable them to envision potential pitfalls and anticipate how things might go wrong. When you create software used at scale, scenarios you perceive as atypical occur frequently.

When I worked on a platform used by global automotive giants, we would process over 4 million requests in just five minutes. We were working on a feature, and my mind was working through potential [failure scenarios and edge cases](https://thenewstack.io/webassembly/case-study-a-webassembly-failure-and-lessons-learned/). When I highlighted a potential bear trap, the business folks would often dismiss it. “The chances of that happening are a million to one,” they said. However, that meant it could happen more than 1,152 times each day, so we had to accommodate it.

When developers have a skeptical mindset, it’s healthy. They are thinking at scale and preventing a constant series of disruptive events. My team was following the “you build it, you run it” pattern, so we were highly motivated to silence the pager by [creating robust software](https://thenewstack.io/using-chatgpt-to-create-software-tests/).

Great [developers can think](https://thenewstack.io/what-do-java-developers-think-of-the-rise-of-genai/) ahead and prevent problems before they write a single line of code. Having low trust in AI-generated output is a key aspect of this mindset.

## The AI Model Is The Q&A Model

Though AI is often considered disruptive, it usually turns out that existing models can (and should) be applied. Those who don’t understand this are relearning lessons on small batches and user-centricity, as AI only exacerbates the problem of changing too much at once and over-investing in a feature idea before learning whether it’s helpful to users.

Similarly, we have an existing model we can apply to AI-generated code. The Q&A model.

When you find an answer on Stack Overflow, you don’t just copy and paste it into your application. Answers on these sites often contain a few crucial lines of code that directly address the question, as well as many additional lines that complete the example. There is some risk in taking those essential lines and even more in taking the wrapping ones.

You’ll see occasional comments from developers highlighting the dangers of those wrapping lines, and while they’re not wrong, the answers would be less helpful if they contained more and better code in the wrapping lines.

Experienced [developers use the answer to understand](https://thenewstack.io/codesee-helps-developers-understand-the-codebase/) how to solve their problem and then write their own solution, or make substantial adjustments to the code in the answer. We should apply these same reservations to all code we didn’t author, whether it’s from a Q&A site or from an AI-assistant. There’s no reason to trust the AI-generated code more than you would the answer on a Q&A site that likely formed a [part of the training data](https://thenewstack.io/data-modeling-part-2-method-for-time-series-databases/) in the first place.

## AI Warned You

Skepticism over AI-generated code shouldn’t be a controversial stance. The tools themselves provide these warnings when you start using them. Everyone using coding [assistants and AI chat](https://thenewstack.io/build-an-ai-chat-assistant-with-stream-and-openai/) has clicked past a message such as: “ChatGPT can make mistakes. Check important info.”

We’d be foolish to place high trust in them and the outcomes would be worse if we did.

While AI-assistance is relatively new, experienced software developers are applying healthy models for handling the code it produces. That’s why enthusiasm for toil-reduction is best served by muted trust levels.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://thenewstack.io/wp-content/uploads/2023/10/e54f7c3f-cropped-fc6cbbe0-steve-fenton-600x600.jpg)

Steve Fenton is an Octonaut at Octopus Deploy, a DORA community guide and a six-time Microsoft MVP with more than two decades of experience in software delivery. He has written books on TypeScript (Apress, InfoQ), Octopus Deploy, and web operations....

Read more from Steve Fenton](https://thenewstack.io/author/steve-fenton/)