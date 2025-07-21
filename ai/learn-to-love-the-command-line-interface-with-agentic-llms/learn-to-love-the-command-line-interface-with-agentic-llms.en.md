We have reached a pivotal time in AI development, with many companies trying to grab mindshare over the right direction for LLMs in coding. Last year, I remained largely unmoved about the outcome until I started seeing code completion finish off a few of my methods, based solely on the cues of standard nomenclature and past patterns.

But today I see that the command line is the best place for the majority of LLM interaction for most developers. I’ve seen multiple offerings that prove the point — from Anthropic’s [Claude Code](https://thenewstack.io/claude-opus-4-with-claude-code-a-developer-walkthrough/), Open AI’s [Codex](https://thenewstack.io/testing-openai-codex-and-comparing-it-to-claude-code/), Google’s [Gemini CLI](https://thenewstack.io/gemini-cli-googles-challenge-to-ai-terminal-apps-like-warp/) and recently [Warp](https://thenewstack.io/warp-launches-ai-first-native-terminal-app-for-windows/). I’ll look at a slightly different direction, in the form of [kiro.dev](https://kiro.dev/), next week; but this week I want to look at what [Zach Lloyd from Warp](https://thenewstack.io/qa-how-warp-2-0-compares-to-claude-code-and-gemini-cli/) refers to as the “agentic development environment.”

Indeed, this does appear to be the agentic era, as [Claude Code usage growing by 300%](https://thenewstack.io/claude-code-user-base-grows-300-as-anthropic-launches-enterprise-analytics-dashboard) attests.

[![](https://cdn.thenewstack.io/media/2025/07/aed0131f-image-1024x574.png)](https://cdn.thenewstack.io/media/2025/07/aed0131f-image-1024x574.png)

[Agent performance over task at www.tbench.ai](www.tbench.ai)

As the diagram shows, there are a lot of well-practiced combinations of the terminal and LLM models. While Claude Code with Opus 4 feels like the most complete package, Warp slightly alters the math by providing a terminal better suited to LLMs. With the likes of [terminal-bench](https://www.tbench.ai/) introducing a nice evaluation harness with a set of tasks, now is a great time to experiment and find out what best suits your needs.

## Tasks Are Engineering

But let’s step back. Most developer jobs are a varied mix of engineering tasks and coding. The DevOps movement recognised that coding and infrastructure support are likely to be done by the same people — or if not, by people working together with the same production goals. But they are approached differently.

Developers have always known this, but coding has never been *exactly* a form of engineering — it’s slightly more art than we care to admit. Yes, there can even be “a vibe.” When you are about to type in a line of code, there are always several options, expressions or approaches you can take. You are both following on from what you were writing before, yet possibly guiding the code to a slightly different future shape. You build the model in your mind as you type. This is why many developers still hate [pair programming](https://thenewstack.io/advance-your-devops-with-pair-programming-even-remotely/) — they like to defer finality to the last responsible moment. Explaining yourself early forces you to open the box and observe the cat before you are ready to leave superposition.

> The CLI is where we do defined tasks. There is one desirable outcome, and probably one sensible way to achieve it.

And this is precisely why LLMs are so good at the command-line interface (CLI), because that is where I am definitely doing engineering. The CLI is where we do defined tasks. There is one desirable outcome, and probably one sensible way to achieve it. For example, if I made changes to code then I need git to stage, commit and push them. My only real decision would be the commit message — and LLMs do a good job with that.

Suddenly being able to write a task in English and have it completed automatically — or in defined stages with permission requests — provides measurable comparisons with doing it yourself. The LLM is really just mapping your statement with a list of existing commands (and scripts).

## When Do LLMs Excel With Dev Tasks?

When writing code, LLMs excel at specific times during the process. They are excellent template production machines. Even if they just grab the right example from the internet and place it in the right context in your project, that is real, measurable work. And if it is measurable, we can work out what we gain. But their role is strongest either before you write code, or when making changes once the code is largely written.

When you are using an IDE, rapid code completion can be useful, but it can also just get in the way much of the time. When I do hesitate, it is because my mind is working on the code — I am not waiting to be directed. The interruption can often feel like a microaggression. This will obviously improve over time, but for now, it isn’t the main event.

There is so much more to the development job than staring at code through the editor. Planning, network design, deployment, debugging, etc. Even though I don’t advocate [letting LLMs write tests](https://thenewstack.io/claude-code-and-the-art-of-test-driven-development/) directly, they can do that too. Starting a project off by asking the LLM in your CLI to set up a common environment and a template example for you is great. Asking it to make changes across your codebase, [like I did with Google’s Jules](https://thenewstack.io/agentic-coding-how-googles-jules-compares-to-claude-code/), does require some prompt engineering skills. But where it doesn’t do enough at first, just try again.

Most developers will use git to backpedal if it truly makes a mess. And in most cases this is no different to letting a junior developer develop the codebase — which is one reason why human interaction is another skill that developers must possess to do their work successfully.

Even the accursed [vibe coding](https://thenewstack.io/vibe-coding-is-here-how-ai-is-reshaping-the-software-developer-profession/) is a style that has its place; for example, when you are doing sprint zero, spitballing and you want to discern the art of the possible (maybe with your manager). Writing down what you want to see, while having little interest in exactly how it is achieved, makes perfect sense in those types of cases.

## Conclusion

One of my favourite artists is Olafur Eliasson. His studio is a collaborative hub with almost a hundred professionals, including craftsmen, technicians, architects and art historians contributing. However he views art, he views making it as a collective effort, with team members playing their part in developing and installing the artwork.

[![](https://cdn.thenewstack.io/media/2025/07/ef555af6-image-1-1024x682.png)](https://cdn.thenewstack.io/media/2025/07/ef555af6-image-1-1024x682.png)

[An installation by Olafur Eliasson](https://thespaces.com/olafur-eliassons-living-observatory/)

He understands, like we developers should, that while art is the product of one human mind, there is plenty of engineering around it. By all means, let the IDE be where you let your code flow, but make the CLI the center of your LLM workbench.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://cdn.thenewstack.io/media/2022/09/2e2ac7a2-cropped-a46bbf33-photo.png)

David has been a London-based professional software developer with Oracle Corp. and British Telecom, and a consultant helping teams work in a more agile fashion. He wrote a book on UI design and has been writing technical articles ever since....

Read more from David Eastman](https://thenewstack.io/author/david-eastman/)