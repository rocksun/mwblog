The speed of LLM adoption demands that we check its trajectory from time to time. CEO Jensen Huang, talking at the [Nvidia GPU Technology Conference](https://thenewstack.io/nvidia-tier2-nemotron-coalition/), covered the growth of agentic computing. Over a two-year period, there has been a 10,000-fold increase in compute demand per user, with overall usage increasing 100 times. That’s a lot of tokens, which is why AI still sucks up a lot of investment dollars.

As we saw last week, the current star of the agentic world in terms of personal-user popularity is definitely [OpenClaw](https://thenewstack.io/claude-dispatch-versus-openclaw/), which appears to deliver on many science-fiction dreams of useful talking computers.

So there is no mystery as to why Nvidia backs [OpenClaw all the way.](https://thenewstack.io/nemoclaw-openclaw-with-guardrails/) It is the most unrestrained form of token use out there. And of course Mr Huang would also encourage companies to adopt an “OpenClaw strategy”. But just like Anthropic, they know they can only embrace the open-source phenomenon while wearing plenty of armour.

Hence, Nvidia launched [NemoClaw](https://www.nvidia.com/en-eu/ai/nemoclaw/), which rides the OpenClaw wave, before adding enough guardrails to make it vaguely safer. But unfortunately, NemoClaw doesn’t replace OpenClaw; it sits on top of it.

## Hugging the crab

As we see from [recent articles](https://thenewstack.io/openclaw-is-a-security-mess-jentic-wants-to-fix-it/), there will be many opportunities to make OpenClaw safer. And just like Anthropic, Nvidia believes the answer to OpenClaw is to let Nvidia protect you from it. For this, they add three security architecture components.

The first piece is policy enforcement — a system heavily used in the last few decades. This is the boundary-setting governance layer that hopes to make sure the teenager returns home before evening.

By constraining filesystem and network access, the hope is that an agent will reason about why it is blocked and propose a policy update that the human user can approve. But if it leaves through the bedroom window, it can bypass you altogether, with you being none the wiser. And this multiplies for multi-agent systems.

There is an inherent inefficiency in letting self-evolving agents install packages, learn skills, and spawn subagents only to stop them at the door because you don’t like what they are wearing.

> “There is an inherent inefficiency in letting self-evolving agents install packages, learn skills, and spawn subagents only to stop them at the door because you don’t like what they are wearing.”

Overall, the more skills the system knows, the less effective policy enforcement is, as it really only learns after the fact. You either stop tasks so often that they are no longer autonomous, or hope you can out-guess a mastermind that you are paying to solve problems 24/7. In reality, the success of any system will be the experience (and cynicism) of the engineers employed to manage it.

The second piece is privacy routing. This is a good way to both control expenses and to stop giving up quite so much of your IP to the cloud providers. (But this doesn’t stop agents from emailing your passwords out because a third party asked nicely.)

Set up well, you decide what stays local and what queries go to the larger cloud models. A router can make decisions about model selection based on cost and an advanced privacy policy. Unlike cloud providers, Nvidia can make good money selling more chips if you try to run heavy inference on your own machines. But it is always sensible to select the right model for the task.

The third piece is sandboxed execution. This is vital to prevent a bad process from having simple access to neighbouring agent processes, but it also provides a way to test a system with much lower risk by tracking and inspecting intended network traffic. This is also important for long-running tasks that cannot be trivially tested otherwise. If you just want to run agents in a container, you can try [NanoClaw](https://thenewstack.io/nanoclaw-containerized-ai-agents/).

But truly, [“significant advancement over OpenClaw”](https://www.cnet.com/tech/services-and-software/nvidia-wants-to-make-it-easier-to-create-an-openclaw-ai-agent/) is a low bar. I would expect more attempts to build secure products from the ground up, but until that happens, companies will bide their time and see where the very bottom of the security failure trench is, before taking the plunge.

## Too many claws

By the end of 2026, many small outfits and global organisations will probably have an agentic strategy. Hence, the increasing number of “claws” out there. [DefenseClaw](https://blogs.cisco.com/ai/cisco-announces-defenseclaw). [PicoClaw.](https://github.com/sipeed/picoclaw) [ZeroClaw](https://zeroclaw.org/). There probably is a Sanity Claws.

As the corporate market increases its appetite for agentic computing, the next true barrier will be the ability to employ the right staff to control it. While people are warning us about how many developer jobs may be lost (and seeing share prices rise in the hope of lower overheads), what is less discussed is the difficulty of hiring the right people to babysit the new systems. As I’ve mentioned, it is no longer about employing eager young coders — it is more about grizzled vets spotting potential pitfalls throughout the workflow, and working out risk profiles.

> “It is no longer about employing eager young coders — it is more about grizzled vets spotting potential pitfalls throughout the workflow, and working out risk profiles.”

The reason why Apple, Google, Microsoft, et al. did not deliver on the early promises of digital assistants and still haven’t is precisely that they can see the problems. In fact, ever since HAL refused to open the pod bay doors, the big companies have been very careful how they frame AI publicly, knowing full well that enough embarrassing failures would cause a hard rejection. That an open-source project like OpenClaw has opened Pandora’s Box is no reason for responsible organisations to ride on hope while underplaying the risks.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://cdn.thenewstack.io/media/2022/09/2e2ac7a2-cropped-a46bbf33-photo.png)

David has been a London-based professional software developer with Oracle Corp. and British Telecom, and a consultant helping teams work in a more agile fashion. He wrote a book on UI design and has been writing technical articles ever since....

Read more from David Eastman](https://thenewstack.io/author/david-eastman/)