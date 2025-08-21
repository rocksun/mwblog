[WebAssembly](https://thenewstack.io/webassembly/) (Wasm) [debugging](https://thenewstack.io/master-the-art-of-python-debugging-with-these-tips/) remains, understandably, a challenge for this relatively new and exciting technology that is still evolving. Originally designed for the browser, it functions well in that environment, especially for debugging web applications from within another browser. [Emscripten](https://thenewstack.io/how-to-compile-c-code-into-webassembly-with-emscripten/), as the toolchain compiler and extensions built in Firefox and Chrome, offers reasonably reliable debugging for Wasm running in the browser.

However, moving beyond the browser — particularly to backend use cases and deployment across different environments and languages — debugging becomes significantly more complex. Despite these challenges, progress has been made.

Last year, during Wasm I/O 2024, there was a stark contrast between the debugging discussions presented then and those in [Wasm I/O 2025](https://2025.wasm.io/), when Microsoft’s [Ralph Squillace](https://github.com/squillace) described the state of debugging JavaScript for the front and backend as “embarrassing.”

## Challenges

During the Wasm I/O 2024 talk, “Nobody Knows the Trouble I’ve Seen: Debugging Wasm for web and server,” Microsoft’s [Natalia Venditto](https://www.linkedin.com/in/anfibiacreativa/) and Squillace described the continued challenges of debugging due to a lack of a standard API for Wasm code beyond the browser, particularly in the backend. As Venditto said during her talk, two challenges have emerged:

First, determining what belongs inside a WebAssembly module versus what should remain in the [JavaScript](https://thenewstack.io/introduction-to-javascript/) standard. Second, managing the debugging process. Multiple layers may exist, and access to those layers may not be straightforward. “New knowledge may be required,” Venditto said.

As Venditto noted, nearly 100% of JavaScript developers, when asked about a preferred code editor, choose [VS Code](https://thenewstack.io/how-to-use-vs-code-for-python-and-why-you-should/). The preferred environment remains consistent throughout the workflow: during build, deployment, and cloud debugging, she said.

“The browser continues to serve as a core environment for JavaScript developers. This environment provides familiarity, well-known tools and efficient workflows,” Venditto said.

Venditto described the scenario of a JavaScript developer looking to use WebAssembly in an application and manage the entire workflow. The challenges have consisted of first, determining what belongs inside a WebAssembly module versus what should remain in the JavaScript standard, and second, managing the debugging process. “Multiple layers may exist, and access to those layers may not be straightforward. New knowledge may be required,” Venditto said. Despite these challenges, “building within a familiar context remains important,” Venditto said.

## SpiderMonkey and VS Code

Flash forward to 2025 Wasm I/O during the talk, “No More Printf: Interactive Debugging Wasm for Web and Server,” given by Squillace and Fermyon’s [Till Schneidereit](https://www.linkedin.com/in/tillschneidereit/?originalSubdomain=de). The discussion focused on debugging JavaScript in WebAssembly using the [SpiderMonkey](https://thenewstack.io/python-meets-javascript-wasm-with-the-magic-of-pythonmonkey/) engine and Visual Studio Code. Key points included the use of components.as.js to generate bindings for debugging, the importance of socket connections for remote debugging and the ability to debug without redeploying. The speaker highlighted the need for a unified debugging experience across different languages, including [.NET](https://thenewstack.io/net-modernization-github-copilot-upgrade-eases-migrations/) and [Python](https://thenewstack.io/what-is-python/), and the goal of enabling debugging across components in a multilanguage environment. The session also covered the use of launch configurations in VS Code for debugging and the potential for post-deployment debugging in live environments.

Squillace expressed enthusiasm about the advancements in debugging tools, particularly highlighting the integration of [C++](https://thenewstack.io/feds-critical-software-must-drop-c-c-by-2026-or-face-risk/) and [static analysis tools](https://thenewstack.io/how-static-analysis-can-save-your-software/). He referenced previous challenges encountered in the past year and noted the transition away from native code dependencies.

Schneidereit emphasized Fermyon’s approach to debugging WebAssembly. He clarified that the focus is not on building a new debugger for WebAssembly bytecode but on utilizing existing tools like SpiderMonkey. This approach avoids the need to inspect bytecode directly, rendering tools like DWARF and LLDB less effective. Instead, the built-in content debugger in SpiderMonkey is employed, connecting to external debuggers such as Visual Studio Code via socket interfaces. This method proves beneficial for production builds, eliminating the necessity for embedded debug symbols or disabled optimizations. Moreover, it is not specific to any particular runtime, unlike other solutions that require comprehensive DWARF-based debugging implementations, Schneidereit said.

The demonstration showcased Node.js running with components processed by Jacob, which transforms the main JavaScript profile into a set of WebAssembly modules accompanied by JavaScript glue code. This setup enables execution in Node.js, which lacks native module support. Jacob, by default, uses port 8000, facilitating the same pipeline to run JavaScript in SpiderMonkey within a WebAssembly component in Node.js. This configuration allows for consistent debugging experiences across different environments, including stepping through code and hitting breakpoints, Schneidereit said.

A notable advantage of this approach is the requirement of only an outgoing socket connection, eliminating the need to run a socket server, Schneidereit said. Traditional debugging often involves running a debug server on the device being debugged, such as in iOS or Android applications. In contrast, this method inverts the process, requiring only an outgoing connection, which simplifies remote debugging. This capability allows for post-deployment debugging in live environments by sending a special request with an authentication key, connecting back to the environment without necessitating redeployment, Schneidereit said.

The next steps involve coordinating with other programming languages, including .NET and Python, aiming to unify debugging experiences across different platforms, Schneidereit said. The goal is to enable the use of the same extension, ideally within Visual Studio Code, to debug various languages. Since the protocol used does not require Visual Studio Code to recognize the specific language being debugged, it only needs to receive appropriate messages regarding stack layouts and other debugging information, Schneidereit said.

“A significant motivation behind this work is to pave the way for a standardized solution where runtimes play a role in facilitating a unified debugging workflow. Currently, the approach is fully contained within the content, which restricts the ability to step between components seamlessly,” Schneidereit said.

Given that the component model emphasizes composing applications from different building blocks in various languages, the “ultimate objective” is to provide a debugging experience that spans across these components, Schneidereit said. “This would allow developers to step into imported functions from other components, transitioning smoothly between different languages, such as moving from JavaScript to C#,” Schneidereit said. “The aspiration is to achieve this integrated debugging capability in the near future.”

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![]()

BC Gain is founder and principal analyst for ReveCom Media. His obsession with computers began when he hacked a Space Invaders console to play all day for 25 cents at the local video arcade in the early 1980s. He then...

Read more from B. Cameron Gain](https://thenewstack.io/author/bruce-gain/)