# Interop Unites Browser Makers To Smooth Web Inconsistencies
![Featued image for: Interop Unites Browser Makers To Smooth Web Inconsistencies](https://cdn.thenewstack.io/media/2025/04/1170f22e-philip-oroni-jmmjzoxngj0-unsplash-1024x683.jpg)
For [the last four years](https://thenewstack.io/browser-vendors-aim-to-heal-developer-pain-with-interop-2022/), the major browser vendors, web standards creators and other contributors to browser engines have joined together to improve the interoperability of the web, coordinating improvements to inconsistent browser implementations so it’s easier to make websites and apps that work the same way in every browser and on different devices.

“When you ask developers about their biggest pain points, it’s usually related to the inherent challenge on the web platform: that it’s not shipped by a single vendor. It’s a very unique thing that the web is shipped by multiple vendors,” points out [Kadir Topal](https://www.linkedin.com/in/kadirtopal/), who works on the web platform at Google. “That leads to the biggest pain point developers have: that things don’t work the same across browsers.”

## Refining the Web
A lot of the interoperability work goes into refining features that have already been specified and shipped, but increasingly, the goal is to ensure newer features are interoperable as they arrive.

As [Philip Jägenstedt](https://www.linkedin.com/in/foolip/?originalSubdomain=se), a software engineer on the web platform team at Google, puts it, “We have two legs we’re standing on in Interop: fixing the old and making sure the new doesn’t need fixing in the future.”

Take the [View Transitions API](https://developer.mozilla.org/en-US/docs/Web/API/View_Transition_API), which is one of the 2025 focus areas. It hasn’t yet shipped in all browsers so it’s not yet part of the web platform [Baseline](https://thenewstack.io/what-does-it-mean-for-web-browsers-to-have-a-baseline/). The goal of including it is to bring it to Baseline, with Interop making sure the testing is sufficiently thorough. “Even though we don’t know exactly what problems developers are going to run into, we test it very well and make sure all the tests are passing on all browsers so we can have much higher confidence than in the past that they’re not going to run into as many things.”

“We have two legs we’re standing on in Interop: fixing the old and making sure the new doesn’t need fixing in the future.”

– Philip Jägenstedt, web platform team at Google
The original impetus for Interop came from “the surprise that a lot of what developers were most frustrated by wasn’t the things that we were thinking — that you can’t style a button or we didn’t have container queries — but the interoperability problems that everyone who writes code bumps up against,” explained Igalia developer advocate [Brian Kardell](https://www.linkedin.com/in/brian-kardell-08a4264/). The bigger frustrations were due to “stuff that was supposed to work for a long time that just didn’t work interoperably.”

Thanks to Interop, “those forever things do get fixed,” Topal said. “There are fewer of those things, so it gives us more of an opportunity to focus on being proactive.”

**Better Together**
The areas to focus on each year are chosen from studies, surveys and [developer feedback](https://github.com/orgs/web-platform-tests/projects/5/views/1?filterQuery=), and progress is measured not by how many web platform tests (WPTs) in those areas individual browsers can pass but by the number of tests that pass in all the browsers, a final result that’s been steadily improving year by year.

Back in 2021, this interop score started at just under 65% and finished at just under 89%. For Interop 2024, the final scores for both measures were high across all 17 focus areas, with the four main browsers hitting 99% and the common interop score reaching 97 (up from an initial 62) — the highest so far. “All of the areas saw significant improvements,” said Igalia web standards advocate [Eric Meyer](https://www.linkedin.com/in/meyerweb/).

“All of the areas saw significant improvements.”

– Eric Meyer, Igalia web standards advocate
This year, the scope of Interop is “quite a lot bigger,” according to Jägenstedt. It also includes focus areas with much more room for improvement.

The starting interop score of 27.5% doesn’t mean the web has suddenly gotten more broken. The 19 focus areas in Interop 2025 include a mix of features where all the browsers receive reasonable scores individually but also all have different areas to catch up on, features that one or two browsers haven’t yet implemented fully (or in some cases, at all, like the navigation API), and areas where either the feature itself or the tests for it are relatively new (like the [WebAssembly focus area](https://thenewstack.io/top-5-uses-of-webassembly-for-web-developers/)).

They also include major features like anchor positioning, view transitions and the navigation API. While the specification for this is relatively new, “the need for something that addresses what that specification addresses has been around forever,” Meyer noted.

Giving web developers better ways to handle navigation inside a complex web application without hijacking the back button will make both developers and users happier.

This is particularly useful for frameworks and for complicated, sophisticated web apps that intercept navigation and update the page instead of loading a new one. “The existing APIs the web has for handling history, like back and forward, are full of bugs and edge cases that we can’t fix because it would break existing sites,” Jägenstedt explained.

“The navigation API is a clean model that actually works, that doesn’t have those bugs, that developers can use to reliably intercept navigations and update the page instead of doing a full reload.” Currently, frameworks and apps do that manually, and probably have bugs in how they do it.

With view transitions, developers can animate smooth transitions between different views and states in a web application. Think of an ebook with pages that turn like in a real book, or a blog with the same kind of swipe and cross-fade transitions you can apply in a slide deck as you open and close articles or click on images to see a larger version. (And if that sounds annoying, telling your browser you prefer reduced animation will turn most of this off, Meyer noted.)

“More importantly, this brings us closer to having cross-document transitions in all browsers, which will eventually make it easier for developers to go with multipage web apps, which browsers are extremely well optimized to handle,” suggested [Kyle Pflug](https://www.linkedin.com/in/kylepflug/), group product manager on Microsoft Edge.

Anchor positioning is another newer feature: including it in Interop means that by the end of the year, all the browsers should have interoperable implementations of a way to create tool tips, anchored side notes, pop-ups anchored to something on the page, and other ways of linking content.

“You could have the thing you want to have pop up at the end of the document, like footnotes, and when somebody mouses over the superscript, the content is positioned right next to it, and then when the mouse goes away, the pop-up goes away and the footnote goes back to the end,” Meyer explained. “You could do the same with side notes if you couple anchor positioning with scroll transitions. You don’t have to know exactly where that thing will be on the screen; you just say ‘put yourself underneath that thing.’”

“Once CSS anchor positioning is interoperable, developers won’t have to use tool-tip libraries, or maintain their own.”

– Kyle Pflug, group product manager on Microsoft Edge
“Once CSS anchor positioning is interoperable, developers won’t have to use tool-tip libraries, or maintain their own. Displaying and positioning tool tips will be easy, fast and won’t require JavaScript,” Pflug added, also noting that “the work done on improving the <details> element will make it possible for developers to use HTML and CSS only to display, and animate, accordion-like components in their apps.”

Anchor positioning also enables something web developers want very much, Jägenstedt predicted: “customizable <select> elements where you can put whatever you want and see your options.”

“If we ask web developers what they don’t love about the web, they say ‘form styling.’ If we say, ‘What do you mean?’ they say ’select.’ If we say, ‘What do you mean?’ they say ‘I want little flags next to each of my options.’ They want customizable select: That’s very close to the top of [developer] pain points, and anchor positioning is on the blocking path to delivering that.”

**Faster, Easier, More Private**
The Core Web Vitals APIs come out of [Google’s work to measure user experience](https://developers.google.com/search/docs/appearance/core-web-vitals) on web pages, like performance and interactivity. Google Search has used these quality signals for page ranking, but performance is something most web developers care about, and it’s useful if the browser can give you key metrics about how quickly pages load, how responsive pages are when users try to click or scroll, or whether the page layout jumps around as different elements load.

Having Firefox and Safari offer ways to get the same metrics developers already get in Chromium browsers will help developers check that performance is consistent across different browsers and devices.

“Performance is a big deal: When web performance increases, people’s happiness using the site increases.”

– James Graham, Mozilla web compatibility engineer
“If we have these really great performance monitoring APIs and they work really well across browsers, then it’s much easier for web authors to check that their site performs across browsers. Performance is a big deal: When web performance increases, people’s happiness using the site increases,” Mozilla web compatibility engineer (and long-time member of the WPT project) [James Graham](https://hacks.mozilla.org/author/jgrahammozilla-com/) points out.

As with [JavaScript](https://thenewstack.io/javascript-due-for-new-time-date-and-set-features-next-year/), CSS is increasingly receiving native features that once required tooling, like [Sass](https://sass-lang.com/) (and an extra build step). When you’re using complex CSS rules, scope lets you apply styles to only certain areas of the page.

“Vue and Svelte make it so you could write CSS in your component and it just applies to that component, and this scoping is often done by generating a class and applying it to each thing, but it would be nice if people didn’t need to use build tools for CSS,” explained Ecma president [Daniel Ehrenberg](https://www.linkedin.com/in/danielehrenberg/). “Letting you author in the language that’s supported by the browser always ends up having benefits: The feature comes out better when it’s done natively.”

WebRTC (real-time communication) underpins video conferencing on the web. Instead of needing a native app for every service you get meeting invitations from, you can just click on a URL to join a video call. But Graham points out that “the level of adherence to standards hasn’t necessarily been as good as the rest of the platform.” In particular, end-to-end encryption with WebRTC has depended on proprietary systems present in some but not all browsers. “Now we have a standard for it.”

The [RTCRtpScriptTransform](https://developer.mozilla.org/en-US/docs/Web/API/RTCRtpScriptTransform) API allows scripts to modify the media stream in a call. Graham described it as one of the one of the prerequisites for end-to-end encrypted video calls.

The focus area also covers transferring WebRTC data channels to workers, moving data processing off the main thread. WebRTC will need more interoperability work in future years, but this is the first time it’s been part of Interop, and “it’s really promising that we’re taking that first step.”

Video conferencing on the web will also benefit from the backdrop filter focus area. If you decide to blur out your video background, that’s how it’s done. But it also handles effects applied to a web page when a dialog is open, whether that’s blurring out an article while a visitor signs in or having tools that float over the page without obscuring it completely.

“You might have a sticky masthead that’s always at the top of the page, no matter how far you scroll up or down, but you might want everything behind it to be blurry,” Meyer suggested. “You can apply whatever filter you want to whatever’s behind it.”

The ongoing saga about third-party cookies is a reminder of the trade-offs between security, privacy and convenience.

The ongoing saga about third-party cookies is a reminder of the trade-offs between security, privacy and convenience. That can be contentious when it means browsers limiting the things that web developers could do previously.

Browsers want to be able to partition storage so that it’s harder to track users. Setting a third-party cookie on one site that another site can access is a trivially easy way to track users as they travel around the web.

“Unfortunately, it turns out that some important workflows depend on having that work,” Graham explained — in particular, authentication. “If you have a single-sign-on provider, you don’t want to have to sign on again for every different subdomain because that defeats the whole point.”

Similarly, if a user wants to click “like” on a YouTube video embedded in an iframe on a web page, they probably don’t want to have to log in to YouTube every time.

The Storage Access API allows sites to opt in to unpartitioned storage for cookies if necessary. “For the vast majority of cases we can nicely partition user data according to which site set that user data, but in these few cases where it’s a really important part of the workflow that we send the cookies to your authentication provider, you can say, ‘It’s okay, send those cookies to my authentication provider.'”

Storage access may be a low-level detail, but Graham expects an API that makes interacting with services more seamless, without leaking significant amounts of user data, that all the browsers are happy to implement, to bring real improvements in privacy. “If you start breaking user workflows, then it’s likely I’m prepared to give up privacy because I need this workflow to work, but that’s not a trade-off we want people to have to make.”

**Fixing the Forever Bugs**
There are far fewer of the long-standing cross-browser layout compatibility issues that were such a big part of Interop in the first few years, but the web compatibility focus area will continue to be a regular part of Interop. “This is a collection of bugs or smaller features where the motivation is that we’ve seen this break real sites in some way.” Graham suggested the value of Interop is how “it provides a framework for fixing bugs across the whole platform, as well as just incentivizing new features.”

Interop “provides a framework for fixing bugs across the whole platform, as well as just incentivizing new features.”

– Graham, Mozilla
Flexbox and grid focus areas have been in Interop for several years (with significant improvements every year). Pflug calls them “incredibly important building blocks for modern layouts, and although they are intended to be simple to use for developers, there is a ton of complexity that browser engines need to deal with.” He added, “The flex and grid sizing and placement algorithms are highly complex and have to work everywhere: within tables, multicolumns, list items, nested into each other, with different writing modes, with images in them, when you resize the page, with overflow content, etc.”

There are still some loose ends to tidy up, and the Edge team is working on fixing a subtle issue with static positioning and alignment that affects flexbox scenarios with and without grid.

“If an [absolute-positioned](https://nam04.safelinks.protection.outlook.com/?url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2Fposition%23absolute&data=05%7C02%7Cmary%40sandm.co.uk%7Cf2aa03258ae649cb286308dd7212b8d8%7C37c7766d87874f888075ac2e2ccaac3c%7C0%7C0%7C638792146957016155%7CUnknown%7CTWFpbGZsb3d8eyJFbXB0eU1hcGkiOnRydWUsIlYiOiIwLjAuMDAwMCIsIlAiOiJXaW4zMiIsIkFOIjoiTWFpbCIsIldUIjoyfQ%3D%3D%7C0%7C%7C%7C&sdata=IDs4u9PeSO8e%2F25zec7rrKtvGsRJJQPPmj74gfV3Wv0%3D&reserved=0) or [fixed-positioned](https://nam04.safelinks.protection.outlook.com/?url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2Fposition%23fixed&data=05%7C02%7Cmary%40sandm.co.uk%7Cf2aa03258ae649cb286308dd7212b8d8%7C37c7766d87874f888075ac2e2ccaac3c%7C0%7C0%7C638792146957049855%7CUnknown%7CTWFpbGZsb3d8eyJFbXB0eU1hcGkiOnRydWUsIlYiOiIwLjAuMDAwMCIsIlAiOiJXaW4zMiIsIkFOIjoiTWFpbCIsIldUIjoyfQ%3D%3D%7C0%7C%7C%7C&sdata=607ZKx0geqwc2oeYO%2F2Du%2FasXdEwh7MLK9HASNj2838%3D&reserved=0) element is positioned using its [static position](https://nam04.safelinks.protection.outlook.com/?url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2Fposition%23static&data=05%7C02%7Cmary%40sandm.co.uk%7Cf2aa03258ae649cb286308dd7212b8d8%7C37c7766d87874f888075ac2e2ccaac3c%7C0%7C0%7C638792146957071380%7CUnknown%7CTWFpbGZsb3d8eyJFbXB0eU1hcGkiOnRydWUsIlYiOiIwLjAuMDAwMCIsIlAiOiJXaW4zMiIsIkFOIjoiTWFpbCIsIldUIjoyfQ%3D%3D%7C0%7C%7C%7C&sdata=AZ6Us8AJO%2Bf5%2FHY1ahh21BK2jUC6LRUhwGVfj9p4pgM%3D&reserved=0), that static position takes alignment into account. [Alignment properties](https://nam04.safelinks.protection.outlook.com/?url=https%3A%2F%2Fdrafts.csswg.org%2Fcss-align-3%2F%23overview&data=05%7C02%7Cmary%40sandm.co.uk%7Cf2aa03258ae649cb286308dd7212b8d8%7C37c7766d87874f888075ac2e2ccaac3c%7C0%7C0%7C638792146957093550%7CUnknown%7CTWFpbGZsb3d8eyJFbXB0eU1hcGkiOnRydWUsIlYiOiIwLjAuMDAwMCIsIlAiOiJXaW4zMiIsIkFOIjoiTWFpbCIsIldUIjoyfQ%3D%3D%7C0%7C%7C%7C&sdata=wU%2BDQm6V%2F9IyetuUVnfcNhEFw27rPE3Yi2RkfuLbycU%3D&reserved=0) can take a ‘[safe](https://nam04.safelinks.protection.outlook.com/?url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2Foverflow-position%23safe&data=05%7C02%7Cmary%40sandm.co.uk%7Cf2aa03258ae649cb286308dd7212b8d8%7C37c7766d87874f888075ac2e2ccaac3c%7C0%7C0%7C638792146957114581%7CUnknown%7CTWFpbGZsb3d8eyJFbXB0eU1hcGkiOnRydWUsIlYiOiIwLjAuMDAwMCIsIlAiOiJXaW4zMiIsIkFOIjoiTWFpbCIsIldUIjoyfQ%3D%3D%7C0%7C%7C%7C&sdata=XEZagNJuqOX8u97QRMqibYu%2FHfltY%2F4lml3JCoT%2Fa%2BA%3D&reserved=0)‘ keyword that says if the item being aligned overflows the alignment container, the browser should align the item as ‘start’-aligned instead (to avoid overflow on the left edge of the viewport).”

But “[safe](https://nam04.safelinks.protection.outlook.com/?url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2Foverflow-position%23safe&data=05%7C02%7Cmary%40sandm.co.uk%7Cf2aa03258ae649cb286308dd7212b8d8%7C37c7766d87874f888075ac2e2ccaac3c%7C0%7C0%7C638792146957137389%7CUnknown%7CTWFpbGZsb3d8eyJFbXB0eU1hcGkiOnRydWUsIlYiOiIwLjAuMDAwMCIsIlAiOiJXaW4zMiIsIkFOIjoiTWFpbCIsIldUIjoyfQ%3D%3D%7C0%7C%7C%7C&sdata=fzXy3gVhZasyC3F%2B4a0jxXAbOgPVL5vp7g%2BqDXcanh4%3D&reserved=0)” isn’t currently taken into account for this scenario in Edge and Chrome, and it turns out [the spec isn’t entirely clear](https://github.com/w3c/csswg-drafts/issues/11934) about what should happen, which leads to the flex/grid test cases failing, he explained.

“This is a bit of a subtle case that many developers won’t run into, but it’s a good example of how a lot of Interop work plays out. In practice, improving interoperability requires chasing down corner cases like this to ensure they are handled consistently, so developers don’t have to worry about confusing snags when trying to get their code working across all browsers.”

Similarly, there’s a focus area making sure all the browsers *remove* a feature or two. Three old mutation events for watching the DOM for changes have been deprecated for well over a decade and replaced by the far more useful Mutation Observer API.

Similarly, browser makers decided at least 15 years ago that vendor-specific prefixes were a bad idea. This year, Interop will do a bit more to keep replacing them by making sure developers can set the style and color of decorative lines (like underlined text or strikethrough) using the text-decoration CSS property (implemented in enough browsers to count as widely available in Baseline) without needing a vendor prefix in Safari.

“These small things often get overlooked because ‘oh, that’s trivial, we could do that in our spare time’; now it’s on the list of things to get done.”

– Meyer, Igalia
Meyer is glad to see Interop include cleanup like this: “These small things often get overlooked because ‘oh, that’s trivial, we could do that in our spare time’; now it’s on the list of things to get done.”

There’s also a reminder of how very far we’ve come since the ‘browser wars’ of the web’s early years: Graham calls the CSS Zoom focus area “the canonical example of something that took much longer than it should have done.”

A proprietary feature in Internet Explorer that Microsoft built before CSS transforms were available — to give the web version of Excel the same zoom experience as the desktop app — was reverse engineered and implemented in WebKit reverse (a lot of Mac users need Office), but it still wasn’t a standard, and Mozilla’s attempts to support it fixed some sites and broke others.

“We went through a whole process with Google to see if we could remove it from the platform if nobody wanted to standardize it. And it turned out no, we can’t remove it — but if we work together, we can figure out a practical way of standardizing when we hadn’t been able to before.”

Now there’s a new [specification](https://nam04.safelinks.protection.outlook.com/?url=https%3A%2F%2Fdrafts.csswg.org%2Fcss-viewport%2F%23zoom-property&data=05%7C02%7Cmary%40sandm.co.uk%7Cb1335944d62d4a8b135b08dd6af7dea0%7C37c7766d87874f888075ac2e2ccaac3c%7C0%7C0%7C638784335019821572%7CUnknown%7CTWFpbGZsb3d8eyJFbXB0eU1hcGkiOnRydWUsIlYiOiIwLjAuMDAwMCIsIlAiOiJXaW4zMiIsIkFOIjoiTWFpbCIsIldUIjoyfQ%3D%3D%7C80000%7C%7C%7C&sdata=FT2268qv5YsesN2jNt5vfIoKK3pGpW61MANPsKzArUE%3D&reserved=0) in the [W3C CSS working group](https://thenewstack.io/a-hotter-pink-css-devs-get-an-explosion-of-new-colors/), and all the browsers are now implementing that.

**Going Further**
The investigation areas in Interop look at how to include things that have been suggested for Interop but can’t be tested. Sometimes it’s because the specification is still changing rapidly (or there isn’t a specification for a particular feature), and that has to go back to the relevant standards group.

Sometimes it’s because new tests need to be written, but often it’s about figuring out how to create and run tests for features where WPT doesn’t already have the testing infrastructure, particularly for mobile or gaming devices. Many tests look at page content, but that isn’t enough to test, say, how touch scrolling performs. That has to be done at a different layer of the browser stack.

“It turns out there’s a bunch of technical challenges on mobile that don’t exist on desktop.”

– Graham, Mozilla
“Why are you running all your tests on desktop when so much browsing goes on on mobile? It turns out there’s a bunch of technical challenges on mobile that don’t exist on desktop,” Graham pointed out. Running the tests on an emulator or a mobile simulator or even on a mobile device can solve that, although at the cost of an extra layer of complexity.

“But it also turns out things we depend on for test automation don’t necessarily work on mobile.” Some tests rely on setting a viewport to a certain size. That’s not always possible on mobile. Gecko has a specific mode in the rendering engine for testing that gives more control over options like the viewport; will other browsers need something similar?

“There are all these technical challenges to figure out what can we even do that works across all browsers.”

That’s why mobile testing is one of the 2025 investigation areas, which might allow frequently proposed features like pointer events to finally become an Interop focus area, although ironically they might only be tested on mobile — because while Windows touch laptops are relatively common, that’s not an option for desktop Safari.

This approach has worked well in previous years, with investigations enabling new focus areas next time around. Interop 2024 included an investigation area on Wasm, because Wasm and JavaScript testing have been done outside WPT and Interop is about tests that run on the WPT infrastructure.

This year’s Interop includes a Wasm focus area that covers things like giving WebAssembly resizable buffers.

Thanks to that work, this year’s Interop includes a Wasm focus area that covers things like giving WebAssembly [resizable buffers](https://thenewstack.io/whats-new-for-javascript-developers-in-ecmascript-2024/) and equivalents of JavaScript’s string processing primitives so developers don’t have write the same glue code to import them over and over again.

These large complex areas are likely to keep coming back. The [accessibility investigation in Interop 2023](https://thenewstack.io/how-interop-2023-will-move-the-web-forward/) built on an extension to WebDriver that allowed testing more of the accessibility stack and created new tests and infrastructure for running them, so Interop 2024 could include an accessibility focus area that finished with all the browsers passing 998 out of 1000 tests.

There’s [another accessibility investigation](https://github.com/web-platform-tests/interop/issues/866) this year, again looking at how to further extend what accessibility features can be tested. In a related area, the [WebVTT investigation area](https://github.com/web-platform-tests/interop/issues/866) is looking at why major video sites don’t use this standard for subtitles and other text displayed next to videos — which is easy for accessibility tools to work with and supports picture-in-picture, but is implemented too differently between browsers to be useful.

The [privacy investigation area](https://github.com/web-platform-tests/interop-privacy) in Interop 2025 is an extremely early look at how privacy features in browsers could be tested when different browsers implement very different protections. Pieters described it as “finding common ground and seeing how to test various privacy related standards.”

**Setting Pragmatic Priorities**
The Modules focus area in Interop 2025 covers what Ehrenberg termed “a small corner” of [the wider modules work](https://thenewstack.io/5-ways-javascript-is-improving-modules-for-developers/) going on in ECMAScript: specifically, the Import Attributes feature that gives a browser (or a bundling tool) more information about a module, like whether it’s JSON (or something else like CSS), so it can both bundle it efficiently and protect you if it turns out the module had been tampered with and is trying to load other code.

This is a feature most browsers are just starting to implement: “It’s landed in the HTML spec, and getting it fully out there to everybody would be really great.”

The Interop work here focuses specifically on JSON imports. That’s because it’s what the web developers who suggested this as an area for Interop to look at asked for, and it’s a good example of how Interop both provides focus and stops what might look like smaller issues from slipping under the radar.

With the sheer number of features in the web platform (depending on how you count subtests, WPT has up to 2 million tests to cover those), there will always be areas where browsers aren’t fully interoperable (the CSS working group alone has over 3,000 open issues) and Interop is very much an exercise in setting priorities as a pragmatic way of tackling that surface area.

“We have these massive tests. The bugs are in there, so you could just fix them,” but Graham pointed out multiple problems with that naïve approach. Browsers aren’t expected to pass every test. Even Google’s resources aren’t infinite, and many tests browsers fail have no impact on web users (tests for, say, an ambient light sensor API deprecated for privacy reasons).

Plus, browser engineers are still developers who want to work on more than maintenance. “If you only do those things, it’s soul-crushing,” Kardell warned. “You don’t want to be spending two months fixing the last table bug that makes absolutely no difference to anyone in on the internet when you could be spending that time making anchor positioning work that a whole bunch of people are going to be really excited about.”

“The point of Interop is to pick these things where everybody can agree this is a really important area that’s worth pursuing this year…”

– Graham, Mozilla
“The point of Interop is to pick these things where everybody can agree this is a really important area that’s worth pursuing this year and we should come together as the web platform community to make this better,” Graham explained. “We’ve looked at the tests and agreed that they’re meaningful tests, that they’re things authors really want. So, by passing these tests, we should end up with really solid implementations in ways that are important, not just to make web developers happy but to make people using the web happy.”

Of course, there are always areas where web developers would like to see progress that don’t get included in Interop (the Temporal JavaScript feature isn’t there and there are no MathML issues on the list, for example — a technology that is still [moving slowly](https://www.igalia.com/2024/12/17/MathML-2024.html)) and haven’t yet been tackled in investigation areas.

“We consistently hear that there are hundreds of features that developers want to see be part of the Interop effort,” Pflug noted, calling prioritization a “significant challenge.”

Different participants pick focus areas to champion: presenting data to show what needs improving, why it should be a priority and that the right tests are in place to validate that working on it will actually make the web more interoperable.

“Championing a focus area entails presenting supporting evidence throughout the process for why the focus area needs to be improved and why it is a priority compared to other areas. It also comes with the responsibility of defining Web Platform Tests to validate that this work did indeed make the web more compatible.”

**Balancing Transparency and Reality**
The detailed discussions, vetoes and even who champions what areas stay private. Some web developers find that frustrating (and it’s obviously tempting to draw conclusions about the politics of browser development from what is and isn’t included), but this is what it currently takes to get consensus between browser companies who still compete with each other.

“In modern life, the web is in everything somehow, so the scope is enormous.”

– Brian Kardell, Igalia
“The use cases of the web platform are literally everything, and the stakeholders in the web are everyone. In modern life, the web is in everything somehow, so the scope is enormous,” added Kardell. “Honestly, the fact that it’s come this far is astonishing and wonderful and slightly terrifying! The work of Interop is to somehow simplify this Venn diagram and coalesce all these shapes into some nice overlapping efforts, which is surprisingly hard and, to be totally honest, leaves a lot out in the cold, but it’s really nice to celebrate all of these things that we get done.”

“The things that don’t get chosen: I’m on the committee, I know the discussions that happen and they don’t get chosen because it’s complicated.”

“Interop is a process with a few organizations leading it,” Ehrenberg agreed, “but I think that’s necessary, because these are technically detailed decisions they’re making that we can’t just put to a vote. They’re also decisions that involve committing resources, so the people committing the resources need to be involved in making the decision.”

Microsoft and Google both talk about wanting more transparency in the process, and the Edge [Top Developer Needs dashboard](https://microsoftedge.github.io/TopDeveloperNeeds/) is one attempt to track long-running developer complaints (some of which do become focus areas in Interop).

“We strive to design in public. We think open debates are not just a side effect: They’re a very integral part of making the web better,” said [Shruthi Sreekanta](https://www.linkedin.com/in/shruthi-sreekanta-8974b94/), a technical manager working on ecosystem strategy at Google. But she readily admits “consensus is a very valuable part of that process.”

And just because a proposal doesn’t become an Interop focus area (perhaps because one browser is busy working on a different subsystem that would mean doing the work twice) doesn’t mean other browsers can’t work on the feature anyway now they know there’s an issue.

Getting browser makers to agree on these priorities has proved to have unexpected benefits, suggests Mozilla web standards engineer Simon Pieters. “Effectively, we align on road maps for a subset of things that we work on, which is good both for browser vendors, but also for web developers because they get to be able to start using a given feature sooner if everyone implements them in the same year.”

“Interop is actually changing the reality of the web.”

– Kadir Topal, web platform at Google
Having multiple browsers implement a feature means multiple teams looking at the same specification from different viewpoints, which is the best way to discover whether the specification is clear enough — and that the tests actually cover the right things. “Each participant is coming at it with different priors and backgrounds and experiences, and when you bring those together, you find things you would have missed,” Graham added.

Specifications improve with every implementation, and when an issue turns up and the specification needs clarifying or tests need changing, the same browser engineers are still assigned to the project, and close enough to the work to be able to update their implementation to match — which means features not only ship faster but also ship interoperably.

“Interop is actually changing the reality of the web,” Topal argued. After two decades during which web developers had no good way to petition browser vendors to prioritize shipping a given technology, Interop offers them a venue, Jägenstedt agreed. “There are now dozens of features that are now part of the web platform that weren’t there before, because somebody took the time to send a proposal, and we looked at that and decided collectively that, yes, this is a priority.”

In theory, there’s a logical path for interoperable browser features to follow from specification to being ready for mainstream use after 30 months of robust cross-browser support, with the annual Interop process and the regular updates to [Baseline](https://thenewstack.io/what-does-it-mean-for-web-browsers-to-have-a-baseline/) as stages on the journey. In practice, things are rarely that straightforward, but the collaborative Web Platform Tests project underpins all these different stages. We’ll be taking a deep dive into that in a future article.

[
YOUTUBE.COM/THENEWSTACK
Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.
](https://youtube.com/thenewstack?sub_confirmation=1)