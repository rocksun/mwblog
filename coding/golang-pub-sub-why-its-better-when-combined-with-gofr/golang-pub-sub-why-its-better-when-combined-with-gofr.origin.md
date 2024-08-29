# Golang Pub/Sub: Why It’s Better When Combined With GoFr
![Featued image for: Golang Pub/Sub: Why It’s Better When Combined With GoFr](https://cdn.thenewstack.io/media/2024/05/1b47a8e1-gofr-logo-2-1024x576.png)
As modern systems evolve, the need for reliable, scalable and real-time communication has never been greater. [Pub/sub (publish-subscribe)](https://thenewstack.io/publish-subscribe-introduction-to-scalable-messaging/) is a messaging pattern that allows different components of a system to communicate asynchronously. This decoupled architecture is the backbone of the Internet of Things (IoT), distributed systems and real-time applications where responsiveness and flexibility are key.

When building these systems, [Golang](https://thenewstack.io/go/) is an obvious choice due to its simplicity, efficiency and built-in concurrency. But to take full advantage of Golang’s capabilities in a pub/sub setup, the framework [GoFr](https://thenewstack.io/gofr-a-go-framework-to-power-scalable-and-observable-apps/) offers optimized solutions that simplify the process and introduce powerful features.

Leading companies have successfully implemented pub/sub systems using frameworks like GoFr to solve complex challenges. For instance, LinkedIn, Pinterest and Walmart have all leveraged event-driven architectures and pub/sub to manage massive amounts of data and ensure system reliability.

GoFr offers a powerful set of tools and features that elevate Golang’s pub/sub capabilities, making it an ideal choice for building scalable, real-time systems, especially in the IoT domain. By choosing GoFr, developers can benefit from a proven framework that simplifies the development process and ensures that their pub/sub systems are reliable and easy to manage.

[Event-driven architecture (EDA)](https://thenewstack.io/the-basics-of-event-driven-architectures/) lies at the core of modern, scalable and resilient real-time systems. Unlike the traditional request-response model, where services communicate synchronously, EDA allows for asynchronous communication. This decouples services, enabling them to operate independently and respond to events in real time.
For IoT applications, where devices continuously generate and exchange data, pub/sub becomes a critical communication mechanism. By implementing pub/sub, IoT systems can handle a large number of devices, ensuring scalability, reliability and real-time responsiveness. Pub/sub’s ability to handle high-throughput, low-latency communication is particularly valuable in these environments.

In this article, I’ll show you why GoFr, combined with Golang, is the perfect match for building high-performance pub/sub systems and how you can get started quickly, with an IoT example using the [communication protocol MQTT](https://www.influxdata.com/mqtt).

## Why Choose GoFr for Pub/Sub in Golang?
[Golang has risen to prominence](https://thenewstack.io/what-made-golang-so-popular-the-languages-creators-look-back/) in building distributed systems because of its impressive performance and concurrency model. Pub/sub architectures benefit significantly from Go’s goroutines, which allow lightweight, asynchronous communication between different services without introducing significant overhead. This is crucial in systems where multiple events must be processed concurrently.
Here’s why GoFr is an ideal choice for developers building IoT systems and other real-time apps in Go:

- Simplicity and efficiency. GoFr abstracts much of the boilerplate code associated with setting up pub/sub, allowing developers to focus on business logic rather than infrastructure management.
- Support for multiple message brokers. GoFr natively supports a variety of message brokers, including
[Apache Kafka](https://thenewstack.io/hybrid-data-collection-from-the-iot-edge-with-mqtt-and-kafka/), Google pub/sub, and MQTT. This flexibility ensures that developers can choose the best broker for their specific use case. - Comprehensive monitoring and security. With built-in monitoring and security features, GoFr ensures that your pub/sub system is not only efficient but also secure and easy to manage.
- Optimized for IoT with MQTT. MQTT is a lightweight messaging protocol designed for IoT, and GoFr’s support for MQTT makes it an excellent choice for IoT backends. GoFr simplifies the setup and management of MQTT brokers, allowing for seamless integration into your IoT systems.
- Routing and middleware. Simplifies setting up REST APIs with built-in route handling and middleware.
- Database support. Easily connects to
[SQL](https://thenewstack.io/how-to-write-sql-queries/),[NoSQL](https://thenewstack.io/why-choose-a-nosql-database-there-are-many-great-reasons/), and[time series databases](https://thenewstack.io/what-are-time-series-databases-and-why-do-you-need-them/)for data storage and processing.
## Optimizing Pub/Sub With GoFr
GoFr is built with scalability and ease of use in mind. It provides native support for MQTT, one of the most popular protocols for real-time communication in IoT systems. By leveraging GoFr’s built-in [pub/sub](https://github.com/gofr-dev/gofr/blob/development/examples/using-publisher/main.go) capabilities, you can set up a robust system with minimal effort.

Here’s how you can set up a simple MQTT-based pub/sub system using GoFr.

### Setting Up the Development Environment
First, initialize your Go module and add the GoFr package to your project:

12 |
go mod init github.com/gofr_iot_projectgo get gofr.dev |
### Example Code for Publishing Messages
This simple example sets up a REST API endpoint `/light`
that receives data about a smart light’s mode and publishes it to the MQTT topic `room-smart-light`
. Any IoT devices subscribed to this topic will receive the message.

You can connect to an [MQTT](https://github.com/gofr-dev/gofr/blob/development/examples/using-subscriber/configs/.env) broker by adding the following configuration in your `.env`
file:

1 |
PUBSUB_BACKEND=MQTT |
In the configuration line `PUBSUB_BACKEND=MQTT`
, there’s no need to specify additional credentials such as an ID or password because we are connecting to a public MQTT broker.
Public brokers, unlike private or secured brokers, don’t require authentication details such as usernames or passwords. This makes it easier to get started and test out your system without worrying about setting up complex security configurations. However, for production environments or more sensitive applications, connecting to a private broker would typically require credentials to ensure secure communication.

Additionally, GoFr simplifies tracing and monitoring by providing a built-in tracer endpoint. This tracer allows you to monitor the flow of data in real time, track event life cycles and identify performance bottlenecks or errors as they occur. This level of visibility is crucial when scaling systems or troubleshooting issues, as it helps you maintain system health and ensure events are processed as expected.

### Example Code for Subscribing to Topics
Similarly, you can create a subscriber that listens to topics and processes incoming messages:

## High-Level Architecture for IoT Backends with GoFr
When designing an IoT backend with GoFr, the architecture typically involves several key components:

**API Gateway.**The API Gateway acts as the central point for managing and routing API requests. With GoFr, setting up a CRUD API is simplified, thanks to features like`AddRESTHandlers`
, which automates route handling and database integration.**Device management.**Secure and scalable device management is crucial for IoT systems. GoFr includes built-in authentication middleware that supports multiple mechanisms like OAuth and Basic-Auth, ensuring secure communication between services.**Data ingestion and processing.**GoFr supports real-time data handling through MQTT and HTTP. It also integrates seamlessly with various databases, making it easy to store and process large volumes of data.**Monitoring and security.**Robust monitoring and security are critical for any IoT backend. GoFr offers comprehensive monitoring capabilities, providing insights into system performance and security.
GoFr is built with scalability and fault tolerance at its core, making it highly suitable for handling high-throughput systems like IoT. It includes essential features such as retry mechanisms, dead-letter queues and circuit breakers, which ensure that even under heavy load or in the event of component failures, the system remains resilient.

Dead-letter queues catch unprocessable messages and move them to a separate queue for further inspection, allowing operators to handle exceptions in a controlled manner.

Circuit breakers prevent cascading failures by halting communication with malfunctioning services until they recover, thus minimizing the impact of individual service failures on the overall system.

Security is another key consideration, and GoFr supports various authentication mechanisms, including OAuth, Basic Auth, and other secure communication methods, ensuring that data is transmitted securely between services.

Try using GoFr for your pub/sub systems built with Go, and see if you don’t reap the benefits I’ve described.

[
YOUTUBE.COM/THENEWSTACK
Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.
](https://youtube.com/thenewstack?sub_confirmation=1)