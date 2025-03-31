Jumpserver 是由 Fit2Cloud 开发的一款开源的特权访问管理 (PAM) 工具。它在中国被广泛使用，并提供了一套全面的功能，包括 SSH、RDP、数据库和 FTP 隧道，使用户友好的 Web 界面。它作为内部网络的堡垒机，为访问内部主机提供了一个集中访问和控制点。但是，如果这个网关本身被攻破了会发生什么？

在 SonarSource，我们致力于帮助开发人员编写安全的代码。我们的漏洞研究团队积极分析开源软件，识别并报告漏洞，以提高生态系统的安全性。在这篇博文中，我们将深入研究 Jumpserver 的安全性，并探讨可能允许攻击者绕过身份验证并完全控制 Jumpserver 基础设施的关键漏洞。

在这些博客文章中讨论的一些发现最初是在去年的 Insomni'hack 上提出的。演讲 [Diving Into JumpServer: The Public Key Unlocking Your Whole Network](https://www.youtube.com/watch?v=uoGNq804-jw) 的录像可在 YouTube 上观看。

## 影响

JumpServer 的集中式特性使其成为关键的安全资产。如果被攻破，攻击者可以访问整个内部网络。结合我们的发现，未经身份验证的攻击者可以绕过身份验证，并完全控制 JumpServer 系统及其底层基础设施。

