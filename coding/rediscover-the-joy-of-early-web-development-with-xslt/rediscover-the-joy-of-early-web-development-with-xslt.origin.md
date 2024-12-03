# Rediscover the Joy of Early Web Development With XSLT
![Featued image for: Rediscover the Joy of Early Web Development With XSLT](https://cdn.thenewstack.io/media/2024/12/25bc3a06-alex-shuper-z85dw2d6roe-unsplashb-1024x576.jpg)
I was a bit surprised to hear a recent talk by a teenager about the joys of eXtensible Stylesheet Language Transformations ([XSLT](https://en.wikipedia.org/wiki/XSLT)). It’s an old web language, having debuted in 1998, so my initial thought was that the presenter should get out more often. But their talk reminded me of how flexible transformations were back in the day.

Over time, as larger XSLT transformations became unworkable, the technology was quietly dropped for less migraine-inducing formats. [JQuery](https://thenewstack.io/why-outdated-jquery-is-still-the-dominant-javascript-library/) and [CSS](https://thenewstack.io/css-frameworks-in-vogue-but-dont-forget-style-fundamentals/) are now considered simpler ways of identifying elements and styling. On the data side, full-blown content management systems (CMS) are an easier way of dealing with chunks of data. However, as people start to question whether DOM-focused methods have added [an extra layer of complexity](https://thenewstack.io/developers-rail-against-javascript-merchants-of-complexity/), it is worth understanding what people did with transformations about a decade ago.

One advantage of XSLT is that it is still baked into browsers, so it is effectively free to use. I’ll start off using online tools for convenience, but in the end, you’ll see that no support libraries are needed. However, we will come across a few issues when we try to do this.

Unfortunately, a full understanding would involve lots of abbreviations that you would eventually need to know (e.g. XHML, XPATH, etc.), but I’ll leave most of these out. If you want to lean into the subject, you can look them up, but for now, let’s just stick with the web basics.

What a transformation does is help squeeze data content into a known template. So, let’s start off with a normal website. Let’s say that I have a simple web page that I intend to fill with information about cities to form my world cities page:

This viewer is from the [w3schools](https://www.w3schools.com/tryit/tryit.asp?filename=tryhtml_hello#login) site, and the *cities.html* file is adapted from examples there. The missing top part is just CSS, which I’ll show later. But we have a simple page.

Whether I intend to just have one city or many, it is fairly obvious that what I’m doing is stuffing some simple facts into an HTML template. This is, of course, the jumping-off point for content management systems, but there are simpler ways I can go about this representation.

Now, let’s start with the data. While [XML has fallen out of fashion](https://thenewstack.io/vintage-computer-festival-2017-giant-floppy-disks-json-vanquished-xml/), it is still a readable form of structured data. Think of it as JSON with an excess of angled brackets. We can represent the actual data in our city listing (with only London in it so far) with cities.xml:

123456789101112 |
<?xml version="1.0" encoding="UTF-8"?> <cities> <city> <title>London</title> <country> London is the capital city of the United Kingdom. </country> <details> It is the most populous city in the United Kingdom, with a metropolitan area of over 13 million inhabitants. </details> <history> Standing on the River Thames, London has been a major settlement for two millennia, its history going back to its founding by the Romans, who named it Londinium. </history> </city> </cities> |
This is just the data cut up with some semantic tags to highlight the constituent pieces. Furthermore, and crucially, there is no styling information attached to it. This separation of concerns means that we can manage the data separately from the information displaying it.
So now we have a different issue. If we accept the separation of concerns, we need a way to suck the data out and place it back into the cities.html template. This is where XSLT fits in.

Or rather, this is where XSLT takes over. Our cities.html template will end up living inside a cities.xslt file. So here is our first attempt at a simple transformation. We’ll use the simple converter at [xsltest](https://xslttest.appspot.com/) to show some transformation code working on our *cities.xml* file:

So, as you can see, the resulting output is created by the HTML that is placed inside the XSL (XSL is the term for the language that does the Transformation).

Let’s look at the XSL code in detail:

123456789101112 |
<?xml version="1.0" encoding="UTF-8"?> <xsl:stylesheet version="1.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform"> <xsl:template match="cities/city"> <html> <body> <h1> <xsl:value-of select="title"/> </h1> <p> <xsl:value-of select="country"/> </p> </body> </html> </xsl:template> </xsl:stylesheet> |
We are still obeying the laws of HTML, but with some new tags.
What we can see is that after the lengthy headers, the `<xsl:template>`
actually contains all we need to create the resulting HTML output.

We know our first job is to navigate into the XML data in order to extract what we need. We do that with the `<xsl:template match="cities/city">`
, which matches the structure of our XML file where we have a `<city>`
entry within the `<cities>`
.

We then select the “title” and “country” entries from the XML and plop them into the corresponding `<p>`
‘s for output.

So, let’s complete the process and put our whole template into *cities.xsl*:

12345678910111213141516171819202122232425262728293031323334353637383940414243444546474849505152535455565758596061626364656667686970717273 |
<?xml version="1.0" encoding="UTF-8"?><xsl:stylesheet version="1.0"xmlns:xsl="http://www.w3.org/1999/XSL/Transform"><xsl:template match="cities/city"><html lang="en"><head><title>Basic HTML layout</title><style>* { box-sizing: border-box;}body { font-family: Arial, Helvetica, sans-serif;}/* Style the header */header { background-color: #666; padding: 30px; text-align: center; font-size: 35px; color: white;}article { float: left; padding: 20px; width: 70%; background-color: #f1f1f1; height: 300px; /* only for demonstration, should be removed */}/* Clear floats after the columns */section::after { content: ""; display: table; clear: both;}/* Style the footer */footer { background-color: #777; padding: 10px; text-align: right; color: white;}</style></head><body><header> <h2>Cities</h2></header><section> <article> <h1><xsl:value-of select="title"/></h1> <p><xsl:value-of select="country"/></p> <p><xsl:value-of select="details"/></p> <p><xsl:value-of select="history"/></p> </article></section><footer> <p><xsl:text disable-output-escaping="yes"><![CDATA[&]]></xsl:text>copy;World Cities</p></footer></body></html></xsl:template></xsl:stylesheet> |
So, in the end, we only have three files. Our XML data, our old HTML template, and the new XSL file should create the same output as we started with if things work well.
We should be able to just add the transformation to the xml, and open it in the browser. That is the point, after all. However, there is a small problem with that.

If I just open the cities.xml directly in Chrome, I see the following, which is more or less expected:

To tell it to use our XSLT, we just add on a line to tell it about the file that is sitting in the same folder:

1 |
<?xml-stylesheet href="cities.xslt" type="text/xsl" ?> |
And voila:
But that won’t work. Why not? Because modern browser tabs are all isolated virtual machines and don’t recognize the other files in your file system for very good security reasons. Now, we could start a browser and tell it to ignore file isolation, but no sensible developer should try to work this way.

Fortunately, we have ways to create very simple web servers these days. If you worked through some of my [previous posts](https://thenewstack.io/a-look-at-gradios-ai-playground-for-machine-learning-devs/), especially on LLMs, you should have Python available.

By using [Python](https://thenewstack.io/what-is-python/), we can start a server in the folder with the files…

…and by opening the browser at localhost:8000, you can navigate to the *cities.xml* file and get the page as it was:

And finally, select cities.xml:

There is one more wrinkle. The copyright symbol — we don’t want the ampersand to be translated twice hence we have the awkward XSL code:

1 |
<p><xsl:text disable-output-escaping="yes"><![CDATA[&]]></xsl:text>copy;World Cities</p> |
Of course, we should then go on to move through a loop to pull out any other cities we may add to the XML later, but I think I should leave that experiment for readers to pursue. Perhaps, like the youngster who gave the talk, you may rediscover the joys of early web development.
[
YOUTUBE.COM/THENEWSTACK
Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.
](https://youtube.com/thenewstack?sub_confirmation=1)