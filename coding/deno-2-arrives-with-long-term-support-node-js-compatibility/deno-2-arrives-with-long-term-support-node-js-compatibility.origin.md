# Deno 2 Arrives With Long-Term Support, npm Compatibility
![Featued image for: Deno 2 Arrives With Long-Term Support, npm Compatibility](https://cdn.thenewstack.io/media/2022/08/caa9cb24-deno.jpg)
Ryan Dahl freed JavaScript from web browsers when he created the Node.js runtime — then expanded the ecosystem even more with Node’s package manager npm. After that came the improved [Deno runtime](https://thenewstack.io/denos-ryan-dahl-is-an-asynchronous-guy/) for JavaScript and TypeScript, to be followed soon by the release of a major-version upgrade — Deno 2.0.

[Andy Jiang](https://www.linkedin.com/in/andyjiang/), Deno’s product marketing manager, tells us “We’re aiming for early October” for the (hopeful) official release date of Deno 2. And Deno creator Ryan Dahl has been marking the upcoming milestone by appearing [on](https://www.youtube.com/watch?v=tZBCq8Ijkgw) [four](https://topenddevs.com/podcasts/javascript-jabber/episodes/unpacking-deno-2-code-stability-free-speech-and-more-jsj-648#player1?catid=0&trackid=0) [different](https://stackoverflow.blog/2024/08/20/ryan-dahl-deno-20-scale-improve-npm-nodejs/) [podcasts](https://podrocket.logrocket.com/deno-2-ryan-dahl) (and in a short [Honeypot documentary](https://www.youtube.com/watch?v=zxitJn9MwYs)).
But Dahl is not just talking about the big changes coming to Deno runtime, but where it fits into the larger story of JavaScript — and the web itself.

[On the “JavaScript Jabber” podcast](https://topenddevs.com/podcasts/javascript-jabber/episodes/unpacking-deno-2-code-stability-free-speech-and-more-jsj-648#player1?catid=0&trackid=0), Dahl stressed that Deno 2, due to be released in early October, is to “make sure it scales up to projects that have 100,000 lines of JavaScript.” Then he ticked through the major new features. . “That includes the npm support, that includes the JavaScript Registry, that means the long-term support and Workspaces — all kind of factor into this scaling up of Deno.”
Deno 2 release candidates started arriving at the end of August, and at about the same time, Bartek Iwanczuk, the lead of Deno’s CLI team [posted](https://www.twitter.com/biwanczuk/status/1829311165001789538) that Deno had its last pre-version 2 release.

## Importing npm Modules
“It’s become pretty clear over the last couple of years that there are a lot of npm packages that people just need to use,” Dahl said in [an interview on the Syntax podcast](https://www.youtube.com/watch?v=tZBCq8Ijkgw).

So Deno 2 will support the importing of [npm packages](https://thenewstack.io/npm-to-adopt-sigstore-for-software-supply-chain-security/).

Dahl calls it “a really large undertaking… We’ve been working on this for essentially two years now”

But he also says they’ve got to a point where “Most npm packages are working out of the box in Deno. But in particular, frameworks… including very complex frameworks like [Next.js](https://en.wikipedia.org/wiki/Next.js) that have build processes and all sorts of stuff. So yeah, you should be able to just run these things in your next project, once we get to Deno 2.”

While Deno uses [HTTP-based import statements](https://deno.com/blog/http-imports), Deno 2 brings “the ability to have a URL that points to an npm module and be able to pull that in…” Dahl said [on the Stack Overflow podcast](https://stackoverflow.blog/2024/08/20/ryan-dahl-deno-20-scale-improve-npm-nodejs/).

“Because it turns out a lot of the JavaScript ecosystem depends heavily on that,” he said

![Arsenii Gorushkin mocks Deno 2 in YouTube comment](https://cdn.thenewstack.io/media/2024/09/93c15fe4-arsenii-gorushkin-mocks-deno-2-in-youtube-comment.png)
In the comments on a Deno 2 announcement video, backend web developer [Arsenii Gorushkin](https://github.com/agorushkin) — also an avid lover of Deno — shared some skepticism.

On the “JavaScript Jabber” podcast, Dahl stresses that “The level of compatibility is fantastic,” between npm and Deno.

“There’s always going to be a ‘long tail’ of incompatibilities, and we consider any module that we can’t run a bug, and we will fix it. But it’s really, really good these days.”

For example, Deno can even import Node modules that have their own compiled extension modules. “It goes very deep… Essentially anything that you pull in should work, out of the box, in Deno these days….

“I would encourage people to try it. You will be shocked.”

In June Deno also began duplicating npm’s popular [Workspace feature](https://docs.deno.com/runtime/fundamentals/workspaces/), which lets developers manage and sync several interdependent packages in one repository. “We support npm workspaces as well as our own form of npm Workspaces,” Dahl said on the Syntax podcast.

This should also make it easier for developers to make the jump from Node to Deno. Citing workspaces but also its general performance, Dahl said [on the PodRocket podcast](https://podrocket.logrocket.com/deno-2-ryan-dahl). “If people try it out, I guarantee you will be shocked at how nice it is.”

## Long-Term Support
Again and again, Dahl has been making the case that Deno is coming of age.

On the PodRocket podcast, Dahl also cited the arrival of Long-Term-Support for Deno, with backported security fixes and promises of API stability, calling this “another way that helps people adopt Deno and use it in more situations. Because if you don’t have stability guarantees, you can’t really use it in certain enterprise settings.”

“We’ve been working on Deno for a while,” Dahl said on the Syntax podcast. “It is stable now, Basically, Deno 2 is kind of our our marker that Deno is ready for production, ready for use cases..”

## The Future of JavaScript
Dahl acknowledged the JavaScript community has a [long-standing proposal](https://blog.logrocket.com/types-as-comments-strong-types-weakly-held/) to make type annotations a valid JavaScript syntax even if they’re ignored by the JavaScript engine (an idea sometimes called “types as comments”). Dahl says that while the proposal isn’t fully formed, he believes it’s “the direction that JavaScript will be going” — maybe ultimately being supported in Google’s V8 JavaScript engine.

“And so I would imagine five years from now, Chrome executes TypeScript natively because it just can do the type-stripping inside of V8 itself. Which would be beautiful.”

But perhaps Dahl’s most succinct pronouncement came on the Syntax podcast. “I just have this theory that JavaScript is here for the long run and that this isn’t, like, a two-year sort of thing. This is like a 20-year sort of thing, because software infrastructure relies so heavily on the browser. And so I just think it’s really important for us to think long-term about where we’re going with this thing…

“We’re building Deno for the future.”

[
YOUTUBE.COM/THENEWSTACK
Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.
](https://youtube.com/thenewstack?sub_confirmation=1)