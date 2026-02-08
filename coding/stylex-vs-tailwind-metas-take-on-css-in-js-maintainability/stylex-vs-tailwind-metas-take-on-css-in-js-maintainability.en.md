Tailwind has [been in the news](https://thenewstack.io/tailwind-creator-says-ai-played-a-role-in-downsizing/) lately, as it struggles to keep its doors open in the AI era. But it’s not the only “CSS-in-JS” solution to compete for developers’ attention. Recently Meta has been promoting its open source, React-based styling project, [StyleX](https://stylexjs.com/). Unlike Tailwind, it’s not a framework — Meta calls it both [a JavaScript library](https://github.com/facebook/stylex) and, more broadly, a “system.” But regardless, StyleX is yet another alternative to directly using the style sheet language CSS (Cascading Style Sheets).

In [a blog post](https://engineering.fb.com/2025/11/11/web/stylex-a-styling-library-for-css-at-scale/) toward the end of last year, Meta’s [Melissa Liu](https://www.linkedin.com/in/mellyeliu/) called StyleX a “styling system for large-scale applications.” Liu is a React components software engineer and a core member of the StyleX project at Meta. In her blog post, she notes that StyleX has become “the standard styling system across Meta products like Facebook, Instagram, WhatsApp, Messenger and Threads, as well as external companies like Figma and Snowflake.”

A quick note about CSS-in-JS: These are solutions in which developers define style using JavaScript, rather than CSS. But at a time when CSS itself is becoming [ever more sophisticated](https://thenewstack.io/web-development-in-2025-ais-react-bias-vs-native-web/) — Google’s [CSS Wrapped 2025](https://chrome.dev/css-wrapped-2025/) listed 22 new CSS features in Chrome last year — why is there a need for Javascript-based styling systems?

At least for Meta, the answer is: scale and code maintainability.

## The Challenge of Styling at Scale

This week, Liu [went on the Meta Tech Podcast](https://engineering.fb.com/2026/01/12/web/css-at-scale-with-stylex/) to discuss StyleX with her colleague Pascal Hartig. She noted that Facebook’s website is made up of “thousands of components” — including, no doubt, a large number of styling components — and it must cope with “hundreds of millions of users” every day. She explained that this kind of complexity and scale demanded a better way to manage styling.

“We also need to think about what’s maintainable from a developer perspective,” she said. “Of being able to have this large code base and make it so that … if someone from the ads team is building a component, that they’re declaring … a button class there; and then, oh, someone from Instagram is also creating a button class….and [so] we need a system … to kind of make it maintainable.”

The implication is that writing CSS code is, by itself, insufficient when it comes to a massive website like facebook.com, not to mention when it integrates with other apps, like Instagram or Threads. The problem here is that CSS is global; if, as Liu said, someone from the Meta ads team changes a button class in CSS, it might inadvertently override or clash with an Instagram button class.

In her blog post, Liu explained the issues with using straight CSS before StyleX (and a precursor named cx) came along:

“Serving CSS at such a scale resulted in collisions across bundles, difficulties in managing dependencies between stylesheets and challenges in reconciling competing rules that frequently led to specificity wars.”

## How StyleX Compares to Tailwind

So how does StyleX work? As noted above, it’s a JavaScript library — and so you’re writing in JavaScript code instead of the CSS language. Since this is Meta, StyleX has been optimized for React, but in [an FAQ](https://stylexjs.com/docs/learn/thinking-in-stylex/) Meta insists that it is framework-agnostic:

“StyleX is a CSS-in-JS solution, not a CSS-in-React solution. Although StyleX has been tailored to work best with React today, it is designed to be used with any JavaScript framework that allows authoring markup in JavaScript.”

> “At its core, StyleX is a compiler that extracts styles at build time and generates a static stylesheet.”  
> **— Melissa Liu, Core StyleX developer at Meta**

Liu noted in her blog post that “at its core, StyleX is a compiler that extracts styles at build time and generates a static stylesheet.” So the end result is CSS, but that comes via JavaScript and the processing of that (into CSS) is done at build time.

Tailwind is also a CSS-in-JS solution, and there are some similarities to StyleX. Tailwind allows the developer to create “utility classes” inside the HTML file, which are then turned into a static CSS file at build. The difference is mostly in the syntax: Tailwind uses its own special classNames, whereas StyleX uses JavaScript objects.

Mainly because of its unique syntax, maintainability has long been a contentious issue with Tailwind. In [a 2023 article](https://thenewstack.io/tailwind-css-debate-another-cool-tool-dissed-by-web-purists/), I noted that many developers dislike the ugly markup that Tailwind imposes on HTML, which in turn makes the codebase more difficult to maintain.

Although Liu only briefly mentioned Tailwind on the Meta Tech Podcast, she seems to have the same concerns about maintainability. She acknowledged that developers love how quick it is to work with, but adds that “you lose out on maintainability with systems like Tailwind.”

> “While Tailwind is very much CSS-in-JS, as a syntax, it’s not very good at being CSS-in-JS.”  
> **— Naman Goel, Core StyleX developer at Meta**

Others in the StyleX team are more critical. One of the co-creators of StyleX (and still a core developer), [Naman Goel](https://www.linkedin.com/in/naman-goel-66747242/), wrote [a post on his personal blog](https://nmn.sh/blog/2025-09-14-tailwind-is-css-in-js) last September arguing that Tailwind is “bad at being CSS-in-JS” because of its syntax:

“While the className abstraction is great for quickly prototyping styles, it falls apart outside of the common use-cases. Writing CSS keyframes, view transitions, anchor positioning and anything out of the ordinary means reaching for an actual CSS file.”

Of course, web standards advocates would say there’s nothing wrong with [going back to the source code](https://thenewstack.io/css-frameworks-in-vogue-but-dont-forget-style-fundamentals/): CSS. But Goel’s point is that with StyleX, you can (apparently) cover all your styling needs with JavaScript.

## The Rise of Atomic CSS

As Goel notes in [a follow-up post](https://nmn.sh/blog/2025-09-16-serving-atomic-styles), both StyleX and Tailwind are examples of what’s become known as “atomic CSS” styling. According to the documentation of yet another CSS-in-JS solution, called [Compiled](https://compiledcssinjs.com/), [atomic CSS](https://compiledcssinjs.com/docs/atomic-css) is “a method of reducing the total amount of defined rules by creating a single rule (and in turn, a unique class name) for every declaration – enabling large style re-use.”

> “At the heart of StyleX is its static compilation into atomic CSS.”  
> **— Liu**

For StyleX, atomic CSS is a key part of its solution. Per Liu’s blog post:

“At the heart of StyleX is its static compilation into atomic CSS. Styles are converted to classes containing a single style declaration for reuse across a codebase so CSS size plateaus as the application grows.”

In his post about atomic CSS, Goel points out that there are various ways “to bundle and serve atomic CSS.” But again, this seems to be applicable only to websites or applications that have a certain, very rare, scale. Even Goel admits that usually a single CSS file works best:

“Having a single CSS bundle for your entire web app is almost always a decent solution. If Facebook.com can get away with it, it’s probably fast enough.”

## What’s Next for StyleX?

At the end of 2025, StyleX launched a new website. Accompanying it was [a blog post](https://stylexjs.com/blog/a-new-year-2026), credited to both Goel and Liu. They wrote that the “new website is built with Waku, a minimal React framework that lets us benefit from, and showcase StyleX’s compatibility with React Server Components.” ([The New Stack profiled Waku](https://thenewstack.io/new-framework-lets-devs-explore-react-server-components/) a couple of years ago, soon after it came out.)

The pair added that in 2026, StyleX will get “better ergonomics, new feature work, and developer tooling.”

StyleX is a CSS-in-JS system to keep an eye on, especially if you’re deep in the React ecosystem. But unless you’re running a website or app the scale of Facebook.com, you’re probably better off sticking with Tailwind or (even better) dealing directly with the CSS language.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://cdn.thenewstack.io/media/2020/03/1c7152c0-ricmac_highres_w400_h400.jpg)

Richard MacManus is a Senior Editor at The New Stack and writes about web and application development trends. Previously he founded ReadWriteWeb in 2003 and built it into one of the world’s most influential technology news sites. From the early...

Read more from Richard MacManus](https://thenewstack.io/author/richard/)