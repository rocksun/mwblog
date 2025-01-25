# Tailwind CSS Gets a ‘Ground-Up Rewrite’ for Version 4.0
![Featued image for: Tailwind CSS Gets a ‘Ground-Up Rewrite’ for Version 4.0](https://cdn.thenewstack.io/media/2024/04/d8b458d6-dev_news_img-2-2-1024x577.png)
“Holy shit it’s actually done — we just tagged [Tailwind CSS v4.0](https://tailwindcss.com/blog/tailwindcss-v4),” Tailwind CSS creator [Adam Wathan](https://www.linkedin.com/in/adam-wathan-9418984a/?originalSubdomain=ca) wrote Tuesday.

It’s an understandable reaction, when you consider that this release is a ground-up rewrite of the framework. The Tailwind team took “everything we’ve learned about the architecture over the years and optimizing it to be as fast as possible,” Wathan wrote.

First, there’s the new Rust-powered performance engine — called [Oxide](https://tailwindcss.com/blog/tailwindcss-v4-alpha) at one point — that was incorporated into this release. It makes both full and incremental builds faster, according to Wathan.

“When benchmarking it on our own projects, we’ve found full rebuilds to be over 3.5x faster, and incremental builds to be over 8x faster,” he wrote. “The most impressive improvement is on incremental builds that don’t actually need to compile any new [CSS](https://thenewstack.io/css-in-js-and-react-server-components-a-developer-guide/) — these builds are over 100x faster and complete in microseconds.”

But that’s not all. Wathan notes that [Tailwind CSS](https://thenewstack.io/tailwind-css-for-developers-style-without-using-css-code/) v4.0 also incorporates cutting-edge CSS features, such as:

- Native cascade layers, which he says provides more control over how different style rules interact with each other;
- Registered custom properties, which makes possible things like animate gradients, but also improves performance significantly on large pages;
- color-mix(), which lets developers adjust the opacity of any color value, including CSS variables and currentColor; and
- Logical properties that simplify RTL support and reduce the size of generated CSS.
Medium frontend writer [Xiuer Old](https://xiuerold.medium.com/about) was one of many frontend devs who offered a [positive review of the new release](https://xiuerold.medium.com/tailwind-css-4-0-is-here-whats-new-and-why-it-matters-580849f70820).

“Tailwind CSS 4.0 isn’t just an update — it’s a reimagining of what a CSS framework can be,” Old wrote. “By blending raw performance with modern CSS capabilities and a frictionless setup, it empowers [developers to build faster](https://thenewstack.io/newly-stable-next-js-compiler-faster-supports-larger-builds/) and more creatively.”

## 16% of Orgs Have Standardized Developer Environment
Seventy-nine percent of more than 550 software professionals surveyed use a fully managed cloud-hosted developer environment, according to the [SlashData for Coder’s State of Development Environments 2025](https://coder.com/blog/insights-and-key-findings-from-the-state-of-development-environments-2025-report) report. Yet, the same study found that 84% of respondents said their organization does not rely on one standardized development environment tool.

The disconnect is because choices about what developer environment to use are sometimes made at the organizational level, while at other times, decisions occur at the team or individual level.

Still, a majority of organizations do have common development workflows or standards.

All study participants worked at large companies (either 100 developers or 1,000 employees) that either used or provided development environments. Notably, only 27% are primarily in a developer role, while the rest were in IT leadership and management roles.

Only 36% of these developers said their organization allows [developers to have full control](https://thenewstack.io/ambassador-labs-combats-tool-sprawl-with-developer-control-plane/) over their development environments.

By comparison, 52% of the administrators/leaders reported that they were in full control of their development environments. Furthermore, administrators are more likely to be positive about their environment’s governance and configurations.

Only 36% of these developers said their organization allows

[developers to have full control]over their development environments.
Currently, only 13% are able to independently create a new [environment with an automated](https://thenewstack.io/gitpod-brings-automated-environments-to-jetbrains-ides/) system. While others have standardized processors to independently create a new environment, 45% must get prior approval from a manager or IT or at least coordinate with another team/department beforehand.

Looking towards the future, a full 78% of study participants plan to work on more standardization of developer environments in the next year. Overall, 42% of these organizations expect to rely on internal [platform or DevOps](https://thenewstack.io/how-platform-engineering-helps-manage-innovation-responsibly/) teams for this standardization.

[Lawrence Hecht](https://thenewstack.io/author/lawrence-hecht/), a research analyst with The New Stack, predicted that developers may be less than thrilled with the progress of these efforts if they continue to have a significantly different outlook than the professionals they rely on to manage and provision these environments.
## Bun 1.2 Called ‘Huge Update’
[Bun released version 1.2](https://bun.sh/blog/bun-v1.2), which Ashcon Partovi, a product manager at Bun, called a “huge update.”
Bun is designed to be a drop-in replacement for [Node.js](https://thenewstack.io/whats-in-the-new-node-js-and-how-do-you-install-it/), but that’s not as easy as it sounds. In a blog post, Partovi outlines how they prioritized and fixed Node.js bugs. With Bun 1.2, they decided to run the Node.js test suite for every change made to Bun.

“Since then, we’ve fixed thousands of bugs and the following Node.js modules now pass over 90% of their tests with Bun,” Partovi wrote.

Bun 1.2 also adds built-in support for [S3](https://cloudian.com/blog/s3-storage-behind-the-scenes/#:~:text=Amazon%20Simple%20Storage%20Service%20(S3,and%20the%20powerful%20S3%20API.), the de facto standard for object storage in the cloud. This support allows developers to read, write and delete files from an S3 bucket using APIs that are compatible with Web standards such as Blob.

There’s also a built-in Postgres client: `Bun.sql`
. MySQL is coming soon, Partovi added.

`bun install`
now uses a text-based lockfile: bun.lock and Express is three times faster in Bun, Partovi noted.
## JavaScript Temporal Sees Experimental Browser Releases
Working with dates in JavaScript can be “hugely simplified and modernized” by browser implementations of the new JavaScript Temporal object, according to [Brian Smith](https://www.linkedin.com/in/bsmth/?originalSubdomain=de), a staff technical writer on the MDN Web Docs team at Mozilla.

[Smith explored the JavaScript Temporal object](https://developer.mozilla.org/en-US/blog/javascript-temporal-is-coming/) in a recent article. First, he explained the role of JavaScript’s `Data`
object, which goes back to the beginning of JavaScript and was copied from Java’s early flawed `java.until.Date`
implementation, he wrote.
“Java replaced this implementation in 1997, but JavaScript is stuck with the same API for almost 30 years, despite known problems,” Smith explained.

“Temporal adds support for time zone and calendar representations, many built-in methods for conversions, comparisons and computations, formatting, and more.”

– Brian Smith, staff technical writer, Mozilla MDN Web Docs
The big issue with this approach is that it only supports the user’s local time and UTC, so there is no time zone support.

“Additionally, its parsing behavior is very unreliable, and Date itself is mutable, which can introduce hard-to-trace bugs,” he wrote. “There are other problems like calculations across Daylight Saving Time (DST) and historical calendar changes, which are notoriously difficult to work with.”

All of which makes it kind of a headache to work with, leaving developers to rely on libraries like Moment.js and date-fns to handle dates and times in applications, he concluded.

Temporal replaces the [Data object](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Date) and it does so in a way that makes date and time management reliable and predictable.

“Temporal adds support for time zone and calendar representations, many built-in methods for conversions, comparisons and computations, formatting, and more,” he wrote. “The API surface has over 200 utility methods, and you can find information about all of them in the [Temporal docs on MDN](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Temporal).”

In the remainder of the article, he explained more about how Temporal object works with code examples and explored browser support.

[
YOUTUBE.COM/THENEWSTACK
Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.
](https://youtube.com/thenewstack?sub_confirmation=1)