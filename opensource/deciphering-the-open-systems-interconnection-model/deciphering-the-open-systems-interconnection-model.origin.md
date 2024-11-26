# Deciphering the Open Systems Interconnection Model
![Featued image for: Deciphering the Open Systems Interconnection Model](https://cdn.thenewstack.io/media/2024/11/87712996-osi-1024x572.png)
Unless you’ve studied for a network cert, the Open Systems Interconnection (OSI) model is probably somewhat of a mystery to you. Maybe you heard of it from a coworker, or maybe you saw it in a marketing campaign for something on AWS.

Maybe you thought “Layer 3” was just some new buzzword. Such shorthand references to the [OSI model](https://thenewstack.io/the-osi-7-layer-model-can-help-define-enterprise-application-security/), however, can be useful if you can decode them, as they can help you understand where in your network stack a tool could fit or where to look for a problem during an incident call.

Before we get too far, let me address a point of contention. Many people will say the theoretical OSI model is outdated. The model is theoretical, true, and the real world is certainly more complex than it may lead you to believe. Its layers don’t neatly map to specific devices, and other models exist that more accurately reflect the real world, such as the Transmission Control Protocol/Internet Protocol (TCP/IP) model.

![](https://cdn.thenewstack.io/media/2024/11/c216fbd4-image1a-242x300.png)
Image 1

It’s useful to think of the OSI model as an abstraction that allows us to reason about the separation of concerns on a network. We use it to think through troubleshooting steps should our data not make it to its destination, and we use it to think through architecture needs as we build our distributed systems.

It’s not a theorem, with rigid boundaries and rules. It’s a theory of the sort we find in systems science: something that attempts to approximate the real world to help us understand it better.

## Layer Walk-Through
To understand the model, let’s follow data from your computer to another system and explore how it changes along the way. Say you are working on your computer and need to chat with a coworker. You pop over to your chat application and write a message. The data movement begins, and the OSI model comes into play the moment you send it. The top four layers of the model are called “host layers,” and since we’re on the host (your computer), that’s where we will begin this exercise.

![The host layers: Application, presentation, session, transport](https://cdn.thenewstack.io/media/2024/11/0ae01391-image2-1024x556.png)
The host layers

### The Host Layers
![Layer 7: Application](https://cdn.thenewstack.io/media/2024/11/7d9229ef-image3a-300x246.png)
Layer 7: Application

We start at Layer 7, the application layer. The “application” here doesn’t mean your chat app necessarily, but rather the implementation of the protocol it uses to send messages. That protocol might be WebSocket, for example. Other protocols at this layer are things like SMTP (Simple Mail Transfer Protocol) for your email app or HTTP (Hypertext Transfer Protocol) for your web browser. The application or API you work with accepts data using these protocols. In our case, your chat app implements the logic to take in the data you’re using and identify the right protocol for transmission.

![Layer 6: Presentation](https://cdn.thenewstack.io/media/2024/11/1f0b5790-image4a-300x248.png)
Layer 6: Presentation

Once your app has identified the right protocol, the data drops down to Layer 6, the presentation layer. At the presentation layer — which is still on your machine and may even be in the same app! — the data gets translated into the correct protocol. If you are sending a GIF, for example, the presentation layer takes the displayed format and encodes it for transmission over the network. Since we’re in a chat app, the chat is probably also billed as an encrypted communication. Data encryption happens at Layer 6 as well, as does compression, which is likely when you send an image.

![Layer 5: Session](https://cdn.thenewstack.io/media/2024/11/dab487fd-image5a-300x248.png)
Layer 5: Session

We then drop to Layer 5, the session layer. (We’re still on your computer.) If you just opened your chat app, you probably had to log in. Layer 5 is where we open a session and authenticate. If you’ve developed or maintained an application with login or auth needs, you’re likely familiar with user sessions. A video or an audio conference app opens a session when starting a call and closes it when terminating the call. In this case, as you logged into the app, it set up and sent the first in a sequence of calls and responses to establish the connection. Depending on the app’s architecture, another session may open as you send the DM with your coworker.

![Layer 4: Transport](https://cdn.thenewstack.io/media/2024/11/166bcc53-image6a-300x246.png)
Layer 4: Transport

Note that we’ve reached Layer 4 and still haven’t left the host! No data has left your computer in this abstracted world, and it’s still just a lump of data with no particular direction. That’s about to change. Layer 4, the transport layer, is the last layer in the host. This is where data starts to get packaged and prepped for transmission. The formal term for this packaging is “encapsulation.” (On the receiving end, when data moves from a lower layer to a higher one, it goes through “decapsulation.”) At Layer 4, a TCP/IP connection, for example, gets a port number to use once the data reaches its destination machine (the destination port), as well as the port number it will depart from (the source port). At this point, the data and its header are called a segment. The segment from here flows into the stream of data that will leave your computer, so the header with all the metadata that gets generated here is critical to parsing it back out on the other end to reach the correct service: your coworker’s chat application.

### The Media Layers
The bottom three layers are called the media layers. The term “media” here refers to hardware, and these layers primarily work on hardware dedicated to networking.

![Layer 3: Network](https://cdn.thenewstack.io/media/2024/11/f1861061-image8a-300x248.png)
Layer 3: Network

At Layer 3, the network layer, the data typically gets broken up into smaller pieces called packets for transmission. Each packet gets a header that includes the host address and address of the final destination (typically an IP address if going over the internet). In hardware terms, Layer 3 is usually represented by the router. The final destination address is usually part of a routing table the device has stored. Routers use routing algorithms to decide the best route to the destination, since it’s usually more than one hop away, and packets often get forwarded from one router to another.

![Layer 2: Data link](https://cdn.thenewstack.io/media/2024/11/44aa8241-image9a-300x247.png)
Layer 2: Data link

After referencing the routing tables to get the IP address, we drop to Layer 2, the data link layer. Here, your MAC (media access control) address is added as the source address to the data’s header, and then the system tries to identify which device should be the next stop on the data’s way to its final destination. Once it has a MAC address for an intermediate connection, the system adds that MAC address as the destination address on the header, creating a frame. Then the system identifies which port to send the frame out of, prepping to drop to Layer 1. If we were to associate the different layers with different pieces of hardware, this layer’s physical box would be the switch, which holds the MAC address table that maps each physical port to a specific MAC address. There’s always one port that’s saved as the catchall, where everything that isn’t in the table gets forwarded along.

In our example, though, no stand-alone switch is involved at this stage. The [logic for Layer 2](https://thenewstack.io/how-to-decide-between-a-layer-2-or-layer-3-network/) (and 3, technically), is inside your computer. Layer 2 logic and the Layer 1 port used to be part of a physical piece of hardware called the network interface controller (NIC). You may know it as the network card if you’ve built a desktop machine before. (You may remember connecting the network card to the motherboard via the bus or plugging in a dongle.) Most user systems now have this interface built into the motherboard or the system-on-a-chip. In a larger environment, though, like an office network, there’s likely a switch (or a switch-router combination device) somewhere along the line at Layer 2.

![Layer 1: Physical](https://cdn.thenewstack.io/media/2024/11/96766ef8-image10-300x248.png)
Layer 1: Physical

Finally, we drop to Layer 1, the physical layer. The data can now be moved! Data always moves as bits in a bitstream (a stream of 0s and 1s) along the physical layer, which can mean physical cable or a wireless connection. If you’re connecting to the internet, though, the data must traverse a physical cable at some point. The biggest cables at [Layer 1 comprise the internet backbone](https://thenewstack.io/traceroute-podcasts-trace-history-of-internet-layer-by-layer/): massive bundles of fiber optic and copper cables running underground and under the oceans between different hubs around the world. The backbone meets at exchange points where data gets transferred from one ISP or network to another. Since there are many exchange points and networks, there are many routes, and that’s where the transportation gets complicated.

### Transport
Realistically, your data bounces around along various routes. It goes through all the OSI layers on your laptop and then hops to your wireless access point along a Layer 1 connection. Then it might go up to Layer 2 inside the access point to get a new MAC address destination before going back down to Layer 1 to hop to a switch that forwards the data to a router. Then the router consults its routing tables to decide which port to use. Assuming your data needs to go over the internet, the router sends it to your ISP, and it through the layers to Layer 1 to get there. It might also get sent to another router, which would then send it in hops and skips to its destination. Devices can handle multiple OSI layers, so the conceptual model can break down some if you’re trying to trace it. If you’re going through a VPN, things get even more complex as your data moves across the internet.

Once your data has made it to the right system, though, it starts working its way back up the layers to your coworker’s computer. It may go through a switch or router (or both!) to get to the right machine and then progress up the stack, from Layer 1 to Layer 7. As it climbs up the layers, the headers are stripped off in a decapsulation process, the data is reassembled decrypted and translated to something the application can understand. Finally, your cat GIF appears on your coworker’s screen.

![](https://cdn.thenewstack.io/media/2024/11/911aa4a9-image11.gif)
If the two of you were on the same network, your data would go down to Layer 1 on your machine, then probably over the connection (Layer 1) to a switch (Layer 2). At the switch, whose table already contains your coworker’s machine’s MAC address, the data wouldn’t need to go to a router. Instead, it would go down to the port and out the connection, directly to your coworker’s machine. This is the simplest network in a real-life setup, as we don’t really use direct physical connections very often any longer. The only time you need to hop up to Layer 3 in this kind of simple setup is if you’re going across multiple networks. If you have a virtual network on your cloud provider of choice and then try to connect to another virtual network, you need to either establish an IP address and open a port to connect across the open internet, or use some kind of a virtual routing solution, like Equinix’s [Fabric Cloud Router](https://aws.amazon.com/marketplace/pp/prodview-l3kzqe5fdbqlw?trk=ce4ea0a3-61d4-484e-aac0-1e6f42b319f9&sc_channel=el&source=equinix), to connect across the networks.

## Real Life
Hardware in the world [outside the OSI abstraction](https://thenewstack.io/layer-8-the-inevitable-semantic-networking-layer/) is not as simple. There are Layer 3 switches with shallow routing tables; multilayer switches that work all the way up to Layer 4, as they understand MAC addresses, IP addresses, protocols and ports; bridge routers that handle Layers 1, 2 and 3; and even gateways that can function at any layer.

Using the OSI model for troubleshooting is common. Just as a developer uses tracebacks and breakpoints to discover where code is breaking, a network engineer uses the OSI model to discover where the data has stopped flowing. From finding a closed port to discovering that HTTP works but HTTPS doesn’t, the OSI model can offer a checklist to validate that all of your network components are working. And it isn’t just for the data center or your local network. You could use the OSI model to troubleshoot a Kubernetes cluster’s virtual network or a Docker container’s ports. Virtual networks generally follow many of the same conventions as physical networks, from ports and connections to VLANs (virtual local area networks) and IP-WANs (Internet Protocol Wide Area Networks).

The TCP/IP model more accurately represents the internet as we know it, and many people consider it the more practical model to learn well. However many, if not all, vendors of networking tools and hardware reference capabilities by using the layer-naming scheme from the OSI model, such as a “Layer 2 on-premises networks” or “Layer 3 network connectivity.” Cybersecurity vendors may talk about attacks at Layers 3 and 4 of a distributed system. It’s important to understand the concept behind these terms, even if simply to keep up with the context of a discussion.

## Closing Thought
If you found this post helpful, let us know on [Equinix Community!](https://community.equinix.com/)

[
YOUTUBE.COM/THENEWSTACK
Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.
](https://youtube.com/thenewstack?sub_confirmation=1)