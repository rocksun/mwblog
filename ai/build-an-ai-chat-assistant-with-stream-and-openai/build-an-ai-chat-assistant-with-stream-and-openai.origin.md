# Build an AI Chat Assistant With Stream and OpenAI
![Featued image for: Build an AI Chat Assistant With Stream and OpenAI](https://cdn.thenewstack.io/media/2025/05/9aeb9a84-chat-1024x577.png)
Have you ever visited a website and found yourself chatting with an [AI assistant](https://getstream.io/blog/ai-assistant/) that feels almost human? You can build an AI chat assistant that lives on your website, knows the business and helps users with their queries in real time.

It will integrate [Stream](https://getstream.io/) for [chat infrastructure](https://getstream.io/chat/) and UI, and the [OpenAI API](https://thenewstack.io/beyond-chatgpt-exploring-the-openai-platform/) for [AI-powered conversations](https://getstream.io/chat/solutions/ai-integration/). This fully functional AI assistant will be tailored to a company’s knowledge base, complete with a sleek UI and a floating chat widget.

The entire code repository can be found [here](https://github.com/DoableDanny/Stream-AI-Assistant-Chat-App).

## Project Setup
### 1. Create the Frontend
Use [Vite](https://vitejs.dev/) to quickly scaffold a React + TypeScript app.

12 |
yarn create vite frontend --template react-tscd frontend |
### 2. Install Dependencies
These packages set up the chat functionality and handle unique IDs for chat sessions.

1 |
yarn add stream-chat stream-chat-react uuid |
`stream-chat`
: Core[Stream Chat SDK](https://getstream.io/chat/sdk/).`stream-chat-react`
: Prebuilt React components for chat UIs.`uuid`
: Used to generate unique channel names or user IDs.
Start the development server:

`yarn dev`
### 3. Set Up Stream API Access
Create a free account at [Stream](https://getstream.io/try-for-free/) and set up a new app in the dashboard.

![](https://cdn.thenewstack.io/media/2025/05/1b4281c3-image1a-1024x347.png)
Image 1

![](https://cdn.thenewstack.io/media/2025/05/bf88877c-image2a-905x1024.png)
Image 2

From **Chat Messaging > Overview**, copy your **App Access Key**.

![](https://cdn.thenewstack.io/media/2025/05/d05265ea-image3a-1024x312.png)
Image 3

Create a `.env`
file in your `frontend`
folder and add the key:

`VITE_STREAM_API_KEY=<your_key>`
📌 *Note: Vite requires environment variables accessible to the frontend to be prefixed with *

*VITE_*
*.*
## Creating the Stream Client
With the frontend project set up and your API key ready, the project is ready to initialize the Stream Chat client and render the [chat UI](https://getstream.io/chat/ui-kit/).

### 1. Replace src/App.tsx
Start by replacing the default content in `App.tsx`
with a basic layout and a placeholder for the chat component:

123456789101112131415161718192021222324 |
import "stream-chat-react/dist/css/v2/index.css";import "./App.css";import AIChat from "./components/AIChat/AIChat";const App = () => { return ( <> <section className="section"> <div className="container"> <h1>Welcome to StreamIO Chat</h1> <p> Lorem ipsum dolor sit amet consectetur adipisicing elit. Sint omnis ipsum, incidunt at quas dolorum a earum aspernatur quaerat amet impedit vero rerum corrupti autem natus dolor sapiente modi nemo. </p> </div> </section> <AIChat /> </> );};export default App; |
### 2. Create AIChat.tsx
Create a new file at `src/components/AIChat/AIChat.tsx`
. This will initialize the Stream client using the API key and connect it to the React SDK.

1234567891011121314151617 |
import { StreamChat } from "stream-chat";import { Chat } from "stream-chat-react";const apiKey = import.meta.env.VITE_STREAM_API_KEY;if (!apiKey) { throw new Error("Missing Stream API key");}const client = new StreamChat(apiKey);const AIChat = () => { if (!client) return <div>Setting up client & connection...</div>; return <Chat client={client} />;};export default AIChat; |
Here’s what’s happening:
- It initalizes a StreamChat instance using the API key.
- If the client is not ready, it shows a loading message.
- Once the client is set, it is passed to the Chat component from
`stream-chat-react`
.
This setup prepares the app to connect to the chat backend, the user and channel have not been created yet. Next build the chat interface and connect a guest user to a temporary channel to talk to the assistant.

## Creating the UI
Build the chat interface using [Stream’s prebuilt React components](https://thenewstack.io/build-a-real-time-voting-app-with-stream-chat-and-next-js/).

### 1. Update AIChat.tsx
Replace the contents of `AIChat.tsx`
with the following. This will handle setting up a guest user, creating a temporary channel and rendering the complete chat interface.

1234567891011121314151617181920212223242526272829303132333435363738394041424344454647484950515253545556 |
import { useEffect, useState } from "react";import { type Channel as ChannelType, StreamChat } from "stream-chat";import { Chat, Channel, MessageInput, MessageList, Thread, Window, ChannelHeader, AIStateIndicator,} from "stream-chat-react";import { v4 as uuidv4 } from "uuid";const apiKey = import.meta.env.VITE_STREAM_API_KEY;if (!apiKey) { throw new Error("Missing Stream API key");}const client = new StreamChat(apiKey);const AIChat = () => { const [channel, setChannel] = useState<ChannelType>(); useEffect(() => { const setUpGuestChat = async () => { // create a guest user await client.setGuestUser({ id: `guest_user` }); // create channel (in other words, a chat room) for this guest const guestChannel = client.channel( "messaging", `ai_support_channel_${uuidv4()}` ); setChannel(guestChannel); }; setUpGuestChat(); }, []); if (!client || !channel) return <div>Setting up client & connection...</div>; return ( <Chat client={client}> <Channel channel={channel}> <Window> <ChannelHeader title="AI Support" /> <MessageList /> <AIStateIndicator /> <MessageInput /> </Window> <Thread /> </Channel> </Chat> );}; |
#### What’s Happening Here?
- A guest user is created so visitors don’t need to log in to use the chat.
- A unique chat channel is created using
`uuidv4()`
to avoid conflicts. - The Stream React components render the complete chat interface:
`ChannelHeader`
– Header area for the chat window.`MessageList`
– Displays the conversation.`MessageInput`
– Input field for sending new messages.`AIStateIndicator`
– Shows AI activity like “thinking…” animations.`Thread`
– Supports threaded conversations.
**At this point, the UI is in place, but an error message might appear: **
**Error**: StreamChat error code 17: GetOrCreateChannel failed with error: “User ‘guest-586486fd-d52e-4626-af0e-a480c83f95c6-guest_user’ with role ‘guest’ is not allowed to perform action CreateChannel in scope ‘messaging'”
This means guest users are not permitted to create message channels (or “chat rooms”). So, in the Stream dashboard, go to “Roles and Permissions”:

![](https://cdn.thenewstack.io/media/2025/05/511e653a-image4a-1024x388.png)
Image 4

For the “guest” Role and “messaging” Scope, add the following permissions:

- Read Channel
- Create Message
- Create Channel
With permissions updated, the chat UI should now load successfully, and guests will have a working chat interface:

![](https://cdn.thenewstack.io/media/2025/05/e9460363-screenshot-2025-05-23-at-11.41.15%E2%80%AFam-290x300.png)
Image 5

## Setting Up the Server
To [connect the chat frontend to an AI model](https://getstream.io/blog/connect-ai-model-chatbot/) like OpenAI, a backend is required that can handle requests, authenticate securely with third-party APIs and trigger the AI agent to join the chat.

Stream provides a ready-to-use Node.js backend for this.

### 1. Clone the Example Server
From the project root:

123 |
git clone <a href="https://github.com/GetStream/ai-assistant-nodejs">https://github.com/GetStream/ai-assistant-nodejs.git</a>cd ai-assistant-nodejsyarn install |
This backend is preconfigured to work with Stream and supports OpenAI and Anthropic. To use OpenAI:
### 2. Get Your OpenAI API Key
- Go to
[https://platform.openai.com/.](https://platform.openai.com/) - Sign in or create an account.
- Go to
**API Keys**:[https://platform.openai.com/api-keys](https://platform.openai.com/api-keys) - Click “+ Create new secret key”.
- Copy the key immediately. (You won’t be able to see it again).
****3. Create an `.env`
File
In the `ai-assistant-nodejs`
folder, create an `.env`
file and add the following:

123456789 |
ANTHROPIC_API_KEY=not_neededSTREAM_API_KEY=insert_your_keySTREAM_API_SECRET=insert_your_secretOPENAI_API_KEY=insert_your_keyOPENWEATHER_API_KEY=not_needed |
### 4. Switch the Backend To Use OpenAI
By default, the backend uses Anthropic. To switch to OpenAI, find this route in `index.ts`
or `app.ts`
:

123456 |
app.post('/start-ai-agent', async (req, res) => { const { channel_id, channel_type = 'messaging', platform = 'openai', } = req.body; |
Ensure `platform = 'openai'`
.
### 5. Start the Server
Now the backend can run locally:

`yarn dev`
This will start the server on `http://localhost:3000`
by default. The frontend will call this server when it needs to add the AI bot to a chat channel.

Next, wire this up in the frontend so the AI joins automatically when a new user opens the chat.

## Checking if AI Is in the Chat
To ensure the AI agent automatically joins the chat when needed, create a custom React hook to monitor the channel’s watchers and check whether the AI bot is present. If not, trigger the backend to add it.

### 1. Create a `useWatchers`
Hook
Create a new file at `frontend/src/custom-hooks/useWatchers.ts`
:

12345678910111213141516171819202122232425262728293031323334353637383940414243444546474849505152535455 |
import { useCallback, useEffect, useState } from "react";import { Channel } from "stream-chat";export const useWatchers = ({ channel }: { channel: Channel }) => { const [watchers, setWatchers] = useState<string[] | undefined>(undefined); const [loading, setLoading] = useState(false); const [error, setError] = useState<Error | null>(null); const queryWatchers = useCallback(async () => { setLoading(true); setError(null); try { const result = await channel.query({ watchers: { limit: 5, offset: 0 } }); setWatchers(result?.watchers?.map((watcher) => watcher.id)); setLoading(false); return; } catch (err) { console.error("An error has occurred while querying watchers: ", err); setError(err as Error); } }, [channel]); useEffect(() => { queryWatchers(); }, [queryWatchers]); useEffect(() => { const watchingStartListener = channel.on("user.watching.start", (event) => { const userId = event?.user?.id; if (userId && userId.startsWith("ai-bot")) { setWatchers((prevWatchers) => [ userId, ...(prevWatchers || []).filter((watcherId) => watcherId !== userId), ]); } }); const watchingStopListener = channel.on("user.watching.stop", (event) => { const userId = event?.user?.id; if (userId && userId.startsWith("ai-bot")) { setWatchers((prevWatchers) => (prevWatchers || []).filter((watcherId) => watcherId !== userId) ); } }); return () => { watchingStartListener.unsubscribe(); watchingStopListener.unsubscribe(); }; }, [channel]); return { watchers, loading, error };}; |
### 2. Create a Custom Channel Header
Now create a new channel header that checks whether the AI is in the channel, and if not, calls the backend to add it.

123456789101112131415161718192021222324252627282930313233343536373839404142434445 |
import { useChannelStateContext } from "stream-chat-react";import { useWatchers } from "../../custom-hooks/useWatchers";import { useEffect } from "react";export default function MyChannelHeader() { const { channel } = useChannelStateContext(); const { watchers } = useWatchers({ channel }); const aiInChannel = (watchers ?? []).filter((watcher) => watcher.includes("ai-bot")).length > 0; useEffect(() => { const addAIAgent = async () => { if (!channel || aiInChannel) return; const endpoint = "start-ai-agent"; await fetch(`http://127.0.0.1:3000/${endpoint}`, { method: "POST", headers: { "Content-Type": "application/json" }, body: JSON.stringify({ channel_id: channel.id }), }); }; addAIAgent(); }, [aiInChannel, channel]); return ( <div className="my-channel-header"> <h2>AI Assistant</h2> {aiInChannel ? ( <span style={{ fontSize: 12, color: "gray" }}> I'm Stream's AI helper! </span> ) : ( <span style={{ fontSize: 14, color: "red" }}>Not connected to AI</span> )} </div> );} |
### 3. Update AIChat.tsx
In `AIChat.tsx`
, replace the default `ChannelHeader`
with the new one:

123456 |
<Window> <MyChannelHeader /> // Add this <MessageList /> <AIStateIndicator /> <MessageInput /></Window> |
Now, whenever a user opens the chat, the app checks whether the AI agent is present. If not, it calls the backend and automatically invites the AI into the chat channel.
Let’s test things out:

![](https://cdn.thenewstack.io/media/2025/05/2eb55610-image6b-300x252.png)
Image 6

Amazing — an AI chat!

However, this wasn’t the end goal. To do yet:

- Make this actually look like an AI assistant.
- Teach the AI assistant about our company and instruct it on how to respond to users’ messages so it actually addresses users’ questions and problems.
First, to address styling…

## Styling Our Chat Assistant
A button in the bottom right corner of each page of our website will open AI chat when clicked.

First, create the button that will toggle the chat display:

123456789101112131415 |
import classes from "./AIChat.module.css";interface Props { onClick: () => void; showAIChat: boolean;}const ToggleAIChatButton = ({ onClick, showAIChat }: Props) => { return ( <button onClick={onClick} className={classes.toggleAIChatButton}> {showAIChat ? "⏷" : "💬"} </button> );};export default ToggleAIChatButton; |
Add the css to `AIChat/AIChat.module.css`
:
123456789101112131415161718192021 |
.toggleAIChatButton { position: absolute; bottom: 20px; right: 20px; width: 60px; height: 60px; background: black; color: white; border-radius: 50%; font-size: 20px; cursor: pointer; border: none; display: flex; align-items: center; justify-content: center; transition: background 0.3s;}.toggleAIChatButton:hover { background: #333;} |
Now [create a new component](https://thenewstack.io/genai-helps-frontend-developers-create-components/), at `src/components/AIChat/AIChatWidget.tsx`
, to conditionally display the AI chat:
12345678910111213141516171819202122232425 |
import { useState } from "react";import AIChat from "./AIChat";import ToggleAIChatButton from "./ToggleAIChatButton";import classes from "./AIChat.module.css";const AIChatWidget = () => { const [showAIChat, setShowAIChat] = useState(false); const toggleAIChat = () => { setShowAIChat((prev) => !prev); }; return ( <div> <div className={`${classes.chatPanel} ${!showAIChat ? classes.hidden : ""}`} > <AIChat /> </div> <ToggleAIChatButton onClick={toggleAIChat} showAIChat={showAIChat} /> </div> );};export default AIChatWidget; |
Add the following classes to `AIChat.module.css`
:
123456789101112 |
.chatPanel { position: absolute !important; bottom: 60px !important; right: 0 !important; height: 400px !important; min-width: 320px !important; max-width: 500px !important;}.hidden { display: none;} |
![](https://cdn.thenewstack.io/media/2025/05/300dff68-image7a-150x150.png)
Image 7

Now there’s a button at the bottom of each page.

When clicked, it toggles the AI chat.

Great! Things are looking better. But this is still just some generic AI chat, like ChatGPT. We want it to respond as though it is an expert for Stream.

## Instructing AI To Be a Stream Expert
Go to your
in the backend, change the assistant’s name and instruct it on how to behave:[OpenAIAgent.ts](http://openaiagent.ts)

12345678910111213141516171819202122232425262728 |
this.assistant = await this.openai.beta.assistants.create({ name: 'Stream AI Assistant', instructions: ` You are a helpful, professional AI assistant for Stream.io, a company providing scalable APIs and SDKs for building in-app chat, video, and activity feeds. Assist users by answering their questions clearly and accurately. If users ask about any of the following, respond with the corresponding information: Support or contacting a human: Direct them to https://getstream.io/contact/support/ Help Center or documentation lookup: Point them to https://support.getstream.io/hc/en-us Pricing details: Guide them to https://getstream.io/chat/pricing/ Company/team info: Refer them to https://getstream.io/team/ Documentation-specific queries: Chat API/docs: https://getstream.io/chat/docs/ Video & audio docs: https://getstream.io/video/docs Activity Feed docs: https://getstream.io/activity-feeds/docs Moderation docs: https://getstream.io/moderation/docs For anything related to configuring Stream, accessing API keys, managing users, teams, or billing, direct users to https://dashboard.getstream.io/ If you're unsure or the topic is not covered, say: "I'm not certain about that, but I recommend reaching out to our support team." Keep your responses friendly, accurate, and focused on helping users efficiently navigate GetStream.io's tools and resources.` |
Restart the server with `yarn dev`
, and let’s see what happens:
![](https://cdn.thenewstack.io/media/2025/05/316a9790-image9b-300x269.png)
Image 8

And just like that, Stream has an AI assistant.

![](https://cdn.thenewstack.io/media/2025/05/625b4593-image10.gif)
**Conclusion**
You now have a working example that handles guest users, manages chat channels and connects to an AI backend.

With this foundation, you can bring your own AI assistant to life and embed intelligent conversations directly into your website.

[
YOUTUBE.COM/THENEWSTACK
Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.
](https://youtube.com/thenewstack?sub_confirmation=1)