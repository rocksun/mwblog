# Playing D&D With AI: The Agentic AI Developer’s Achilles Heel
![Featued image for: Playing D&D With AI: The Agentic AI Developer’s Achilles Heel](https://cdn.thenewstack.io/media/2025/06/35635bdd-dragons12-1024x576.jpg)
To make good agentic AI apps, developers need to get good at what they’re terrible at: documentation. That’s because Agentic AI apps use a lot of tools, and to understand when and why to use those tools, the AIs need good documentation.

I’ve been coding [Model Context Protocol (MCP)](https://thenewstack.io/model-context-protocol-a-primer-for-the-developers/) servers to help me play solo Dungeons & Dragons with [Claude](https://thenewstack.io/claude-opus-4-with-claude-code-a-developer-walkthrough/), as I covered in [my previous article on this topic](https://thenewstack.io/if-ai-can-play-dungeons-dragons-it-can-run-your-erp/). Playing D&D with just the AI robots is fun and delightful. Adding in [agentic AI workflows](https://thenewstack.io/the-architects-guide-to-understanding-agentic-ai/) improves it a lot: It adds randomness to the AIs that can break it out of predictable plots. As I’ve made these little MCP tools, I find that I spend most of my time writing the descriptions of what each tool does and refining those descriptions as I test out the tools. That’s why I think documentation is more important than ever when it comes to agentic AI, whether it’s having fun exploring creepy forests or reconciling regional purchasing orders.

## Documentation Is Important
When you look at examples of MCP code, you see that the primary way of telling the AI what the tool does is with natural language descriptions of the tool. Each tool has a description and each of the tool’s parameters has a description as well. So, if you’re writing a bunch of MCP tools, the way you describe them to the robot becomes important.

These MCP tool descriptions are not typical API descriptions. Typical API descriptions document *what *something does. The really good ones also describe *how* the code does it, including error handling and behavior.

That’s certainly important for agentic AI documentation, but you also want to describe when the AI should use a tool, why it would use it and how to apply the tool’s results. You want to have an opinion of what the tool is good for. And once you load in examples, your docs end up almost looking like a story.

## Oracles
A good example of this is writing an MCP tool to serve as an “oracle” in solo roleplaying. In solo roleplaying, as the name implies, you’re playing by yourself, making up a story as you go along. In these cases, you often want random ideas to drive what happens in your story that help you come up with unexpected twists and turns. An oracle is a way of generating these random ideas when you’re solo roleplaying. For example, you might have an oracle that gives you ideas for how something smells: fresh, like bacon, three-day-old tofu, apples and so forth. There could be a list of 20 or 100 of these. When your character has walked into a room and sees a pile of something, to find out what the pile was, you would roll some dice and use one of the randomly selected entries from this oracle. You roll 54: “old shoes.” And, thus, in your solo roleplaying journal, you write “Sven the gnome walked into a poorly lit room behind the stables and spotted a pile of something. Using his considerable olfactory sense, he smelled something unmistakable: goblin shoes.”

In my favorite solo roleplaying system, [the Plot Unfolding Machine](https://jeansenvaars.itch.io/plot-unfolding-machine), there are well over 40 oracles for things from smells, non-player character (NPC) intentions, conversation topics, how any given object looks and so forth.

When I play solo D&D with Claude, it does a decent job of responding to my gnome with what happens next in the story. But, by design, it’s very predictable in reply. That’s after all, what generative AI does: It tells you the next likely words (sure, tokens) that follow what you just typed. In this case, the most predictable thing that’d happen is that some monster is hiding under that pile of shoes, or that it’s some kind of monster that’s mimicking a pile of shoes.

Using the result from oracle can break it out of this predictability. Now, normally, I’d roll dice on an oracle I have and then type in the result to Claude. But, with an MCP tool, I can create a little tool *and* have Claude decide when to call the oracle. I no longer have to manage looking up things like “old shoes” in an oracle and pass it to Claude.

The result, as we’ll see, is that I can stay “in game” more and not decide when an oracle needs to be called.

## The Code Is Simple
Let’s look at an example of Claude desktop doing reasoning to use a tool and then using the tool. First, we’ll look at the end result, and then at the code. This will show why the documentation for the tool is so valuable.

Below, I ask Claude to start playing D&D and tell it a little bit about the situation, a peddler walking down a road. In the UI, you can see it calling the EasyChatDM tools, three of them:

What you see is Claude doing a simple agentic AI workflow:

- It attempts to look up the existing adventure by reading the DM Journal. This is the first time we’ve played, so there is no DM Journal, so Claude starts a new adventure.
- There’s a new NPC, so Claude calls the NPC Motivation tool (“EasyChatDM_NPC_Motivations”). I have that call open so you can see the basic input and output. I’ll comment on that questionContext later.
- Finally, Claude calls a tool to get guidance input on how the peddler looks. You can’t see it here, but the response was “rectangular.” Kind of odd, but that’s the point of an oracle: What fun thing will happen with such a weird description of a person?
This is a very simple workflow, but it exhibits the distinguishing features of “agentic.”

Claude is acting autonomously. It has decided to call each of these tools, putting together a plan and responding to the results. This results in Claude coming up with the peddler’s next move. Depending on how you’re playing, this process can get even more detailed. For more complex things like creating an adventure, I’ve seen it call 10 or more tools in one agentic chain.

The tools I’m using here are simple — the NPC Motivation oracle just picks a random line of text from a file. But, it’s easy to see how you could do more complex things behind the tools like retrieving custom records, searching for inventory, even doing documents verification. The tools can do anything you want, it’s just code.

Instead of just a line of code, you could also return much more structured output, like JSON. You could kick off a chain of other events outside of Claude, like a batch job for further analysis. But, for my case, just knowing that the peddler wants to pump up perceptions about their intellect is enough for me.

## Spring AI Makes the Code Quick and Easy
As I said in my previous post, the actual oracle code is pretty boring. I’m using [Spring AI’s MCP libraries](https://docs.spring.io/spring-ai/reference/api/mcp/mcp-overview.html), so I don’t really have to do much of the scaffolding work to make an MCP server. And when you finally get to the code and scrape off all the error handling and logging, all the code does is randomly select one of 303 lines from a text file.

What I’ve found is that the documentation for the NPC motivation is what’s important. The description of what the tool does and when to use it is an interesting work:

That description of the tool works well in my playing: It gets called pretty regularly and I like the way it’s incorporated into the ongoing story. Now, I could have had no documentation and just called the MCP tool “NPC Motivation.” The AI can probably figure out what to do with that. I could also just have docs that say “Descriptions of the motivation of an NPC.” Both of these are the type of documentation I usually encounter: either nothing or a not-too-clever rewording of the method name.

Those two methods of documenting don’t give the AI much guidance about when to call it, what to do with it and when *not* to call it. The documentation is your chance to give direction and style of play to the AI.

The NPC Motivation one is relatively simple. Often, though, you need a lot of imagination and nuance to interpret the result from an oracle. For example, another type of oracle tells you the degree to which something happens. You might ask, “Is there a belligerent goblin hiding in that pile of shoes? A simple yes/no oracle would answer … yes or no. But, there are also more nuanced oracles that will return a gradient of answers like “Yes, but …” or “No, not yet …”

In this case, I like to coach the AI with some examples of how to interpret the results, as you can see in the documentation for the [EasyChatDM_Subjective_Oracle](https://github.com/cote/EasyChatDM/blob/main/src/main/java/io/cote/EasyChatDM/OracleTools.java):

## A New Skill for Developers
What I’m doing in the EasyChatDM_Subjective_Oracle documentation, and for[ other tools](https://github.com/cote/EasyChatDM/tree/main), is coaching the AI on how to think about and use these tools. Giving examples is also, as ever, important. That’s why documentation is important and, I think, documenting your AI tools in a more detailed, humanistic way is very important.

Of course, we know the reality of most code documentation: It tells you nothing, because the [developers didn’t write](https://thenewstack.io/developers-put-ai-bots-to-the-test-of-writing-code/) it. Most people would say documentation is important, but based on what we see, it’s low on the priority list.

What I’ve found is that the better the docs, the better the D&D session with the robots. And, I’m pretty sure that’ll be the case for all those thrilling enterprise AI use cases too.

Better get good at writing docs.

[
YOUTUBE.COM/THENEWSTACK
Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.
](https://youtube.com/thenewstack?sub_confirmation=1)