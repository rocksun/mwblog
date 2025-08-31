Flutter 3.35 was released on Aug. 16 with updates that include the stable release of stateful hot reload on the web and the [Dart and Flutter MCP Server](https://dart.dev/tools/mcp-server). It also includes the experimental release of Widget Previews.

Developer productivity was a key aspect of this release, according to a [Flutter blog post](https://medium.com/flutter/whats-new-in-flutter-3-35-c58ef72e3766) by [Kevin Chisholm](https://www.linkedin.com/in/kevin-chisholm/), a technical program manager for Dart and Flutter at Google.

Stateful hot reload on the web is now enabled by default, Chisholm wrote. The feature means a developer can edit their web application’s code and see the changes instantly in the browser without losing the application’s current state.

Hot reload is a process that enables the development server to automatically inject new code into a running application after a file is saved, avoiding a full page refresh. The “stateful” part means the application’s current state — like data in a form, a user’s position in a game, or a toggle that’s been flipped — is preserved during the hot reload.

“Our goal is to provide a seamless and consistent hot reload experience across all platforms,” Chisholm wrote. “While you can still disable this feature using a flag, we plan to remove that ability in a future release.”

Also, The Dart and Flutter [MCP Server](https://thenewstack.io/remote-mcp-servers-inevitable-not-easy/) is now available in the stable channel of the Dart SDK.

“The Dart and Flutter MCP Server acts as a bridge, giving [AI coding assistants](https://thenewstack.io/enhancing-ai-coding-assistants-with-context-using-rag-and-sem-rag/) access to even more of your project’s context via the Dart and Flutter toolchain,” Chisholm wrote. “Instead of just suggesting code, your AI assistant can now understand your project deeply and take action on your behalf. This allows you to stay focused on your goals while the AI handles the mechanics.”

The release also includes Widget Previews, a new experimental feature that allows developers to view and iterate on a single widget in isolation, directly within their IDE, without having to run the entire application.

It complements the stateful hot reload, Chisholm said.

“Widget previews complements this by allowing you to visualize and test your widgets in a sandboxed environment, completely separate from a full app,” he wrote. “This is invaluable when building out a design system or testing a component across a matrix of different configurations, such as various screen sizes, themes, and text scales, all at once and side-by-side.”

It speeds up the development process by allowing developers to focus on a specific UI component for fine-tuning the widget’s design and behavior, but without needing to build and run the full app.

Also noteworthy in this release is [WebAssembly](https://thenewstack.io/what-debugging-javascript-on-webassembly-looks-like/) dry runs.

“In anticipation of enabling WebAssembly (Wasm) as the default web build target, every JS build now performs a ‘dry run’ compilation to Wasm,” Chisholm wrote. “A series of checks determines the Wasm-readiness of your application, and any findings are emitted to the console as warnings.”

## Google Changes Android App Installation

Google has changed the [Android](https://thenewstack.io/code-anywhere-turn-your-android-tablet-into-a-dev-machine/) app installation process: App installation on certified devices will require verified developers starting in March 2026.

That means developers will need to register and prove their identity regardless of how they’re distributing their app — even through third-party app sources, according to a [report by Techgig](https://content.techgig.com/technology-guide/google-android-app-installation-rules-developer-verification-2026/articleshow/123522363.cms).

[![green Android robot head](https://cdn.thenewstack.io/media/2025/08/b76c67db-android-head_flat.png)](https://cdn.thenewstack.io/media/2025/08/b76c67db-android-head_flat.png)

Image via Google

Google said this new requirement provides an added layer of security.

“Following recent attacks, including those targeting people’s financial data on their phones, we’ve worked to increase developer accountability to prevent abuse,” Suzanne Frey, the vice president of Product, Trust & Growth for Android, wrote on the [Android blog](https://android-developers.googleblog.com/2025/08/elevating-android-security.html). “We’ve seen how malicious actors hide behind anonymity to harm users by impersonating developers and using their brand image to create convincing fake apps.”

It’s a significant problem, she added. Recent analysis by Google found over 50 times more malware from internet-sideloaded sources than on apps available through Google Play, she stated.

A [new developer console](https://support.google.com/android-developer-console/answer/16450960) will support this effort. Android has also published a [guide about the Android developer verification](https://developer.android.com/developer-verification/guides). The open pilot testing will begin in October.

## DigitalOcean Rolls Out MCP Server

Cloud infrastructure developer [DigitalOcean is now offering an MCP](https://www.digitalocean.com/blog/mcp-server-public-release) (Model Context Protocol) server that allows developers to manage cloud resources with natural language prompts through AI-enabled tools.

[MCP is an open source protocol](https://thenewstack.io/mcp-the-missing-link-between-ai-agents-and-apis/) that connects AI systems to external tools, systems and data sources. [Developers can use Claude Code](https://thenewstack.io/claude-code-and-the-art-of-test-driven-development/), Cursor, VS Code, Windsurf, and any other MCP-compatible clients to access the server.

The server can currently access nine services: Accounts, App Platform, Databases, DOKS, Droplets, Insights, Marketplace, Networking, and Spaces Storage.

“Instead of juggling multiple dashboards or tools, you can manage common cloud operations right inside your favorite MCP-compatible tools,” the team wrote.

It also allows developers to “turn plain English into real [API](https://thenewstack.io/generative-ai-creates-apis-faster-than-teams-can-secure-them/) actions.” That means developers can:

* **Deploy and manage apps:** Run commands like deploy a [Ruby on Rails](https://thenewstack.io/dhh-wants-to-make-web-dev-easy-again-with-ruby-on-rails/) app from a [GitHub](https://thenewstack.io/github-loses-its-ceo-and-independence/) repo or check which apps are on the developer’s account.
* **Create and manage databases:** Provision a new PostgreSQL database or create a new database.
* **Work with files:** Upload files from a local directory to a Spaces bucket, create a temporary access key, and get public URLs for files.
* **Check Certificates and Monitoring.**
* **Check the status of an SSL certificate**.
* **Optimize and understand costs**: Get visibility on cloud costs, drill down into monthly app spending, or view a billing history for the last 12 months to understand reasons for higher bills in specific months.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://thenewstack.io/wp-content/uploads/2023/08/4de88b83-4756312a-326a38b7-lorainelawson2-600x600-1-600x600.jpeg)

Loraine Lawson is a veteran technology reporter who has covered technology issues from data integration to security for 25 years. Before joining The New Stack, she served as the editor of the banking technology site Bank Automation News. She has...

Read more from Loraine Lawson](https://thenewstack.io/author/loraine-lawson/)