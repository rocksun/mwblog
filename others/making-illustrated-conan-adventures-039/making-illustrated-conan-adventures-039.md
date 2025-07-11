
<!--
title: 图文再现《蛮王柯南》：黑色巨像
cover: https://substackcdn.com/image/fetch/$s_!pSdf!,w_1200,h_600,c_fill,f_jpg,q_auto:good,fl_progressive:steep,g_auto/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F73f53deb-8629-47fb-b489-4f9863b06d55_1802x1185.png
summary: 作者分享了如何使用AI工具制作图文并茂的《黑色巨像》版本，包括图像生成、优化、修复和评分等技术细节，以及对不同AI模型和工作流程的比较与反思。他还探讨了AI在公共领域作品插图方面的潜在应用。
-->

作者分享了如何使用AI工具制作图文并茂的《黑色巨像》版本，包括图像生成、优化、修复和评分等技术细节，以及对不同AI模型和工作流程的比较与反思。他还探讨了AI在公共领域作品插图方面的潜在应用。

> 译自：[Making Illustrated CONAN Adventures: Black Colossus](https://brianheming.substack.com/p/making-illustrated-conan-adventures-039)
> 
> 作者：Brian Heming

我制作了一个图文并茂的版本，改编自罗伯特·E·霍华德于1933年6月首次发表的第四部柯南故事*黑色巨像（Black Colossus）*。先说几个要点：

[![](https://substackcdn.com/image/fetch/$s_!pSdf!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F73f53deb-8629-47fb-b489-4f9863b06d55_1802x1185.png)](https://substackcdn.com/image/fetch/$s_!pSdf!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F73f53deb-8629-47fb-b489-4f9863b06d55_1802x1185.png)

滚动浏览为特定 LLM/Imagegen 组合生成的所有图像。

[![](https://substackcdn.com/image/fetch/$s_!0HNm!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fb226ab82-6c3b-4478-a6f5-1e4329271c09_1600x2560.jpeg)](https://substackcdn.com/image/fetch/$s_!0HNm!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fb226ab82-6c3b-4478-a6f5-1e4329271c09_1600x2560.jpeg)

这是一张由两张图片合成的图片，都是对书中图片的进一步优化。上面的图片来自第二章，雅丝美娜公主向柯南询问她的王国为何陷入困境，同时用她美丽的眼睛吸引着他。然而，书中找到的那张分辨率明显较低：1152x858。

[![](https://substackcdn.com/image/fetch/$s_!FGpm!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F22dd5bec-b282-4f9c-ba02-4f8f08c4c62e_1152x858.jpeg)](https://substackcdn.com/image/fetch/$s_!FGpm!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F22dd5bec-b282-4f9c-ba02-4f8f08c4c62e_1152x858.jpeg)

亚马逊Kindle封面需要1600x2560的大小，所以我们将图像放大，使其宽度达到1600以上。这可以用通用的放大和优化轻松完成，在 krita-ai-diffusion 中，有一个方便的选项卡可以从 UI 界面快速完成此操作：

[![](https://substackcdn.com/image/fetch/$s_!jGG5!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fc7fea5c3-ba50-435f-ae61-718f4987379f_456x314.png)](https://substackcdn.com/image/fetch/$s_!jGG5!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fc7fea5c3-ba50-435f-ae61-718f4987379f_456x314.png)

然而，我发现通过放大图像，然后在较低强度和相同提示下优化图像，可以获得更好的图像。对于封面图像，我们很在意效果，所以我们可以让 ComfyUI 生成新版本，直到我们喜欢为止。这是我使用的流程：

[![](https://substackcdn.com/image/fetch/$s_!4h_S!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fe1fc4001-9741-4562-b47e-24b4502bf80b_1010x570.png)](https://substackcdn.com/image/fetch/$s_!4h_S!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fe1fc4001-9741-4562-b47e-24b4502bf80b_1010x570.png)

相关部分用红色圈出。这里发生了什么？我们加载图像，通过简单地插值相邻像素，将其分辨率提高 1.39 倍——从 1152 像素宽到 1601 像素宽——不需要神经网络。然后我们通过 VAE 对其进行编码，以 50% 的去噪率优化图像（必须小于 1.0，否则我们基本上只是生成一张新图像），进行 VAE 解码，并保存它。CLIP 提示是我最初生成图像时使用的提示。然后我只需在 instant-requeue 上运行生成器，直到得到我喜欢的图像。请注意，这种方法会稍微改变图像，但嘿，也许你更喜欢图像以你更喜欢的方式进行微妙的改变，对吧？

顺便说一句，我用于该章节的图像并不是 LLM→Imagegen 流程生成的实际图像。实际上，我采用了我从流程中得到的最好的图像并对其进行了优化。问题是最好的图像是柯南没有穿盔甲，这在文本上是不准确的：

[![](https://substackcdn.com/image/fetch/$s_!5vQe!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fec71c6a1-6768-463d-ad17-b941945df83d_1152x896.png)](https://substackcdn.com/image/fetch/$s_!5vQe!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fec71c6a1-6768-463d-ad17-b941945df83d_1152x896.png)

***由 gemma3:12b-it-qat 生成的提示：*** 雅丝美娜公主双手托着下巴，被他的存在所吸引，用她深邃、黑暗的眼睛专注地凝视着柯南，一种无声的好奇心和逐渐增长的迷恋充满了豪华的房间。, 宽敞华丽的房间

柯南应该穿着锁子甲。所以我调整了提示，然后做了和 upscale 中使用的几乎相同的工作流程，只是没有 upscale。我在否定提示中添加了 shirtless, topless，并在肯定提示中明确指定了他的盔甲：

[![](https://substackcdn.com/image/fetch/$s_!PP64!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F584364b0-cb8d-45b4-9d0d-e95f95f493e1_1198x852.png)](https://substackcdn.com/image/fetch/$s_!PP64!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F584364b0-cb8d-45b4-9d0d-e95f95f493e1_1198x852.png)

我们需要更高的强度，因为我们在这里完全重写柯南的外观，但它的工作方式几乎相同，我们的输出图像仍然保持输入图像的一般形状和构图。

现在是封面图像的下半部分：

[![](https://substackcdn.com/image/fetch/$s_!9EW_!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F9bc75e2c-dba4-4f2d-b96b-1c0366cb1cb5_1600x1600.png)](https://substackcdn.com/image/fetch/$s_!9EW_!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F9bc75e2c-dba4-4f2d-b96b-1c0366cb1cb5_1600x1600.png)

黑色巨像（Black Colossus）是第一部以拯救衣不蔽体的少女为标志性情节线的柯南故事。这张图片来自最后一章的结尾，柯南从邪恶的巫师手中救出了现在赤身裸体的雅丝美娜公主，而这个巫师正要献祭她——当然，他必须先脱掉她所有的衣服才能献祭她。因为一些原因。因为魔法巫师的东西。是的。

所以，在我们大部分符合文本描述的书籍插图中，这是图像（*我已经警告过你上面有裸露内容了，好吗？*）

[![](https://substackcdn.com/image/fetch/$s_!otFz!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F2a8d2bdc-2dcc-4258-b9d7-6a78763170cf_848x800.jpeg)](https://substackcdn.com/image/fetch/$s_!otFz!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F2a8d2bdc-2dcc-4258-b9d7-6a78763170cf_848x800.jpeg)
> **Prompt**: A close-up view of Conan the Barbarian in chainmail, holding dark-haired Princess Yasmela's naked body tightly as she clings to him with convulsive strength. Their embrace is passionate and desperate, reflecting the chaos and destruction that surrounds them. The room still radiates an unholy glow from the black jade altar, but it seems less intense now that the sorcerer's power has been broken. The atmosphere is charged with emotions as both Conan and Yasmela grapple with the aftermath of their harrowing experiences. Despite the carnage that has occurred and the work that lies ahead, they find solace in each other's arms, affirming their bond amidst the ruins of a once-powerful sorcerer's lair. -text, watermark, signature

是的，是的，很好，对吧？没有露点，对吧？但关于亚马逊封面的一点是，情色小说作者已经深入研究了哪些内容会导致你的书在亚马逊上被屏蔽，并且发现任何暗示其中一个角色没有穿裤子，或者女性角色没有穿上衣的暗示，无论是否露出私处，都足以让你的书被屏蔽，并且你的账户可能被封禁。所以我们必须给这些角色穿上一些衣服！在这里，我在 krita-ai-diffusion 中工作，基本上只是在她比基尼上衣和下装的位置粘贴了一些大的棕色多边形，并在柯南的腹部盔甲的位置粘贴了一个灰色斑点，然后用这个提示优化了图像，这个提示是原始提示减去 naked，并在否定提示中加入了 nudity：

> A close-up view of Conan the Barbarian in chainmail, holding dark-haired Princess Yasmela's richly-dressed body tightly as she clings to him with convulsive strength. Their embrace is passionate and desperate, reflecting the chaos and destruction that surrounds them. The room still radiates an unholy glow from the black jade altar, but it seems less intense now that the sorcerer's power has been broken. The atmosphere is charged with emotions as both Conan and Yasmela grapple with the aftermath of their harrowing experiences. Despite the carnage that has occurred and the work that lies ahead, they find solace in each other's arms, affirming their bond amidst the ruins of a once-powerful sorcerer's lair. -text, watermark, signature, shirtless, topless, naked, chain

请注意，这是一个自然语言提示。如果在 krita-ai-diffusion 及其默认模型中使用大量自然语言优化图像，那么你的模型选项可能是 Flux 和 Flux (schnell)；1.5 模型和 XL 模型基本上以基于标签的提示风格工作

## 更多内容！试用图像模型。

我开始制作这本书时有两个基本想法：尝试一些不同的图像生成模型，并尝试使用多模态模型进行图像评分，而不是让人自己浏览成千上万张图像。为了实现这一点，我做了两个概念验证章节，并将它们发布到 substack 上。第一个，我尝试使用 shuttle-diffusion 代替 flux 进行图像生成。像 flux 一样，这是一个自然语言模型，只需四个步骤即可生成良好的图像。在我完成我之前的柯南插图书籍《*猩红城堡（The Scarlet Citadel）*》之后，有人建议尝试一下。所以这是我的原型第一章，主要使用 shuttle 3.1 进行插图，提示由 dolphin3-8b 生成：[黑色巨像，第 1 章：图解柯南历险记](https://brianheming.substack.com/p/black-colossus-chapter-1-illustrated) 。

我发现 shuttle 产生的图像很好，但总的来说不如 flux 那样擅长遵循提示。Shuttle 3.1 也有其自身的特定艺术风格，并且不擅长遵循“动漫风格”或“漫画风格”等风格标签，这在 Shuttle 3 中不是问题。无论如何，当我开始为实际书籍制作插图时，我注意到的一件事是图像在文本上不准确：谢瓦塔斯（Shevatas）是本章的主要人物，他被描述为皮肤黝黑，除了红色缠腰布外什么也没穿。随着章节的进行，语言模型失去了这种语境，并停止描述他，即使我们提示它这样做，我们最终会得到一个穿着深色衣服的普通黑发白人，这是模型对小偷的看法。好吧。我们当然可以尝试更奇特的基于 LLM 的解决方案，让模型编辑提示以添加他的外貌，或者我们可以直接在文本中搜索并替换谢瓦塔斯，用对他的描述来代替，这样语境就不会丢失——我在第 2 章和第 4 章中就是这样做的，强制在所有提到柯南的地方都穿上锁子甲。但在这一点上，我已经厌倦了生成更多的图像，已经积累了超过 20,000 张图像，所以我只是在原型中使用了所有的图像，在 krita-ai-diffusion 中选择了谢瓦塔斯，并将他重新绘制成一个穿着红色缠腰布的巴基斯坦小偷。效果很好。感谢 inpainting。

[![](https://substackcdn.com/image/fetch/$s_!5ZB6!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F3e4c63e2-32dd-4e93-91e8-aec66ed394c3_1152x896.png)](https://substackcdn.com/image/fetch/$s_!5ZB6!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F3e4c63e2-32dd-4e93-91e8-aec66ed394c3_1152x896.png)

> 我的原型中使用的图像。***由 Dolphin3-Llama3.1-8b 生成的提示：*** An illustration depicting Shevatas advancing on the balls of his feet towards the giant serpent, his sword poised to strike. The image should capture the intense action as the snake strikes with blinding speed, narrowly missing the thief who instinctively holds out his sword to block its path. A close-up view would best show the thief's face contorted in fear and surprise, with his eyes tightly shut and a cry escaping his lips., , The next scene transition would be of Shevatas opening his eyes in amazement upon seeing himself still alive, standing over the thrashing serpent now transfixed by the sword he unwittingly found its mark. The background should highlight the eerie red glow from the gigantic gemstone above, casting an otherworldly ambiance on the thief and the slain serpent., , Lastly, the illustration would shift to Shevatas stepping gingerly over the serpent's body and pushing open the door, revealing the treasure-filled interior of the dome. An awe-struck expression would be depicted on his face as he takes in the dazzling array of jewels and precious artifacts arranged in a mesmerizing display that seems almost magical and ethereal under the pulsing crimson light., large ornate room

[![](https://substackcdn.com/image/fetch/$s_!-G78!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F2b9a1c7f-f029-4fb5-8c2d-4f7783ffc197_1152x896.jpeg)](https://substackcdn.com/image/fetch/$s_!-G78!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F2b9a1c7f-f029-4fb5-8c2d-4f7783ffc197_1152x896.jpeg)

在 krita-ai-diffusion 中进行 inpainting 后的图像。只需选择一个包含谢瓦塔斯的区域，然后描述你想要他是什么样子。先粗略地画出他大致应该是什么样子，以便得到更接近你创意愿景的结果。我在实际书籍中使用了这张图片，以保证文本的准确性。

无论如何，虽然我足够喜欢这些图像，但 shuttle 并不适合后期章节中更复杂的图像，因为它的提示跟踪能力不足以完成像一辆由黑色骆驼拉着的战车，由一个长袍巫师坐在里面的恶魔猴子驾驶，绑架公主，然后柯南骑着马追赶它的疯狂事情。实际上，我不确定是否有任何模型可以处理所有这些，但 flux 更接近。

我还尝试了 DreamShaperXL，它生成图像的速度比自然语言模型快得多，并且在《*猩红城堡（The Scarlet Citadel）*》中效果很好。对于这本书，它只对第一章产生了有用的结果，因为基于标签的图像生成对于屏幕上的多个角色效果不佳，没有很好的方法来指定只有其中一个角色的属性。在这个故事中，只有第一章是专注于单一角色的，当然我已经用 shuttle3.1 对它进行了说明。

在制作我上一本柯南插图书籍《猩红城堡》时，我最终产生了用计算机代替我的眼睛从 10,000 多张图像中挑选好图像的想法，将一些工作转移到计算机上。我尝试了大量足够小以在我的 GPU 上本地工作的大型多模态图像+文本→文本模型，发现它们中的大多数都很糟糕。有些模型坚持认为任何图片，包括一张随机的长颈鹿图片，都与文本中描述的完全一致。长颈鹿怎么能是柯南用剑砍杀怪物，这真是令人费解。Facebook 的 Llama-3.2 表现还不错，但随机地认为一扇门的图片是色情作品，并拒绝对其进行评级——有一些方法可以避免愚蠢的拒绝，但我宁愿不使用这样做这些模型，特别是对于涉及血腥和裸露的柯南故事。最终，只有两个模型产生了有用的输出：gemma3 和 dolphin-vision——尽管在我发布这本书后，我发现最近发布的 Mistral-Small-3.2-24B-Instruct-2506 在测试中表现非常好。这是我使用 gemma3 为第 2 章制作的原型：[ Black Colossus, chapter 2: CONAN with Pure Algorithmic Illustration](https://brianheming.substack.com/p/black-colossus-chapter-2-conan-with)


图像提示由 Dolphin3.0-Llama3.1-8B 生成。图像由 fluxFusionV24Steps 生成。图像由 gemma3:12b-it-qat 在艺术性、诗意、非怪异性和文本准确性方面进行评分。包括所有一次性得分 > 37.0/40 的图像（从 1490 张评分的图像中选出 8 张），包括裸露。包括柯南出现后得分 37.0/40 的所有图像（9 张）……

这些图像远不如人类选择的好。在分析模型的输出时，我发现这不仅仅是模型的不准确性：gemma3 会主动降低具有肌肉发达的柯南、穿着华丽的公主或文本准确描述的黑暗魔法的图像的排名，声称它认为这些特征“怪异”，然后给出低排名，尽管被告知只根据图像生成伪影（如额外的手和飞剑）来对非怪异性进行排名。Gemma3 是谷歌的模型，可能反映了谷歌在这里为反人类政治偏见所做的脑叶切除术。当然，对于原型，我没有指示模型假装它是一个喜欢美丽公主和黑暗魔法的柯南粉丝，所以可能有一些我可以在提示中做的反制措施。

我在这里添加了一个类别权重并调整了权重，我发现通过将非怪异性的权重降低到非常低，并将文本准确性加倍计算，我可以让它对最好的图像进行更高的排名。无论如何，我想象通过添加多个类别（例如，美丽、艺术性、诗意、非怪异性、对男性的吸引力、性感、动作、特异性、对柯南粉丝的吸引力），使用一个政治脑叶切除术较少的模型，提示该模型假装它是一个柯南粉丝，并使用一个小的回归模型来权衡类别得分以匹配我的人类偏好，我可能会得到一些非常好的结果，至少对于挑选一个前 10 名供人类进一步挑选而言。但我放弃了它，直到制作完这本书之后，我想象一旦我制作了这本书，我就可以使用我在这本书中选择的图像来测试评分模型并训练类别权重模型。

## 困难案例

有些图像对于文本到图像生成器来说很容易；有些很难；有些基本上是不可能的。它们擅长于风景。在任何涉及单个主要角色的特写镜头中都非常擅长。在将两个看起来非常不同的人放在一个场景中而不会混淆他们的属性方面很糟糕。对于它们几乎没有训练数据的东西来说很糟糕，这包括大多数模型的血腥，但也包括诸如没有马鞍或缰绳骑马之类的东西。在一次性生成具有大量不同且具体描述的怪人的单个图像方面毫无用处。所以当然，我们来到了故事中最难的图像，来自第 4 章：

[![](https://substackcdn.com/image/fetch/$s_!s5fa!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fb7df1095-a3cf-42b1-98ea-316e44338462_1880x660.png)](https://substackcdn.com/image/fetch/$s_!s5fa!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fb7df1095-a3cf-42b1-98ea-316e44338462_1880x660.png)

如果你能读懂这些小字，你会看到它描述了一辆由黑色骆驼拉着的战车，由一个人形黑猿驾驶，穿着长袍的巫师纳托克（Natohk）站在后面，绑架了雅丝美娜公主，然后被柯南扑向。哎哟。难怪由此产生的图像并不完全准确。制作这些图像的简短答案是“inpainting”，尽管“拼贴”也可以。从模型中获得你能得到的最好的东西，它可能只包含两个元素，然后使用 inpainting 模型来填充其余部分，或者单独生成其他元素并使用照片编辑器（如 GIMP）将它们粘贴进去。无论如何，对于这一个，我采用了我拥有的最好的图像并查找了它的提示，故意从提示中删除了巫师纳托克（Natohk），生成图像直到我喜欢一个，然后将一个穿着绿色长袍的巫师（纳托克）重新绘制到战车的后面。所以，用一图胜千言：

[![](https://substackcdn.com/image/fetch/$s_!5g7V!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fe15b5521-a79c-4879-8fab-8c39a8d4a106_1152x896.png)](https://substackcdn.com/image/fetch/$s_!5g7V!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fe15b5521-a79c-4879-8fab-8c39a8d4a106_1152x896.png)

***由 LLM 生成的提示：*** 一辆战车的特写镜头，冲上山谷，一头巨大的黑色生物，类似于骆驼，推动它前进。司机纳托克（Natohk）站在战车上，他的长袍在他身后飘扬，他抓住缰绳，猛烈地鞭打动物。在他旁边蹲伏着一个威胁性的人形生物，可能是怪物猿或其他一些黑暗的异国情调生物，增加了危险和混乱感。, 宽敞华丽的房间(A close-up view of the chariot hurtling up the valley, with a great black creature resembling a camel propelling it forward. The driver Natohk stands in the chariot, his robes billowing behind him as he grips the reins and lashes the animal fiercely. Crouched beside him is a menacing, anthropomorphic being that could be either a monstrous ape or some other dark, exotic creature, adding to the sense of danger and chaos., large ornate room)

重新生成，将纳托克（Natohk）从提示中删除，并将驾驶员修复为猿：

[![](https://substackcdn.com/image/fetch/$s_!I5m0!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F51b48e48-938d-4824-939f-3f5f3a117111_1152x896.avif)](https://substackcdn.com/image/fetch/$s_!I5m0!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F51b48e48-938d-4824-939f-3f5f3a117111_1152x896.avif)

***手动编辑的提示：*** 一辆战车的特写镜头，冲上山谷，一头巨大的黑色生物，类似于骆驼，推动它前进。司机是一个威胁性的人形生物，可能是怪物猿或其他一些黑暗的异国情调生物，增加了危险和混乱感，并抓住缰绳，猛烈地鞭打动物。战车很大，司机后面的座位是空的。(A close-up view of the chariot hurtling up the valley, with a great black creature resembling a camel propelling it forward. The driver is a menacing, anthropomorphic being that could be either a monstrous ape or some other dark, exotic creature, adding to the sense of danger and chaos, and grips the reins and lashes the animal fiercely. The chariot is large, and the seat behind the driver is empty.)

使用 krita-ai-diffusion，在后座上重新绘制一个戴着面具的绿袍巫师，然后裁剪：

[![](https://substackcdn.com/image/fetch/$s_!igMd!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fb843da97-7f42-4e58-80e8-81b736d86d54_1093x804.jpeg)](https://substackcdn.com/image/fetch/$s_!igMd!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fb843da97-7f42-4e58-80e8-81b736d86d54_1093x804.jpeg)


## 总结想法

在这个项目中，我做过多的事情是尝试新东西——新的图像生成模型、不同的语言模型来生成提示、多模态评分模型、摆弄方法论。结果是我最终得到了太多的图像，并且这本书的出版时间比计划晚了几个月。可能，我应该只选择一个主要的事情来尝试，无论是不同的模型、图像评分还是其他什么。尽管如此，我还是能够通过拒绝运行更多的自动生成并使用我拥有的东西来扼杀它。

将审美判断卸载到机器的想法可能有点早，但我们至少可以让机器丢弃那些完全糟糕的图像，并节省一些人类的脑力。我看到基于模型的评分的最大问题是计算费用：更简单的图像生成模型可以在 5 秒内生成图像，并且我的笔记本电脑上的 flux 每 20 秒生成一张图像，不断变化的复杂的自然语言提示。但是目前，能够理解柯南故事的文本并判断图像在该上下文中是否良好的模型需要足够长的时间才能运行，如果我们想在之后对其进行评分，我们会放弃很多生成的图像。当然，我们可能可以做一些优化。如果我们*确实*始终如一地获得良好的审美判断，我们可以悄悄地为所有公共领域的作品添加插图，而无需人类做更多的事情，只需运行一个脚本然后上床睡觉，也许早上只需根据自己的口味裁剪生成的图像。

最后，与我上一本《柯南历险记》插图书籍相同的结束语：

---

鉴于这是 Substack，可能有义务就神经网络用于此的更广泛的社会影响发表意见。嗯，在这种特殊情况下——缺乏插图版本的公共领域故事——我看到了实质性的积极因素，而负外部性很少。我们得到了一个经典故事的详细插图版本，该故事可能从未获得过插图版本，原因可能是其权利被孤立，然后之后，为公共领域故事添加插图没有利润，许多人会简单地免费下载它。我们得到了免费的图像，可供任何人用于各种未来的项目。而且可能没有艺术家未能获得报酬来为它添加插图，因为自从这个故事出版以来的 92 年里，没有艺术家最终获得报酬来为它添加插图。

至于这些技术的广泛社会影响以及关于其训练数据和输出的道德和法律问题，那是另一篇 Substack 帖子的主题，可能由其他人撰写。