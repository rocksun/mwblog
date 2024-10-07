
<!--
title: 面向API的AI：AI辅助SDK生成技术
cover: https://cdn.thenewstack.io/media/2024/10/7a96f473-alex-shuper-p-9g0uixuuq-unsplashb.jpg
-->

AI 在 SDK 生成中的一个关键优势是它能够处理日常任务。但最佳方案是混合模型，由开发人员牢牢掌控。

> 译自 [AI for APIs: Techniques for AI-Assisted SDK Generation](https://thenewstack.io/ai-for-apis-techniques-for-ai-assisted-sdk-generation/)，作者 Robert Kimani。

随着 GitHub Copilot 和 ChatGPT 等人工智能工具的兴起，AI 如何帮助开发者生成和使用 API SDK（软件开发工具包）引起了极大的兴趣。人工智能在简化重复编码任务方面的潜力为增强 API 工作流带来了激动人心的机会。但是，这种新方法也带来了显着的挑战，包括可靠性、安全性以及非确定性问题。

在本文中，我们将深入探讨 AI 在 SDK 生成中所扮演的助手角色，审查常见的陷阱（例如幻觉），并探究 AI 如何补充传统的代码生成方法，以提供平衡且高效的开发体验。

## 人工智能在 SDK 生成中的潜力 

API 是现代软件应用程序的支柱，使不同的系统能够相互通信。SDK 通过为开发人员提供预打包库和工具来简化 API 使用。传统上，SDK 生成一直是一个手动且耗时的过程。然而，人工智能的最新进展为自动化 SDK 创建开启了新的可能性。

人工智能在 SDK 生成中的一个主要优点是它能够处理单调、重复的任务。通过解析 OpenAPI 规范或 API 文档，人工智能可以自动创建模型、服务和其他构建 SDK 所需的组件。这减少了人工工作量，使开发人员能够专注于更复杂和富有创意的任务。

例如，APIMatic 等平台正在尝试使用人工智能来改善开发人员体验，方法是训练人工智能与传统的代码生成工具协同工作。在这种混合模型中，人工智能可以动态地回答开发人员查询并探索 API 文档，而确定性代码生成器则负责可靠地创建静态 API 访问代码。

## 示例：Spotify API 

以下 C# 代码演示了如何与 Spotify API 进行交互以创建新的播放列表、获取艺术家的热门曲目，并使用 Spotify Web API SDK 将这些曲目添加到创建的播放列表中。它是由 APIMatic 的 API 协作工具根据查询“如何创建新的播放列表并添加 10 首最流行的 Taylor Swift 歌曲？”生成的。

此代码处理以下完整工作流：

1. 通过 OAuth 2.0 验证必要权限，用于修改用户的歌单。
2. 使用 Spotify 的 API 为用户创建新歌单。
3. 获取 Taylor Swift 的热门歌曲。
4. 将获取到的歌曲添加到新创建的歌单中。

```csharp
using SpotifyWebAPI.Standard;
using SpotifyWebAPI.Standard.Authentication;
using SpotifyWebAPI.Standard.Controllers;
using SpotifyWebAPI.Standard.Exceptions;
using SpotifyWebAPI.Standard.Http.Response;
using SpotifyWebAPI.Standard.Models;
using System;
using System.Collections.Generic;
using System.Threading.Tasks;

namespace TestConsoleProject
{
    public class Program
    {
        public static async Task Main()
        {
            // Initialize the Spotify client with OAuth credentials
            SpotifyWebAPIClient client = new SpotifyWebAPIClient.Builder()
                .AuthorizationCodeAuth(
                    new AuthorizationCodeAuthModel.Builder(
                        "OAuthClientId",          // Your client ID
                        "OAuthClientSecret",      // Your client secret
                        "OAuthRedirectUri"        // Your redirect URI
                    )
                    .OAuthScopes(
                        new List<OAuthScopeEnum>
                        {
                            OAuthScopeEnum.PlaylistModifyPrivate,
                            OAuthScopeEnum.PlaylistModifyPublic,
                        })
                    .Build())
                .Environment(SpotifyWebAPI.Standard.Environment.Production)
                .Build();

            try
            {
                // Redirect user for OAuth authorization and obtain the token
                string authUrl = await client.AuthorizationCodeAuth.BuildAuthorizationUrl();
                string authorizationCode = "TODO: Replace Code";  // Replace with obtained authorization code
                OAuthToken token = client.AuthorizationCodeAuth.FetchToken(authorizationCode);

                // Rebuild the client with the OAuth token
                client = client.ToBuilder()
                    .AuthorizationCodeAuth(
                        client.AuthorizationCodeAuthModel.ToBuilder()
                            .OAuthToken(token)
                            .Build())
                    .Build();
            }
            catch (Exception e)
            {
                Console.WriteLine(e.Message);
            }

            // Create a new playlist
            PlaylistsController playlistsController = client.PlaylistsController;
            string userId = "smedjan";  // Replace with your Spotify user ID
            UsersPlaylistsRequest body = new UsersPlaylistsRequest
            {
                Name = "Taylor Swift Top 10",
                MPublic = false,
                Description = "Top 10 most popular songs by Taylor Swift",
            };

            ApiResponse<PlaylistObject> createPlaylistResult = null;
            try
            {
                createPlaylistResult = await playlistsController.CreatePlaylistAsync(userId, body);
            }
            catch (ApiException e)
            {
                Console.WriteLine(e.Message);
            }

            // Get Taylor Swift's top tracks
            ArtistsController artistsController = client.ArtistsController;
            string artistId = "06HL4z0CvFAxyc27GXpf02";  // Taylor Swift's Spotify artist ID
            string market = "US";
            ApiResponse<ManyTracks> topTracksResult = null;
            try
            {
                topTracksResult = await artistsController.GetAnArtistsTopTracksAsync(artistId, market);
            }
            catch (ApiException e)
            {
                Console.WriteLine(e.Message);
            }

            // Add top tracks to the new playlist
            if (createPlaylistResult != null && topTracksResult != null)
            {
                string playlistId = createPlaylistResult.Data.Id;
                List<string> trackUris = new List<string>();
                foreach (var track in topTracksResult.Data.Tracks)
                {
                    trackUris.Add(track.Uri);
                }

                string uris = string.Join(",", trackUris);
                try
                {
                    ApiResponse<PlaylistSnapshotId> addTracksResult = await playlistsController.AddTracksToPlaylistAsync(
                        playlistId,
                        null,
                        uris
                    );
                }
                catch (ApiException e)
                {
                    Console.WriteLine(e.Message);
                }
            }
        }
    }
}
```

下面是对代码的细分。

### 1. 授权设置

代码首先通过设置 OAuth 2.0 授权码流程来获取 Spotify API 访问权。它定义了 OAuth 客户端 ID、客户端密钥和重定向 URI，并请求管理播放列表所需的作用域： 

- PlaylistModifyPrivate：修改私有播放列表。 
- PlaylistModifyPublic：修改公开播放列表。

在用户同意后，客户端会通过将用户重定向到 Spotify 授权页面来获取 OAuth 令牌。此令牌随后用于验证 API 调用。

### 2. 创建一个新播放列表 

在授权之后，就会实例化一个 PlaylistsController 以与播放列表进行交互。使用 CreatePlaylistAsync 方法创建一个名称为“泰勒·斯威夫特排名前 10”的播放列表，其中包含隐私和描述的参数。

### 3. 获取 Taylor Swift 的热门单曲 

ArtistsController 用于获取 Taylor Swift 的热门单曲，方法是使用 GetAnArtistsTopTracksAsync 指定艺术家的 Spotify ID (06HL4z0CvFAxyc27GXpf02) 和市场（美国）。结果是热门单曲的列表，包括它们的 URI（Spotify 的唯一曲目标识符）。

### 4. 向歌单中添加曲目

代码将这些热门曲目添加到使用 AddTracksToPlaylistAsync 新创建的歌单中。它使用从歌单创建响应获取的 playlistId，向歌单发送一个曲目 URI 列表。

## 如何操作

1. OAuth 流程：提示用户登录 Spotify，然后应用检索授权代码，之后该代码会转换为 OAuth 令牌。
2. 创建播放列表：为经过身份验证的用户创建名为“泰勒·斯威夫特前 10 名”的私人播放列表。
3. 获取艺术家的热门曲目：代码从 Spotify 提取泰勒·斯威夫特的热门曲目，特别针对美国市场。
4. 将曲目添加到播放列表：使用 Spotify URI 将曲目添加到新创建的播放列表中。

## 其他注意事项 

- 异常处理：代码包括尝试捕获块以捕获 API 调用期间的异常（例如，如果授权失败或无法创建播放列表）。
- 用户授权：AuthorizationCodeAuth 模型用于安全访问，允许应用程序在明确同意后修改用户播放列表。

通过利用 API 副驾驶，这系列复杂的 API 交互被简化为结构化和可执行的格式。副驾驶确保正确地处理端点、身份验证流程和 API 参数，使开发人员更容易实现复杂的特性，如播放列表创建和歌曲管理，而无需手动编写每个细节。

## AI 生成的 SDK 的挑战

虽然这听起来很有希望，但基于 AI 的 SDK 生成远非完整的解决方案。尽管它有优势，但仍有一些关键挑战需要解决。

### 1. 非确定性和幻觉

非确定性是指 AI 模型无法对相同的输入始终如一地生成相同的输出。这对 SDK 生成来说尤其成问题，因为一致性是关键。如果由 AI 助手生成的 SDK 每次都略有不同，则可能会在将来导致重大的集成问题。开发人员需要相信生成的代码将是一致且可靠的——这是 AI 目前无法做到的。

一个相关的问题是“幻觉”，即 AI 生成语法正确的代码，但与底层逻辑或 API 文档不一致。例如，AI 可能会误解 API 端点或创建看似功能齐全但实际上完全不可用的函数。

这会导致令人沮丧的调试会话，开发人员必须筛选错误的 AI 生成的代码行以纠正幻觉或不一致。

### 2. 输入和输出限制

像 GPT-4 这样的大型语言模型 (LLM) 在严格的令牌限制内运行。这些限制限制了可以在一次运行中处理的输入量（例如，API 文档或 OpenAPI 规范）和输出量（例如，SDK 代码）。对于更大或更复杂的 API，这成为一个重大的瓶颈。由于 SDK 生成通常需要处理大型代码库，因此 AI 当前的令牌限制阻止它在一遍中生成完整的 SDK。

### 3. 安全问题

AI 模型是在大量现有代码上训练的，其中包括安全和不安全的示例。这使得它们容易生成容易受到常见安全威胁（如 SQL 注入、跨站点脚本 (XSS) 或路径遍历攻击）的代码。例如，一个看似无害的 AI 生成的函数可能存在隐藏的漏洞，例如允许未经授权的文件访问，如果未经适当审查。

现代 API 的复杂性通常涉及管理身份验证、速率限制和敏感数据，所有这些都需要安全处理。仅仅依靠 AI 来生成此类代码而没有人工监督可能会导致严重的安全性漏洞。因此，每段 AI 生成的代码都必须由人工开发人员仔细审查和测试。

### 4. 状态管理和内存限制

AI 生成的 SDK 的另一个挑战是 LLM 难以在长时间交互中管理状态和上下文。SDK 生成通常涉及多个步骤，其中对先前状态的记忆至关重要，例如链接 API 调用或跟踪身份验证状态。如果没有有效的内存机制，AI 可能会生成无法正确管理这些交互的代码，从而导致工作流程中断。

## 混合方法：结合 AI 和确定性代码生成

鉴于上述限制，AI 尚未准备好取代传统的 SDK 生成方法。但是，结合 AI 和确定性工具优势的混合方法提供了一种有希望的解决方案。虽然 APIMatic 等确定性代码生成器确保可靠、可重复的结果，但 AI 可以增强灵活性并帮助完成更动态的任务。

1. **使用 AI 探索 API**: 在深入代码之前，开发人员需要了解 API 的概念、限制和潜在用例。AI 很适合动态地回答这些类型的查询，筛选文档并提供有关 API 功能的高级见解。通过利用 AI 的自然语言理解能力，开发人员可以快速了解复杂的 API，而无需手动解析大量文档。
2. **用于 API 访问的静态代码生成**: 一旦概念阶段结束，确定性代码生成工具应该接管。这些工具旨在处理可重复、可靠的 API 访问代码生成，包括身份验证流程、请求处理和端点通信。由于工作流程的这一部分需要一致性和安全性，因此传统方法仍然是最合适的。
3. **使用 AI 进行自定义业务逻辑**: 静态 SDK 代码到位后，AI 可以再次帮助开发人员构建与 API 交互的自定义业务逻辑。开发人员可以利用 AI 生成样板代码，快速搭建应用程序逻辑或探索针对其特定用例的创意解决方案。但是，此阶段中每行 AI 生成的代码都应仔细审查，以避免潜在的幻觉和安全漏洞。

## AI 在 SDK 生成中的未来

随着 AI 的不断发展，其在 SDK 生成中的作用预计会越来越大，尽管仍然存在一些挑战。目前，将 AI 与传统代码生成方法相结合，提供了一种平衡的方法来提高开发人员的生产力，而不会牺牲可靠性或安全性。但是，未来的一个重大发展是将面向工作流的规范（如 [Arazzo](https://spec.openapis.org/arazzo/latest.html)）集成到 API 设计和使用中。

Arazzo 是在 OpenAPI Initiative (OAI) 下开发的工作流规范，它允许开发人员超越基本的端点描述，并捕获 API 交互的完整序列，包括状态转换和依赖关系。通过将 AI 驱动的工具与 Arazzo 等规范相结合，开发人员可以更有效地描述和自动化复杂的 API 工作流。

此规范可以通过帮助管理需要上下文感知和状态管理的多步骤工作流，极大地有利于 AI 在 SDK 生成中的应用。例如，涉及多个身份验证步骤、支付网关或用户驱动工作流的 API 可以通过 Arazzo 更好地表示。这种抽象级别可以帮助 AI 工具更好地理解 API 调用的流程，并生成更准确、更可靠的 SDK 代码。

此外，Arazzo 的可扩展性允许开发人员在其工作流中定义自定义业务逻辑，从而在确定性代码生成和 AI 驱动的辅助之间创建更全面的集成。这意味着，虽然 AI 继续处理动态查询解析和初始代码搭建，但像 Arazzo 这样的工具可以指导生成更复杂、有状态的 API 工作流。

随着令牌限制的扩展以及 AI 系统在保持上下文和内存方面的能力的提高，未来的发展可能会使 AI 更有效地处理更大的代码库和多步骤工作流。借助 Arazzo 等增强型规范，AI 生成的 SDK 的准确性和适用性将得到提高，为更无缝、更可靠的开发体验铺平道路。

总之，AI 在 SDK 生成中的未来很可能涉及与 Arazzo 等工作流驱动规范的更深层次集成，增强 AI 处理复杂 API 交互和有状态操作的能力，同时仍然依赖传统方法进行静态代码生成和安全管理。

## 结论

AI 正在成为开发人员越来越有价值的工具，尤其是在探索 API 和自动化重复性任务方面。但是，仍然存在重大挑战，特别是在非确定性、幻觉、安全风险以及无法处理大型代码库方面。

虽然 AI 可以增强 SDK 开发过程，但它还没有准备好完全取代传统方法。目前最有效的方法是混合模型，它利用 AI 的动态能力和传统代码生成器的可靠性。
