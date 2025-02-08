# Beyond DX: Developers Must Now Learn Agent Experience (AX)
![Featued image for: Beyond DX: Developers Must Now Learn Agent Experience (AX)](https://cdn.thenewstack.io/media/2025/02/44ca9d29-ave-calvar-h5rexzafgdi-unsplashb-1024x576.jpg)
In a blog post this month introducing the concept of “[Agent Experience](https://biilmann.blog/articles/introducing-ax/)” (AX), Netlify CEO [Matt Biilmann](https://www.linkedin.com/in/mathias-biilmann-christensen-a5a3805/) noted that “today, more than 1,000 sites are being created on Netlify directly from ChatGPT every single day.”

Despite knowing that the majority of software developers already use [AI-assisted coding tools](https://thenewstack.io/whats-ahead-for-ai-assisted-coding-open-source-and-more/), I was surprised to read that 1,000 new sites are created each day on Netlify directly from AI. That indicates a deeper trend: that the start of a development project is increasingly being automated using AI — either through a chatbot like ChatGPT (as in Netlify’s case), or through [AI agents](https://thenewstack.io/ai-agents-a-comprehensive-introduction-for-developers/).

I spoke to Biilmann to find out more about the trend of AI automation in software development projects. We also talk about AX, which Biilmann says is an associated developer pattern that has already become a key part of Netlify’s platform.

## Why Are Devs Using AI To Launch Sites and Apps?
Much of the ChatGPT activity on Netlify is coming through [a plugin](https://www.netlify.com/integrations/openai/netlify-chatgpt-plugin-netlify-api/) the company developed for ChatGPT. The description reads: “Simply describe the website you want to build, and ChatGPT will deploy it to Netlify for you!”

“In integrating with ChatGPT, we learned that we needed to give it specific flows around authentication and handovers and so on.”

– Matt Biilmann, Netlify CEO
But what kinds of sites are being created using ChatGPT? Biilmann told me there are two or three main use cases.

“One is what you would almost call, like, ephemeral sites or apps […] where people ask ChatGPT to build something displaying some information or some data, or a reading card, or a fun slide, or a spur of the moment — deploy it, and they have a URL they can share, right?”

That’s similar to how developers use [a platform like Glitch](https://thenewstack.io/glitch-brings-view-source-philosophy-to-react-node-js/), so there’s nothing really new there. But the second usage Biilmann sees for ChatGPT is “people figuring out how to start a new project.” Both experienced developers and people who aren’t professional developers are doing this, suggests Biilmann.

“That’s the [use case] that may be bifurcated into two, where one is more of an actual developer who knows what they’re doing but wants to start faster,” he said. “I think more of those are now going outside of ChatGPT and directly to tools like Bolt or Lovable, or tools that really cater to them, or Windsurf — it’s that level of tooling.”

## Rise of the Agentic IDE
The tools that Biilmann mentioned are just a few of the, for want of a better term, [agentic IDEs](https://generativeprogrammer.com/p/ai-coding-assistants-landscape) that have recently come onto the market. [Bolt](https://bolt.new/) is a tool that was spun out of StackBlitz last October, [Windsurf](https://codeium.com/windsurf) was released in November (and actually calls itself an “agentic IDE”), while [Lovable](https://lovable.dev/) launched in its current iteration (it was previously an open source project called GPT Engineer) in December. So these are all very new products — and all three seem to have grown rapidly in recent months.

![](https://cdn.thenewstack.io/media/2025/01/5fca8da5-windsurfermain.jpg)
The Windsurf UI, via [a recent tutorial on The New Stack](https://thenewstack.io/windsurf-an-agentic-ide-that-thinks-and-codes-with-you/) by Jack Wallen.

It’s also worth mentioning Replit and Vercel, both of which have released AI automation products. [Replit Agent](https://blog.replit.com/introducing-replit-agent) was launched last September and is described as “our AI system that can create and deploy applications.” Vercel launched [v0](https://v0.dev/) way back in October 2023, although it’s positioned more as a chat product (like ChatGPT but for frontend developers) than an IDE.

Last month, Matt Biilmann created a new personal blog using one of these tools: Bolt.

“This blog was built almost exclusively through prompting,” [wrote Biilmann](https://biilmann.blog/articles/i-built-a-blog/) in his first post. “It started with a bolt.new prompt that spun up a simple Astro-based blog deployed to Netlify, followed by a few tweaks here and there with Cursor and Windsurf.”

The beauty of these tools is that they make developing a custom website or app more approachable for people who aren’t necessarily full-time developers. As Biilmann put it, there’s “a whole new class of developers that are suddenly learning to build for the web” by using AI tools.

## Designing for AI Agents
The path toward what’s now turned into AX began when Netlify integrated with ChatGPT for its plugin. This led them to the realization that an agent will use the Netlify platform differently than a human user.

![Status quo before AX](https://cdn.thenewstack.io/media/2025/02/c27569d5-statusquo.png)
![Status quo before AX](https://cdn.thenewstack.io/media/2025/02/c27569d5-statusquo.png)
Status quo before AX, from [an article](https://agentexperience.ax/research/agent-web-and-its-interface/) by Netlify’s Sean Roberts.

“In integrating with ChatGPT, we learned that we needed to give it some specific flows around authentication and handovers and so on,” said Biilmann. “Projects suddenly start from an agent, not from a user doing something — so you need that agent to be able to, for example, deploy to Netlify before the user has created an account themselves.”

But he also noted that AX isn’t necessarily just improving the “experience” of an AI agent — it’s also important to consider the human in the loop.

“Sometimes it’s solely about how you make the experience for an agent better,” Biilmann explained. “What you need to think through is how you make the experience better for an agent collaborating with a human.”

In [the company blog](https://www.netlify.com/blog/the-era-of-agent-experience-ax/), it was noted that Netlify has become “the deploy target for the agents” of several partners: Devin, Bolt and Stripe are mentioned. But enabling agents to automatically deploy their sites and apps to Netlify is just the beginning, says Biilmann.

“We also are thinking a lot about how to make our primitives better, to write for a Cursor or a Copilot, or any of those [AI coding tools]. I just see it as […] a very strong natural tendency that all developers will be working together with coding agents to build their projects.”

In other words, AX and agents will become a key part of [Netlify’s “composable web” platform](https://thenewstack.io/netlify-launches-composable-web-platform-for-enterprise-devs/).

## An Open Agent World
In addition, Biilmann would like to see open standards emerge for AI agents, similar to web standards.

“We need to also start doing some industry work around […] how are we actually going to make the web better for agents? What shared standards can we come up with, and what do the agents actually need for the web?”

“People will bring the agent

theywant to use, versus the agent you want them to use.”
– Biilmann
Netlify has always been a supporter of the open web — because, frankly, it’s good for their business — and now the company wants to get behind open agents. Similar to how Netlify has what it calls a “[framework agnostic](https://thenewstack.io/why-netlify-is-tech-agnostic-and-its-role-in-jamstack-development/)” view on web development tools, it wants to embrace all kinds of different agents. As Biilmann put it, “People will bring the agent *they* want to use versus the agent you want them to use.”

To kickstart this movement, Netlify has created a website at [AgentExperience.ax](https://agentexperience.ax/) (to save you the search query: .ax is the domain for the Åland Islands, an autonomous region in Finland). A bit like Netlify’s [website for Jamstack](https://web.archive.org/web/20171005081251/http://jamstack.org/) back in 2016/17, the Agent Experience site lays out some definitions and concepts while also inviting the community to get involved.

[
YOUTUBE.COM/THENEWSTACK
Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.
](https://youtube.com/thenewstack?sub_confirmation=1)