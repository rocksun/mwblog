# 2025 年最危险的 JavaScript 漏洞

![2025 年最危险的 JavaScript 漏洞的特色图片](https://cdn.thenewstack.io/media/2024/09/c4219e20-wesley-tingey-uk1lnvksmyw-unsplash-1024x683.jpg)

JavaScript 再次[成为 Stack Overflow 年度开发者调查](https://survey.stackoverflow.co/2024/technology)中排名第一的编程语言（总体排名，不仅仅是 Web 开发），击败了[Rust 等竞争对手](https://thenewstack.io/rust-growing-fastest-but-javascript-reigns-supreme/)，但这并不意味着它坚不可摧。

相反，JS 在客户端进行验证，这意味着黑客不断开发新的方法来利用漏洞，并始终领先于开发人员和安全专家。

因此，在本文中，我们将探讨对 JavaScript 开发人员造成最大困扰的漏洞和攻击媒介。从目前的情况来看，这些问题将在 2025 年及以后继续成为热门话题。

## JavaScript：安全问题和挑战

2023 年，一种特别恶劣的 JavaScript 恶意软件[在全球 40 家银行和 50,000 名用户中肆虐](https://thehackernews.com/2023/12/new-javascript-malware-targeted-50000.html)。它通过网络钓鱼传播，生成虚假登录页面，并配备恶意 JS 代码，旨在窃取 OTP（一次性密码）和其他登录数据。

这个案例，以及许多类似的案例，突出了这样一个事实，即使像 JS 这样无处不在的东西也可能容易受到攻击。

首先，当然会造成声誉损失。但如果攻击者利用 JS 漏洞并设法访问用户数据，尤其是如果数据[以 MS 365 备份的形式保存](https://www.cloudally.com/microsoft-365-backup/)或[保存在保护不当的 Google Drive 上](https://cybersecuritynews.com/google-drive-security-flaw/)，后果将不堪设想。

如果发生此类事件，被利用的网站可能要对任何经济损失负责。更不用说，相关当局将仔细审查该网站，并检查是否存在任何其他违规行为。

更糟糕的是，有数千个第三方 JS 库，每个库都有各种已知的漏洞，攻击者可以利用这些漏洞，难度各不相同。如果网站所有者未能实施相关的[安全策略，例如 CSP 和 SRI](https://sansec.io/guides/csp-sri)，这些风险可能会被放大，因为 JavaScript 环境[没有内置的安全权限作为标准](https://github.com/nodejs/security-wg/issues/993)。

重点是：如果你不在乎为了安全目的加强你的 JS 代码，那么成本将是惊人的！

## 2025 年需要注意的 7 个 JavaScript 漏洞

攻击者正在转向新的、更先进的技术来绕过现有的安全协议，并将 JS 变成他们的摇钱树。与此同时，一些旧的威胁仍然潜伏在幕后。

### 1. 高级跨站脚本攻击 (XSS)

XSS 攻击[涉及黑客将恶意脚本注入网站](https://owasp.org/www-community/attacks/xss/)，可以通过多种方式实现。一旦注入，脚本通常会执行恶意软件，当用户访问网站或应用程序时，恶意软件会感染网站或用户的机器。

目标是窃取敏感信息或修改网站以进行恶意活动。这种攻击通常针对银行、金融机构和[处理金融交易的网站](https://internationalbanker.com/technology/banks-remain-uniquely-vulnerable-to-sophisticated-cyber-attacks/)。

这可能是网络犯罪分子[读取银行对账单](https://www.docuclipper.com/blog/how-to-read-a-bank-statement/)、[记录财务详细信息的输入（嗅探）](https://sourcedefense.com/glossary/javascript-sniffers-js-sniffer/)，以及寻找漏洞来攻击最终用户或金融机构本身的一种偷偷摸摸的方式。

### 2. 跨站请求伪造 (CSRF)

跨站请求伪造 (CSRF)[迫使经过身份验证的最终用户执行意外的操作](https://portswigger.net/web-security/csrf)。它通常通过社会工程技术传播，例如在电子邮件、网络聊天或短信中发送链接，诱骗用户转账或输入财务详细信息。

如果这种技术损害了具有高访问权限的用户，可能会危及整个应用程序及其所有用户，后果将更加灾难性。更糟糕的是，[人工智能生成的攻击使情况更加复杂](https://thenewstack.io/why-ai-cant-protect-you-from-ai-generated-attacks/)，因为很难区分假页面和真页面。
因此，除了教育网络用户了解社会工程学风险外，防止 CSRF 攻击最有效的方法是在相关请求中[包含 CSRF 令牌](https://brightsec.com/blog/csrf-token/)。这些令牌强制执行严格的标准，这些标准与每个用户会话唯一绑定，从而阻止恶意行为者发起攻击。

### 3. 服务器端 JavaScript 注入 (SSJI)
服务器端代码注入漏洞存在于将用户可控数据集成到由代码解释器动态验证的字符串中的 Web 应用程序中。

如果数据未正确验证，威胁行为者可以[修改输入并注入在服务器上执行的任意代码](https://secops.group/a-deep-dive-into-server-side-javascript-injection-ssji-vulnerabilities/)。如果成功，这种类型的攻击可能会在数据和功能方面损害整个应用程序，甚至使用 Web 服务器对其他系统发起更多攻击。

为了防止 SSJI 攻击，用户可控数据不应[包含在动态评估的代码中](https://softwareengineering.stackexchange.com/questions/157698/what-is-meant-by-dynamic-code-evaluation)。如果无法做到这一点，则所有代码都需要严格验证，最好使用仅接受特定值的白名单。

### 4. 表单劫持
表单劫持是一种古老的威胁，但仍然可以相对轻松地导致数据盗窃。所需要的只是一个粗制滥造的代码库，然后就会发生以下情况：

- 攻击者通常会将一小段 JS 代码注入网站的表单处理流程中。
- 当用户提交表单时，恶意 JS 会拦截数据并将其发送到攻击者的服务器，然后再（或代替）发送到合法目的地。
- 用户和网站所有者通常不知道盗窃行为，因为表单的行为正常。
表单劫持是一个日益严重的问题，特别是对于电子商务网站或任何[通过表单处理敏感用户信息的 Web 应用程序](https://unit42.paloaltonetworks.com/anatomy-of-formjacking-attacks/)。应对这种众所周知的风险的唯一方法是定期运行完整性检查并为用户提供一次性付款选项。

### 5. 原型污染
原型污染是一种 JS 漏洞，[允许威胁行为者向全局对象原型添加任意属性](https://learn.snyk.io/lesson/prototype-pollution/)，用户定义的对象也可以继承这些属性。然后，这些原型可用于允许或覆盖对象行为。

为了发起攻击，威胁行为者必须识别允许任意代码执行的 JS 函数或 DOM 元素。

在利用这些全局对象后，黑客可以控制 Web 应用程序中原本无法获得的属性，从而允许他们从内部发起攻击。

在客户端 JavaScript 被利用的情况下，[黑客可能会尝试进行 DOM XSS](https://book.hacktricks.xyz/pentesting-web/xss-cross-site-scripting/dom-xss)。同时，在服务器端，原型污染通常用于执行远程代码执行。

### 6. 不安全的直接对象引用 (IDOR)
不安全的直接对象引用 (IDOR) 主要影响[依赖用户提供的输入来访问对象和数据库记录的 Web 应用程序](https://www.vaadata.com/blog/what-are-idor-insecure-direct-object-references-attacks-exploits-security-best-practices/)。

这种不正确的访问控制实现会导致这些控制被重定向，从而授予威胁行为者未经授权的访问权限。想象一下一个[使用 Node.js 构建的应用程序从数据库中访问用户 ID](https://www.loginradius.com/blog/engineering/guest-post/nodejs-authentication-guide/)，以及由此引发的一系列问题。

如何[对抗 IDOR 攻击](https://cheatsheetseries.owasp.org/cheatsheets/Insecure_Direct_Object_Reference_Prevention_Cheat_Sheet.html)？开发人员在构建 JS 应用程序时应避免使用直接对象引用，而是[实施用户输入验证](https://cheatsheetseries.owasp.org/cheatsheets/Input_Validation_Cheat_Sheet.html)、全局唯一标识符 (GUID) 和随机标识符来防止 IDOR 漏洞。

### 7. 供应链攻击
供应链攻击针对用于提供 Web 功能的第三方工具和服务。例如，包含预先编写的脚本以[使开发网站和应用程序更容易](https://levelup.gitconnected.com/the-good-bad-and-ugly-of-using-third-party-libraries-b0ddb2bf990c#:~:text=Time%20and%20Effort%20Savings%3A%20Third,unique%20aspects%20of%20their%20applications.)的第三方库。

因此，间接攻击针对将第三方工具连接到应用程序的依赖项，例如为 AI 聊天机器人提供支持或允许网站接受付款的依赖项。
攻击者通常会针对特定供应商，在其软件中添加恶意代码，然后在客户安装更新时将其推广到客户。由于客户信任来源，这些攻击可以成功地大规模渗透。

[2024 年 6 月使用 Polyfill.io JS 库的攻击](https://censys.com/july-2-polyfill-io-supply-chain-attack-digging-into-the-web-of-compromised-domains/) 可能是这种类型攻击的最新示例。虽然显而易见的解决方案是关注知名开源库，但这也会通过减缓[更新、更高效的 JS 库](https://thenewstack.io/top-10-javascript-libraries-to-use-in-2024/) 的采用来抑制创新。

## 结论
JavaScript 在构建网站和 Web 应用程序方面的优势显而易见，但这种编程语言的广泛流行也带来了风险。由于 JavaScript 在客户端进行验证，因此保护应用程序的过程变得更加困难。

许多这些漏洞[是在应用程序开发时创建的](https://www.synopsys.com/blogs/software-security/javascript-security-best-practices.html)，其中输入验证错误和使用用户可控数据是两种最常见的错误。

但是，一些攻击需要更高级的缓解技术，例如使用安全令牌。在外面注意安全。

[YOUTUBE.COM/THENEWSTACK](https://youtube.com/thenewstack?sub_confirmation=1)
技术发展迅速，不要错过任何一集。订阅我们的 YouTube 频道以流式传输我们所有的播客、访谈、演示等。