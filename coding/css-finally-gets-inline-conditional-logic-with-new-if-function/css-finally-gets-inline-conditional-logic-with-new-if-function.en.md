Inline conditional processing is coming to CSS.

Those who have felt boxed in by the web’s universal style sheets’ declarative nature are about to enjoy a bit more freedom to mix it up a bit.

For years, devs and designers [have asked](https://stackoverflow.com/questions/2446812/css-equivalent-of-the-if-statement) in [Stack Overflow](https://thenewstack.io/stack-overflow-on-snowflake-cortex-answers-without-attitude/) and elsewhere if CSS had any conditional logic, finding [only workarounds as a possibility](https://stackoverflow.com/questions/1129699/can-you-use-if-else-conditions-in-css). Now, the technical committee behind the style standard has ratified a new function for the style sheet, *if()*, which opens up a whole new world of choice for designers.

“This is the first time, that I’m aware of, that you can do this logic inline and not have a dedicated code block on the bottom of your file,” said [Mark Adkins](https://markadkins.design/), a principal user experience designer at financial firm Fidelity Investments, in a talk about some of the latest developments with [CSS](https://www.w3.org/Style/CSS/Overview.en.html) at the [AllThingsOpen 2025](https://2025.allthingsopen.org/schedule) conference in Raleigh, N.C. earlier this week.

Managed by the [World Wide Web Consortium](https://www.w3.org/about/) (W3C), CSS is the standardized way of specifying the presentation, styling and layout of web pages, working alongside [HTML for the layout](https://thenewstack.io/html-css-and-the-path-to-accessible-web-design/) of the pages and [JavaScript for their logic](https://thenewstack.io/javascript-standards-update-whats-new-in-ecmascript-2025/).

CSS is a mature technology, so it doesn’t get updated as much as it used to. Once a year, W3C issues a snapshot that aggregates all the latest developments across different parts of the specification (2025’s edition was [posted last month](https://www.w3.org/TR/css-2025/)). It is then up to the browser makers to see these specs get implemented, the progress of which has been dutifully tracked by the [Can I use](https://caniuse.com/) site.

## What Is the CSS *if()* Function?

The new function, arriving in the 2025 snapshot, is unprecedented for CSS.

“This one really caught me off guard,” admitted Adkins to the audience.

While most of CSS is about the shading and coloring and various other details of presentation, the spec has not offered much in the way of logic processing.

*If()* builds from previous work to allow developers to specify variables, or “[custom properties](https://developer.mozilla.org/en-US/docs/Web/CSS/CSS_cascading_variables/Using_CSS_custom_properties#:~:text=Custom%20properties%20(sometimes%20referred%20to,%2Dcolor:%20blue;%20).),” Adkins said. The properties, defined in the browser’s Document Object Model ([DOM](https://thenewstack.io/pivoting-from-react-to-native-dom-apis-a-real-world-example/)), can then be changed with JavaScript.

The new functionality extends logic properties into the inline code itself.

In the world of programming, the *if()* function itself is nothing new — most imperative languages have a version of the function. The *if()* function is based on the JavaScript [*if … else*](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/if...else) function, and provides a way for the programmer to set different values of a property depending on the result of a conditional test. If *a* then *x*, if *b* then *y*, and so on.

You can also supply an *else* statement if none of the conditionals are met.

In the case of CSS, the test [can be based](https://caniuse.com/css-if) on a [style query](https://developer.mozilla.org/en-US/docs/Web/CSS/CSS_media_queries/Using_media_queries), a [media query](https://developer.mozilla.org/en-US/docs/Web/CSS/CSS_media_queries/Using_media_queries) or a [feature query](https://developer.mozilla.org/en-US/docs/Web/CSS/CSS_conditional_rules/Using_feature_queries).

## How the if() Function Works in CSS

According to [the specification](https://drafts.csswg.org/css-values-5/#if-notation), the statement consists of an ordered semi-colon-separated list of statements, each specifying a condition and a value, separated by a colon.

The function’s syntax, as purloined Mozilla Development Network [docs](https://drafts.csswg.org/css-values-5/#if-notation), can be seen here:

This file contains hidden or bidirectional Unicode text that may be interpreted or compiled differently than what appears below. To review, open the file in an editor that reveals hidden Unicode characters.
[Learn more about bidirectional Unicode characters](https://github.co/hiddenchars)








|  |  |
| --- | --- |
|  | <if-condition> |
|  | An <if-test> or the else keyword. |
|  |  |
|  | <if-test> |
|  | A style query, media query, or feature query. |
|  |  |
|  | else |
|  | A keyword representing an <if-condition> that always evaluates to true. |
|  |  |
|  | <value> |
|  | A property value. |
|  |  |
|  | Return value |

MDN also provides an example of how *if()* could be used: Below, you will find that one of two background images can be deployed on a web page depending on which theme is chosen (“ice” or “fire”):

This file contains hidden or bidirectional Unicode text that may be interpreted or compiled differently than what appears below. To review, open the file in an editor that reveals hidden Unicode characters.
[Learn more about bidirectional Unicode characters](https://github.co/hiddenchars)








|  |  |
| --- | --- |
|  | div { |
|  | background-image: if( |
|  | style(--scheme: ice): linear-gradient(#caf0f8, white, #caf0f8); |
|  | style(--scheme: fire): linear-gradient(#ffc971, white, #ffc971); |
|  | else: none; |
|  | ); |
|  | } |

The function can be built into any property of a class, or as part of a selector, Adkins said.

## Current Browser Adoption and Support

Currently, the *if()* function is only partially supported across browsers.

[![test results](https://cdn.thenewstack.io/media/2025/10/deea1f01-css-if-support-browers.jpg)](https://cdn.thenewstack.io/media/2025/10/deea1f01-css-if-support-browers.jpg)

Browser support of the CSS if() function, as of October 2025. Source: [Can I use](https://caniuse.com/).

Chrome and Edge support the function, while Safari and Firefox still lag behind. Mobile development lags even further, with only Chrome for Android and the Android browsers recognizing the statement.

[![Test results](https://cdn.thenewstack.io/media/2025/10/56b6c7c0-css-if-support-mobile-browers.jpg)](https://cdn.thenewstack.io/media/2025/10/56b6c7c0-css-if-support-mobile-browers.jpg)

Mobile browser support of the CSS if() function, as of October 2025. Source: [Can I use](https://caniuse.com/).

## New Possibilities With CSS Conditionals

“The addition of *if()* provides a new architectural opportunity for CSS developers,” wrote Google Web UI DevRel Lead [Una Kravets](https://x.com/una) in [a blog post](https://developer.chrome.com/blog/if-article) describing the ways the new conditional could be used.

The function could be used to create inline media queries, Kravets suggested. As an example, a website could change designs based on the user’s preference for light or dark mode. It could also be used to do inline support queries, checking to see if the hardware supports the design, and switching to an alternative design if not. It could be a handy way to visualize the state of a running process, with different images designating whether the job is finished or not.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://thenewstack.io/wp-content/uploads/2017/05/327440bd-joab-jackson_avatar_1495152980.-600x600.jpeg)

Joab Jackson is a senior editor for The New Stack, covering cloud native computing and system operations. He has reported on IT infrastructure and development for over 30 years, including stints at IDG and Government Computer News. Before that, he...

Read more from Joab Jackson](https://thenewstack.io/author/joab/)