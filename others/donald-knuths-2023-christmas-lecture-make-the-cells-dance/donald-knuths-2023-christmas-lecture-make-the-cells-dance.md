<!--
title: 唐纳德·克努斯2023圣诞讲座：让细胞起舞
cover: https://cdn.thenewstack.io/media/2023/12/3de4fdaf-donald-knuth-screenshot-from-stanford-online-2023-christmas-lecture-on-dancing-cells-1024x505.png
-->

一本1974年的计算机科学书籍中的一道“难忘的作业”问题，如何启发了一种更为高效的集合排序方法。

> Donald Knuth，计算机科学领域的巨匠，以多方面的成就引人关注。他创造了TeX排版系统，成为科技文档排版的标杆。著有《计算机程序设计艺术》的他被誉为计算机科学的权威，该书至今仍为学科经典。本文译自 [Donald Knuth’s 2023 Christmas Lecture: Making the Cells Dance](https://thenewstack.io/donald-knuths-2023-christmas-lecture-make-the-cells-dance/)，作者 David Cassel。

就像是为假期拜访一位老朋友一样…

快到86岁生日的唐纳德·克努斯（Donald Knuth）——斯坦福大学备受喜爱的计算机科学大师——秉持长期的传统，举办了一场[12月的“圣诞讲座”](https://online.stanford.edu/donald-e-knuth-lectures)，同时也在网上为他所有的粉丝[直播](https://youtu.be/622iPkJfYrI)。

“像我这样的老人，在我们的傲慢中，过去曾经认为到1970年或1980年时，所有重要的数据结构都已经被深入理解，” 克努斯对观众开玩笑说道，“所以，不需要学到更多的东西。

“但今天我要谈论的是我在三年前学到的东西…”

## 唐纳德·克努斯的好奇心

所有这一切证明，总有更多有趣的数学惊喜等待探索。60多年前，1962年，时年24岁的唐纳德·克努斯首次开始编写《计算机程序设计艺术》—这是一部关于算法的全面分析，在2023年，他仍在努力完成。

[30年前](https://youtu.be/0TOK73ij7C0?list=PLoROMvodv4rOAvKVR_dyCigSBMcYjevYB)，克努斯还开始每年12月罕见地在斯坦福大学面前亮相，面向学生们。五年前，《纽约时报》称克努斯为“[算法领域的精神导师](https://www.nytimes.com/2018/12/17/science/donald-knuth-computers-algorithms-programming.html)”，看到他现场分享他独特的深思熟虑的分析方式确实有一种特殊的感觉。

随着岁月的流逝，克努斯继续保持他那带着微笑的、温和的好奇心。

最近，斯坦福大学[上传了几十年来](https://www.youtube.com/playlist?list=PLoROMvodv4rOAvKVR_dyCigSBMcYjevYB)克努斯过去的圣诞讲座，还包括了[1985年的22个视频系列](https://www.youtube.com/playlist?list=PLoROMvodv4rNbeodV7vqxxxWpe4s_SFty)，名为“‘Aha’ 专题”（数学问题解决课程）。此外，还有[两组不同的](https://www.youtube.com/playlist?list=PLoROMvodv4rN1PKcXvzjor-Bl6o6eSNTN)1981年的五个视频，展示了克努斯介绍他新创建的排版系统 TeX。甚至还有1982年的[12个视频](https://www.youtube.com/playlist?list=PLoROMvodv4rM2JuHk3qBhQDxY9QGrLrYE)，展示了克努斯所称的“有关内部细节的深入课程”。

而在12月6日，身着传统的棕色假日毛衣，克努斯再次进行了现场演示，展现了他以清晰精准而著称的风采…

## 超越“跳舞链接”

那么，今年的主题是什么呢？

初学者学到的关于链表的知识——列表中的每个元素不仅包含一个值，还包括下一个和前一个元素的位置。克努斯帮助[推广了一种通过这些元素移动的方式](https://en.wikipedia.org/wiki/Dancing_Links)，其中“在计算机中，这些数字似乎在进行一场优雅编排的舞蹈，这就是为什么我称之为跳舞链接的原因。” 克努斯[在2018年](https://thenewstack.io/donald-knuths-christmas-tree-lecture-on-dancing-links-and-organ-music/)讨论过它们，而今年的讲座被描述为一种续集。

“我们现在已经将跳舞链接升级到了一个具有时髦名称的东西，称为跳舞细胞。”

然后，就像圣诞过去的幽灵一样，克努斯回顾了将近半个世纪的历史。“整个故事始于计算机科学领域的一本最早的伟大著作之一，”他告诉观众，展示了他自己翻烂了的《[计算机算法的设计与分析](https://www.amazon.com/Design-Analysis-Computer-Algorithms/dp/0201000296/ref=asc_df_0201000296/)》一书，作者是阿尔弗雷德·阿霍、杰弗里·乌尔曼和约翰·霍普克劳夫特。

那本1974年的书包含了一个挑战读者的练习，要求找到一种在首次访问矩阵时始终将其值初始化为零的方法。而解决方案既巧妙又出乎意料地实用。它涉及维护一个更小的列表，仅包含已知值。

将近20年后，1993年的[一篇论文](https://dl.acm.org/doi/pdf/10.1145/176454.176484)重新审视了这个想法。在实际应用中，它被证明对于处理编译器实现中内存中的值非常有帮助。该论文甚至引用了那本1974年的教材，指出他们的解决方案是“受一个难忘的家庭作业问题启发而来的……”

“换句话说，” 克努斯嘲笑地对观众说，“家庭作业问题实际上确实会以某种方式引起注意。”

1993年的研究人员还添加了一个聪明的删除值的操作，克努斯在他[计算机程序设计艺术卷4B](https://shop.harvard.com/book/9780201038064)的最新更新中也包含了对它的讨论（该更新于2022年发布）。“这是一个美妙的圣诞礼物，” 克努斯对观众开玩笑说，引起了一些欣赏的笑声。

但这也是克努斯展示一些非常高效的数据处理方法的机会…

![](https://cdn.thenewstack.io/media/2023/12/4db079c7-donald-knuth-demonstrates-dancing-cells-in-2023-christmas-lecture-screenshot-from-stanford-online-video.png)

原来在数字列表中删除一个数值有一种非常简单的方法：只需将其与列表中最后一个位置的任何数字交换，然后将列表的长度缩短一位。列表长度之外的所有位置的数字现在都已知已被删除，它们形成了一个方便的簇，包含所有已删除的数值。由于自然形成的模式，它们甚至是有序的——最近删除的数字首先出现。

这还有另一个附加的好处。克努斯随后创建了第二个列表，保存了第一个列表中每个数字的位置。然后，你可以通过该位置数字是否高于列表的长度来判断一个数字是否已被删除或未被删除！

“因此，随着算法的进行，这里的这些数字就像在跳舞一样。” 这就像“跳舞链接”算法一样，通过双向链接列表中的路径，但现在它正在跟踪“删除”或“未删除”的状态。因此，对于这一现象，计算机科学教授克里斯汀·索尔农([Christine Solnon](https://scholar.google.com/citations?user=sjJg9JAAAAAJ&hl=en))提出了一个更好的名称：“跳舞细胞（dancing cells）”。

然后，克努斯跳到了时间的另一端，到了2013年一篇承认这一想法重要性的论文…

## 终极大结局

克努斯开始解释[约束满足问题](https://en.wikipedia.org/wiki/Constraint_satisfaction_problem)的概念——即各种变量的值是否可以满足所有要求，或者所有布尔变量是否可以为真。克努斯告诉观众，一旦创建，其中一些模型可以应用于无限集合的数值。“但那对我来说太高深了。我是个有限的人。”

有一个涉及用颜色覆盖地图的问题的第三个子集，克努斯开玩笑说这是一个如此偏门的主题，以至于“截至今天，它仍然没有维基百科页面……这真是个耻辱，”他补充说——因为它是《计算机程序设计艺术》第四卷的一半的主题。“我在等人们意识到这有多么伟大。”

演讲最后展示了如何使用“跳舞细胞”算法来解决这类问题——在许多情况下，这比旧的“跳舞链接”算法更高效、更快，有时提升了20倍。

克努斯表示他可能会在未来发表一场演讲，以推广这个想法——只是为了帮助世界跟上。但除此之外，“我没有时间等待。

我得写更多的书。”

## 之前的唐纳德·克努斯圣诞讲座

- [唐纳德·克努斯2022年的“圣诞树”讲座关于树](https://thenewstack.io/donald-knuths-2022-christmas-tree-lecture-is-about-trees/)
- [唐纳德·克努斯2019年的“圣诞树讲座”探讨《计算机程序设计艺术》中的圆周率](https://thenewstack.io/donald-knuths-2019-christmas-tree-lecture-explores-pi-in-the-art-of-computer-programming/)
- [唐纳德·克努斯2018年的圣诞树讲座：关于“跳舞链接”和管风琴音乐](https://thenewstack.io/donald-knuths-christmas-tree-lecture-on-dancing-links-and-organ-music/)
- [唐纳德·克努斯2017年的圣诞树讲座解决组合几何中的“奇怪问题”](https://thenewstack.io/donald-knuths-christmas-tree-lecture-addresses-curious-problem-combinatorial-geometry/)

