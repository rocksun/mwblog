<!--
title: 使用Stream和OpenAI构建AI聊天助手
cover: https://cdn.thenewstack.io/media/2025/05/9aeb9a84-chat.png
summary: 用Stream和OpenAI快速构建AI聊天助手！前端Vite+React集成`stream-chat` SDK，后端Node.js用OpenAI API驱动。通过Stream Chat UI创建访客用户和临时频道，`useWatchers` Hook监控AI机器人加入。轻松定制AI助手，解决用户疑问！
-->

用Stream和OpenAI快速构建AI聊天助手！前端Vite+React集成`stream-chat` SDK，后端Node.js用OpenAI API驱动。通过Stream Chat UI创建访客用户和临时频道，`useWatchers` Hook监控AI机器人加入。轻松定制AI助手，解决用户疑问！

> 译自：[Build an AI Chat Assistant With Stream and OpenAI](https://thenewstack.io/build-an-ai-chat-assistant-with-stream-and-openai/)
> 
> 作者：Danny Adams

您是否曾经访问过某个网站，发现自己在与一个感觉几乎像人类的 [AI 助手](https://getstream.io/blog/ai-assistant/) 聊天？您可以构建一个 AI 聊天助手，它驻留在您的网站上，了解业务，并实时帮助用户解决他们的疑问。

它将集成 [Stream](https://getstream.io/) 用于 [聊天基础设施](https://getstream.io/chat/) 和 UI，以及 [OpenAI API](https://thenewstack.io/beyond-chatgpt-exploring-the-openai-platform/) 用于 [AI 驱动的对话](https://getstream.io/chat/solutions/ai-integration/)。这个功能齐全的 AI 助手将根据公司的知识库进行定制，配有时尚的 UI 和浮动聊天小部件。

整个代码仓库可以在 [这里](https://github.com/DoableDanny/Stream-AI-Assistant-Chat-App) 找到。

## 项目设置

### 1. 创建前端

使用 [Vite](https://vitejs.dev/) 快速搭建一个 React + TypeScript 应用程序。

```bash
yarn create vite frontend --template react-ts
cd frontend
```

### 2. 安装依赖项

这些包设置了聊天功能并处理聊天会话的唯一 ID。

```bash
yarn add stream-chat stream-chat-react uuid
```

- `stream-chat`: 核心 [Stream Chat SDK](https://getstream.io/chat/sdk/)。
- `stream-chat-react`: 用于聊天 UI 的预构建 React 组件。
- `uuid`: 用于生成唯一的频道名称或用户 ID。

启动开发服务器：

```bash
yarn dev
```

### 3. 设置 Stream API 访问

在 [Stream](https://getstream.io/try-for-free/) 创建一个免费帐户，并在仪表板中设置一个新的应用程序。

![](https://cdn.thenewstack.io/media/2025/05/1b4281c3-image1a-1024x347.png)

*图片 1*

![](https://cdn.thenewstack.io/media/2025/05/bf88877c-image2a-905x1024.png)

*图片 2*

从 **聊天消息 > 概述**，复制您的 **应用程序访问密钥**。

![](https://cdn.thenewstack.io/media/2025/05/d05265ea-image3a-1024x312.png)

*图片 3*

在您的 `frontend` 文件夹中创建一个 `.env` 文件，并添加密钥：

```
VITE_STREAM_API_KEY=<your_key>
```

📌 *注意：Vite 要求前端可访问的环境变量以 `VITE_` 开头。*

## 创建 Stream 客户端

在设置好前端项目并准备好 API 密钥后，项目就可以初始化 Stream Chat 客户端并渲染 [聊天 UI](https://getstream.io/chat/ui-kit/)。

### 1. 替换 src/App.tsx

首先，将 `App.tsx` 中的默认内容替换为基本布局和聊天组件的占位符：

```tsx
import "stream-chat-react/dist/css/v2/index.css";
import "./App.css";
import AIChat from "./components/AIChat/AIChat";

const App = () => {
  return (
    <>
      <section className="section">
        <div className="container">
          <h1>Welcome to StreamIO Chat</h1>
          <p>
            Lorem ipsum dolor sit amet consectetur adipisicing elit. Sint omnis
            ipsum, incidunt at quas dolorum a earum aspernatur quaerat amet
            impedit vero rerum corrupti autem natus dolor sapiente modi nemo.
          </p>
        </div>
      </section>
      <AIChat />
    </>
  );
};

export default App;
```

### 2. 创建 AIChat.tsx

在 `src/components/AIChat/AIChat.tsx` 创建一个新文件。这将使用 API 密钥初始化 Stream 客户端，并将其连接到 React SDK。

```tsx
import { StreamChat } from "stream-chat";
import { Chat } from "stream-chat-react";

const apiKey = import.meta.env.VITE_STREAM_API_KEY;

if (!apiKey) {
  throw new Error("Missing Stream API key");
}

const client = new StreamChat(apiKey);

const AIChat = () => {
  if (!client) return <div>Setting up client & connection...</div>;

  return <Chat client={client} />;
};

export default AIChat;
```

以下是正在发生的事情：

- 它使用 API 密钥初始化一个 StreamChat 实例。
- 如果客户端未准备好，它会显示一条加载消息。
- 客户端设置好后，它会从 `stream-chat-react` 传递到 Chat 组件。

此设置准备应用程序连接到聊天后端，但尚未创建用户和频道。接下来，构建聊天界面并将访客用户连接到临时频道以与助手交谈。

## 创建 UI

使用 [Stream 的预构建 React 组件](https://thenewstack.io/build-a-real-time-voting-app-with-stream-chat-and-next-js/) 构建聊天界面。

### 1. 更新 AIChat.tsx

将 `AIChat.tsx` 的内容替换为以下内容。这将处理设置访客用户、创建临时频道和渲染完整的聊天界面。
```tsx
import { StreamChat } from 'stream-chat';
import {
  Chat,
  Channel,
  ChannelHeader,
  MessageInput,
  MessageList,
  Thread,
  Window,
} from 'stream-chat-react';
import 'stream-chat-react/dist/css/v2/index.css';
import { v4 as uuidv4 } from 'uuid';
import { useEffect, useState } from 'react';

const apiKey = import.meta.env.VITE_STREAM_API_KEY;

if (!apiKey) {
  throw new Error('Missing Stream API key');
}

const client = new StreamChat(apiKey);

const AIChat = () => {
  const [channel, setChannel] = useState(null);
  const [thread, setThread] = useState(null);
  const [isOpen, setIsOpen] = useState(false);

  useEffect(() => {
    const initChat = async () => {
      const userId = uuidv4();

      await client.setUser(
        {
          id: userId,
          name: 'Guest User',
        },
        client.devToken(userId)
      );

      const channelId = 'ai-assistant';
      const channel = client.channel('livestream', channelId, {
        name: 'AI Assistant',
      });

      await channel.create();
      setChannel(channel);
    };

    initChat();
  }, []);

  if (!channel) return <div>Setting up client & connection...</div>;

  return (
    <div className="AIChat">
      <Chat client={client} theme="messaging light">
        <Channel channel={channel}>
          <Window>
            <ChannelHeader />
            <MessageList onThreadSelect={(thread) => setThread(thread)} />
            <MessageInput />
          </Window>
          <Thread thread={thread} />
        </Channel>
      </Chat>
    </div>
  );
};
```

**这里发生了什么？**

- 创建了一个访客用户，因此访问者无需登录即可使用聊天。
- 使用 `uuidv4()` 创建唯一的聊天频道以避免冲突。
- Stream React 组件呈现完整的聊天界面：
  - `ChannelHeader` – 聊天窗口的标题区域。
  - `MessageList` – 显示对话。
  - `MessageInput` – 用于发送新消息的输入字段。
  - `AIStateIndicator` – 显示 AI 活动，例如“正在思考…”动画。
  - `Thread` – 支持线程对话。

**此时，UI 已经就位，但可能会出现一条错误消息：**

**Error**: StreamChat 错误代码 17：GetOrCreateChannel failed with error: “User ‘guest-586486fd-d52e-4626-af0e-a480c83f95c6-guest_user’ with role ‘guest’ is not allowed to perform action CreateChannel in scope ‘messaging'”

这意味着不允许访客用户创建消息频道（或“聊天室”）。因此，在 Stream 仪表板中，转到“角色和权限”：

![](https://cdn.thenewstack.io/media/2025/05/511e653a-image4a-1024x388.png)

*图片 4*

对于“guest”角色和“messaging”范围，添加以下权限：

- Read Channel（读取频道）
- Create Message（创建消息）
- Create Channel（创建频道）

更新权限后，聊天 UI 现在应该可以成功加载，并且访客将拥有一个可用的聊天界面：

![](https://cdn.thenewstack.io/media/2025/05/e9460363-screenshot-2025-05-23-at-11.41.15%E2%80%AFam-290x300.png)

*图片 5*

## 设置服务器

要将聊天前端[连接到 AI 模型](https://getstream.io/blog/connect-ai-model-chatbot/)（如 OpenAI），需要一个后端来处理请求、安全地通过第三方 API 进行身份验证并触发 AI 代理加入聊天。

Stream 为此提供了一个即用型的 Node.js 后端。

### 1. 克隆示例服务器

从项目根目录：

```bash
git clone https://github.com/GetStream/ai-assistant-nodejs
cd ai-assistant-nodejs
yarn install
```

此后端已预先配置为与 Stream 配合使用，并支持 OpenAI 和 Anthropic。要使用 OpenAI：

### 2. 获取您的 OpenAI API 密钥

- 前往 [https://platform.openai.com/.](https://platform.openai.com/)
- 登录或创建一个帐户。
- 前往 **API 密钥**: [https://platform.openai.com/api-keys](https://platform.openai.com/api-keys) - 单击“+ Create new secret key”。
- 立即复制密钥。（您将无法再次看到它）。

### 3. 创建一个 `.env` 文件

在 `ai-assistant-nodejs` 文件夹中，创建一个 `.env` 文件并添加以下内容：

```
ANTHROPIC_API_KEY=not_needed
STREAM_API_KEY=insert_your_key
STREAM_API_SECRET=insert_your_secret
OPENAI_API_KEY=insert_your_key
OPENWEATHER_API_KEY=not_needed
```

### 4. 切换后端以使用 OpenAI

默认情况下，后端使用 Anthropic。要切换到 OpenAI，请在 `index.ts` 或 `app.ts` 中找到此路由：

```typescript
app.post('/start-ai-agent', async (req, res) => {
 const {
   channel_id,
   channel_type = 'messaging',
   platform = 'openai',
 } = req.body;
```

确保 `platform = 'openai'`。

### 5. 启动服务器

现在后端可以在本地运行：

`yarn dev`

默认情况下，这将在 `http://localhost:3000` 上启动服务器。前端需要将 AI 机器人添加到聊天频道时，将调用此服务器。

接下来，在前端中连接它，以便 AI 在新用户打开聊天时自动加入。

## 检查 AI 是否在聊天中

为了确保 AI 代理在需要时自动加入聊天，请创建一个自定义 React Hook 来监视频道的观察者，并检查 AI 机器人是否存在。如果不存在，则触发后端以添加它。

### 1. 创建一个 `useWatchers` Hook

在 `frontend/src/custom-hooks/useWatchers.ts` 创建一个新文件：
```typescript
// Content of useWatchers.ts


import { useCallback, useEffect, useState } from "react";
import { Channel } from "stream-chat";

export const useWatchers = ({ channel }: { channel: Channel }) => {
  const [watchers, setWatchers] = useState<string[] | undefined>(undefined);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState<Error | null>(null);

  const queryWatchers = useCallback(async () => {
    setLoading(true);
    setError(null);
    try {
      const result = await channel.query({ watchers: { limit: 5, offset: 0 } });
      setWatchers(result?.watchers?.map((watcher) => watcher.id));
      setLoading(false);
      return;
    } catch (err) {
      console.error("An error has occurred while querying watchers: ", err);
      setError(err as Error);
    }
  }, [channel]);

  useEffect(() => {
    queryWatchers();
  }, [queryWatchers]);

  useEffect(() => {
    const watchingStartListener = channel.on("user.watching.start", (event) => {
      const userId = event?.user?.id;
      if (userId && userId.startsWith("ai-bot")) {
        setWatchers((prevWatchers) => [
          userId,
          ...(prevWatchers || []).filter((watcherId) => watcherId !== userId),
        ]);
      }
    });

    const watchingStopListener = channel.on("user.watching.stop", (event) => {
      const userId = event?.user?.id;
      if (userId && userId.startsWith("ai-bot")) {
        setWatchers((prevWatchers) => (prevWatchers || []).filter((watcherId) => watcherId !== userId));
      }
    });

    return () => {
      watchingStartListener.unsubscribe();
      watchingStopListener.unsubscribe();
    };
  }, [channel]);

  return { watchers, loading, error };
};

```

### 2. 创建自定义频道头部

现在创建一个新的频道头部，用于检查 AI 是否在频道中，如果不在，则调用后端以添加它。

```javascript
import { useChannelStateContext } from "stream-chat-react";
import { useWatchers } from "../../custom-hooks/useWatchers";
import { useEffect } from "react";

export default function MyChannelHeader() {
  const { channel } = useChannelStateContext();
  const { watchers } = useWatchers({ channel });

  const aiInChannel = (watchers ?? []).filter((watcher) => watcher.includes("ai-bot")).length > 0;

  useEffect(() => {
    const addAIAgent = async () => {
      if (!channel || aiInChannel) return;

      const endpoint = "start-ai-agent";
      await fetch(`http://127.0.0.1:3000/${endpoint}`, {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ channel_id: channel.id }),
      });
    };

    addAIAgent();
  }, [aiInChannel, channel]);

  return (
    <div className="my-channel-header">
      <h2>AI Assistant</h2>
      {aiInChannel ? (
        <span style={{ fontSize: 12, color: "gray" }}> I'm Stream's AI helper! </span>
      ) : (
        <span style={{ fontSize: 14, color: "red" }}>Not connected to AI</span>
      )}
    </div>
  );
}
```

### 3. 更新 AIChat.tsx

在 `AIChat.tsx` 中，将默认的 `ChannelHeader` 替换为新的：

```jsx
<Window>
  <MyChannelHeader /> // Add this
  <MessageList />
  <AIStateIndicator />
  <MessageInput />
</Window>
```

现在，每当用户打开聊天时，应用程序都会检查 AI 代理是否存在。如果不存在，它会调用后端并自动邀请 AI 进入聊天频道。
让我们测试一下：

![](https://cdn.thenewstack.io/media/2025/05/2eb55610-image6b-300x252.png)
Image 6

太棒了——一个 AI 聊天！

但是，这并不是最终目标。 还需要做：

- 使其看起来像一个 AI 助手。
- 教会 AI 助手关于我们公司的信息，并指示它如何回复用户的消息，以便它实际解决用户的问题，以便它实际解决用户的问题。

首先，解决样式问题...

## 样式化我们的聊天助手

网站每个页面右下角的按钮将在单击时打开 AI 聊天。

首先，创建将切换聊天显示的按钮：

```jsx
import classes from "./AIChat.module.css";

interface Props {
  onClick: () => void;
  showAIChat: boolean;
}

const ToggleAIChatButton = ({ onClick, showAIChat }: Props) => {
  return (
    <button onClick={onClick} className={classes.toggleAIChatButton}>
      {showAIChat ? "⏷" : "💬"}
    </button>
  );
};

export default ToggleAIChatButton;
```

将 css 添加到 `AIChat/AIChat.module.css`：

```css
.toggleAIChatButton {
  position: absolute;
  bottom: 20px;
  right: 20px;
  width: 60px;
  height: 60px;
  background: black;
  color: white;
  border-radius: 50%;
  font-size: 20px;
  cursor: pointer;
  border: none;
  display: flex;
  align-items: center;
  justify-content: center;
  transition: background 0.3s;
}

.toggleAIChatButton:hover {
  background: #333;
}
```

现在[创建一个新组件](https://thenewstack.io/genai-helps-frontend-developers-create-components/)，位于 `src/components/AIChat/AIChatWidget.tsx`，以有条件地显示 AI 聊天：

```markdown
import { useState } from "react";
import AIChat from "./AIChat";
import ToggleAIChatButton from "./ToggleAIChatButton";
import classes from "./AIChat.module.css";

const AIChatWidget = () => {
  const [showAIChat, setShowAIChat] = useState(false);

  const toggleAIChat = () => {
    setShowAIChat((prev) => !prev);
  };

  return (
    <div>
      <div
        className={`${classes.chatPanel} ${!showAIChat ? classes.hidden : ""}`}
      >
        <AIChat />
      </div>
      <ToggleAIChatButton onClick={toggleAIChat} showAIChat={showAIChat} />
    </div>
  );
};

export default AIChatWidget;

```

将以下类添加到 `AIChat.module.css`:

```css
.chatPanel {
  position: absolute !important;
  bottom: 60px !important;
  right: 0 !important;
  height: 400px !important;
  min-width: 320px !important;
  max-width: 500px !important;
}

.hidden {
  display: none;
}
```

![](https://cdn.thenewstack.io/media/2025/05/300dff68-image7a-150x150.png)

*图片 7*

现在，每个页面底部都有一个按钮。

单击时，它会切换 AI 聊天。

太棒了！情况看起来好多了。但这仍然只是一些通用的 AI 聊天，比如 ChatGPT。我们希望它像 Stream 专家一样做出回应。

## 指示 AI 成为 Stream 专家

转到您的在后端，更改助理的姓名并指示其行为：[OpenAIAgent.ts](http://openaiagent.ts)

```typescript
this.assistant = await this.openai.beta.assistants.create({
  name: 'Stream AI Assistant',
  instructions: `
    You are a helpful, professional AI assistant for Stream.io, a company providing scalable APIs and SDKs for building in-app chat, video, and activity feeds. 
    Assist users by answering their questions clearly and accurately. 
    If users ask about any of the following, respond with the corresponding information:

    Support or contacting a human: Direct them to https://getstream.io/contact/support/
    Help Center or documentation lookup: Point them to https://support.getstream.io/hc/en-us
    Pricing details: Guide them to https://getstream.io/chat/pricing/
    Company/team info: Refer them to https://getstream.io/team/

    Documentation-specific queries:
      Chat API/docs: https://getstream.io/chat/docs/
      Video & audio docs: https://getstream.io/video/docs
      Activity Feed docs: https://getstream.io/activity-feeds/docs
      Moderation docs: https://getstream.io/moderation/docs

    For anything related to configuring Stream, accessing API keys, managing users, teams, or billing, direct users to https://dashboard.getstream.io/

    If you're unsure or the topic is not covered, say: "I'm not certain about that, but I recommend reaching out to our support team."

    Keep your responses friendly, accurate, and focused on helping users efficiently navigate GetStream.io's tools and resources.
  `
});
```

使用 `yarn dev` 重新启动服务器，让我们看看会发生什么：

![](https://cdn.thenewstack.io/media/2025/05/316a9790-image9b-300x269.png)

*图片 8*

就这样，Stream 就有了一个 AI 助手。

![](https://cdn.thenewstack.io/media/2025/05/625b4593-image10.gif)

## 结论

您现在有了一个可用的示例，可以处理访客用户、管理聊天频道并连接到 AI 后端。

有了这个基础，您可以将自己的 AI 助手变为现实，并将智能对话直接嵌入到您的网站中。