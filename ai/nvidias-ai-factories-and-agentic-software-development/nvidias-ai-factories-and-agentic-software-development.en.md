I normally look at large language model (LLM) software tools that I can test immediately, but this post started because of software I couldn’t test. I was looking at how Solver, a [so-called “self-driving” AI coding tool](https://thenewstack.io/self-driving-software-solver-launches-autonomous-ai-coder/), was doing since our article a year ago. And I noticed that it had gone — [sold to NVIDIA](https://techstartups.com/2025/09/03/nvidia-acquires-ai-coding-startup-solver-amid-growing-ai-investment-spree/). Solver was already using an agent-based approach last year, so it was ahead of the curve. But what does NVIDIA want with it?

“NVIDIA is a hardware company” would normally have been enough to curb my enthusiasm for examining anything further. But of course NVIDIA’s chips are the heart of the AI revolution, and consequently it was the first company in the world to be worth 4 trillion dollars. So it is worth looking at what it is doing, even if your interests lie with the software development world.

NVIDIA has been making a lot of purchases recently, including the kind of [investments in its own ecosystem](https://thenewstack.io/how-solid-is-ed-zitrons-case-against-generative-ai/) that cause share prices to inflate without the income to truly back it up. Muddying the waters even more, NVIDIA also announced it would pump $100 billion into OpenAI. But what is the different world it is betting on? The clue is in the dusty term “vertical integration.”

## Understanding Vertical Integration in AI

Let’s look at the typical agentic CLI setup that that I review regularly. I start with a terminal (usually [Warp](https://thenewstack.io/warp-goes-agentic-a-developer-walk-through-of-warp-2-0/)), then I install the target agentic CLI app on it (for example, [Claude Code](https://thenewstack.io/claude-opus-4-with-claude-code-a-developer-walkthrough/)). When running, it queries maybe the Claude Sonnet LLM, communicating via Anthropic, which runs its models on AWS clouds. This is treating everything as a component in a chain. You are hoping for the chance to use the best in class, or at least the most affordable. The argument normally made is that once a model is trained, it can be run on cheaper chips and on a commodity cloud, giving us a horizontal or modular market.

By comparison, vertical integration is what Apple does. It makes its own hardware, its own chips, its own operating system, and begrudgingly allows people to write software applications for their own ecosystem. At the very least, this improves reliability and security.

What’s wrong with the horizontal market for AI? In the agentic era we are no longer asking a one-shot question to a chatbot. Multiple agents work in parallel, which complicates the relationship with the LLM (or LLMs). As NVIDIA founder and CEO [Jensen Huang](https://www.linkedin.com/in/jenhsunhuang/) puts it, the true resource limitation isn’t cost per chip anymore; it is how many tokens you can generate per kilowatt, because the limiting factor is now power. However you source the electricity, just pumping it through one large location consistently is a challenge. Soon, the limiting factor may well be water.

## NVIDIA’s Advantage: The AI Factory Model

This is where NVIDIA’s advantage lies: in having a variety of the most powerful chips that generate the most tokens per kilowatt. To serve lots of different types of request (short or deep) NVIDIA has a software layer that optimizes the way AI models run across potentially hundreds or thousands of GPUs, dynamically allocating resources based on workload needs in their AI factories or data servers.

But we don’t really need to get into the weeds because the integrated example of the Apple MacBook is demonstration enough. The MacBook is just more efficient because the operating system doesn’t have to make educated guesses about the hardware. It can stop itself and restart itself instantly without mysterious “sleep” or “hibernation” mechanics that work inconsistently. Ask any PC gamer about never knowing how well their latest game will run on their machine until they run it.

NVIDIA’s AI factories are intended for industrial placement. The idea is that they can train for a specific sector, and then handle the inference requests. But lets imagine that a suitable factory is eventually available for downstream developers.

## The Future of Agentic Startups and NVIDIA’s Role

So how would a future agentic CLI work in an AI factory work?

You would probably have an account at your local “AI factory,” or maybe a more comprehensive deal through NVIDIA. And there should be just one bill, whose size can be tracked (or predicted) accurately in real time.

If your code was sitting in a repository visible to NVIDIA, that would allow for project scanning and [isolated branches for parallel running](https://thenewstack.io/a-hands-on-review-of-conductor-an-ai-parallel-runner-app/). The advantage of owning GitHub remains squarely with Microsoft (and by extension, OpenAI). Either way, the project would be scanned locally and sent up to the “AI factory” or read via a shared repo. One advantage of vertical integration is that your query is going through fewer hands. You obviously have to trust NVIDIA, but potentially no one else. NVIDIA has to decide how much this matters to its customers.

NVIDIA could make different service offerings based on the range of chips available for your account. The greater the range offered, the easier it would be to offload shallow agents to cheaper LLMs, which might allow the user to gain a cut on the savings.

Now, I would expect that an API would be available, but the temptation to design (or buy in) a Claude Code-style agentic CLI would be too great. Of course this is where we started, talking about Solver.

## Conclusion

What happens behind the scenes shouldn’t matter too much for the software developer, but the advantages of the agentic era are tightly coupled to the speed of token generation and parallel running.

At some point the agentic startup bloom must reach winter. When that comes, NVIDIA will certainly be one of the companies in a great position to pick up the pieces. Of course, it doesn’t have a relationship with the development community beyond the specialized [CUDA platform](https://developer.nvidia.com/cuda-toolkit). So if it were coming this way, I would expect to see beta tools released while the agentic era is still enjoying its summer.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://cdn.thenewstack.io/media/2022/09/2e2ac7a2-cropped-a46bbf33-photo.png)

David has been a London-based professional software developer with Oracle Corp. and British Telecom, and a consultant helping teams work in a more agile fashion. He wrote a book on UI design and has been writing technical articles ever since....

Read more from David Eastman](https://thenewstack.io/author/david-eastman/)