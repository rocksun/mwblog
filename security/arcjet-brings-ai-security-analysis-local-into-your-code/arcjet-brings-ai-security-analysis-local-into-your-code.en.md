Security platform provider [Arcjet](https://arcjet.com/) today announced the launch of a local [AI model](https://thenewstack.io/frontier-ai-models-now-becoming-available-for-takeout/) that runs [security analysis](https://thenewstack.io/startup-embeds-ai-security-analysis-in-dev-workflow/) directly inside application request handlers. Instead of routing traffic through [cloud-based security](https://thenewstack.io/zero-trust-in-cloud-security-never-trust-always-verify/) services, the model analyzes threats right where the application runs, giving it access to business context that perimeter tools never see.

This is a response to a problem that’s been nagging developers for years: security tools that block legitimate users along with actual threats. Get too aggressive with your rules, and you’re turning away real customers. Too lenient and attacks slip through. For e-commerce sites and [Software as a Service (SaaS) applications](https://thenewstack.io/service-as-software-how-ai-agents-are-transforming-saas/), that trade-off hits the bottom line directly.

“Legacy perimeter solutions see packets, not users or business context,” [David Mytton](https://www.linkedin.com/in/davidmytton), Arcjet’s founder and CEO, told The New Stack. “Our local AI model brings [context-aware security analysis](https://thenewstack.io/why-context-aware-ai-is-quickly-replacing-code-only-tools/) into the request path, where you actually understand what’s happening in your application.”

## Why False Positives Matter

The false positive problem gets worse in the places where security matters most. Block someone at checkout, and you’ve lost a sale. Flag a legitimate signup as suspicious, and you’ve potentially killed a conversion. Traditional security tools operate at the network level, matching patterns against traffic without understanding whether that traffic represents a real customer or a bot, Mytton said.

Arcjet’s model runs after your application’s security rules fire — bot detection, rate limiting, [web application firewall (WAF)](https://thenewstack.io/how-attackers-bypass-commonly-used-web-application-firewalls/) protections — and analyzes the request using machine learning (ML) trained on signals across its platform. Because it runs locally with access to your application state, it can see things like session history, user behavior patterns and business logic that inform whether a request is actually suspicious.

The result is what Arcjet calls a “refined” security recommendation that combines rule-based analysis with learned signals. Developers can inspect both the deterministic rule results and the AI recommendation, then decide in code how to handle each request.

“Arcjet’s AI model combines deterministic rules with learned signals to analyze each request and return a refined recommendation you can act on, in code,” Mytton wrote in a blog post.

## How Developers Use It

The AI model ships as a separate npm package that installs alongside Arcjet’s SDK. Integration is opt-in and straightforward. Here’s what it looks like in a Next.js form handler:

This file contains hidden or bidirectional Unicode text that may be interpreted or compiled differently than what appears below. To review, open the file in an editor that reveals hidden Unicode characters.
[Learn more about bidirectional Unicode characters](https://github.co/hiddenchars)








|  |  |
| --- | --- |
|  | typescript |
|  |  |
|  | const aj = arcjet({ |
|  | key: process.env.ARCJET\_KEY!, |
|  | rules: [ |
|  | detectBot({ mode: "LIVE" }), |
|  | shield({ mode: "LIVE" }), |
|  | ], |
|  | }); |
|  |  |
|  | export async function POST(req: NextRequest) { |
|  | // Run deterministic rules |
|  | const decision = await aj.protect(request); |
|  |  |
|  | // Use the AI model as an additional layer |
|  | const aiDecision = await refine(decision); |
|  |  |
|  | if (aiDecision.isDenied()) { |
|  | return NextResponse.json( |
|  | { error: "Unauthorized" }, |
|  | { status: 403 } |
|  | ); |
|  | } |
|  |  |
|  | // Your form logic here |
|  | } |

The model adds one to two milliseconds of latency — fast enough that it works in real-time request handling. Mytton said the team experimented with [small language models](https://thenewstack.io/should-you-try-small-language-models-for-ai-app-development/) but found they require about half a gigabyte of memory, which isn’t feasible in serverless environments. Instead, they built a lightweight ML model that runs on the CPU with minimal resource requirements.

Because everything runs locally, sensitive data never leaves your production environment, Mytton said. You can test the same security configuration on your laptop that runs in production, which solves a longstanding problem where security tools exist separately from the application being secured.

## Picking Your Battles

Arcjet positions the AI model as one layer in a broader security strategy, not a replacement for existing measures. Developers can choose where to apply AI-powered analysis — maybe just on signup and checkout flows where false positives are most costly, while using faster deterministic rules everywhere else.

The model works alongside Arcjet’s existing features: bot detection, rate limiting, email validation, sensitive information detection and Shield WAF protection. The company is betting that developers want security that integrates into their workflow rather than security that requires managing a separate infrastructure layer.

“Developers aren’t indifferent to security, they just haven’t always had the right tools that speak their language and fit their workflow,” said [Kate Holterhoff](https://www.linkedin.com/in/kateholterhoff/), a senior analyst at RedMonk, in a statement. “Security tools that don’t integrate with modern development workflows simply won’t get used.”

## The Bigger Picture

The approach reflects a broader shift in how security works for modern applications. Bots now outnumber humans online, and AI is making attacks more adaptive and harder to detect with simple pattern matching, Mytton said. Traditional perimeter defenses struggle to keep up.

Mytton said Arcjet is seeing adoption primarily in two scenarios: user signups, where blocking legitimate users damages growth, and e-commerce, where false positives directly cost revenue. One early user customer reduced serverless costs by 66% by blocking scrapers at the application layer instead of processing their requests.

Arcjet has about 1,000 developers using its technology across more than 500 production applications. The company has a 10-person team with engineers spread across Phoenix, San Francisco, Philadelphia and New York. Mytton recently moved from London to New York and is planning to open an office in Manhattan’s Flatiron District.

The local AI model will roll out as a preview to Arcjet customers. The platform currently supports [JavaScript](https://thenewstack.io/introduction-to-javascript/) applications on [Node.js](https://thenewstack.io/node-js-22-release-improves-developer-experience/), [Bun](https://thenewstack.io/node-removes-corepack-bun-runs-native-c-from-javascript/) and [Deno](https://thenewstack.io/denos-response-to-nodes-recent-support-for-typescript/), with framework support for [Next.js](https://thenewstack.io/next-js-deployment-spec-simplifies-frontend-hosting/), [Remix](https://thenewstack.io/remix-takes-on-next-js-in-battle-of-the-react-frameworks/), [SvelteKit](https://thenewstack.io/rich-harris-talks-sveltekit-and-whats-next-for-svelte/) and others, Mytton said.

Mytton’s vision is an interesting bet on where application security is headed. Instead of routing everything through centralized security infrastructure, Arcjet is arguing that security works better when it lives close to the code — where you understand what your application is doing and can make informed decisions about what to block and what to allow.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://thenewstack.io/wp-content/uploads/2021/06/a95bb5bc-image-576x600.png)

Darryl K. Taft covers DevOps, software development tools and developer-related issues from his office in the Baltimore area. He has more than 25 years of experience in the business and is always looking for the next scoop. He has worked...

Read more from Darryl K. Taft](https://thenewstack.io/author/darryl-taft/)