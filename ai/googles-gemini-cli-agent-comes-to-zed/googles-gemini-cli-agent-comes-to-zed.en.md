Since it first [announced Gemini CLI](https://thenewstack.io/gemini-cli-googles-challenge-to-ai-terminal-apps-like-warp/), Google’s open source AI agent in the terminal, in June, the company worked to bring it to other surfaces as well, including [GitHub](https://thenewstack.io/googles-gemini-cli-agent-comes-to-github/) and [VS Code](https://developers.googleblog.com/en/gemini-cli-vs-code-native-diffing-context-aware-workflows/). Today, Google is adding [Zed](https://zed.dev/) to the mix, the high-performance open source code editor written in Rust.

Zed, which has long used its underpinnings as a multiplayer editor to also bring AI agents into the mix, will now also allow developers to integrate Gemini CLI directly into the editor.

“We really built Gemini CLI to be infinitely extensible,” [Ryan J. Salva](https://www.linkedin.com/in/ryanjsalva/), the senior director of product at Google in charge of developer experiences, told me. “We’ve had lots and lots of folks build out GitHub Actions, using it, build out their own custom slash commands, use it to organize notes, to conduct research, do all sorts of things. But there’s one developer tool out there that rather than them coming to us to integrate, we came to them to integrate.”

That product, he said, was Zed, in part because he and his colleague [Keith Ballinger](https://www.linkedin.com/in/keithba/) are heavy Zed users themselves. Surely, it also helped that Salva and Zed co-founder [Nathan Sobo](https://www.linkedin.com/in/nathan-sobo-92b46720/) worked on the Copilot project together at GitHub, where Ballinger also worked in the past.

[![](https://cdn.thenewstack.io/media/2025/08/3856348a-gemini-cli-zed-integration.gif)](https://cdn.thenewstack.io/media/2025/08/3856348a-gemini-cli-zed-integration.gif)

Image credit: Google.

When talking to the Zed team, the focus was on how they could take the CLI tool and best integrate it into the IDE. The fact that both projects are open source also helped here, as well as Zed being extensible from day one.

“As we built our initial agentic experience in Zed for editing, I was like: we should make this extensible,” Sobo said. “It’s crazy that we didn’t do it at the first cut, we compiled the agent basically directly into the Zed binary, and we have our own agent offering. But I’m like, it seems like there’s going to be more than one of these things, there’s going to be potentially a lot of different agents solving different problems in different domains.”

Meanwhile, he noted, developers will likely also want to talk to more than one agent. “The idea of letting more people play that game with us and Zed, and just letting developers use the agent that they want to use, or even build their own, is what I’m excited about,” Sobo explained.

As Ballinger also stressed, the developer experience for using AI agents may start with chat, which Zed has been doing for a while using its agent side pane, but that’s just the beginning.

“This is one of the nice things about the tip of the spear of being developers: we can experiment and find the right ways, right? And so we’re following the edits. Or when you’re doing a next edit, completion — you’re no longer chatting, right? Or you’re doing something else and it’s in there with you — we’re going to see that,” Ballinger said.

That’s something Sobo agrees with, too, and he noted that Zed’s background as a multi-user editor (something that the team hasn’t emphasized all that much in the AI era but that’s still very much at the core of Zed) will likely turn out to be helpful here.

“I think [humans and AI agents] need to be in this shared environment together, and building the illusion of this shared, continuous environment that we all share? One of our big 2026 initiatives is to solve that.”

In its current iteration, the Gemini CLI in Zed allows the user to follow what the agent is doing in real-time, with a debug mode available that lets you see exactly what the agent is thinking at any given time. As with similar tools, once the agent is done, the user will be presented with a diff for every proposed edit, allowing the developer to review, accept or modify any changes.

One other feature the team stressed is that you can also give the agent access to your documentation or API specs by providing it with the relevant links.

## Making It All Work: The New Agent Client Protocol (ACP)

Making this all work is the new Agent Client Protocol (ACP), which the Zed team built to make it easier to integrate the agent into the editor — or really any other program that wants to provide a user interface for AI agents.

“The ACP creates a blueprint for how any editor can communicate with any AI agent, paving the way for a more modern and interconnected development stack for everyone,” the Zed team explains in today’s announcement. As Sobo noted, the idea here was to build “the simplest possible thing that could work.” It’s basically just a handful of JSON-RPC requests and responses, he said.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://thenewstack.io/wp-content/uploads/2025/03/15a7eb12-cropped-4e88ac40-frederic-profile-2-600x600.jpg)

Before joining The New Stack as its senior editor for AI, Frederic was the enterprise editor at TechCrunch, where he covered everything from the rise of the cloud and the earliest days of Kubernetes to the advent of quantum computing....

Read more from Frederic Lardinois](https://thenewstack.io/author/frederic-lardinois/)