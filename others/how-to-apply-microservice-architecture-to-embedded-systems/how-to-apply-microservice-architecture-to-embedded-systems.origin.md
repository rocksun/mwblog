# How to Apply Microservice Architecture to Embedded Systems
![Featued image for: How to Apply Microservice Architecture to Embedded Systems](https://cdn.thenewstack.io/media/2024/07/f1de25f7-how-to-apply-microservice-architecture-to-embedded-systems-2-1024x576.jpg)
It’s no wonder that [microservices](https://thenewstack.io/microservices/) architecture is foundational to the distributed applications published by global enterprises like Facebook, [Netflix](https://thenewstack.io/how-culture-impacts-technology-choice-a-review-of-netflixs-use-of-microservices/) and [Uber](https://thenewstack.io/devpod-ubers-monorepo-based-remote-development-platform/). Isolating services at a fine grain and then aggregating them to work in concert makes for distributed systems less cumbersome to manage than monolithic systems.

But, for embedded systems — applications made up of small, dedicated computers that are physically embedded in a particular device that work together towards a common purpose — things are a bit different.

Unlike microservice-oriented architectures (MOAs) that run in and across data centers, embedded systems tend to be specialized in terms of hardware and use case — for example, running a fleet of robotic workers operating in an industrial assembly plant or controlling a self-driving car.

Microservice-oriented architecture can be applied to these types of environments, but special considerations need to be made. When things go wrong, you can’t just spin up another container to replace the failing one. More is needed.

Programming microservice-oriented architecture for embedded systems requires a different design and implementation approach. This article describes this approach.

## Microservice-Oriented Architecture 101
Before we go into the details of applying an MOA to embedded systems, let’s start with a general understanding of the architecture’s essentials.

Microservice-oriented architecture is about breaking up the behavior of an application into discrete services that exist independently yet act in concert. The way that an MOA works is that discrete services are distributed to a variety of remote locations.

Typically, these services send and receive data using a well-known transport protocol such as TCP, UDP or HTTP. Some type of organizing, frontend client mechanism, such as a web page or native code running on desktop or mobile devices, aggregates the various services together into a unified representation of the overall application. However, as mentioned previously, each of the services that make up the MOA are hosted remotely.

The application’s frontend calls into a remote routing/controller service. The routing/controller service knows the location of the microservices that make up the application and forwards the call to the appropriate service according to some sort of identifier that is part of the calling code. The microservice processes the call and sends the result back to the router/controller for further processing — or, if the given call is complete, a response is sent back to the calling client.

![Figure 1: The basic pattern for a microservice-oriented architecture.](https://cdn.thenewstack.io/media/2024/07/5fdd3c4a-microservices-figure-01-1024x576.png)
Figure 1: The basic pattern for a microservice-oriented architecture.

The idea of separating an application into functionality that is hosted at remote locations has its beginnings with remote procedure calls (RPC). The MOA builds upon the RPC pattern by adding a set of conventional requirements. Under an MOA, each microservice:

- Supports a single concern.
- Is discrete.
- Carries its own data.
- Is transportable.
- Is ephemeral.
Here’s what each of those requirements mean:

### Supports a Single Concern
A microservice should confine its behavior to a single concern, such as: a login service, an ordering service, a purchase, a service to handle credit card transactions, a service for supporting customer profiles, a service to perform tax calculations, or a logging service.

One microservice can use another microservice; for example, a purchasing service can use a tax calculation service to determine the total amount of the order. However, no two services should be combined into one code base or a single deployment unit.

### Is Discrete
A microservice should be discrete in that it should confined to a single deployment unit and well bounded on the network. That deployment unit might be a Linux container or it might be a code artifact such as a Java .jar file, a .NET DLL, or a Rust binary file. In the case of an embedded system, the deployment unit might be an actual piece of hardware.

A microservice’s internals should be private and inaccessible to the public. However, public access should be provided by a well-defined API.

### Carries Its Own Data
A microservice carries its own data and does not share data with another microservice other than through its API. Typically, a microservice will have its own database or well-isolated tables in a database. While data redundancy among microservices can occur, this condition is acceptable and necessary for a microservice to maintain its own operational state and boundaries.

### Is Transportable
A microservice must be able to be transported to any hosting environment at any time. Transportability is important in a situation in which a microservice is running on a machine that fails, for example, losing electric power, and must be redeployed to another functioning machine.

### Is Ephemeral
A microservice must be able to be created or destroyed on demand. This is particularly important in situations where a microservice performs high-intensity computing and only needs to exist to meet a momentary demand. For example, a microservice performs special effects processing on a particular video file.

## What’s So Special About MOAs for Embedded Devices?
Implementing an MOA for an embedded environment requires a different approach than writing one for a data center application.

For starters, most data centers use the Linux operating system to drive their machines. Linux is a full-powered operating system that takes a good deal of room, both in terms of memory and on disk. Even with a stripped-down distribution of Linux such as Alpine, which only has essential features, that OS weighs in at 5 MB of storage.

Many embedded chips, such as the EPS32, ship with about 520KB of internal RAM, of which some of that capacity is dedicated to non-volatile storage. Some chips can have up to 4 MB of RAM and 2 MB to 16 MB of Flash Memory when a special configuration is used.

Still, when an embedded device has a limited amount of storage, under 4MB, there’s no way that Linux is going to work. Rather, embedded devices generally use some version of a real-time operating system (RTOS). FreeRTOS, the operating system used on the ESP32 chipset, requires only 5 to 10 KB of storage of code, with RAM usage going as low as 300 KB. As you can see, the system requirements for embedded devices are minuscule compared to a machine running in a data center.

Also, while Linux supports [containers](https://thenewstack.io/containers/), allowing multiple microservices to run within a cluster of virtual machines, container support is more the exception than the rule in an embedded system. Typically, a microservice will run on a dedicated, embedded microprocessor. The one-to-one relationship between the microservice and the hardware that runs the microservice affects how a microservice is deployed and upgraded.

It’s not a matter of using a container management framework such as [Kubernetes](https://thenewstack.io/kubernetes/) to redeploy containers. Rather, to do upgrades, a direct connection to the embedded processor is required, and in many cases, the device that’s the target of the upgrade needs to be deactivated.

For example, upgrading the microservice running the braking system of an automobile requires the car to be off-road and stationary.

In short, the process of deploying and upgrading microservices for an embedded system has a strong dependency on the physical state of the system’s hardware. But there’s another significant constraint as well: data exchange.

Data exchange between embedded devices is best implemented using a binary data format. Space and bandwidth capacity are limited in an embedded processor, so text-based formats such as XML and JSON won’t work well.

Rather, a binary format such as protocol buffers or a custom binary format is better suited for communication in an MOA scenario in which each microservice in the architecture is hosted on an embedded processor.

However, data exchange between embedded processors that run onboard within a particular device, such as an automobile, and external devices, such as a cellphone, requires special consideration. Most embedded processors ship with other chips on a small mini-board, as shown in Figure 2.

![Figure 2: The ESP32 mini-board supports Bluetooth and Wi-Fi communication.](https://cdn.thenewstack.io/media/2024/07/43ddcceb-microservices-figure-02-300x227.png)
Figure 2: The ESP32 mini-board supports Bluetooth and Wi-Fi communication.

These mini-boards have Bluetooth and Wi-Fi capabilities built-in. Embedded chipsets can communicate with off-board devices using these capabilities. In cases where the embedded chipset is communicating with a known external device, according to a known format, communication using binary formats is still viable.

However, there are cases, such as communication using HTTP to a remote web API, when the bulkier text-based data formats are the prescribed means of data exchange. Having each embedded chipset engage in text-based communication can be a problem, given the storage and memory constraints of the chip.

The alternative is to conduct communication with external devices using a dedicated proxy chipset that supports HTTP and has enhanced storage and memory capabilities. The dedicated proxy manages communication with external targets from other onboard embedded processors. (See Figure 3.)

![Figure 3: A dedicated proxy to external targets enables embedded chipsets to communicate efficiently.](https://cdn.thenewstack.io/media/2024/07/50d14b93-microservices-figure-03-1024x710.png)
Figure 3: A dedicated proxy to external targets enables embedded chipsets to communicate efficiently.

Service routing is another consideration. Just as an MOA running in a data center needs an API Gateway to route traffic to designated microservices, an MOA running in an embedded environment also needs such a router/controller mechanism. In an automobile, the router/controller is the electronic control unit (ECU) that runs on the automobile’s controller area network (CAN). (See Figure 4.)

![Figure 4: The CAN in an automobile uses an electronic control unit (ECU) to coordinate data exchange between microservices running on embedded devices.](https://cdn.thenewstack.io/media/2024/07/0694890b-microservices-figure-04-1024x564.png)
Figure 4: The CAN in an automobile uses an electronic control unit (ECU) to coordinate data exchange between microservices running on embedded devices.

The ECU is aware of all the components running within an automobile and can route traffic accordingly. Also, the ECU can be the point of control that maintains global state.

Many traditional distributed applications can operate without each microservice in the application being immediately aware of the overall state of the application. However, knowing the system’s overall state is important for microservices running within an embedded system.

For example, when the sensors in a self-driving vehicle see an obstruction in the road, the braking systems need to know that the vehicle is in a dangerous global state so they can react accordingly, hence the need for a universal awareness of global state.

Flight control systems (FCS) and building management systems (BMS) also have a mechanism for maintaining and reporting global state. In an FCS, the control mechanism is called a flight management system or flight management computer.

In a BMS, the component is called a building automation controller or building automation system controller. A building automation controller reports the state of all subsystems in a building, such as HVAC, lighting, security, elevators, electrical systems, and fire safety equipment.

The important thing to understand is that any embedded system will need a routing mechanism to coordinate traffic and data exchange among the various devices that make up the system.

## Putting It All Together
The explosive growth of the Internet of Things and smart devices — everything from smart homes to autonomous automobiles to factories run by robots and everything in between — provides increased opportunities for software developers who are well-versed in microservice-oriented architecture to get involved with embedded systems.

Applying a microservice-oriented architecture to an embedded system requires some new knowledge and a slightly different approach to software development from the usual practices used to create business applications that run on virtualized environments in data centers. But considering the opportunities at hand, it’s worth tackling the challenge, given the potential for a large return on investment.

[
YOUTUBE.COM/THENEWSTACK
Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.
](https://youtube.com/thenewstack?sub_confirmation=1)