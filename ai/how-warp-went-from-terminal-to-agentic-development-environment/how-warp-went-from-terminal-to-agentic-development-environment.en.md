For this week’s edition of The New Stack Agents, we talked to [Zach Lloyd](https://www.linkedin.com/in/zachlloyd/), the founder and CEO of terminal/agentic development environment [Warp](https://www.warp.dev/). Not entirely by coincidence, we talked to Lloyd on the day he launched [Warp Code](https://www.warp.dev/blog/introducing-warp-code-prompt-to-prod), the latest iteration of Warp’s journey from [reinventing the terminal](https://thenewstack.io/a-review-of-warp-another-rust-based-terminal/) when it launched in 2022 to becoming a [full agentic environment for developers](https://thenewstack.io/warp-goes-agentic-a-developer-walk-through-of-warp-2-0/) to code with agents, debug their code, and push it into production.

VIDEO

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

## Warp Code

With Warp Code, the Rust-based Warp desktop app is introducing a slew of new features, including a built-in file editor, tools for reviewing the code written by the agent, and WARP.md files, Warp’s version of AGENTS.md or CLAUDE.md for steering the agent with project rules and other instructions.

The main goal here, Lloyd told us, is to give developers the tools to not just interact with the agent but also review the code so that they can be confident that when they send it to be reviewed, it’s correct.

“How people use agents — and what the number one complaint is — is that you have agents writing a bunch of code that they don’t understand, that has subtle bugs that they’re scared to push up for code review, that they’re scared to introduce security holes,” Lloyd said. “And so what you actually need to make this workflow more effective right now are tools for comprehending and guiding and making sure you, as the engineer who’s working with the agent, can stand behind the code that you’re asking someone else on your team to review.”

The reason for this is that the tools aren’t there yet. Because the models aren’t smart enough yet to be fully trusted, developers have to work very closely with the agent and provide very precise instructions. With its new code review capabilities, that’s what Warp is now trying to add to its tool.

“What you need in the tools today is something that shows you the agent’s work, the explanation the agent has at every single step that it goes — and to me that, that is a solved problem, it almost looks like code review,” Lloyd said. “It’s just you want a human code reviewing the agent as it’s writing the code, so you don’t get into this position where you, as the developer are like: What the hell did it do?”

That means working with code more directly in Warp, including editing files and a file tree to select them, but Lloyd stressed that Warp doesn’t want to be an editor. Instead, this is meant to make it easier for developers to see the structure of their projects in Warp and also make quick edits and see the agent-generated diffs without having to switch context.

One other interesting new feature Warp is adding is the ability to steer the agent while it’s running. “You don’t have to kill the agent to redirect it. We call it persistent input. That’s a nice feature that lets you steer it as it goes,” said Lloyd.

The way Warp does this is by having the agent keep an internal task list and when the user interjects, the agent stops working on that list, adjusts it in light of the new instructions, and goes back to work.

## From Terminal to Agents

How did Warp get to this stage? The early idea behind it was to finally bring the terminal, which was always very powerful but also hard to use — and unnecessarily so, according to Lloyd.

“A lot of the best developers I ever worked with just knew how to do stuff with it that I couldn’t do,” he said. “Actually, I was kind of lazy. I never like learned how to fully master it. I was: Why is this power locked in such an old, antiquated interface, you know?”

So he set out to figure out how to make the workflows in the terminal easier, including basics like copy-paste and using the mouse more effectively. “It was meant to be something very different,” he said.

Pre-AI, the team was also focused on adding more collaboration features to the terminal, which may not be a surprise given Lloyd’s background on the Google Docs team.

Then, when AI came along, even before ChatGPT, the team started adding some basic AI features to the terminal to allow users to describe what they wanted to do and have Warp translate that into commands. Over time, that morphed into adding more and more agentic features, culminating with today’s Warp Code launch.

“We don’t even really even call it a terminal anymore,” Lloyd said. “It’s really a platform for developing with agents that happens to have a form factor that looks a lot like a terminal — and you can still use it as a terminal, but now it’s an agentic development environment. To call it a terminal creates a set of expectations around what it is and what it does, which don’t match what the product actually is.”

## Code Country

VIDEO

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Our conversation, which you can find on YouTube and by subscribing to our podcast, also touched upon more details about the launch and how the Warp team thinks about interfacing with agents, among other things. But just as importantly, we also talked about why Lloyd donned a cowboy hat and delivered the announcement of the new Warp Code from the back of a horse in a Western Town.

“The theme of the launch is ‘Code on Warp’, which is ‘cow’ – C, O, W – and we were talking about what it would be like, what would be funny, honestly, or what would be memorable? Because when you look at every other launch for one of our competitors — and we’ve done this, too — it’s usually some tech person in an office, you know, sitting on a set of stairs or a nice chair, explaining what the new features are. And we’re: I don’t know. I thought it’d be kind of fun to do it, to just do it on a horse. And so that was what people probably noticed first of all. There’s so many releases in our space, we’re like: what would people notice and think is memorable. And so then we’re like, you know, why not also make a Western ad?”

So the team rented out a Western town film set, hired extras, and got to work. I’ll take that over the usual launch video any day.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://thenewstack.io/wp-content/uploads/2025/03/15a7eb12-cropped-4e88ac40-frederic-profile-2-600x600.jpg)

Before joining The New Stack as its senior editor for AI, Frederic was the enterprise editor at TechCrunch, where he covered everything from the rise of the cloud and the earliest days of Kubernetes to the advent of quantum computing....

Read more from Frederic Lardinois](https://thenewstack.io/author/frederic-lardinois/)