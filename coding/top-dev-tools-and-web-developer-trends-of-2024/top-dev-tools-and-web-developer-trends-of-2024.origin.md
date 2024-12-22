# Top Dev Tools and Web Developer Trends of 2024
![Featued image for: Top Dev Tools and Web Developer Trends of 2024](https://cdn.thenewstack.io/media/2023/12/88ad96d3-year-wrapup-1-1024x576.png)
Sometimes a technology grabs the limelight while also creating space and resources for other things to grow in the canopy. The extra money flooding in to the LLM space has had a secondary effect of giving more breathing room for other, slightly more mundane, yet necessary, software projects. While not directly in the line of fire, other software projects have benefited from the disruption.

This post looks back at some of the highlights in developer tooling that I covered in 2024. Though I start with LLMs, I saw many other interesting developments in areas outside of AI.

## AI Tools for Developers
I think LLM development has become more parochial this year. Multimodal AI — the ability to consume or respond with images, sound and video — has been the standout practical achievement. Models have expanded their own abilities, competing with their own previous releases. The big vendors gave us bigger ([and smaller](https://thenewstack.io/the-rise-of-small-language-models/)) models. But there have been less obvious exponential jumps that reach outward. The launch of the Humane AI Pin reminded us that LLMs and their backers don’t have a firm grip on what AI means for most people. It’s telling that autonomous car projects have quietly reduced their expectations. Just last month, I pointed out that LLMs don’t yet have a place [within standard component development](https://thenewstack.io/why-llms-within-software-development-may-be-a-dead-end/) — neither in code, nor testable services.

However, tools that just host LLM behavior directly for their users have had a good year. We saw both [Cursor AI](https://thenewstack.io/using-cursor-ai-as-part-of-your-development-workflow/) and [Zed AI](https://thenewstack.io/an-introduction-to-zed-ai-and-how-it-compares-to-cursor-ai/) give users inline and chat access to LLMs, to improve some aspects of coding. [JetBrains AI](https://thenewstack.io/ai-and-ides-walking-through-how-jetbrains-is-approaching-ai/) also boosted its critically successful Rider product. However, LLM as add-ons always run the risk of effectively handing your business roadmap directly over to LLM providers when depending on them for improvements — in one case, Eric Yuan, CEO and founder of Zoom, admitted that the future of digital clones could only happen with an external innovation [“down the stack.”](https://www.theverge.com/2024/7/30/24209552/down-the-stack-baby)

Makers of IDEs that add AI may initially want to integrate the products more closely, but those decisions have trade-offs. Cursor AI chose to fork VS Code to improve the UI for their product, as opposed to just writing a plug-in. But that meant they couldn’t run .NET code directly, since Microsoft rejected non-Microsoft assembly. Incidentally, I’ve moved over to VS Code this year because [Visual Studio for Mac was retired](https://learn.microsoft.com/en-us/visualstudio/releases/2022/what-happened-to-vs-for-mac). So far, so good.

For more on AI for developers, check out our [wrap up of AI engineering trends](https://thenewstack.io/top-5-ai-engineering-trends-of-2024/) this year.

## Programming Trends for 2024
Meanwhile, much happened in dev tools outside of LLMs.

I mentioned Zed earlier — it [launched on Linux](https://thenewstack.io/zed-ported-its-text-editor-to-linux-and-its-pretty-special/) this year and was well received (but Zed shows no further signs of putting its name to a Windows version). Also in the Rustbelt, Warp is coming soon to Windows. Linux users also [got Warp this year](https://thenewstack.io/warp-is-a-power-users-dream-terminal-for-linux/), but to those users a partially closed-source, VC-funded, MacOS-first product with AI as a central feature was a bit of a turn off — they’re quite satisfied with [Kitty](https://sw.kovidgoyal.net/kitty/), thank-you.

We saw quite a few launches, or significant updates, for new languages this year. Both [Virgil](https://thenewstack.io/introduction-to-virgil-a-new-language-by-wasms-co-creator/) and [Zig](https://thenewstack.io/introduction-to-zig-a-potential-heir-to-c/) are lightweight high-performance systems with in-built cross-compilers. [Gleam](https://thenewstack.io/introduction-to-gleam-a-new-functional-programming-language/) is a new type-safe functional language, while [MoonBit](https://thenewstack.io/moonbit-wasm-optimized-language-creates-less-code-than-rust/) is optimized for WebAssembly (Wasm). Indeed, Wasm has given another option for complex behavior in websites — I’d suggest this was a good year for understanding what Wasm can offer.

The interest in new languages is a product of the continuing multilingual nature of modern developers but also the massive improvement in the understanding of onboarding from even one-person projects. Almost all projects have a coherent *getting started* path these days and understand the worth of [playgrounds](https://thenewstack.io/playgrounds-for-developers-uses-and-design-patterns/).

## Frameworks and Deployment Tools
Last year we saw the start of a [cloud computing backlash](https://techcrunch.com/2023/03/20/the-cloud-backlash-has-begun-why-big-data-is-pulling-compute-back-on-premises/). In February this year, [Kamal](https://thenewstack.io/how-to-exit-the-complexity-of-kubernetes-with-kamal/) was revealed by [David Heinemeier Hansson](https://www.linkedin.com/in/david-heinemeier-hansson-374b18221/)’s software company as a local deployment system — or “[Capistrano](https://thenewstack.io/why-capistrano-got-usurped-by-docker-and-then-kubernetes/) for containers.”

Talking of DHH, I also looked at [Omakub](https://thenewstack.io/introduction-to-omakub-a-curated-ubuntu-environment-by-dhh/), a heavily curated Ubuntu installation for developers. This is typically opinionated but is a good place to start as a Unix developer if you haven’t honed a Linux build over the last few years. As I did, you can check this over on a virtual machine.

Looking at app frameworks, [Payload](https://thenewstack.io/introduction-to-payload-a-headless-cms-and-app-framework/), the headless CMS, moved to version 3 this year. I also looked at the static site generator [Eleventy](https://thenewstack.io/introduction-to-eleventy-a-modern-static-website-generator/) over a [couple of posts](https://thenewstack.io/getting-up-to-speed-with-eleventy-config-and-collections/). A new static site generator I recently checked was [Nue](https://thenewstack.io/nue-a-new-static-site-generator-taking-on-next-js/), which is quite clearly riffing off Vue and competing with Next.js. If the term [Jamstack](https://thenewstack.io/is-jamstack-toast-some-developers-say-yes-netlify-says-no/) is diminishing in use, it is only because deploying to CDNs is just a default now.

[Deno](https://thenewstack.io/how-oop-developers-can-get-to-know-typescript-through-deno/) is a JavaScript runtime that treats TypeScript as first class. While I looked into how TypeScript can help bridge the coding gap between JavaScript and the likes of C# or Java, Deno also has a Heroku-style deployment offering which looks nice.
There are a number of projects that don’t fit into identifiable niches. While [Glamorous Toolkit and moldable development](https://thenewstack.io/a-developer-guide-to-using-glamorous-toolkit-on-at-protocol/) are still locked into Smalltalk, they offer a strong alternative to looking at and thinking about a codebase, and are slowly making it more accessible. In the post, I looked at using the toolkit to examine Bluesky’s AT protocol (this was before the growth spurt in Bluesky as a platform).

[System Initiative](https://thenewstack.io/how-system-initiative-treats-aws-components-as-digital-twins/) went live this year with its digital twin approach to infrastructure deployment. It now has a solid SaaS offering, as well as a local build option. It only works with AWS right now, and I do hope they can integrate with other cloud providers. As it is, Amazon could have its eye on acquiring System Initiative to help hoist itself a little higher up the value chain.
[Markwhen](https://thenewstack.io/introduction-to-markwhen-a-markdown-timeline-tool-for-devs/) rounded off the year, appropriately enough looking at time and how it can be represented in a Markdown-like language. The editor can be used to show GANT-like project charts, but time will tell if it gets adopted by other projects.
## 2024 in a Nutshell
I think this was a pretty vibrant year for development tool releases, some with LLM assistance — but also many without.

On the programming front, Wasm use has expanded, and people are measuring its value.

There seems to have been fewer pure open source plays this year, which has resulted in teams needing to communicate trust — so more blogs, videos and social media posts.

I’ve enjoyed reporting on the continuing growth of the bigger efforts, as well as the more innovative one-person projects. Roll on, 2025.

[
YOUTUBE.COM/THENEWSTACK
Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.
](https://youtube.com/thenewstack?sub_confirmation=1)