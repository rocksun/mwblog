
<!--
title: 最新Node.js有什么，以及如何安装？
cover: https://cdn.thenewstack.io/media/2025/01/3878e196-getty-images-nvlb6gvemlc-unsplash-1.jpg
-->

最新长期支持版 Node.js 在保持其作为企业级 JavaScript 应用程序首选运行时的同时，带来了更新。

> 译自 [What's in the New Node.js, and How Do You Install It?](https://thenewstack.io/whats-in-the-new-node-js-and-how-do-you-install-it/)，作者 Jack Wallen。

[Node.js](https://thenewstack.io/dev-news-node-js-23-and-rust-1-82-released-this-week/) 仍然是最流行的 [JavaScript](https://thenewstack.io/5-technical-javascript-trends-you-need-to-know-about-in-2025/) 运行时之一。事实上，它就像一个巨无霸：自 2009 年推出以来，它似乎势不可挡。事实上，Node.js 是 JavaScript 的行业标准运行时，被 [Netflix](https://thenewstack.io/developer-productivity-engineering-at-netflix/)、Uber、eBay、PayPal、[LinkedIn](https://thenewstack.io/linkedin-shares-its-developer-productivity-framework/)、Trello、[NASA](https://thenewstack.io/nasa-programmer-remembers-debugging-lisp-in-deep-space/)、沃尔玛、Groupon 等许多公司使用。

这个开源的跨平台运行时环境是开发可扩展网络应用程序的绝佳工具，并且已成为最广泛使用的 Web 框架之一。Node.js 如此流行的原因之一是它可以将加载时间减少多达 60%。对于大规模应用程序而言，这极其重要。

但是，最新版本有什么值得兴奋的呢？说实话，您必须回到 23.0.0 版本才能找到一个未被特别列为安全版本的版本。由于 23.0.0 版本于 2024 年 10 月 16 日发布，在科技年代中它可能看起来有点过时了，但它是一个 LTS 版本，因此它将存在一段时间。

至于 Node.js 23 中的新功能，让我们来看一下。

此版本有四个主要亮点：

- `require(esm)` 语句已默认启用。这允许您使用 `require()` 函数加载 ESM 模块。这对于仍然依赖于 [CommonJS](https://thenewstack.io/how-javascript-is-finally-improving-the-module-experience/) 但又想利用 ESM 功能的项目特别有用。
- 已删除对 Windows 32 位系统的支持。
- `node --run` 命令已稳定。
- 测试运行器已增强。

### require(esm)

默认启用 `require(esm)` 后，当使用 `require()` 加载 ES 模块时，Node.js 将不再抛出 ERR_REQUIRE_ESM 错误。但是，如果要加载的 ES 模块包含顶级 await，它仍然可能抛出 ERR_REQUIRE_ASYNC_MODULE 错误。

### Windows 32 位系统

如果您仍在使用 32 位 Windows 操作系统，Node.js 23.0.0 将不再运行。

### node --run

Node.js 提供了一个内置的任务运行器，允许您执行在 package.json 文件中定义的特定命令。这是使用 `--run` 标志完成的，并且在 23.0.0 版本中，该选项得到了改进，现在更加稳定。

### 测试运行器

Node.js 测试运行器使创建 JavaScript 测试成为可能。以下是测试运行器的一些增强功能：

- 它现在支持 glob 匹配覆盖文件。
- 包括对 v8-stats 的更新。
- 当未使用 `--test` 时仅检测测试。
- 始终使 spec 成为默认报告器。
- 将 lcov 报告器公开为可新建函数。
- 支持在 run() 中使用自定义参数。
- 添加了 test:summary 事件。
- 添加了通过 run() 支持覆盖率。

## 其他更改

v23 中 Node.js 的其他更改包括：

- V8: cherry-pick cd10ad7cdbe5
- 从 v23 版本开始，在 AIX 上使用 GCC 12
- 在触发事件之前将中止状态传播到相关信号
- 更改 WeakMap 和 WeakSet 比较处理
- Buffer: 写入缓冲区之外时抛出异常
- Buffer: 使文件可克隆
- Build: 将嵌入器字符串重置为“-node.0”
- Build: 包含 v8-sandbox.h
- CLI: 删除已弃用的 v8 标志
- CLI: 删除 –no-experimental-global-customevent 标志
- Crypto: 运行时弃用 crypto.fips
- Net: 验证服务器侦听的主机名
- Process: 删除 process.assert

您可以在此处阅读完整的 [Node.js 更改日志](https://nodejs.org/en)。

## 如何安装 Node.js 23

首先，让我们在基于 Ubuntu 的 [Linux](https://thenewstack.io/introduction-to-linux-operating-system) 发行版上安装 Node.js 23。为此，请按照以下步骤操作。

使用以下命令安装必要的依赖项：

`sudo apt-get install ca-certificates curl gnupg -y`

使用以下命令导入必要的 GPG 密钥：

```
curl -fsSL https://deb.nodesource.com/gpgkey/nodesource-repo.gpg.key | sudo gpg --dearmor -o /etc/apt/keyrings/nodesource.gpg
```

使用以下命令添加 Node.js 存储库：

```
NODE_MAJOR=23
echo "deb [signed-by=/etc/apt/keyrings/nodesource.gpg] https://deb.nodesource.com/node_$NODE_MAJOR.x nodistro main" | sudo tee /etc/apt/sources.list.d/nodesource.list
```

使用以下命令更新 apt：

`sudo apt-get update`

使用以下命令安装 Node.js：

`sudo apt-get install nodejs -y`

接下来，我们将使用 nvm 作为安装程序在 macOS 上安装 Node.js 23。

使用以下命令下载并安装 nvm：

`curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.40.1/install.sh | bash`

使用以下命令下载并安装 Node.js：

`nvm install 23`

最后，我们将使用 fnm 在 Windows 上安装 Node.js 23。

使用以下命令使用 winget 下载并安装 fnm：

`winget install Schniz.fnm`

使用以下命令安装 Node.js 23：

`fnm install 23`

您可以使用 `node -v` 命令验证安装。

您应该在输出中看到类似以下内容：

`v23.6.1`

如果您发现 Linux 系统仍然报告版本 20，则需要删除 Node.js (`sudo apt-get remove nodejs -y`)，然后按照以下步骤安装它。

使用以下命令下载并安装 nvm：

`curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.40.1/install.sh | bash`

关闭并重新打开您的终端窗口。终端打开后，使用以下命令安装 Node.js：

`nvm install 23`

这就是安装最新版 Node.js 的全部步骤。这个强大的运行时将在未来数年内为您提供良好的服务。
