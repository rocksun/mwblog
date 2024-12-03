
<!--
title: 使用XSLT重新发现早期Web开发的乐趣
cover: https://cdn.thenewstack.io/media/2024/12/25bc3a06-alex-shuper-z85dw2d6roe-unsplashb.jpg
-->

随着Web开发者开始质疑其工作的复杂性，了解开发者曾经如何使用XSL转换是有价值的。

> 译自 [Rediscover the Joy of Early Web Development With XSLT](https://thenewstack.io/rediscover-the-joy-of-early-web-development-with-xslt/)，作者 David Eastman。

最近听到一位青少年在演讲中谈到可扩展样式表语言转换（[XSLT](https://en.wikipedia.org/wiki/XSLT)）的乐趣，我感到有些惊讶。这是一种古老的Web语言，诞生于1998年，所以我最初的想法是，这位演讲者应该多出去走走。但他们的演讲让我想起了过去数据转换的灵活之处。

随着时间的推移，较大的XSLT转换变得难以处理，这项技术逐渐被更易于使用的格式所取代。[JQuery](https://thenewstack.io/why-outdated-jquery-is-still-the-dominant-javascript-library/)和[CSS](https://thenewstack.io/css-frameworks-in-vogue-but-dont-forget-style-fundamentals/)现在被认为是识别元素和样式的更简单方法。在数据方面，完整的內容管理系统(CMS)是处理数据块的一种更简便的方法。然而，随着人们开始质疑以DOM为中心的方法是否增加了[额外的复杂性](https://thenewstack.io/developers-rail-against-javascript-merchants-of-complexity/)，了解大约十年前人们如何使用转换是有价值的。

XSLT的一个优点是它仍然内置于浏览器中，因此使用起来实际上是免费的。一开始我会为了方便使用在线工具，但最终你会发现不需要任何支持库。但是，当我们尝试这样做时，我们会遇到一些问题。

不幸的是，要完全理解它需要了解很多缩写（例如XHML、XPATH等），但我将省略大部分内容。如果你想深入了解这个主题，可以查找它们，但现在让我们只关注Web基础知识。

转换的作用是帮助将数据内容压缩到已知的模板中。因此，让我们从一个普通的网站开始。假设我有一个简单的网页，我打算用关于城市的信息来填充它，以形成我的世界城市页面：

![](https://cdn.thenewstack.io/media/2024/11/76dd5d8a-image-1024x510.png)

这个查看器来自[w3schools](https://www.w3schools.com/tryit/tryit.asp?filename=tryhtml_hello#login)网站，*cities.html*文件改编自那里的示例。缺少的顶部部分只是CSS，我稍后会展示。但我们有一个简单的页面。

无论我打算只有一个城市还是多个城市，很明显，我正在做的是将一些简单的信息填充到HTML模板中。这当然是内容管理系统的起点，但我可以用更简单的方法来实现这种表示。

现在，让我们从数据开始。虽然[XML已经过时](https://thenewstack.io/vintage-computer-festival-2017-giant-floppy-disks-json-vanquished-xml/)，但它仍然是一种可读的结构化数据形式。可以把它想象成带有过多尖括号的JSON。我们可以用cities.xml表示城市列表中的实际数据（目前只有伦敦）：

```xml
<?xml version="1.0" encoding="UTF-8"?>
<cities>
  <city>
    <title>London</title>
    <country>London is the capital city of the United Kingdom.</country>
    <details>It is the most populous city in the United Kingdom, with a metropolitan area of over 13 million inhabitants.</details>
    <history>Standing on the River Thames, London has been a major settlement for two millennia, its history going back to its founding by the Romans, who named it Londinium.</history>
  </city>
</cities>
```

这只是用一些语义标签分割的数据，以突出各个组成部分。此外，至关重要的是，它没有附加任何样式信息。这种关注点分离意味着我们可以单独管理数据和显示数据的信息。

所以现在我们面临一个不同的问题。如果我们接受关注点分离，我们需要一种方法来提取数据并将其放回cities.html模板中。这就是XSLT发挥作用的地方。

或者更确切地说，这就是XSLT接管的地方。我们的cities.html模板最终将位于cities.xslt文件中。所以这是我们第一次尝试简单的转换。我们将使用[xsltest](https://xslttest.appspot.com/)上的简单转换器来展示一些转换代码在我们的*cities.xml*文件上的工作情况：

![](https://cdn.thenewstack.io/media/2024/11/65b41329-image-1-1024x448.png)

因此，正如你所看到的，结果输出是由放置在XSL中的HTML创建的（XSL是执行转换的语言的术语）。

让我们详细看看XSL代码：

```xml
<?xml version="1.0" encoding="UTF-8"?>
<xsl:stylesheet version="1.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform">
  <xsl:template match="cities/city">
    <html>
      <body>
        <h1>
          <xsl:value-of select="title"/>
        </h1>
        <p>
          <xsl:value-of select="country"/>
        </p>
      </body>
    </html>
  </xsl:template>
</xsl:stylesheet>
```

我们仍然遵守HTML的规则，但有一些新的标签。

我们可以看到，在冗长的头部之后，`<xsl:template>`实际上包含了我们创建最终HTML输出所需的一切。

我们的首要任务是导航到XML数据以提取所需内容。我们使用`<xsl:template match="cities/city">`来实现，它匹配我们XML文件中的结构，其中`<cities>`内包含`<city>`条目。

然后，我们从XML中选择“title”和“country”条目，并将它们放入相应的`<p>`中以进行输出。

所以，让我们完成整个过程，并将我们的整个模板放入*cities.xsl*中：

```xml
<?xml version="1.0" encoding="UTF-8"?>
<xsl:stylesheet version="1.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform">
  <xsl:template match="cities/city">
    <html lang="en">
      <head>
        <title>Basic HTML layout</title>
        <style>
          * { box-sizing: border-box;}
          body { font-family: Arial, Helvetica, sans-serif;}
          /* Style the header */
          header { background-color: #666; padding: 30px; text-align: center; font-size: 35px; color: white;}
          article { float: left; padding: 20px; width: 70%; background-color: #f1f1f1; height: 300px; /* only for demonstration, should be removed */}
          /* Clear floats after the columns */
          section::after { content: ""; display: table; clear: both;}
          /* Style the footer */
          footer { background-color: #777; padding: 10px; text-align: right; color: white;}
        </style>
      </head>
      <body>
        <header> <h2>Cities</h2></header>
        <section> 
          <article> 
            <h1><xsl:value-of select="title"/></h1> 
            <p><xsl:value-of select="country"/></p> 
            <p><xsl:value-of select="details"/></p> 
            <p><xsl:value-of select="history"/></p> 
          </article>
        </section>
        <footer> 
          <p><xsl:text disable-output-escaping="yes"><![CDATA[&copy;]]></xsl:text>World Cities</p>
        </footer>
      </body>
    </html>
  </xsl:template>
</xsl:stylesheet>
```

所以，最终我们只有三个文件。我们的XML数据、旧的HTML模板和新的XSL文件，如果一切正常，应该会创建与我们开始时相同的输出。

![](https://cdn.thenewstack.io/media/2024/11/13391291-image-3-1024x249.png)

我们应该能够将转换添加到xml中，然后在浏览器中打开它。毕竟，这就是重点。但是，这其中有一个小问题。

如果我直接在Chrome中打开cities.xml，我会看到如下内容，这或多或少是预期的：

![](https://cdn.thenewstack.io/media/2024/11/8235284f-image-4-1024x148.png)

为了让它使用我们的XSLT，我们只需添加一行代码来告诉它关于位于同一文件夹中的文件：

```xml
<?xml-stylesheet href="cities.xslt" type="text/xsl" ?>
```

瞧：

![](https://cdn.thenewstack.io/media/2024/11/9b80a5f1-image-5.png)

但这行不通。为什么？因为现代浏览器标签都是隔离的虚拟机，出于安全原因，它们无法识别文件系统中的其他文件。现在，我们可以启动一个浏览器并告诉它忽略文件隔离，但没有哪个明智的开发者会尝试这种方式。

幸运的是，如今我们有方法创建非常简单的Web服务器。如果您阅读了我的一些[之前的文章](https://thenewstack.io/a-look-at-gradios-ai-playground-for-machine-learning-devs/)，特别是关于LLM的文章，那么您应该可以使用Python。

通过使用[Python](https://thenewstack.io/what-is-python/)，我们可以在包含这些文件的文件夹中启动一个服务器……

![](https://cdn.thenewstack.io/media/2024/11/82ba3672-image-6-1024x201.png)

……通过在localhost:8000处打开浏览器，您可以导航到*cities.xml*文件并获得页面，就像它一样：

![](https://cdn.thenewstack.io/media/2024/11/2a9748dd-image-7.png)

最后，选择cities.xml：

![](https://cdn.thenewstack.io/media/2024/11/7dd4954c-image-8-1024x489.png)

还有一个问题。版权符号——我们不希望＆符号被转换两次，因此我们使用了笨拙的XSL代码：

```xml
<p><xsl:text disable-output-escaping="yes"><![CDATA[&copy;]]></xsl:text>World Cities</p>
```

当然，我们接下来应该继续循环遍历，以提取以后可能添加到XML中的任何其他城市，但我认为我应该把这个实验留给读者去探索。也许，像那个做演讲的年轻人一样，你会重新发现早期Web开发的乐趣。
