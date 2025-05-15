# 使用 Stream Chat 和 Next.js 构建实时投票应用

![使用 Stream Chat 和 Next.js 构建实时投票应用的特色图片](https://cdn.thenewstack.io/media/2025/05/f9283f84-voting12-1024x534.png)

在您希望从各种来源收集意见的情况下，您可以设置一个实时投票系统，允许用户实时投票选择不同的选项，并即时更新结果。以下是如何使用 [Stream Chat API](https://getstream.io/chat/) 和 [Next.js](https://nextjs.org/) 构建该系统的教程。

Stream 是一个强大的工具，可用于向应用程序添加实时聊天功能。它提供诸如频道、消息和用户等功能，可以轻松构建交互式聊天应用程序。

Next.js 是一个流行的 [React 框架](https://getstream.io/chat/sdk/react/)，可以简化 [服务器渲染应用程序](https://thenewstack.io/the-pros-and-cons-of-using-react-today/) 的构建。它提供诸如自动代码拆分、服务器端渲染和热模块替换等功能，使其成为构建现代 Web 应用程序的绝佳选择。

**设置聊天消息**

在 [在 Stream 上创建一个新项目](https://getstream.io/blog/stream-getting-started-guide/) 之前，您需要一个 Stream 帐户，并且需要生成一个 API 密钥才能使用 Stream Chat API。您可以 [免费创建一个新的 Stream 帐户](https://getstream.io/try-for-free/)。

注册后，创建一个新项目并生成一个身份验证令牌，以使用 Stream Chat API 验证您的应用程序。按照 [本教程](https://getstream.io/blog/livestream-chat-nextjs/#setting-up-a-new-stream-application) 中的步骤生成身份验证令牌并设置 Stream Chat API。这将：

- 在 Stream 仪表板上创建一个新组织。
- 通过单击“创建应用”按钮，在该组织内创建一个新应用。
- 通过设置角色和权限来配置应用，并从“应用访问密钥”部分获取“key”和（可选）“secret”。

在生产应用程序中，您应该使用“key”和“secret”生成身份验证令牌。但是，在本教程中，为简单起见，您将仅使用“key”。

要禁用身份验证，请在 Stream Chat 仪表板中启用设置“禁用身份验证检查”。

**应用程序概述**

在构建应用程序之前，请查看您将实现的关键组件和功能。

该应用程序将具有以下屏幕：

**登录**：用户必须提供用户名才能加入投票。

**投票系统**：这是应用程序中进行投票的部分。

从功能上讲，该应用程序具有以下功能：

- 用户登录后，他们可以查看所有现有问题并对其进行投票。
- 用户可以添加带有多个选项的新问题。
- 结果会随着用户的投票而实时更新。

请注意，我们不会在本教程中实现身份验证，也不会专注于用户界面 (UI) 设计。但是，最终代码可供参考。相反，我们将专注于投票系统的核心功能及其与 Stream Chat 的集成。

**设置您的项目**

使用 `create-next-app` 命令创建一个具有必要配置的新 Next.js 项目：

```bash
npx create-next-app my-voting-app
cd my-voting-app
```

**安装依赖项**

接下来，安装使用 Stream Chat API 所需的依赖项：

```bash
npm install stream-chat-react
```

除了 [Stream Chat SDK](https://github.com/GetStream/stream-chat-js/) 之外，您还必须安装其他依赖项，包括 `zustand`，这是一个轻量级的状态管理库，用于管理应用程序状态：

```bash
npm install zustand
```

**初始化 Stream 客户端**

创建一个 Stream 客户端实例以与 Stream Chat API 交互。为此，创建一个名为 `src/lib/stream.ts` 的新文件并添加以下代码：

```typescript
import { StreamChat } from 'stream-chat';

const chatClient = StreamChat.getInstance('your_api_key');
```

您将使用此客户端实例来创建频道、发送消息和处理应用程序中的实时更新。

**管理用户**

当用户登录时，他们将连接到 Stream Chat 并被添加到投票会话频道。这将允许用户发送和接收实时投票会话消息。

步骤如下：

- 将用户连接到 Stream Chat。
- 将用户添加到投票会话频道。
- 从频道加载现有问题和投票。
- 返回会话频道对象以在前端与投票会话进行交互。

**1. 将用户连接到 Stream Chat**

要将用户添加到投票会话频道，您需要将他们连接到 Stream Chat。使用 Stream Chat SDK 提供的 `connectUser` 方法：

```typescript

```
export const initializeStream = async (username: string) => {
  try {
    // Connect user to Stream
    await chatClient.connectUser(
      { id: username, name: username },
      chatClient.devToken(username)
    );
  } catch (error) {
    console.error('Error connecting to Stream Chat:', error);
  }
};

传递用户 ID 和姓名作为参数，以在聊天中识别用户。然后使用 `devToken` 方法生成一个开发令牌，以[验证用户](https://thenewstack.io/master-difficult-user-authentication-requirements-with-oauth/)。

**2. 将用户添加到投票会话**

一旦用户连接到 Stream Chat，将其添加到投票会话频道。这允许用户在投票会话中发送和接收消息：

```javascript
// Create or connect to the session channel if not already connected
if (!sessionChannel) {
  sessionChannel = chatClient.channel('messaging', 'voting-session', {
    name: 'Voting Session',
    members: [username],
  });
}
```

此代码首先检查会话频道是否存在。如果不存在，它使用 `chatClient.channel` 方法创建一个新频道，类型为 `messaging`，ID 为 `voting-session`。它将频道名称指定为 `Voting Session`，并将用户作为成员添加到频道。如果频道已存在，Stream Chat 会将用户连接到现有频道并返回频道对象。

**3. 加载现有问题和投票**

在将用户连接到 Stream Chat 并将其添加到投票会话频道后，从频道加载现有问题和投票：

```javascript
// Get all messages from the channel
const response = await sessionChannel.query({
  messages: { limit: 100 }, // limit is not required but added for demonstration
  state: true,
});

const messages = response.messages || [];

// Process messages to get questions and votes
const questions: VotingQuestion[] = [];
const seenQuestions = new Set();

// Process from oldest to newest to maintain order and get latest state
messages.reverse().forEach((msg: MessageResponse) => {
  if (msg.type === 'regular') {
    const customData = msg.data as any;
    if (customData?.type === 'new_question' && !seenQuestions.has(customData.id)) {
      questions.push({
        id: customData.id,
        question: customData.question,
        options: customData.options,
        votes: customData.votes || {},
      });
      seenQuestions.add(customData.id);
    }
  }
});

// Update store with existing questions
if (questions.length > 0) {
  useVoteStore.setState({ questions });
}
```

这会查询频道以获取最新的消息和状态。然后，它处理消息以从频道数据中提取问题和投票。它将问题存储在一个数组中，并将投票存储在一个映射中，以便于访问。

将上述函数添加到您的 `initializeStream` 函数中，以处理投票系统中的用户管理。此函数应返回会话频道对象，应用程序使用该对象在投票会话中发送和接收消息。

应用程序的状态会针对收到的每条消息进行更新，以反映新的问题和投票。这确保了 UI 始终与投票会话中的最新数据保持同步。

这是更新后的 `initializeStream` 函数，其中包含用户管理逻辑：

```javascript
// Create a singleton instance for the session channel
let sessionChannel: any = null;

const initializeStream = async (username: string) => {
  try {
    // Connect user to Stream
    // ... (as shown above)

    // Create or connect to the session channel if not already connected

    // Get all messages from the channel

    // Process messages to get questions and votes

    // Update store with existing questions

    return sessionChannel;
  } catch (error) {
    console.error('Error initializing Stream:', error);
    return null;
  }
};
```

此设置将用户连接到 Stream Chat，将他们添加到投票会话频道，并从频道加载现有问题和投票。

在下一节中，您将实现允许用户对问题进行投票并将新问题添加到投票会话的逻辑。

**投票系统**

接下来，让我们专注于实现投票系统的核心功能。用户应该能够对现有问题进行投票，并添加具有多个选项的新问题。为此，您将定义以下功能：

- 在用户登录时将他们添加到会话。监听来自会话的新问题和投票。
- 允许用户对问题进行投票并添加新问题。这应该实时传播到会话。

**Vote Store**

在实现投票系统之前，使用 Zustand 设置一个存储来[管理应用程序状态](https://thenewstack.io/how-to-better-manage-stateful-applications-in-kubernetes/)。配置 Zustand 以创建一个存储来[管理用户](https://thenewstack.io/managing-user-access-in-multiregion-deployments/)、问题和投票：
```typescript
// Define our store types
interface User { 
  username: string;
}

export interface VotingQuestion { 
  id: string; 
  question: string; 
  options: string[]; 
  votes: Record<string, string>; // userId -> optionId
}

interface VoteStore { 
  user: User | null; 
  questions: VotingQuestion[]; 
  setUser: (user: User | null) => void; 
  addQuestion: (question: Omit<VotingQuestion, "id" | "votes">) => void; 
  vote: (questionId: string, option: string) => void; 
  addQuestionFromStream: (question: VotingQuestion) => void; 
  addVoteFromStream: (questionId: string, userId: string, option: string) => void;
}

// 这定义了用户、投票问题和 store 本身的 store 类型。该 store 包含 user 对象、投票问题数组和用于更新 store 状态的方法。我不会在这里详细介绍每种方法，但你将在构建投票系统时实现它们。
// 使用 Zustand 创建 store 并导出它以在我们的应用程序中使用：

// Create the store
export const useVoteStore = create<VoteStore>((set) => ({ 
  // contains implementation of the store methods
}));

// **监听会话中的消息**
// 你将使用 `initializeStream` 函数返回的会话通道对象来显示现有问题和选项。

// 当用户登录时，他们将连接到 Stream Chat，并且将加载通道中现有的问题和投票。然后，应用程序将在前端显示问题和选项：

// Handle form submission 
const handleSubmit = async (e: React.FormEvent) => { 
  e.preventDefault(); 
  if (username.trim()) { 
    try { 
      const channel = await initializeStream(username.trim()); 
      // Listen for new messages 
      channel.on('message.new', (event: any) => { 
        if (event.user?.id !== username.trim()) { 
          const customData = event.message.data; 
          if (customData?.type === 'new_question') { 
            useVoteStore.getState().addQuestionFromStream(customData); 
          } 
          if (customData?.type === 'new_vote') { 
            const { questionId, userId, option } = customData; 
            useVoteStore.getState().addVoteFromStream(questionId, userId, option); 
          } 
        } 
      }); 
      setUser({ username: username.trim() }); 
      router.replace("/vote"); 
    } catch (error) { 
      console.error('Failed to initialize Stream:', error); 
      // Handle error appropriately 
    } 
  } 
};

// 这从表单输入中获取用户名，并调用 `initializeStream` 函数以将用户连接到 Stream Chat。然后，它侦听投票会话通道中的新消息，并根据收到的消息更新应用程序状态。最后，它设置用户状态并导航到投票页面。
// 接收到的新数据要么是新问题，要么是投票。通过相应地更新本地状态对象，它们会显示在 UI 上。

// **添加新问题和投票**
// 接下来，你将实现逻辑来处理投票系统中用户的交互。无论用户是对现有问题进行投票还是添加具有多个选项的新问题，投票和问题创建都必须实时传播到投票会话。

// 我将把这两种交互都建模为发送到会话通道的消息。我将从添加一个新问题开始：

addQuestion: (questionData) => { 
  const newQuestion = { ...questionData, id: generateId(), votes: {} }; 
  // Update local state first 
  set((state) => ({ questions: [...state.questions, newQuestion] })); 
  // Then broadcast to other users 
  if (sessionChannel) { 
    void sessionChannel.sendMessage({ text: JSON.stringify(newQuestion), data: { type: 'new_question', ...newQuestion } }); 
  }
}

// 当用户添加问题时，应用程序会生成一个唯一的 ID，并使用新问题更新本地状态。然后，它将包含新问题数据的消息发送到会话通道。请注意，消息类型设置为 `new_question`，以便将其与投票消息区分开。
// 你可以类似地实现处理用户投票的逻辑：

vote: (questionId, option) => { 
  const username = useVoteStore.getState().user?.username; 
  if (!username) return; 
  // Send vote to stream 
  sessionChannel?.sendMessage({ text: 'New vote cast', type: 'regular', data: { type: 'new_vote', questionId, userId: username, option } }); 
  set((state) => ({ questions: state.questions.map(q => q.id === questionId ? { ...q, votes: { ...q.votes, [username]: option } } : q ) }));
}

// 此项目的[最终代码](https://github.com/tyaga001/voting-system)可在 GitHub 上找到以供参考。

// 如果你喜欢这个，你可能也会喜欢我的[关于使用 Stream 构建自定义视频会议应用程序的详细指南](https://www.freecodecamp.org/news/how-i-built-a-custom-video-conferencing-app-with-stream-and-nextjs/)。

// [
// YOUTUBE.COM/THENEWSTACK
// Tech moves fast, don't miss an episode. Subscribe to our YouTube
// 技术发展迅速，不要错过任何一集。订阅我们的 YouTube
```
channel 来播放我们所有的播客、访谈、演示等内容。[The New Stack 的 YouTube 频道](https://youtube.com/thenewstack?sub_confirmation=1)