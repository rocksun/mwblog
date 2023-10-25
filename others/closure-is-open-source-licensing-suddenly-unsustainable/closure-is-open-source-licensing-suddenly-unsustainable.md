<!--
# 封闭：开源模式的可持续性遭质疑
https://cdn.thenewstack.io/media/2023/10/eaab2562-231010-hashiconf-02-day-1-keynote-dave-mcjannet-ceo-1024x576.jpg
Scott， HashiConf 2023 webcast.
 -->

HashiCorp 最近决定将旗下产品Terraform转为更严格的商业许可证，这可能不是最后一家寻求对旗下产品带来的市场运营享有更大控制权的公司。

译自 [Closure: Is Open Source Licensing Suddenly Unsustainable?](https://thenewstack.io/closure-is-open-source-licensing-suddenly-unsustainable/) 。

我们似乎一直在回避这个讨论：开源软件到底属于谁？从法律上说，它仍属于最初的创造者。软件开发社区享有的任何权利，都只是通过软件许可被创造者授予的。

这样的授权是否意味着创造者永远无法声称对软件背后的理念拥有排他权？更重要的是，它是否可以排除创造者对软件带动形成的市场享有排他所有权？

从另一面看，同样的问题也同样合理：假设初创公司进入一个新的未开发市场的唯一途径就是通过开源许可，那么围绕这项创新编写代码的开发者社区是否也应享有创新的部分收益？

这个社区是否可以直接获取这项创新，并将其移植到其他平台上由他人运营？当这种情况发生时，创造者对客户流失是否会有合法的诉求？

现在引发这些问题浮出水面的是Terraform的贡献开发者与其创造者HashiCorp之间出现裂痕。8月，[HashiCorp](https://www.hashicorp.com/?utm_content=inline-mention)宣布将Terraform和其他产品的许可模式从非常宽松的Mozilla公共许可证2.0，[改为](https://thenewstack.io/opentf-disgruntled-hashicorp-rivals-threaten-to-fork-terraform/)MariaDB简洁明确的商业源代码许可证1.1。

![](https://cdn.thenewstack.io/media/2023/10/a290d129-231010-hashiconf-02-day-1-keynote-dave-mcjannet-ceo.jpg)

_HashiConf 2023上的HashiCorp CEO Dave McJannet_


## 商业源代码许可证(Business Source License)

BUSL足够简短，可以在餐巾纸上写出。其首句话最重要："特此授予您复制、修改、创建衍生作品、重新分发许可作品及进行非商业使用的权利。" 这里的关键词是非商业使用。这可以并应该被解释为：根据许可方规定，除非我们书面批准，否则您不能通过对我们产品的贡献获得商业利益，只能在我们规定的条件下进行。(HashiCorp 和数据库制造商MariaDB均拒绝就本文发表评论。)

然而，HashiCorp此举 - 其股票于2021年12月在纳斯达克上市 - 显然不是首次偏离开放许可，未来类似情况可能还会继续出现。最近我们看到：

* [Red Hat](https://www.openshift.com/try?utm_content=inline-mention)将[RHEL代码的可用性限制在](https://thenewstack.io/red-hat-deprecates-linux-centos-in-favor-of-a-streaming-edition/)仅面向商业客户。
* 2018年，[MongoDB](https://www.mongodb.com/cloud/atlas/?utm_content=inline-mention)推出了其服务器端公共许可证(SSPL)，这是一种“源代码可用”许可，要求任何对代码做出贡献的人必须公开发布他人运行代码所需的一切。
* [Redis](https://redis.com/?utm_content=inline-mention)对代码使用的[限制](https://thenewstack.io/redis-pulls-back-on-open-source-licensing-citing-stingy-cloud-services/)特别针对其内存缓存和数据库的扩展模块，在一则后来修改的网贴中声称(未明确指出AWS ElastiCache)"云提供商"寻求通过重新包装的专有托管服务获利。

这里存在更深层次的问题：即使在非常宽松的许可下，软件产品的原创者是否也应被授权或允许排他地拥有并运营围绕该产品形成的市场或生态系统？

如果是这样，就会提出一个问题，即开源许可证是否可以利用托管服务作为支点做开源本意图避免的事情：锁定供应商。但是如果不是这样，开发者随时可以围绕一个产品建立自己的市场。他们还可以保留作为谈判工具的这样做的权利。

这种影响力可以用来约束许可方，防止它威胁更改条款。如果许可方试图从其软件可能制定的任何标准周围形成的生态系统中获利，开发者也可以执行选择权。

最近我们还看到:

* 去年7月，SUSE[分支了最新的公开可用RHEL代码](https://www.suse.com/products/suse-liberty-linux/)，以构建一个新的发行版，与Red Hat最新版CentOS不同，它与RHEL兼容。
* 2021年，亚马逊网络服务分[支了Elasticsearch，命名为OpenSearch](https://thenewstack.io/this-week-in-programming-aws-completes-elasticsearch-fork-with-opensearch/)，表面上是对Elasticsearch加新条款的回应，亚马逊称这会限制其在其云平台上提供搜索作为服务的能力。
* 社区成员多次分支Node.js，因为他们认为其许可条款被[未经授权地修改过](https://thenewstack.io/node-js-forked-complaints-repeated-harassment/)。

也许最典型的例子发生在2015年，当时谷歌实际上将新兴的容器生态系统[从Docker转移到了Kubernetes](https://thenewstack.io/google-officially-launches-kubernetes-1-0-promises-to-give-you-evolution/)。这一切发生得非常迅速和顺利，造成的市场变革极为彻底，以至于当时的市场分析师难以理解发生了什么。

如果开放性是相对的，那么善意也有局限。可以期望一个组织给予开发社区多少开放性，而不会使其资产在投资者眼中贬值？如果无法控制谁应该从技术的使用中获利，最初发明这项技术的意义是什么？

## 非生产

HashiCorp 在这个问题上的立场已经非常明确。[2022年10月](https://thenewstack.io/hashicorp-is-standardizing-and-industrializing-the-cloud/)，在与The New Stack的Alex Williams的访谈中，HashiCorp CEO [David McJanne](https://twitter.com/davidmcj?lang=en)t说他的公司设立Terraform Console(其基础设施即代码语言的解释器)是为了使项目开源。

“但要明确的是，”McJannet宣称，“它们100%由HashiCorp控制。”

真是这样吗？来自广泛Terraform开发者社区的直接反应，是抛弃HashiCorp，取最新开源许可的Terraform，围绕它[建立一个新平台OpenTofu](https://thenewstack.io/linux-foundation-joins-opentf-to-fork-for-terraform-into-opentofu/)，并将其捐赠给[Linux基金会](https://training.linuxfoundation.org/training/course-catalog/?utm_content=inline-mention)。 更重要的是，这些开发者及其支持Terraform的产品和项目也一起迁移到了OpenTofu，实际上将Terraform生态系统的重要部分迁移到了一个全新的平台。

“基于基础设施即代码构建基础设施部署的公司，” OpenTofu的主要贡献开发者之一[Pawel Hytry](https://www.linkedin.com/in/hytry/) 在接受The New Stack采访时评论道，“本着它会保持开源的前提进行运作。这意味着，他们满怀信心地花费多年时间根据这个框架来构建基础设施。

“但这个前提被打破了，”Hytry继续说道，“在我看来，这对更广泛的生态系统意味着，如果前提被打破，总会有开源的替代方案出现。”

“我认为这可能是一个真正的转折点，”Brigham Young大学法学院Hugh W. Colton教授[Clark Asay](https://law.byu.edu/directory/faculty/clark-d-asay/)评论道，

“显然，多年来开源软件运动已经在很大程度上商业化......志愿者社区与领导项目的组织之间的关系，或收购项目的组织，或指导项目的组织之间出现了相当大的负面动态。这类事件可能会推动软件开发向与过去20至30年完全不同的方向发展。”

## 这样合法吗？

HashiCorp通过从开源转向更严格的许可证，是否违反了任何法律?

自美国成立以来，有法律先例确立创意或方法的创造者有权主张对其用途的排他性。但是，一旦这样的方法被指定为公有领域，任何人都不能再合法地声称其为原创。

众所周知，开源软件不属于公有领域。其创始人保留通过许可授予开放可用性的权利。从技术上说，这意味着软件的开源状态永远不能被推定为永久。然而，如果其许可证措词使受让方认为其期限无限，那么事后加新限制可能会被视为违反原许可条款和声明。

换言之，没有任何法律能保证软件分发的开放程度。但违反软件最初可用性条款可能是非法的。广义上，当供应商从宽松许可转向限制性许可，与原宽松许可相矛盾时，这是否合法?

“不一定合法，”Red Hat高级法律顾问兼GPL第3版合著者[Richard Fontana](https://twitter.com/richardfontana)回应说，“取决于情况。”

Fontana解释，对软件的唯一版权持有人，其任何组件都不是他人以许可形式提供的，有各种许可选择。

从开源转向专有许可是一种选择。但像GPL第3版这样的典型开源许可是永久和不可撤销的。这种许可可能施加的条件是有限的，但如Fontana所说，存在一种“社区认可的对这些条件的限制”。

“只要你遵守这些条件，你的许可就是永久的，” Fontana告诉The New Stack，“所以开源软件的许可方不能收回已经授予的许可。但是，如果他们有权利这样做，他们可以决定对未来的修改、新变更或补充使用不同的许可证。”

在不提及任何具体情况下，Fontana补充说，假设的许可方被确定没有权利对之前开放的许可条件加限制，这是完全可能的。一个原因可能是代码库已经积累了来自公司或领域外的贡献，这些贡献本身是以许可形式授予许可方的。

“我认为采取这类步骤的公司往往会非常小心，”Fontana说，“但我确实看到，当这些事发生时，社区会严肃提出这个问题：他们真的有权利这样做吗？这些问题有时非常严肃。”

对BYU的Asay提出的同一问题，他回答“是的，这在法律上是合法的”，但补充了一些注意事项:

“人们可能为这些项目团结合作了多年，在某些情况下，投入了大量时间和资源，这在很大程度上基于参与者之间的这些规范和信任，每个人在某种程度上站在同一立场”，Asay告诉The New Stack，“但严格根据版权法，只要该组织被视为作品、联合作者或版权材料的多个作者之一，那么他们可以根据一套非常宽松的条款对其许可，然后选择非常严格的条款。”

Asay（他的兄弟 Matt，恰巧曾经是 [New Stack 的贡献值](https://thenewstack.io/author/mattasay/)）描绘了原创者和贡献者之间的关系，这些角色之间的界限随时间推移外界观察者和某些记者看来可能变得模糊，但从法律角度通常不是这样。

当发生时，原创者和被许可方之间最初的违反是对信任的违反。

然而，在Asay看来，两方被视为共同作者的界限变得足够模糊并非不可能。存在法律先例支持外部贡献者被判断为工作的大部分内容的提供者。

与如今决定我们命运的许多因素一样，这一先例可能来自我们影响范围之外：2000年，Jefri Aalmuhammed 控告导演 Spike Lee 的一项美国第九巡回上诉法院[裁决](https://law.justia.com/cases/federal/appellate-courts/F3/202/1227/592674/)。Aalmuhammed认为，通过他直接负责的内容量，他已成为李纪录片《Malcolm X 》的“共同作者”。因此，他认为有权获得电影利润的一份。(1976年《版权法》没有明确定义“作者”，但后来的判例法将制作人、导演甚至编辑归结为“作者”。)

第九巡回法院的裁决也许没有取悦任何人，它建立了一个三点测试，在没有明确合同的情况下判断某人是否符合作品的共同作者条件：

- 该人或实体对整体作品的控制程度；
- 所有各方意图共同合作的某种表示——假定存在信任的某种实质理由；以及
- 评估每个参与方对作品的贡献量的公式缺失，否则将确定某人不是共同作者。

Asay教授表示，根据具体情况，联合或单独行事的开发者是否构成开源软件的共同作者，这是一个开放性问题。许可证不是合同，如果它避免声明开发者不是共同作者，该问题仍有待确定。而且，如果开源许可的产品没有销售价格或产生收入，如何分配各方份额的问题可能无关紧要。

归根结底，这个问题可能取决于谁从软件存在中受益最多。解决这个难题可能需要一个现今最高法院不愿做出的决定：软件市场所基于的平台是否是软件本身的一部分？换言之，生态系统是否会吸收并因此具现化赋予它生命的东西？

## “中心化的共享服务”

“Terraform的建立基于它将保持开源的期望”，OpenTofu的Pawel Hytry解释说。“这是前提:我们有社区，我们共同建立这个项目。当然，HashiCorp是推动者，但你也有其他贡献者。这意味着基于基础设施即代码构建基础设施部署的公司，是基于它将保持开源这个前提进行运作的。因此，他们满怀信心地花费多年时间根据这个框架开发基础设施。”

Hytry的主要工作是担任[Spacelift](https://thenewstack.io/sponsor/spacelift/)的CEO，该公司为Terraform及Red Hat Ansible、[Pulumi](https://www.pulumi.com/?utm_content=inline-mention)等设计了基础设施即代码策略代理和管理平台。HashiCorp在以生产[集群管理平台Vagrant](https://thenewstack.io/tns-analysts-show-62-at-hashiconf-2015/)而知名的同时，将Terraform放在了地图上。但可以说，Spacelift和其他类似产品的出现，使Terraform变得可见并获得了合法性。

曾几何时，HashiCorp可能会提出同样的论点。一年半前，就在本刊物上，HashiCorp被举为建立“培育社区”的典范，正如撰稿人Emily Omier所说，与公司关系更交易性的群体形成对比。

现在，根据Hytry的说法，希望成为HashiCorp Terraform注册表中包含配置模块的官方提供商的组织，必须预先承诺生产仅面向Terraform的独占模块。这可能让那些已经认为他们与HashiCorp的关系由Mozilla公共许可证定义的提供商感到惊讶。

“所以我们就建立了自己的开放注册表”，Hytry继续说，“这有点像猫捉老鼠的游戏...... 没有大的云提供商会同意有人可以利用其provider、connector创造垄断。”

OpenTofu基础设施定义或“提供者”注册表目前托管在GitHub上，尽管有消息表示GitHub是一个临时主机。目前，它可能是转型生态系统的临时住所。

如果您不了解提供商周围的情况，McJannet在10月10日的[HashiConf主题演讲](https://thenewstack.io/hashicorp-hears-users-rolls-out-new-testing-qa-tools-for-terraform/)中的措辞可能会被完全不同地解释。在那里，他解释了他继续称为“开源”在Terraform商业产品生命周期中的作用。在他身后，幻灯片将该生命周期分为三个阶段，后两个阶段代表了生命周期的商业部分。 

他解释说，在最初签署客户时，有大约6个月的时间，当时他们正在努力寻找自己的道路，他们的平台团队被混乱所压倒，他们的安全模型悬而未决。“就是在那段时间里，”McJannet说，“我们的开源产品被使用 - 在许多情况下，可能比云原生产品更多，因为已经实现的广泛集成面积有助于标准化了一些核心概念。”

“然后不可避免地，某人必须控制它，”他继续说，“一个核心团队被分配来给它带来某种秩序。” 随着秩序的到来，他继续说，客户合作变得更加合并、可管理和交易化。 CEO将这个核心团队或平台团队描述为公司采用Terraform的自然结果。

“这一直是我们的产品理念的基石，”McJannet宣称，“为了说明清楚，我们的开源产品一直被设计为解决用户的“1.0版本”问题，我们的商业产品 - 因为全球2000很久以前就要求我们这样做 - 满足了将这些作为公司的中心化共享服务进行运行的需求。”

## 这样符合伦理吗？

“当我们谈论开源软件时，我看到不同的伦理系统发挥作用，”Red Hat的Richard Fontana对这个问题的回答是，“在一个层面上，如果你有权利将项目的许可从非常宽松的开源许可更改为不开源的东西 - 更具限制性的非开源许可，在某种程度上，你可以说这是基本的伦理。我们有一个法律系统促进了某种行为，这在规则之内。”

但是Fontana断言，在开源背景下，这更复杂。

“当一些有争议的许可变更发生时，我经常听到使用“诱导式切换”这一短语。我认为这揭示了一个可能的伦理问题。”

Fontana看到一种趋势正在出现，这与McJannet的演示幻灯片非常兼容：初创公司声称非常宽松的开源许可 - 比GPLv3更宽松，更像MPL - 一直到他们成功建立开发社区为止。 “如果一开始你没有使用开源许可，”他说，“你可能不会在围绕项目建立社区方面取得如此成功...... 如果你使用的许可具有限制性，使其不成为开源。”

可能需要供应商几年时间来建立社区的好感和积极的期望。然后，通过一个完全合法的举动，供应商将许可证更改为非开源许可证。 “我认为这里存在一个伦理问题，”Fontana说，“我认为这是一个难题。问题的一部分是，你是否给社区足够的通知？您是否给他们提供反馈的机会 对您看到的问题，这让您想要做出这种许可更改？我确实认为，花费很长时间培育对项目开源的期望，然后切换到不同模式，这是个问题。”

可以断言，McJannet提供了这样的通知 - 例如，在他与Alex Williams的清晰访谈中。 从访谈中推断出的线索能否被解释为“通知”？或者这样的事情必须以书面形式，在法律信笺上？这是您期望法官解决的法律问题。 我们准备开始讨论法官了吗?

“我认为开源社区在很大程度上依靠规范和信任运作”，Clark Asay评论道，“并接受定义和理解。 但一旦那种信任开始消失，你就需要一个仲裁者 - 某人或某事来定义游戏规则。 以前，游戏是基于这些规范进行的。 如果那些规范消失了，那么你需要其他东西来取代它们。 将取代它们的东西可能是版权法和专利法中的默认值 - 其中一些将是相当模糊的，因为这些年来开源没有进行过多的讼诉。 法院介入这一领域，并处理所有这些事实，有助于提供清晰的指导方针。 这也可能会很快走样。”

“人们想要开源，他们想拥有开源的自由，”OpenTofu的Hytry说，“他们不想依赖其他方面。 个人、用户、公司不喜欢依赖别人，特别是如果他们违背了自己的框架或他们建立的东西的初衷。 因此，开源最终会胜利，无论公司有多大。”
