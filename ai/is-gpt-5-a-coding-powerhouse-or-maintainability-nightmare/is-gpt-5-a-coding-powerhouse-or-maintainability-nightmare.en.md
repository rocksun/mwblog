It’s been a few weeks since OpenAI’s latest model, GPT-5, was [released to mixed reviews](https://thenewstack.io/gpt-5-a-choose-your-own-adventure-for-frontend-developers/) — with one prominent frontend developer even doing a 180 and completely changing their tune within days. But now that developers have had time to put the new model through its paces, we can better determine whether GPT-5 “excels at frontend coding,” as [OpenAI claimed](https://openai.com/index/introducing-gpt-5-for-developers/).

I reached out to OpenAI with a series of questions based around frontend development. [Ishaan Singal](https://www.linkedin.com/in/ishaan-singal/), a researcher at OpenAI, responded by email. Singal, who has previously worked as a software engineer at Stripe and Microsoft, told me that early feedback on GPT-5 “has been positive, [but] it’s still early days.”

For my first question, I noted that in the [GPT-5 prompting guide](https://cookbook.openai.com/examples/gpt-5/gpt-5_prompting_guide), there are three recommended frameworks: Next.js (TypeScript), React, and HTML. Was there any collaboration with the Next.js and React project teams, I asked, to optimize GPT-5 for those frameworks?

“We picked these frameworks based on their popularity and commonality, but we did not collaborate directly with the Next.js or React teams on GPT-5,” replied Singal.

We know that Vercel, the company that [shepherds the Next.js framework](https://thenewstack.io/vercels-frontend-and-the-rise-of-the-hybrid-developer/), is a fan of GPT-5. On launch day, it called GPT-5 “the best frontend AI model.” So there is a nice quid pro quo happening here — GPT-5 was able to become an expert in Next.js because of its popularity, which presumably increases its popularity even more. That helps both OpenAI and Vercel.

[![An example of "organizing code editing rules for GPT-5" from OpenAI's GPT-5 prompting guide.](https://cdn.thenewstack.io/media/2025/09/f028e3a8-screenshot-2025-09-05-at-10.55.25.png)](https://cdn.thenewstack.io/media/2025/09/f028e3a8-screenshot-2025-09-05-at-10.55.25.png)

An example of “organizing code editing rules for GPT-5” from OpenAI’s [GPT-5 prompting guide](https://cookbook.openai.com/examples/gpt-5/gpt-5_prompting_guide).

But what if you [don’t want to use Next.js](https://thenewstack.io/after-a-decade-of-react-is-frontend-a-post-react-world-now/), or indeed any web framework? How does GPT-5 cope if tasked with creating a sophisticated web app using *only* the core web platform technologies, I asked — referencing HTML, CSS, JavaScript, and any of the [web APIs](https://developer.mozilla.org/en-US/docs/Web/API) listed on Mozilla’s MDN.

“GPT-5 is a strong general-purpose model, and can also be used to make web apps with just HTML / CSS / JavaScript,” replied Singal, rather vaguely.

I tried a different angle with one of my next questions: Could developers, particularly frontend developers, ‘train’ GPT-5 to only use web platform technologies — i.e. use GPT-5 to wean themselves off framework and/or [React reliance](https://thenewstack.io/web-development-trends-in-2024-a-shift-back-to-simplicity/)?

“GPT-5 is the most steerable model out there, and developers have had great success in prompt engineering very specific behaviors and outcomes out of it,” Singal responded. “I wouldn’t be surprised if GPT-5 can help with this use case.”

> “GPT-5 is the most steerable model out there, and developers have had great success in prompt engineering very specific behaviors and outcomes out of it.”  
> **– Ishaan Singal, OpenAI researcher**

Another non-committal answer. Let’s try again: does OpenAI think GPT-5 could accelerate adoption of more modern web native features — like [CSS Houdini](https://developer.mozilla.org/en-US/docs/Web/CSS/CSS_properties_and_values_API/Houdini) and [Web Components](https://thenewstack.io/how-microsoft-edge-is-replacing-react-with-web-components/) — that frameworks often overshadow?

“This somewhat depends on the application leveraging GPT-5 to provide their users with tools to build UI components,” replied Singal. “Many of these applications are opinionated in the type of technologies and features they prefer, and I imagine that influences this adoption.”

So, what we’ve learned so far is that GPT-5 can, theoretically, cover all frontend use cases — but a lot depends on the tools you’re already using and what approach you, the developer, want to take. It’s also worth noting that OpenAI, itself, is being “opinionated” with the tools it recommends for GPT-5: Next.js (TypeScript), React and HTML; and, for styling, it recommends Tailwind CSS, shadcn/ui and Radix Themes.

## What Do Others Say About GPT-5?

If OpenAI is (understandably) reticent about reporting back on actual developer experience at this stage, the code security company Sonar isn’t so shy. It recently released an update to its [State of Code Report on LLM personalities](https://www.sonarsource.com/sem/the-coding-personalities-of-leading-llms/?utm_medium=paid&utm_source=newstack&utm_campaign=ss-state-of-llms25&utm_content=newsletter-TNS-newsletter-stateofllm-x-x&utm_term=ww-psp-x&s_category=Paid&s_source=Paid%20Other&s_origin=newstack&utm_content=inline-mention), featuring [new data on GPT-5](https://www.sonarsource.com/blog/the-coding-personalities-of-leading-llms-gpt-5-update/).

Sonar concluded that GPT-5 is not, according to its tests, the leader in coding performance.

Here’s a summary of Sonar’s findings:

* Even after GPT-5’s arrival, Claude Sonnet 4 remains the performance leader out of all the models Sonar tested.
* GPT-5 generates a “larger and more complex volume of code than any other model,” which makes it “a serious challenge to review and maintain.”
* For every task GPT-5 completes successfully, it introduces “significantly more potential defects than its competitors, resulting in a large downstream technical debt, quality, security, and verification burden.”
* GPT-5 produces the lowest density of vulnerabilities, but it has “a much higher density of code smells,” meaning the code is weak in terms of quality and maintainability.

Sonar concludes by saying that GPT-5 is “undeniably a powerful new force in AI code generation,” with the caveats that the model “carries a significant quality cost and presents a different profile of security and reliability considerations.”

> GPT-5 “carries a significant quality cost and presents a different profile of security and reliability considerations.”  
> **– Sonar report on GPT-5 and coding**

Sonar has also done [a separate study of GPT-5’s reasoning modes](https://www.sonarsource.com/blog/how-reasoning-impacts-llm-coding-models/) across more than 4,400 Java tasks. That revealed a clear trade-off: “while higher reasoning delivers best-in-class functional performance, it achieves this by generating a massive volume of complex and hard-to-maintain code.”

To add a second external voice to the GPT-5 analysis, let’s return to our old YouTuber friend, Theo Browne — he was the prominent developer who did the 180. In fact, he was among the developers featured in one of OpenAI’s launch day videos, at which point [he loved GPT-5](https://x.com/theo/status/1953516806104056096). But then just a week later, he posted a video entitled “[I was wrong about GPT-5](https://www.youtube.com/watch?v=k68ie2GcEc4).” So how does Browne feel about GPT-5 now?

In [his latest video about GPT-5](https://www.youtube.com/watch?v=SOxmiupQm7w), a couple of weeks after its launch, Browne blamed some of the issues he encountered on how GPT-5 is implemented in both ChatGPT and Cursor. “There’s a lot of UX failures in Cursor’s implementation right now that are still pervasive,” he added. “But despite all of that, I still think 5 is an incredible model. It’s still the one I use for all the work I do.”

[![Frontend development influencer Theo Browne trying to decide what he thinks of GPT-5.](https://cdn.thenewstack.io/media/2025/09/3de70858-theo-browne-gpt5-3weekslater.jpg)](https://cdn.thenewstack.io/media/2025/09/3de70858-theo-browne-gpt5-3weekslater.jpg)

Frontend development influencer Theo Browne trying to decide what he thinks of GPT-5.

So both Sonar and Browne acknowledge that GPT-5 is a powerful coding tool, although Sonar is more critical of its code quality and maintainability.

## One-Shotting or An Eye to Maintenance?

Back to OpenAI’s responses to my questions. OpenAI’s guide also states that “GPT-5 is excellent at building applications in one shot.” That seems targeted at so-called “[vibe coders](https://thenewstack.io/the-field-cto-view-ai-vibe-coding-and-developer-skillsets/)“; but I asked whether professional developers are also being encouraged to “one-shot” everything in GPT-5, or should they take a more considered approach? For instance, taking into account the future maintenance of the code, as Sonar would clearly like it to do.

“GPT-5 is trained to be good at both generating zero-to-one apps and developing more full-stack applications agentically in a repo,” replied Singal, unsurprisingly covering all use cases. But he was slightly more effusive in the next part of his reply:

“For developers building a new prototype, zero-shotting an app end-to-end can be a quick way to validate ideas. For developers that are either working on existing applications or building something to maintain for longer, using an agentic harness and iterating over granular features might be more preferable. It really depends.”

> “At the end of the day, it is the developer’s choice.”  
> **– Singal**

It’s common for internet vendors to put all the responsibility back on the user — it’s [not Napster’s fault](https://cybercultural.com/p/napster-1999/) some of its users download illegal content, it’s not Facebook’s fault some of its users have extreme political views, etc. In the same way, OpenAI is saying to developers: hey, it’s your choice how you use GPT-5.

“At the end of the day, it is the developer’s choice,” Singal said, “but established repos have better support from the community. This aids developers in self-serve maintenance.”

About GPT-5’s usage so far, Singal added that “we’ve seen a good mix of both vibe coders / zero-to-one app developers and folks plugging this into their existing giant applications for iteration.”

## Frameworks Optimized for AI

One of Singal’s more opinionated replies was to a forward-looking question I threw in for fun.

What do you think of the possibility of frameworks optimised for AI, I asked? For example, smaller runtime footprints or AI-friendly component APIs. Singal seemed intrigued.

“This is an interesting idea! The considerations would be around maintainability and how much “human-in-the-loop” presence is optimal. It is possible that what is optimal for AI does not make for interpretable human consumption. That said, eventually, this might become a lot more prevalent as AI for coding continues to become part of the mainstream workflow.”

So, keep an eye out for AI-optimized frontend frameworks in the near future. In the meantime, have at GPT-5 in whichever way works best for you — but be mindful of code quality and maintainability.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://cdn.thenewstack.io/media/2020/03/1c7152c0-ricmac_highres_w400_h400.jpg)

Richard MacManus is a Senior Editor at The New Stack and writes about web and application development trends. Previously he founded ReadWriteWeb in 2003 and built it into one of the world’s most influential technology news sites. From the early...

Read more from Richard MacManus](https://thenewstack.io/author/richard/)