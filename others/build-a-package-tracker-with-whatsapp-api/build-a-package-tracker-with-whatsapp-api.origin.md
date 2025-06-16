# Build a Package Tracker With WhatsApp API
![Featued image for: Build a Package Tracker With WhatsApp API](https://cdn.thenewstack.io/media/2025/06/f3827f22-t-shirt-1024x576.jpg)
Customers expect fast, transparent updates about their orders. Think shipping status, delays, delivery confirmations and more.

The WhatsApp Business App makes it easy to communicate with your customers through features like catalogs, payments and quick replies. This is helpful for small businesses.

But once your business grows, the app starts falling short:

**The WhatsApp Business App is designed for individual use.**As the volume of ordered items grows and customer inquiries and conversations increase, it becomes unmanageable for a single person. While you can link your WhatsApp Business Account to multiple devices, that isn’t also scalable as you don’t have control over the actions staff members decide to take on your account. Not to mention that interactions will still be manual.**The app doesn’t have automation features for operations**such as automatically sending shipping addresses and delivery notifications.**There’s no centralized view**to track customers’ packages and interactions.
That’s where the WhatsApp Business Platform Cloud API comes in. It lets you integrate WhatsApp directly into your existing business system. And when paired with [Stream Chat](https://getstream.io/chat/), you get a powerful tool for real-time customer support, order tracking and automation.

In this tutorial, you will learn how to build a complete package tracker using WhatsApp Cloud API and Stream Chat.

## Prerequisite
To follow along, you need:

- A free
[Stream account](https://getstream.io/try-for-free/). - A
[WhatsApp Business Platform account](https://developers.facebook.com/docs/whatsapp/). We’ll work through setting this up in the next section. - Node ≥ v20.11.1 and npm ≥ v10.5
## Setting up Your WhatsApp Platform Account
Follow the steps below to set up your WhatsApp Platform Account. This account will allow us to integrate with WhatsApp via the Cloud API.

- Create a
[Meta for Developers account](https://developers.facebook.com/async/registration). - Create your app.
- Specify what you want your app to do.
- Select an app type. In our case, let’s select
**“Business.”**That gives us permission to use the WhatsApp Cloud API. - Add an app name.
Next, add the WhatsApp product to your app. It’s the only one you need for this tutorial.
Follow the next prompt to complete the setup.
- Select “
**Start using the API**” to get your API key.
- WhatsApp gives you a temporary access token that expires every 24 hours and a test phone number for development purposes. When you are ready to deploy to production, you can get a permanent access token and use your phone number.
## Setting Up a Webhooks Endpoint
Next, let’s set up a webhooks endpoint in Node.js (Express).

`routes/webhook.js`
123456789101112131415161718192021222324252627282930313233343536373839404142434445464748495051525354555657585960616263 |
const express = require("express");const webhook = express .Router() .use(express.json(), express.urlencoded({ extended: false }));webhook.post("/webhook", async (req, res) => { // Check the Incoming webhook message if (req.body.object) { if ( req.body.entry && req.body.entry[0].changes && req.body.entry[0].changes[0] && req.body.entry[0].changes[0].value.messages && req.body.entry[0].changes[0].value.messages[0] ) { let from = req.body.entry[0].changes[0].value.messages[0].from; // extract the phone number from the webhook payload const msg_type = req.body.entry[0].changes[0].value.messages[0].type; // extract the message type res.sendStatus(200); } else { // Return a '404 Not Found' if event is not from a WhatsApp API res.sendStatus(404); }}});// Accepts GET requests at the /webhook endpoint. You need this URL to set up webhook initially.webhook.get("/webhook", (req, res) => { /** * UPDATE YOUR VERIFY TOKEN *This will be the Verify Token value when you set up webhook **/ const verify_token = process.env.VERIFY_TOKEN; // Parse params from the webhook verification request let mode = req.query["hub.mode"]; let token = req.query["hub.verify_token"]; let challenge = req.query["hub.challenge"]; // Check if a token and mode were sent if (mode && token) { // Check the mode and token sent are correct if (mode === "subscribe" && token === verify_token) { // Respond with 200 OK and challenge token from the request //console.log("WEBHOOK_VERIFIED"); res.status(200).send(challenge); } else { // Responds with '403 Forbidden' if verify tokens do not match res.sendStatus(403); } }});module.exports = webhook; |
In the code above, check the incoming webhook message and extract the phone number (`from`
) and message type (`msg_type`
). The `GET`
endpoint sets up the webhook using the value of `verify_token`
. Add this value to the WhatsApp webhook configuration page to complete the webhook setup.
This is what the .env file looks like.

`.env`
1234 |
VERIFY_TOKEN=writeanyvalueyouwantWHATSAPP_TOKEN=EAARNGxxxxxWHATSAPP_PHONE_ID=xxxxxxxxxSTREAM_SECRET=yourstreamsecret |
Complete setup by adding the value of `verify_token`
and the callback URL (your server’s URL) to the WhatsApp Cloud API webhook page in the Meta Developer Portal.
WhatsApp will send webhook events to the server as long as it is HTTPS and has a valid SSL certificate. Subscribe to the
webhook field. We need only this field.**messages**

## Showcasing Products on WhatsApp Business
When a customer chats with our WhatsApp Business number, we want to send them the list of products for sale.

Customers get a list of available products when they send “#product” in the chat.

`routes/webhook.js`
12345678910111213141516171819202122232425262728293031323334353637383940414243 |
const express = require("express");const webhook = express .Router() .use(express.json(), express.urlencoded({ extended: false }));const {StreamChat} = require("stream-chat")const { sendUserAMessage, sendInteractiveProductMessage } = require("../utils")webhook.post("/webhook", async (req, res) => { // Check the Incoming webhook message if (req.body.object) { if ( req.body.entry && req.body.entry[0].changes && req.body.entry[0].changes[0] && req.body.entry[0].changes[0].value.messages && req.body.entry[0].changes[0].value.messages[0] ) { let from = req.body.entry[0].changes[0].value.messages[0].from; // extract the phone number from the webhook payload const msg_type = req.body.entry[0].changes[0].value.messages[0].type; if(msg_body.toLowerCase().trim() === "#product"){ sendInteractiveProductMessage(from) } res.sendStatus(200); } else { // Return a '404 Not Found' if event is not from a WhatsApp API res.sendStatus(404); }}});module.exports = webhook; |
If the chat value is `#product`
, we automatically send the customer an interactive message with a list of our products through the `sendInteractiveProductMessage`
function. Let’s create the `sendInteractiveProductMessage`
and `sendUserAMessage`
functions inside another file.
`utils.js`
12345678910111213141516171819202122232425262728293031323334353637383940414243444546474849505152535455565758596061626364656667686970717273747576777879808182838485868788 |
const axios = require("axios");const whatsappToken = process.env.WHATSAPP_TOKEN;const business_phone_id = process.env.WHATSAPP_PHONE_ID;const sendUserAMessage = (phone, message) => { axios ({ method: "POST", url: `https://graph.facebook.com/v22.0/${business_phone_id}/messages?access_token=${whatsappToken}`, data: { messaging_product: "whatsapp", to: phone, text: {body: `${message}`} }, headers: {"Content-Type": "application/json"} });}const sendInteractiveProductMessage = (phone) => { axios ({ method: "POST", url: `https://graph.facebook.com/v22.0/${business_phone_id}/messages?access_token=${whatsappToken}`, data: { messaging_product: "whatsapp", to: phone, type: "interactive", interactive: { type: "list", header: { type: "text", text: "Select a Product to Purchase" }, body: { text: "What would you like to shop from us today?" }, footer: { text: "Discount: 6% discount on all our products today. Shop now!TM" }, action: { button: "Shop Now!", sections: [ { title: "Shirts", rows: [ { id: "t-shirt-0001", title: "Plain T-Shirt", description: "Size: Large" }, { id: "sleeveless-001", title: "Sleeveless", description: "Size: Medium" } ] }, { title: "Caps", rows: [ { id: "base-cap-xl", title: "Baseball Cap", description: "Unisex cap (delivery in 2 days)" }, { id: "br-xxl", title: "Beret", description: "Unisex" } ] } ] } } }, headers: {"Content-Type": "application/json"} });}module.exports = { sendUserAMessage, sendInteractiveProductMessage } |
`SendInteractiveProductMessage`
sends an [interactive list](https://developers.facebook.com/docs/whatsapp/cloud-api/messages/interactive-list-messages) of products to the user. [Catalog templates](https://developers.facebook.com/docs/whatsapp/business-management-api/message-templates/catalog-templates/) are a far more effective way to share your products directly with customers within WhatsApp. However, we’ll use interactive list instead since we want to keep this tutorial focused on core integration.
`SendUserAMessage`
allows us to send plain text chats.
Next, we will prompt the customer to make a payment after choosing the product(s) they want to buy.

`routes/webhook.js`
123456789101112 |
const assignMsgVal = (type) => { let msg_body; if (type === "text") { msg_body = req.body.entry[0].changes[0].value.messages[0].text.body; } else if (type === "interactive" && req.body.entry[0].changes[0].value.messages[0].interactive.type === "list_reply") { msg_body = `${req.body.entry[0].changes[0].value.messages[0].interactive.list_reply.title}\n${req.body.entry[0].changes[0].value.messages[0].interactive.list_reply.description}` sendUserAMessage(from, `Make payment for the following item\n${msg_body}\nclick https://test.payment.com to make your payment.`) } return msg_body; }; |
Here, we verified the message type sent from the WhatsApp Cloud API webhooks to determine our next action: sending a payment request to the customer for the purchased products.
## Tracking Ordered Items on Stream Chat
It’s important to track ordered items and communicate with customers from a central hub outside WhatsApp. Stream Chat enables you to consolidate all your customer conversations from WhatsApp into Stream Chat, allowing you and your team to track purchases and engage with customers without needing to use the WhatsApp app.

### Create a Channel
Create a Stream channel right inside the webhook.js file.

`routes/`
[webhook.js](http://webhook.js)
123456789101112131415161718192021222324252627 |
//…const {StreamChat} = require("stream-chat");const chatServer = StreamChat.getInstance( process.env.STREAM_KEY, process.env.STREAM_SECRET)webhook.post("/webhook", async (req, res) => { //... //create users await chatServer.upsertUsers([ {id: from, name: "customer", role: "user"}, {id:"businessowner", name: "business", role: "admin"} ]) //create channel and users to the channel const channel = chatServer.channel("messaging", "order_tracking", { name: "Order Tracker", members: [from, "businessowner"], created_by_id: from, }); await channel.create() //...}); |
When a customer sends a message to our WhatsApp business line, we immediately add them as a Stream user, create an `order_tracking`
channel, and add both the customer and business to the channel.
### Send Message as Customer
In addition to creating a user in Stream and adding that user to a channel, we also want to send every chat the customer sends to our WhatsApp Business number to Stream Chat.

`routes/webhook.js`
1234567891011121314 |
//…webhook.post("/webhook", async (req, res) => { //... const message = { text: msg_body, reply_number: from, user_id: from }; await channel.sendMessage(message); //...}); |
Chats (`msg_body`
) from customers received through the WhatsApp message hook are sent to Stream Chat. Each message includes a custom `reply_number`
value, which identifies the customer’s phone number so the business can reply directly from Stream Chat.
Before building the UI of our package tracker, set up the authorization route.

`routes/auth.js`
1234567891011121314151617181920212223 |
const express = require('express');const auth = express.Router();const { StreamChat } = require('stream-chat')const chatServer = StreamChat.getInstance( process.env.STREAM_KEY, process.env.STREAM_SECRET )auth.post("/auth", async (req, res) => { const { businessId } = await req.body; try { const token = chatServer.createToken(businessId); res.json({ token }) } catch (error) { res.status(500).json({error: error}) }});module.exports = auth;Building the Stream Chat UI |
Build the Chat UI to see and respond to customers’ messages and orders.
Create a `Chat.jsx`
in your React application.

`Chat.jsx`
1234567891011121314151617181920212223242526272829303132333435363738394041424344454647484950515253545556575859606162636465666768697071727374757677787980818283848586878889909192939495969798 |
import React, {useState, useEffect, useCallback} from 'react';import {Channel, ChannelHeader, MessageList, MessageInput, Window, Chat, useChannelActionContext } from 'stream-chat-react';import { StreamChat } from 'stream-chat';const chatClient = StreamChat.getInstance(import.meta.env.VITE_STREAM_KEY);const CustomMessageInput = () => { const { sendMessage } = useChannelActionContext(); const submitHandler = async (params) => { const { localMessage, message, sendOptions } = params; try { // Send the message using the provided sendMessage function await sendMessage({ localMessage, message, options: sendOptions }); const phoneNumber = localStorage.getItem("phoneNumber"); await fetch("https://yourserverurl.com/response", { method: 'POST', headers: { 'Content-Type': 'application/json', }, body: JSON.stringify({chat: message.text, phoneNumber }) }); } catch (error) { console.error('Error sending message:', error); } } return ( <div className='relative'> <MessageInput overrideSubmitHandler={submitHandler} /> </div> );}export default function ChatComponent() { const [channel, setChannel] = useState(null); const businessId = "businessowner" useEffect(() => { const initialize = async () => { try{ const getToken = await fetch("https://yourserverurl.com/auth", { method: 'POST', headers: { 'Content-Type': 'application/json', }, body: JSON.stringify({businessId}) }); const { token } = await getToken.json() await chatClient.connectUser({id: businessId}, token) //join the order_tracking channel created in the backend const channel = chatClient.channel("messaging", "order_tracking"); await channel.watch() setChannel(channel); channel.on("message.new", (event) => { if(event.user.name.toLowerCase() === "customer"){ localStorage.setItem("phoneNumber", event.message.reply_number); } }); } catch (error) { console.error("Chat initialization error", error); } } initialize() }, []) return ( <div> <Chat client={chatClient}> <Channel channel={channel}> <Window> <ChannelHeader /> <MessageList /> <CustomMessageInput /> </Window> </Channel> </Chat> </div> )} |
The `CustomMessageInput`
component has a `submitHandler`
function that sends chats from the business to the customer’s WhatsApp. We’ll create a `response.js`
route in our backend shortly to handle communication from the company (package tracker UI) to the customer’s WhatsApp.
The business is authenticated to join the `order_tracking`
channel when the component mounts. We are also listening for new messages from customers. When a new message from a customer comes in, extract the WhatsApp phone number (`reply_number`
) and store it in localStorage. (For production apps, you should store this in your database.) The business uses this phone number inside the `submitHandler`
function to send back messages to the customer’s WhatsApp.

Create the `response`
route in the backend:

`routes/response.js`
1234567891011 |
const express = require ("express");const response = express.Router();const { sendUserAMessage } = require("../utils")response.post("/response", (req, res) => { const {chat, phoneNumber } = req.body; sendUserAMessage(phoneNumber, chat)});module.exports = response; |
Remember to add the `ChatComponent`
to the main page:
`App.jsx`
12345678910 |
import './App.css';import "stream-chat-react/dist/css/v2/index.css";import ChatComponent from './Chat';function App() { return <ChatComponent />}export default App |
## Chat Between Customers and Business
Our package tracker application is ready. Let’s test it out:

- Text
`#product`
to the test phone number provided by WhatsApp.
- The customer will immediately get a list of available products to shop.

- Once they choose, they receive a payment link to complete the purchase.
- They can chat with the business at any time.
-
- The business receives WhatsApp conversations in the package tracker UI.
- You can send the customer a response from the business’s package tracker UI, and they’ll receive it in their WhatsApp.
Chat

## Conclusion
With Stream Chat and WhatsApp Business Cloud API, you can build a package tracker that showcases products, collects payments, resolves issues, sends delivery updates and keeps customers informed — all in one place.

Stream empowers you to build communication apps and is flexible enough to integrate with your existing business tools to better serve your customers.


[
YOUTUBE.COM/THENEWSTACK
Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.
](https://youtube.com/thenewstack?sub_confirmation=1)