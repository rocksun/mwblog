**Google is giving coding agents like Anthropic’s Claude Code and OpenAI’s Codex deeper access** to its Android development tools, including devices, performance profilers and production crash reports; now, agents can now investigate bugs, test changes, and verify their own fixes.

The push spans Android Studio and the terminal-based Android CLI, with Google opening both to third-party agents rather than steering developers toward Gemini. [Matthew McCullough](https://www.linkedin.com/in/matthewjmmccullough/), vice president of product for Android, has emphasized giving developers the freedom to choose their own models and coding agents.

In a [Wednesday post](https://developer.android.com/blog/posts/android-dev-summit-26-developer-tools-performance), [Adarsh Fernando](https://www.linkedin.com/in/adarsh-fernando-87905462/), senior product manager for Android developer tools, describes the goal as giving developers and their agents “the tools and knowledge to build high-quality Android apps faster.” The updates were announced Wednesday at [Android Dev Summit](https://developer.android.com/events/dev-summit).

## Bring your own agent

The company’s Bring Your Own Agent feature now supports more than 40 coding agents that speak the open [Agent Client Protocol](https://agentclientprotocol.com/), among them Anthropic’s Claude Agent, OpenAI’s Codex, and Google’s own Antigravity, and Google says the feature is now stable in Wednesday’s release of Android Studio Rabbit 2.

A developer can install several and switch between them without leaving the IDE, and connected agents inherit the IDE’s own read on a project — its structure, build configuration, symbols, and tools such as Compose Preview, the emulator, and Logcat — context they would otherwise have to rebuild through code searches and terminal guesswork.

Alongside it, a new Change Review feature scans an agent’s pending changes for common issues and can walk a developer through a large set of modifications before anything is applied, and Google is pushing the same reach beyond the IDE with official Android CLI plugins for Claude Code, and Codex that cover project creation, emulator management, UI inspection, and its Android documentation.

## Compose previews from the terminal

Another announcement includes the new android preview command that lets coding agents render Jetpack Compose previews directly in the terminal without launching an IDE or emulator.

The company says agents using it completed UI tasks 77% faster while using up to three times fewer tokens, though it shared little about how it measured those results. The CLI also adds android device remote, giving agents access to physical devices in Google’s lab for testing.

> agents using it completed UI tasks 77% faster while using up to three times fewer tokens, though it shared little about how it measured those results.

## Finding memory leaks with Claude

Google is also giving agents more ways to investigate problems after an app is built, including performance issues, production crashes and memory leaks. In one demo, Claude Code worked with LeakCanary, an open source leak-detection library, to check critical user journeys for memory leaks using a single instruction from the developer.

Claude Code ran the journeys across multiple devices in parallel, analyzed heap dumps through the CLI’s LeakCanary integration, and traced the leaks back to the offending code. It then made the fixes and reran the tests to confirm they worked. Google says the tooling helped capable models complete these investigations nearly twice as fast while using up to 25% fewer tokens.

> autonomous bug-finding can outrun autonomous bug-fixing — an Anthropic scanner flagged some 29,000 possible vulnerabilities in open-source code while only a few hundred were ever fixed.

The demo is very impressive, and it also runs against a record that counsels patience, since autonomous bug-finding can outrun autonomous bug-fixing — an Anthropic scanner flagged [some 29,000 possible vulnerabilities in open-source code while only a few hundred were ever fixed](https://thenewstack.io/anthropic-oss-scanner-vulnerabilities/).

A companion android signals command now pipes Android vitals and Firebase Crashlytics data into the same terminal workflow, which gives agents a direct line to production crashes, ANRs, and memory problems, but none of this retires the human in the loop, as developers who watched [Claude Code land a Linux kernel fix only for reviewers to catch a race condition](https://thenewstack.io/torvalds-claude-code-kernel/) can attest.

> A companion android signals command now pipes Android vitals and Firebase Crashlytics data into the same terminal workflow

## Benchmarking agents with Android Bench

Google is also introducing Android Bench 2.0 to evaluate how models and agent harnesses perform on more complex Android development tasks. It tests whether completed apps actually run with assignments ranging from building an app from mockups to migrating an existing interface. Some tasks are modeled on work that would take an Android engineer several days, and the benchmark also measures completion time and cost.

[AI Engineer
Step by step guide to becoming an AI Engineer in 2026

Introduction
Working With LLMs
Context Engineering
AI Models
Embeddings & Vector Databases
Embedding Models
RAGs
AI Agents
AI Safety and Ethics
Evaluation & Observabiity](https://roadmap.sh/ai-engineer?utm_source=thenewstack&utm_medium=referral&utm_campaign=roadmap-card&utm_content=android-agents-build-debug)

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://thenewstack.io/wp-content/uploads/2026/06/c176528b-cropped-54a705ce-amandacaswellheadshot_4-600x600.jpeg)

Amanda Caswell is an AI journalist, certified prompt engineer, and technology commentator whose work and expertise have been featured on Fox News and CBS News. She covers artificial intelligence, developer tools, foundation models, and emerging technologies, with a particular focus...

Read more from Amanda Caswell](https://thenewstack.io/author/amanda-caswell/)