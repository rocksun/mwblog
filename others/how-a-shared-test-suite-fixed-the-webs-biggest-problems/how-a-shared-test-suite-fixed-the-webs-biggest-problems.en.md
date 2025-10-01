It’s a key part of how web standards and browsers are developed, which grew from tiny beginnings, depends on a remarkably small number of people, is funded by the main browser companies together, and isn’t widely known despite the fact that even governments care about browser [competitiveness](https://www.courtlistener.com/docket/18552824/united-states-of-america-v-google-llc/) and the [compatibility](https://assets.publishing.service.gov.uk/media/67d1abf60f8734b8791a1da1/Appendix_A_-_browser_comparison_1.pdf) it underpins.

Today, [Web Platform Tests](https://web-platform-tests.org/) (WPT for short) is a comprehensive test suite for the web platform that helps ensure browser interoperability; exactly what you’d expect from a platform driven by specifications and multiple competing implementations, that’s used by three billion people every day. Think of WPT as the engine for interoperability on the web.

“Web Platform Tests is essential for anybody who’s implementing a browser, so that they can ensure compatibility,” Ecma president [Daniel Ehrenberg](https://www.linkedin.com/in/danielehrenberg/) told The New Stack. “Sometimes people can read the same spec and get different ideas out of it and Web Platform Tests makes sure that really, concretely, the same behavior is being shipped.”

Except that it wasn’t always like that…

> “Web Platform Tests makes sure that really, concretely, the same behavior is being shipped.”  
> **– Daniel Ehrenberg, Ecma president**

“For half the lifetime of web standards there was no testing,” Igalia developer advocate [Brian Kardell](https://www.linkedin.com/in/brian-kardell-08a4264/) pointed out. Individual browsers ran their own test suites, but “from when Tim Berners-Lee said ‘here’s a paper about what I want to do’ until now, we get halfway into history before web platform tests even became a thing.”

The complexity and scale of the web meant that was an increasing problem.

“The web platform is the largest software platform in the world; it’s got so much surface area that trying to test the web platform externally wasn’t working,” former Boucoup CEO [Boaz Sender](https://www.linkedin.com/in/boazsender/) told us.

“WPT came out of the frustration that the web was not working properly and we needed to do something about it,” added [Philippe Le Hégaret](https://www.linkedin.com/in/philippelehegaret/), VP of technical strategy at the W3C.

Along the way, WPT also shifted the culture around building browsers — from thinking about the software they were coding, to thinking about making the web platform that developers depend on interoperable so that everyone wins.

> “WPT came out of the frustration that the web was not working properly and we needed to do something about it.”  
> **– Philippe Le Hégaret, VP of technical strategy at the W3C**

“The goal of WPT was, and still is, to act as a comprehensive test suite that covers the standards-based web platform, across all of its implementations,” explained [Patrick Brosset](https://www.linkedin.com/in/patrickbrosset/), a senior product manager on Microsoft’s Edge browser and co-chair of the W3C WebDX community group.

“The driving idea was to consider the open web platform as one entity, one combined software project, which web devs build their products on top of. Because of this, we need the platform to be robust and interoperable, which requires thorough testing.”

## From Browser-Specific Tests to a Unified Web Platform

How did the web manage to get so far without having common tests? “We managed by it simply being, very often, a terrible developer experience,” admitted [Robin Berjon](https://www.linkedin.com/in/robinberjon/?originalSubdomain=be), former editor of the HTML spec.

In fact, the early W3C wasn’t thought of as a standards organization by the people who were involved, Berjon pointed out; “it was much more ‘hey, let’s get together and agree on the features we want’ and then the features happen because people are just implementing them.”

Because W3C specifications have long required multiple implementations before they’re ratified, anyone not actually building a browser probably assumed that always included testing.

“If you asked browser engineers who are engineering features on a day-to-day basis, they would say it’s not really like that; usually that stuff happens after the features are already shipped in browsers,” [Rick Byers](https://www.linkedin.com/in/rick-byers/?originalSubdomain=ca), director of Google’s web platform team, pointed out. “And by then, honestly, it’s too late.”

Working on the HTML5 spec in the days before WPT, both Berjon and Le Hégaret were concerned that without better testing, it wasn’t going to be interoperable. “The web was not working the way we wanted it to work,” Le Hégaret said. “Part of my frustration was the complexity was increasing significantly and [we didn’t even know how to test the stuff](https://www.w3.org/2009/11/05-w3cdev-minutes.html#plh).” In 2010, he [warned that HTML5 wasn’t ready](https://www.computerworld.com/article/1541527/w3c-html5-isn-t-ready-yet.html) because it wasn’t interoperable.

> “…the television industry came to us and said, ‘we need to figure out how to do the testing, because that’s what we do for television — where are your tests for the web?’”  
> **– Le Hégaret**

That was holding up phone and TV manufacturers, who were interested in adopting HTML but were used to doing extensive testing. “Smart TVs were looking at deploying HTML as their platform,” said Le Hégaret, “and the television industry came to us and said, ‘we need to figure out how to do the testing, because that’s what we do for television — where are your tests for the web?’ And we looked at them like they were from another planet.”

It’s not that no one was doing *any* testing; it’s that the tests weren’t comprehensive or consistent. “The web has always had tests,” [Philip Jägenstedt](https://www.linkedin.com/in/foolip/?originalSubdomain=se), a software engineer on the web platform team at Google, noted. “Browser engineers implementing features would write tests, and sometimes they would share them with other browser engines, perhaps.”

Take Test262, the ECMAScript test project (which has its own maintainers, infrastructure and integration with projects): it’s a key part of how new features are developed for JavaScript, and proposals can’t advance until there’s a full test suite ([the recently introduced ECMAScript 2.7 stage](https://thenewstack.io/inside-ecmascript-javascript-standard-gets-an-extra-stage/) is there specifically to make writing tests a more effective and less demanding process). That started around 2010 — when Google and Microsoft contributed their own internal ECMAScript tests to TC39.

“Each engine always had tests,” Kardell agreed. “But they were all just doing their own thing and you didn’t know what their tests were: if they were any good, if they were testing the same thing as the tests on the other browsers.”

“They were basically really focused on the problem of ‘how do we stop having regressions?’,” explained Mozilla web compatibility engineer [James Graham](https://hacks.mozilla.org/author/jgrahammozilla-com/), who worked on automating test suites at Opera. “And they were really specific to that browser.” Copying another browser’s tests became “a maintenance nightmare,” added Simon Pieters, another Mozilla engineer who worked on the Opera test suite.

In the early 2000s, the process for a new specification becoming a W3C recommendation had begun requiring a test suite showing two independent implementations; as a sign, Berjon recalled, of the importance of the web. But process requirements can easily be treated as annoying bureaucracy if they don’t come with a culture change. “It used to be you’d do all this work on the spec, and then when you’re trying to get the recommendation stamp on it, you do the extra work to prove that you have the test suite,” Byers noted.

> “The whole of SVG had maybe 200 tests, which is ridiculous! That’s not even enough to test shapes or colours.”  
> **– Robin Berjon, former editor of the HTML spec**

Seeing it as extra work didn’t necessarily make for comprehensive tests. One day of a W3C meetup would be set aside for working on tests, but that ‘interop day’ might only produce a handful of tests for a specification with many hundreds of pages, Berjon remembered. “The whole of SVG had maybe 200 tests, which is ridiculous! That’s not even enough to test shapes or colours.”

“These things strike us as crazy now,” Berjon continued. “We knew then that it wasn’t great – but it also wasn’t considered horrendous. The web was still successful, people still shipped things. But it was problematic in that the problems it caused accumulated.”

Again, some browsers contributed some of their tests to W3C working groups, building test suites for HTML, DOM and CSS — but those included very limited numbers of tests, lived in separate test repositories, were only intended for the W3C itself to check the initial implementations of a spec actually complied with it, were often only run once — and were typically forgotten after the spec was ratified, even if it changed later.

“They were only meant to check that, yes, you can implement a specification. They were never meant to make sure that the web is working properly as well,” Le Hégaret told us.

When WHATWG arrived with the concept of HTML as a “living standard” that kept evolving, a few fossilized tests weren’t a good fit for supporting that.

“If another browser changed the behavior of an API, or implemented a new API, or the spec has changed: at that time, there wasn’t a policy to file browser bugs for spec changes, or a culture of filing bugs on other browser vendors when you changed your own implementation,” Pieters noted. “Some other browser changed or the spec changed, and other browsers changed but one browser didn’t notice. They didn’t get any bugs filed, and they would only notice once websites started to break, and then they needed to investigate and reverse engineer it and figure out what happened.”

The working group test suites also weren’t automated, Graham noted. The CSS 2 test suite took two days to run because “it required somebody like me sitting looking at things and deciding if they passed or failed.” Designed for internal spec purposes, they didn’t work effectively for interop: “They weren’t going to find edge cases or things that were breaking websites for authors.”

> “We had browser specific tests that were high quality tests but specific to a given browser.”  
> **– James Graham, Mozilla web compatibility engineer**

The independent ACID test was an attempt at a more comprehensive test, but it had its own issues. Loading a web page with a mix of features to test a browser’s implementation of standards led to browsers over-focusing on passing the test and fixing bugs that reduce their scores. But by ACID 3, browser makers were questioning the choice of which features were included in the test, and the emphasis on ACID scores meant that some browsers implemented just enough of a feature to pass the test, “but was basically broken if you tried to use it in any other way,” said Graham.

“Web Platform Tests was a reaction to all these things,” Graham continued. “We had browser-specific tests that were high-quality tests, but specific to a given browser. We had shared tests that were hard to run and not very deep, we had the ACID tests that were deep but turning into a marketing exercise. The goal with WPT in the early days was, let’s try and build a really engineering-focused shared test suite where we collect all the tests together and make it possible to share them between browser vendors, so engineers are motivated to say ‘there’s a bug in my implementation, I should fix that’ — without it being about marketing or to progress a standard.”

## The Independent Origins and Influence of WPT

When Le Hégaret and [Tobie Langel](https://www.linkedin.com/in/tobielangel), Facebook’s then web standards lead, drew up a likely budget for an [Open Web Platform testing project](https://www.w3.org/2013/Talks/0129-testing/#(3)) and went looking for support from W3C members, there were few takers; only a couple of organizations offered money and it was more like $200,000 than a share of the $7 million an official project would take. At the time, Le Hégaret estimated [each individual test would cost $100](https://www.w3.org/2013/Talks/0129-testing/#(16)) to write and validate.

Having been pushing for a better approach to testing [since 2009](https://www.w3.org/2009/11/05-w3cdev-minutes.html#plh), he recalled, “I felt like a broken record.”

Adobe funded the [Test the Web Forward](https://web.archive.org/web/20120619032148/https:/testthewebforward.org/) events, which were hackathons aimed at contributing tests to multiple browser engines. It didn’t necessarily produce a lot of useful tests, but did help raise awareness, Berjon suggested. “I think it helped to broaden the community, because it [gave the project legitimacy](https://archive.fosdem.org/2014/schedule/speaker/james_graham/).”

Even working group chairs weren’t always supportive of the idea of common tests, sometimes viewing it as a distraction from finishing specifications. Although it started inside the W3C, in 2014 WPT became an [independent project](https://web.archive.org/web/20230529015807/https:/www.w3.org/blog/2013/02/testing-the-open-web-platform/)  (with some funding from Facebook) — and a very grassroots one with just a few people involved.

> “The other browser vendors at that time didn’t — and still, to some degree don’t — have the same kind of separate testing team that Opera did.”  
> **– Mike Smith, W3C**

In fact, what became the WPT collection of tests started just by collecting existing tests in one place and [renaming what had been the HTML test suite repo](https://lists.w3.org/Archives/Public/public-html-testsuite/2013Mar/0005.html) to web platform tests, Berjon explained. “I started moving stuff over in the simplest way possible. I made a massive list of all the tests in CVS and Mercurial and the other git repos and the ZIP files people were emailing around, and I started importing everything, with history if possible, and then I ran the dirtiest search and replace on them to make them work with the same test harness — and then we had something.”

That test harness was part of Graham’s work on automation at Opera, Le Hégaret said. “James Graham had written a short JavaScript library to be able to write tests more easily, and we piggybacked on that.”

“The other browser vendors at that time didn’t — and still, to some degree don’t — have the same kind of separate testing team that Opera did,” added W3C’s [Mike Smith.](https://www.w3.org/staff/#mike)

He worked on the imports with Berjon, who described these small beginnings as ‘stubborn’, but enough to start testing. “We started having at that thing. It crashed almost every browser because the browsers didn’t like being tested that hard! From that point on, we actually had a project.” Their work slowly attracted other people to contribute or review tests. “We started getting momentum.”

The core team of WPT [remained small](https://lists.w3.org/Archives/Public/public-test-infra/2018OctDec/0017.html) and it took time to build up the number of tests. Despite its importance to the web, CSS wasn’t initially included in WPT, due to some constraints in the way CSS tests worked, which conflicted with the WPT approach.

“We wanted to design the incentive structure to be towards interoperability and also lower the barrier to contributing to the test suites as much as possible, so that browser engineers would write tests in WPT instead of doing the simple thing, which is to continue to write internal tests,” Pieters explained. “The CSS test suites had a lot of requirements for tests that set the bar too high for browser engineers to meaningfully contribute to that test suite.”

The overhead of getting their tests into a standard test suite had been more than the value from contributing them: WPT was about making it easier to do the right thing.

> “WPT is such an important aspect of standards that it’s its own entity. It works independently with its own working mode and its own processes and its own membership.”  
> **– Boaz Sender, Boucoup CEO**

Eventually, the CSS test suite was integrated into the main WPT repository, although different working groups — like the CSS Working Group — still have their own processes for integrating with WPT. [By 2017](https://www.w3.org/blog/2017/the-web-platform-tests-project/), WebKit and Edge were getting involved.

Ironically, the failure to raise the funds to make WPT a formal part of the W3C probably gave it more influence because of its independence (even if that influence is technically informal and more to do with consensus than any explicit authority).

“I believe in balance of power, so I wanted the project to be independent,” Le Hégaret explained. “I wanted the testing people to be able to challenge any of the WC working groups.”

“W3C produces standards for the web, which gives W3C some amount of power over the web, even though our standards are voluntary,” Le Hégaret said. “The browser vendors themselves also have power over the web because they are implementing the browsers — if something doesn’t get implemented by your browser, it’s not really part of the web.”

Specifications, implementations and documentation like MDN are all fundamental. “If you don’t have documentation for developers,” Le Hégaret added, “it’s less easy to use the technology as such. And I wanted testing to become another pillar.”

“WPT is such an important aspect of standards that it’s its own entity,” Sender agreed. “It works independently with its own working mode and its own processes and its own membership.”

“Testing is a form of peer review,” he suggested. Or as Fermyon co-founder [Matt Butcher](https://www.linkedin.com/in/mattbutcher/), who is working on Wasm standards in the Bytecode Alliance, put it: “Standards are nice when they’re written in words, and better when they’re written in words and in code.”

## Fostering a Culture of Collaboration Among Browser Vendors

When Google (somewhat belatedly) made WPT a key part of the Chrome engineering process in 2016, it came from the same realisation that continuing developer frustration with the inconsistency of the web went back to [software development fundamentals](https://www.w3.org/2017/11/07-testing-minutes.html). “Step one in software engineering is you should have a coherent test suite,” Byers recalled. “Our main product that developers are relying on doesn’t even have a reliable test suite: we’ve not been doing our job as engineers.”

Tests had existed for years, Jägenstedt noted: “The problem was we didn’t care very much about it.”

Deciding that all future work in Chromium needed to come with conformance tests that *all* browsers could use for interoperability was about [changing the culture](https://www.w3.org/2017/11/07-testing-minutes.html) in the Chromium project the way it had [begun to change in working groups](https://lists.w3.org/Archives/Public/public-pointer-events/2016JulSep/0383.html), who had originally pushed back on the importance of shared tests.

> “Our main product that developers are relying on doesn’t even have a reliable test suite: we’ve not been doing our job as engineers.”  
> **– Rick Byers, director on Google’s web platform team**

“It’s not really a shift from not caring to testing, to suddenly writing tests,” Jägenstedt pointed out; “but a lot of work to actually make these processes work, where one browser vendor can write tests and have those show up for another browser vendor, and have a shared dashboard where we can see the results.”

It also brought Google’s influence (and funding) to the project. The Chrome team funded Bocoup to help Chromium engineers contribute tests they wrote to WPT so they would show up like that. Apple and Mozilla implemented their own synchronization based on that, and Microsoft also paid them to migrate its internal Edge tests (which included a fork of WPT used to test Trident Edge) when it moved to Chromium. Google also worked with Bocoup to build out the infrastructure to automatically run WPT tests for every new browser version. Those results are what you now see on the WPT dashboard.

Along the way, WPT also helped W3C and WHATWG (which had initially had rather antagonistic approaches) learn to work better with each other, Berjon told us.

“All these people had basically the same goal; they were working on somewhat different deliverables, but the overlap was much more than the difference. I figured if we could get a bunch of people working on something that they all cared about, that we could safely say was joint work, then we’d have something that would help mend the community.”

That worked; in fact, not only do WHATWG living standards now mandate WPT tests, but Smith noted, “you can’t even get a pull request merged until you have written tests and gotten those into WPT”.

## How WPT Results Drive the Interop Initiative

One of the reasons WPT may seem so invisible is that although it’s [on GitHub](https://github.com/web-platform-tests/wpt) and you can [try the tests out](https://wpt.live/) from a browser of your choice (particularly useful for smaller projects like [Ladybird](https://ladybird.org/)), it’s used very much behind the scenes. Browser makers integrate their own deployment of WPT tests in their own CI/CD systems (importing a copy of the tests and exporting the results back to WPT, as well as syncing in new tests they write). For example, before a new feature can ship in Chrome, the relevant tests have to be integrated to WPT and passing — and you can see an archive of the latest public test scores on the [WPT dashboard](https://wpt.fyi/results/?label=master&label=experimental&aligned).

Browser engineers might use WPT results to prioritize features that will be more interoperable, based on how well other browsers already support them, Smith suggested. “If you look at WPT results, and you see all red with one column of green, maybe that’s not the one that I want to implement.”

The place where most people who *aren’t* building a browser or a server-side runtime will explicitly come across WPT is in the annual [Interop](https://thenewstack.io/interop-unites-browser-makers-to-smooth-web-inconsistencies/) initiative, which comes up with a list of priorities for improving browser compatibility in areas where WPT scores show interoperability isn’t as good as it should be.

Individual browser scores on WPT give a very [imperfect impression](https://bkardell.com/blog/WPT-Dashboard.html) of the state of the web platform overall, because what matters is not how high those individual scores are (since they measure different combinations of tests and subtests) but how many tests all of the browsers pass, so developers can rely on those features working in every browser.

> “If you look at WPT results, and you see all red with one column of green, maybe that’s not the one that I want to implement.”  
> **– Mike Smith, W3C**

The WPT dashboard does let you explore, say, whether [Chrome and Firefox pass more tests than Safari](https://wpt.fyi/results/?label=master&label=experimental&aligned&q=chrome%3Apass%20safari%3Afail%20firefox%3Apass), whether there are features in [Firefox that pass tests Chrome and Safari both fail](https://wpt.fyi/results/?label=experimental&label=master&aligned&q=chrome%3Afail%20safari%3Afail%20firefox%3Apass), or whether [Chrome passes tests neither of the non-Chromium browsers do](https://wpt.fyi/results/?label=master&label=experimental&aligned&q=chrome%3Apass%20safari%3Afail%20firefox%3Afail) (which can give you a feel for whether Chrome is possibly moving too fast, or if there might be a reason for [developer complaints about interoperability in Safari](https://bsky.app/profile/lea.verou.me/post/3lzgm4ms5a22z)).

“Google is the one that’s funded well enough, and is able to do test implementations of things; they’re usually the first to implement when the call for implementations goes out,” Meyer pointed out.

But raw WPT numbers can include tests for features still in development as well as proposals since deprecated, like the ambient light sensor that turned out to have privacy issues. The number of tests a particular browser fails or the fact some tests aren’t even relevant for all browsers isn’t necessarily an indication of that browser falling behind on web standards. At [one point last year](https://bkardell.com/blog/BSF.html), Safari was failing the most tests, but Firefox was failing the most subtests — making it even less helpful to use the scores as a comparison.

That was always a deliberate difference from the ACID test, Graham noted. “There was no assumption that being ready means that we have a 100% pass rate on every single test. Maybe some of these tests are about the interaction with another feature that you don’t ship at all. Maybe they’re extreme edge cases.”

The tests aren’t always right either. WPT is a resource for new browsers like Ladybird (which Smith contributes to): “it’s a requirement for getting on the iPhone that you have to be passing 90% of WPT tests,” he noted — but added that sometimes WPT and the specs don’t agree.

“There are cases where you will find that you cannot implement strictly according to what the spec says and also pass the WPT tests, because some of the WPT tests are written not according to the spec requirements, but according to what the implementations were doing.” Ladybird implements to match WPT for interoperability, but also raises an issue with the spec — which may have actually been written to document existing browser implementations and not been updated.

“The first implementation of a feature will include tests for what the engineers thought of, and those will be part of the specification, but later implementations might find issues where the tests and the specification don’t quite match up,” Meyer agreed.

> “We had to do a little bit of a dance in the early days of WPT to reassure the browser vendors we were not here to blame them for not implementing the standard properly but to give them a tool to improve their implementation.”  
> **– Le Hégaret, W3C**

WPT was never intended to rank browsers: it was about helping them all improve — which is what Interop is about too. “We had to do a little bit of a dance in the early days of WPT to reassure the browser vendors we were not here to blame them for not implementing the standard properly but to give them a tool to improve their implementation,” Le Hégaret said.

That’s why the Interop scores Sender proposed to replace pass/fail rates are a more helpful comparison. For a start, they cover the subset of WPT that all the main browsers agree matters enough to invest effort in passing, because that improves interoperability on features. It also prunes out tests for experimental features that might be interesting for developers (like [WebSerial](https://wicg.github.io/serial/) and [WebBluetooth](https://webbluetoothcg.github.io/web-bluetooth/) for connecting to devices) but that aren’t yet agreed web standards.

“The Interop score is a good solution for that because it can evolve every year and it also doesn’t pit people against each other; because in order for this to work, the companies need to cooperate,” Sender pointed out. “The things that aren’t interoperable between Safari and Chrome are based on strategic decisions around technology, privacy or hardware integration. There’s competition, but implementation of the standard is not where they compete.”

“Obviously, every vendor has its own strategy and thinking on what’s important to them and their customers and users,” Topal agreed. “But one thing that is also clear is that there is one developer audience, so when they have problems, when they run into issues, basically that’s the ground truth for all vendors.”

Interop and WPT move everyone forward, Ehrenberg suggested. “Everyone agreeing that [what] we’re doing to focus on becoming conformant to this set of tests really helps build a stable base for web users, so that once this is complete, it’ll be in [Newly Available Baseline](https://thenewstack.io/baseline-newly-available-stay-on-top-of-new-web-features/) and then full [Baseline](https://thenewstack.io/what-does-it-mean-for-web-browsers-to-have-a-baseline/). This all forms a very nice pipeline for web developers to get new features that are usable reliably, because we know that when features are only available in some browsers, or when they’re available but broken in some places, then people stay clear of them. They won’t get as much uptake, won’t provide as much value if they’re not broadly implemented and implemented correctly.”

> “…we know that when features are only available in some browsers, or when they’re available but broken in some places, then people stay clear of them.”  
> **– Ehrenberg, Ecma**

WPT underpins Interop, Google web platform product manager [Kadir Topal](https://www.linkedin.com/in/kadirtopal/?originalSubdomain=de) said; “we need to make sure we actually have good coverage, test-wise, for features, and the Interop dashboard gives us a really good view into the status of features on the dashboard.” That helps developers “get a sense for the level of the implementation of a given feature in browsers” Brosset added.

Although the areas Interop tackles come from problems developers complain about in the annual State of HTML, CSS and JavaScript surveys (run by the Web DX community group) or submit as interoperability bugs, it relies on and also improves WPT tests.

The [Interop dashboard scores](https://wpt.fyi/interop-2025) show how well each browser does on the WPT tests in each focus area, but part of tackling a focus area is checking that WPT includes the right tests and sometimes improving or expanding them. Features without tests can’t be part of Interop, because as Meyer pointed out, “how are we supposed to evaluate interoperability if we don’t have the test or the specification clarity to know what we should even be doing?”

WPT test results feed into tools like [Web Platform Status](https://webstatus.dev/), which shows the status of web platform features across browsers — including browser support, baseline status and WPT results. While the WPT and Interop sites clearly show results, they don’t give as much information about the features tested; the idea behind Web Status is to fill that gap, Topal explained.

“We’ve mapped the whole web platform to individual features like popover and promise.try and a little more than 1,000 web features. And we are now in the process of mapping the web platform tests to those features so that you get clarity like on the Interop dashboard, but for the whole platform.”

“We hope this will be useful to maintainers of the web platform, to see where the gaps are,” Jägenstedt added. “If you’re implementing [View Transitions](https://thenewstack.io/interop-unites-browser-makers-to-smooth-web-inconsistencies/) and you want it to be solid, how do you do it? It used to be there was no scaffolding around in and now it’s quite clear: here are the tests for anchor positioning and you’re passing 92%”

Microsoft also uses WPT test scores in [the list of Top Developer Needs it compiles](https://microsoftedge.github.io/TopDeveloperNeeds/) from its own experience and developer feedback. WPT results don’t show up in other web feature dashboards like [CanIWebView](https://caniwebview.com/) or the MDN documentation, but pages in the WebDX [Web Platform Features Explorer](https://web-platform-dx.github.io/web-features-explorer/) link to WPT results for each feature, alongside other details like usage stats and the original specifications.

## The Technical Infrastructure Underpinning WPT

WPT hasn’t yet featured much in the current debate about the ownership, funding and competitive landscape of browsers, but Kardell noted “the funding that holds up the web is mainly from Google search,” which he describes as “a load-bearing monopoly.” That includes some of the [infrastructure](https://www.bocoup.com/blog/lessons-learned-from-a-year-of-testing-the-web-platform) for WPT; it also uses services donated by Mozilla — itself largely funded by Google — and Microsoft for running tests, although Apple runs Safari testing on macOS internally (because of licensing complexity).

Core WPT personnel also work at browser makers and in the W3C, which is funded by member organizations.

> “…the funding that holds up the web is mainly from Google search” [and it’s] “a load bearing monopoly”.  
> **– Brian Kardell, Igalia**

That’s as much pragmatism as altruism. “WPT represents millions of dollars’ worth of work and infrastructure that saves browser vendors significant resources by providing a shared testing framework,” Smith pointed out. “We’re fortunate that Mozilla and Google and Apple, over time, have really understood that it’s important to have people paid to work on this stuff.”

The tests themselves are HTML, JavaScript and CSS. “The simplest ones are you make a web page that draws boxes on the screen, and then you make another page that makes some boxes on the screen with a different set of features. Do they match?” Kardell explained.

Tests use [WebDriver](https://w3c.github.io/webdriver/) for browser automation that can’t be done in JavaScript: “having that cross-browser way of doing things that you can’t do inside a browser is really important,” Graham said, because it was another incentive to move away from internal browser tests.

The core test harness for WPT is written in Python, originally for running tests locally, and it uses the basic HTTP server built into Python. That has some limitations for performance when browser makers run it as part of their CI pipeline, especially as the number of tests in WPT has grown.

“Maybe it doesn’t sound so hard, but making it work reliably is actually quite hard,” Jägenstedt noted.

“[WPT is] just like the web; it’s grown, it’s evolved that way and it would be very hard to go back in and replace it and rewrite it all,” Smith pointed out.

The investigation areas in Interop each year are usually about seeing how to add tests to WPT to cover more areas, which might be as simple as writing new tests (or improving existing tests if they turn out to be inaccurate) but often involve looking at what’s possible with browser automation, which might in turn mean [adding new options to WebDriver](https://w3c.github.io/webdriver-bidi/).

> “[WPT is] just like the web; it’s grown, it’s evolved that way and it would be very hard to go back in and replace it and rewrite it all.”  
> **– Smith, W3C**

Test262 remains separate from WPT. There’s obviously some overlap — since every browser has a JavaScript engine — but while the WPT project and the Test262 team have talked about whether it makes sense to bring them together more closely, there are obvious differences as well: For one thing the server-side JavaScript runtimes like Node.js, Deno and Bun often behave differently from browsers because they’re doing different things. For another, there are places where the behaviour that the JavaScript specification requires isn’t the same as what the HTML specification requires (which is why importing JSON modules is in both [Interop 2025](https://thenewstack.io/interop-unites-browser-makers-to-smooth-web-inconsistencies/) and [ECMAScript 2025](https://thenewstack.io/javascript-standards-update-whats-new-in-ecmascript-2025/)).

Node.js Technical Steering Committee member Joyee Cheung pointed out the nuances: “You want to be able to interoperate with code written for another environment and the tests are a way to verify that, but the harnesses we use to run the tests might actually create differing behaviour in the interop.”

JavaScript features like this are rare in Interop and it’s not clear whether that’s because TC39 is already handling these issues or if it’s a chicken and egg problem. The Interop score can only be calculated for tests that are part of WPT and so far that’s been done by copying the relevant Test262 tests into WPT, but without an Interop score for more JavaScript features, developers may not think of the project as a natural venue for JavaScript interoperability issues.

Even in the browser, there are some areas — particularly on mobile devices and in screen readers — that are hard to test through WPT, and there’s a whole new [bidirectional WebDriver protocol in development](https://github.com/w3c/webdriver-bidi) to handle testing service workers, window management and other things that aren’t web pages.

The platform differences mean that not all of WPT is even relevant for JavaScript server-side runtimes: “Most of the things that need WebDriver integration are not APIs that are supported in server-side runtimes,” [WinterTC](https://wintertc.org/) co-chair [Andreu Botella](https://www.linkedin.com/in/andreu-botella-botella/) noted.

But as part of defining the minimum subset of web APIs developers can expect server-side runtimes to support, “WinterTC is working on identifying a subset of the WPT tests that can be used as a test suite,” Botella said. That may even help developers who are used to working in the browser to understand where runtimes have deliberately different behavior (often because they have different security models, but sometimes for compatibility with early Node.js decisions).

> “The web is everywhere; the web is on watches and washing machines and refrigerators and TVs”.  
> **– Sender**

“There’s a boundary of what the web platform is, and the libraries that are included in the web browser, and I think that that does make sense from a testing perspective,” Sender pointed out, but WPT is also trying to move beyond that where possible because of the scope of the platform. “The web is everywhere; the web is on watches and washing machines and refrigerators and TVs”.

Some of the Interop investigation areas move slowly for logistical reasons (touch testing still excludes mobile devices because they’re hard to instrument), but he also notes the juggling act of dealing with competitive organizations.

“WPT is a group of 15-20 people from six or seven companies who have to go back to their thousand-person engineering teams and be accountable for getting folks to align on the shared status product road map; and there’s only so much they can do.”

## The Scale of WPT and Community Involvement

Test coverage in WPT is significantly better than it was in the early days: Depending how you count different sub-tests, there are around 2 million individual tests grouped into around 60,000 main tests.

WPT is probably never going to achieve complete coverage of everything in the web platform, because the web platform just keeps on expanding every year — Kardell called it a moving target and Le Hégaret noted that “what we achieved with WPT was exactly what we wanted, but the problem is we keep growing the web platform.”

WPT is fairly neutral about what tests are included, Jägenstedt told us. “As long as it’s a spec you can put your test in WPT, even if there’s just one browser vendor who thinks it’s a good idea. Basically, everyone is welcome and if others want to come along later, that’s cool.”

> “…what we achieved with WPT was exactly what we wanted, but the problem is we keep growing the web platform.”  
> **– Le Hégaret**

There is a slight catch-22 in [the way WPT tests are written,](https://web-platform-tests.org/writing-tests/index.html) though. Ideally, what they test is how well browsers implement specifications, and what that ought to measure is how useful they are to web developers; but as Smith pointed out, the people writing WPT tests are mostly browser engineers and system developers who are familiar with C and C++, rather than web developers with expertise in HTML, CSS and JavaScript.

That includes browser makers and consultancies like Igalia. “Sometimes it’s individual contributors, people who really care about a given technology that is not getting the love from other people will contribute tests,” Meyer noted.

“If you want to get a thing fixed in a browser, having a failing web platform test is a really good start, because nothing is going to get fixed without a failing web platform test,” Kardell agreed. “If you’re Wix or Shopify and you have a business online and it costs you a lot of money to have bugs, if you desperately want this feature because it will save you money or time, contributing WPT is one way that you can invest in the platform while getting something out of it yourself. Because this will make it more likely to get [a feature] implemented or get [a bug] addressed.”

There have been attempts to get more web developers involved in writing WPT tests, going all the way back to Test The Web Forward, which many hoped would be “an on-ramp to web standards,” Sender noted. But that didn’t always produce high-quality tests, because writing good tests that cover all the scenarios and contexts is hard and getting up to speed with WPT itself takes time.

> “It’s a messy, imperfect and improvable system, but it’s still good to have the community involved and to keep pushing for that.”  
> **– Berjon**

“There’s a bit of a learning curve,” Jägenstedt agreed; “you’ll need a buddy in WPT to spend time coaching you and reviewing your tests.”

Plus, web developers do tend to be busy working on building websites and apps, and the [timescales don’t always match up well](https://infrequently.org/2018/06/effective-standards-work-part-2-threading-the-needle/), because it will likely take multiple years until their customers are using a new browser that would pass a test they contribute.

“I like the idea that this has potential for public accountability, even though it’s way too challenging in practice,” Berjon said. “It’s a messy, imperfect and improvable system, but it’s still good to have the community involved and to keep pushing for that.”

## The Lasting Impact of WPT on Web Development

The goal of WPT was that “it should be possible to have multiple comparable implementations of the web platform, and they should all be high quality, and the users could really have genuine choice. We weren’t going to run into this situation where it was just too hard to build a web browser that worked with the real web,” Graham recalled.

WPT has helped put paid to the CSS hacks and arcane browser workarounds of a decade ago. Even a static website needed to be extensively tested in multiple browsers just to make sure it rendered. Sender remembered: Thanks to WPT, “the pain of doing those basic things went away and we got all these new features into the web”.

“It’s had much more positive impact than I could have imagined when we started the project,” Pieters agreed. “It would have been hard to imagine Interop then. Now browsers are aligning on which features to implement when, and getting 99% pass rates on the tests: that’s the dream!”

> “Your thing becomes more valuable if the other person’s thing works with yours because the web platform works.”  
> **– Sender**

Although the motivation for some browser makers may have included “90s antitrust fear — [WPT] is unique and it’s remarkable and also I think it’s a kind of antitrust protection”, it’s also a win-win scenario, according to Sender. “Your thing becomes more valuable if the other person’s thing works with yours because the web platform works. You sell more ads if you’re Google if more people are using it, you sell more phones if you’re Apple if more people are using it, Microsoft sells more Windows licences.”

Shared public tests are a unique approach that suits the web, he suggested. “Lots of other platforms don’t have this, but lots of other platforms aren’t interoperable in the same way, with such different code bases that do something so similar.”

Could it work elsewhere? “This is remarkable and perhaps a playbook for how we can do other things”. That might include accessibility, or perhaps the proliferation of design system UI libraries could be integrated in a way that WPT or Interop would enable. “We could have a standard UI library for the web.”

The WPT approach “all seems kind of obvious in hindsight, that that’s the right way to do things,” Smith noted.

> “It’s impossible to imagine now that we can maintain the web and the velocity of standardization that we have without having these shared tests.”  
> **– Graham**

It’s hard to imagine the modern web without it, Graham agreed. “It’s impossible to imagine now that we can maintain the web and the velocity of standardization that we have without having these shared tests.”

“Once a feature ships you expect to be able to use it. That’s definitely the expectation that we should have as a platform and I think without WPT, it would be completely unrealistic to have that kind of expectation.” Thanks to WPT, “the platform is doing more, but it’s also doing it better.”

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://cdn.thenewstack.io/media/2023/12/e2700739-maryb.jpg)

After completing an MSc in Intelligent Knowledge Based Systems in 1990, Mary Branscombe was convinced that promising as the AI techniques she’d been studying were, they weren’t even close to being ready. Since then, she’s been a technology journalist for...

Read more from Mary Branscombe](https://thenewstack.io/author/marybranscombe/)