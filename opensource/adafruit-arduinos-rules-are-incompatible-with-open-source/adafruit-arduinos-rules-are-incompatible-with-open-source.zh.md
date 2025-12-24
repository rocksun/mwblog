开源硬件社区正在讨论在公司被高通收购后，Arduino 的[新条款和条件](https://www.arduino.cc/en/terms-conditions/)。

[![Arduino_Uno_-_R3 - Creative Commons via Wikipedia - by SparkFun Electronics from Boulder, USA](https://cdn.thenewstack.io/media/2025/12/20d64af2-arduino_uno_-_r3-creative-commons-via-wikipedia-by-sparkfun-electronics-from-boulder-usa-150x150.jpg)](https://cdn.thenewstack.io/media/2025/12/20d64af2-arduino_uno_-_r3-creative-commons-via-wikipedia-by-sparkfun-electronics-from-boulder-usa-150x150.jpg)

Arduino 微控制器板

主要的微控制器竞争对手 Adafruit 认为，新条款通过限制云工具的逆向工程、主张用户上传内容的永久许可，以及对人工智能相关功能实施广泛监控，威胁了开放原则。

Arduino 为这些修改辩护，声称限制仅适用于其 [SaaS 云应用程序](https://thenewstack.io/cloud-services/)，数据处理是现代平台的标准操作，并且其对开源硬件的承诺保持不变。

## 关于 Arduino 新条款和条件的争议

上周，我与 Arduino、Adafruit 和 EFF 讨论了高通在[十月收购](https://thenewstack.io/can-arduino-teach-a-tech-giant-how-to-win-over-developers/)这家以其[单板微控制器套件](https://youtu.be/QxPBCBX8ac8)而闻名的公司。

许多批评来自竞争对手 Adafruit，其产品包括兼容 Arduino 的硬件套件。11 月下旬，Adafruit 的执行编辑 Phillip Torrone [在 LinkedIn 上警告其 36,000 多名关注者](https://www.linkedin.com/posts/adafruit_opensource-privacy-techpolicy-activity-7396903362237054976-r14H/)（除其他事项外），Arduino 用户现在“被明确禁止进行逆向工程，甚至不得尝试理解该平台的工作原理，除非 Arduino 授权”。

但 Arduino [在一篇博客文章中回应称](https://blog.arduino.cc/2025/11/21/the-arduino-terms-of-service-and-privacy-policy-update-setting-the-record-straight/)，“逆向工程的限制特别适用于我们的软件即服务云应用程序。任何开放的东西都将保持开放。”

一位 Arduino 发言人表示，他们的博客文章让许多读者感到放心，他们表示“理解并松了一口气，我们对[开源精神](https://thenewstack.io/open-source/)的承诺坚定不移，Arduino 的核心使命保持不变。”然而，Adafruit 的批评性 LinkedIn 帖子获得了超过 1,575 个赞。我要求双方澄清他们的立场。这是否真的代表着自 Arduino 于 2004 年成立以来的一个转折点？

以下是他们的看法。

## 逆向工程：云应用程序与硬件板

我问了 EFF 竞争和知识产权诉讼总监 Mitch Stoltz，他同意 Arduino“没有对改装或逆向工程 Arduino 板施加任何新的禁令”。

与 Adafruit 一样，Arduino 的主要用户群是家庭爱好者。Arduino 提供了一个开源电子平台——其中包括 [Arduino UNO](https://www.arduino.cc/product-uno-q) 等单板微控制器——以及各种套件/扩展板/配件，以及开发软件。

[![Limor_Fried_TC2013 (Creative Commons via Wikipedia) - by TechCrunch from TechCrunch Disrupt NY 2013 Day Three](https://cdn.thenewstack.io/media/2025/12/085e125a-limor_fried_tc2013-creative-commons-via-wikipedia-by-techcrunch-from-techcrunch-disrupt-ny-2013-day-three-207x300.jpg)](https://cdn.thenewstack.io/media/2025/12/085e125a-limor_fried_tc2013-creative-commons-via-wikipedia-by-techcrunch-from-techcrunch-disrupt-ny-2013-day-three-207x300.jpg)

Limor Fried（维基百科）

尽管如此，Adafruit 创始人 Limor “Ladyada” Fried 表示，Arduino 的回应“轻描淡写了云和网络工具在 Arduino 体验中变得多么核心”。

Fried 说：“如果你访问 Arduino 软件页面和云页面，你会强烈被鼓励使用云编辑器/网页 IDE 和云计划，尤其是在 ChromeOS 等平台上，[云编辑器](https://cloud.arduino.cc/)是推荐或唯一可行的途径。” “所以当 Arduino 说‘这些限制仅适用于 SaaS’时，这仍然意味着这些限制适用于许多新用户被引导作为其主要 Arduino 环境的工具。”

“最重要的是，使用这些云工具通常需要一个 Arduino 账户，注册流程中会突出显示营销和画像同意，包括同意出于商业目的处理个人数据和为定制优惠进行画像。”

[![Adafruit's LadaAda shares screenshot of Arduino signup - ag1Ca7zTnZDHZ4dS](https://cdn.thenewstack.io/media/2025/12/c2f26d6f-adafruits-ladaada-shares-screenshot-of-arduino-signup-ag1ca7ztnzdhz4ds.png)](https://cdn.thenewstack.io/media/2025/12/c2f26d6f-adafruits-ladaada-shares-screenshot-of-arduino-signup-ag1ca7ztnzdhz4ds.png)

Fried 说：“这与‘下载本地 IDE 并直接开始修改硬件’的模式大相径庭。”

她指出，“即使底层固件和库保持开源，许多用户的实际切入点也在发生变化”，因为账户与个人数据绑定，引入了营销和画像提示，并与集中式、订阅导向的云服务相关联。

## 理解用户上传内容的许可

[![](https://cdn.thenewstack.io/media/2025/12/2d396bc0-1685947-300x300.jpg)](https://cdn.thenewstack.io/media/2025/12/2d396bc0-1685947-300x300.jpg)

Phillip Torrone

Adafruit 的 Torrone 还表示，Arduino 的新文件“对用户上传的任何内容引入了不可撤销的永久许可”。

但 Arduino 辩称，他们只是在澄清“您选择在 Arduino 平台上发布的内容仍然属于您，并且可以用于启用您请求的功能，例如云服务和协作工具”。

在后续采访中，Arduino 发言人提供了澄清示例：

* “如果用户在他们的 Arduino Cloud 订阅中上传代码草图，内容仍归他们所有，对他们来说是私有的，授予 Arduino 的许可权利严格限于执行请求的功能（例如在云中编译草图）。”
* “如果用户将代码或内容上传到 Project Hub 或论坛，并且内容对所有其他用户可见，则 Arduino 要求用户（保留内容所有权）授予处理发布的许可。”

“[W]没有这个许可，我们将无法在云端运行用户项目或在论坛中显示他们的帖子，这就是为什么任何现代云服务或社交平台通常都需要这种类型的许可。”

EFF 的 Stoltz 指出，Arduino 的旧使用条款也要求对发布材料的使用进行许可，他称这“对于任何在线平台来说都是正常的”。

但 Stoltz 补充说：“尽管如此，条款的一些变化仍令人担忧。”

Arduino 的旧条款“不同寻常地赋予用户随时撤销该许可的能力。新条款取消了这一能力，使许可变得不可撤销。看到一个曾经特别保护用户的平台回归常态，这令人失望。”

## 用户数据和删除账户的权利

Arduino 还指出了一项额外的隐私保护措施。“所有用户保留随时请求删除其账户和/或内容的权利。删除后，相关内容将不再对其他用户可见。”

Torrone 曾抱怨“即使在账户删除后，用户名仍保留多年”，但 Arduino 称这“是对我们政策的误解……当用户请求删除账户时，我们会立即删除账户并从所有相关论坛帖子中删除用户的用户名。”

“用户名五年公共保留期仅适用于 24 个月未登录其 Arduino 用户账户*且*未提交任何数据或账户删除请求的用户。”（在这些情况下，Arduino 寻求一种状态，即“贡献仍归属于非活动用户名，以表彰他们对社区的贡献。”）

因此，对于那些两年未活跃的用户，账户会自动停用，Arduino 的博客文章澄清说，但用户名会保留在 Arduino 论坛中，“以响应论坛社区维护用户生成内容归属的明确请求。”（如果用户确实请求删除账户，“用户名将立即删除，相关帖子将匿名化。”）

即使如此，对于那些非活跃账户，“五年后，用户名将被删除，”Arduino 发言人解释说，“相关用户帖子或评论将去身份化。”

“此政策并非旨在用于商业用途的数据保留，而是仅仅为了帮助保留内容归属，这是社区强调的宝贵之处。”

但 Adafruit 的 Fried 仍然认为用户名保留和不删除的方式存在令人担忧的模式。“对待社区身份和数据的政策选择是将其视为受管理资产，而不是用户可以完全控制的东西。”

## Arduino 上的 AI 功能和用户监控政策

文化差异最明显体现在新条款和条件中列出了几项“禁止使用的 AI 用途”，其中包括犯罪使用和违法行为、意图伤害（包括传播虚假信息和操纵或欺骗行为）、生成面部识别数据库和[军事用途](https://news.ycombinator.com/item?id=46013385)。

Arduino 的博客文章指出，其新的 AI 功能是可选的——包括 AI 驱动的[计算机视觉和音频模型](https://www.arduino.cc/en/uno-q/)以及[带预训练 AI 模型的 IDE](https://docs.arduino.cc/software/app-lab/)。但在新条款和条件中，Arduino “保留监控用户账户和 AI 产品使用情况的权利……[以]验证是否遵守法律和本政策。”

Arduino 表示，监控是为了“遵守现行法律法规，包括适用的隐私法、出口管制和其他全球监管要求”，以及“验证是否符合法律和政策标准”。他们补充说，其最终目标是“保护用户和 Arduino”，并实现“AI 产品的稳健可靠运行”。

但他们的条件还包括出于其他原因进行监控的权利，包括“管理和运营 Arduino 的业务”。

Adafruit 的 Fried 表示，Arduino“当然应该遵守适用法律并对明确的犯罪活动证据作出适当回应”。但“他们应该设计其 AI 和云产品，以便监控具有狭窄的目标、适度且解释清晰，而不是默认对所有用户进行广泛监控。”

> “你不能说‘这段代码是开源的，但不得用于军事目的’，同时还称该许可是开源的。”
>
> **— Adafruit 创始人 Limor Fried**

Fried 反而认为这是“一种持续的监控姿态，而不仅仅是对具体、有充分根据的滥用报告作出回应”。

所以，是的，一个开源应用程序可以监控面部识别数据库的创建或军事用途，“只要他们透明地说明他们记录了什么、保留了多久以及在什么情况下进行审查。”但人们担心“广泛的持续监控会侵蚀用户信任，尤其是在教育/创客环境中，许多人是未成年人或业余爱好者，他们期望一个相对私密的环境。”

还有一个更大的原则问题。Fried 说：“真正的开源许可证[不允许限制使用领域](https://www.gnu.org/licenses/gpl-faq.en.html?utm_source=chatgpt.com#NoMilitary)。”“你不能说‘这段代码是开源的，但不得用于军事目的’，同时还称该许可是开源的。”

一旦你将某物呈现为开源，你就不再能挑选“好”用户或“坏”用户。Fried 称这种限制“与[开源许可](https://thenewstack.io/how-do-open-source-licenses-work-the-ultimate-guide/ "开源许可")从根本上不兼容”，并希望看到 Arduino 将其删除。“如果一个项目想要那种控制，它应该诚实地称自己为‘源代码可用’或类似的东西，而不是开源。”

Torrone 指出，Arduino 的条款和条件还规定，用户承诺不使用 Arduino 平台或服务“识别或提供证据支持对 Arduino……或 Arduino 或 Arduino 关联公司的任何供应商和/或直接或间接客户的任何潜在专利侵权索赔。”但这些细节几乎不值一提。Fried 表示，Arduino 的使用限制“实际上凌驾于许可证本应保证的自由之上”。

## Arduino 和开源社区的下一步是什么？

“透明度和开放对话是 Arduino 精神的基础，”其发言人周五表示，“理解社区的担忧，我们渴望澄清事实并重申我们对开源社区的承诺。”

该代表还补充说：“我们致力于继续听取社区反馈。”

那么 Adafruit 接下来会怎么做呢？Fried 周五表示，Adafruit 不会改变，并将“继续设计和发布开源硬件，提供硬件、固件和软件，以便人们可以从中学习、修改和在此基础上构建。”该公司还支持“多个”生态系统，并继续致力于 Wi-Fi/蓝牙低能耗 (BLE) 芯片、基于 Matter 的物联网 (IoT) 以及 Linux 基金会的实时操作系统 [Zephyr](https://www.zephyrproject.org/)。

“我们始终乐于与其他创客和公司合作，包括 Arduino，只要合作能让我们提供拥有强大文档和真正开源许可的优秀产品。”