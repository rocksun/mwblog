# Integration of AI With IoT Brings Agents to Physical World
![Featued image for: Integration of AI With IoT Brings Agents to Physical World](https://cdn.thenewstack.io/media/2024/10/efc035ef-jorge-ramirez-1gldpzticru-unsplashb-1024x576.jpg)
The rise of generative AI and LLMs is going to significantly impact the [Internet of Things](https://thenewstack.io/what-does-it-mean-to-be-on-the-internet-of-things/) (IoT) and [edge computing](https://thenewstack.io/edge-computing/). With the evolution of [small language models](https://thenewstack.io/how-to-get-started-running-small-language-models-at-the-edge/) and [on-device models](https://thenewstack.io/google-wants-developers-to-build-on-device-ai-applications/), edge computing is beginning to leverage AI. Developers can now combine sensors, edge devices running on-device models, and [multimodal](https://thenewstack.io/gemini-all-you-need-to-know-about-googles-multimodal-ai/) AI models running in the cloud to build innovative solutions. This approach, when combined with [agentic workflows](https://thenewstack.io/semantic-router-and-its-role-in-designing-agentic-workflows/), takes automation to the next level.

One of the early examples of such innovation is the [SenseCAP Watcher](http://seeedstudio.com/watcher), an innovative physical AI agent developed by [Seeed Studio](https://www.seeedstudio.com/), which is designed to augment the capabilities of smart environments. It combines IoT, edge computing, on-device models, and multimodal AI models running in the cloud (or a data center) to run agentic workflows.

This article explores the hardware, software architecture, and integration features of the SenseCAP Watcher while highlighting its potential use cases for AI developers.

## Hardware Overview
The SenseCAP Watcher stands out due to its comprehensive hardware design. It incorporates several critical components that work in harmony to deliver an intuitive user experience.

At the heart of the Watcher is the [OV5647 camera module](https://www.seeedstudio.com/OV5647-69-1-FOV-Camera-module-for-Raspberry-Pi-3B-4B-p-5484.html?srsltid=AfmBOopBky9Q7r3SP8MtNyey5Iuo_tlIB08uAZgxWvRc-1y1QlcptiDn), which enables advanced computer vision capabilities. This component facilitates real-time monitoring and analysis of the environment.

Equipped with a microphone and speaker, the Watcher supports voice interactions, allowing users to issue commands and receive audio feedback seamlessly. The 1.46-inch touchscreen serves as the primary interface for navigating settings and accessing features, enhancing user engagement.

Built on the[ ESP32-S3 platform](https://esp32s3.com/), the Watcher supports both Wi-Fi and Bluetooth Low Energy (BLE) for efficient communication with other devices. It also includes a USB port for charging and data transfer, along with a microSD card slot to expand storage capabilities. The [Himax HX6538 chip](https://www.himax.com.tw/products/wiseeye-ai-sensing/wiseeye2-ai-processor/), featuring Cortex M55 and US5 cores, enables the Watcher to handle AI-related tasks, enhancing its operational intelligence and responsiveness. This chip is capable of running on-device [TinyML](https://www.tinyml.org/) models, providing local inference.

The[ I2C interface](https://learn.sparkfun.com/tutorials/i2c/all) at the back of the device supports over 100 [Grove](https://wiki.seeedstudio.com/Grove_System/) sensors, facilitating expansion and experimentation. There is also a [UART interface](https://docs.arduino.cc/learn/communication/uart/) to connect to external microcontrollers and boards from [Arduino](https://www.arduino.cc/) and [Raspberry Pi](https://www.raspberrypi.org/).

## Software Architecture
The [SenseCraft AI](https://sensecraft.seeed.cc/ai/#/home) platform powers the software architecture of the SenseCAP Watcher. This platform provides a robust framework for task orchestration, data processing, and user interactions.

The Task Orchestration Service enables the Watcher to process tasks via direct voice commands or through the SenseCraft Mate app. Tasks are routed through an HTTP interface, processed by AI models, and returned to the device for execution. The Watcher’s capability to analyze visual data is a game changer, allowing users to select between SenseCraft’s local models and third-party AI services for versatile image analysis and object detection.

A significant advantage of the SenseCAP Watcher is its hybrid processing capability, which leverages both on-device AI models and cloud-based LLMs. This flexibility allows developers to choose the best processing route based on the task requirements — whether they prioritize speed and responsiveness with local models, or leverage the extensive capabilities of cloud-based LLMs for complex analyses.

The Watcher’s capability to analyze visual data is a game changer.

The integration of SenseCAP Watcher with SenseCraft AI is a key differentiator in its functionality. The device can leverage both local processing and cloud-based LLMs, providing developers with multiple deployment options to enhance application performance. Users can choose between cloud-efficient processing, hybrid smart processing, and local secure processing flows — each offering a unique balance of efficiency, data security, and operational control.

When the agent selects the cloud-based LLM, the software behind the scenes converts the camera’s keyframe into a prompt and sends it to a highly capable multimodal AI model, which extracts the description in a structured format. Based on the response, it triggers the rest of the workflow. It is also possible to send the prompt to a local LLM running in a developer workstation or a powerful edge device, such as Nvidia Jetson Orin.

The device can deliver alerts through various channels, including push notifications via the SenseCraft cloud, UART connections to other hardware, and HTTP connections to local servers, ensuring users receive timely updates on monitored events.

Additionally, the Watcher supports integration with popular IoT platforms, such as Node-RED and Home Assistant. This compatibility allows developers to create complex automations and data flows, making it a versatile tool for various applications.

## Key Use Cases and Scenarios
The SenseCAP Watcher’s capabilities make it ideal for a wide range of applications. In smart home environments, the Watcher can monitor activity, detect unusual behaviors, and provide alerts to homeowners. For instance, it can recognize when a person enters a room and send a notification, enhancing security and awareness.

The open source nature of the device encourages developers to explore its capabilities, experiment with different sensors, and contribute to the growing ecosystem around the SenseCraft platform.

In retail settings, the Watcher can track customer movements and interactions, enabling store owners to analyze traffic patterns and optimize layout strategies for improved customer engagement. Similarly, in industrial automation, the device serves as a behavior sensor, providing real-time insights into equipment status and workforce activity, leading to reduced downtime and improved operational efficiency.

Developers looking to leverage the SenseCAP Watcher can easily get started by following comprehensive installation instructions, which include device binding and network configuration. The SenseCraft Mate mobile app serves as the primary interface for managing tasks, monitoring performance, and receiving alerts. It also facilitates firmware updates and device customization. The open source nature of the device encourages developers to explore its capabilities, experiment with different sensors, and contribute to the growing ecosystem around the SenseCraft platform.

The SenseCAP Watcher represents a leap forward in the AIoT landscape — the integration of AI with IoT technologies. By combining robust hardware with a flexible software architecture and extensive integration options, it provides developers with a powerful tool to create intelligent applications across various domains. The hybrid approach of utilizing both on-device models and LLMs allows for optimal performance tailored to specific use cases, enhancing its usability.

In the next part of this series, I will walk you through the steps involved in building a physical AI agent powered by SenseCraft Watcher and a vision language model. Stay tuned!

[
YOUTUBE.COM/THENEWSTACK
Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.
](https://youtube.com/thenewstack?sub_confirmation=1)