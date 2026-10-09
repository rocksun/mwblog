**GitHub Copilot will soon decide whether coding tasks run locally or get sent to cloud models**, with automatic routing expected by the end of October. Microsoft outlined the plan Wednesday in a post co-written by [Patrick Nikoletich](https://www.linkedin.com/in/patrick-nikoletich-99a42918/), a GitHub product manager, and [Stuart Schaefer](https://www.linkedin.com/in/stuart-schaefer-43337/), a Windows platform partner architect.

The announcement coincided with GitHub making its new sandboxing controls generally available, but the protections differ depending on which tools Copilot uses. Shell commands and local MCP servers receive OS-level restrictions, while built-in file tools rely on checks inside the agent harness. Remote MCP servers remain outside the local process sandbox.

Nikoletich and Schaefer acknowledge that “local inference does not make the session offline.” Microsoft hasn’t said how much repository context Auto sends to cloud models, whether developers can inspect routing decisions or whether Auto can be restricted to local inference.

## Copilot decides where inference runs

GitHub is expanding Project HydraFusion, which already selects models for coding tasks, to handle where those models run. Microsoft says Copilot will weigh task context and cache state when switching between local and cloud inference, including during multi-turn sessions.

In Copilot CLI, the Copilot app and VS Code, developers can use Auto routing or select a local model themselves. Options include MAI Code 1.1 Flash through the Windows ML provider and OpenAI-compatible local endpoints.

## Auto routing raises questions

Microsoft hasn’t said how much conversation history or repository context Auto sends to the cloud when it routes a task. It also hasn’t said whether developers can see those decisions or restrict inference to local models. Teams with strict data-handling policies still don’t know what repository data Copilot sends to the cloud. Similar questions came up last month when [Anthropic said it could route Claude Sonnet 5.5 requests to Sonnet 5](https://thenewstack.io/claude-sonnet-cyber-safeguards/) when it detects higher-risk activity.

> Teams with strict data-handling policies still don’t know what repository data Copilot sends to the cloud.

Selecting a local model keeps inference on the device, but it doesn’t stop the agent from reaching external services or making network requests through its tools. Developers who need a fully local session will also have to lock down what those tools can access.

MAI Code 1.1 Flash is a mixture-of-experts model with 137 billion total parameters and 6.8 billion active, and Microsoft used mixed-precision quantization at roughly 3.3 bits per weight to shrink it to 53GB, an 80% reduction from the bfloat16 cloud version.

The pressure to squeeze models onto smaller hardware has pushed similar efforts elsewhere, including Intel’s work to [compress a 1.58-bit LLM even further](https://thenewstack.io/intel-bitcos-ternary-compression/). Microsoft paired quantization with speculative decoding, in which a drafter proposes blocks of tokens for the main model to verify, to speed up local inference.

> Microsoft paired quantization with speculative decoding, in which a drafter proposes blocks of tokens for the main model to verify, to speed up local inference.

## Quantization meets memory limits

The initial rollout targets NVIDIA RTX Spark Windows PCs such as Surface Laptop Ultra, which offers up to 128GB of unified memory. On that machine, Microsoft measured peak memory use of 75.5GB at a 256K-token context, a figure that rules out most developer laptops with 16GB or 32GB of RAM.

The 53GB of weights is only part of the bill. The operating system, applications, inference runtime, and key-value cache all need room, and the cache keeps growing as the agent reads files and receives tool results, so developers running longer sessions will need to budget for memory well beyond the model itself.

## Benchmarks with fine print

Microsoft reports that the quantized model scored 70.8% on SWE-Bench Verified, compared with 72.6% for the full-precision version, and that it outperformed the original on Terminal-Bench 2.1 with 66.29% against 62.9% on a dataset of 89 tasks. On a benchmark that small, the gap amounts to three tasks. The results suggest the company shrank the model without sacrificing much coding performance, but fall well short of showing that quantization made it better.

Copilot uses Microsoft’s open source Execution Containers (MXC) library to enforce sandbox policies, with the BaseContainer tier of the ProcessContainer backend on Windows, Seatbelt on macOS and bubblewrap on Linux.

When sandboxing is enabled, Copilot applies OS-enforced restrictions to shell commands and, where supported, local MCP and language servers. GitHub says those restrictions apply regardless of whether a task runs on a local or cloud model.

Copilot’s built-in file tools run inside the agent process, where the harness checks requests against sandbox policy rather than relying on OS-enforced isolation. Remote MCP servers also sit outside the local sandbox, with Copilot checking their connection policies when MCP sandbox controls are enabled.

> Remote MCP servers also sit outside the local sandbox, with Copilot checking their connection policies when MCP sandbox controls are enabled.

Microsoft’s demo uses MAI Code 1.1 Flash to build a daily triage dashboard in a sandboxed `copilot-sdk` project, which it describes as an offline workflow. Yet the prompt uses GitHub issue and pull request metadata instead of the local repositories and tests described earlier in the post. Microsoft doesn’t say whether that metadata was retrieved over the network or cached locally, leaving its offline claim unverified.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://thenewstack.io/wp-content/uploads/2026/06/c176528b-cropped-54a705ce-amandacaswellheadshot_4-600x600.jpeg)

Amanda Caswell is an AI journalist, certified prompt engineer, and technology commentator whose work and expertise have been featured on Fox News and CBS News. She covers artificial intelligence, developer tools, foundation models, and emerging technologies, with a particular focus...

Read more from Amanda Caswell](https://thenewstack.io/author/amanda-caswell/)