Thirty years ago, Netscape engineer Brendan Eich famously created a new client-side scripting language [in just ten days](https://thenewstack.io/brendan-eich-on-creating-javascript-in-10-days-and-what-hed-do-differently-today/). It was initially called Mocha, but by the end of the year it would be renamed JavaScript. In 1995, nobody could’ve predicted that JavaScript would become the [world’s most popular programming language](https://survey.stackoverflow.co/2024/technology#most-popular-technologies). But that’s exactly what happened.

How did JavaScript become the defining technology of the modern web? In this article, we’ll look at ten milestone moments in JavaScript’s 30-year history. It’s remarkable how much the JavaScript ecosystem — and by extension the web ecosystem — has expanded and transformed during that time.

## **1. 1995: Adding Interactivity to the Web**

The first key moment was, of course, those ten days in May 1995. The idea was to create a Netscape equivalent to Microsoft’s Visual Basic — a web language that was easy for beginner developers, web designers and DIY folks to use. Or as Brendan Eich himself later put it, “there was a need for a language that was approachable, that you could put directly in the web page.”

Putting into the web page, in practical terms, meant using a scripting language to create client-side programs that ran inside the Netscape browser. The name JavaScript was largely a marketing term devised by Netscape and Sun Microsystem executives. But there was a kind of logic to it: JavaScript would be for designing small interactive effects — such as form validation or animated buttons — while Java would be for developing more complex web components.

[JavaScript was publicly announced](https://cybercultural.com/p/1995-the-birth-of-javascript/) at the end of 1995, as part of Netscape’s beta launch of its Navigator 2.0 browser.

## **2. 1997: ECMAScript 1.0**

Over 1996, early developers and webmasters began to experiment with JavaScript. At first, JavaScript was put to use in fairly trivial ways — scrolling text, silly animations, tricks with colors (fading, rainbow effects, and so on). Eich himself later referred to [these types of JS features](https://cybercultural.com/p/1996-javascript-annoyances-and-meeting-the-dom/) as “annoyances.”

But by 1997, [JavaScript had become a sophisticated language](https://cybercultural.com/p/1997-javascript-apps-dynamic-web/) — with new features like Netscape’s layers adding a further dynamic dimension to its capabilities. By this time Microsoft had [its own version of JS](https://cybercultural.com/p/1996-microsoft-activates-the-internet-with-activex-jscript/) called JScript; since JavaScript was open source, Microsoft had been free to copy and tweak JS to suit its Internet Explorer browser. Netscape, Microsoft and other companies then agreed to have an impartial specification produced, via a standards body called Ecma International. The first [ECMA-262 specification](https://ecma-international.org/wp-content/uploads/ECMA-262_1st_edition_june_1997.pdf) (nick-named ECMAScript) was published in June 1997, giving JavaScript a neutral roadmap.

## **3. 1999: XMLHttpRequest Debuts**

This is where things get really interesting for JavaScript — but curiously it was Microsoft that provided a great technical leap forward, not Netscape.

Internet Explorer 5 quietly introduced a technology called XMLHttpRequest, letting scripts [fetch data in the background](https://medium.com/@mohamedtayee3/make-an-http-request-in-javascript-with-xmlhttprequest-xhr-e08f8c79a9d1). It was an API in the form of a JavaScript object, using asynchronous calls to enable pages to update without full refreshes. It was the seed of what would later be called Ajax.

One of the Microsoft engineers responsible for this technology, Alex Hopmann, [later explained](https://web.archive.org/web/20090130092236/http://www.alexhopmann.com/xmlhttp.htm) that they created the technique for use in a web version of Outlook. When it came time to include XMLHttpRequest in IE5, it was added as part of the MSXML library (Microsoft XML Core Services). Hopmman said that’s where the “XML” part of the name comes from — “the thing is mostly about HTTP and doesn’t have any specific tie to XML other than that was the easiest excuse for shipping it so I needed to cram XML into the name,” he wrote.

More than anything else seen in [JavaScript programming](https://thenewstack.io/javascript/ "JavaScript programming") up till then, XMLHttpRequest pushed the web browser to evolve from document viewer to application platform.

## **4. 2005: Ajax & jQuery in Web 2.0**

After the dot-com period, browser innovation atrophied — which also meant there wasn’t a lot of innovation happening in JavaScript either (although shoutout to JSON — JavaScript Object Notation — which Douglas Crockford invented in 2001). However, [when Web 2.0 began around 2004](https://cybercultural.com/p/003-the-first-web-20-conference-2004/), things picked up again.

Notably, XMLHttpRequest got a rebrand. UX architect Jesse James Garrett coined the term Ajax on [February 18, 2005](https://designftw.mit.edu/lectures/apis/ajax_adaptive_path.pdf) (it stood for “asynchronous JavaScript and XML”). One month later, Google Maps showcased its potential. Ajax became perhaps the trendiest Web 2.0 feature — although [shiny, rounded corners](https://jonathannicol.com/blog/2006/10/21/the-visual-design-of-web-20/) gave it a run for its money.

[In August 2005](https://www.slideshare.net/slideshow/history-of-jquery/151586#4), developer John Resig began what would become the most popular — [and durable](https://thenewstack.io/why-outdated-jquery-is-still-the-dominant-javascript-library/) — JavaScript library of them all: [jQuery](https://en.wikipedia.org/wiki/JQuery). When he released it in January 2006, he promoted it as “new wave JavaScript.” Basically, it smoothed away DOM quirks, giving developers a single, chainable API.

## **5. 2009: Node.js Escapes the Browser**

At JSConf EU on 27 May 2009, Ryan Dahl [unveiled Node.js](https://www.youtube.com/watch?v=ztspvPYybIY), marrying Chrome’s V8 engine to an event-loop server model. Suddenly JavaScript could handle the backend as well as the UI.

As a result of Node.js, the catchphrase “JavaScript everywhere” became common. The analysis firm Redmonk used the term in [a July 2010 blog post](https://redmonk.com/cote/2010/07/29/makeall007/), adding that JavaScript was now “the lingua franca of the cloud.” Certainly startups loved the single-language stack concept; and enterprises soon adopted it too.

The phrase caught on — “Run JavaScript Everywhere” is currently emblazoned across [the project’s homepage](https://nodejs.org/en).

## **6. 2014: npm Expansion**

As the JavaScript ecosystem broadened to include the backend as well as the frontend, so the number of libraries and JS packages expanded too.

Npm was created in 2010 as a registry for JavaScript projects. By the time npm, Inc. was formed in 2014, commercializing the registry, the number of modules had ballooned from 6,000 in early 2012 [to 50,000 packages](https://blog.npmjs.org/post/156076312840/search-update.html). This was helped by npm’s easy install command, which encouraged a culture of ultra-small modules.

The rise of npm meant that developers moved from copy-pasting scripts to composing applications out of many tiny JS packages. That made code reuse easier, although it also added security and reliability risks in the dependency chain.

## **7. 2015: ES6 Modernises the Language**

The long-awaited [ECMAScript 2015 (ES6)](https://ecma-international.org/wp-content/uploads/ECMA-262_6th_edition_june_2015.pdf) aligned JavaScript with modern programming tastes. Indeed, [the official specification](https://262.ecma-international.org/6.0/index.html#sec-scope) acknowledged that JavaScript was now a “fully featured general propose programming language.” Here’s how the spec put it:

“ECMAScript usage has moved beyond simple scripting and it is now used for the full spectrum of programming tasks in many different environments and scales. As the usage of ECMAScript has expanded, so has the features and facilities it provides.”

ECMAScript 2015 was not just the largest-ever update to the language, but also added “a reliable process for annual updates that have brought a succession of improvements, large and small,” as The New Stack’s Mary Branscombe [put it last year](https://thenewstack.io/inside-ecmascript-javascript-standard-gets-an-extra-stage/).

## **8. 2016: React and the Component Revolution**

In Stack Overflow’s [2016 developer survey](https://survey.stackoverflow.co/2016), React was listed as the top “trending tech” of that year (the previous year, React hadn’t even been mentioned in the report).

There’s no doubt that [React was a revolutionary change](https://thenewstack.io/after-a-decade-of-react-is-frontend-a-post-react-world-now/) to JavaScript development. When it was initially released in 2013 by Facebook, it gave developers two “virtual” copies of the DOM (a before and after for each interaction), from which you then run a “diffing” process to establish what exactly has changed. React then applies those changes to the actual DOM — meaning only a portion of the DOM is changed, with the rest of it staying as-is. That, in turn, means that only a portion of the webpage needs to be re-rendered for the end user. Facebook developer Christopher Chedeau compared React to “version control for the DOM.”

One of the other important concepts behind React was that it wasn’t template-based, like previous popular frameworks (such as Ruby on Rails and Django). As Facebook’s Pete Hunt said in 2013, “React approaches building user interfaces differently by breaking them into components [which] means React uses a real, full-featured programming language to render views.”

React was in full flow by 2016, but it was also starting to attract critics — whose main complaints were that React apps or pages were bloated with JavaScript code, too slow, and too complicated (especially in regards to state management).

## **9. 2019: TypeScript Breakthrough**

RedMonk’s [June 2019 language rankings](https://redmonk.com/sogrady/2019/07/18/language-rankings-6-19/) placed TypeScript tenth — the first new entrant to the top 10 in five years and the first time TypeScript had broken into the top ten.

What [TypeScript](https://thenewstack.io/what-is-typescript/) — a superset of JavaScript — brought to the table was static typing, IDE autocompletion, refactor-friendly tooling, and more. These features helped convince large enterprise teams that JavaScript could scale to millions of lines.

Part of the reason for TypeScript’s growing popularity from 2019 was its support by the main JavaScript frameworks. TypeScript integrates seamlessly with React, it is the primary language of Angular, and it is integrated with [Vue.js](http://vue.js). Plus, it is supported by server-side JS platforms like Deno (which has always had TypeScript support) and [Node.js](http://node.js) (which added it in [March this year](https://thenewstack.io/denos-response-to-nodes-recent-support-for-typescript/)).

In Redmonk’s most recent rankings, [for January 2025](https://redmonk.com/sogrady/2025/06/18/language-rankings-1-25/), TypeScript is number 6. So it continues to gain influence in the JS ecosystem.

## **10. 2022: WebAssembly and the Edge**

WebAssembly became a W3C Recommendation [in December 2019](https://www.w3.org/2019/12/pressrelease-wasm-rec.html.en), but the developer inflection point came when Cloudflare open-sourced its [workerd](https://blog.cloudflare.com/workerd-open-source-workers-runtime/) JavaScript/Wasm runtime in September 2022. JavaScript now commonly runs in datacenters worldwide, side-by-side with Wasm modules.

Practically speaking, this means that JavaScript is now being used on the network edge and is often teamed with WebAssembly for compute-heavy tasks — a glimpse, perhaps, of a polyglot future for programming (using multiple programming languages within a single project).

You might ask, wasn’t the original point of WebAssembly to compile other languages so that developers can use them in the browser via JavaScript? Yes indeed, but that is changing. As Fastly’s Guy Bedford told Mary Branscombe [in April 2023](https://thenewstack.io/webassembly/will-javascript-become-the-most-popular-webassembly-language/), “WebAssembly has all these benefits which apply in all the different environments where it can be deployed, because of its security properties and its performance properties and its portability.” In other words, Wasm by itself has many benefits — particularly at the edge — and so bringing JavaScript into its ecosystem is worthwhile for certain projects.

## **What’s Next?**

Will JavaScript even last another 30 years, in an era when [AI might make programming itself obsolete](https://thenewstack.io/coding-sucks-anyway-matt-welsh-on-the-end-of-programming/)? Nobody can answer that right now, but we do know that the web development community is starting to kick back against the [complexity of the modern JavaScript ecosystem](https://thenewstack.io/developers-rail-against-javascript-merchants-of-complexity/). As my colleague Alex T. Williams wrote in a post published earlier today, React in particular is [being challenged](https://thenewstack.io/why-react-is-no-longer-the-undisputed-champion-of-javascript/). “Modern browsers are more capable, developers are more discerning, and the jig is almost up,” he noted.

So perhaps it’s time for a return to simplicity in the world of JavaScript. Regardless, let’s celebrate three decades of wide-ranging innovation for the web’s premier programming language. Thanks Brendan Eich for those 10 hectic days in 1995, and here’s to 30 more years!

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://cdn.thenewstack.io/media/2020/03/1c7152c0-ricmac_highres_w400_h400.jpg)

Richard MacManus is a Senior Editor at The New Stack and writes about web and application development trends. Previously he founded ReadWriteWeb in 2003 and built it into one of the world’s most influential technology news sites. From the early...

Read more from Richard MacManus](https://thenewstack.io/author/richard/)