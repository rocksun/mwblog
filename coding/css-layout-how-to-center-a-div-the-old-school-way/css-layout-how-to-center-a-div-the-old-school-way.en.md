In the early days of the internet, centering something on a webpage was easy: Just put a *<center>* tag on it.

When it [revised the HTML](https://frontendinterviewquestions.medium.com/center-tag-in-html5-9b7ab0ff0a46) to version 4.0, however, the [World Wide Web Consortium](https://www.w3.org/about/) (W3C) deprecated the center tag, in its enthusiasm for [separation of concerns](https://www.w3.org/TR/html-design-principles/). Ease of use was sacrificed for [architectural purity](https://www.w3schools.com/html/html_xhtml.asp). And centering things somehow became the province of [Cascading Style Sheets](https://www.w3.org/Style/CSS/Overview.en.html).

This proved to be problematic in that there was nothing in place to replace the effective but architecturally incorrect center tag directly. The W3C provided a list of new layout elements (*header*, *nav*, *aside*), but none of those helped the coder proportion elements within the page itself.

“Having studied grid layout, you will probably be surprised how complicated this all seems!” The Mozilla dev page [actually stated](https://developer.mozilla.org/en-US/docs/Learn_web_development/Core/CSS_layout/Legacy_Layout_Methods) on the now legacy methods the web community first embraced.

To be fair, putting something in the “middle” of a webpage is a philosophical conundrum, given the canvas for HTML’s webpage is effectively infinite. It has no sides, it has no top or bottom. So the middle must be defined by whatever canvas the developers puts on the page (if they realize they are supposed to do that at all).

> Divs “work by giving items a size, and pushing them around to line them up in a way that looks like a grid,”
>
> –Mozilla Developer Network documentation.

It was a big ask for a supposedly democratic technology like the web. It sent many a web designer down a rabbit hole of confusion, which went on for over a decade until the [CSS Grid](https://thenewstack.io/get-grid-last-css-grid-template-markup/) and [CSS Flexbox](https://thenewstack.io/open-source-leaders-thomas-park-hops-easy-css-development-flexbox-froggy/) came along to simplify things.

Still, a whole generation of websites were built without Grid or Flexbox, and today are no doubt still many administrators who won’t touch the legacy and very fussy code for centering things, afraid that one excess or misplaced tag would collapse their whole site design.

So there is a way to center elements on a web page with Grid or Flexbox, that was assembled from community-generated best practices. It’s all based around the HTML *<div>* tag.

## Divvy Up Is What Div Does

The HTML *[<div>](https://www.w3schools.com/tags/tag_div.ASP)* tag defines a section, or division, within a web document.

Divs are the elements are right below *<body>* in the hierarchy of an HTML document, just as *<body>* follows *<head>* and is hierarchically under the top level *<html>* tag.

This file contains hidden or bidirectional Unicode text that may be interpreted or compiled differently than what appears below. To review, open the file in an editor that reveals hidden Unicode characters.
[Learn more about bidirectional Unicode characters](https://github.co/hiddenchars)








|  |  |
| --- | --- |
|  | /\*Inserted into the header file of an HTML document\*/ |
|  |  |
|  | <head> |
|  | <style> |
|  | div { |
|  | display: block; |
|  | } |
|  | </style> |
|  | </head> |

You can think of each *<div> </div>* set as a sort of a container, with which you can style with CSS (or manipulate with JavaScript), by adding a **class** or **id** attribute of the *<div>*. The [id](https://www.w3schools.com/html/html_id.asp) attribute refers to one specific *<div>* of a web page; whereas [class](https://www.bing.com/videos/riverview/relatedvideo?q=html+class+attribute&mid=AE045DAA6DEBA1D7C9F0AE045DAA6DEBA1D7C9F0&FORM=VAMTRV) can apply to more than one *<div>*.

So *<div>* can be given a class name, and the browser will execute that action for all members of the class.

This file contains hidden or bidirectional Unicode text that may be interpreted or compiled differently than what appears below. To review, open the file in an editor that reveals hidden Unicode characters.
[Learn more about bidirectional Unicode characters](https://github.co/hiddenchars)








|  |  |
| --- | --- |
|  | <html> |
|  |  |
|  | <head> |
|  | <style> |
|  | .red-text {background-color:red} |
|  | </style> |
|  | </head> |
|  |  |
|  | <body> |
|  | <div class="red-text">"Soul Kitchen"</div> |
|  | </body> |
|  | </html> |

**IDs** work in a similar way, except they use [identifiers by hashtags rather than a single leading dot](https://gist.github.com/joabj/9f714841776afecde24daea061d58b27).

Thus, the easiest possible way to center a bit of content on a page is by using a *<div>* tag to define a content area.

As Kevin Powell [explains](https://www.youtube.com/watch?v=ULVu2VNM_54) in this helpful video, many devs actually call this *<div>* a container. Using **class** or **id**, they then set the **width** of that container to 50% (half) of the allotted size of that webpage. As the size of the browser window changes, the container stays at a corresponding 50%.

This file contains hidden or bidirectional Unicode text that may be interpreted or compiled differently than what appears below. To review, open the file in an editor that reveals hidden Unicode characters.
[Learn more about bidirectional Unicode characters](https://github.co/hiddenchars)








|  |  |
| --- | --- |
|  | <html> |
|  |  |
|  | <head> |
|  | <style> |
|  | .container {width: 50%; /\*Sets the size of the container as |
|  | a percentage of overall page \*/ |
|  | margin: 0 auto; /\*Margin above and below the content text set to 0; |
|  | and left/right margin is claculated by the browser\*/ |
|  | } |
|  | </style> |
|  | </head> |
|  |  |
|  | <body> |
|  | <div class="container">Tell me, O Muse, of the man of many devices, who wandered full many ways after he had sacked the sacred citadel of Troy. Many were the men whose cities he saw and whose mind he learned, aye, and many the woes he suffered in his heart upon the sea, seeking to win his own life and the return of his comrades. Yet even so he saved not his comrades, though he desired it sore, for through their own blind folly they perished—fools, who devoured the kine of Helios Hyperion; but he took from them the day of their returning. Of these things, goddess, daughter of Zeus, beginning where thou wilt, tell thou even unto us. Now all the rest, as many as had escaped sheer destruction, were at home, safe from both war and sea, but Odysseus alone, filled with longing for his return and for his wife, did the queenly nymph Calypso, that bright goddess, keep back in her hollow caves, yearning that he should be her husband.</div> |
|  | </div> |
|  | </body> |
|  |  |
|  | </html> |

The CSS [**width**](https://www.w3schools.com/cssref/pr_dim_width.php) property can also be set with fixed lengths in pixels (though fixed lengths can be problematic when changing the size of the window itself).

In the code snippet above, the [**margin**](https://www.w3schools.com/css/css_margin.asp) property spaces the text from within the container sides.the first number (“0”) sets the space above and below the text, the second (set here as “auto”) is the margin on the right and left of the text. These margins can be specified more exactly with lengths or percentages, if need be.

Make sure any classes called are done so in dumb quotes (“) not smart quotes.

The above code renders centers the sample text on the page:

[![Centered text on a web page.](https://cdn.thenewstack.io/media/2025/12/33aecbc3-div-center.jpg)](https://cdn.thenewstack.io/media/2025/12/33aecbc3-div-center.jpg)

Crazy that is the *easiest possible way* acceptable to all browsers to center something on a webpage.

Most web designers require more centering than that, alas.

## Balance Multiple Columns in a Browser Window

First, though, a detour into the world of the [CSS float property](https://www.w3schools.com/css/css_float.asp). The **float** property was originally designed for positioning images inside of boxes. If the image was smaller than the box, should it align right or left or up or down?

But desperate web devs found that **float**, however can be used to position any HTML element. Namely, it can position smaller *<divs>* within the container *<div>*.

A two column web page can be composed of two divs, one that floats left and the other that floats to the right. They need to be balanced in their proportions so they aren’t larger than the container, or, like too many cats at a feeding bowl, that they don’t crowd each other out, and leave your site all lopsided. You have to figure out those numbers yourself.

This file contains hidden or bidirectional Unicode text that may be interpreted or compiled differently than what appears below. To review, open the file in an editor that reveals hidden Unicode characters.
[Learn more about bidirectional Unicode characters](https://github.co/hiddenchars)








|  |  |
| --- | --- |
|  | <html> |
|  |  |
|  | <head> |
|  | <link rel="stylesheet" href="styles.css"> |
|  | <style> |
|  | .container {width: 90%; |
|  | max-width: 700px; /\* A hard-limit maximum size for the container \*/} |
|  |  |
|  | .left { |
|  | width: 48%; /\*That's 48% of the 100% allocated to the container \*/ |
|  | float: left; |
|  | background-color: red; |
|  | } |
|  |  |
|  | .right { |
|  | width: 48%; |
|  | float: right; |
|  | background-color: orange; |
|  | } |
|  |  |
|  | .clearfix { |
|  | clear: both; |
|  | } |
|  | </style> |
|  | </head> |
|  |  |
|  | <body> |
|  | <div class="container"> |
|  |  |
|  | <div class="left"> |
|  | <h2>First Column</h2> |
|  | <p> |
|  | Chicken |
|  | </p> |
|  | </div> |
|  |  |
|  |  |
|  | <div class="right"> |
|  | <h2>Second Column</h2> |
|  | <p> |
|  | Waffles |
|  | </p> |
|  | </div> |
|  |  |
|  | <div class="clearfix"></div> |
|  |  |
|  | </div> |
|  | </body> |

In the above example, the container is set at 90% of the browser window, and two divs are set to take up 48% each of the 100% that is given to the container *<div>.* One is floated to the right, and one is floated to the left.

Here is how the above code renders on the page:

[![Two columns rendered in CSS.](https://cdn.thenewstack.io/media/2025/12/d4da6c6e-two-columns.jpg)](https://cdn.thenewstack.io/media/2025/12/d4da6c6e-two-columns.jpg)

Note that due to a faulty way the browsers order the calculations of sizing the *<div>*, a patch, called [Clear Fix](https://www.w3schools.com/howto/howto_css_clearfix.asp), should be added, also as a *<div>.* I don’t know how it works, but it is what W3C prescribes.

What about three columns, the favored for many websites (including TNS itself, with the help of [WordPress](https://thenewstack.io/wordpress-turmoil-and-the-fair-package-manager/))? The best approach is to play around with the properties of the divs, and see how they stack up in the browser window.

This file contains hidden or bidirectional Unicode text that may be interpreted or compiled differently than what appears below. To review, open the file in an editor that reveals hidden Unicode characters.
[Learn more about bidirectional Unicode characters](https://github.co/hiddenchars)








|  |  |
| --- | --- |
|  |  |
|  | <html> |
|  |  |
|  | <head> |
|  | <link rel="stylesheet" href="styles.css"> |
|  | <style> |
|  | .container { |
|  | width: 90%; |
|  | margin: 0 auto; |
|  | } |
|  |  |
|  |  |
|  | .column { /\*a class to set the attributes that will be applied to all the columns\*/ |
|  | float: left; |
|  | padding: 10px; /\* Padding will be added to the width \*/ |
|  | box-sizing: border-box; /\*Needed for setting width with padding/border \*/ |
|  | } |
|  |  |
|  | .left { |
|  | float: left; |
|  | width: 25%; |
|  | background-color: red; |
|  | } |
|  |  |
|  | .middle { |
|  | width: 50%; |
|  | background-color: white; |
|  | } |
|  |  |
|  | .right { |
|  | float: right; |
|  | width: 25%; |
|  | background-color: blue; |
|  | } |
|  |  |
|  | .clearfix { |
|  | clear: both; |
|  | } |
|  | </style> |
|  |  |
|  | </head> |
|  | <body> |
|  | <div class="container"> |
|  |  |
|  |  |
|  | <div class="left column"> |
|  | <h2>First column</h2> |
|  | <p> |
|  | Navigation column |
|  | </p> |
|  | </div> |
|  |  |
|  |  |
|  | <div class="middle column"> |
|  | <h2>Second column</h2> |
|  | <p> |
|  | The Feature Well |
|  | </p> |
|  | </div> |
|  |  |
|  | <div class="right column"> |
|  | <h2>Third column</h2> |
|  | <p> |
|  | A column for ads. |
|  | </p> |
|  | </div> |
|  |  |
|  | <div class="clearfix"></div> |
|  |  |
|  | </div> <!--Wrapping up the container div--> |
|  |  |
|  | </body> |

In the above example, both the right and left columns are given **float** directions to move them to the right and left, respectively, and the middle one is not given a **float**, so lands in the middle.

Also in the above code is a new class called column, which allows the *<dev>* to define attributes that are the same across all the columns. Note how each element can be defined by multiple classes (i.e. “left column” is actually two classes).

The code above will render thusly:

[![An example three-column layout.](https://cdn.thenewstack.io/media/2025/12/15a9037a-three-columns.jpg)](https://cdn.thenewstack.io/media/2025/12/15a9037a-three-columns.jpg)

As noted, multiple column layouts can be more easily rendered today with [Grid](https://www.w3schools.com/css/css_grid.asp) and/or [Flexbox](https://www.w3schools.com/css/css3_flexbox.asp), which we will cover in future tutorials. For now, though, you can take pride in being one of the few developers who actually know the age-old conundrum of how to center a *<div>*.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://thenewstack.io/wp-content/uploads/2017/05/327440bd-joab-jackson_avatar_1495152980.-600x600.jpeg)

Joab Jackson is a senior editor for The New Stack, covering cloud native computing and system operations. He has reported on IT infrastructure and development for over 30 years, including stints at IDG and Government Computer News. Before that, he...

Read more from Joab Jackson](https://thenewstack.io/author/joab/)