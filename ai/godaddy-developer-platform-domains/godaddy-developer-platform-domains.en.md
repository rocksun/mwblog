On Wednesday, GoDaddy launched its [new developer platform](https://developer.godaddy.com/), giving developers a way to manage domains without leaving their development environment. Domain management has become a core part of the deployment process — shifting into CI/CD pipelines and Infrastructure as Code — and GoDaddy’s platform is designed to work inside existing development workflows.

GoDaddy built its business serving consumers and small businesses, but the Developer Platform is aimed at a different audience. The company is making a play for engineering teams that want to manage domains through code and skip the web dashboard.

> AI is fundamentally changing how software is created, and the infrastructure behind the internet has to evolve with it.

## Bringing domain management into developer workflows

Developers can already use AI tools to help build a website, but setting up the domain still usually requires leaving the coding environment and handling it through a registrar.

“AI is fundamentally changing how software is created, and the infrastructure behind the internet has to evolve with it,” said Travis Muhlestein, chief technology officer of product AI at GoDaddy. “Our Developer Platform now connects GoDaddy domain services directly into developer tools, giving our customers, whether they have one domain or thousands, the ability to complete the entire domain lifecycle. The result is faster domain search, purchase, and configuration – going from idea to a live online presence in minutes.”

## Competing with cloud DNS providers

Many engineering teams already manage domains through APIs rather than registrar dashboards. AWS Route 53, Cloudflare, and Vercel all support that approach. Route 53 and [Cloudflare](https://thenewstack.io/cloudflare-ai-web-economics/) offer mature DNS APIs but function primarily as infrastructure and CDN providers — teams use them to manage records and routing for domains they’ve registered elsewhere. Vercel handles domain configuration as part of its deployment abstraction, so developers rarely interact with DNS directly. GoDaddy is trying to bring that same experience to its own registrar by allowing domain management to happen alongside the rest of the development process, including work performed by AI coding assistants. The difference is that GoDaddy is making the registration and purchasing sides programmable and going beyond the DNS layer.

> The difference is that GoDaddy is making the registration and purchasing sides programmable and going beyond the DNS layer.

## Programmable domain purchase safeguards

The new range of capabilities includes a set of domain APIs that let developers search for available domains, retrieve pricing, purchase domain names, configure DNS settings, and manage registrations without leaving their applications or workflows.

The new v3 Domains API uses a quote-then-execute model for purchases. The short-lived token locks in the price, an idempotency key prevents duplicate charges, and a consent object ties every registration to human approval. These are needed when purchases are initiated by automated or AI agents rather than by a human clicking through a checkout page.

> A consent object ties every registration to human approval. These are needed when purchases are initiated by automated or AI agents rather than by a human clicking through a checkout page.

## OAuth scoping for AI agents

The platform also incorporates OAuth-based authentication, which allows developers to grant AI agents access only to the specific resources they require. To maintain user control, GoDaddy has built-in safeguards such as scoped permissions and approval flows for irreversible actions.

## CLI and LLM-optimized documentation

The release also includes a new CLI for developers who prefer working from the command line. GoDaddy updated its developer portal, adding guided onboarding and documentation designed for both human developers and AI coding assistants.

At launch, the platform handles the day-to-day work of managing domains, from registration and DNS changes to renewals and redirects. The company says it’s aimed at developers as well as organizations responsible for large numbers of domains.

While the free beta release focuses on core domain operations, more features are planned. Future updates are expected to add deeper support for domain investors, reseller workflows, larger bulk operations, and tighter integration with other GoDaddy services. Separately, GoDaddy is co-authoring an IETF draft for Agent Name Service (ANS), an open standard for AI agent identity and verification built on DNS and public key infrastructure. For engineering teams, the larger shift may be that domains are beginning to look like another [programmable component of application infrastructure](https://thenewstack.io/safari-mcp-platform-infrastructure/).

The platform is available now. Developers already using GoDaddy’s existing APIs don’t need to change anything immediately, but they can move to the new platform when they’re ready.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://thenewstack.io/wp-content/uploads/2026/06/c176528b-cropped-54a705ce-amandacaswellheadshot_4-600x600.jpeg)

Amanda Caswell is an AI journalist, certified prompt engineer, and technology commentator whose work and expertise have been featured on Fox News and CBS News. She covers artificial intelligence, developer tools, foundation models, and emerging technologies, with a particular focus...

Read more from Amanda Caswell](https://thenewstack.io/author/amanda-caswell/)