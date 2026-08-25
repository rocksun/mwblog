Anthropic launched a new Browser Use tool that gives Claude a structured view of a web page in addition to what is visually rendered. Announced Thursday, the tool uses the page’s accessibility tree to help Claude find and interact with specific elements directly rather than having to work out where they are on the screen.

Browser Use is part of a broader Anthropic release that also brings Computer Use, the Skills API and Files API into general availability. Developers can access the browser tool through the Claude API using browser\_toolset\_20260801.

> Browser Use is part of a broader Anthropic release that also brings Computer Use, the Skills API and Files API into general availability.

The change gives Claude a more direct way to interact with a web page. Instead of working out a button’s position from a viewport image and targeting coordinates such as `x: 640, y: 320`, Claude can receive a reference such as `ref_3` tied to that element and use it when it wants to act.

## Page references replace coordinates

Computer Use can operate across an entire desktop by looking at screenshots and sending mouse coordinates and keyboard commands. Browser Use works within the browser itself, where it can use page structure that would be difficult to recover reliably from pixels alone.

When Claude calls `read_page`, the developer’s executor returns a text representation of the accessibility tree, in which elements such as links, buttons, and text boxes can be tagged with references. If Claude later wants to click a button represented by `ref_3`, it can send that reference along with the requested operation rather than trying to calculate where the button is on the screen.

That said, if the tab navigates to a new page or the page changes enough, a reference that pointed to a button a moment ago may no longer work. The API will not catch that on its own, so the executor has to recognize when the reference no longer matches the underlying element, reject the action and have Claude read the page again before continuing.

## Batching cuts model calls

Playwright, for example, can represent a page as an ARIA snapshot and locate elements by role rather than coordinates. At the same time, Microsoft’s Playwright MCP server already exposes structured accessibility snapshots with references a model can use to identify elements. The concepts line up closely with Browser Use, but the protocols do not: Playwright MCP speaks MCP, while Anthropic’s tool uses its own client-toolset protocol, so developers would still need an adapter that translates Claude’s requests into Playwright actions and returns the results in the format Claude expects.

Puppeteer offers many of the same building blocks, exposing the browser’s accessibility tree via Accessibility.snapshot() and providing APIs for controlling Chrome and Firefox. A developer could use those APIs for navigation or page reads, then maintain Anthropic’s reference mappings on top.

> A developer could use those APIs for navigation or page reads, then maintain Anthropic’s reference mappings on top.

Slightly confusing, an unrelated open-source project also called [Browser Use](https://github.com/browser-use/browser-use) runs AI browser agents against Chromium through the Chrome DevTools Protocol. Despite the shared name, it has no connection to Anthropic’s tool and comes with its own agent loop and browser abstractions, so connecting the two would still require integration work.

## Several browser actions can happen in one turn

Anthropic is also reducing the back-and-forth between Claude and the browser by allowing multiple actions to be requested in a single model turn. Now actions can arrive together as several tool\_use blocks. The application executes them in order and sends the results back together, avoiding another model call between every click and keystroke. Anthropic says that can lower latency and costs, particularly as workflows scale from a handful of interactions to dozens or hundreds.

That matters more as browser tasks get longer. [Cheaper models alone will not solve the token cost problem in agentic workflows](https://thenewstack.io/agentic-ai-token-costs/), so cutting unnecessary model calls is another way to reduce costs.

If Claude has to return to the model after every click or keystroke, a long browser task can quickly rack up model calls. Batching cuts out some of that back-and-forth by letting Claude request several actions at once, but the browser still has to carry them out in order because each one depends on what happened before it. If Claude asks to click a button, fill in a field, and submit a form, for example, the executor cannot simply move on to the next step if that first click fails, because everything that follows is now based on a page state Claude never reached.

> Batching cuts out some of that back-and-forth by letting Claude request several actions at once, but the browser still has to carry them out in order because each one depends on what happened before it.

## Developers host the browser

Browser Use is currently limited to the Claude API and is not available inside [Claude Managed Agents](https://thenewstack.io/with-claude-managed-agents-anthropic-wants-to-run-your-ai-agents-for-you/). Adding it to a Messages API request exposes 27 browser operations by default. Claude can decide which of those operations it wants to use, but Anthropic does not execute them. The application has to translate each request into an action inside its own browser environment, preserve the session between turns and return enough information for Claude to understand what happened.

Loading all of those operations has a token cost. Anthropic’s [pricing documentation](https://platform.claude.com/docs/en/about-claude/pricing) says the default Browser Use toolset adds roughly 6,600 input tokens to a request, before counting screenshots, accessibility trees and other results sent back to Claude. Developers can turn off operations they do not need to reduce that overhead.

It also creates a different hosting split from some of the other tools Anthropic announced Thursday. Skills uploaded through the Skills API can run inside Anthropic’s code execution sandbox, while the Files API stores documents that can be reused by ID. Browser sessions, along with their downloads and uploaded files, stay in the developer’s environment.

## Approval gates need rethinking

Claude can still encounter a prompt injection in web content or be redirected to an unexpected location, which is why Anthropic recommends running the browser in an isolated container or virtual machine with minimal access. JavaScript and file uploads should remain disabled unless needed, since code generated by Claude runs with the page’s privileges and can reach data or make requests available to that page.

Batching makes approval a little trickier because several actions can arrive at once, and a routine click at the beginning of a sequence could eventually lead to something that requires the user’s permission. That means the executor has to check actions as they happen and stop for approval when needed.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://thenewstack.io/wp-content/uploads/2026/06/c176528b-cropped-54a705ce-amandacaswellheadshot_4-600x600.jpeg)

Amanda Caswell is an AI journalist, certified prompt engineer, and technology commentator whose work and expertise have been featured on Fox News and CBS News. She covers artificial intelligence, developer tools, foundation models, and emerging technologies, with a particular focus...

Read more from Amanda Caswell](https://thenewstack.io/author/amanda-caswell/)