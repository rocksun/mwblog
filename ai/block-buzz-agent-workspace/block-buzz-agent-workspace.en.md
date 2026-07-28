Block on Tuesday launched [Buzz](https://buzz.xyz/), a free, open-source workspace meant to give people and AI agents a Slack-like service for collaboration.

The company built Buzz on Nostr, the decentralized messaging protocol best known as a censorship-resistant alternative to Twitter and backed for years by Block founder Jack Dorsey. Using Nostr, each agent gets its own cryptographic identity that is connected to its human owner.

At first, Buzz looks a lot like Slack or Discord, with channels, threads, direct messages, voice, media sharing, and code repositories. But the difference here is that it treats agents as full participants in these conversations. It can work with any model and any popular agent harness, so teams can plug in Claude Code, Codex, [goose](https://thenewstack.io/block-goose-agentic-foundation/) (which came out of Block), or bring their own.

The code for Buzz has actually been on GitHub (under an Apache 2.0 license) since earlier this year, but recently, Block decided to host its own Nostr relay for Buzz, and with this launch, public signups are now open.

![](https://cdn.thenewstack.io/media/2026/07/67cb9b69-block-buzz-ai-agents-app-macos-screenshot-2-1024x740.png)

Credit: Block.

As Bradley Axen, Block’s head of AI capabilities, tells *The New Stack*, much of the actual work with coding agents happens in private and then disappears.

> “Everyone misses that second conversation, and at least for building software, that’s where the conversation is really interesting. That’s where you make all the technical decisions.”   
> —Bradley Axen, Head of AI Capabilities, Block.

“Right now, you’ll make a post, you’ll go work by yourself for an hour with an agent, and then you’ll maybe copy and paste something the agent said back in as if it’s from you,” Axen says. “Everyone misses that second conversation, and at least for building software, that’s where the conversation is really interesting. That’s where you make all the technical decisions.”

## An identity of its own

On Nostr, every participant is, at its core, a public-private keypair. Buzz gives an agent its own keypair and treats it as an independent actor, but what’s important here is that it then also adds a second signature that ties it back to a person.

“It starts like a human. It’s just got its own public key, and it signs events, and then there’s one extra message that we publish on the relay,” Axen says. “We’ve got this cryptographic paper trail that neither of us could have done alone that says, okay, this is my agent, and anyone else can review and confirm that that’s true.”

[](https://cdn.thenewstack.io/media/2026/07/7857e254-block-buzz-ai-agents-product-demo-video-4k.mp4)

Credit: Block.

That paper trail lets a workspace enforce rules, such as allowing only agents owned by a member into a private channel. Block has proposed the identity scheme to Nostr as an upstream extension, though it hasn’t been accepted just yet.

Agents connect through the [Agent Client Protocol](https://zed.dev/acp) (ACP), the open standard Zed introduced last year for wiring coding agents into different tools. Axen sits on the steering committee of the Linux Foundation’s [Agentic AI Foundation](https://thenewstack.io/agentic-ai-foundation-launch/) and says the group is looking at bringing ACP into its fold.

## ’A relay you own’

Buzz needs a Nostr relay to work and any team can stand up its own and have full control of its infrastructure with nothing routing through Block. Axen’s comparison is a Discord server, except that no single company owns it. Still, Block spent the final weeks before launch building a hosted option, betting that most teams won’t want to deal with the added complexity of running their own relay.

“I’m really excited that you can, but I think the majority of people just want an off-the-shelf solution,” Axen says.

Block’s hosted relays are free at launch, which Axen calls a beta. The company hasn’t set usage limits yet. Axen says a 10-person open-source project is cheap to host, while a replacement for “enterprise-grade Slack” would eventually need a different arrangement.

## From goose to BuilderBot

It’s worth noting that Buzz isn’t Block’s first agent project. The company, after all, open-sourced goose, its agent framework, in January 2025. That project now has more than 50,000 GitHub stars.  
In June, Block also detailed [BuilderBot](https://thenewstack.io/how-block-manages-its-fleet-of-ai-coding-agents-from-slack/), an internal system engineers summon by tagging it in Slack. The company says it runs more than 200,000 operations a day, merges about 1,500 pull requests a week, and accounts for about 15 percent of Block’s production code changes.

## Living alongside Slack

Block isn’t alone in wiring agents into the tools teams already use. Atlassian has added agents to Jira, and companies across the industry now run coding agents inside Slack. Block still uses Slack internally, and Axen argues that the two can be used in parallel.

“Can it be a full replacement for Slack? We’ll have to see over time, because Slack also encodes a lot of business workflows,” he says. “We’ve got a decade of history in Slack.”

For now, Buzz is still in its early days. The repository, public since earlier this year, has drawn just over 100 stars, a small fraction of goose’s.

The launch also comes as Block reshapes itself around AI. In February, the company cut more than 40 percent of its staff, from more than 10,000 employees to just under 6,000, with Dorsey citing AI as enabling what he called “a new way of working.”

Buzz is the collaboration layer Block is building for that smaller, more agent-heavy company.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://thenewstack.io/wp-content/uploads/2025/03/15a7eb12-cropped-4e88ac40-frederic-profile-2-600x600.jpg)

Before joining The New Stack as its senior editor for AI, Frederic was the enterprise editor at TechCrunch, where he covered everything from the rise of the cloud and the earliest days of Kubernetes to the advent of quantum computing....

Read more from Frederic Lardinois](https://thenewstack.io/author/frederic-lardinois/)