**Open-weight model runner [Ollama](https://ollama.com/) has reintroduced** an integration with [Claude Desktop](https://thenewstack.io/claude-code-desktop-redesign/) that lets users connect Anthropic’s app to models served via Ollama, including those running locally on their machines.

This effectively means Claude users can tap into Ollama’s library, which includes popular models such as [Qwen](https://thenewstack.io/qwen38-27b-local-inference/), [DeepSeek](https://thenewstack.io/deepseek-v4-flash-open-weights/), [Kimi](https://thenewstack.io/kimi-k3-inference-bottleneck/), and [GLM](https://huggingface.co/zai-org/GLM-5.2), while remaining within the Claude Desktop interface — with Ollama serving as the gateway to whichever model handles the request.

![Ollama's model catalog inside Claude Desktop](https://cdn.thenewstack.io/media/2026/08/f301e75e-641249150-c02fd93b-f599-40a9-83c3-d0555c0ac182-1024x615.png)

*Ollama’s model catalog inside Claude Desktop*

## A second shot at Claude Desktop

This isn’t Ollama’s first attempt to bring its model catalog to Anthropic’s tools. Back in January, the company [added support](https://ollama.com/blog/claude) for Anthropic’s Messages API, allowing Claude Code to point to Ollama and use local or cloud-hosted models instead of Claude.

In April, Anthropic [quietly opened a similar opportunity](https://testingcatalog.net/claude-desktop-app-now-supports-third-party-api-proxies/) within the Claude Desktop app, adding a developer setting that let it connect to third-party inference gateways. Ollama [seized on that](https://github.com/ollama/ollama/releases/tag/v0.23.0) with [ollama launch claude-desktop](https://github.com/ollama/ollama/releases/tag/v0.23.2), which configured the desktop app to use Ollama; however, the integration lasted mere days — following a Claude Desktop update, users found that the app’s gateway accepted the connection but rejected non-Anthropic model IDs. And so Ollama [removed the feature](https://github.com/ollama/ollama/releases/tag/v0.23.2), saying Claude Desktop’s third-party integration had become “limited to Anthropic models.”

Fast forward to Aug. 21, and Ollama quietly introduced a new implementation in [v0.33.0](https://github.com/ollama/ollama/releases/tag/v0.33.0) that addresses that mismatch with a [dedicated local proxy](https://github.com/ollama/ollama/blob/main/internal/proxy/claude_desktop.go) for Claude Desktop. In a [blog post](https://ollama.com/blog/claude-desktop) published on Tuesday formally announcing the support, Ollama notes that developers can now configure Claude Desktop to use it as a “third-party gateway provider.” Ollama itself handles the setup: users open the Ollama app, select Claude, and enable the integration, after which Ollama automatically configures Claude Desktop’s third-party gateway. Switching it off restores the user’s previous Claude setup.

![Enabling Claude Desktop](https://cdn.thenewstack.io/media/2026/08/38be7c9e-start-1024x330.png)

*Enabling Claude Desktop*

As part of the update, Ollama has also added the Claude integration directly to its Mac menu, where users can toggle “Use Ollama models” on or off.

![Use Ollama models](https://cdn.thenewstack.io/media/2026/08/878db792-gif1.gif)

*Use Ollama models*

Once enabled, models available through Ollama — whether running locally or via Ollama Cloud — appear in Claude Desktop’s model picker, allowing users to select one without leaving Anthropic’s app.

![Claude Desktop model picker](https://cdn.thenewstack.io/media/2026/08/a10bd1ba-gif2.gif)

*Claude Desktop model picker*

Because Claude Desktop is built around Anthropic’s own model options, Ollama also lets users choose which underlying model should sit behind each slot. In the example below, selecting “Opus 5” routes the request to Kimi K3, while “Sonnet 5” maps to DeepSeek V4 Pro.

![Auto Mode option](https://cdn.thenewstack.io/media/2026/08/64ac4dfe-auto-mode-1024x753.png)

*Auto Mode option*

It is also worth noting that the “Auto mode” option preserves Claude Desktop’s built-in Auto mode, which lets the app decide when it should ask the user for permission before making changes.

The launch prompted a swathe of questions from the community on X, perhaps chief among them: [why use](https://x.com/voidpulse11/status/2092542538221555714?s=20) an alternative model through Claude Desktop rather than use Claude?

The answer, perhaps somewhat unsurprisingly, comes down to choice. The company [points to](https://x.com/ollama/status/2092545484456161371?s=20) cost, speed, and portability, as well as the ability to use models fine-tuned on a developer’s own data. Users can choose between models running locally or on Ollama Cloud, and, of course, they can still lean on Anthropic’s frontier models wherever they like.

Some developers also [wondered](https://x.com/GrowthPact/status/2092534518578360587?s=20) how any of this differed from using Ollama with Claude Code, which was already possible. Claude Code is Anthropic’s terminal-based coding agent, and could already be pointed at Ollama’s Anthropic-compatible API to use local or cloud models. This release brings the same basic idea directly to the Claude Desktop app.

> “The future of AI is open models running everywhere work gets done.”

For now, the new Claude Desktop integration is limited to Ollama’s Mac app, though Ollama suggested in replies on X that Windows support [might be in the works](https://x.com/ollama/status/2092475441009639741?s=20).

## ‘Open models running everywhere work gets done’

Claude Desktop support arrives less than two months after Ollama [raised](https://www.businesswire.com/news/home/20260709429551/en/Ollama-Raises-%2465M-Series-B-Funding-to-Grow-its-Open-source-AI-Platform) a $65 million funding round. In a statement issued at the time of the funding announcement in July, Ollama co-founder and CEO [Jeffrey Morgan](https://www.linkedin.com/in/jmorganca/) described a future in which open models are available wherever developers choose to work.

“Open models should be easy to run, easy to build with, and available wherever people need them — on your own machine, in the cloud, or both,” Morgan said. “Ollama started as an open-source project, and has since grown into a community of millions of developers. Everything we do next is in service of that community and their best work. The future of AI is open models running everywhere work gets done — and Ollama is here to power this shift.”

The update also builds on Ollama’s [broader push](https://thenewstack.io/connect-to-a-local-ollama-ai-instance-from-within-your-lan/) to make local models easier to use [within existing developer tools](https://thenewstack.io/how-to-integrate-vs-code-with-ollama-for-local-ai-assistance/). At the same time, recent work, such as [native Apple MLX](https://thenewstack.io/ollama-taps-apples-mlx/) support, has focused on improving local inference on Macs.

Support for Claude Desktop is the latest expression of that strategy: letting developers keep the apps they already use while Ollama supplies the underlying model.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://thenewstack.io/wp-content/uploads/2026/02/bd93adde-cropped-9c2ecfc5-a-600x600.jpg)

Paul is an experienced technology journalist covering some of the biggest stories from Europe and beyond, most recently at TechCrunch where he covered startups, enterprise, Big Tech, infrastructure, open source, AI, regulation, and more. Based in London, these days Paul...

Read more from Paul Sawers](https://thenewstack.io/author/paul-sawers/)