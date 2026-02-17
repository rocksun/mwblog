<!--
title: OpenClaw 安全告急：被称“灾难现场”，Deno Sandbox 带来一线生机！
cover: https://cdn.thenewstack.io/media/2026/02/2611e898-getty-images-g3qsdop2isy-unsplash-scaled.jpg
summary: 本文指出 OpenClaw 存在安全漏洞，并介绍了 Deno Sandbox 作为运行不可信代码的安全方案。它通过轻量级 Linux 微虚拟机和秘密混淆等功能，有效防止数据泄露，在当前生成代码激增的背景下具有重要价值。
-->

本文指出 OpenClaw 存在安全漏洞，并介绍了 Deno Sandbox 作为运行不可信代码的安全方案。它通过轻量级 Linux 微虚拟机和秘密混淆等功能，有效防止数据泄露，在当前生成代码激增的背景下具有重要价值。

> 译自：[OpenClaw is being called a security “Dumpster fire,” but there is a way to stay safe](https://thenewstack.io/deno-sandbox-security-secrets/)
> 
> 作者：David Eastman

早在今年二月的一篇博客中，Snyk 工程师表示他们[扫描了整个 ClawHub](https://snyk.io/blog/openclaw-skills-credential-leaks-research/)（OpenClaw 市场），发现超过 7% 的技能包含暴露敏感凭据的缺陷。他们报告说：“这些是功能强大、受欢迎的代理技能，它们指示 AI 代理错误处理秘密，迫使它们通过 LLM 的上下文窗口以纯文本形式传递 API 密钥、密码甚至信用卡号到输出日志中。”

好的，所以我们知道 OpenClaw 目前是一个安全“垃圾场大火”，[正如我们所报道的。](https://thenewstack.io/openclaw-moltbot-security-concerns/)

我曾关注 [Deno](https://thenewstack.io/how-oop-developers-can-get-to-know-typescript-through-deno/) 一段时间；它将 TypeScript 视为一等公民。我禁不住注意到他们最近的 [沙盒更新](https://deno.com/deploy/sandbox/) 中的这个细节：

*你不希望直接在你的服务器上运行不受信任的代码（由你的 LLM、你用户的 LLM，甚至用户手写生成）。它会危及你的系统，窃取你的 API 密钥，并调用恶意网站。你需要隔离。*

*Deno 沙盒为你提供轻量级的 Linux 微虚拟机（在 Deno Deploy 云中运行），以深度防御安全运行不受信任的代码。*

好的，沙盒并不新鲜，但 Deno 的部署环境引起了我的注意。

### Deno 和 Deno Deploy

嗯，距离我[上一篇关于 Deno 和 TypeScript 的文章](https://thenewstack.io/how-oop-developers-can-get-to-know-typescript-through-deno/)已经有一段时间了，所以我将快速过一遍我的例子，以确保我仍然记得所有内容，然后我们再查看新的沙盒内容。

那么，让我们在我的 Mac 上安装 [Deno](https://deno.com/)。幸运的是，这看起来和以前一样：

![](https://cdn.thenewstack.io/media/2026/02/0f814b57-image-1024x331.png)

和以前一样，Deno 正确检测到了我的 shell。重启后，我检查了一切都很顺利：

![](https://cdn.thenewstack.io/media/2026/02/7bb7584b-image-1-1024x723.png)

所以我不是一个 TypeScript 专家，但在那篇文章中，我写了一些代码来让自己相信 TypeScript 只是根据内容进行等价性判断。（查阅该文章了解更多关于 OOP 开发者如何理解 TypeScript 的信息）

```

class Car {
  drive() {
    // hit the pedal to the floor
  }
}
class Golfer {
  drive() {
    // hit the ball far
  }
}
// No error?
let w: Car = new Golfer();
```

所以让我们做上次做的事情，使用项目初始化器来运行 TypeScript 测试。

![](https://cdn.thenewstack.io/media/2026/02/057578c1-image-2.png)

我用上面提到的 drive 方法示例替换了 *main.ts*，并运行它：

![](https://cdn.thenewstack.io/media/2026/02/7a95bc3f-image-3-782x1024.png)

所以 Deno 将我的 TypeScript 作为一等对象处理，并证明它是一个结构化类型系统。但让我们来看看好东西，并登录 Deno：

![](https://cdn.thenewstack.io/media/2026/02/8b16e47e-image-4-1024x567.png)

在我们使用沙盒之前，我们需要通过一个小的验证环节：

![](https://cdn.thenewstack.io/media/2026/02/ad80cccf-image-5-1024x443.png)

别担心——它只是检查你的信用卡是否存在，使用一个方便的 StripeLink，它会像钓鱼请求一样出现在你的手机上。现在我们可以进行设置了——我将按照右侧的代码集成栏操作：

![](https://cdn.thenewstack.io/media/2026/02/1beb213e-image-6-1024x482.png)

现在，我们面临着将我们的身份连接到我们的请求的典型问题。你可以直接在代码中创建沙盒，这很棒——但首先，我们需要一个令牌。

所以我将创建一个组织令牌来将我的身份连接到 Deno。我按照上面面板的建议安装了 SDK，并使用漂亮的蓝色按钮创建了一个令牌。这里的一个小抱怨是，“访问令牌”、“组织令牌”和“部署令牌”这些术语似乎可以互换使用。

好的，在我的 shell 中设置 DENO_DEPLOY_TOKEN 环境变量后，我们应该准备好运行一些代码并在 Deno 的云上创建我们自己的沙盒了。

我将以下代码保存为 *main.ts*。我将假设 `await` 是一种 promise，因为这显然是异步代码。（“await”这个词在维多利亚时代的散文中也足够熟悉。）

```

import { Sandbox } from "@deno/sandbox"; 
await using sandbox = await Sandbox.create(); 
await sandbox.sh`echo "Hello, world!"`;
```

请记住，为了证明这确实发生了，Deno 即使在沙盒过期后也必须保留其记录。由于我们正在处理安全解决方案，我们确实需要告诉 Deno，我们乐意使用正确的标志进行网络连接：

![](https://cdn.thenewstack.io/media/2026/02/acfbe120-image-8.png)

好的，根据语句的调用方式，这似乎奏效了。更好的证明必须体现在我的记录中沙盒的出现：

![](https://cdn.thenewstack.io/media/2026/02/2231618c-image-9-1024x206.png)

我们可以从仪表板上一个可过滤的事件日志中看到实例的更多细节：

![](https://cdn.thenewstack.io/media/2026/02/275dc57d-image-10-1024x314.png)

嗯，这很顺利。我在我的笔记本电脑上编写了一些代码，并在 Deno 的云沙盒中运行了它。但我们需要做更多事情来避免数据泄露的恐惧。

### 数据泄露防护

究竟什么是数据泄露？当然，我可以举流行多人游戏（你可能知道，也可能不知道）的例子，它们的目的是在游戏服务器中以化身出现，窃取物品，然后逃脱。这在现实生活中也可能意外发生；你见过媒体设法看到一位政客在私人会议中做的笔记，结果他自信地走出去，暴露了他手中的笔记。在这种情况下，这位政客误解了他们的安全界限——或者从未使用过他们相机的变焦功能。

这不是一篇安全文章，我也不是 Bruce Schneier——但你明白了我的意思。你不希望在你的舒适沙盒中运行捕获并带走秘密的代码。一种对抗方法是限制出口点，另一种是在数据驻留在沙盒中时混淆你的私有数据。这就是 Deno 所说的 *秘密修订和替换*。

配置的秘密永远不会进入沙盒环境变量。相反，Deno Deploy 会替换它们，只有当沙盒向经批准的主机发出出站请求时才会揭示它们。

我将部分展示这个过程。我们可以简单地设置一个秘密，以及将揭示它的批准主机：

```

await using sandbox = await Sandbox.create({
  secrets: {
    ANTHROPIC_API_KEY: {
      hosts: ["api.anthropic.com"],
      value: process.env.ANTHROPIC_API_KEY,
    },
  },
});
```

所以这意味着 Deno 将混淆它在我的笔记本电脑中找到的环境密钥，但将其发送给 Anthropic，只有在它离开沙盒 *后* 才会揭示：

我不会在沙盒中对 LLM 进行真实调用（我当然可以，因为我可以通过 CLI 访问沙盒并让它持续我需要的时间），但我会在我的笔记本电脑环境中设置一个秘密，就像我正在做的那样：

![](https://cdn.thenewstack.io/media/2026/02/a4bc1c05-image-12.png)

我的代码修改后：

![](https://cdn.thenewstack.io/media/2026/02/a2b45df8-image-13.png)

我将运行代码并查看沙盒中秘密的值是什么：

![](https://cdn.thenewstack.io/media/2026/02/b0ae2293-image-14-1024x110.png)

正如我所说，要完全证明这一点，我必须用我的密钥联系 Anthropic 来证明这个过程——但我把这个留给你来做。

![](https://cdn.thenewstack.io/media/2026/02/335ba3ad-image-15-1024x371.png)

来自 Deno 教学视频。该图出现在主机下方，因为他们正在演示沙盒。

### 结论

我只关注了一个方面，即混淆，但你也可以同样轻松地控制允许的出站地址。我们已经探讨了 Deno Deploy 服务的其他方面。

显然，时机再好不过了。随着生成和不受信任代码（人们却希望信任）的指数级增长，这种服务就是金子。我相信它很快就会出现在不同的服务中。