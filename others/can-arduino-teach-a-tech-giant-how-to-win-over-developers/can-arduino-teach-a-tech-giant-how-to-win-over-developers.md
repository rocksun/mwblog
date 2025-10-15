
<!--
title: 小小Arduino，能否给科技巨头上“开发者一课”？
cover: https://cdn.thenewstack.io/media/2025/10/868db9de-daniel-andrade-0izc2kyhyio-unsplashb.jpg
summary: 高通收购Arduino，旨在通过其社区推广边缘AI和机器人技术。新推出的UNO Q板卡和App Lab开发环境支持Linux和AI工作流，是高通开放生态、赋能开发者的战略转变。
-->

高通收购Arduino，旨在通过其社区推广边缘AI和机器人技术。新推出的UNO Q板卡和App Lab开发环境支持Linux和AI工作流，是高通开放生态、赋能开发者的战略转变。

> 译自：[Can Arduino Teach a Tech Giant How To Win Over Developers?](https://thenewstack.io/can-arduino-teach-a-tech-giant-how-to-win-over-developers/)
> 
> 作者：Mary Branscombe

开发者和创客对高通收购开源电子原型平台Arduino的[消息](https://www.youtube.com/live/uYb8YzdMWbc)反应不甚积极。高通坚称Arduino仍将是一个开放的生态系统，并且该公司将作为一家独立的子公司，与多家芯片供应商合作——只是现在拥有更广阔的覆盖范围。

人们担心高通可能不会对Arduino进行投资，或者误解其优势。但讽刺的是，这正是高通需要Arduino的原因：帮助它更好地与开发者和创客合作。

## 高通针对开发者社区的战略布局

尽管Arduino拥有约3万名工业和企业[专业板卡](https://www.arduino.cc/pro/)的商业客户，但高通真正追求的是其全球超过3300万创客和开发者的社区——更不用说它在硬件初创公司中的普遍存在，这些公司使用Arduino进行从原型开发到实验室测试系统运行的各种工作。其目的可能是向这些现有用户推销更强大的计算能力，特别是用于边缘AI和机器人技术。

Arduino公司本身的历史有些复杂，偶尔还充满争议。它早已不是一家勇敢的学术初创公司，曾经历过[商标和制造权方面的激烈分歧](https://makezine.com/article/maker-news/arduino-cc-arduino-org-reconcile-settlement-agreement-become-one-company/)，并自2022年以来筹集了[5400万美元的风险投资](https://blog.arduino.cc/2023/09/06/what-will-we-do-with-an-additional-22m/)。然而，持续开放工具和规范需要大量的资源。

该公司从未真正建立起[承诺的Arduino基金会](https://hackaday.com/2017/06/19/the-arduino-foundation-whats-up/)，该基金会本应负责管理Arduino IDE——这款软件一直是让一代开发者接触嵌入式系统编程的门户。那么，Arduino能否保持其独立性、[保持开放](https://content.arduino.cc/assets/Arduino%20Open%20Source%20Report%202024.pdf)，并教会高通如何理解和支持开发者呢？

> “高通收购Arduino，是继此前整合Foundries.io和Edge Impulse之后，又一个战略性转变，旨在通过自助服务方式赋能开发者。”
> 
> **—— Leendert van Doorn，高通工程高级副总裁**

“高通收购Arduino，是继此前整合Foundries.io和Edge Impulse之后，又一个战略性转变，旨在通过自助服务方式赋能开发者，”工程高级副总裁[Leendert van Doorn](https://www.linkedin.com/in/leendert-van-doorn-740170/)告诉The New Stack。

“具体来说，对于Arduino UNO Q板卡，所有源代码均公开可用并集成到上游仓库中，允许开发者独立于高通构建和定制软件。此举为该公司未来的基于Linux的产品建立了新标准。”

这样的文化变革不仅使开发者更容易与高通合作；它们也更有可能让Arduino保持真正的独立性。到目前为止，Foundries.io（去年被高通收购）和Edge Impulse都已实现这一点，Edge Impulse仍支持多家硬件供应商。但和所有文化变革一样，高通不会一夜之间变得更加开放。

> “高通能否以及如何维持Arduino的开源精神，这将非常有趣……”
> 
> **—— James Governor，RedMonk联合创始人兼分析师**

“高通的业务建立在大批量销售给客户的基础上，所以这无疑是一个改变，”RedMonk联合创始人兼分析师[James Governor](https://www.linkedin.com/in/jamesgovernor/)告诉我们。“高通能否以及如何维持Arduino的开源精神，以及它能否帮助Arduino抓住新市场——即机器人技术，这将非常有趣。然而，Arduino目前非常偏向于业余爱好者市场。”

Governor表示，这可能需要一种平衡：高通能否“既足够放手，不至于搞砸它正在收购的东西，又足够积极，将Arduino重新定位为机器人和工业制造公司的原型开发平台”？

## 借UNO Q板卡连接两个世界

Arduino和高通不仅宣布了收购，他们还已经合作开发了一款售价44美元的板卡，名为[UNO Q](https://www.arduino.cc/product-uno-q)。这是一款相当典型的Arm SBC（一种单板计算机，集成了CPU、GPU、RAM和存储，用于物联网、工业控制器和机器人等嵌入式应用），配备了一颗经济型高通Dragonwing处理器，运行完整的Debian Linux。但它背面也带有一个Arduino微控制器，用于连接构建高通推荐Dragonwing使用的机器人和“日常物联网设备”所需的传感器和执行器，并通过一个Arduino桥接库处理它们之间的通信。

> Arduino和高通已经合作开发了一款售价44美元的板卡，名为UNO Q。

这不是第一次尝试将Arduino和Linux置于同一个系统上，但这可能是第一次成功。Arduino Yun（使用了一个相当冷门的Linux发行版）和TRE（因诉讼而取消）都没有产生太大影响，而Arduino的Portenta X8则明确面向其工业客户。

在工业物联网中，将传感器、控制器和与其协同工作的AI视觉模型结合起来变得越来越普遍。但是，那些需要其设备拥有复杂用户界面和数据存储，或者像板载AI一样高要求的创客，以及需要读取传感器和控制电机或其他电子设备的创客，通常不得不[自己集成这两个系统](https://raspberrypicase.com/can-raspberry-pi-and-arduino-work-together-and-how/)，这通常意味着需要额外的连接组件。

这是Arduino长期以来一直希望解决的问题。它希望提供一款产品，该产品拥有Raspberry Pi的强大功能，采用经典的UNO外形（和引脚布局）——现有Arduino用户所熟悉——并与现有可为Arduino板卡添加功能和连接性的扩展板兼容。价格当然与高端Pi相当；性能可能不及，尽管高通声称这些系统将非常适合运行本地AI模型（您还可以获得内置的实时控制）。

## 新的App Lab开发环境

这意味着您不仅仅需要Arduino IDE来使用UNO Q，因此还有一个新的（同样是开源的）[App Lab开发环境](https://www.arduino.cc/en/software/#app-lab-section)，它支持Arduino、C++、Python、Linux和AI工作流，包含库和名为“bricks”的模块化组件，开发者无需考虑处理Docker容器等复杂问题。如果您想用Python在Linux上通过USB摄像头构建一个带有图像识别功能的智能门锁，然后让Arduino在识别出您时驱动电机解锁门，App Lab提供了一个统一的平台来实现这一切。

[![Arduino UNO Q](https://cdn.thenewstack.io/media/2025/10/4670ed28-image3-6.png)](https://cdn.thenewstack.io/media/2025/10/4670ed28-image3-6.png)

*UNO Q为您提供了一个完整的开发栈；图片来源：高通*

一个巧妙之处是：虽然您可以在普通电脑上运行App Lab，但它也预装在UNO Q上：只需插入显示器和键盘，您就可以使用运行在Dragonwing上的Debian来编程Arduino MCU。

Arduino此前已经与[Edge Impulse](https://edgeimpulse.com/arduino-integrations)合作，后者是高通最近收购的另一家公司，旨在简化从传感器数据到部署AI模型的流程。App Lab包含了多个可在UNO Q上运行的预构建AI模型——包括对象检测、音频分类（如识别“唤醒词”，如果您连接麦克风）、计算机视觉（只需插入USB摄像头）和异常检测。Dragonwing的GPU支持OpenCL，开发者可以使用App Lab或标准的Edge Impulse CLI工作流上传或训练自己的模型。

App Lab还使用Arduino Cloud进行设备生命周期管理和远程更新。如果您想使用自定义的Debian或Yocto镜像，App Lab则会利用高通最近收购的另一家公司FoundriesFactory，该公司提供[一个用于开源嵌入式开发的SaaS平台](https://foundries.io/products/)（类似于AWS IoT或Azure Sphere）。

## Arduino如何开放高通的生态系统

Arduino是第一个让任何开发者都能轻松入门嵌入式系统的平台，也是原型开发的标准，但它现在面临诸多竞争：Adafruit的Circuit Python、支持多种硬件选项的PlatformIO IDE、ExpressIf ESP板卡，以及来自Nordic、NXP和Silicon Labs等知名厂商的预认证Matter堆栈，这些都让开发者可以编写应用程序，并将硬件视为一个纯粹的平台。高通的支持可能会减轻一些压力，并允许Arduino扩展到如今必不可少的AI领域。

Arduino在专业制造领域的声誉不如其在创客市场中那样强大，尤其是在需要合规性和干扰测试的设备方面。高通在手机和汽车领域的经验可能会在这方面助其一臂之力。

初创公司能够从使用创客板进行原型开发，到与同一供应商合作生产集成所有功能的定制设计，这种想法并不总是现实的。但高通可能押注，那些从原型阶段就使用其芯片的硬件初创公司，将会在设备中不可被定制逻辑板替代的AI部分继续使用高通的芯片。

> 高通需要学习如何更好地支持开发者；而这正是Arduino可以教给他们很多东西的领域。

过去，开发者通常从高通那里获得的是评估套件和开发套件，通常包含用于设备原型开发的特定硬件附件，或者模块和参考设计——有时与[微软等平台供应商](https://azure.microsoft.com/en-us/blog/microsoft-and-qualcomm-accelerate-ai-with-vision-ai-developer-kit/?msockid=008cd2595c2d61d01ab4c3ac582d631f)合作提供。这非常适合高通的典型客户——设备制造商，但对于更广泛的开发者来说，效果并不总是那么好。

十年前，高通与Arrow合作，后者制造了[DragonBoard](https://www.arrow.com/en/research-and-events/articles/qualcomm-snapdragon-with-arrow)——第一款预装Android的骁龙芯片开发板，面向物联网和嵌入式开发者。这款产品并未在市场上留下深刻印象。最近，高通与微软合作设计的Snapdragon X Elite Dev Kit——旨在为开发者提供一个桌面设备，用于为基于Arm的Copilot+笔记本电脑构建应用程序——[屡次延迟后突然取消](https://www.jeffgeerling.com/blog/2024/where-qualcomms-snapdragon-x-elite-dev-kit)。高通表示它未能达到其通常标准，微软则暗示，鉴于所有这些延迟，开发者已经可以购买更强大的笔记本电脑了。

## Arduino改变高通交付硬件和软件的方式

UNO Q是一个更加开放的提案；无需签署条款和条件即可查看硬件信息，您可以像订购任何其他板卡一样从Arduino商店订购它。它是开源硬件，具有标准的硬件抽象层，因此代码可以在不同板卡之间移植。[原理图、引脚布局和CAD文件](https://docs.arduino.cc/hardware/uno-q/)均已可用，理论上其他制造商可以生产兼容板卡（尽管他们必须是高通的合作伙伴才能获得Dragonwing处理器，并且可能需要以不切实际的大批量订购）。

这是Arduino已经改变高通交付硬件和软件方式的第一个迹象。通常，高通提供闭源的SDK——例如高通神经网络处理SDL，其针对Windows的延迟交付意味着基于Arm的Copilot+笔记本电脑虽然首先上市销售，但直到数月后才对开发者有用——同时支持常见的开源项目。

> 尽管高通在持续开源贡献方面没有像Arduino那样悠久的历史，但它一直在加大对Linux、Mesa、U-boot和可使用其芯片的开源AI项目的上游贡献……

尽管高通在持续开源贡献方面没有像Arduino那样悠久的历史，但它一直在加大对Linux、Mesa、U-boot和可使用其芯片的开源AI项目的上游贡献。

运行在Dragonwing上的是标准的Debian Linux，选择它是为了吸引开发者（如果不是用于生产用途，至少可以用于原型开发）。作为高通的首次尝试，[该项目建立在上游Debian之上](https://github.com/arduino/arduino-deb-images/tree/428f37ea60bcc8ff87bc1e438554485a3691b0fd)，持续基于最新内核进行rebase，并随项目进展提交补丁，这意味着补丁质量必须足够好，才能在项目进行中被上游接受，而不是等到最后才希望它能迅速发生。

这是一种对开发者友好的方法，有望成为所有高通支持Linux设备的规范，在这种模式下，开发者无需向高通请求信息，更不用说许可了：他们可以直接上手并进行所需的任何更改。