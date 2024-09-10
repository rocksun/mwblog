# Try Mediasoup: An Open Source Streaming Media Tool
![Featued image for: Try Mediasoup: An Open Source Streaming Media Tool](https://cdn.thenewstack.io/media/2024/09/51b01709-mediasoup-streaming-data-1024x576.jpg)
[Mediasoup](https://mediasoup.org/), an open source server-side WebRTC library, revolutionizes the development of scalable real-time applications. Known for its superior codec support, Mediasoup offers a creative platform for building advanced real-time media streaming services.
It builds on [WebRTC](https://webrtc.org/)’s capability to enable browser-based interactions such as video calls and data transfers without plugins, enhancing it with a strong server-side solution for large-scale media handling. It features a flexible and scalable architecture, making it a top choice for developers focused on delivering high-quality real-time communication experiences.

## Scalability: Uninterrupted Media Flow
Mediasoup’s scalability comes from its specialized architecture. It’s a [Node.js](https://roadmap.sh/nodejs) library that works with [C++](https://roadmap.sh/cpp) subprocesses called **workers**, each running on a separate CPU core to handle media streams.

**Routers** in these workers manage audio and video real-time transport protocol (RTP) packet exchanges, similar to managing multiparty conference rooms. For example, in a setting with several conference rooms, each room uses a different Mediasoup router, spreading the load across multiple workers.
As the number of users increases, especially in large broadcast events with hundreds or thousands of viewers, Mediasoup allows for adding more workers or spreading rooms across several hosts for smooth media flow. A key feature here is the `router.pipeToRouter()`
function, enabling routers to communicate with each other for workload distribution, whether on the same or different hosts. This setup helps avoid overloading any single server and reduces latency and packet loss.

Mediasoup also efficiently manages video RTP transmission for large-scale broadcasts. It uses a server-side re-encoder to handle video packet retransmissions and keyframe requests, maintaining smooth video streams as the audience grows. This re-encoder processes streams from the broadcaster, re-encodes them and sends them to various Mediasoup routers serving many viewers. This way, it efficiently manages packet loss or keyframe requests without straining the broadcaster’s endpoint or affecting the viewing quality.

## Versatility: Supporting Diverse Media Codecs
Mediasoup’s versatility shines through its robust support for a multitude of media codecs, an essential feature that empowers developers to design applications catering to a wide range of user preferences concerning video and audio formats. This codec support is not static but flexible, allowing the RTP parameters from producer endpoints to have different values from the preferred router capabilities, although they must still be present in the router’s capabilities.

The framework accommodates various popular codecs such as VP8, VP9, H.264 and Opus. Moreover, it’s possible to use different video codecs for different producers, for instance, utilizing H264 for webcam and VP8 for screen sharing. This enables fine-grained control over media encoding and decoding processes to achieve the desired balance between performance and quality.

## Extensibility: Adapting and Enhancing
Mediasoup’s architecture is robust and flexible, ideal for developers who need to add extra features or to adapt the platform for specific business requirements. A key example of its flexibility is its integrations with FFmpeg and GStreamer.

Mediasoup allows easy media production and consumption from external sources, crucial for recording, transcoding and HTTP live streaming (HLS). Developers can simply create a server-side plain transport in Mediasoup and use the `produce()`
or `consume()`
functions with the necessary parameters to manage media.

## Mediasoup’s Architecture
Mediasoup’s architectural entities are comprised of workers, routers, transports, producers and consumers. Together they provide the building blocks for real-time media applications.

### Worker: Powering Media Processing
A Mediasoup worker is a [C++](https://thenewstack.io/c-on-the-move/) subprocess responsible for media processing, performing the computation necessary for media manipulation. Workers host multiple routers and run in separate threads to ensure non-blocking operations within an application.

To create a worker, you can use the `mediasoup.createWorker()`
method, which is then used to instantiate a router.

### Router: Orchestrating Media Streams
A router is a core entity acting as a container and manager for media streams. It’s the hub where media streams are routed between producers and consumers. Each router operates within the context of a worker and can manage multiple producers and consumers, orchestrating the flow of media streams within a specific room or context.

### Transport: Enabling Communication Channels
Transports are responsible for carrying media streams between peers and the router. Transports are created within the context of a router and are pivotal for establishing communication channels for media streams. Each transport has a set of parameters and events, facilitating the connection, error handling and closure of media transmission channels.

### Producer: Sending Media Streams
A producer represents a media source, serving as an endpoint that sends media streams to a router. Producers are created when a peer intends to start sending media.

### Consumer: Receiving Media Streams
A consumer is an endpoint that receives media streams from a router. Consumers are created when a peer aims to start receiving media.

## Try Mediasoup With a Demo Project
The demo project showcases a simplistic implementation of a real-time video communication platform using `mediasoup,`
`mediasoup-client`
and `socket.io`
. The project has both server and client parts that work together to establish a real-time video communication channel between users.

### Prerequisites for the Demo
Before beginning the demo, you need the following:

**Tools, Libraries and Technologies**
`mediasoup`
for WebRTC communication on the server.`socket.io`
for real-time, bidirectional communication between the server and client.`Nextjs`
for building the user interface.`mediasoup-client`
for client-side Mediasoup functionalities.
#### Background Knowledge
- A basic understanding of
[JavaScript](https://thenewstack.io/javascript/)/[TypeScript](https://thenewstack.io/typescript/). - Familiarity with
[React](https://thenewstack.io/after-a-decade-of-react-is-frontend-a-post-react-world-now/). - Understanding of WebRTC concepts.
#### Project Setup
Begin by cloning or downloading the [project repository](https://github.com/emmayusufu/mediasoup-learning-demo). Start the server and client, per the instructions in the repository [README](https://github.com/emmayusufu/mediasoup-learning-demo/blob/main/README.md).

### Project Walkthrough
This demonstration establishes a basic Mediasoup server for sharing video streams. In this demo, a single participant both produces and consumes media: They generate the media using a producer from their device and simultaneously consume it using a consumer on the same device. This setup offers a clear illustration of the basic functionalities and interactions within a Mediasoup environment for video streaming.

**Initialize the **Server
Create an HTTP server using `express`
, the `http`
module. This server serves as the foundation for handling incoming client requests and WebSocket connections.

WebSocket connections are facilitated using the `socket.io`
library, which provides the infrastructure for real-time, bidirectional communication between the server and clients.

To introduce the Mediasoup component for managing media streams, routing and transcoding, you need to initialize and configure Mediasoup within your server code. This typically involves creating a Mediasoup router, producers and consumers and handling various media-related events.

#### Initialize the Mediasoup Worker and Router
Start by initializing the core variables. These will be assigned to the actual Mediasoup components once they are created:

`worker`
: Manages media transmission processes.`router`
: Directs media streams between producers and consumers.`producerTransport`
and`consumerTransport`
: WebRTC transports for sending and receiving media.`producer`
and`consumer`
: Handle the outgoing and incoming media streams, respectively.
The `createWorker`
function initializes a Mediasoup worker.

**Configure the **Media Codecs
This code segment sets up the core client-server communication by defining an essential array of media codecs, including audio and video formats. This setup is pivotal for ensuring compatible and reliable media transmission between clients and the server.

I chose the Opus codec for its superior audio quality and the VP8 codec for video due to its real-time communication efficiency. Critical parameters such as the audio clock rate and channels and the video payload type are also specified. These configurations are not merely technical details; they are crucial for high-quality, low-latency media delivery.

#### Set Up Event Handlers for Peer Connections
This code segment outlines the setup and management of peer connections for media streaming using WebRTC and Mediasoup. Below is a summarized overview:

`connection`
: When a new peer connects, its connection is logged, and a success message is emitted back to the peer with its socket ID. A router is also created for each connected peer, enabling the routing of media streams. The router is configured with predefined media codecs.`disconnect`
: An event handler is set up to log when a peer disconnects, allowing for resource cleanup.`getRouterRtpCapabilities`
: An event handler allows peers to request the router’s RTP capabilities, which are essential for setting up transports and producers/consumers.`createTransport`
: An event handler manages requests to create transports (either for sending or receiving media), using a callback to provide transport parameters to the peer.`connectProducerTransport`
: An event handler is used to connect the sending transport with the necessary security parameters ([DTLS](https://en.wikipedia.org/wiki/Datagram_Transport_Layer_Security)).`transport-produce`
: An event handler sets up a media producer on the sending transport, handling the source of a single media track.`connectConsumerTransport`
: A similar event handler is used for connecting the receiving transport.`consumeMedia`
: An event handler facilitates media consumption from peers, checking router capabilities and creating a consumer on the consumer transport.`resumePausedConsumer`
: Another event handler allows for resuming media reception if it was previously paused.
#### Configure the WebRTC Transport Creation Function
The `createWebRtcTransport`
function is the backbone of WebRTC media transfer in this application. It’s an asynchronous function that creates WebRTC transports and provides the necessary parameters for establishing and handling WebRTC connections.

#### Set Up Server Listening
The HTTP server listens on port 4000 to start the application. This is the main entry point of the server where it begins accepting client connections.

#### Initialize the Client
This client application sets up a connection to the `/mediasoup`
namespace on the server using the `socket.io-client`
library. This connection is essential for signaling and coordinating media transmission between the client and server.

Upon connecting to the server, the client triggers the `startCamera`
function, which attempts to access the camera and capture a media stream. This media stream is then attached to the local video element for preview.

#### Set Up Local and Remote Video Elements
HTML video elements for displaying the local camera feed and the remote peer’s video stream are created and managed using React’s `useRef`
hook. These elements are essential for visualizing the video streams on the client’s user interface.

#### Prepare Button Actions for Various Workflow Steps
The client interface includes a series of buttons, each associated with a specific step in the media exchange workflow. These buttons trigger client-side functions that interact with the server to perform actions such as getting router RTP capabilities, creating devices, creating transports and consuming media.

#### Get Router RTP Capabilities
The client initiates a request to the server to obtain the router’s RTP capabilities. RTP capabilities describe the supported media formats and configurations for the server’s router. This information is crucial for configuring the Mediasoup device on the client side to ensure compatibility with the server.

#### Create a Device
Upon receiving the router’s RTP capabilities from the server, the client creates a Mediasoup device. The device is a client-side entity that interacts with the server’s router to manage media communication. Loading the router’s RTP capabilities into the device ensures that it can use compatible codecs and parameters for media transmission.

#### Create a Send Transport
The client sends a request to the server to create a send transport. A send transport is used for sending media from the client to the server. The server replicates the transport parameters on the client side, and the client initializes its own send transport based on these parameters.

#### Connect the Producer Transport and Producing Media
The client connects its send transport to the server. The transport’s `connect`
event is triggered when it’s ready to establish a connection. The client uses the provided DTLS parameters to connect the transport. After connecting the transport, the client starts producing media (audio or video) using the local camera. The produced media is sent through the send transport to the server.

#### Create a Consumer Transport
The client requests that the server create a receive transport. A consumer transport is used for receiving media from the server. The server replicates the transport parameters on the client side, and the client initializes its consumer transport based on these parameters.

#### Connect the Receive Transport and Start to Consume Media
The `connectRecvTransport`
function connects the client’s received transport to the server and starts consuming media received from the server. The transport’s `connect`
event is triggered when it’s ready to establish a connection. The client uses the provided DTLS parameters to connect the transport. After connecting the transport, the client displays the consumed media in the remote video element on the user interface.

## Conclusion
Mediasoup provides a comprehensive platform for building scalable and versatile real-time communication applications. Its ability to handle large-scale media streams with efficient load distribution and minimal latency makes it ideal for high-demand environments. The support for various codecs and seamless integration with external tools like FFmpeg and GStreamer offer developers flexibility in customizing their applications.

Whether used for broadcasting or interactive video communication, Mediasoup’s architecture ensures reliable performance and smooth media handling, allowing developers to create rich, high-quality user experiences.

[
YOUTUBE.COM/THENEWSTACK
Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.
](https://youtube.com/thenewstack?sub_confirmation=1)