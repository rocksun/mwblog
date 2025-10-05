There seems to be an underlying assumption that the best language for an agentic web is JavaScript. [Chris McCord](https://github.com/chrismccord), an Elixir developer, begs to differ.

McCord is the creator of the [Elixir](https://thenewstack.io/elixir-an-alternative-to-javascript-based-web-development/)-based [Phoenix web framework](https://www.phoenixframework.org/) and spoke at September’s  [ElixirConf US 2025](https://elixirconf.com/), which was recently [released on YouTube](https://www.youtube.com/watch?v=6fj2u6Vm42E). To prove his point, he started his talk by spinning up an AI agent to create a Slack clone using [Phoenix](https://github.com/phoenixframework/phoenix) and an Agents.md in the project.

“Agents.md is just a flat markdown file and this isn’t documentation,” he said. “[Agents.md is for LLM](https://github.com/openai/agents.md)s, not for humans.

McCord noticed that frontier models tended to falter with Elixir in a couple of ways, he said. To fix that, he wrote a customized [AGENT.md file](https://github.com/phoenixframework/phoenix/commit/50ffaa5aa1c60503f01cd2107edd43f22435f9e7) to teach the AI to write correct, idiomatic Elixir code and warn against common errors, such as the tendency of [large language models (LLMs)](https://thenewstack.io/taming-llm-sprawl-why-enterprises-need-an-ai-gateway-now/) to list index-based access.

“Really, this is just to smooth over the things that the agents do that are dumb, like trying to do list index-based access,” he said of the AGENTS.md file. “AGENTS.md is lessons learned from me, burning a ton of tokens. In the [Phoenix.new](https://phoenix.new/) product, that now exists in everyone’s project starting out.”

The file also provides context by providing the agent with a consistent architectural starting point to ensure the AI-generated code aligns with Phoenix’s conventions. When coupled with the AGENT.md, he argued, Elixir is the language best prepared to be the frontend language for an [Agentic AI world](https://thenewstack.io/the-agentic-web-how-ai-agents-are-shaping-the-webs-future/).

## Some Context about AI Agents

“The reason why you can’t stop hearing about agentic coding, agentic workflows is because people have taken these chatbots and put them in a loop and they can actually accomplish real tasks in the world, and they can do it remarkably well,” McCord said. “We’re on this [Moore’s Law](https://newsroom.intel.com/press-kit/moores-law) of what they can do and how long they can stay on track.”

And research shows agents are doubling in task link capacity every seven months, he said.

“What this means is, I can stick [Claude Code](https://thenewstack.io/claude-code-user-base-grows-300-as-anthropic-launches-enterprise-analytics-dashboard/), [Gemini CLI](https://thenewstack.io/googles-gemini-cli-agent-comes-to-github/), whatever LLM I want, put it in a loop and stick it on a task and how long it can actually work on completing that task without going off the rails is doubling every seven months,” he said. “In less than a year, we’re having this quadratic growth.”

Even if that plateaus, he said, Elixir has already broken a “useful value threshold where context windows are big enough” that LLMs can stay on track long enough and collapse their windows but keep working on problems.

> “What really matters for us is Elixir can own this space. It’s basically our time to build with agents and build agents, and Elixir just happens to be the perfect language to do that.”  
> **— Chris McCord, creator of the Phoenix framework**

For instance, the new Phoenix agent self-collapses its context window but keeps working, he added.

“It can work on these long-term problems without having to say, ‘Start a new chat because there’s just too much in my brain right now,'” McCord said. “It can self-summarize and it can continue.”

That also means the time between starting a task and ending it is getting longer, he said. We’re shifting from a straight chat experience to more of an assistant, where a user can tell the LLM to go and take action, and then find that it did actually complete the action.

## AI Agents Joining the Workforce

While McCord did advise everyone to take a grain of salt when facing AI hype, he also thinks a lot of the hype could become reality — and outside the early adoption domain of programming.

McCord pointed out that OpenAI CEO [Sam Altman](https://thenewstack.io/openais-sam-altman-sees-a-future-with-a-collective-superintelligence/) caught a lot of flack for saying 2025 would bring the [first AI agents into the workforce](https://www.axios.com/2025/01/10/ai-agents-sam-altman-workers) and would materially change the output of companies. While many took that to mean it would replace every job, if you look at it, Altman wasn’t wrong, McCord said.

“He caught a lot of flack for this, and the funny thing is, we could have developers today, in this room, that use [Claude code every day](https://thenewstack.io/testing-openai-codex-and-comparing-it-to-claude-code/), or some other coding agent, and read this statement and scoff at it,” he said. “Simultaneously, they’re using an AI agent who has joined their company that is materially changing the output of their company. So I think that statement is actually true at least in the realm of tech companies.”

AI is doing hours of independent work for people on par with experts, McCord said, and that is expanding what every person in the team is capable of.

“This is my lived experience,” he said. “I’m burning tokens for hours per week and it’s materially changing the output that I can do for myself and within the company.”

But AI companies are predicting more advancements. For example, [Anthropic predicts](https://ai-2027.com/) we will soon see breakthrough solutions that would have taken years to accomplish without AI.

Regardless of which path is true — that we’re slowly tapering off AI’s capabilities or that we’re only seeing the beginning of its power — this is an opportunity for Elixir, McCord said.

“What really matters for us is Elixir can own this space,” he said. “It’s basically our time to [build with agents](https://thenewstack.io/dont-build-chatbots-build-agents-with-jobs/) and build agents and Elixir just happens to be the perfect language to do that.”

## The Accidental AI Genius

McCord noted that the Erlang and its [virtual machine BEAM](https://elixirforum.com/t/what-does-beam-have-to-do-with-erlang/50775), which powers Elixir, “accidentally made the perfect language for multicore before multicore was invented.”

“They accidentally made the perfect language for the modern Internet before the Internet existed and they accidentally made the perfect language in VM for this [agentic age before LLMs](https://thenewstack.io/learn-to-love-the-command-line-interface-with-agentic-llms/) were a thing,” said McCord. “It’s like we continually constantly find these things that accidentally … happen to perfectly map themselves to the modern problems of programming and computing.”

In the same way, Elixir was “perfectly well suited to really dominate ” agentic AI, he said.

“We’ve always been about being on the bleeding edge of technology and what we’re trying to accomplish if you look throughout our history,” McCord said. “We’ve always been about building the things we want to build, building the future we want to see.”

And “what we’ve wanted to build, at least for me, was servers, multiplayer games, collaborative chat apps that scale to millions of users,” he said. ”We have the perfect platform to do that. So, we did it.”

> “It’s like we continually constantly find these things that accidentally … happen to perfectly map themselves to the modern problems of programming and computing.”  
> **— McCord**

So how does Elixir help with LLMs? “We’re keeping a system index in memory on a gen server, we monitor the file system on the client and we monitor the file system on the client and we send every file change up to the server with that file content,” he said. “At any time, the LM has a current view of the working files of the codebase.”

Elixir is prepared to deal with LLM problems that other people are still trying to solve, McCord said, such as caching temporarily and garbage collection.

“There’s all these problems that other folks will necessarily need to solve with agents …  that are just not problems for us. It’s not even in our consciousness,” he said. “We just write the trivial thing and it just works.”

The problem is, LLMs are trained on the internet and the majority of code on the internet is JavaScript. So LLMs tend to write apps in JavaScript. That’s led to the negative opinion in the Elixir community that Elixir will be left behind; he warned against that. Instead, he said, the view should be that anyone can now use Elixir or Phoenix with the support of an LLM.

He pointed to the Elixir ecosystem’s unified tooling. That gives Elixir a major advantage in the age of AI, especially when compared to fragmented ecosystems like JavaScript. Elixir is about being developer-first, he noted, but that also makes it good for LLMs.

“Other than [Go](https://thenewstack.io/go-experts-i-dont-want-to-maintain-ai-generated-code/), we’re probably one of the few platforms that have this non-fragmented, cohesive experience because we have Mix, your build tool,” he said. “All the new features of Phoenix, we’re always thinking about how do we best serve the LLM. But by best serving an LLM, we’re actually serving the developer who’s using these tools that are large language models.”

The community’s focus should be on providing everyone with the best experience with an LLM. To do that, Elixir has introduced [Tideway Web](https://tidewave.ai/), a specialized AI-powered coding agent designed for full-stack development in the Ruby on Rails and Phoenix/Elixir ecosystems. It runs in the browser, he said, and can be used for vibe coding.

There’s also Phoenix.New, a remote AI runtime for Phoenix that offers a low-code application option.

“Someone that’s not a programmer can just come in and ask for an app and they can they have a editor in the browser, but they don’t actually need to know what they’re doing and they can actually get into Phoenix,” he said. “They can have a working app that they can try and run and then clone on the computer.”

Elixir’s cohesive tooling and language design, McCord argued, make it the perfect platform for agentic AI: “The whole idea is giving someone the best experience they have with these coding agents.”

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://thenewstack.io/wp-content/uploads/2023/08/4de88b83-4756312a-326a38b7-lorainelawson2-600x600-1-600x600.jpeg)

Loraine Lawson is a veteran technology reporter who has covered technology issues from data integration to security for 25 years. Before joining The New Stack, she served as the editor of the banking technology site Bank Automation News. She has...

Read more from Loraine Lawson](https://thenewstack.io/author/loraine-lawson/)