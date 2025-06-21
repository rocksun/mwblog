The web platform is always evolving and improving; the downside for web developers is knowing which new features are available and when they are ready to work with.

[Interop](https://thenewstack.io/browser-vendors-aim-to-heal-developer-pain-with-interop-2022/) is a reasonable guide to web features you can expect to become mature enough to use over the next few years, but it only covers what *everyone* in the browser world has agreed to work on. The new [Safari 26 beta](https://developer.apple.com/videos/play/wwdc2025/233/) adds support for anchor positioning: an extremely popular feature from the [Interop 2025](https://thenewstack.io/interop-unites-browser-makers-to-smooth-web-inconsistencies/) list that was also the most requested option in the “CSS features you can’t use yet” question from the [2024 State of CSS survey](https://2024.stateofcss.com/en-US/) (and the related Popover API was a top request in the [State of HTML 2024](https://2024.stateofhtml.com/en-US) survey). But Safari 26 beta also includes cross-document view transitions: the View Transitions API work in Interop 2025 focuses on transitions in the same document.

Research like these surveys also shows that web developers tend to be [extremely conservative about using new CSS features](https://patrickbrosset.com/articles/2024-11-08-state-of-css-and-state-of-html-2024/), possibly because they have users in multiple browsers, or because they’ve run into cross-browser compatibility issues with new features in the past; but also because it’s not easy to notice when new features are not just shipping, but worth trying out. Similarly, suppose you’ve used a framework or polyfill to adopt a new feature that’s not widely supported in browsers. How do you know when you can remove what’s usually a large amount of code, or skip a transpiler build step because the feature is now available natively?

> It’s not easy to notice when new web features are not just shipping, but worth trying out.

“It used to be, way back in the day, that you had a browser policy: we support the latest browser for two years, or two revisions,” points out Igalia developer advocate [Brian Kardell](https://www.linkedin.com/in/brian-kardell-08a4264/). “Well, now that’s like four weeks for Chrome, so that’s out the window! It used to be a nice, simple thing that you could use, as a developer, to say ‘here’s what I need to learn.’”

You can check [CanIUse](https://caniuse.com/) and [CanIWebView](https://caniwebview.com/), but you have to know a feature exists to look it up. There’s always the release notes, blogs, origin trials, experimental feature tests, explainers, roadmaps, planned feature lists and positions on upcoming standards from the browser creators ([Patrick Brosset](https://www.linkedin.com/in/patrickbrosset/), senior product manager on Microsoft Edge and co-chair of the [W3C Web Developer Experience (WebDX) Community Group](https://www.w3.org/community/webdx/), maintains [a handy list of these and other resources](https://patrickbrosset.com/lab/navigating-the-web-platform/)), but that’s a lot to keep up with.

The handy [BCD Watch](https://bcd-watch.igalia.com/) put out by Igalia has weekly updates on what’s changed in the Browser Compatibility Data project that underpins MDN, but the details can be a little cryptic.

Much more developer friendly is the [Baseline project](https://thenewstack.io/what-does-it-mean-for-web-browsers-to-have-a-baseline/) started by Google, using definitions from the WebDX CG – which has created [a comprehensive list of features](https://web-platform-dx.github.io/web-features-explorer/features/) that are part of the web platform; including specs, browser support, usage and vendor opinions — to try and categorize whether those features are available and complete in the core set of browsers, so it’s easier to decide whether or not to use them.

> “The Baseline project is about simplifying this quite complicated information about which features exist on the web platform, and how usable they are.”  
> **— James Graham, Mozilla web compatibility engineer**

“The Baseline project is about simplifying this quite complicated information about which features exist on the web platform, and how usable they are, into a much simpler form so that if you’re quite conservative — say you’re writing a library — you can ask quite a simple yes/no question that covers most use cases,” explains Mozilla web compatibility engineer [James Graham](https://hacks.mozilla.org/author/jgrahammozilla-com/). “For the majority of cases, it takes away that level of cognitive effort of working out, is this even usable?”

Making information about who is implementing which web standards in a format that’s relatively easy to understand might also reduce some of that caution, by making it clear which features are widely supported and should be safe to use.

“One of the things we saw is that web developers sometimes have been reluctant to use things that were actually working quite well across the platform for quite a long time after they were working well,” said Graham, “because they still had the idea that it’s a new thing so it’s probably still quite broken, or maybe it’s not really everywhere yet.”

## Ready To Use

Initially, [Baseline](https://web-platform-dx.github.io/web-features/) was an annual list of all the features that had been available in the last two versions of major desktop browsers (Chrome, Edge, Firefox and Safari), with widely supported features labelled on MDN pages.

“What developers care about the most is what’s in [browser] engines and what’s out there in users’ hands,” points out [Kadir Topal](https://www.linkedin.com/in/kadirtopal/), who works on the web platform (including Interop and Baseline) at Google.

“We want to make the web platform more stable, we want to have a platform that is more interoperable, and at the same time, we want to make sure that developers actually know about it: that’s what Baseline does. For those things that are actually available across browsers, it makes it clear to developers what those things are and how they change year over year. Since the web doesn’t really have any releases, it’s really hard to say what has changed from last year to this year. With Baseline, you can say ‘what was Baseline in 23 versus 24’ and it gives you what’s changed. People can pay attention once a year, and know what has come out recently, in that year, like a moment in time.”

But developers don’t only care about whether a feature is interoperable, in the sense that it’s available in all major browsers — which is easy to track — they want to know when they can safely implement a feature on their own site without worrying about support issues; and that varies with the geography and userbase of each site.

> Safari updates are tied to a new release of the underlying operating system, so they take much longer to reach the same usage as the other browsers.

Some users on some devices in some countries will update their browser as soon as there’s a new release: Chrome, Edge and Firefox updates usually [reach 95% of users within three months](https://web.dev/case-studies/rumvision#browser_adoption_across_the_web). But Safari updates are tied to a new release of the underlying operating system, so they take around 19 months to reach the same usage, and some updates may even need a new device. Some developers are also willing to use polyfills and fallbacks so they can pick up a new feature sooner, while others want to wait until their users have upgraded.

Sometimes new features become available in at least one browser as soon as you hear about them, but sometimes it can take a very long time — as with [Temporal](https://thenewstack.io/the-new-javascript-features-coming-in-ecmascript-2023/), the new JavaScript date and time support, which has finally appeared in Firefox nightly builds. If web developers are going to make the most of all the new web features in browsers, they need a way to know what’s coming, as well as what’s fully baked and ready to rely on.

Now Baseline has more granularity, with three different levels that Kardell views as “degrees of realness” corresponding to “the number of spoonfuls of sugar you need to take with it”.

## Adding More Granularity

Baseline Widely Available tells you when a web platform feature is mature and ready to use in all the mainstream browsers, including mobile versions, because it’s been there for 30 months, which allows time for users to update to the latest version.

“30 months is based on looking at a couple of years’ worth of data with OS updates and turnover and where things land,” said Kardell. “After two and a half years, maybe fewer than 5% of people have something older than that” — although he encourages developers to continue polyfilling features for those users, who are probably those who can least afford either a new device or a broken site.

> “Baseline Widely Available is the strongest and simplest signal that developers can use to know if a feature is working for all of their traffic.”  
> **– Patrick Brosset, senior product manager on Microsoft Edge**

That’s a little late to start experimenting: Ideally, by the time most users have updated to get that new feature, developers want to be ready to refactor their code to use it rather than just start learning about it. “Baseline Widely Available is the strongest and simplest signal that developers can use to know if a feature is working for all of their traffic, but waiting for Widely Available is also the most conservative choice,” Microsoft Edge’s Brosset notes.

Mozilla’s Graham encourages web developers to be more confident about using new features, because standards and tests have made the web platform more reliable.

“We expect that, as soon as a browser is shipping a feature, then the limiting factor isn’t that there shouldn’t be bugs in that feature; the limiting factor is how fast the users start using that browser,” Graham explained. “The time between something being initially available in all browsers and being considered Baseline Widely Available is about being mindful of users getting on the latest versions. Ten years ago, it was a very different world: it was the world of CSS hacks and you were expected to know all these arcane workarounds to different browser bugs. There’s a lot less of that now!”

Baseline now helps you get ready. Features that aren’t yet implemented in all four core browsers, both desktop and mobile, are flagged as Limited Availability — which isn’t a signal not to use them, just an indication that it’s going to take [more work](https://developer.mozilla.org/en-US/docs/MDN/Writing_guidelines/Experimental_deprecated_obsolete#experimental), whether that’s polyfills and transpilers, or progressive enhancement and fallbacks for unsupported users.

Once a feature is in at least the latest stable version of all the Baseline browsers, it counts as Baseline Newly Available; Brosset calls it “a major event in the life of a web feature.”

> “Once it’s implemented everywhere, you should be aware that [it] happened: that’s worth knowing about, that’s worth featuring on the evening news of the web.”  
> **– Brian Kardell, Igalia developer advocate**

“It’s the point in time where a feature truly becomes part of the web platform. The feature is now implemented across all engines which Baseline takes into account. This moment represents a great time for developers to begin working with new features with confidence that they are interoperable. Not all users will be on the latest version of every browser, so Widely Available is intended to provide a stronger guarantee that a feature is available to almost all of a site’s traffic.”

“You can imagine it like a thermometer with degrees of readiness,” Kardell suggests, because the last browser implementing a feature is a useful signal. “Once it’s implemented everywhere, you should be aware that [it] happened: that’s worth knowing about, that’s worth featuring on the evening news of the web. It’s up to you when you use it, but even if it’s only experimental in browsers, this is coming, this is real.”

At the very least, it’s a good time to start learning about new features, because you also have a clear idea of how long it should take to reach Baseline Widely Available (assuming no implementation issues are discovered). Widely Available is more of a moving target than an annual roundup: an acknowledgement that websites take time to build and get updated, so developers will re-evaluate what features are suitable over time.

Kardell suggests the annual Interop announcement each February marks a good time to check in on new features. “You should be looking at that as a developer because it’s very high signal to noise: even if you tried [a feature] before and it didn’t work so well, this is the time you should take a minute and give it a serious look.”

> “If something is in Interop, then it’s a reasonable expectation that it will be Baseline Newly Available by the end of that.”  
> **— Graham, Mozilla**

“If something is in Interop, then it’s a reasonable expectation that it will be Baseline Newly Available by the end of that,” agrees Graham.

“Anchor positioning by the end of this year, hopefully will be Baseline Newly Available and then in the middle of 2028 it will just be Baseline, predicts Igalia web standards advocate [Eric Meyer](https://www.linkedin.com/in/meyerweb/).

The progression from the first implementation in any browser to reaching all four core browsers is much more variable. WebDX CG co-chair [Francois Daoust](https://www.linkedin.com/in/francois-daoust-66668b41/) has created [a timeline of web platform baselines](https://web-platform-dx.github.io/web-features-explorer/timeline/) (going back much longer than the Baseline project has been around, but using the same principles) and some features have taken as long as 240 months. Interestingly, the features that have taken the longest to reach Baseline, Newly Available in 2023 and 2024, are a testament to the way Interop is improving interoperability.

The HTML [summary](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/summary) element for details was first implemented in 2010: the WebKit implementation came in 2019 and Edge didn’t support it until it switched to the Chromium Engine in 2020. Similarly, the [ariaDetailsElements](https://developer.mozilla.org/en-US/docs/Web/API/Element/ariaDetailsElements) property, which Kardell describes as “maybe ten years in the making,” has recently become Baseline Newly Available. “There are a lot of ways to get to Baseline. There’s a continuum: a lot of things will take much longer but still eventually get there. Lots of things are arriving, crawling and panting from exhaustion, but they get there still.”

## Widely Referenced

Baseline isn’t intended to be the final answer on which features you should and shouldn’t use: but it’s there to make it easier for developers to answer that question themselves.

“Early adoption helps push the web forward by creating a healthy feedback loop between implementers and users, and exposing features that are Newly Available helps developers embrace capabilities as they enter broad adoption,” Brosset points out. “Developers have the best view of the mix of devices, browsers and versions visiting their sites, and in many cases they may want to begin deploying or experimenting with features in earlier phases, such as when using them as progressive enhancements. We’re seeing evidence that Baseline Newly Available is helping fill a gap in the community, where developers are having trouble keeping track of the rapid pace of change.”

Helpfully, the information is now available in a lot more places: it’s in the MDN developer documentation, on [CSS-Tricks](https://css-tricks.com/), CanIUse and CanIWebView and in dashboards like the WebDX [Web platform features explorer](https://web-platform-dx.github.io/web-features-explorer/), Google’s [Web Platform Status](https://webstatus.dev/) (which has lists of the annual Baseline features back to 2020), the [Edge 2024 Top Developer Needs](https://microsoftedge.github.io/TopDeveloperNeeds/) that Microsoft compiles as well as independent sites like [Web Platform Features](https://web-features.lttr.cz/). The [State of HTML survey](https://2024.stateofhtml.com/en-US) now includes the Baseline status of features mentioned in each question, which should be a great way to raise awareness.

> “We’re seeing evidence that Baseline Newly Available is helping fill a gap in the community, where developers are having trouble keeping track of the rapid pace of change.”  
> **– Brosset, Microsoft Edge**

There are plenty of ways to keep on track of what’s becoming part of baseline. Google’s Web.Dev has [a monthly update](https://web.dev/baseline#the-baseline-monthly-digest) on Baseline features and news, the WebDX features explorer lets you view features that are [Limited Availability](https://web-platform-dx.github.io/web-features-explorer/limited-availability/), [Newly Available](https://web-platform-dx.github.io/web-features-explorer/newly-available/) or [Widely Available](https://web-platform-dx.github.io/web-features-explorer/widely-available/); and the [monthly release notes](https://web-platform-dx.github.io/web-features-explorer/release-notes/march-2025/) cover what features have reached a new baseline status. [Rick Viscomi](https://www.linkedin.com/in/rviscomi/) from Google’s web performance devrel team has [a more minimal timeline](https://rviscomi.github.io/timebase/) of features getting a Baseline status each month.

But maybe more usefully, Baseline details are showing up right inside tools. Hover over a web feature — CSS or HTML — in VS Code, and the [hover card shows the Baseline status](https://web.dev/blog/baseline-vscode); JetBrains plans to add something similar to [WebStorm](https://www.jetbrains.com/webstorm/nextversion/).

What’s really useful is knowing which Baseline features are available to the people who use your site. You can look at Akamai’s [RUM Insights](https://rumarchive.com/insights/#baseline) to see real user measurements by country, showing which Baseline levels their browsers support — or if you have enough details about their browser usage to know which annual Baseline is a good fit, you can use [the browserslist-config-baseline package](https://www.npmjs.com/package/browserslist-config-baseline) or the [bl2bl Baseline browserslist module](https://github.com/web-platform-dx/bl2bl) to [target](https://web.dev/articles/use-baseline-with-browserslist) that in tools like Autoprefixer, Babel, PostCSS, webpack and Vite. [Give ESLint your baseline target](https://github.com/GoogleChromeLabs/baseline-demos/tree/main/tooling/eslint) and it will warn you if you’re using features newer than that (there’s an [html-eslint](https://github.com/yeonjuan/html-eslint) plugin if you need more than CSS). Stylelint also has a [Baseline plugin](https://www.npmjs.com/package/stylelint-plugin-use-baseline).

If you use [Google Analytics](https://chrome.dev/google-analytics-baseline-checker/), [Netlify](https://app.netlify.com/extensions/baseline) or [RUMvision](https://www.rumvision.com/help-center/monitoring/dashboard/baseline/), you can get recommendations for which Baseline target is the best fit for your visitors, so you can decide whether you need to wait for features to reach Widely Available, or adopt features like container queries and popovers more quickly.

> Useful as Baseline is, it’s not a replacement for using your own judgement on what features to adopt.

Useful as Baseline is, it’s not a replacement for using your own judgement on what features to adopt: just because your linter gives you a [warning](https://github.com/eslint/css/blob/main/docs/rules/use-baseline.md) that a feature in your code isn’t in the Baseline you’re targeting, doesn’t mean you can’t use it. It just means you can tell more easily which features your users are ready for and which will take more work and testing to support.

“We’re seeing very rapid growth in developers’ awareness of what Baseline is,” Brosset agrees. “The word itself is filling a gap in how developers have been talking about the platform. It’s a reassuring flag that helps them make quicker decisions. We’re seeing more and more mentions of Baseline on blogs, social media, and conference talks. Baseline is giving developers a new way to talk about the web platform, which seems to resonate very well with them.”

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://cdn.thenewstack.io/media/2023/12/e2700739-maryb.jpg)

After completing an MSc in Intelligent Knowledge Based Systems in 1990, Mary Branscombe was convinced that promising as the AI techniques she’d been studying were, they weren’t even close to being ready. Since then, she’s been a technology journalist for...

Read more from Mary Branscombe](https://thenewstack.io/author/marybranscombe/)