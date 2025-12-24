From a software development perspective, there is little doubt what 2025 will be known for when looking back. In fact, it already has a somewhat wild name: the Agentic Era. It didn’t even need a full year to pick up that moniker.

At the beginning of the year, we were all getting used to a ChatGPT box appearing in IDEs like VS Code — for example, [JetBrains made an extension available](https://thenewstack.io/exploring-the-jetbrains-ai-assistant-for-visual-studio-code/). But early April was the first time I would write about [Claude Code](https://thenewstack.io/claude-code-and-the-art-of-test-driven-development/) and come across an “agentic CLI” (command line interface).

On re-reading the article now, I quoted the term “agentic” only once and never use the term CLI. It wasn’t until the end of May — when [Claude Opus](https://thenewstack.io/claude-opus-4-with-claude-code-a-developer-walkthrough/), a stronger Large Language Model (LLM), was introduced — that I mentioned the term “agentic” multiple times.

One of the better ways of thinking about the relationship between an LLM and the web is to remember that the intelligence is already in the web — because we humans wrote the pages. Think of LLMs as oracles who can read “between” the pages somehow. They don’t really know anything as such, but they do know how to look at the web in a way we cannot, then extract information and format it into useful answers. Mostly.

## What Is an AI Agent in Software Development?

What is an agent? [It’s just an LLM, a loop, and enough tokens](https://ampcode.com/how-to-build-an-agent). But the importance of the agentic loop hits home when you see it re-enter it’s own solution and fix it. This does not necessarily work so well in the real world: I’ve seen a few examples of the two-frame comic meme of someone asking AI whether a particular mushroom is edible, the AI says “yes” and in the next frame the person is dead — and the AI says “sorry” and “would you like to learn more about poisonous mushrooms?” to a gravestone. But there is no problem doing this in code. In fact it is more effective than you initially imagine.

What chained agent calls also add is the ability to move step-by-step, to try again and to improve. We humans understand this behavior. Agents can also to try to use local tools (via the Model Context Protocol, MCP, which we’ll come to) that might fail for reasons that can be corrected. This stops the AI solution being a Jenga tower that will all come down if one of the foundation blocks isn’t safe.

## Key Use Cases for Agentic LLMs in Coding

Within the coding community, most developers grokked it. Plenty of areas remain in dispute, but in the main there is no doubt that agentic LLMs just work — and work well in constrained cases. This is actually quite rare; most new ideas get a much more uneven uptake. But with LLMs, one quickly got an idea of what they really could manage. Task-oriented jobs, working with existing patterns, “thinking” as a junior engineer (not a senior one). Here are the shining examples:

* Transformation of formatted data, like JSON. By transformation, I mean following a rule to change one pattern into another. For example, I tried this with [Codex](https://thenewstack.io/testing-openai-codex-and-comparing-it-to-claude-code/). And after making a change, an agent has the ability to look at its own solution and fix it if it sees the format has been broken.
* Style and code fixes, and even imaginative improvements where examples exist and the style is understood within computing. Vitally, because LLMs do understand context, they can be trusted with finding suitable matches, unless your subject matter is too far out. [In my Jules example](https://thenewstack.io/agentic-coding-how-googles-jules-compares-to-claude-code/), Jules was able to find appropriate icons from reading my menu lines, while updating my UI layout with Bootstrap. These are relatively low-risk tasks.
* Code generation tasks that are logical extensions of existing code. Best seen in code completion, but new sections of code can always be usefully generated where local examples exist. In addition, writing methods are based solely on convention. So if I write a SwitchOn() method, a compatible SwitchOff() method can be generated.
* Setting up project templates on your drive. Once permission is granted, LLMs can find the appropriate project setup and run it locally to create the folders and files on your machine. If they make permission errors or get the configuration wrong, they can generally fix this. I believe this has accelerated vibe coding more than anything else, because this flips the switch from “your code” to “my code.”

## The Evolution From IDE Chatbots to Agentic CLIs

Previously, we would have used a standard IDE, opened the ChatGPT box, and explained the task to be done. We probably would’ve needed to be in the file, or have selected a fragment.

The first agentic requests were done by shooting off separate small tasks like “you go and adjust the file,” “check the style used in the rest of the project,” and “check our knowledge of this area.” This means that work was split into units and progress was visible. In comparison to Agentic CLI, the ‘ChatGPT box in an IDE’ approach is somewhat limited — although it is probably much cheaper in terms of tokens.

## Understanding the Model Context Protocol (MCP)

The other differences we saw with agentic code platforms is that they could access your drive. This was down to [Model Context Protocol](https://thenewstack.io/model-context-protocol-a-primer-for-the-developers/) — think of it as a **universal connector of tools to LLMs**. This open protocol from Anthropic allows an agent to “choose” a tool that advertises itself as being appropriate for a task. So a tool that writes and reads from a drive doesn’t have to be rewritten again and again. We saw this used to maximum effect with [OpenAI’s Apps SDK](https://thenewstack.io/openais-apps-sdk-a-developers-guide-to-getting-started/).

I can’t help feeling the good vibes that Anthropic got from Claude helped it get the nod without too much examination — there are other connection protocols out there, but MCP came at just the right time.

## Learning to Limit and Control AI Agent Access

While trust in agentic systems is increasing, we still want to limit what an agent can do (especially on your machine) and where they can do it. The advantage of acting within a shell is that you are using shell commands to make changes to your drive contents; access commands can be controlled by allow lists and deny lists.

As for reach, most agentic platforms stick to recognizing a workplace or folder as their limits, or the files recognized from a git pull.

## The Rise of Parallel Runners in Agentic Workflows

I’ve noticed that the term “parallel” gets bandied about as a marketing term. So you see “parallel coding” or “parallel agents.” To make it clear, if you really want to run tasks in parallel on the same project, you really need to work in separate workplaces from isolated git branches, and then merge the results. Otherwise, tasks working on the same code could clash.

The most effective late trend has been the “parallel runner,” emphasised by [Conductor](https://thenewstack.io/a-hands-on-review-of-conductor-an-ai-parallel-runner-app/) and more recently [Verdent](https://thenewstack.io/first-look-at-verdent-an-autonomous-coding-agent-from-china/) — and it’s also probably what [Google’s Antigravity](https://thenewstack.io/hands-on-with-antigravity-googles-newest-ai-coding-experiment/) is going for. These tools follow the model of isolated branches that allow for tasks to be run and merged in later. Instead of waiting for a task to be done, we just start one and go on to the next one, each task working in its own isolated code workspace. One task after another.

Working solo, this seems like the dream of someone with an attention deficit problem — yet it also closely mirrors how we work with a team. But this is only feasible when you are confident about which type of tasks are simple for an agentic LLM to complete without intervention.

## Conclusion

One of the secrets that the development community knows is that LLMs do work well in constrained cases. No, not for advising humans about edible fungi. And not for creating finished products from thin air.

When we hear bad uses of LLMs that “fail” followed by visions of a bubble bursting, the counter to that is lots of available servers doing what LLMs are actually good at. A mini-crash might actually stop the meaningless chase for “God in the Machine” and benefit the providers of useful tools.

What comes next will be another post, but I suspect much of the future will be refining the tools from this agentic era.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://cdn.thenewstack.io/media/2022/09/2e2ac7a2-cropped-a46bbf33-photo.png)

David has been a London-based professional software developer with Oracle Corp. and British Telecom, and a consultant helping teams work in a more agile fashion. He wrote a book on UI design and has been writing technical articles ever since....

Read more from David Eastman](https://thenewstack.io/author/david-eastman/)