这些漏洞已在 JumpServer 3.10.12、4.0.0 版本中**完全解决**，并被追踪为 [CVE-2023-43650](https://github.com/jumpserver/jumpserver/security/advisories/GHSA-mwx4-8fwc-2xvw), [CVE-2023-43651](https://github.com/jumpserver/jumpserver/security/advisories/GHSA-4r5x-x283-wm96), [CVE-2023-43652](https://github.com/jumpserver/jumpserver/security/advisories/GHSA-fr8h-xh5x-r8g9), [CVE-2023-42818](https://github.com/jumpserver/jumpserver/security/advisories/GHSA-97hj-xpgc-9ccw), [CVE-2023-46123](https://github.com/jumpserver/jumpserver/security/advisories/GHSA-hvw4-766m-p89f), [CVE-2024-29201](https://github.com/jumpserver/jumpserver/security/advisories/GHSA-pjpp-cm9x-6rwj), [CVE-2024-29202](https://github.com/jumpserver/jumpserver/security/advisories/GHSA-2vvr-vmvx-73ch), [CVE-2024-40628](https://github.com/jumpserver/jumpserver/security/advisories/GHSA-rpf7-g4xh-84v9), [CVE-2024-40629](https://github.com/jumpserver/jumpserver/security/advisories/GHSA-3wgp-q8m7-v33v)。

在本文中，我们将重点关注身份验证绕过漏洞（CVE-2023-43650、CVE-2023-43652、CVE-2023-42818、CVE-2023-46123），这些漏洞允许攻击者冒充用户，并为利用后续漏洞铺平道路，这些漏洞将在下一篇博文中介绍。

## 技术细节

### 背景

JumpServer 为用户提供了一个集中且用户友好的 Web 界面，用于访问内部网络中的各种资源。这种简化的方法简化了访问管理并增强了整体用户体验。

![](https://assets-eu-01.kc-usercontent.com:443/8c150fae-fba4-0115-ef12-b10a8a4e2715/916fe268-2655-44dd-966d-b09a913bbbf2/id_shell_example.png?w=1268&h=735&auto=format&fit=crop)

对于那些喜欢更传统方法的人，JumpServer 还支持通过 SSH 客户端直接访问。这种灵活性满足了不同的用户偏好和现有工作流程。

![](https://assets-eu-01.kc-usercontent.com:443/8c150fae-fba4-0115-ef12-b10a8a4e2715/c1eb88cc-3b99-4c65-9bcb-f5b0f8f5fb4f/jumpserver_ssh_ui.png?w=1026&h=491&auto=format&fit=crop)

但在深入研究我们的发现的细节之前，首先了解 JumpServer 的底层架构至关重要。这些知识将为理解如何利用这些缺陷来破坏系统并获得对敏感资源的未经授权的访问提供必要的背景信息。

#### 架构

JumpServer 的核心是建立在微服务架构之上的。这意味着它由几个独立的组件组成，这些组件协同工作以提供其功能。这些组件中的每一个本质上都是一个 Docker 容器。以下是本博客系列中将相关的关键组件的细分：

![](https://assets-eu-01.kc-usercontent.com:443/8c150fae-fba4-0115-ef12-b10a8a4e2715/5c67728c-cb47-4379-8e59-4ba86fc7c4f4/general_arch_jumpserver.png?w=1999&h=921&auto=format&fit=crop)
**核心（主 API）：** 使用 Python-Django 编写，它充当中央 API，负责调度任务、身份验证、授权等。这个关键组件直接与数据库微服务交互，以验证用户凭据并管理访问权限。

**数据库：** 存储敏感信息的关键组件，包括用户凭据和网络中各种主机的凭据。这使其成为攻击者的主要目标，因为攻陷数据库可能会授予他们广泛的访问和控制权限。

**Koko：** 使用 Go 开发，此微服务处理核心隧道功能，从 Web 终端和 FTP 文件资源管理器到 SSH 隧道，提供与内部主机的直接 SSH 连接。

**Celery：** 以流行的 Python 库命名，它充当 JumpServer 的任务管理器。Celery 处理用于重复任务（如连接测试）的“任务队列”，并维护主机上自定义作业的“作业调度”。

**Web 代理：** 最后，Web 代理是基于 Web 的连接的入口点，将请求转发到核心 API。

为了从外部攻击者的角度评估潜在的漏洞，我们将首先检查 Koko 和 Web API，因为这些组件暴露于外部威胁。

#### 身份验证

JumpServer 提供灵活的身份验证选项，允许用户通过 Web UI (HTTP) 或 SSH 客户端进行身份验证：

**Web UI** 采用传统的身份验证流程。当用户尝试登录时，提供的凭据会根据数据库进行验证。如果凭据有效，则会生成会话令牌并发送给用户，从而授予对系统的访问权限。

![](https://assets-eu-01.kc-usercontent.com:443/8c150fae-fba4-0115-ef12-b10a8a4e2715/3a1a741b-67c0-472e-ae96-7c29226ce5df/http_login_flow.png?w=1999&h=323&auto=format&fit=crop)

**SSH 身份验证** 提出了一个独特的挑战，因为传统的会话令牌不容易在此上下文中应用。JumpServer 通过自定义实现来解决此问题。

当用户使用 SSH 客户端连接时，Koko 容器管理与客户端的通信。它本质上充当一个中介，获取用户的密码凭据并通过核心 API 执行身份验证过程，从而镜像 Web UI 的身份验证流程。

身份验证成功后，Koko 容器存储生成的会话令牌，并将其与用户的 SSH 通道相关联，这允许容器有效地管理和跟踪 SSH 用户的会话。

![](https://assets-eu-01.kc-usercontent.com:443/8c150fae-fba4-0115-ef12-b10a8a4e2715/5b3dee29-cb20-4f7f-863f-c9a90f122452/Koko_login_example_flow.png?w=1999&h=323&auto=format&fit=crop)

但是，SSH 身份验证可以通过[非对称密钥](https://en.wikipedia.org/wiki/Public-key_cryptography)执行；它甚至是推荐的方法。Koko 如何处理这种类型的身份验证？

首先，通过接收来自用户的公钥，然后从核心 API 获取会话密钥。在 Koko 收到令牌后，它知道存在具有此类公钥的用户，并继续直接与用户执行密钥验证。

![](https://assets-eu-01.kc-usercontent.com:443/8c150fae-fba4-0115-ef12-b10a8a4e2715/8f8b9f01-9dce-4c5b-a3e2-5fe9843bc626/login_ssh_key_koko_flow.png?w=1999&h=609&auto=format&fit=crop)

### 身份验证绕过 (CVE-2023-43652)

您可能已经注意到此机制中的一个危险信号，核心 API 仅通过提供公钥向 Koko 提供有效的会话令牌。

考虑到 JumpServer 的微服务架构，我们知道还有另一种访问核心 API 的方法，那就是通过 nginx HTTP 接口。查看代码时，当 JumpServer 尝试使用公钥[验证](https://github.com/jumpserver/jumpserver/blob/7c67d882aa884da6ea268427e5999db2560aa296/apps/authentication/backends/pubkey.py#L18)用户身份时，无法验证请求是否来自 Koko 服务：

```
def authenticate(self, request, username=None, public_key=None, **kwargs):
    if not public_key:
        return None
    if username is None:
        username = kwargs.get(UserModel.USERNAME_FIELD)
    try:
        user = UserModel._default_manager.get_by_natural_key(username)
    except UserModel.DoesNotExist:
        return None
    else:
        if user.check_public_key(public_key) and \
           self.user_can_authenticate(user):
            return user
```

攻击者可以使用 HTTP 接口直接执行相同的请求，本质上是在不需要任何密钥验证的情况下模拟 Koko 容器。

![](https://assets-eu-01.kc-usercontent.com:443/8c150fae-fba4-0115-ef12-b10a8a4e2715/9a129612-2fb4-43d2-96e8-7e9b09212d34/login_bypassing_koko_flow.png?w=1999&h=701&auto=format&fit=crop)

获取用户的公钥并不是一项复杂的任务；顾名思义，它们是公开的。出于演示目的，您可以转到任何 GitHub 用户个人资料，只需将 `.keys` 添加到 URL，即可查看他们的公钥。
### MFA 绕过 (CVE-2023-46123)，或第二步

试图利用公钥认证绕过的攻击者，如果受害者账户启用了[多因素认证](https://en.wikipedia.org/wiki/Multi-factor_authentication) (MFA)，可能会面临另一个障碍。

![](https://assets-eu-01.kc-usercontent.com:443/8c150fae-fba4-0115-ef12-b10a8a4e2715/51c0031b-9ef7-4475-a053-a3a437e77912/mfa_ui.png?w=948&h=680&auto=format&fit=crop)

与身份验证类似，在 SSH 上下文中实现这样的功能不如在 Web 上那么明显。那么，它在 Jumpsever 内部是如何工作的呢？
在 SSH 协议中，服务器维护一个支持的身份验证方法列表，例如 `public key`, `password`, `host-based`, 和 `keyboard-interactive`。当客户端尝试连接时，服务器会共享此列表，客户端必须选择一种可用的方法进行身份验证。身份验证成功后，会发送“`SUCCESS`”消息，启动 SSH 会话。

为了实现 MFA，SSH 协议还支持“`partial success`”消息，告诉用户虽然身份验证正确，但还需要一个额外的步骤。在这里，它可以更改为“`keyboard-interactive`”类型，以允许客户端输入 MFA 代码。

如前所述，Jumpserver 隧道 SSH 会话，需要实现某些功能才能支持 MFA。成功的双因素身份验证如下所示：

![](https://assets-eu-01.kc-usercontent.com:443/8c150fae-fba4-0115-ef12-b10a8a4e2715/5c012d58-47e5-4256-8829-3d21b71120f7/mfa_flow.png?w=1612&h=1136&auto=format&fit=crop)

攻击者绕过基于 TOTP 的 MFA 的一种常见方法是暴力破解。如果应用程序未能实现预防机制，攻击者可以简单地尝试每个可能的 TOTP 代码，因为它只是一个 6 位数的字符串。但是尝试在 Jumpserver 中这样做会很快导致速率限制响应。
速率限制验证通常通过检查 IP 地址发出的请求数量来完成，但由于一切都集中在核心 API 中，Jumpserver 会将从 SSH 连接中获取的客户端 IP 作为 `/api/mfa` 请求中的额外参数转发：

```
POST /api/mfa
{
"code": "133337",
"remote_addr": "12.34.56.78"
}
```

与之前的漏洞类似，[没有验证](https://github.com/jumpserver/jumpserver/blob/72b215ed03e2475b83eb1b52bdeae9c72803356a/apps/authentication/mixins.py#L105)此请求是否来自 Koko 容器：

```python
def get_request_ip(self):
    ip = ''
    if hasattr(self.request, 'data'):
        ip = self.request.data.get('remote_addr', '')
    ip = ip or get_request_ip(self.request)
    return ip
```

攻击者可以直接通过 Web 代理调用核心 API，每次都更改 `remote_addr` 参数，从而绕过速率限制机制。这种速率限制绕过还允许攻击者通过不同的端点暴力破解密码本身。

此外，Sonar 还发现并披露了其他漏洞，例如密码重置时缺乏速率限制 ([CVE-2023-43650](https://github.com/jumpserver/jumpserver/security/advisories/GHSA-mwx4-8fwc-2xvw)) 以及使用公共 SSH 密钥和自定义客户端绕过 `partial success false` 响应 ([CVE-2023-42818](https://github.com/jumpserver/jumpserver/security/advisories/GHSA-97hj-xpgc-9ccw))。

### 补丁

此处讨论的漏洞已通过各种方式和版本修复：

- CVE-2023-43650:
  已在 2.28.20 和 3.7.1 版本中[修复](https://github.com/jumpserver/jumpserver/pull/11696/files)，通过添加 3 次尝试的速率限制
- CVE-2023-43652:
  已在 2.28.20 和 3.7.1 版本中[修复](https://github.com/jumpserver/jumpserver/pull/11706/files)，通过将公钥身份验证 API 与令牌生成分离，并且仅将其提供给 Koko 进行验证。
- CVE-2023-42818:
  已在 >= 3.7.2 版本中[修复](https://github.com/jumpserver/koko/pull/1231/files)，通过引入通过 `SSHAuthLogCallback` 代码进行部分成功的状态跟踪机制。如果没有 `CONTEXT_PARTIAL_SUCCESS_METHOD`，则第二个身份验证阶段将被拒绝。
- CVE-2023-46123:
  已在 >= 3.8.0 版本中[修复](https://github.com/jumpserver/jumpserver/pull/11812/files)，通过仅信任来自 Koko 的 `remote_addr` 参数（如果它使用签名）。

依赖 JumpServer 的组织应确保他们运行的是最新的已修补版本，这些版本已在 JumpServer 3.10.12 和 4.0.0 版本中得到完全解决。

## 时间线

日期 | 操作
---|---
2023-09-18 | 我们向 JumpServer 报告了我们的初步发现
2023-09-25 | Fit2Cloud 确认了这些问题
2023-09-27 | Fit2Cloud 发布了 2.28.20 和 3.7.1 版本，解决了 CVE-2023-43650 和 CVE-2023-43652
2023-10-05 | 我们发送了一份包含其他发现的后续报告
2023-10-05 | Fit2Cloud 确认了这些问题
2023-10-23 | Fit2Cloud 发布了 3.7.2 版本，解决了 CVE-2023-42818
2023-10-24 | Fit2Cloud 发布 3.8.0 版本，修复 CVE-2023-46123 漏洞 |

## 概要

在这篇博文中，我们将探讨主要源于架构错误的的安全缺陷。具体来说，我们将重点介绍与微服务隔离不足相关的风险，其中意外的跨服务交互可能导致重大的安全影响。这些漏洞突显了安全编码实践、全面测试、威胁建模和持续安全评估的重要性。通过了解这些漏洞的根本原因，开发人员可以学习构建更安全的系统，并防范类似的攻击。

我们要感谢 Fit2Cloud 在解决这些问题方面的积极响应以及他们对安全的承诺。我们还要感谢其他研究人员的贡献，特别是 [Ethan Yang](https://github.com/justlovediaodiao), [Hui Song](https://github.com/songofhawk), [pokerstarxy](https://github.com/pokerstarxy), [Lawliet](https://github.com/KiruaLawliet) 和 [Zhiniang Peng](https://x.com/edwardzpeng)，他们的发现为我们自己的发现铺平了道路。