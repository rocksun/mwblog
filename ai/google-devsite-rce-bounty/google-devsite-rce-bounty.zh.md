**谷歌花了两个月时间才修补其开发者文档基础设施中的一个未授权远程代码执行（RCE）漏洞**。问题在于一个被重复使用的OAuth客户端密钥，DevSite将其存储在Flask会话Cookie中，并同时用于对会话进行签名。任何恢复该密钥的人都可以伪造一个有效的Cookie并在服务器上执行Python代码。

Otark GmbH的软件工程师[Simon Köck](https://www.linkedin.com/in/simonkoeck/)在谷歌的[DevSite](https://developers.google.com/)基础设施中[发现了这个漏洞](https://simonkoeck.com/writeups/google-devsite-flask-session-pickle-rce)，该基础设施是developers.google.com及几个同级文档网站背后的共享平台。Köck告诉《The New Stack》，所有七个受影响的域都接受了伪造的会话（这些域依赖于两个不同的签名密钥），并且他在其中三个域（developers.google.com、docs.partner.android.com和web.dev）上运行了他的代码执行验证。

> Köck告诉《The New Stack》，所有七个受影响的域都接受了伪造的会话（这些域依赖于两个不同的签名密钥），并且他在其中三个域上运行了他的代码执行验证

谷歌将该漏洞评级为S0（其严重程度等级的最高级别），并[向Köck颁发了90,000美元的漏洞赏金](https://simonkoeck.com/writeups/google-devsite-flask-session-pickle-rce)。这一数字反映了谷歌归类为普通应用层中的S0 RCE的基础赏金75,000美元，乘以1.2倍的卓越报告质量奖励。

Köck通过Python睡眠负载（sleep payload）确认了未授权的RCE，测量了与他的负载相匹配的响应延迟，并刻意没有运行命令或触及文件、凭据或内部服务。“我会称之为一个极其严重的RCE，因为任何人无需账号或与受害者交互就能触及它，”他告诉《The New Stack》，并补充说他不知道他测试的三台主机是否共享相同的后端机器。

> “我会称之为一个极其严重的RCE，因为任何人无需账号或与受害者交互就能触及它，”

更具影响力的未知因素在于服务器本身之后。Köck告诉《The New Stack》，总部位于新加坡的研究员[Arvin Shivram](https://brutecat.com/about)（网名为@brutecat，据他自己统计已报告了130多个谷歌漏洞）随后指出，内部App Engine应用通常可以访问Stubby（谷歌内部的服务间通信系统）。Köck承认这种访问“可能是影响力的主要部分”，尽管他说他没有验证这个特定的DevSite进程能接触到什么。

令人担忧的问题之一是攻击者是否可以修改谷歌的开发者文档，用恶意命令替换安装命令或下载链接。这可能会引发[供应链攻击](https://thenewstack.io/attackers-up-their-game-with-latest-npm-package-compromise/)，但Köck没有测试内容系统的写权限，谷歌也没有公开DevSite的进程权限或后端访问权限。

泄露的密钥还允许Köck伪造DevSite会话，尽管他没有进一步检查这些会话是否可以冒充用户或访问任何人的数据。据他自己计算，已证明的实际影响相当于在三台主机上执行代码，并在七个主机上接受了伪造的会话，而全部的爆炸半径（包括进入谷歌内部服务的任何路径）仍未得到证实。

## 一个OAuth密钥，两项工作

DevSite在Flask会话Cookie中存储了一个来自谷歌 `oauth2client` 库的序列化 `OAuth2WebServerFlow` 对象（谷歌已经[弃用该库并转而支持 google-auth](https://google-auth.readthedocs.io/en/latest/oauth2client-deprecation.html)），在此过程中[暴露了OAuth客户端密钥](https://thenewstack.io/best-practices-for-storing-access-tokens-in-the-browser/)。谷歌还重复使用了该[OAuth客户端密钥](https://thenewstack.io/the-different-token-types-and-formats-explained/)作为DevSite的[Flask会话签名密钥](https://flask.palletsprojects.com/en/stable/quickstart/#sessions)，Köck通过离线重现Cookie的签名确认了这一点，这赋予了他伪造服务器会话接受的能力。

## Pickle将伪造转化为RCE

OAuth回调使用[Python的pickle](https://docs.python.org/3/library/pickle.html)来反序列化会话数据，因此Köck将flow对象换成了恶意的pickle负载，对伪造的Cookie进行了签名，并让回调执行了它。这条漏洞链取决于三个对齐的失误：Cookie中暴露的密钥、充当签名密钥的双重职责的同一个密钥，以及对会话数据的不安全反序列化，修复其中任何一个都能打破它。

> 这条漏洞链取决于三个对齐的失误：Cookie中暴露的密钥、充当签名密钥的双重职责的同一个密钥，以及对会话数据的不安全反序列化，修复其中任何一个都能打破 it。

## 补丁速度引发质疑

Köck于8月6日报告了该漏洞，谷歌于次日接受了该漏洞。该公司于8月27日批准了赏金，但[直到10月7日才部署修复程序](https://simonkoeck.com/writeups/google-devsite-flask-session-pickle-rce)。

谷歌尚未解释两个月的修复窗口期，也没有说明是否实施了临时缓解措施，关于修复本身也存在疑问。Köck对两个独立签名密钥的描述解释了为什么他的建议提到了两个暴露的OAuth客户端密钥，但谷歌尚未确认这两个密钥是否都被轮换，或者现有会话是否已失效。

Köck告诉《The New Stack》，他从未获得法医调查结论，也不知道谷歌在打补丁前是否发现了被利用的证据，该公司也未对此发表评论。截至本文更新时，谷歌尚未回应置评请求。

*本文的早期版本称单个签名密钥在所有七个受影响的域上都有效。Köck表示这些域使用了两个不同的签名密钥。本文也已根据Köck的评论进行了更新。*