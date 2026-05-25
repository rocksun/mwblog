OpenClaw made the always-on agent feel personal by making it live somewhere you could point at — a Mac mini on a shelf, drawing seven watts, running while you sleep. Peter Steinberger’s open-source project surpassed 300,000 GitHub stars by April and became one of the fastest-growing repositories on GitHub. The whole appeal was ownership: your hardware, your credentials, your lobster.

On Tuesday at I/O, [Google launched Gemini Spark](https://thenewstack.io/google-ai-ultra-pricing/#:~:text=AI%20Ultra%20subscribers%20(at%20both%20the%20%24100%20and%20%24200%20tier)%2C%20will%20also%20be%20the%20first%20to%20get%20access%20to%20Gemini%20Spark%2C%20Google%E2%80%99s%20new%2024/7%20AI%20agent%2C%20and%20Gemini%20Omni%2C%20Google%E2%80%99s%20new%20multimodal%20model.), and it makes the opposite bet. Spark is a 24/7 personal agent built on Gemini 3.5 Flash and connected to Google’s Antigravity agent stack. It runs in the background on virtual machines on Google Cloud. You never see the machine. Google plans to let you text and email the agent directly, so it works while your laptop is shut.

## The split is about where the agent lives, not what it does

Strip away the branding, and Spark and OpenClaw do roughly the same job. Watch an inbox, draft the status update, browse the web, run the recurring task. Both are converging on MCP for tool connectivity, though the implementations differ in maturity. Both promise the assistant who does things rather than answers questions.

> The substrate decides who holds your context, who sees your credentials, and who can change the terms later.

The difference is the substrate. OpenClaw runs on the metal you bought. Spark runs on metal Google rents to you and never names. That sounds like a deployment detail. It is actually the whole argument. The substrate decides who holds your context, who sees your credentials, and who can change the terms later.

## Convenience usually wins this fight, and Google knows it

The self-hosted version asks for real work. Buy the Mac mini, keep it awake, install a daemon, set up Tailscale, and rotate the key when it expires. The reward is control. Your credentials and workflows can stay under your own hand, depending on how you wire up models and integrations. That control is not the same as safety. A misconfigured local agent with shell, browser, and inbox access is its own hazard, and Chinese regulators have already flagged exactly that risk with OpenClaw.

Spark asks for nothing. It is already inside Gmail, Docs, and Sheets, with no manual wiring, because Google owns both ends. That out-of-the-box reach is the structural advantage no third-party agent can copy. The history here is fairly settled. Dropbox beat the home NAS. Gmail beat the mail server. Managed nearly always beats self-hosted for the median user, because most people will trade control for not having to think about it.

> OpenClaw is not losing. It is being sorted into the smaller, stickier half.

So the personal-agent layer splits in two. A hosted tier where Google, and soon OpenAI, own the runtime and the context. A self-hosted tier for developers who want the credentials on their own hardware and will pay for the setup time. OpenClaw is not losing. It is being sorted into the smaller, stickier half.

## The privacy bargain here is not the one Dropbox asked for

This is where I would slow down before calling the race. Cloud storage won because the thing you handed over was inert. Files sat in a Dropbox folder, and nobody read them. A personal agent is of a different kind. To be useful, Spark needs broad standing access to your Gmail, Docs, Sheets, calendar, and live inbox. It does not just store your context. It reads it to act on it.

That changes the deal. Handing Google a folder of files is not the same as handing Google a system that processes your job, your relationships, and your calendar well enough to send mail on your behalf. The honest version of the worry is not that Google keeps your data. It is the unsettled gap between access, retention, and what trains the next model.

The self-hosted camp is small today, but that’s not because of nostalgia for running your own server. It is the instinct that an agent this intimate should answer to you, on hardware you can unplug. That instinct does not scale to everyone. It does not have to. It only has to hold the developers and the privacy-sensitive, and that is a durable floor.

The question for developers is not which agent is better. It is whether you are comfortable with Google holding the keys to the one that runs your life.

## **More stories from Google I/O:**

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://thenewstack.io/wp-content/uploads/2026/04/18d53696-cropped-4edbc4dd-dp-square-600x600.png)

Janakiram MSV (Jani) is a practicing architect, research analyst, and advisor to Silicon Valley startups. He focuses on the convergence of modern infrastructure powered by cloud-native technology and machine intelligence driven by generative AI. Before becoming an entrepreneur, he spent...

Read more from Janakiram MSV](https://thenewstack.io/author/janakiram/)