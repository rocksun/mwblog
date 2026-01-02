<!--
title: 旧版安卓应用告急！现代加密实践保驾护航
cover: https://cdn.thenewstack.io/media/2025/12/2bc7e8f6-mobile-security3.jpg
summary: 移动开发需更新安全实践。淘汰MD5、SHA-1、DES、AES/ECB等旧算法，改用SHA-256、Argon2、AES/GCM、Android密钥库、ECC等现代加密，提升应用安全性。
-->

移动开发需更新安全实践。淘汰MD5、SHA-1、DES、AES/ECB等旧算法，改用SHA-256、Argon2、AES/GCM、Android密钥库、ECC等现代加密，提升应用安全性。

> 译自：[Securing Legacy Android Apps: Modern Encryption Practices](https://thenewstack.io/securing-legacy-android-apps-modern-encryption-practices/)
> 
> 作者：Stephen Henry

随着软件工程师从初级职位晋升到[移动开发](https://thenewstack.io/intertwined-worlds-platform-and-mobile-app-engineering/)领域的管理岗位，[良好的代码实践](https://thenewstack.io/why-quality-code-matters-and-how-to-achieve-it/)变得越来越重要，不再是事后才考虑的事情。衡量资深能力的标准之一是适应现代安全实践的能力。

值得注意的是，随着移动生态系统快速发展，针对用户数据的攻击也以同样的速度演变。因此，工程师有责任对遗留实现进行现代化改造，即使它们看起来仍然有效。这是因为它们会将用户暴露在安全威胁之下，并使应用程序容易受到攻击。

一些通常隐藏在旧代码下的安全债务包括但不限于：

*   使用[MD5](https://www.okta.com/identity-101/md5/#:~:text=The%20message%2Ddigest%20algorithm%20MD5,matched%20with%20a%20public%20key.)或[SHA-1](https://www.nist.gov/news-events/news/2022/12/nist-retires-sha-1-cryptographic-algorithm)进行密码哈希或验证数据完整性。
*   依赖[DES](https://www.geeksforgeeks.org/computer-networks/data-encryption-standard-des-set-1/)或[AES/ECB](https://www.npmjs.com/package/aes-ecb)进行加密（两者都容易产生可预测模式）。
*   硬编码的API密钥或对称密钥存储在SharedPreferences中，而不是Android密钥库系统。
*   过时的认证流程，例如基本认证(Basic Auth)或自定义令牌处理。
*   使用已废弃且被[ESAPI禁止的API](https://www.appmarq.com/public/tqi,1039044,Avoid-usage-of-BannedAPI-when-using-ESAPI-library)，例如`android.webkit.WebView.setJavaScriptEnabled(true)`和`Math.Random.*`。
*   不符合最新的OWASP十大安全漏洞列表。

AppSec工具（如Checkmarx）对移动应用程序进行的典型安全扫描，通常会揭示上述实践，这些实践曾一度常见，但现在被认为是危险的。

让我们探讨常见的遗留加密算法及其现代替代品。

## 弱哈希算法（MD5和SHA-1）的危险

MD5和SHA-1是已知的密码哈希函数，因其漏洞（包括易受碰撞攻击）而臭名昭著。密码哈希函数接受任何输入（可以是消息、文件或密码），生成该数据的简短而独特的指纹。当两个不同的输入产生相同的哈希值时，就会发生碰撞攻击，攻击者可以通过逆向工程或哈希操纵，导致身份欺骗、[篡改签名数据和其他安全漏洞](https://thenewstack.io/how-iam-missteps-cause-data-breaches/)。

这些算法已被公开破解多年。对于MD5，在消费级硬件上可在毫秒内生成碰撞。一个关键的漏洞是：SHA-1在[谷歌于2017年发起的SHAttered攻击](https://thehackernews.com/2017/02/sha1-collision-attack.html#:~:text=The%20Google%2Dled%20attack%20on%20SHA1%2C%20dubbed%20SHAttered%2C,attackers%20to%20break%20communications%20encoded%20with%20SHA1.)后被官方弃用。随着时间的推移，密码分析表明SHA-1在敏感应用中已不再足够安全。

此外，持续使用这些算法进行密码存储、签名生成或完整性检查可能导致不符合监管机构的要求，例如欧盟数据隐私法GDPR、全球支付卡行业安全标准PCI-DSS等。

## 数据完整性和密码哈希的替代方案

因此，为了保护您的遗留应用程序，请考虑用以下算法替换上述脆弱算法：

对于数据完整性，与其使用MD5校验和，不如考虑更安全的密码哈希函数，例如[SHA-256](https://www.movable-type.co.uk/scripts/sha256.html)或[SHA-3](https://csrc.nist.gov/projects/hash-functions/sha-3-project)。它们对碰撞攻击和原像攻击提供更强的抵抗力。使用SHA-256或SHA-3还能通过确保相同输入总是产生相同哈希值来保证确定性，同时确保即使微小的输入变化也会导致输出的显著变化。这种雪崩效应有助于检测最微小的单比特篡改或损坏。

谈到密码存储和哈希，请考虑一种不仅提供数据完整性而且确保机密性的算法。这正是MD5和SHA-1失败的地方。这些密码哈希函数是为完整性和速度而设计的，但绝不是为了安全的密码存储。此外，这些哈希值总是通过加盐存储，使其容易受到彩虹表攻击。

为了克服这个问题，请考虑使用以安全为重点的算法，例如[bcrypt](https://auth0.com/blog/hashing-in-action-understanding-bcrypt/)、[Argon2](https://argon2.online/)或[PBKDF2](https://hexdocs.pm/pbkdf2_elixir/Pbkdf2.html)。这些不仅是哈希算法，更是密钥派生函数（KDF），旨在抵抗暴力破解和GPU攻击。

基于密码的密钥派生函数2 (PBKDF2) 是最广泛使用的KDF之一，并得到了美国国家标准与技术研究院 (NIST) 的批准。PBKDF2通过向预哈希密码添加盐值来增强哈希密码的安全性，确保相同的密码产生不同的哈希值。这种方法挫败了彩虹表攻击。PBKDF2还应用了哈希过程的多次迭代，称为拉伸。拉伸意味着将哈希函数多次（数千甚至数百万次）应用于密码和盐值的组合。这种方法减慢了哈希计算，从而降低了暴力破解攻击的可行性。

PBKDF2可生成的盐值数量有限，因此工程师有责任单独生成和存储盐值。正是这一限制使bcrypt成为许多人的首选。由于其内置和自动盐值处理，bcrypt被认为更安全，因为它能够抵抗GPU破解。

它较旧、CPU密集型且更易于实现。这使得它成为要求不高的应用或遗留应用的合理选择，但它并不是现有最锐利的工具。为此，Argon2是双刃的“本庄正宗”之剑。

Argon2是一种现代、安全的KDF，旨在通过内存硬性来保护密码，这意味着它需要更多的内存资源。这使得使用快速硬件（如GPU）的暴力破解攻击效率大大降低且成本更高。它还具有高度可配置性，可以对内存使用、迭代次数和并行度等安全参数进行微调，使其能够抵抗不断演进的破解技术。

值得一提的是，KDF应该在后端服务器上实现以进行密码存储，因为客户端（Android）上的哈希处理在服务器被攻陷时是不安全的。

## DES和AES/ECB加密的漏洞

除上述之外，如果您的应用程序使用对称加密作为替代方案，请将AES/ECB或DES替换为[AES/GCM](https://medium.com/@pravallikayakkala123/understanding-aes-encryption-and-aes-gcm-mode-an-in-depth-exploration-using-java-e03be85a3faa)。对称加密是现代密码学的两大基石之一，与公钥（非对称）加密并驾齐驱。在对称加密中，加密和解密使用相同的密钥。它也在现代移动开发中广泛使用，从文件加密和令牌存储到安全偏好设置。

高级加密标准（AES）取代了已废弃的数据加密标准（DES），后者是20世纪70年代的56位对称密码。DES的密钥空间非常小，很容易被暴力破解。

AES/ECB（电子密码本）存在固有的模式暴露弱点。根据设计，AES/ECB将明文分成固定大小的块，并使用相同的密钥独立加密每个块。尽管它很简单，但它被认为是不安全的，因为相同的明文块会产生相同的密文块，从而泄露模式。

## 现代对称和非对称加密替代方案

现代且安全的替代方案包括：

[AES/CBC](https://www.cincopa.com/learn/what-is-cipher-block-chaining-cbc-mode-in-aes#:~:text=Mode%20in%20AES?-,Cipher%20Block%20Chaining%20(CBC)%20is%20a%20block%20cipher%20mode%20of,if%20plaintext%20contains%20repetitive%20patterns.)（密码块链），其中每个明文块在加密前与前一个密文块进行[异或运算](https://www.youtube.com/watch?v=h7Cgx-pn9bw)，从而产生链式效应。第一个块还必须有一个唯一的初始化向量（IV）。

[AES-GCM](https://datatracker.ietf.org/doc/html/rfc5288#:~:text=Abstract%20This%20memo%20describes%20the,Hellman%2Dbased%20key%20exchange%20mechanisms.)（伽罗瓦/计数器模式）是当今Android和大多数安全系统上现代、以完整性为中心且推荐的对称加密模式。它通过递增计数器并将结果与明文进行异或运算来工作。GCM是一种[带有关联数据的认证加密（AEAD）](https://developers.google.com/tink/aead)模式，这意味着它可以在一个高效的步骤中同时提供机密性和完整性。

至关重要的是，要确保对称密钥没有硬编码或存储在不安全的位置（如SharedPreferences）。相反，应使用Android密钥库系统，它以隔离且不可导出的方式存储密钥，并使用带有正确转换字符串（如`AES/GCM/NoPadding`）的Cipher类。

另一方面，非对称加密（公钥加密）对于[移动应用程序上的大量数据](https://thenewstack.io/how-time-plays-a-crucial-role-in-aggregating-mobile-data/)来说太慢。它主要用于以混合方式补充对称加密，以安全地交换AES对称密钥，并支持数字签名以进行认证和数据完整性。[RSA（Rivest-Shamir-Adleman）](https://www.geeksforgeeks.org/computer-networks/rsa-algorithm-cryptography/)依赖于大素数分解的难度。它使用公钥进行加密，私钥进行解密。

对于公钥加密，考虑使用[RSA/OAEP（最优非对称加密填充](https://www.cs.rit.edu/~spr/COURSES/CRYPTO/oaep.pdf)）或[ECC（椭圆曲线密码学）](https://blog.cloudflare.com/a-relatively-easy-to-understand-primer-on-elliptic-curve-cryptography/)，而不是RSA/ECB/PKCS1，因为后者缺乏现代密码学保证。RSA/ECB/PKCS1中使用的填充方案（PKCS1）是漏洞的主要原因，因为它已过时，缺乏现代安全证明，并且容易受到选择密文攻击。OAEP填充通过添加随机性和使用哈希函数消除了这些漏洞。

出于签名或证书目的，考虑转向更强的算法，例如带有SHA-256的RSA或[ECDSA（椭圆曲线数字签名算法）](https://www.cs.miami.edu/home/burt/learning/Csc609.142/ecdsa-cert.pdf)。在Android安全和其他资源受限的环境中，ECDSA备受青睐，因为它可以生成更小、处理速度更快的密钥，这对于TLS/SSL通信非常重要。

此外，为了保护证书并在应用程序与服务器之间通过TLS/SSL通信时建立信任，请考虑证书固定（certificate pinning）。它通过确保应用程序只信任特定的预设证书或公钥来增加一层安全，这是对抗中间人（MITM）攻击的关键防御措施。

## **结论**

迁移到现代密码学应该是一个金丝雀发布过程，涉及对遗留算法使用情况的清晰审计、风险分类、兼容性迁移，最后是密集的测试和验证。所有这些过程还应包括对项目蓝图的清晰文档，以供未来开发。