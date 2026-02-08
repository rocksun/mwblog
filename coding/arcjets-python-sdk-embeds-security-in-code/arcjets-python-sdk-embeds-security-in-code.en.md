Security platform provider [Arcjet](https://arcjet.com/) has launched a [Python](https://thenewstack.io/what-is-python/) SDK to bring application-layer security directly into code.

The SDK, now in beta, extends Arcjet’s security platform to Python-based services and APIs to meet customer demand and AI-driven Python growth, said Arcjet Founder and CEO [David Mytton](https://www.linkedin.com/in/davidmytton/).

“We started with the [JavaScript](https://thenewstack.io/introduction-to-javascript/) ecosystem, because that’s where most new applications are being built with full stack development,” he told The New Stack. The company started with support for both JavaScript and [TypeScript](https://thenewstack.io/what-is-typescript/) applications.

However, “With the Python SDK, we’re extending Arcjet’s application-layer approach to one of the largest developer ecosystems in the world,” Mytton said in a statement. “Teams rely on Python for critical services, from public APIs to internal systems. This release gives developers a clear way to apply meaningful security controls directly in code without introducing operational overhead.”

Arcjet received a lot of requests for support for additional languages, with Python being the most popular.

The [Django](https://thenewstack.io/what-is-pythons-django/) Python framework “is a particular driver of this, given its popularity for web applications and APIs, but AI use cases have accelerated Python’s popularity,” Mytton wrote.

## Python Security Needs

Indeed, Python security is increasingly relevant as AI development drives Python adoption.

Earlier this week, [Anthropic](https://www.anthropic.com/), a leading AI research and products company, invested $1.5 million in the [Python Software Foundation](https://www.python.org/psf-landing/) (PSF). The investment will support the foundation overall, with a particular focus on [Python ecosystem security](https://thenewstack.io/whos-keeping-the-python-ecosystem-safe/).

Anthropic’s funds will enable the PSF to make progress on its security roadmap, including work designed to protect millions of [PyPI](https://thenewstack.io/compiled-python-code-used-in-a-new-pypi-attack/) users from attempted supply chain attacks, the foundation said.

Python is widely used for backend services and APIs — especially for AI applications — but most security tools operate at the network or edge layer, Mytton said. Arcjet brings security decisions into application code where developers have full access to request context and business logic, making protections more accurate and easier to manage, he explained.

Overall, the Arcjet Python SDK supports application-layer protections, including rate limiting, bot detection, email validation and signup spam prevention, Mytton said in the blog. These protections are evaluated using Arcjet’s contextual decision engine and applied as part of normal request handling, allowing teams to tailor behavior based on user activity, request patterns and application-specific signals.

The Arcjet SDK provides building blocks so security becomes just another feature, regardless of the deployment environment.

## WebAssembly Component

Arcjet’s approach involves embedding a [WebAssembly (Wasm)](https://thenewstack.io/webassembly/) module in its SDK, allowing for local analysis of incoming requests at near-native speed.

The Wasm module is compiled from [Rust](https://thenewstack.io/rust-growing-fastest-but-javascript-reigns-supreme/) and provides a secure sandbox for analysis, which is cross-platform and has now been extended to another language beyond [JavaScript](https://thenewstack.io/web-app-development-sans-javascript-with-microsoft-blazor/), Mytton said.

“The first version of the Python SDK is framework-ready for us to insert the WebAssembly bits into it so that we can do all the local analysis that we’ve been doing on the JavaScript side of things,” he said.

Furthermore, “Wasmtime allows us to execute WebAssembly inside Python,” Mytton explained. Wasmtime is an open source WebAssembly runtime hosted by the [Bytecode Alliance](https://thenewstack.io/webassembly-to-let-developers-combine-languages/) and designed for use either as part of a larger stack or as a standalone runtime.

Just like Arcjet’s JavaScript SDK, the Python SDK uses WebAssembly for local security analysis. This is currently in test/beta phase, but it enables them to run their security analysis locally rather than just using an API client.

In addition, the Python SDK supports both [FastAPI](https://github.com/arcjet/example-fastapi?ref=blog.arcjet.com)-style (asynchronous) and [Flask](https://github.com/arcjet/example-flask?ref=blog.arcjet.com)-style (synchronous) APIs. Arcjet has example applications for both FastAPI and Flask.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://thenewstack.io/wp-content/uploads/2021/06/a95bb5bc-image-576x600.png)

Darryl K. Taft covers DevOps, software development tools and developer-related issues from his office in the Baltimore area. He has more than 25 years of experience in the business and is always looking for the next scoop. He has worked...

Read more from Darryl K. Taft](https://thenewstack.io/author/darryl-taft/)