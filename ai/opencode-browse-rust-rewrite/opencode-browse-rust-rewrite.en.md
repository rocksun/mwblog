![developer with code on his screen](https://cdn.thenewstack.io/media/2026/11/57fc2d31-rizki-ardia-i-aetokirtk-unsplash-1024x753.jpg)

OpenCode developer Dax Raad says he rebuilt the project’s browser automation tool in Rust for $60, replacing the parts of Playwright and Patchright it actually used and dramatically reducing its memory footprint.

## A 4.3 MB binary

The figures [he](https://thdxr.com/) posted to [X on Saturday](https://x.com/thdxr/status/2121692397323350468) are striking. The new Rust binary is just 4.3 MB, compared with 53 to 64 MB for the previous Node version. Memory use for each [OpenCode Browse](https://github.com/anomalyco/browse) connector also fell from roughly 190 MB to 5.6 MB after a few calls, a reduction of about 97%.

> The new Rust binary is just 4.3 MB, compared with 53 to 64 MB for the previous Node version.

The relay that wires AI coding agents to the browser shows a similar gap, with Raad’s comparison putting the Rust implementation at 6 MB idle, or 6.6 MB once it has served calls, against 353 MB for the old Node relay after six days of running.

## Replacing Playwright and Patchright

OpenCode Browse connects AI coding agents to a developer’s existing browser through a Chromium extension and an [MCP server](https://thenewstack.io/model-context-protocol-bridges-llms-to-the-apps-they-need/). The previous Node implementation used Playwright for browser automation and Patchright to reduce detection, but Raad rebuilt the functionality Browse needed in Rust to cut runtime overhead.

> Raad rebuilt the functionality Browse needed in Rust to cut runtime overhead.

The new Rust relay communicates with the Chromium extension over WebSockets and uses the Chrome DevTools Protocol to handle browser operations, agent sessions, recordings, and network captures. It also embeds QuickJS to execute agent-supplied JavaScript without requiring the previous Node runtime.

## Inside the pull request

The [merged pull request](https://github.com/anomalyco/browse/pull/264) confirms that Raad replaced the Node-based CLI and relay while keeping the existing Chromium extension and using the Chrome DevTools Protocol for browser operations.

The team ran two rounds of testing with about 10 regression agents against a real Chrome browser. Browse scored 85% on Stealth Bench v2, compared with 90.5% for Browser Use Cloud, although the pull request doesn’t include a score for the old Node version.

Not everything made it into the rewrite; Raad dropped time zone and locale emulation along with the download tool, which Chrome blocks for extensions. The Rust version also retains a problem from the Node implementation where a busy-looping eval can’t be stopped through the extension.

Browse still includes relay authentication, extension pairing and origin restrictions, and agents are limited to tabs they open themselves or that users explicitly share with them.

## The real $60 cost

Raad says the rewrite “only cost $60” and confirmed in a reply on X that he used Claude Opus as his main coding model and DeepSeek as a subagent.

The two models helped him replace the Playwright and Patchright functionality Browse needed, although the $60 figure doesn’t include the time he spent checking, testing, and fixing the code. The [challenge with Rust rewrites](https://thenewstack.io/is-a-rust-rewrite-really-worth-it/) is finding a smaller replacement that matches the original’s functionality without creating more maintenance work.

> the $60 figure doesn’t include the time he spent checking, testing, and fixing the code

The memory savings are impressive, but Raad has also taken on responsibility for code that Playwright and Patchright previously maintained. His team will also have to deal with browser updates, authentication changes and security fixes that previously came through those libraries. That’s where [AI-generated technical debt](https://thenewstack.io/ai-technical-debt-verification/) can become a problem, especially when code is cheap to produce but takes considerably more work to maintain.

The post [Dax Raad rebuilt his browser tool in Rust for $60. Then memory use fell 97%.](https://thenewstack.io/opencode-browse-rust-rewrite/) appeared first on [The New Stack](https://thenewstack.io).