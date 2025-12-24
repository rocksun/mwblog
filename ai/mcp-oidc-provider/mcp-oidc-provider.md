<!--
title: Tigris对象存储正式开源MCP OIDC身份提供商
cover: https://www.tigrisdata.com/blog/assets/images/mcp-oid-8c0a6ed2ecb4c261895605373b7e58b6.webp
summary: mcp-oidc-provider是专为MCP服务器设计的OIDC提供商，简化认证授权，连接客户端与上游IdP，支持OAuth/OIDC发现，且与供应商无关。
-->

mcp-oidc-provider是专为MCP服务器设计的OIDC提供商，简化认证授权，连接客户端与上游IdP，支持OAuth/OIDC发现，且与供应商无关。

> 译自：[We're open sourcing our MCP OIDC Provider | Tigris Object Storage](https://www.tigrisdata.com/blog/mcp-oidc-provider/)
> 
> 作者：Abdullah Ibrahim

**TLDR: 在构建远程 MCP 服务器时，你很可能需要在客户端（如 Claude、Cursor 等）和上游 IdP（如 Auth0、Clerk 等）之间添加一个 OIDC 层。我们为你创建了一个开箱即用的解决方案，它与供应商无关：你可以使用任何你想要的 IdP。**

MCP 服务器需要真实的身份验证和授权。必须颁发、刷新、验证令牌，并将其与上游身份关联。客户端需要登录、获取凭据，并安全地调用你的 MCP 服务器。这很复杂，尤其如果你不是一名安全工程师。你不应该自己实现认证，但如果现有工具无法开箱即用，你该怎么办？

实现[远程托管的 MCP 服务器](https://support.claude.com/en/articles/11503834-building-custom-connectors-via-remote-mcp-servers)需要实现[MCP 授权协议](https://modelcontextprotocol.io/specification/draft/basic/authorization)，该协议基于 OAuth 2.1 (DRAFT)。理论上，这应该很简单，因为现代应用程序要么自己实现 OAuth 规范，要么使用符合 OAuth 标准的 IdP，如 Auth0 或 Clerk。我至少是这样认为的，但当我开始实现时，却遇到了重大问题。

这就是为什么我们构建并开源了 [mcp-oidc-provider](https://github.com/tigrisdata/mcp-oidc-provider)：一个专门为 MCP 工作流设计的、极简的、生产就绪的 OIDC provider。

## MCP 协议需要发现 (OAuth 或 OIDC)[​](#mcp-protocol-requires-discovery-oauth-or-oidc "直接链接到 MCP 协议需要发现 (OAuth 或 OIDC)")

MCP 规范 ([2025-11-25](https://modelcontextprotocol.io/specification/2025-11-25/basic/authorization#protected-resource-metadata-discovery-requirements)) 明确要求使用 OAuth。根据规范：

* 受保护的 MCP 服务器作为 OAuth 2.1 资源服务器，能够接受并使用访问令牌响应受保护的资源请求。
* MCP 客户端作为 OAuth 2.1 客户端，代表资源所有者发出受保护的资源请求。

对于发现机制，MCP 授权服务器（本软件包用于此目的）必须提供至少一种发现机制：

* OAuth 2.0 授权服务器元数据 ([RFC8414](https://datatracker.ietf.org/doc/html/rfc8414))
* OpenID Connect Discovery 1.0

OpenID Connect Discovery (OIDC) 在技术上是可选的，但你需要一个身份层来充分保护你的 MCP 服务器。OAuth 提供了一种方式，让客户端可以请求你的 MCP 授权服务器去获取资源所有者的授权。它不验证客户端的身份。OIDC 为你处理身份部分。

如果没有 OIDC，你必须为每个提供商构建自定义集成来验证身份。你需要实现自己的令牌刷新逻辑，包括 `offline_access` 支持。像 `mcp://cursor/auth` 或 `claude://oauth/callback` 这样的重定向 URI 会被标准 IdP 拒绝，因为它们不是网络 URL，并且需要明确的 OIDC 支持。而且你的 MCP 服务器无法与 Claude 和 Cursor 等桌面客户端配合使用。

直接使用 OIDC 吧。它简单得多。

### 你需要 OAuth 和 OIDC 两者[​](#you-need-both-oauth-and-oidc "直接链接到你需要 OAuth 和 OIDC 两者")

在这个软件包中，我同时实现了 OAuth 和 OIDC 发现端点，原因是什么？MCP 客户端必须支持尝试两种发现机制，但并非所有客户端都符合规范。因此，例如，如果它们只实现了 OpenID Connect Discovery 1.0 进行发现，`mcp-oidc-provider` 仍然会工作。

我们众所周知的 [OIDC 端点](https://mcp.storage.dev/.well-known/openid-configuration)是 OpenID 开箱即用的。为了最大程度的兼容性，我们实现了 OAuth 端点：

## 动态客户端注册：仅靠上游 IdP 无法解决此问题[​](#dynamic-client-registration-upstream-idps-alone-dont-solve-this "直接链接到动态客户端注册：仅靠上游 IdP 无法解决此问题")

根据 MCP 规范：“授权服务器和 MCP 客户端**应**支持 OAuth 2.0 动态客户端注册协议 ([RFC7591](https://datatracker.ietf.org/doc/html/rfc7591))。” 表面上看，这似乎应该让支持动态客户端注册的 IdP 对大多数 MCP 客户端都有效。

在第一次迭代中使用 Auth0 时，我们启用了动态客户端注册。它在技术上无需任何中间件即可授权 MCP 客户端，但每个临时客户端都显示在长期存在的第三方应用程序列表中。因此，对于每个用户，每个会话我们都有一个第三方应用程序。正如你所想象的，我们点击那个列表点得手都疼了。而且，为每个客户端颁发有范围的访问令牌也很痛苦。

![一堆动态创建的 OAuth 客户端淹没了静态定义的客户端](https://www.tigrisdata.com/blog/assets/images/oauth-clients-1f309154bab0cc028818e1d876ddb0e7.webp)

我们需要列表中只有一个第三方应用程序，一个小的 OIDC 提供商，能够控制所有 MCP 客户端的访问。以免我们的眼睛被仪表板的臃肿所伤害。

## 介绍 mcp-oidc-provider

一个极简的、有主见的 OIDC provider，专为 MCP 服务器构建，你可以与任何兼容 OIDC 的 IdP 一起使用。

使用它，你将获得规范中明确要求的功能：

* 受保护的 MCP 服务器作为 OAuth 2.1 资源服务器，能够接受并使用访问令牌响应受保护的资源请求。
* 客户端作为 OAuth 2.1 客户端，代表资源所有者发出受保护的资源请求。

此外，我们将会话、令牌、授权和 OIDC 适配器数据存储在一个键值存储中。你可以像我们一样使用 Tigris 作为你的 KV 存储，或者使用 [Keyv](https://github.com/jaredwray/keyv/) 支持的任何其他存储，如 Redis 或 Postgres。

![alt text](https://res.cloudinary.com/dkrpg71cx/image/upload/v1766030444/g6qfasopkxfpqzrbqkvl.png)

### 用法：参考独立实现[​](#usage-referencing-the-standalone-implementation "直接链接到用法：参考独立实现")

最好的起点是[独立 OIDC provider](https://github.com/tigrisdata/mcp-oidc-provider/tree/main/example/standalone-oidc)。如果你已在 Express 以外的不同技术栈中实现了 MCP，或者想将认证作为可独立扩展的独立微服务运行，请使用它。你可以让你的 MCP 服务器使用 NextJS 或其他框架，然后独立运行此服务器，并将认证请求代理到此服务器。

独立 provider 包含：

* 引导服务器代码
* provider 配置
* 上游 IdP 连接
* 路由设置
* 存储适配器示例
* 完整的 OIDC 端点注册

此外，你可以选择使用 Tigris 作为你的键值存储。

克隆仓库并使用 `npm install` 安装依赖后，设置你的环境：

```
cat .env  
# configure your upstream IdP  
UPSTREAM_ISSUER=https://YOUR_DOMAIN.auth0.com  
UPSTREAM_CLIENT_ID=...  
UPSTREAM_CLIENT_SECRET=...  
UPSTREAM_REDIRECT_URI=http://localhost:3000/callback  
  
#configure your own provider issuer  
OIDC_ISSUER=http://localhost:4000  
OIDC_PORT=4000  
  
# Tigris (for @tigrisdata/keyv-tigris)  
TIGRIS_STORAGE_ACCESS_KEY_ID=tid_xxxxx  
TIGRIS_STORAGE_SECRET_ACCESS_KEY=tsec_yyyyy  
TIGRIS_STORAGE_BUCKET=my-kv-bucket  

```

MCP 客户端将获取 `[http://localhost:4000/.well-known/openid-configuration](http://localhost:4000/.well-known/openid-configuration)` 来发现 OAuth 流程所需的端点。

你使用 `npm start` 运行 provider。你可以将其与你的 MCP 服务器一起运行，认证请求将代理到它。

将你的客户端指向你的 OIDC issuer。例如，Claude Desktop 期望：

```
{  
  "auth": {  
    "issuer": "http://localhost:4000"  
  }  
}  

```

当你的 MCP 服务器收到请求时，你使用 JWKS 验证令牌：

```
import { createRemoteJWKSet, jwtVerify } from "jose";  
  
const jwks = createRemoteJWKSet(new URL("http://localhost:4000/jwks"));  
  
const { payload } = await jwtVerify(accessToken, jwks);  
  
console.log("User:", payload.sub);  

```

就是这样。你拥有了一个功能齐全的基于 OIDC 的 MCP 认证流程。

### 用法：集成模式 (Express + MCP)[​](#usage-integrated-mode-express--mcp "直接链接到用法：集成模式 (Express + MCP)")

如果你使用 Node / Express 构建 MCP 服务器，这是最简单的入门方式。在集成模式下，你运行一个 Express 应用程序，它将：

* 托管 OIDC provider (/.well-known/openid-configuration, /authorize, /token, /jwks, /register)
* 托管你的 MCP 端点
* 端到端处理所有 OAuth + OIDC 流程
* 暴露一个单一的 BASE\_URL，你的 MCP 客户端将指向它

首先，安装你的依赖项：

```
npm install mcp-oidc-provider keyv openid-client express  

```

如果你使用 TS，你可能还需要 `typescript`、`ts-node` 等，但那是标准配置。

其次，一次性生成你的 JWKS 签名密钥。你将它们保存到 `.env` 文件中。

```
npx mcp-oidc-provider --pretty  

```

复制打印出的 JSON 并将其存储在一个安全位置（例如密钥管理器），然后通过 JWKS 环境变量注入。

对于开发环境，你可以跳过此步骤（密钥会自动生成，但令牌在重启后，令牌缓存过期后会失效）。

第三，配置你的环境：

```
cat .env  
BASE_URL=http://localhost:3000          # Where this combined server runs  
OIDC_CLIENT_ID=your-idp-client-id  
OIDC_CLIENT_SECRET=your-idp-client-secret  
SESSION_SECRET=some-long-random-string  
JWKS=...                                # JSON from `npx mcp-oidc-provider --pretty` (prod only)  

```

BASE\_URL 必须是客户端将用于以下目的的公共 URL：

* OIDC 发现 (/.well-known/openid-configuration)
* OAuth 回调 (/oauth/callback)
* MCP 端点（你在此服务器下选择的任何路由）

现在，你可以通过使用 `setupMcpExpress()` 函数将 OIDC provider 添加到你的服务器。它将：

* 将 OIDC provider 路由挂载到 Express 应用程序
* 连接 MCP 认证（Bearer 认证 + 令牌验证）
* 返回：
  + app：配置好的 Express 实例
  + `handleMcpRequest(handler)`：一个帮助函数，用于注册你的 MCP 请求处理器，其中认证 + 用户已解析

以下是如何使用它的示例：

```
import express from "express";  
import { Keyv } from "keyv";  
import { setupMcpExpress } from "mcp-oidc-provider/mcp";  
import { OidcClient } from "mcp-oidc-provider/oidc";  
import type { JWKS } from "mcp-oidc-provider";  
  
async function main() {  
    
  const jwks: JWKS | undefined = process.env.JWKS  
    ? JSON.parse(process.env.JWKS)  
    : undefined;  
  
  if (!process.env.BASE_URL) {  
    throw new Error("BASE_URL is required");  
  }  
  if (!process.env.OIDC_CLIENT_ID || !process.env.OIDC_CLIENT_SECRET) {  
    throw new Error("OIDC_CLIENT_ID and OIDC_CLIENT_SECRET are required");  
  }  
  if (!process.env.SESSION_SECRET) {  
    throw new Error("SESSION_SECRET is required");  
  }  
  
    
  const idpClient = new OidcClient({  
    issuer: "https://your-tenant.auth0.com",   
    clientId: process.env.OIDC_CLIENT_ID,  
    clientSecret: process.env.OIDC_CLIENT_SECRET,  
    redirectUri: `${process.env.BASE_URL}/oauth/callback`,  
      
  });  
  
    
  const store = new Keyv();   
  
    
    
    
    
  const { app, handleMcpRequest } = setupMcpExpress({  
    idpClient,  
    store,  
    baseUrl: process.env.BASE_URL,  
    secret: process.env.SESSION_SECRET,  
    jwks,  
  });  
  
    
    
  handleMcpRequest(async (req, res) => {  
    console.log("Authenticated user:", req.user);  
  
      
      
      
  
      
    res.json({  
      jsonrpc: "2.0",  
      id: req.body?.id ?? null,  
      result: {  
        message: "Hello from integrated MCP + OIDC server!",  
        user: req.user,  
      },  
    });  
  });  
  
  const port = Number(process.env.PORT ?? 3000);  
  app.listen(port, () => {  
    console.log(`MCP + OIDC server listening on ${port}`);  
    console.log(`Base URL: ${process.env.BASE_URL}`);  
  });  
}  
  
main().catch((err) => {  
  console.error(err);  
  process.exit(1);  
});  

```

最后，你可以将客户端指向你的 MCP 服务器。例如，Claude Desktop 期望：

```
{  
  "auth": {  
    "issuer": "http://localhost:4000"  
  }  
}  

```

实际的配置形式取决于客户端，但模式是：

* Issuer = 此服务器的 BASE\_URL
* MCP endpoint = 你的集成服务器暴露的任何 MCP 路由（由 handleMcpRequest 连接的那个）

配置完成后：

* 客户端访问你的服务器上的 `/.well-known/openid-configuration`。
* 它对你的服务器执行 `/.authorize` → `/token` 流程。
* 你的服务器通过 OidcClient 将登录联邦到上游 IdP。
* 你的服务器颁发 MCP 特定令牌并验证 `/mcp` 请求。
* 你的处理器接收已填充 `req.user` 的已认证请求。

就是这样。你的服务器现在是一个集成的 OIDC issuer、令牌端点和 MCP 端点。

## 在生产环境中使用 mcp-oidc-provider[​](#using-the-mcp-oidc-provider-in-production "直接链接到在生产环境中使用 mcp-oidc-provider")

我们将其用于我们托管的 MCP 服务器，并且我们足够信任它，因此将其提供给你。它使用标准库进行身份验证和授权。而且，它不会将你锁定到任何供应商。

我们已尽可能地将 mcp-oidc-provider 泛化，包括添加额外的配置来增强你的 IdP 所提供的功能。例如，我们允许你配置 JWKS 缓存设置，以防你的 IdP 不提供 `Cache-Control: max-age` 头。如果你的公司对密钥轮换事件有安全要求，需要密钥在一定时间后过期，这将很有帮助。

如果你正在使用 `jose.createRemoteJWKSet`，你通常通过在创建 JWKS fetcher 时传递选项来控制过期：

```
import { createRemoteJWKSet } from "jose";  
  
const jwksUri = new URL("https://your-issuer/.well-known/jwks.json");  
  
const jwks = createRemoteJWKSet(jwksUri, {  
    
  cooldownDuration: 30_000,  
    
  cacheMaxAge: 600_000,  
});  

```

如果你需要任何其他定制，请联系我们！我们非常乐意让 mcp-oidc-provider 适配你的 MCP 服务器。

# 尝试 mcp-oidc-provider

准备好构建一个安全的 MCP 服务器了吗？立即开始使用 mcp-oidc-provider，并使用你想要的任何兼容 OIDC 的 IdP。