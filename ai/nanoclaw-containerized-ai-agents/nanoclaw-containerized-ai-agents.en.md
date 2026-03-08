On the one hand, I feel a bit conflicted pointing out the recognised [security issues with OpenClaw](https://www.theregister.com/2026/02/02/openclaw_security_issues/), even as serious AI thought leaders are naming their agents “Arnold” and shouting orders at them. I feel duty-bound to take their enthusiasm seriously, while also stressing that this whole area remains problematic.

Enter [NanoClaw](https://nanoclaw.dev/). And it’s more than just a [very small claw](https://thenewstack.io/nanoclaw-minimalist-ai-agents/).

Firstly, NanoClaw can isolate each agent in its own container. So the agentic loop starts with no knowledge of other agents, and only knows about the resources you tell it about.

The other intriguing thing is that the app isn’t a large configuration file talking to a monolith; it is just the code you need (and the appropriate Claude skills) — with Claude hacking itself as needed. Given that code is “cheap” now, and Claude editing is reliable, this does make sense. And it does keep the code size down.

### WhatsApp? No thanks.

My first question was… how does a bot get access to WhatsApp? This is the preferred contact choice of most OpenClaw users (and NanoClaw). The problem here is that unless you have a business account, you surely don’t own enough stake in the platform to host an arbitrary new user. On closer inspection, it appears that the WhatsApp connection relies on a module called [Baileys](https://baileys.wiki/docs/intro/) that scans WhatsApp Web’s WebSocket-based data, which Meta strongly discourages. In fact, accounts using unauthorised methods to connect to WhatsApp are actively monitored and restricted.

I’m hardly going to encourage using such a method, but fortunately, we don’t have to. I do pay for a Slack workspace, and while connecting to Slack is a little painful, it is at least fully accounted for.

### Installing

I have Claude installed, of course, connected to a “Pro” account. With the [instructions](https://github.com/qwibitai/nanoclaw), I do the usual thing:

```

git clone https://github.com/qwibitai/nanoclaw.git
```

Then I ran Claude within the new directory with `/setup`:

![](https://cdn.thenewstack.io/media/2026/03/1d768e10-image-1024x227.png)

I have Docker Desktop installed, as this part requires:

![](https://cdn.thenewstack.io/media/2026/03/441984c7-image-1-1024x167.png)

On a Mac, you will see the familiar Docker icon in the Menu Bar if you didn’t start it yourself.

Then we move to how you are connecting to Claude:

![](https://cdn.thenewstack.io/media/2026/03/6b1ce776-image-2-1024x366.png)

Usually, I have to remember to turn the API key off because it’s more expensive than a subscription. This is the first time I’ve seen the two options mentioned side by side—a good sign.

Then we get to the contentious bit:

![](https://cdn.thenewstack.io/media/2026/03/8e4f04e3-image-3.png)

As I’ve indicated, I don’t think WhatsApp is appropriate, so I’ll be using Slack.

Then we were given the great Slack sidequest:

![](https://cdn.thenewstack.io/media/2026/03/96178f0c-image-5-1024x554.png)

I now have to find two tokens, but not with my sword and trusty shield, but with the Slack API. I only recommend this campaign for an experienced adventurer. Onwards.

### Generating the tokens in Slack

Fortunately, there are some good instructions on the [Slack skill](https://nanoclaw.dev/skills/slack), and Claude is patient. First, we need to generate the tokens and scopes.

On Slack, I found the appropriate dialog:

![](https://cdn.thenewstack.io/media/2026/03/9f0bb9db-image-6-1024x510.png)

We need to turn on Socket Mode:

![](https://cdn.thenewstack.io/media/2026/03/a629702a-image-7-1024x379.png)

Then we need to subscribe to a set of bot events:

![](https://cdn.thenewstack.io/media/2026/03/98b1369f-image-8-956x1024.png)

And add scopes for OAuth – these limit what the NanoClaw App can do in the account:

![](https://cdn.thenewstack.io/media/2026/03/ad92906a-image-9-947x1024.png)

And finally, you get to install your new app and fetch the final ~~dungeon key~~ token:

![](https://cdn.thenewstack.io/media/2026/03/61d8d647-image-10-892x1024.png)

I have slain the dragon / found the treasure / defeated the Rocketeer. Well, not quite.

Claude crashed. But I quickly got back to where I was, and Claude appears to fix the errant Slack script, and accept my two tokens for its `.env` file:

![](https://cdn.thenewstack.io/media/2026/03/d9d4b3a1-image-11-1024x221.png)

Then it was a case of introducing NanoClaw into my Slack channel.

I suspected we were done with Slack itself, but we needed to give it access to my server folders. Remember, this is what we did with [Claude Cowork](https://thenewstack.io/how-claude-cowork-helps-developers-spread-the-ai-knowledge/) to give it real power:

![](https://cdn.thenewstack.io/media/2026/03/6a99c032-image-13-1024x399.png)

A nicer way to select the folders would be cool, but I added the folders I was happy for NanoClaw to see:

![](https://cdn.thenewstack.io/media/2026/03/4295839c-image-14-1024x122.png)

And then I was able to communicate with NanoClaw on my Slack channel, after getting the correct Claude auth token:

![](https://cdn.thenewstack.io/media/2026/03/afcaebd0-image-15-1024x378.png)

My initial attempt to confirm that NanoClaw could see my folders on my Mac failed:

![](https://cdn.thenewstack.io/media/2026/03/af544214-image-16-1024x162.png)

This is both good and bad. It proved that the agent is sitting in a container and **not part of** a single app. And of course, I asked Claude to fix itself. I had been tailing the log, so I could relay all the problems back to Claude, which eventually mapped the folders in a way that the NanoClaw agent could understand:

![](https://cdn.thenewstack.io/media/2026/03/803bac9b-image-17-1024x141.png)

Note how it refers to “the agent” as a separate entity. So I had a back-and-forth between the NanoClaw agent and Claude. I’m still very much the engineer here – but the separation of control is fine. The errors were the ones we all make, not understanding what Linux wants. No one understands what Linux wants.

Eventually, it fixed its internal database and restarted what it needed to for the container. And with the new mapping, I could see my Documents folder:

![](https://cdn.thenewstack.io/media/2026/03/b8585ee1-image-18-1024x155.png)

To check, I added a new file to check it really was mapped live to the directory. Eventually, it did reflect that the file was there.

> “I like the fact that Claude thought of the agent sitting in the container as quite separate from itself, and overall this is certainly a much more sensible and secure setup if you really want to be a ‘power user’ who really just needs a secretary to yell at.”

Now this isn’t running on a Mac Mini under my cupboard, but on my laptop. So I won’t be asking for a research document based on a report in my inbox at 2 a.m. while out for a jog, but if I were into that sort of thing, NanoClaw can clearly provide this fairly safely.

While I did need to play engineer to get everything working, in reality, I was telling Claude my problems, and Claude fixed them. For that, I got a direct connection from my mobile Slack app to my server. I like the fact that Claude thought of the agent sitting in the container as quite separate from itself, and overall, this is certainly a much more sensible and secure setup if you really want to be a “power user” who really needs a secretary to yell at.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://cdn.thenewstack.io/media/2022/09/2e2ac7a2-cropped-a46bbf33-photo.png)

David has been a London-based professional software developer with Oracle Corp. and British Telecom, and a consultant helping teams work in a more agile fashion. He wrote a book on UI design and has been writing technical articles ever since....

Read more from David Eastman](https://thenewstack.io/author/david-eastman/)