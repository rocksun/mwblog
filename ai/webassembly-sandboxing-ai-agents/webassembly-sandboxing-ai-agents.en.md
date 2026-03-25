AI agent-generated code poses an often-overlooked threat: the possibility that an agent will generate unchecked, potentially lethal commands. Think of Hal 9000 taking over the mission in Stanley Kubrick’s *2001: A Space Odyssey*. While that was sci-fi, it’s not far from a real scenario playing out today: Code derived from LLM output can produce AI agents that gain access to sensitive data and applications, wreaking havoc on the environment.

It’s a scenario that [Dan Phillips](https://www.linkedin.com/in/d-philla/), a systems engineer and founder of WebAssembly Chicago, explored during his talk at Wasm I/O held this month in Barcelona.

## Agents run code and need isolation

Phillips outlined why WebAssembly can provide excellent isolation and sandboxing for untrusted AI-generated code. As agents have evolved into actors that perform actions on a user’s behalf, they need an execution environment, he said.  
  
“This is because they don’t just think – they run code derived from LLM output and produce artifacts,” Phillips said. “Code is deterministic, so adding isolation provides a core primitive for agents.”

## Containers share a kernel problem

Several technologies are currently used to sandbox code, but they often rely on a shared kernel. Often, containers, the [gVisor](https://gvisor.dev/) security layer, or microVMs like Firecracker offer some isolation but can be woefully inefficient. These methods rely on a shared kernel, have heavy runtime layers, and add orchestration complexity involving nomads, namespaces, and control planes,   Phillips said.

> “Instead of starting from the kernel or containers, you start with nothing and then add from there. This makes certain exploits unavailable by construction.”

“This is expensive in terms of money, time, and understanding. It can be hard to reason about and slow to spin up,” Phillips said. “These all rely on a shared kernel, right? These have relatively heavy runtime layers, and they’re on top of these; things will start to be things like orchestration complexity.”

## Wasm starts with nothing

However, WebAssembly offers that much-needed isolation layer for AI agents. This is because it has no shared kernel and uses a different memory model. “Instead of starting from the kernel or containers, you start with nothing and then add from there,” Phillips said. “This makes certain exploits unavailable by construction.”

WebAssembly modules, through which applications and code run, can also be orders of magnitude smaller, which is one of Wasm’s standout features. Its well-known benefits include ultra-rapid startup times and what Phillips called Wasm’s enablement of  isomorphic computing, where the same code runs in the browser, phone, cloud, or home server.”

## Boxer removes developer friction

Despite the Wasm offers for AI Agent sandboxes, developers often don’t want to rewrite code for a new technology if they don’t understand the benefits, Phillips said. Developers expect a platform and full system access, even if it’s limited. Phillips described how open-source Boxer allows users to take a Dockerfile and distribute it as a universally runnable Wasm distribution.

> “For most things that you could do with Docker, you can do in Wasm also.”

“The project’s goal is to allow the running of unmodified code with no rewrites and no compromises,” Phillips said. “This helps take away friction and make Wasm more accessible. This basically means that for most things that you could do with Docker, you can do in wasm also.”

Despite its technical benefits, WebAssembly faces a “mental model gap,” Phillips said.  Developers often expect a full platform with system access and are reluctant to rewrite existing code.  “People don’t want to rewrite code when they deploy,” Phillips said. “So, a new technology, specifically one that has a reduced environment, and they don’t really want to do it if they don’t understand the benefits.”

The future of sandboxing extends beyond the cloud to “isomorphic computing,” where the same agentic code can move seamlessly between browsers, mobile devices, and home servers. “It’s not just cloud, but also isomorphic computing, where you have the same code running in your browser, your phone on the cloud, your server at home, where you can move these things between these different elements seamlessly,” Phillips said.

Yes, developers, platform, and engineering teams do not want to have to fiddle with potential incompatibilities or add layers of “glue” to ensure code – created by AI agents or otherwise – remains sandboxed. But regardless, WebAssembly already offers at least a very solid level of isolation, which is much needed for the explosion in the distribution of AI agentic code.

For advocates, the question becomes rhetorical: Why would you *not* sandbox AI agents with WebAssembly modules?

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://cdn.thenewstack.io/media/2020/04/4d3b9442-bruce-gain.jpg)

BC Gain is founder and principal analyst for ReveCom Media. His obsession with computers began when he hacked a Space Invaders console to play all day for 25 cents at the local video arcade in the early 1980s. He then...

Read more from B. Cameron Gain](https://thenewstack.io/author/bruce-gain/)