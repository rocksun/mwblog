Warp, the popular Rust-based agentic development environment, has released its client as open source.

Warp began in 2022 as, believe it or not, [a terminal program](https://thenewstack.io/a-review-of-warp-another-rust-based-terminal/) for Macs. In addition, you could use [Warp](https://www.warp.dev/) as an IDE. From there, it [evolved](https://thenewstack.io/warp-goes-agentic-a-developer-walk-through-of-warp-2-0/) into what the company calls an agentic development environment (ADE) and became available on Linux and Windows as well. That’s a lot of change in a short time, and now the Warp client is going [open source](https://www.warp.dev/blog/warp-is-now-open-source) under the AGPL.

In a blog post announcing the shift on Tuesday, CEO and founder [Zach Lloyd](https://www.linkedin.com/in/zachlloyd/) writes that “the Warp client is now open source, and the community can participate in building it using an agent-first workflow managed by [Oz](https://www.warp.dev/oz), our cloud agent orchestration platform.”

OpenAI is the “founding sponsor of the new, open‑source Warp repository,” and the agent workflows that power it are built on GPT models. Warp describes this as “our vision of how software will be built in the future,” with humans supervising “a fleet of agents” that handle most of the implementation work.

The company argues that the long‑standing bottleneck in development is no longer typing code, but all the “human-in-the-loop activities around the code: speccing the product and verifying behavior.”

Besides, agents can already “handle the implementation heavy lifting really well,” so why not enable contributors to focus on higher‑level design and verification? Their argument makes sense.

And, what does that have to do with open source? Warp’s leadership explained its decision to go open source as a mix of practical product concerns and a bet on where AI‑assisted development is headed. The company says it believes it “can ship a better Warp, more quickly, if we open source and work with our community to help supervise a fleet of agents.”

Well, that has certainly always been a big reason why countless other companies have embraced open source. Usually, though, companies start with an open-source project and then turn it into a product or service. We’ll see if this flip-around of the usual open-source-to-product path works out for Warp.

A second motivation is to give developers more say over the shape of “agentic development.” Warp states that “there isn’t a full-featured open agentic development environment on the market.”

The company presents the open‑sourced client as an alternative to closed tools from larger incumbents. The company is also pitching it as a starting point for others who want to build their own tools on top of Warp and Oz.

As part of the shift, Warp says it is moving “from a closed product development process to an open one.” Public GitHub issues will now be the “source of truth” for feature tracking, with the company promising to publish its ADE roadmap and hold technical and product discussions in the open.

For now, the [Warp open‑source repo](https://github.com/warpdotdev/warp) is tightly coupled to Warp’s commercial Oz orchestration platform. The company emphasizes that “Warp’s new open-source agent workflows are powered by OpenAI models, with OpenAI supporting the next generation of collaborative software development.”

In the blog post, OpenAI engineering lead [Thibault Sottiaux](https://www.linkedin.com/in/thibault-sottiaux-27195366/) adds, “Open source has long been central to how developers learn, build, and push the field forward. We’re excited to support experiments that explore how AI can help maintainers and contributors collaborate more effectively at scale.” That said, Warp notes that contributors are “free to use other coding agents as well,” but says its preference is for Oz, which it claims has “the correct skills and verification loops built-in.”

There’s more than a licensing change happening here.  The company is rolling out several product updates, which it describes as making the tool “more open and customizable.” Those include:

* Support for “a much wider range of open source models,” including Kimi, MiniMax, and Qwen, plus an “auto (open)” routed option that picks what Warp deems the best open model for a given task.
* A more flexible UI configuration so users can run Warp as “just a terminal,” add lightweight features such as diff view and file tree, or turn it into a “full-fledged ADE with built-in agents.”
* A “long-overdue” settings file designed to give both users and agents programmatic control over configuration and easier portability across machines.

What all this means, Warp hopes, is that by improving the program and opening the client, it will help the company “build a successful business” in a market filled with “highly funded, closed-source competitors.”

> Without the ability to out-spend rivals, the company is making a slight gamble on its ability to innovate.

Without the ability to out-spend rivals, the company is making a slight gamble on its ability to innovate. The company’s [blog post](https://www.warp.dev/blog/warp-is-now-open-source) states that “Warp is a smart way for us to accelerate product development.

“We need to build our business by offering the best possible product to the most excited community,” the blog post reads, acknowledging the challenge — and inherent risk — ahead.

Warp also presents the move as the fulfillment of an original plan from its early “Show HN” launch, saying “the plan was always to open source the client,” but that internal debates about the trade‑offs have continued “every year.” The rise of AI agents, Lloyd writes, finally shifted the calculus: “We could just keep going with our current model, privately guessing at the roadmap and scaling more and more agents to build internally, but that feels like a missed opportunity.”

Will this prove to be Warp’s golden chance? We’ll find out.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://cdn.thenewstack.io/media/2023/03/cee63948-cropped-8a0b5c52-steven-vaughan-nichols.jpg)

Steven J. Vaughan-Nichols, aka sjvn, has been writing about technology and the business of technology since CP/M-80 was the cutting-edge PC operating system, 300bps was a fast internet connection, WordStar was the state-of-the-art word processor, and we liked it.

Read more from Steven J. Vaughan-Nichols](https://thenewstack.io/author/sjvn/)