<!--
title: CSS 终迎 if() 函数，内联条件逻辑大爆发
cover: https://cdn.thenewstack.io/media/2025/10/2b8ac123-ato25-mark_adkins.jpg
summary: CSS引入if()函数，实现行内条件逻辑，提升样式灵活性。它基于条件查询，Chrome和Edge已支持，Safari和Firefox正在跟进，带来新的架构可能。
-->

CSS引入if()函数，实现行内条件逻辑，提升样式灵活性。它基于条件查询，Chrome和Edge已支持，Safari和Firefox正在跟进，带来新的架构可能。

> 译自：[CSS Finally Gets Inline Conditional Logic With New if() Function](https://thenewstack.io/css-finally-gets-inline-conditional-logic-with-new-if-function/)
> 
> 作者：Joab Jackson

CSS即将迎来行内条件处理。

那些曾因网页通用样式表的声明性质而感到束缚的人，即将享受到更多的自由，来混合使用样式。

多年来，开发者和设计师们在[Stack Overflow](https://thenewstack.io/stack-overflow-on-snowflake-cortex-answers-without-attitude/)以及其他地方[询问](https://stackoverflow.com/questions/2446812/css-equivalent-of-the-if-statement)CSS是否有任何条件逻辑，但[只找到了变通方法](https://stackoverflow.com/questions/1129699/can-you-use-if-else-conditions-in-css/)。现在，样式标准背后的技术委员会已经批准了一项针对样式表的新函数，即 *if()*，这为设计师们开启了一个全新的选择世界。

富达投资公司（Fidelity Investments）的首席用户体验设计师 Mark Adkins 本周早些时候在北卡罗来纳州罗利举行的 [AllThingsOpen 2025](https://2025.allthingsopen.org/schedule) 大会上，在谈及 [CSS](https://www.w3.org/Style/CSS/Overview.en.html) 的最新发展时表示：“据我所知，这是您第一次能够在线执行这种逻辑，而无需在文件底部设置专用代码块。”

由[万维网联盟](https://www.w3.org/about/)（W3C）管理的CSS是指定网页呈现、样式和布局的标准化方式，它与用于页面[布局的HTML](https://thenewstack.io/html-css-and-the-path-to-accessible-web-design/)以及用于其[逻辑的JavaScript](https://thenewstack.io/javascript-standards-update-whats-new-in-ecmascript-2025/)协同工作。

CSS是一项成熟的技术，因此它不像以前那样频繁更新。W3C每年发布一个快照，汇总规范不同部分的所有最新发展（2025年版[已于上个月发布](https://www.w3.org/TR/css-2025/)）。然后由浏览器制造商负责实现这些规范，其进展情况由[Can I use](https://caniuse.com/)网站忠实地跟踪。

## 什么是CSS的 *if()* 函数？

这项新函数将随2025年快照一同发布，对CSS来说是前所未有的。

Adkins向听众承认：“这个功能确实让我措手不及。”

虽然大多数CSS都与阴影、颜色以及演示文稿的其他各种细节有关，但规范在逻辑处理方面并未提供太多内容。

Adkins表示，*if()* 函数是在先前的基础上开发的，允许开发者指定变量，即“[自定义属性](https://developer.mozilla.org/en-US/docs/Web/CSS/CSS_cascading_variables/Using_CSS_custom_properties#:~:text=Custom%20properties%20(sometimes%20referred%20to,%2Dcolor:%20blue;%20).)”这些属性在浏览器的文档对象模型（[DOM](https://thenewstack.io/pivoting-from-react-to-native-dom-apis-a-real-world-example/)）中定义，然后可以通过JavaScript进行更改。

新功能将逻辑属性扩展到行内代码本身。

在编程世界中，*if()* 函数本身并不新鲜——大多数命令式语言都有该函数的一个版本。*if()* 函数基于JavaScript的[*if … else*](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/if...else)函数，它为程序员提供了一种根据条件测试结果设置属性不同值的方法。如果为*a*则为*x*，如果为*b*则为*y*，依此类推。

如果所有条件都不满足，您还可以提供一个 *else* 语句。

在CSS中，测试[可以基于](https://caniuse.com/css-if)[样式查询](https://developer.mozilla.org/en-US/docs/Web/CSS/CSS_media_queries/Using_media_queries)、[媒体查询](https://developer.mozilla.org/en-US/docs/Web/CSS/CSS_media_queries/Using_media_queries)或[功能查询](https://developer.mozilla.org/en-US/docs/Web/CSS/CSS_conditional_rules/Using_feature_queries)。

## if()函数在CSS中如何工作

根据[规范](https://drafts.csswg.org/css-values-5/#if-notation)，该语句由一个有序的、以分号分隔的语句列表组成，每个语句指定一个条件和一个值，两者之间用冒号分隔。

该函数的语法，摘自Mozilla开发网络[文档](https://drafts.csswg.org/css-values-5/#if-notation)，如下所示：

This file contains hidden or bidirectional Unicode text that may be interpreted or compiled differently than what appears below. To review, open the file in an editor that reveals hidden Unicode characters.
[Learn more about bidirectional Unicode characters](https://github.co/hiddenchars)

```css
<if-condition>
An <if-test> or the else keyword.

<if-test>
A style query, media query, or feature query.

else
A keyword representing an <if-condition> that always evaluates to true.

<value>
A property value.

Return value
```

MDN还提供了一个关于如何使用 *if()* 的示例：在下方您可以看到，根据所选主题（“ice”或“fire”），网页上可以部署两种背景图片中的一种：

```css
div {
  background-image: if(
    style(--scheme: ice): linear-gradient(#caf0f8, white, #caf0f8);
    style(--scheme: fire): linear-gradient(#ffc971, white, #ffc971);
    else: none;
  );
}
```

Adkins表示，该函数可以内置到类的任何属性中，或者作为选择器的一部分。

## 当前浏览器采用和支持情况

目前，*if()* 函数在各浏览器中仅得到部分支持。

[![test results](https://cdn.thenewstack.io/media/2025/10/deea1f01-css-if-support-browers.jpg)](https://cdn.thenewstack.io/media/2025/10/deea1f01-css-if-support-browers.jpg)

CSS if()函数在浏览器中的支持情况，截至2025年10月。来源：[Can I use](https://caniuse.com/)。

Chrome和Edge支持该功能，而Safari和Firefox仍处于落后。移动端开发更是滞后，只有Android版Chrome和Android浏览器能识别该语句。

[![Test results](https://cdn.thenewstack.io/media/2025/10/56b6c7c0-css-if-support-mobile-browers.jpg)](https://cdn.thenewstack.io/media/2025/10/56b6c7c0-css-if-support-mobile-browers.jpg)

CSS if()函数在移动浏览器中的支持情况，截至2025年10月。来源：[Can I use](https://caniuse.com/)。

## CSS条件语句带来的新可能性

Google Web UI DevRel负责人 Una Kravets 在[一篇博文](https://developer.chrome.com/blog/if-article)中描述了新条件语句的多种用法，她写道：“*if()* 的加入为CSS开发者提供了新的架构机会。”

Kravets 建议，该函数可用于创建行内媒体查询。例如，网站可以根据用户对浅色或深色模式的偏好来更改设计。它还可以用于执行行内支持查询，检查硬件是否支持该设计，如果不支持则切换到替代设计。这也可以是一个方便的方式来可视化正在运行的进程状态，用不同的图像指示任务是否完成。