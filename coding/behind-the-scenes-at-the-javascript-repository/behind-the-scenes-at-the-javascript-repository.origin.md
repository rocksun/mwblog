# Behind the Scenes at the JavaScript Registry
![Featued image for: Behind the Scenes at the JavaScript Registry](https://cdn.thenewstack.io/media/2024/10/80113a3b-jsr-1024x683-1.jpg)
Today, I learned if you rotate the JSR logo upside-down (see above) — it looks exactly the same

Since its public beta in March, [the JavaScript Registry](https://jsr.io/) (JSR) has been sharing tips, insights, and general goodwill for its community of curious developers on podcasts, in blog posts, and in comments around the web.

“Package authors who published to JSR loved the experience,” said [Andy Jiang](https://theorg.com/org/deno/org-chart/andy-jiang), [Deno](https://thenewstack.io/deno-2-arrives-with-long-term-support-node-js-compatibility/)’s product marketing manager, in an email interview with The New Stack. “JSR handles a ton behind the scenes so authors can publish TypeScript source code without needing a transpile or build step.”

The open source site is part of an ambitious plan to build a better package repository for [JavaScript](https://thenewstack.io/JavaScript/) (and for [TypeScript](https://thenewstack.io/TypeScript/)), supporting features like type declaration files and offering an easy way to give packages cryptographic signatures. And yes, while it’s focused on JavaScript (and TypeScript), the JSR supports only ES modules. In a [spring interview](https://the-stack-overflow-podcast.simplecast.com/episodes/why-the-creator-of-nodejs-created-a-new-javascript-runtime/) with Stack Overflow, [Ryan Dahl](https://thenewstack.io/denos-ryan-dahl-is-an-asynchronous-guy/) pointed out that [ECMAScript](https://thenewstack.io/inside-ecmascript-javascript-standard-gets-an-extra-stage/) is “now kind of embedded into all of the web browsers, the real way of doing modules.” Or, as the repository’s [FAQ](https://jsr.io/docs/why) explains, “ECMAScript modules have arrived as a standard.

## A Modern Registry
“A modern registry should be designed with TypeScript in mind.”

But modern JavaScript is still welcome. “While we did want to design for TypeScript from the outset, you can definitely happily write and publish plain JavaScript code on JSR,” Deno’s developer relations head [Kevin Whinnery](https://www.linkedin.com/in/kevinwhinnery/), posted in March [on Hacker News](https://news.ycombinator.com/item?id=39563688). (Whinnery added at the time that, “We probably need to do a better job explaining and featuring this,” and the JSR’s home page now proudly announces that it’s a package registry “for modern JavaScript and TypeScript”.)

It’s all part of the ongoing outreach effort to familiarize developers with lots of details about the new registry — and hopefully, even encourage them to give it a try

## Secure By Default
On Deno’s blog, an [April post](https://deno.com/blog/how-we-built-jsr) titled “How We Built JSR” explained some of the site’s internals, including the fact that it’s “secure-by-default, supporting token-less publishing from GitHub Actions and package provenance using Sigstore.”

An earlier [blog post in March](https://deno.com/blog/jsr_open_beta) included instructions on linking GitHub repositories to JSR. “Publishing this way also gives your users peace of mind that the artifact they’re including in their project was indeed uploaded from CI, with a provenance transparency log available for viewing.”

As Dahl said [on Stack Overflow’s podcast](https://thenewstack.io/ryan-dahl-from-node-js-and-deno-to-the-modern-jsr-registry/) back in March, “At the end of the day, you’re going to take a number of dependencies and build your microservice and then run that as a Docker container in some Kubernetes infrastructure. And it would be very nice… to be able to say all software running inside this Docker container has attestations that trace it all the way back to a verified user somewhere and that there is no code that is running here that we don’t know where it came from. We’re kind of building up the infrastructure for this.”

The April blog post explained how they’d had to build not just a robust way to host packages, but also to accept and analyze new packages for invalid dependencies or syntax errors (and to calculate a score to display for the packages — and generate documentation).

## Up in the Cloud
But that blog post also included some fun details how they’ve architected their infrastructure. Most data is stored on a Postgres cluster, accessed using JSON over an HTTP REST API.

Written in [Rust](https://thenewstack.io/rusts-rapid-rise-foundation-fuels-language-growth/), the API server sits next to the database on [Google Cloud Run](https://cloud.google.com/?utm_content=inline+mention), where it also “enforces authentication and authorization policies,” talking to the GitHub API and to Sigstore..

On Stack Overflow’s podcast, Ryan Dahl emphasized that it’s “designed to be able to run very cheaply on commodity cloud software.” As the [FAQ](https://jsr.io/docs/faq) puts it, “Currently hosting bills for JSR are paid for by the Deno Company. In the future, JSR may be funded by alternative means, like sponsorships, donations, or a foundation.”

“We expect that the Deno Company will be able to continue paying for JSR’s hosting bills for the foreseeable future — JSR is designed to be very cheap to run.”

As Dahl said on the podcast, “We’re trying to build an institution here for the future of JavaScript.”

“[T]here is no magic,” the blog post acknowledges. “We use incredibly boring, very well understood, and very reliable cloud infrastructure.” A Google Cloud L7 load-balancer routes requests appropriately — to the frontend, the API server, or to the Google Cloud CDN backend hosting the source code and npm tarballs. “So how do we make serving modules reliable? We defer the entire problem to Google Cloud. The same infrastructure that serves google.com and YouTube is used to host modules on JSR….

“Only if Google itself goes down, will JSR come down too. But at that point — probably half the internet is down so you don’t even notice.”

That April blog post also detailed the specifics of their web front end. (Because “If you’re writing a service for humans to use, you discover pretty quickly that most humans do not in fact want to manually invoke API calls using curl.”) They built it with Fresh (which they describe as “a modern ‘server-side render first’ web framework), carefully optimizing it for fast responses by “parallelizing” many API calls to run at the same time.

## How Packages Are Published
The end result is surprisingly performant. The publishing script bundles files into a .tar.gz file, triggering the API server to perform its own validations (like checking that the tarball is [smaller than 20 megabytes](https://jsr.io/docs/quotas-and-limits#other-limits)). And according to the blog post, background workers start on 99% of those tarballs in under 30 milliseconds, validating that there are fields for “name,” “version,” and “exports.” For most packages, the existence of all imported modules is also verified (along with the validity of the TypeScript of JavaScript code) within 10 milliseconds.

An auto-generated module graph is then used to create documentation using TypeScript syntax analysis in Rust.

During the service’s public beta, a [March blog post](https://deno.com/blog/jsr_open_beta) explained to prospective users that “Once you’ve found the right module, installation and usage instructions can be found on the top of every page in the module’s automatically-generated API reference documentation.”

At some point, the service even generates a tarball for the JSR’s npm compatibility layer, creating “imports that node_modules/ resolution understands” (by transforming TypeScript source code into a .js file and .d.ts declaration file), “along with a package.json.”

And there may be more features to come, according to a comment by Deno’s developer relations head [Kevin Whinnery](https://www.linkedin.com/in/kevinwhinnery/), who posted in March [on Hacker News](https://news.ycombinator.com/item?id=39561988). “We’ve also been exploring how to create a good developer experience around simultaneously publishing JSR modules to npm, so publishers can control their namespace there as well. We definitely know it’s a usage pattern folks are interested in.”

And then, of course, the Postgres database is updated…

## About That Frontend
A new [blog post last week](https://deno.com/blog/designing-jsr) looks back to where it all came from. In the post, product design lead [John Donmoyer](http://linkedin.com/in/johndonmoyer) points out that in addition to everything else, the JSR is open source. So besides “tens of thousands” of packages added to the registry, “we’ve been thrilled to see the community embrace JSR, with over 240 additional contributions from more than 35 contributors outside of Deno.”

May saw the arrival of Deno’s standard library, giving it “autogenerated documentation and SemVer deduplication,” according to [another blog post](https://deno.com/blog/std-on-jsr), “while enhancing accessibility and versatility for developers worldwide.” (Although its original location at deno.land/std “will still be available indefinitely. All programs that depend on deno.land/std will keep working. Don’t worry!”)

with 44 modules ranging from data parsing/manipulation, working with web protocols, and general helper functions, the Deno Standard Library probably has what you need.

[https://t.co/9inNA4dMXe][https://t.co/CZybUAhr9a][pic.twitter.com/BFCeQbrsU0]— JSR (@jsr_io)

[August 21, 2024]
And Donmoyer also tells the inside story of JSRF’s logo design — starting with the way they’d adopted the yellow tones of the [Unofficial JavaScript Logo](https://github.com/voodootikigod/logo.js) by Chris Williams). But then the design team had “started playing with the concept of ‘blocks,’ to evoke a system composed of many smaller parts”, and ended up with the JSR’s ambigram — that is, a logo that’s identical when rotated 180 degrees.

An image in the blog post also shows several other versions they’d considered… “The concept that eventually became the official JSR logo was originally just a hurried sketch,” remembers Deno frontend engineer [Josh Collinsworth](https://www.linkedin.com/in/joshcollinsworth/). “I was trying out a bunch of ideas, drawing inspiration from projects I’d done during my time in design school…”

Curious how the JSR logo and website design came together? 🤔️

Here’s a 👀️into our design process.

[https://t.co/NoIeaOUFRn]— JSR (@jsr_io)

[September 4, 2024]
But the engineers began using it as a placeholder — and in the end, began advocating for it. “I was initially reluctant to crown it the winner, since I still saw it as a quick concept sketch. But the more we lived with it, the more its straightforward simplicity actually felt just right for the project.”

It’s interesting how one thing led to another. The next step was matching the rest of the site’s color palette to the logo. And regular visitors eventually realized that their cursor can draw lines from the little squares that are always drifting up in the page’s background (thanks to the delightful open-source library [particles.js](https://vincentgarreau.com/particles.js/)). The end result “a fun effect that ties into both the JSR brand and the boxes motif, with some fun little interactivity baked in.” (It’s also highly performant — loading less than 10 kilobytes, which is deferred until the rest of the page loads.)

## Beyond npm
Back when the JSR was still in its public beta, a [March blog post](https://deno.com/blog/jsr_open_beta) acknowledged npm’s 2.5 million packages “and about 250 billion downloads in the last 30 days alone”, saying numbers like this make it “arguably the world’s most successful package registry. JavaScript might not enjoy the status it has today were it not for this incredible ecosystem that the JavaScript community built together.”

But then it moves on to JSR’s value proposition. “We believe it is time to reimagine how a package registry should work in 2024.”

So the idea is to create an extension of npm — but with big ambitions.
In [an April blog post](https://deno.com/blog/jsr-is-not-another-package-manager), Dahl argued that the JSR was “not just another tool in the ecosystem but a fundamental shift in how we think about distributing JavaScript and TypeScript…”

“JavaScript is the common language of many programmers, making it both universal and accessible. The language merits a central hub — a town square — where developers can share their work without undue complexity.

“We believe JavaScript will remain central to software development for many years, and JSR aims to support this enduring relevance.”

[
YOUTUBE.COM/THENEWSTACK
Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.
](https://youtube.com/thenewstack?sub_confirmation=1)