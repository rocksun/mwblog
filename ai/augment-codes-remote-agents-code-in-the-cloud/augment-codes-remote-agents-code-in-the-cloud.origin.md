# Augment Code’s Remote Agents Code in the Cloud
![Featued image for: Augment Code’s Remote Agents Code in the Cloud](https://cdn.thenewstack.io/media/2025/06/9d7de112-goran-ivos-toracb4aqrc-unsplash-1024x769.jpg)
[Goran Ivos](https://unsplash.com/@goran_ivos?utm_content=creditCopyText&utm_medium=referral&utm_source=unsplash)on
[Unsplash](https://unsplash.com/photos/macbook-air-beside-white-coffee-cup-TorAcb4AQRc?utm_content=creditCopyText&utm_medium=referral&utm_source=unsplash).
[Augment Code](https://www.augmentcode.com/), the AI coding tool that specifically [targets professional developers](https://thenewstack.io/augment-code-an-ai-coding-tool-for-real-development-work/), recently previewed a feature it calls Remote Agents. These AI agents extend Augment Code’s existing code completion and chat features in a way that’s not unlike GitHub’s [recently announced Coding Agent](https://thenewstack.io/github-launches-its-coding-agent/).
As the name implies, developers can give these agents specific tasks (think fixing small bugs to refactoring code or extending test coverage), and then Augment Code will spin up a cloud environment for the agent to work on this issue and test its code. For Augment Code, there’s another twist here: you can run up to ten of these agents in parallel (though they don’t interact with each other yet — that’s on the roadmap, though).

The Remote Agents are now generally available.

As Augment Code co-founder and CEO (and former Pure Storage CEO) [Scott Dietzen](https://www.linkedin.com/in/scottdietzen/) told me, the one feature that has always set Augment Code apart — and that explains its growing popularity in a market that is starting to feel a bit saturated now — is its context engine. As Dietzen noted, Augment Code’s first product was essentially a synchronous code completion tool, similar to what its competitors were doing already.

“The thing that made our original agent unique was this deep knowledge of customer code,” he explained. “In general, agents often get lost. But if you can have an agent that’s an expert in your code base rather than a novice, they can be entrusted to do a great deal more. And so this context engine that our AI research team built over two and a half years turns out to be a profound differentiator for agents, because the more autonomous you’re looking something to be, the more you critically rely on that context.”

The promise of Augment Code’s context engine is that it can build a full semantic map of a company’s code base — all while respecting existing access controls so that the bot won’t reason over code that a given user doesn’t normally have access to. This map is updated in real time and then becomes the basis of Augment Code’s retrieval-augmented generation (RAG) pipeline. This is what allows these agents and code completion tools to access the right context to work on a problem. Then, if the agent needs more context, it can always request it.

Most recently, the company also launched the [Augment Agent](https://www.augmentcode.com/blog/meet-augment-agent), a synchronous agent that’s more akin to a Claude Code and the tools built into products like Cursor and Windsurf. And while Augment Code saw a 15x increase in inference cycles consumed by the early adopters of the Augment Agent, it’s still a tool that runs in the IDE and expects developers to wait for it to finish its work.

“If you want to be a tech lead for a team of agents, you don’t want to have to wait for the first agent to finish its job before you start the second. So really, before we even launched the synchronous agent model, we wanted a remote or asynchronous agent model where you could spin up, in our case, up to 10 agents and have them all working on different tasks in parallel,” Dietzen said.

For both the synchronous and asynchronous agents, Augment Code also uses its Memories feature, which allows users to write down the exact preferences for how the agent should write the code. Those may be language preferences, for example, or even more detailed instructions about how exactly the agent should go about its work.

Dietzen noted that, at least in their current form, Remote Agents typically work best for tackling tasks that would typically take a seasoned developer half a day to a day to work through. Anything more open-ended, and the agent will likely “get lost and flail and not succeed,” Dietzen said. Developers need to come in with realistic expectations of what these tools can do, he noted.

“The challenge still in front of us is helping all enterprises across broader teams,” he said. “We’re doing very well with these expert early adopters, and they’re the ones that love our product. We go into lots of shops where we find competitors [GitHub] Copilot and Cursor and so on. But often, it’s the expert users that have dropped them because they don’t find that they add enough value for them to stick with them.”

## Agents and the Rise of the Meta Programmer
One interesting statistic here is that the Cursor IDE is actually the third-most popular IDE for Augment Code users (with VS Code and the JetBrains family of IDEs leading the pack).

Dietzen also explained that increasingly, he is seeing what he calls “meta developers,” that is, developers who never really touch the code itself but have the agents handle all of that. “They consider a point of pride that the agent does all of the programmatic manipulation,” he said. “And I’m like: sometimes you’re working harder to get the agent to do what you want. But you know what, I think it’s a great exercise of the paradigm that they’re staying out of the code themselves, and it shows you how much we have progressed. Because that wouldn’t have been possible even five months ago, to have an agent do all of the coding, provided you give them the insight.”

Compared to working with a novice human programmer, you may have to be a bit more prescriptive to get the agent to do what you want it to do, but Dietzen noted that the agent also needs less help because it has this deep contextual understanding of the codebase.

We’ll still need the software engineers for the inspiration, Dietzen said. Somebody has to have the creative insights and set the direction, after all. And, he stressed, the majority of coding, especially in the enterprise, isn’t about starting new projects. It’s about maintaining existing code and adding new features to it.

“Vibe coding is fun, right? And turning on software development to people that never got to do it before is interesting,” Dietzen said. “But if you want to make the world a better place, there’s a staggering amount of value in our existing software that is not being properly levered because of missing features, reliability, so on, and so being able to go after that software, bringing AI to bear on the software that runs the world, as we say, and help professional software engineers, to me, that’s so much more exciting than vibe coding is.”

[
YOUTUBE.COM/THENEWSTACK
Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.
](https://youtube.com/thenewstack?sub_confirmation=1)