With 60+ million weekly downloads, [JSON Schema](https://json-schema.org/) is one of the most widely used standards for describing data — but that doesn’t necessarily make it a crowd pleaser. With dense specifications and a steep learning curve, the standard is notoriously cumbersome, intricate, and difficult to use for both large-scale Fortune 100 companies and independent developers working on side projects.

[Sourcemeta](https://www.sourcemeta.com/) is hoping to lower the barrier to entry and create an overall better, more intuitive developer experience for [JSON Schema](https://thenewstack.io/an-introduction-to-json/) with its self-hosted registry. A bootstrapped, self-funded start-up, Sourcemeta is led by a member of the JSON Schema Technical Steering Committee, [Juan Cruz Viotti](https://www.linkedin.com/in/jviotti/), who’s confident he can reshape the entire ecosystem.

Viotti pointed out that he understands developers’ struggles firsthand because he used to be one of them: “It all started with me trying to scratch my own itch. I entered the JSON Schema ecosystem as just another user, trying to get stuff done and getting very frustrated with the current status quo.”

## Troubles With the Status Quo

In Viotti’s eyes, the status quo is failing on two fronts: poor education and a lack of mature tooling.

“Historically, documentation for JSON Schema has been pretty terrible,” he says. Learning the standard requires an enormous amount of dense specification reading, which, unsurprisingly, few manage to slog their way through. “That mean[s] JSON Schema literacy for anything beyond the trivial is something almost nobody has,” he explains.

Unwieldy documentation and subpar educational resources are just part of the problem. Even developers well-versed in the intricacies of the standard, once thrown into the full JSON Schema ecosystem, are met with a startling lack of tooling, e.g., there’s no easy way for testing schemas, debugging complex schemas, linting schemas to enforce best practices, etc. According to Viotti, “Those things either didn’t exist, or some tools tried to do it but either are not very spec-compliant and miss lots of things beyond the trivial or are just plain wrong.”

There lies yet another problem waiting for developers as they grapple with JSON Schema: Compliance. For Viotti, this is one of the most significant roadblocks keeping developers and organizations from succeeding with JSON Schema — and one of the major ways Sourcemeta aims to help developers.

“All of the tooling at Sourcemeta is 100% spec-compliant, down to all the very nitty gritties,” says Viotti, also calling out Sourcemeta’s [Blaze](https://arxiv.org/abs/2503.02770) as the world’s fastest JSON Schema validator that is at least 10x faster than any of the other competitors, while being 100% spec-compliant. This is noticeably more advanced than other schema validators, which Viotti says are largely no-spec-compliant — and thus the source of many developers’ troubles: “A lot of people rely on these broken implementations and get utterly confused, as what they read about JSON Schema doesn’t seem to be what they see, and many schema they end up creating are incompatible with everything else.”

Beyond compliance, Sourcemeta is promising to help with discoverability and reusability, i.e., making it easier for developers to browse, search, and reuse diverse data models, no matter which version of JSON Schema they’re working with.

Essentially, the start-up is slowly ingesting all open source JSON Schema data models in one easily accessible, searchable place, enabling developers to use them with any version of the standard. It promises to pack a powerful punch, cutting down repetitive work and reducing friction to eliminate the complexity of operating schemas at scale.

## How Most Organizations Approach JSON Schema Today

If the JSON Schema universe is as messy as Viotti purports, it may be curious why no one else has taken a crack at bringing order to the chaos. But Viotti says it’s simply been too difficult.

Unfortunately, this has left most companies floundering without direction when it comes to JSON Schema management. Or in Viotti’s words: “Most of them are reinventing the wheel every single time.”

He claims this is true no matter who you are, from independent developers to large-scale enterprises in fintech, energy, etc. And reinventing the wheel isn’t cheap. In fact, Viotti claims that in his experience, he sees the average API company waste $200,000 a year on simple, [schema-related issues](https://thenewstack.io/debunking-the-myth-of-going-schemaless/): “They are trying so hard and spending so much money… building internal tooling on their own, recreating everything on their own. It’s a huge amount of investment.”

A huge amount of investment for what’s still a huge headache.

With so many organizations and developers falling victim to the same JSON Schema management problems, including himself, Viotti decided it was time to change the dynamic — but he didn’t get there right away. “It took me many years of getting down into the rabbit hole… of learning way too many things about JSON Schema… to now be in a position where I can actually serve a wider audience.”  And Viotti claims that what he’s come up with is different than anything else on the market.

## Reimagining the Ecosystem for a Better Dev Experience

Compliance is, of course, one of Sourcemeta’s major breakthroughs: “You can trust that any processing that you do with JSON Schema with Sourcemeta tooling is actually going to give you the right response,” Viotti affirmed.

What also makes the start-up stand out is its [GitOps-first approach](https://thenewstack.io/7-major-gaps-in-todays-gitops-tools/), which allows developers to easily deploy the registry from one or more GitHub schema repositories for greater scalability and consistency across environments.

There are other goodies to come, like health monitoring and an advanced schema playground, but bottom line, Viotti says the main goal of Sourcemeta is to improve the developer experience:

“It’s very developer-oriented. We’re trying to fix all of these little mechanics of using JSON Schema in production, these little annoyances… One by one, we’re trying to solve them all. And together, they make for a huge difference in the developer experience.”

So far, developers are taking to the tools. Many, in fact, flock to the site for its reference documentation, video courses, and other training content, without even knowing there’s a dedicated company behind it. Viotti says this isn’t a surprise, because at the end of the day, the biggest obstacles with JSON Schema management all come down to education — or a lack thereof: “A lot of people are very eager to know more about JSON Schema…, but they cannot find a way to actually do it properly. [Sourcemeta] is where you can actually get the resources to get started.”

Beyond the free educational content, Sourcemeta provides software licenses and private training to help organizations tackle their specific JSON Schema management woes. Eventually, Viotti plans to offer an off-the-shelf product that simplifies this problem-solving.

“We are literally trying to fix the entire [JSON Schema] ecosystem,” says Viotti — a lofty goal, but one that the industry certainly needs.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.