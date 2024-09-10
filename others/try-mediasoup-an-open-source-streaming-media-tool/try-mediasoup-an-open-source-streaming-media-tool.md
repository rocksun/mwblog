
<!--
title: 试用Mediasoup：一款开源流媒体工具
cover: https://cdn.thenewstack.io/media/2024/09/51b01709-mediasoup-streaming-data.jpg
-->

学习如何使用 Mediasoup 构建强大的实时音视频流应用，本教程将为您提供详细的步骤指导。

> 译自 [Try Mediasoup: An Open Source Streaming Media Tool](https://thenewstack.io/try-mediasoup-an-open-source-streaming-media-tool/)，作者 Emmanuel Yusufu Kimaswa。

[Mediasoup](https://mediasoup.org/) 是一个开源的服务器端 WebRTC 库，它彻底改变了可扩展实时应用程序的开发。Mediasoup 以其卓越的编解码器支持而闻名，为构建先进的实时媒体流服务提供了一个创造性的平台。

它建立在 [WebRTC](https://webrtc.org/) 的基础之上，WebRTC 能够实现基于浏览器的交互，如视频通话和数据传输，而无需插件，并通过强大的服务器端解决方案增强了大规模媒体处理能力。它具有灵活且可扩展的架构，使其成为专注于提供高质量实时通信体验的开发人员的首选。

## 可扩展性：不间断的媒体流

Mediasoup 的可扩展性源于其专门的架构。它是一个 [Node.js](https://roadmap.sh/nodejs) 库，与称为 **worker** 的 [C++](https://roadmap.sh/cpp) 子进程一起工作，每个子进程都在一个单独的 CPU 内核上运行，以处理媒体流。

这些 worker 中的 **Router** 管理音频和视频实时传输协议 (RTP) 数据包交换，类似于管理多方会议室。例如，在有多个会议室的环境中，每个会议室都使用不同的 Mediasoup Router ，将负载分散到多个 worker 上。

随着用户数量的增加，尤其是在拥有数百或数千名观众的大型广播活动中，Mediasoup 允许添加更多 worker 或将会议室分散到多个主机上，以实现流畅的媒体流。这里的关键特性是 `router.pipeToRouter()` 函数，它使Router 能够相互通信以进行工作负载分配，无论是在同一主机上还是在不同主机上。这种设置有助于避免任何单台服务器过载，并减少延迟和丢包。

Mediasoup 还高效地管理大规模广播的视频 RTP 传输。它使用服务器端重新编码器来处理视频数据包重传和关键帧请求，从而在观众数量增加时保持流畅的视频流。此重新编码器处理来自广播公司的流，对其进行重新编码，然后将其发送到为众多观众提供服务的各种 Mediasoup Router 。这样，它可以有效地管理丢包或关键帧请求，而不会给广播公司的端点带来压力或影响观看质量。

## 多功能性：支持多种媒体编解码器

Mediasoup 的多功能性体现在它对多种媒体编解码器的强大支持，这是一个基本特性，使开发人员能够设计满足各种用户对视频和音频格式偏好的应用程序。这种编解码器支持不是静态的，而是灵活的，允许来自生产者端点的 RTP 参数与首选Router 功能具有不同的值，尽管它们必须仍然存在于Router 的功能中。

该框架支持各种流行的编解码器，如 VP8、VP9、H.264 和 Opus。此外，还可以对不同的生产者使用不同的视频编解码器，例如，对网络摄像头使用 H264，对屏幕共享使用 VP8。这使得能够对媒体编码和解码过程进行细粒度控制，以在性能和质量之间取得理想的平衡。

## 可扩展性：适应和增强

Mediasoup 的架构强大而灵活，非常适合需要添加额外功能或根据特定业务需求调整平台的开发人员。其灵活性的一个关键例子是它与 FFmpeg 和 GStreamer 的集成。

Mediasoup 允许从外部源轻松进行媒体制作和消费，这对于录制、转码和 HTTP 实时流媒体 (HLS) 至关重要。开发人员只需在 Mediasoup 中创建一个服务器端普通传输，并使用 `produce()` 或 `consume()` 函数以及必要的参数来管理媒体。

## Mediasoup 的架构

Mediasoup 的架构实体由 worker、Router 、transport、producer 和 consumer 组成。它们共同构成了实时媒体应用程序的构建块。

### Worker：为媒体处理提供动力

Mediasoup worker 是一个 [C++](https://thenewstack.io/c-on-the-move/) 子进程，负责媒体处理，执行媒体操作所需的计算。Worker 托管多个Router ，并在单独的线程中运行，以确保应用程序中的非阻塞操作。

要创建 worker，可以使用 `mediasoup.createWorker()` 方法，然后使用该方法实例化Router 。

### Router：协调媒体流

Router 是一个核心实体，充当媒体流的容器和管理器。它是媒体流在生产者和消费者之间路由的中心。每个Router 都在一个工作器的上下文中运行，并且可以管理多个生产者和消费者，协调特定房间或上下文中的媒体流。

### Transport：启用通信通道

传输负责在对等方和Router 之间传送媒体流。传输是在Router 的上下文中创建的，对于建立媒体流的通信通道至关重要。每个传输都有一组参数和事件，有助于媒体传输通道的连接、错误处理和关闭。

### Producer：发送媒体流

生产者表示媒体源，充当将媒体流发送到Router 的端点。当对等方打算开始发送媒体时，就会创建生产者。

### Consumer：接收媒体流

消费者是从Router 接收媒体流的端点。当对等方打算开始接收媒体时，就会创建消费者。

## 使用演示项目试用 Mediasoup

该演示项目展示了使用 `mediasoup`、 `mediasoup-client` 和 `socket.io` 的实时视频通信平台的简单实现。该项目包含服务器和客户端部分，它们协同工作以在用户之间建立实时视频通信通道。

### 演示先决条件

在开始演示之前，您需要具备以下条件：

**工具、库和技术**

1. `mediasoup`：用于服务器上的 WebRTC 通信。
2. `socket.io`：用于服务器和客户端之间的实时双向通信。
3. `Nextjs`：用于构建用户界面。
4. `mediasoup-client`：用于客户端 Mediasoup 功能。

**背景知识**

1. 对 [JavaScript](https://thenewstack.io/javascript/) / [TypeScript](https://thenewstack.io/typescript/) 的基本了解。
2. 熟悉 [React](https://thenewstack.io/after-a-decade-of-react-is-frontend-a-post-react-world-now/)。
3. 了解 WebRTC 概念。

**项目设置**

首先克隆或下载 [项目存储库](https://github.com/emmayusufu/mediasoup-learning-demo)。根据存储库 [README](https://github.com/emmayusufu/mediasoup-learning-demo/blob/main/README.md) 中的说明启动服务器和客户端。

### 项目演练

此演示建立了一个基本的 Mediasoup 服务器，用于共享视频流。在此演示中，单个参与者既生成媒体又消费媒体：他们使用来自其设备的生产者生成媒体，并同时使用同一设备上的消费者消费媒体。此设置清楚地说明了 Mediasoup 环境中用于视频流的基本功能和交互。

**初始化服务器**

使用 `express`、`http` 模块创建一个 HTTP 服务器。此服务器充当处理传入客户端请求和 WebSocket 连接的基础。

WebSocket 连接是使用 `socket.io` 库实现的，该库为服务器和客户端之间的实时双向通信提供了基础结构。

要引入 Mediasoup 组件来管理媒体流、路由和转码，您需要在服务器代码中初始化和配置 Mediasoup。这通常涉及创建 Mediasoup Router 、生产者和消费者，以及处理各种与媒体相关的事件。

```js
import express from "express";
import http from "http";
import { Server } from "socket.io";
import cors from "cors";
import mediasoup from "mediasoup";

const app = express();
const port = 4000;
const server = http.createServer(app);

// Initialize a Socket.IO server for WebSocket connections
const io = new Server(server, {
  cors: {
    origin: "*",
    credentials: true,
  },
});

// Create a namespace "/mediasoup" for mediasoup-related socket events
const peers = io.of("/mediasoup");
```

**初始化 Mediasoup 工作器和Router** 

首先初始化核心变量。这些变量将在创建实际的 Mediasoup 组件后分配给它们：

*   `worker`：管理媒体传输过程。
*   `router`：在生产者和消费者之间定向媒体流。
*   `producerTransport` 和 `consumerTransport`：用于发送和接收媒体的 WebRTC 传输。
*   `producer` 和 `consumer`：分别处理传出和传入的媒体流。

`createWorker` 函数初始化一个 Mediasoup 工作器。

```ts
let worker: mediasoup.types.Worker<mediasoup.types.AppData>;
let router: mediasoup.types.Router<mediasoup.types.AppData>;
let producerTransport:
  | mediasoup.types.WebRtcTransport<mediasoup.types.AppData>
  | undefined;
let consumerTransport:
  | mediasoup.types.WebRtcTransport<mediasoup.types.AppData>
  | undefined;
let producer: mediasoup.types.Producer<mediasoup.types.AppData> | undefined;
let consumer: mediasoup.types.Consumer<mediasoup.types.AppData> | undefined;

const createWorker = async (): Promise<
  mediasoup.types.Worker<mediasoup.types.AppData>
  
// Create a mediasoup worker with specific configuration
    const newWorker = await mediasoup.createWorker({
    rtcMinPort: 2000, // Minimum port number for RTC traffic
    rtcMaxPort: 2020, // Maximum port number for RTC traffic
  });

// Log the worker process ID for reference
  console.log(`Worker process ID ${newWorker.pid}`);

// Event handler for the 'died' event on the worker
newWorker.on("died", (error) => {
    console.error("mediasoup worker has died");
    // Gracefully shut down the process to allow for recovery or troubleshooting.
    setTimeout(() => {
      process.exit();
    }, 2000);
  });

  return newWorker;
};
```

**配置媒体编解码器**

此代码段通过定义基本媒体编解码器数组（包括音频和视频格式）来设置核心客户端-服务器通信。此设置对于确保客户端和服务器之间兼容且可靠的媒体传输至关重要。

我选择 Opus 编解码器是因为其卓越的音频质量，选择 VP8 编解码器是因为其在视频方面的实时通信效率。还指定了关键参数，例如音频时钟速率和通道以及视频有效负载类型。这些配置不仅仅是技术细节；它们对于高质量、低延迟的媒体交付至关重要。

```ts
/**
 * The media codecs configuration array.
 * Each object in this array provides configuration for a specific audio or video codec.
 */
const mediaCodecs: mediasoup.types.RtpCodecCapability[] = [
  {
    /** Indicates this is an audio codec configuration */
    kind: "audio",
    /**
     * Specifies the MIME type for the Opus codec, known for good audio quality at various bit rates.
     * Format: <type>/<subtype>, e.g., audio/opus
     */
    mimeType: "audio/opus",
    /**
     * Specifies the number of audio samples processed per second (48,000 samples per second for high-quality audio).
     * Higher values generally allow better audio quality.
     */
    clockRate: 48000,
    /** Specifies the number of audio channels (2 for stereo audio). */
    channels: 2,
    /**
     * Optional: Specifies a preferred payload type number for the codec.
     * Helps ensure consistency in payload type numbering across different sessions or applications.
     */
    preferredPayloadType: 96, // Example value
    /**
     * Optional: Specifies a list of RTCP feedback mechanisms supported by the codec.
     * Helps optimize codec behavior in response to network conditions.
     */
    rtcpFeedback: [
      // Example values
      { type: "nack" },
      { type: "nack", parameter: "pli" },
    ],
  },
  {
    /** Indicates this is a video codec configuration */
    kind: "video",
    /** Specifies the MIME type for the VP8 codec, commonly used for video compression. */
    mimeType: "video/VP8",
    /** Specifies the clock rate, or the number of timing ticks per second (commonly 90,000 for video). */
    clockRate: 90000,
    /**
     * Optional: Specifies codec-specific parameters.
     * In this case, sets the starting bitrate for the codec.
     */
    parameters: {
      "x-google-start-bitrate": 1000,
    },
    preferredPayloadType: 97, // Example value
    rtcpFeedback: [
      // Example values
      { type: "nack" },
      { type: "ccm", parameter: "fir" },
      { type: "goog-remb" },
    ],
  },
];
```

**为对等连接设置事件处理程序**

此代码段概述了使用 WebRTC 和 Mediasoup 设置和管理媒体流的对等连接。以下是概述：

- `connection`：当一个新的 peer 连接时，它的连接会被记录，并且会向该 peer 发送一条包含其套接字 ID 的成功消息。同时，还会为每个连接的 peer 创建一个Router ，以实现媒体流的路由。该Router 配置了预定义的媒体编解码器。
- `disconnect`：设置了一个事件处理程序，用于在 peer 断开连接时记录日志，以便进行资源清理。
- `getRouterRtpCapabilities`：一个事件处理程序允许 peer 请求Router 的 RTP 功能，这对于设置传输和生产者/消费者至关重要。
- `createTransport`：一个事件处理程序使用回调函数来提供传输参数给 peer，从而管理创建传输（用于发送或接收媒体）的请求。
- `connectProducerTransport`：一个事件处理程序使用必要的安全参数（[DTLS](https://en.wikipedia.org/wiki/Datagram_Transport_Layer_Security)）将发送传输与之连接。
- `transport-produce`：一个事件处理程序在发送传输上设置媒体生产者，处理单个媒体轨道的来源。
- `connectConsumerTransport`：一个类似的事件处理程序用于连接接收传输。
- `consumeMedia`：一个事件处理程序促进从 peer 消费媒体，检查Router 功能并在消费者传输上创建消费者。
- `resumePausedConsumer`：另一个事件处理程序允许在先前暂停的情况下恢复媒体接收。

```ts
// Event handler for new peer connections
peers.on("connection", async (socket) => {
 // ... Peer connection event handling ...

 /**
  * Create a router.
  * Since there are only two peers in this application, we only need one router for each peer.
  * In a more complex application, you may need multiple routers to handle multiple peers.
  * A router is required to route media to/from this peer.
  */
 router = await worker.createRouter({
   mediaCodecs: mediaCodecs,
 });

 /**
  * Event handler for fetching router RTP capabilities.
  * RTP capabilities are required for configuring transports and producers/consumers.
  * This function is called when a peer requests the router RTP capabilities.
  * The callback function is used to send the router RTP capabilities to the peer.
  */
 socket.on("getRouterRtpCapabilities", (callback) => {
   // ... Handling router RTP capabilities ...
 });

/**
  * Event handler for creating a transport.
  * A transport is required for sending or producing media.
  * The callback function is used to send the transport parameters to the peer.
  * @param {boolean} data.sender - Indicates whether the transport is for sending or receiving media.
  * @param {function} callback - A callback function to handle the result of the transport creation.
  */
 socket.on("createTransport", async ({ sender }, callback) => {
   // ... Creating sender/receiver transports ...
 });


 /**
  * Event handler for producing media.
  * This function sets up a producer for sending media to the peer.
  * A producer represents the source of a single media track (audio or video).
  * @param {object} data.dtlsParameters - Datagram Transport Layer Security (DTLS) parameters.
  * These parameters are necessary for securing the transport with encryption.
  */
 socket.on("connectProducerTransport", async ({ dtlsParameters }) => {
   // ... Connecting the sending transport ...
 });

 // Event handler for producing media
 socket.on("transport-produce", async ({ kind, rtpParameters }, callback) => {
   // ... Producing media ...
 });

 // Event handler for connecting the receiving transport
 socket.on("connectConsumerTransport", async ({ dtlsParameters }) => {
   // ... Connecting the receiving transport ...
 });

 /**
  * Event handler for consuming media.
  * This function sets up a consumer for receiving media from the peer.
  * A consumer represents the endpoint for receiving media of a single kind
  * (audio or video) from a remote peer. Creating a consumer involves multiple
  * steps to ensure that the media can be received and decoded correctly.
  */
 socket.on("consumeMedia", async ({ rtpCapabilities }, callback) => {
   // ... Consuming media ...
 });

 // Event handler for resuming media consumption
 socket.on("resumePausedConsumer", async (data) => {
   // ... Resuming media consumption ...
 });
});
```

**配置 WebRTC 传输创建函数**

`createWebRtcTransport` 函数是此应用程序中 WebRTC 媒体传输的支柱。它是一个异步函数，用于创建 WebRTC 传输并提供建立和处理 WebRTC 连接所需的参数。

```ts
const createWebRtcTransport = async (
  callback: (arg0: {
    params: mediasoup.types.WebRtcTransportOptions | { error: unknown };
  }) => void
) => {
 // ... WebRTC transport creation, configuration, and event handling ...
};
```

**设置服务器监听**

HTTP 服务器监听端口 4000 以启动应用程序。这是服务器开始接受客户端连接的主要入口点。

```ts
server.listen(port, () => {
  console.log(`Server running at http://localhost:${port}`);
});
```

**初始化客户端**

此客户端应用程序使用 `socket.io-client` 库设置到服务器上 `/mediasoup` 命名空间的连接。此连接对于客户端和服务器之间的信号传输和媒体传输协调至关重要。

连接到服务器后，客户端会触发 `startCamera` 函数，该函数尝试访问摄像头并捕获媒体流。然后，此媒体流附加到本地视频元素以进行预览。

```ts
import { useEffect, useRef, useState } from "react";
import { io } from "socket.io-client";
import { Device } from "mediasoup-client";

export default function Home() {
 /**
  * References to the local and remote video HTML elements.
  * These refs are used to attach media streams to the video elements for playback.
  */
 const videoRef = useRef<HTMLVideoElement | null>(null);
 const remoteVideoRef = useRef<HTMLVideoElement | null>(null);

 /**
  * State to hold encoding parameters for the media stream.
  * Encoding parameters control the quality and bandwidth usage of the transmitted video.
  * Each object in the encoding array represents a different layer of encoding,
  * allowing for scalable video coding (SVC). The parameters defined here are:
  * - rid: The encoding layer identifier.
  * - maxBitrate: The maximum bitrate for this layer.
  * - scalabilityMode: The scalability mode which specifies the temporal and spatial scalability.
  *
  * Additionally, codecOptions are provided to control the initial bitrate.
  */
 const [params, setParams] = useState({
   encoding: [
     { rid: "r0", maxBitrate: 100000, scalabilityMode: "S1T3" }, // Lowest quality layer
     { rid: "r1", maxBitrate: 300000, scalabilityMode: "S1T3" }, // Middle quality layer
     { rid: "r2", maxBitrate: 900000, scalabilityMode: "S1T3" }, // Highest quality layer
   ],
   codecOptions: { videoGoogleStartBitrate: 1000 }, // Initial bitrate
 });

 /**
  * State to hold references to various mediasoup client-side entities.
  * These entities are crucial for managing the media transmission and reception.
  */
 const [device, setDevice] = useState<any>(null); // mediasoup Device
 const [socket, setSocket] = useState<any>(null); // Socket for signaling
 const [rtpCapabilities, setRtpCapabilities] = useState<any>(null); // RTP Capabilities for the device
 const [producerTransport, setProducerTransport] = useState<any>(null); // Transport for sending media
 const [consumerTransport, setConsumerTransport] = useState<any>(null); // Transport for receiving media

 /**
  * Effect to initialize the socket connection on component mount.
  * The socket is used for signaling to coordinate media transmission.
  * On successful connection, the camera is started to obtain a media stream.
  */
 useEffect(() => {
   const socket = io("http://localhost:4000/mediasoup");

   setSocket(socket);
   socket.on("connection-success", (data) => {
     startCamera();
   });
   return () => {
     socket.disconnect();
   };
 }, []);

 /**
  * Function to start the camera and obtain a media stream.
  * This stream is then attached to the local video element for preview.
  */
 const startCamera = async () => {
   try {
     const stream = await navigator.mediaDevices.getUserMedia({ video: true });
     if (videoRef.current) {
       const track = stream.getVideoTracks()[0];
       videoRef.current.srcObject = stream;
       setParams((current) => ({ ...current, track }));
     }
   } catch (error) {
     console.error("Error accessing camera:", error);
   }
 };

}
```

**设置本地和远程视频元素**

使用 React 的 `useRef` 钩子创建和管理用于显示本地摄像头馈送和远程 peer 视频流的 HTML 视频元素。这些元素对于在客户端用户界面上可视化视频流至关重要。

```ts
//...
      <video ref={videoRef} id="localvideo" autoPlay playsInline />
      <video ref={remoteVideoRef} id="remotevideo" autoPlay playsInline />
//...
```

**为各种工作流程步骤准备按钮操作**

客户端界面包含一系列按钮，每个按钮都与媒体交换工作流程中的特定步骤相关联。这些按钮触发与服务器交互的客户端函数，以执行获取Router  RTP 功能、创建设备、创建传输和消费媒体等操作。

```ts

      <div style={{ display: "flex", flexDirection: "column", gap: "20px" }}>
        <button onClick={getRouterRtpCapabilities}>
          Get Router RTP Capabilities
        </button>
        <button onClick={createDevice}>Create Device</button>
        <button onClick={createSendTransport}>Create send transport</button>
        <button onClick={connectSendTransport}>
          Connect send transport and produce
        </button>
        <button onClick={createRecvTransport}>Create recv transport</button>
        <button onClick={connectRecvTransport}>
          Connect recv transport and consume
        </button>
      </div>
```

**获取 Router RTP 功能**

客户端向服务器发起请求以获取Router 的 RTP 功能。RTP 功能描述了服务器Router 支持的媒体格式和配置。此信息对于配置客户端上的 Mediasoup 设备以确保与服务器兼容至关重要。

```ts

   * Step 1: Retrieve the Router's RTP Capabilities.
   * This function requests the router's RTP capabilities from the server,
   * which are essential to configure the mediasoup Device.
   * The router's RTP capabilities describe the codecs and RTP parameters supported by the router.
   * This information is crucial for ensuring that the Device is compatible with the router.
   */
  const getRouterRtpCapabilities = async () => {
    socket.emit("getRouterRtpCapabilities", (data: any) => {
      setRtpCapabilities(data.routerRtpCapabilities);
      console.log(`getRouterRtpCapabilities: ${data.routerRtpCapabilities}`);
    });
  };
```

**创建设备**

从服务器接收Router 的 RTP 功能后，客户端会创建一个 Mediasoup 设备。该设备是一个客户端实体，用于与服务器的Router 交互以管理媒体通信。将Router 的 RTP 功能加载到设备中可确保它可以使用兼容的编解码器和参数进行媒体传输。

```ts
 /**
   * Step 2: Create and Initialize the mediasoup Device.
   * This function creates a new mediasoup Device instance and loads the router's RTP capabilities into it.
   * The Device is a client-side entity that provides an API for managing sending/receiving media with a mediasoup server.
   * Loading the router's RTP capabilities ensures that the Device is aware of the codecs and RTP parameters it needs to use
   * to successfully send and receive media with the server.
   *
   * If the Device is unable to load the router's RTP capabilities (e.g., due to an unsupported browser),
   * an error is logged to the console.
   */
  const createDevice = async () => {
    try {
      const newDevice = new Device();

      await newDevice.load({ routerRtpCapabilities: rtpCapabilities });

      setDevice(newDevice);
    } catch (error: any) {
      console.log(error);
      if (error.name === "UnsupportedError") {
        console.error("Browser not supported");
      }
    }
  };
```

**创建发送传输**

客户端向服务器发送请求以创建发送传输。发送传输用于将媒体从客户端发送到服务器。服务器在客户端复制传输参数，客户端根据这些参数初始化自己的发送传输。

```ts
/**
* Step 3: Create a Transport for Sending Media.
* This function initiates the creation of a transport on the server-side for sending media,
* and then replicates the transport on the client-side using the parameters returned by the server.
*/
const createSendTransport = async () => {
 // Request the server to create a send transport
 socket.emit(
   "createSendTransport",
   { sender: true },
   ({ params }: { params: any }) => {
     if (params.error) {
       console.log(params.error);
       return;
     }

     /**
      * Replicate the send transport on the client-side.
      * The `device.createSendTransport` method creates a send transport instance on the client-side
      * using the parameters provided by the server.
      */
     let transport = device.createSendTransport(params);

     // Update the state to hold the reference to the created transport
     setProducerTransport(transport);

     /**
        * Event handler for the "connect" event on the transport.
        * This event is triggered when the transport is ready to be connected.
        * The `dtlsParameters` are provided by the transport and are required to establish
        * the DTLS connection between the client and the server.
        * This event it emitted as a result of calling the `producerTransport?.produce(params)`
        * method in the next step. The event will only be emitted if this is the first time
        */
     transport.on(
       "connect",
       async ({ dtlsParameters }: any, callback: any, errback: any) => {
         try {
           console.log("----------> producer transport has connected");
           // Notify the server that the transport is ready to connect with the provided DTLS parameters
           await socket.emit("transport-connect", { dtlsParameters });
           // Callback to indicate success
           callback();
         } catch (error) {
           // Errback to indicate failure
           errback(error);
         }
       }
     );

     /**
        * Event handler for the "produce" event on the transport.
        * This event is triggered when the transport is ready to start producing media.
        * The `parameters` object contains the necessary information for producing media,
        * including the kind of media (audio or video) and the RTP parameters.
        * The event is emitted as a result of calling the `producerTransport?.produce(params)`
        * method in the next step.
        */
     transport.on(
       "produce",
       async (parameters: any, callback: any, errback: any) => {
         const { kind, rtpParameters } = parameters;

         console.log("----------> transport-produce");

         try {
           // Notify the server to start producing media with the provided parameters
           socket.emit(
             "transport-produce",
             { kind, rtpParameters },
             ({ id }: any) => {
               // Callback to provide the server-generated producer ID back to the transport
               callback({ id });
             }
           );
         } catch (error) {
           // Errback to indicate failure
           errback(error);
         }
       }
     );
   }
 );
};
```

**连接生产者传输并生成媒体**

客户端将其发送传输连接到服务器。传输的 `connect` 事件在准备好建立连接时触发。客户端使用提供的 DTLS 参数连接传输。连接传输后，客户端使用本地摄像头开始生成媒体（音频或视频）。生成的媒体通过发送传输发送到服务器。

```ts
const connectSendTransport = async () => {
 // Producing media using the send transport
 let localProducer = await producerTransport.produce(params);

 // Event handlers for track ending and transport closing events
 localProducer.on("trackended", () => {
   console.log("trackended");
 });
 localProducer.on("transportclose", () => {
   console.log("transportclose");
 });
}
```

**创建消费者传输**

客户端请求服务器创建接收传输。消费者传输用于从服务器接收媒体。服务器在客户端复制传输参数，客户端根据这些参数初始化其消费者传输。

```ts
const createRecvTransport = async () => {
 // Requesting the server to create a receive transport
 socket.emit(
   "createTransport",
   { sender: false },
   ({ params }: { params: any }) => {
     if (params.error) {
       return;
     }

     // Creating a receive transport on the client-side using the server-provided parameters
     let transport = device.createRecvTransport(params);
     setConsumerTransport(transport);

     // Event handler for the connect event on the transport
     transport.on(
       "connect",
       async ({ dtlsParameters }: any, callback: any, errback: any) => {
         try {
           // Notifying the server to connect the receive transport with the provided DTLS parameters
           await socket.emit("transport-recv-connect", { dtlsParameters });
           callback();
         } catch (error) {
           errback(error);
         }
       }
     );
   }
 );
};
```

**连接接收传输并开始消费媒体**

connectRecvTransport 函数将客户端接收的传输连接到服务器，并开始使用从服务器接收的媒体。当传输准备建立连接时，将触发其 connect 事件。客户端使用提供的 DTLS 参数连接传输。连接传输后，客户端会在用户界面上显示远程视频元素中消耗的媒体。

```ts
const connectRecvTransport = async () => {
 // Requesting the server to start consuming media
 await socket.emit(
   "consume",
   { rtpCapabilities: device.rtpCapabilities },
   async ({ params }: any) => {
     if (params.error) {
       return;
     }

     // Consuming media using the receive transport
     let consumer = await consumerTransport.consume({
       id: params.id,
       producerId: params.producerId,
       kind: params.kind,
       rtpParameters: params.rtpParameters,
     });

     // Accessing the media track from the consumer
     const { track } = consumer;

     // Attaching the media track to the remote video element for playback
     if (remoteVideoRef.current) {
       remoteVideoRef.current.srcObject = new MediaStream([track]);
     }

     // Notifying the server to resume media consumption
     socket.emit("consume-resume");
   }
 );
};
```

## 总结

Mediasoup 为构建可扩展且通用的实时通信应用程序提供了一个全面的平台。它能够以高效的负载分配和最低的延迟处理大规模媒体流，使其成为高要求环境的理想选择。对各种编解码器的支持以及与 FFmpeg 和 GStreamer 等外部工具的无缝集成，使开发人员能够灵活地定制其应用程序。

无论是用于广播还是交互式视频通信，Mediasoup 的架构都能确保可靠的性能和平稳的媒体处理，使开发人员能够创造丰富、高质量的用户体验。
