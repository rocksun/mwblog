After following vibe coding’s rapid rise as the top software development trend, I decided to use it to build a solution for a problem I regularly encounter: excessive browser tabs. I’ve developed a habit of never closing a tab because I’m unsure when I’ll need to use it again. However, since I have hundreds of open browser tabs, many are often duplicates. Building a browser plugin to help address this problem seemed like the perfect use case for my first [vibe-coding project](https://thenewstack.io/to-vibe-or-not-to-vibe-when-and-where-to-use-vibe-coding/).

## The Force Awakens

I have coded my entire life; however, I have never developed a browser plugin, and I didn’t want to start reading tutorials and other materials. Ultimately, this was the promise of vibe coding: I can start right away by [simply prompting what I want to do](https://thenewstack.io/vibe-coding-where-everyone-can-speak-computer-programming/).

So, I asked ChatGPT to teach me how to develop a browser plugin, and the first impression was amazing. It showed me how to set up the project and immediately generated a Hello World-like browser extension experience for me to try, in addition to demonstrating how to install and test the plugin in my browser.

By simply typing prompts into ChatGPT about the desired functionality and user experience, I quickly had version 1 of my plugin within 30 minutes. While having coding experience was helpful, about 95 percent of the code was generated by the [large language model (LLM)](https://thenewstack.io/what-is-a-large-language-model/).

## Expanding

I wanted more, which required an integrated development experience (IDE) where I could better use the power of vibe coding for my project without having to copy and paste code between ChatGPT and VS Studio. After researching options, I settled on [Trae](https://www.trae.ai/), which has a free offering and provides the best experience. While all IDEs use the same foundational models for coding, with just a few simple tweaks in user experience, they become significantly better.

Using an IDE well-suited for vibe coding for my project released my inner coding beast. I immediately identified areas for improvement in my plugin, becoming obsessed with upgrading it. How much further could vibe coding take this project, and would it eventually break it?

## The LLM Strikes Back

By the time I started working on the next version of the plugin, the project had become increasingly complex. While I was still relying on vibe coding to generate 90 percent of the code, the more the project evolved, the more it required my attention.

One issue stood out: The plugin wasn’t detecting duplicates reliably. For example, if a link changed but the underlying page content stayed the same, the plugin failed to recognize the change. You might move a page to a different location, but even if the content remains identical, the URL changes. I wanted the plugin to catch these cases by checking both the URL and the page title independently.

But no matter how many prompt variations or detailed explanations I gave, the LLM I was using at the time couldn’t grasp the distinction. It kept merging the URL and title into a single string instead of comparing them separately. That was the first time my excitement began to fade. It was not a complicated requirement, yet the LLM insisted on a different approach that did not align with the goal.

## Reality Check

The next major challenge I encountered was making the browser plugin compatible with both Chrome and Firefox. While the LLM did a great job generating code for that goal initially, it tended to forget the cross-browser requirement unless I explicitly reminded it. If I didn’t keep that context fresh in the prompt, it would generate new code that ignored the compatibility constraint, leading to duplicate implementations, inconsistent behavior or subtle bugs that took significant time to track down.

The dual-browser requirement turned out to be more demanding than expected. The LLM started duplicating logic in multiple places or making sweeping changes across the codebase. Without the ability to instantly read and fully understand those changes, I found myself blindly accepting broken or incomplete updates. I was spending more time debugging or reverting changes than actually moving forward.

To manage this, I had to establish a new process. I learned to ask for one specific feature at a time, providing just enough detail for the LLM to understand it correctly. Then I’d review the code, test it, and only after confirming the results would I move on to the next prompt. This helped me isolate problems more easily and revert quickly if something didn’t work. But as the project grew more complex, my trust in the LLM’s changes began to erode.

## Productivity Gains

Despite those challenges, once I found the right rhythm and developed an intuition for what works and what doesn’t, my productivity remained higher than it would have been without the LLM. Having a [strong coding background made a big difference](https://thenewstack.io/no-code-is-dead/). It became clear that at this stage of vibe coding, good coding skills aren’t just helpful, they’re essential.

The ability to quickly read and understand the generated code and sense whether something would work before even running it, as well as to craft prompts that guided the model more effectively, all proved invaluable. The boilerplate was almost always handled perfectly by the LLM. But as the project became more complex, my coding skills were put to the test like never before.

## Lessons for the Future

Vibe coding feels like just the beginning. It’s hard to predict exactly where it will lead, but one thing is clear: It significantly boosts productivity for experienced developers. At this stage, the technology still relies heavily on the strong coding skills of the one who wields it. Developers with that foundation can elevate their output to new levels.

Without vibe coding, I probably wouldn’t have sat down to bring this project to life, so it’s exciting to imagine what other personal ideas might finally see the light of day. This shift is worth embracing and learning from. Vibe coding can’t yet solve novel problems on its own; it still depends on the human touch, the drive to improve, to refine, to strive for excellence. That’s what has always pushed us forward. I’m excited to see where it takes us next.

For anyone looking to begin harnessing vibe coding for themselves, these are the five things you should be aware of:

1. **Prioritize an IDE based on your needs.** As projects scale quickly, evaluate options according to your unique requirements. While I used Trae, VS Code plugins have become very effective, so try a few before settling on one.
2. **Write clear prompts and keep the context updated.** Don’t expect the LLM to fully understand your project or requirements just by reading your code.
3. **Validate everything.** Don’t blindly accept code suggestions; make sure you verify everything yourself, or you will be in trouble.
4. **Coding skills are essential.** The better you are at coding, the more you get out of vibe coding. If you’re not confident in your coding skills, you become the bottleneck, unable to review, debug or guide the model effectively when things go wrong.
5. **Embrace unexpected benefits.** One surprising advantage was on the user experience side. I’ve never enjoyed dealing with CSS or styling, especially with the headache of ensuring cross-browser compatibility. However, thanks to multimodal models, I can now provide a mockup and obtain usable results. That alone saved me hours of tedious work.

I’ve published my plugin in both the [Chrome](https://chromewebstore.google.com/detail/duplicate-tab-detector/gkeihjnfokfjdgcdkgcpicokjmfdcbbd?hl=en) and [Firefox](https://addons.mozilla.org/en-US/firefox/addon/duplicate-tab-detector/) stores. If you’re interested in trying it out or have feature suggestions, don’t hesitate to reach out!

*The views expressed in this article are mine and do not reflect the views of Oracle.*

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://thenewstack.io/wp-content/uploads/2025/07/aab6a63b-cropped-090dde64-lyudmil-pelov-600x600.jpeg)

As a senior principal product manager for generative AI at Oracle Cloud, Lyudmil Pelov leads the delivery of cutting-edge generative AI and agent services designed for enterprise customers. With extensive experience in building successful engineering projects and driving product innovation,...

Read more from Lyudmil Pelov](https://thenewstack.io/author/lyudmil-pelov/)