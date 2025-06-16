
<!--
title: 使用WhatsApp API构建一个包裹追踪器
cover: https://cdn.thenewstack.io/media/2025/06/f3827f22-t-shirt.jpg
summary: 用 WhatsApp Cloud API + Stream Chat，轻松打造爆款包裹追踪器！对接 WhatsApp Business Platform，实现订单状态、物流通知自动化。Node.js 建 Webhooks，集成产品目录，Stream Chat 集中管理客户对话，赋能 AI 实时客服，提升用户体验！
-->

用 WhatsApp Cloud API + Stream Chat，轻松打造爆款包裹追踪器！对接 WhatsApp Business Platform，实现订单状态、物流通知自动化。Node.js 建 Webhooks，集成产品目录，Stream Chat 集中管理客户对话，赋能 AI 实时客服，提升用户体验！

> 译自：[Build a Package Tracker With WhatsApp API](https://thenewstack.io/build-a-package-tracker-with-whatsapp-api/)
> 
> 作者：Emmanuel Aiyenigba

客户希望快速、透明地了解其订单的最新状态。例如，运输状态、延误、交货确认等。

WhatsApp Business App 通过目录、付款和快速回复等功能，可以轻松地与客户沟通。这对小型企业很有帮助。

但是，一旦您的业务增长，该应用程序就会开始出现不足：

- **WhatsApp Business App 专为个人使用而设计。** 随着订购商品数量的增长以及客户咨询和对话的增加，单个人员将变得难以管理。虽然您可以将您的 WhatsApp Business 帐户链接到多个设备，但这也不是可扩展的，因为您无法控制员工决定对您的帐户执行的操作。更不用说交互仍然是手动的。
- **该应用程序没有用于运营的自动化功能，** 例如自动发送送货地址和交货通知。
- **没有集中的视图**来跟踪客户的包裹和互动。

这就是 WhatsApp Business Platform Cloud API 的用武之地。它允许您将 WhatsApp 直接集成到您现有的业务系统中。当与 [Stream Chat](https://getstream.io/chat/) 结合使用时，您将获得一个强大的工具，用于实时客户支持、订单跟踪和自动化。

在本教程中，您将学习如何使用 WhatsApp Cloud API 和 Stream Chat 构建一个完整的包裹追踪器。

## 前提条件

要继续学习，您需要：

- 一个免费的 [Stream account](https://getstream.io/try-for-free/)。
- 一个 [WhatsApp Business Platform account](https://developers.facebook.com/docs/whatsapp/)。我们将在下一节中完成此设置。
- Node ≥ v20.11.1 和 npm ≥ v10.5

## 设置您的 WhatsApp 平台帐户

按照以下步骤设置您的 WhatsApp 平台帐户。此帐户将允许我们通过 Cloud API 与 WhatsApp 集成。

- 创建一个 [Meta for Developers account](https://developers.facebook.com/async/registration)。
- 创建您的应用。
- 指定您希望您的应用执行的操作。
- 选择一个应用类型。在我们的例子中，让我们选择 **“Business”**。这使我们有权使用 WhatsApp Cloud API。
- 添加一个应用名称。

接下来，将 WhatsApp 产品添加到您的应用。这是本教程中您唯一需要的产品。
按照下一个提示完成设置。

- 选择“**Start using the API**”以获取您的 API 密钥。
- WhatsApp 为您提供一个每 24 小时过期的临时访问令牌和一个用于开发目的的测试电话号码。当您准备好部署到生产环境时，您可以获得永久访问令牌并使用您的电话号码。

## 设置 Webhooks 端点

接下来，让我们在 Node.js (Express) 中设置一个 webhooks 端点。

`routes/webhook.js`

```javascript
const express = require("express");
const webhook = express
  .Router()
  .use(express.json(), express.urlencoded({ extended: false }));

webhook.post("/webhook", async (req, res) => {
  // Check the Incoming webhook message
  if (req.body.object) {
    if (
      req.body.entry &&
      req.body.entry[0].changes &&
      req.body.entry[0].changes[0] &&
      req.body.entry[0].changes[0].value.messages &&
      req.body.entry[0].changes[0].value.messages[0]
    ) {
      let from = req.body.entry[0].changes[0].value.messages[0].from; // extract the phone number from the webhook payload
      const msg_type = req.body.entry[0].changes[0].value.messages[0].type; // extract the message type
      res.sendStatus(200);
    } else {
      // Return a '404 Not Found' if event is not from a WhatsApp API
      res.sendStatus(404);
    }
  }
});

// Accepts GET requests at the /webhook endpoint. You need this URL to set up webhook initially.
webhook.get("/webhook", (req, res) => {
  /**
   * UPDATE YOUR VERIFY TOKEN
   *This will be the Verify Token value when you set up webhook
   **/
  const verify_token = process.env.VERIFY_TOKEN;

  // Parse params from the webhook verification request
  let mode = req.query["hub.mode"];
  let token = req.query["hub.verify_token"];
  let challenge = req.query["hub.challenge"];

  // Check if a token and mode were sent
  if (mode && token) {
    // Check the mode and token sent are correct
    if (mode === "subscribe" && token === verify_token) {
      // Respond with 200 OK and challenge token from the request
      //console.log("WEBHOOK_VERIFIED");
      res.status(200).send(challenge);
    } else {
      // Responds with '403 Forbidden' if verify tokens do not match
      res.sendStatus(403);
    }
  }
});

module.exports = webhook;
```

在上面的代码中，检查传入的 webhook 消息并提取电话号码 (`from`) 和消息类型 (`msg_type`)。`GET` 端点使用 `verify_token` 的值设置 webhook。将此值添加到 WhatsApp webhook 配置页面以完成 webhook 设置。
这就是 .env 文件的样子。

`.env`

```
###
```

`VERIFY_TOKEN=writeanyvalueyouwantWHATSAPP_TOKEN=EAARNGxxxxxWHATSAPP_PHONE_ID=xxxxxxxxxSTREAM_SECRET=yourstreamsecret`

通过将 `verify_token` 的值和回调 URL（你的服务器 URL）添加到 Meta 开发者门户的 WhatsApp Cloud API webhook 页面来完成设置。只要服务器是 HTTPS 并且具有有效的 SSL 证书，WhatsApp 就会将 webhook 事件发送到服务器。订阅 webhook 字段。我们只需要这个字段：**messages**

## 在 WhatsApp Business 上展示产品

当客户与我们的 WhatsApp Business 号码聊天时，我们希望向他们发送待售产品列表。

当客户在聊天中发送“#product”时，他们会收到可用产品列表。

`routes/webhook.js`

```javascript
const express = require("express");
const webhook = express
  .Router()
  .use(express.json(), express.urlencoded({ extended: false }));
const { StreamChat } = require("stream-chat");
const { sendUserAMessage, sendInteractiveProductMessage } = require("../utils");

webhook.post("/webhook", async (req, res) => {
  // Check the Incoming webhook message
  if (req.body.object) {
    if (
      req.body.entry &&
      req.body.entry[0].changes &&
      req.body.entry[0].changes[0] &&
      req.body.entry[0].changes[0].value.messages &&
      req.body.entry[0].changes[0].value.messages[0]
    ) {
      let from = req.body.entry[0].changes[0].value.messages[0].from; // extract the phone number from the webhook payload
      const msg_type = req.body.entry[0].changes[0].value.messages[0].type;
      if (msg_body.toLowerCase().trim() === "#product") {
        sendInteractiveProductMessage(from);
      }
      res.sendStatus(200);
    } else {
      // Return a '404 Not Found' if event is not from a WhatsApp API
      res.sendStatus(404);
    }
  }
});

module.exports = webhook;
```

如果聊天值为“#product”，我们会通过 `sendInteractiveProductMessage` 函数自动向客户发送包含我们产品列表的互动消息。让我们在另一个文件中创建 `sendInteractiveProductMessage` 和 `sendUserAMessage` 函数。

`utils.js`

```javascript
const axios = require("axios");
const whatsappToken = process.env.WHATSAPP_TOKEN;
const business_phone_id = process.env.WHATSAPP_PHONE_ID;

const sendUserAMessage = (phone, message) => {
  axios({
    method: "POST",
    url: `https://graph.facebook.com/v22.0/${business_phone_id}/messages?access_token=${whatsappToken}`,
    data: {
      messaging_product: "whatsapp",
      to: phone,
      text: { body: `${message}` },
    },
    headers: { "Content-Type": "application/json" },
  });
};

const sendInteractiveProductMessage = (phone) => {
  axios({
    method: "POST",
    url: `https://graph.facebook.com/v22.0/${business_phone_id}/messages?access_token=${whatsappToken}`,
    data: {
      messaging_product: "whatsapp",
      to: phone,
      type: "interactive",
      interactive: {
        type: "list",
        header: {
          type: "text",
          text: "Select a Product to Purchase",
        },
        body: {
          text: "What would you like to shop from us today?",
        },
        footer: {
          text: "Discount: 6% discount on all our products today. Shop now!TM",
        },
        action: {
          button: "Shop Now!",
          sections: [
            {
              title: "Shirts",
              rows: [
                {
                  id: "t-shirt-0001",
                  title: "Plain T-Shirt",
                  description: "Size: Large",
                },
                {
                  id: "sleeveless-001",
                  title: "Sleeveless",
                  description: "Size: Medium",
                },
              ],
            },
            {
              title: "Caps",
              rows: [
                {
                  id: "base-cap-xl",
                  title: "Baseball Cap",
                  description: "Unisex cap (delivery in 2 days)",
                },
                {
                  id: "br-xxl",
                  title: "Beret",
                  description: "Unisex",
                },
              ],
            },
          ],
        },
      },
    },
    headers: { "Content-Type": "application/json" },
  });
};

module.exports = { sendUserAMessage, sendInteractiveProductMessage };
```

`SendInteractiveProductMessage` 向用户发送产品的[互动列表](https://developers.facebook.com/docs/whatsapp/cloud-api/messages/interactive-list-messages)。[目录模板](https://developers.facebook.com/docs/whatsapp/business-management-api/message-templates/catalog-templates/)是一种更有效的方式，可以直接在 WhatsApp 中与客户分享您的产品。但是，我们将使用互动列表，因为我们希望本教程侧重于核心集成。

`SendUserAMessage` 允许我们发送纯文本聊天。

接下来，我们将提示客户在选择他们想要购买的产品后付款。

`routes/webhook.js`

```javascript
const assignMsgVal = (type) => {
  let msg_body;
  if (type === "text") {
    msg_body = req.body.entry[0].changes[0].value.messages[0].text.body;
  } else if (
    type === "interactive" &&
    req.body.entry[0].changes[0].value.messages[0].interactive.type ===
      "list_reply"
  ) {
    msg_body = `${req.body.entry[0].changes[0].value.messages[0].interactive.list_reply.title}\n${req.body.entry[0].changes[0].value.messages[0].interactive.list_reply.description}`;
    sendUserAMessage(
      from,
      `Make payment for the following item\n${msg_body}\nclick https://test.payment.com to make your payment.`
    );
  }
  return msg_body;
};

在这里，我们验证了从 WhatsApp Cloud API webhook 发送的消息类型，以确定我们的下一步操作：向客户发送购买产品的付款请求。

## 在 Stream Chat 上跟踪订购的商品

跟踪订购的商品并从 WhatsApp 外部的中央枢纽与客户沟通非常重要。Stream Chat 使您可以将来自 WhatsApp 的所有客户对话整合到 Stream Chat 中，使您和您的团队无需使用 WhatsApp 应用程序即可跟踪购买情况并与客户互动。

### 创建频道

在 `webhook.js` 文件中直接创建一个 Stream 频道。

`routes/webhook.js`

```javascript
//…
const {StreamChat} = require("stream-chat");
const chatServer = StreamChat.getInstance(
  process.env.STREAM_KEY,
  process.env.STREAM_SECRET
)

webhook.post("/webhook", async (req, res) => {
  //...
  //create users
  await chatServer.upsertUsers([
    {id: from, name: "customer", role: "user"},
    {id:"businessowner", name: "business", role: "admin"}
  ])

  //create channel and users to the channel
  const channel = chatServer.channel("messaging", "order_tracking", {
    name: "Order Tracker",
    members: [from, "businessowner"],
    created_by_id: from,
  });
  await channel.create()
  //...
});
```

当客户向我们的 WhatsApp 商业专线发送消息时，我们会立即将他们添加为 Stream 用户，创建一个 `order_tracking` 频道，并将客户和商家都添加到该频道。

### 以客户身份发送消息

除了在 Stream 中创建用户并将该用户添加到频道之外，我们还希望将客户发送到我们的 WhatsApp Business 号码的每条聊天消息都发送到 Stream Chat。

`routes/webhook.js`

```javascript
//…
webhook.post("/webhook", async (req, res) => {
  //...
  const message = {
    text: msg_body,
    reply_number: from,
    user_id: from
  };
  await channel.sendMessage(message);
  //...
});
```

通过 WhatsApp 消息 hook 收到的来自客户的聊天消息（`msg_body`）被发送到 Stream Chat。每条消息都包含一个自定义的 `reply_number` 值，用于标识客户的电话号码，以便商家可以直接从 Stream Chat 回复。

在构建我们的包裹跟踪器的 UI 之前，请设置授权路由。

`routes/auth.js`

```javascript
const express = require('express');
const auth = express.Router();
const { StreamChat } = require('stream-chat')

const chatServer = StreamChat.getInstance(
  process.env.STREAM_KEY,
  process.env.STREAM_SECRET
)

auth.post("/auth", async (req, res) => {
  const { businessId } = await req.body;
  try {
    const token = chatServer.createToken(businessId);
    res.json({ token })
  } catch (error) {
    res.status(500).json({error: error})
  }
});

module.exports = auth;
```

构建聊天 UI 以查看和回复客户的消息和订单。
在您的 React 应用程序中创建一个 `Chat.jsx`。

`Chat.jsx`

```jsx

```

import React, {useState, useEffect, useCallback} from 'react';
import {Channel, ChannelHeader, MessageList, MessageInput, Window, Chat, useChannelActionContext } from 'stream-chat-react';
import { StreamChat } from 'stream-chat';

const chatClient = StreamChat.getInstance(import.meta.env.VITE_STREAM_KEY);

const CustomMessageInput = () => {
  const { sendMessage } = useChannelActionContext();

  const submitHandler = async (params) => {
    const { localMessage, message, sendOptions } = params;

    try {
      // Send the message using the provided sendMessage function
      await sendMessage({ localMessage, message, options: sendOptions });

      const phoneNumber = localStorage.getItem("phoneNumber");
      await fetch("https://yourserverurl.com/response", {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({chat: message.text, phoneNumber })
      });
    } catch (error) {
      console.error('Error sending message:', error);
    }
  }

  return (
    <div className='relative'>
      <MessageInput overrideSubmitHandler={submitHandler} />
    </div>
  );
}

export default function ChatComponent() {
  const [channel, setChannel] = useState(null);
  const businessId = "businessowner"

  useEffect(() => {
    const initialize = async () => {
      try{
        const getToken = await fetch("https://yourserverurl.com/auth", {
          method: 'POST',
          headers: {
            'Content-Type': 'application/json',
          },
          body: JSON.stringify({businessId})
        });

        const { token } = await getToken.json()
        await chatClient.connectUser({id: businessId}, token)

        //join the order_tracking channel created in the backend
        const channel = chatClient.channel("messaging", "order_tracking");
        await channel.watch()
        setChannel(channel);

        channel.on("message.new", (event) => {
          if(event.user.name.toLowerCase() === "customer"){
            localStorage.setItem("phoneNumber", event.message.reply_number);
          }
        });
      } catch (error) {
        console.error("Chat initialization error", error);
      }
    }

    initialize()
  }, [])

  return (
    <div>
      <Chat client={chatClient}>
        <Channel channel={channel}>
          <Window>
            <ChannelHeader />
            <MessageList />
            <CustomMessageInput />
          </Window>
        </Channel>
      </Chat>
    </div>
  )
}
```

`CustomMessageInput` 组件有一个 `submitHandler` 函数，用于将业务聊天发送到客户的 WhatsApp。我们稍后将在后端创建一个 `response.js` 路由，以处理公司（包裹追踪 UI）到客户 WhatsApp 的通信。

当组件挂载时，业务已通过身份验证以加入 `order_tracking` 频道。我们还在监听来自客户的新消息。当收到来自客户的新消息时，提取 WhatsApp 电话号码 (`reply_number`) 并将其存储在 localStorage 中。（对于生产应用程序，您应该将其存储在数据库中。）业务在 `submitHandler` 函数中使用此电话号码将消息发送回客户的 WhatsApp。

在后端创建 `response` 路由：

**routes/response.js**

```javascript
const express = require ("express");
const response = express.Router();
const { sendUserAMessage } = require("../utils")

response.post("/response", (req, res) => {
  const {chat, phoneNumber } = req.body;
  sendUserAMessage(phoneNumber, chat)
});

module.exports = response;
```

请记住将 `ChatComponent` 添加到主页：

**App.jsx**

```javascript
import './App.css';
import "stream-chat-react/dist/css/v2/index.css";
import ChatComponent from './Chat';

function App() {
  return <ChatComponent />
}

export default App
```

## 客户与企业之间的聊天

我们的包裹追踪应用程序已准备就绪。让我们测试一下：

- 将 `#product` 发送到 WhatsApp 提供的测试电话号码。
- 客户将立即获得可购买的可用产品列表。
- 一旦他们选择，他们将收到一个付款链接以完成购买。
- 他们可以随时与企业聊天。
- 企业会在包裹追踪 UI 中收到 WhatsApp 对话。
- 您可以从企业的包裹追踪 UI 向客户发送回复，他们将在 WhatsApp 中收到该回复。

## 结论

借助 Stream Chat 和 WhatsApp Business Cloud API，您可以构建一个包裹追踪器，该追踪器可以展示产品、收取付款、解决问题、发送交货更新并让客户随时了解情况——所有这些都在一个地方完成。

Stream 使您能够构建通信应用程序，并且足够灵活，可以与您现有的业务工具集成，从而更好地为您的客户提供服务。

[YOUTUBE.COM/THENEWSTACK](https://youtube.com/thenewstack?sub_confirmation=1)
技术发展迅速，不要错过任何一集。订阅我们的 YouTube 频道以流式传输我们所有的播客、访谈、演示等。