
<!--
title: OpenVPN还是WireGuard？详细性能对比
cover: https://cdn.thenewstack.io/media/2024/11/0b44e284-dayne-topkin-u5zt-hoocrm-unsplash-scaled.jpg
-->

OpenVPN虽然可靠，但在性能和复杂性方面不及WireGuard。

> 译自 [OpenVPN or WireGuard? A Detailed Performance Breakdown](https://thenewstack.io/openvpn-or-wireguard-a-detailed-performance-breakdown/)，作者 Edward Viaene。

OpenVPN 自 2001 年发布以来一直是 VPN 领域的主导者。凭借 23 年的历史，OpenVPN 已证明是一种可靠且安全的协议。然而，它也有一些缺点，尤其是在性能和易用性方面。

OpenVPN 使用 SSL/TLS 加密在两个端点之间创建安全隧道。虽然强大，但该协议很复杂，需要大量资源才能有效运行。设置和管理 OpenVPN 可能很麻烦，尤其是对于需要处理多个环境和配置的 [DevOps](https://thenewstack.io/devops/) 团队而言。OpenVPN 服务器因 TLS 证书过期而停止工作的情况屡见不鲜。

另一方面，WireGuard 是近年来出现的新秀。WireGuard 与 OpenVPN 的不同之处在于它的简洁性和效率。OpenVPN 依赖于较旧、更复杂的加密算法，而 WireGuard 使用更快速、更安全的现代加密技术。

与 OpenVPN 不同，WireGuard 直接集成到 Linux 内核中，这意味着它在较低级别运行，开销更少。这带来了更快的连接时间和更低的资源使用率。WireGuard 的一大优势是其最小的代码库——大约是 OpenVPN 的 10%——这减少了攻击面，并使其更容易维护和审计安全漏洞。

WireGuard 的美妙之处在于它的简洁性。WireGuard 使用简单的密钥对交换，而不是管理复杂的证书，这大大减少了管理负担。这使其成为需要轻量级、易于配置的 VPN 解决方案的 DevOps 专业人员的绝佳选择。

## OpenVPN 和 WireGuard 的优缺点

1. **性能：**

*   OpenVPN：以稳定性著称，但由于 SSL/TLS 加密的开销，速度可能较慢。
*   WireGuard：速度更快，这得益于其内核级集成和高效的加密算法，连接时间更短，CPU 使用率更低。

2. **复杂性：**

*   OpenVPN 的配置更复杂，尤其是在集成 OIDC 或 SAML 等现代身份验证协议时。它需要手动管理证书。
*   WireGuard：简单轻便。无需复杂的证书管理。使用密钥对身份验证来确保连接安全。

3. **安全性：**

*   OpenVPN：仍然安全且定期更新，但其庞大的代码库意味着存在更多潜在漏洞。
*   WireGuard：代码库更小，更易于审计和维护。它使用现代加密算法，降低了漏洞风险。

4. **用例：**

*   OpenVPN：适用于需要与各种设备兼容的旧系统或环境。
*   WireGuard：非常适合现代 DevOps 环境，提供简洁性、速度和易用性。

## 演示：基于 WireGuard 构建的专有 VPN 服务器产品

在最近的[“云与 DevOps 播客”节目](https://youtu.be/uWVpYP8FeUE)中，我们演示了基于 WireGuard 构建的专有 VPN 服务器产品，旨在解决他们在使用 OpenVPN 时遇到的一些限制。让我们看看演示以及该产品如何解决常见的 VPN 挑战。专有 VPN 服务器的主要功能：

1. **OIDC 集成：**

与需要手动管理证书的传统 VPN 设置不同，此 VPN 产品[与 Azure AD、OneLogin 和 Okta 等现代身份提供商集成](https://thenewstack.io/essentials-for-integrating-identity/)，通过 OIDC 实现。这使得管理用户访问变得更加容易，无需处理证书的复杂性。

2. **用户管理：**

通过与身份提供商的集成，VPN 服务器可以实现无缝的用户 onboarding 和 offboarding。用户可以在通过 OIDC 身份验证后直接下载其 VPN 配置文件，管理员可以在必要时轻松暂停或撤销访问权限。

3. **TLS 集成：**

管理界面的一项功能是与 Let’s Encrypt 自动集成以获取 TLS 证书。这意味着 VPN 服务器可以生成和管理 HTTPS 证书，而无需手动干预，从而更容易维护安全的设置。

4. **轻量级和高效：**

该产品可在小型实例上运行，例如内存最小的 ARM64 机器。这使其成为寻求节省云[基础设施成本而不牺牲性能](https://thenewstack.io/improving-price-performance-lowers-infrastructure-costs/)的公司的理想解决方案。

5. **快速连接时间：**

该演示最令人印象深刻的方面之一是快速连接时间。与 OpenVPN 连接可能需要几秒钟才能建立不同，基于 WireGuard 的服务器几乎可以立即连接。这种速度极大地有利于经常在不同环境之间切换的 DevOps 团队。

## 产品现场演示

[在演示期间](https://youtu.be/HDXKMhIYaiI)，我们逐步讲解了如何在最小实例上设置 VPN 服务器、启动必要的服务以及通过 WireGuard 连接客户端。

1. **启动服务：**

主机首先启动了管理 WireGuard VPN 接口的 root 服务，然后启动了处理用户身份验证的 REST API。他们指出了以非 root 用户身份运行服务以增强安全性的好处。

2. **生成密钥和配置：**

用户可以通过 OIDC 进行身份验证并在 VPN 服务器运行时下载其 VPN 配置文件。客户端的私钥是动态生成的，并在下载配置后删除，确保服务器上不存储敏感数据。

3. **连接客户端：**

身份验证后，主机使用官方 WireGuard 应用程序连接了客户端。即使来自不同的地理位置，连接也几乎立即建立，延迟极低。

4. **安全注意事项：**

一个值得注意的功能是服务器不存储私钥，这增加了一个额外的安全层。此外，可以通过在身份提供程序中暂停或删除用户的帐户来[实时撤销用户访问权限](https://thenewstack.io/change-data-capture-for-real-time-access-to-backend-databases/)。


## 赢家？

OpenVPN 和 WireGuard 都是可行的 VPN 解决方案，但 WireGuard 作为现代 DevOps 环境的卓越选择脱颖而出。它的简洁性、速度和安全性使其成为希望简化 VPN 设置而不牺牲性能的团队的绝佳选择。正如播客中演示的那样，我们基于 WireGuard 构建的专有 VPN 服务器产品展示了现代 VPN 解决方案如何能够极大地简化用户管理和改进连接时间，同时保持强大的安全标准。

对于希望减少开销并提高性能的 DevOps 团队来说，WireGuard（以及基于它的产品）为 OpenVPN 等传统 VPN 解决方案提供了一个强大的替代方案。
