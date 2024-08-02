
<!--
title: Tauri：将JavaScript与Rust结合构建GUI桌面应用
cover: https://cdn.thenewstack.io/media/2024/07/a75b38c0-tengyart-7puyvaygtta-unsplashb.jpg
-->

我们重新审视 Tauri，这是一个使用任何前端框架和 Rust 核心构建桌面应用程序的框架。我们查看了 2.0 beta 版。

> 译自 [Tauri: Mixing JavaScript With Rust for GUI Desktop Apps](https://thenewstack.io/tauri-mixing-javascript-with-rust-for-gui-desktop-apps/)，作者 David Eastman。

在 [我 2022 年 1 月对 Tauri 的首次评论](https://thenewstack.io/how-tauri-turns-web-designs-into-compact-native-apps/) 中，我指出它是一个框架，可以使用任何前端框架和 Rust 内核构建桌面应用程序。由于 Rust 语言在过去两年半的时间里 [在流行度方面取得了显著进步](https://thenewstack.io/rust-the-future-of-fail-safe-software-development/)，我认为再次回顾 Tauri 是值得的——尤其是因为它 [最近发布了 2.0 版本](https://v2.tauri.app/blog/tauri-2-0-0-beta/)。

Tauri 的宣传语是 **“构建一个针对多平台部署的优化、安全且与前端无关的应用程序”**，这与之前的说法一致，但更多的部署目标使其更符合我最近发布的 [其他](https://thenewstack.io/introduction-to-omakub-a-curated-ubuntu-environment-by-dhh/) [产品](https://thenewstack.io/introduction-to-moonbit-a-new-language-toolchain-for-wasm/)。额外的好处是，可以使用熟悉的 Web 方法构建桌面和移动应用程序。

> 我们获得了 Rust 的安全性，但也获得了 Web 开发的熟悉性和灵活性。

我们将尝试看看构建一个可以在我的 Mac 上完全打包运行的 UI 应用程序的路径是否变得更加平滑。Tauri 仍然将自己称为一个“工具包”，这仍然是事实。

从概念上讲，Tauri 充当一个静态 Web 主机。因此，Tauri 与 Rust 框架和系统的原生 Web 视图协同工作，以输出一个体积适中的可执行应用程序。理论上，我们获得了 Rust 的安全性，但也获得了 Web 开发的熟悉性和灵活性。

[入门](https://v2.tauri.app/start/) 路线看起来更新了一些，现在流行的是单行启动。在我们开始之前，我怀疑我有一个旧的 Rust 安装，所以我应该更新它。使用 [先决条件说明](https://v2.tauri.app/start/prerequisites/#rust)：

![](https://cdn.thenewstack.io/media/2024/07/705ae8ee-untitled-1024x191.png)

最后，它提醒您启动一个新的 shell 或使用 env 文件。我注意到所有这些都有一种新的更友好的口吻——就好像，也许，Rust 现在很流行！

好的，现在我应该可以使用 Tauri 的单行命令：

![](https://cdn.thenewstack.io/media/2024/07/f9dfdc5c-untitled-1-1024x183.png)

请注意，我们已经进入了 Tauri 2.0 的测试版。

模板安装选项认识到工具包的多样性。我可以使用 .NET，但我将使用 JavaScript 来获得更通用的视图。显然，Rust 也可用。

![](https://cdn.thenewstack.io/media/2024/07/7b0d7dd2-untitled-2-1024x301.png)

我保留了我稍微旧的 npm/node 组合并构建了我的模板：

![](https://cdn.thenewstack.io/media/2024/07/bfd72f83-untitled-3-1024x188.png)

然后我们在开发环境中运行模板：

![](https://cdn.thenewstack.io/media/2024/07/41674c6e-untitled-4-1024x246.png)

这将构建我们开始所需的所有包，第一次需要几分钟。这些将是 Rust 与您的操作系统窗口通信的方式。最终，它将启动应用程序：

![](https://cdn.thenewstack.io/media/2024/07/441eccf6-untitled-5-1024x685.png)

因此，我们启动了一个应用程序，它弹出了，在我的托盘中显示为一个标准的 Mac 应用程序。

好的，让我们看看它是如何组成的。在我们深入研究之前，请注意，点击图标会启动一个浏览器页面，在文本框中输入您的姓名并按下按钮会显示一个问候语：

![](https://cdn.thenewstack.io/media/2024/07/2906a162-untitled-6.png)

这将帮助我们稍后找出 Rust 的一部分。代码结构是人们对 Web 应用程序的期望：

![](https://cdn.thenewstack.io/media/2024/07/b7aeb688-untitled-7-1024x391.png)

我选择了原生 JavaScript，因此我们在模板中得到了一个非常原生的 **index.html**：

```html
<!doctype html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <link rel="stylesheet" href="styles.css" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>Tauri App</title>
  <script type="module" src="/main.js" defer></script>
</head>
<body>
  <div class="container">
    <h1>Welcome to Tauri!</h1>
    <div class="row">
      <a href="https://tauri.app" target="_blank">
        <img src="/assets/tauri.svg" class="logo tauri" alt="Tauri logo" />
      </a>
      <a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript" target="_blank" >
        <img src="/assets/javascript.svg" class="logo vanilla" alt="JavaScript logo" />
      </a>
    </div>
    <p>Click on the Tauri logo to learn more about the framework</p>
    <form class="row" id="greet-form">
      <input id="greet-input" placeholder="Enter a name..." />
      <button type="submit">Greet</button>
    </form>
    <p id="greet-msg"></p>
  </div>
</body>
</html>
```

中央 `div` 显示一个锚点中的图像，该锚点处理链接行为。请注意，JavaScript 位于 **main.js** 中，窗口本身的应用程序标题与这里定义的标题不同。我们有一个非常老式的 `form` 用于输入文本。因此，我们知道我们将不得不处理该表单以提取输入的名称，并将结果放置在最终的 `p` 中。这是 **main.js** 的内容：

```javascript
const { invoke } = window.__TAURI__.core;
let greetInputEl;
let greetMsgEl;

async function greet() {
  // Learn more about Tauri commands at https://tauri.app/v1/guides/features/command
  greetMsgEl.textContent = await invoke("greet", { name: greetInputEl.value });
}

window.addEventListener("DOMContentLoaded", () => {
  greetInputEl = document.querySelector("#greet-input");
  greetMsgEl = document.querySelector("#greet-msg");
  document.querySelector("#greet-form").addEventListener("submit", (e) => {
    e.preventDefault();
    greet();
  });
});
```

在选择活动元素并为表单按钮添加事件侦听器之后，我们会运行一个处理输入并将之粘贴到输出段落的函数。这需要调用一些 Rust，所以我们了解一些它的工作原理。

如果我们回到在生成区域中的主目录，我们会注意到 src-tauri：

![](https://cdn.thenewstack.io/media/2024/07/8d96c808-untitled-9-1024x394.png)

而有些 Rust 代码位于 src 中的 main.rs 中：

```rust
// Learn more about Tauri commands at https://tauri.app/v1/guides/features/command
#[tauri::command]
fn greet(name: &str) -> String {
  format!("Hello, {}! You've been greeted from Rust!", name)
}

fn main() {
  tauri::Builder::default()
    .plugin(tauri_plugin_shell::init())
    .invoke_handler(tauri::generate_handler![greet])
    .run(tauri::generate_context!())
    .expect("error while running tauri application");
}
```

我们能够看到 JavaScript 中的 invoke 调用到达处理字符串的 Rust greet 函数。这是很好的一点，因为我们可以使用 Tauri 帮我们管理的 Rust 函数。（我们还需要了解 greet 函数的生成器。）

要显示的最终文件是以 JSON 格式的，用于控制窗口本身，tauri.conf.json：

```json
{
  "productName": "thenewstack",
  "version": "0.0.0",
  "identifier": "com.tauri.dev",
  "build": {
    "frontendDist": "../src"
  },
  "app": {
    "withGlobalTauri": true,
    "windows": [
      {
        "title": "thenewstack",
        "width": 800,
        "height": 600
      }
    ],
    "security": {
      "csp": null
    }
  },
  "bundle": {
    "active": true,
    "targets": "all",
    "icon": [
      "icons/32x32.png",
      "icons/128x128.png",
      ...
    ]
  }
}
```

为了确保我们理解了一切，让我们设定一个可识别的目标，并称呼一个友好的新问候者。

“我们改变上述目标以使其更小，并添加一个唯一的标识符：

```json
{
  ...
  "identifier": "io.thenewsatck",
  ...
  "app": {
    "windows": [
      {
        "title": "Welcome to TheNewStack",
        "width": 600,
        "height": 200
      }
    ],
    ...
  },
  ...
}
```

然后我们适当地更改消息代码。这将强迫构建检查更改。

最后，我们运行完整构建，以查看它对可执行文件所做的更改。

![](https://cdn.thenewstack.io/media/2024/07/644eaa80-untitled-10.png)

当然，这是需要时间的，因为它是第一次。结果是dmg和app文件。一旦我们把app移动到应用程序文件夹中，我们可以像正常的mac应用程序一样执行它：  

![缩放](https://cdn.thenewstack.io/media/2024/07/e0543acc-untitled-13-1024x417.png)  

应用程序大小仍然有点胖（10.7 mb），但我没有做任何事情来精简自动添加到模板的板条箱。  

## 结论 

我认为我们很快从零变英雄与模板，尽管允许一系列 JavaScript 框架的灵活性确实让一切都变得有点复杂。我想知道更武断的方法是否会更好。但总体而言，我认为 Tauri 仍然是打造桌面应用程序而无需担心窗口内部的一个非常可靠的解决方案。