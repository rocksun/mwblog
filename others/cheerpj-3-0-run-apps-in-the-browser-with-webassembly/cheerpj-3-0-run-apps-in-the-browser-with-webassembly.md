<!--
title: CheerpJ 3.0: 在浏览器中用WebAssembly运行应用
cover: https://cdn.thenewstack.io/media/2024/02/b46c95e3-cheerpj-3.0-1024x538-1-1024x459-1.jpg
-->

CheerpJ 3.0标志着在浏览器中利用WebAssembly部署应用程序取得重大进展，特别是Java应用。

> 译自 [CheerpJ 3.0: Run Apps in the Browser with WebAssembly](https://thenewstack.io/cheerpj-3-0-run-apps-in-the-browser-with-webassembly/)，作者 B. Cameron Gain 是ReveCom Media的创始人和首席分析师。 20世纪80年代初，他黑掉了太空侵略者控制台，可以整天打游戏只需25美分，从那时起他就对计算机着迷。

[CheerpJ](https://cheerpj.com/) 3.0展示了[WebAssembly](https://thenewstack.io/webassembly/)在浏览器中的一个有趣的应用，表明其有潜力用于部署和运行用[Java](https://thenewstack.io/what-do-java-developers-think-of-the-rise-of-genai/)编写的复杂应用程序和运行时环境。开发人员可以用任何语言创建应用程序，并通过简单点击就可打包部署，使最终用户可以测试和使用。

虽然CheerpJ 3.0的开发仍在继续，但它代表了用WebAssembly在浏览器中部署应用程序的重大进步，特别是用Java。这补充了其他侧重于加密和能够将用[C++](https://thenewstack.io/c-on-the-move/)编写的应用程序部署到浏览器中的项目。

![Zoom](https://cdn.thenewstack.io/media/2024/02/64ada4bc-capture-decran-2024-02-13-185936.png)

随着[CheerpJ 3.0](https://labs.leaningtech.com/blog/cheerpj-3-deep-dive)的发布，该公司声称Java客户端应用程序，例如Java小程序、Java Web Start应用程序和独立的Java应用程序，可以在现代浏览器上无修改地运行，无需本地Java安装。其理念是使运行时环境(在本例中是Java)能够更好地运行，就像用户拥有端点服务器的资源可以自由发挥一样——在浏览器中。

“就像[Docker](https://www.docker.com/?utm_content=inline-mention)允许您在计算机上运行二进制文件的容器一样，您需要拥有使您能够在浏览器中以与通常在普通平台操作系统上相同的方式运行二进制工作负载的技术。” [Leaning Technologies](https://leaningtech.com/)的首席执行官兼创始人[Stefano Marco Maria De Rossi](https://www.linkedin.com/in/sderossi)向The New Stack透露。

设置CheerpJ 3.0相当简单，文档中有清晰的步骤概述，且与绝大多数浏览器兼容，该公司称。在游乐场方面，使用CheerpJ iText合并PDF文件非常简单。用户只需将PDF文件输入API，点击几次鼠标，文件就在“浏览器中完成合并”。您需要先访问iText[演示页面](https://cheerpjdemos.leaningtech.com/iTextDemo.html):

![Zoom](https://cdn.thenewstack.io/media/2024/02/390e102e-capture-decran-2024-02-07-174645-1024x371.png)  

上传您要合并的PDF文件，并按提示合并文档:

![Zoom](https://cdn.thenewstack.io/media/2024/02/c0331e35-capture-decran-2024-02-07-173433-1024x360.png)

按提示合并PDF文件即可:

![Zoom](https://cdn.thenewstack.io/media/2024/02/6d5c7d85-capture-decran-2024-02-07-173823-1024x476.png)

如上例所示，可以在CheerpJ 3.0的WebAssembly模块中编写和实现Java，以便[跨浏览器分发和执行](https://leaningtech.com/demo/)任何用Java编写的应用程序，至少在理论上是这样。近期内会有更多用CheerpJ在浏览器中运行的有趣应用程序。

Leaning Technologies提供的一个更有趣的例子，展示了它如何通过CheerpJ在浏览器中启用Java，那就是[Browsercraft](https://browsercraft.cheerpj.com/)，它允许在浏览器中运行Minecraft游戏，以便用户可以直接(免费)玩游戏:

![Zoom](https://cdn.thenewstack.io/media/2024/02/63dcd8ee-capture-decran-2024-02-13-203734-300x136.png)
 
![Zoom](https://cdn.thenewstack.io/media/2024/02/d0091d43-capture-decran-2024-02-13-203547-300x141.png)

## 引擎盖下

![Zoom](https://cdn.thenewstack.io/media/2024/02/402488cb-capture-decran-2024-02-13-185928.png)  

文档中将CheerpJ 3.0描述为一个在浏览器中编译Java字节码为JavaScript的WebAssembly [Java虚拟机](https://thenewstack.io/this-week-in-programming-microsoft-jumps-back-into-java-with-openjdk-build-preview/)(如上所述)，其组件包括:

- 一个用于Java字节码的WebAssembly JVM和即时编译器。类文件中包含的代码进行编译和优化。JIT编译器支持诸如内联和动态虚拟化等高级优化。
- OpenJDK的完整且未修改的构建版本。  
- 一个虚拟化的系统层，包括:
  - 通过HTTP访问资产的虚拟化文件系统，通过IndexedDB提供本地持久化R/W存储，通过/str/与JavaScript数据交互。
  - 通过Tailscale提供虚拟化网络支持。支持服务器和客户端应用程序。

正如De Rossi所指出的，在不使用WebAssembly的情况下，开发人员必须分别针对x86、Linux或其他目标体系结构使用运行时代码，无论是使用[Rust](https://thenewstack.io/rust-project-reveals-new-constitution-in-wake-of-crisis/)、C++、[Python](https://thenewstack.io/python-for-beginners-when-and-how-to-use-tuples/)、Java还是任何其他语言。代码被编译以在不同平台上运行。但是Wasm代表了一个统一的目标。“关键区别在于，Wasm是独一无二的，不管您的浏览器是Linux上的Chrome还是macOS上的Safari亦或Windows上的Firefox。” De Rossi说。“最终，Wasm创建了这种抽象，允许工具制造商为几乎任何语言创建工具。是的，由于Wasm变得越来越强大，越来越类似于本机平台，未来会出现越来越多的语言。”  
