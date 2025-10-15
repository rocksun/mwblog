The initial reaction from developers and makers to the [news](https://www.youtube.com/live/uYb8YzdMWbc) that Qualcomm is buying Arduino, the open source electronic prototyping platform, has been less than positive. Qualcomm maintains that Arduino will remain an open ecosystem and the company will be an independent subsidiary that works with multiple silicon vendors — just with more reach now.

The concern is that Qualcomm might fail to invest in Arduino or misunderstand its strengths. But ironically, that’s exactly why Qualcomm needs Arduino: to help it work better with developers and makers.

## Qualcomm’s Strategic Play for the Developer Community

Although Arduino has around 30,000 business customers for its industrial and enterprise [Pro boards](https://www.arduino.cc/pro/), what Qualcomm is after is its worldwide community of over 33 million makers and developers — not to mention its pervasive presence in hardware startups, who use Arduino for everything from prototyping to running test systems in their labs. The idea might be to upsell these existing users to more powerful compute, especially for edge AI and robotics.

Arduino itself has a somewhat tangled and occasionally contentious history as a company. It’s a long way from the plucky academic startup, having gone through [a fractious disagreement about trademarks and manufacturing rights](https://makezine.com/article/maker-news/arduino-cc-arduino-org-reconcile-settlement-agreement-become-one-company/) and raised [$54 million in VC funding](https://blog.arduino.cc/2023/09/06/what-will-we-do-with-an-additional-22m/) since 2022. But continuing to open source tools and specifications takes a lot of resources.

The company never quite managed to create the [promised Arduino Foundation](https://hackaday.com/2017/06/19/the-arduino-foundation-whats-up/), which was supposed to handle governance of the Arduino IDE — software that’s been the gateway to making embedded systems programming accessible to a generation of developers. So can Arduino keep its independence, [stay open](https://content.arduino.cc/assets/Arduino%20Open%20Source%20Report%202024.pdf), and teach Qualcomm how to understand and support developers?

> “Qualcomm’s acquisition of Arduino, following its earlier integrations of Foundries.io and Edge Impulse, signals a strategic shift toward empowering developers with a self-service approach.”  
> **– Leendert van Doorn, Qualcomm Senior VP of engineering**

“Qualcomm’s acquisition of Arduino, following its earlier integrations of Foundries.io and Edge Impulse, signals a strategic shift toward empowering developers with a self-service approach,” senior vice president of engineering [Leendert van Doorn](https://www.linkedin.com/in/leendert-van-doorn-740170/) told The New Stack.

“Specifically, for the Arduino UNO Q board, all source code is openly available and integrated into upstream repositories, allowing developers to build and customize software independently of Qualcomm. This move establishes a new standard for future Linux-based products from the company.”

Culture changes like this don’t just make Qualcomm easier for developers to work with; they also make it more likely that Arduino will stay truly independent. So far that’s happened for Foundries.io (which was bought by Qualcomm last year) and Edge Impulse still supports multiple hardware vendors. But like all culture changes, Qualcomm won’t become more open overnight.

> “It will be interesting to see whether and how Qualcomm sustains Arduino’s open source ethos…”  
> **– James Governor, RedMonk cofounder and analyst**

“Qualcomm’s business is predicated on selling to customers buying in volume, so this is certainly a change,” RedMonk cofounder and analyst [James Governor](https://www.linkedin.com/in/jamesgovernor/) told us. “It will be interesting to see whether and how Qualcomm sustains Arduino’s open source ethos, and whether it can help Arduino capture new markets — namely robotics. Arduino is currently very much skewed to the hobbyist market, however.”

That might require a balancing act, Governor suggested: can Qualcomm “manage to be both hands off enough not to mess up what it’s acquiring, and yet hands on enough to reposition Arduino as a prototyping platform for robotics and industrial manufacturing companies”?

## Bringing Two Worlds Together With the UNO Q Board

Arduino and Qualcomm didn’t just announce the acquisition; they’ve already worked together to build a $44 board called the [UNO Q](https://www.arduino.cc/product-uno-q). That’s a fairly typical Arm SBC (a single-board computer that integrates CPU, GPU, RAM and storage for embedded applications like IoT, industrial controllers and robotics) with a budget Qualcomm Dragonwing processor running full Debian Linux. But it also has an Arduino microcontroller on the back for working with the sensors and actuators you need for actually building the kind of robotics and “everyday IoT devices” Qualcomm recommends the Dragonwing for, with an Arduino bridge library handling the communication between them.

> Arduino and Qualcomm have already worked together to build a $44 board called the UNO Q.

This isn’t the first attempt at putting Arduino and Linux on the same system, but it might be the first one to be successful. The Arduino Yun (which used a fairly obscure Linux distro) and the TRE (cancelled due to lawsuits) didn’t have much of an impact and Arduino’s Portenta X8 is firmly aimed at its industrial customers.

Combining sensors, controls and an AI vision model that works with them is getting common in industrial IoT. But makers who need their device to have a complex user interface and data storage or something as demanding as on-board AI, as well as reading sensors and controlling motors or other electronics, have usually had to [integrate the two systems themselves](https://raspberrypicase.com/can-raspberry-pi-and-arduino-work-together-and-how/), which usually means extra components for connectivity.

That’s something Arduino has wanted to address for a while. It’s hoping to deliver a product with the power of a Raspberry Pi in the classic UNO form factor (and pin layout) — familiar to existing Arduino users — and compatible with the existing shields that add features and connectivity to Arduino boards. The price is certainly comparable to a high-end Pi; the performance might not be, although Qualcomm is claiming the systems will be ideal for running local AI models (you’re also getting the real-time control built in).

## The New App Lab Development Environment

That means you need more than just the Arduino IDE to work with the UNO Q, so there’s a new (also open source) [App Lab development environment](https://www.arduino.cc/en/software/#app-lab-section) that supports Arduino, C++ Python, Linux and AI workflows with libraries and modular components called ‘bricks’, without developers needing to think about complexities like handling Docker containers. If you want to build a smart lock with image recognition in Python running on Linux with a USB webcam and then have the Arduino drive the motor that unlocks the door when it recognizes you, App Lab gives you one place to do that.

[![Arduino UNO Q](https://cdn.thenewstack.io/media/2025/10/4670ed28-image3-6.png)](https://cdn.thenewstack.io/media/2025/10/4670ed28-image3-6.png)

The UNO Q gives you a whole development stack; image credit: Qualcomm

A clever twist: although you can run App Lab on your usual computer, it’s also preinstalled on the UNO Q: Just plug in a screen and keyboard and then you can use Debian running on the Dragonwing to program the Arduino MCU.

Arduino was already working with [Edge Impulse](https://edgeimpulse.com/arduino-integrations), another recent Qualcomm acquisition for making it easy to go from sensor data to a deployed AI model. App Lab includes several of their pre-built AI models that run on the UNO Q — including object detection, audio classification like recognizing a ‘wake word’ (if you connect a microphone), computer vision (just plug in a USB webcam) and anomaly detection. The Dragonwing’s GPU supports OpenCL and developers can upload or train their own models using App Lab or the standard Edge Impulse CLI workflow.

App Lab also uses Arduino Cloud for device lifecycle management and remote updates. And if you want to use custom Debian or Yocto images, App Lab uses another recent Qualcomm acquisition, FoundriesFactory, which offers [a SaaS platform for open source embedded development](https://foundries.io/products/) (similar to AWS IoT or Azure Sphere).

## How Arduino Is Opening Up Qualcomm’s Ecosystem

Arduino was the first system that made it easy for any developer to get started with embedded systems and it’s the standard for prototyping, but it has a lot of competition now: Adafruit with Circuit Python, the PlatformIO IDE that works with multiple hardware options, ExpressIf ESP boards, and pre-certified Matter stacks from big-name vendors like Nordic, NXP and Silicon Labs that let developers write applications and treat the hardware as just a platform. Qualcomm’s backing may take the pressure off a little, as well as allowing Arduino to expand into the now-obligatory AI areas.

Arduino doesn’t have as strong a reputation in professional manufacturing as it does in the maker market, particularly in devices that need compliance and interference testing. Qualcomm’s experience in phones and automotive may give it a leg up there.

The idea that a startup could go from prototyping with a maker board to getting runs of a custom design that integrates everything with the same supplier isn’t always realistic, but Qualcomm is likely betting that hardware startups that start with their chip in a prototype will stick with that for the AI half of a device that can’t be replaced by a custom logic board.

> Qualcomm needs to learn to better support developers; and that’s an area where Arduino has a lot to teach them.

To appeal to those potential joint customers, Qualcomm needs to learn to better support developers; and that’s an area where Arduino has a lot to teach them.

What developers have typically got from Qualcomm in the past have been evaluation and developer kits, often with specific hardware accessories for prototyping devices, or modules and reference designs — sometimes offered in conjunction with [platform vendors like Microsoft](https://azure.microsoft.com/en-us/blog/microsoft-and-qualcomm-accelerate-ai-with-vision-ai-developer-kit/?msockid=008cd2595c2d61d01ab4c3ac582d631f). That’s a good fit for the device manufacturers that have been Qualcomm’s typical customers, but it hasn’t always worked as well for more general developers.

A decade ago it worked with Arrow, which made the [DragonBoard](https://www.arrow.com/en/research-and-events/articles/qualcomm-snapdragon-with-arrow) — the first development board with Snapdragon chips preloaded with Android, aimed at IoT and embedded developers. That didn’t make much of an impression on the market. More recently, the Snapdragon X Elite Dev Kit it designed with Microsoft — to give developers a desktop box for building apps for Arm-based Copilot+ laptops — was [repeatedly delayed and then abruptly cancelled](https://www.jeffgeerling.com/blog/2024/where-qualcomms-snapdragon-x-elite-dev-kit). Qualcomm said it didn’t meet its usual standards and Microsoft suggested that with all the delays, developers could already buy more powerful laptops.

## Arduino Changing How Qualcomm Delivers Hardware and Software

The UNO Q is a much more open-ended proposition; no signing up to terms and conditions just to see information about the hardware, and you can just order it from the Arduino store like any other board. It’s open source hardware with the usual Hardware Abstraction Layer, so code can be portable between different boards. The [schematics, pinout and CAD files are already available](https://docs.arduino.cc/hardware/uno-q/), so in theory other manufacturers can produce compatible boards (although they would have to be Qualcomm partners to get the Dragonwing processors, and might need to order in unfeasibly large numbers).

That’s the first sign that Arduino is already changing the way Qualcomm delivers both hardware and software. Typically, Qualcomm offers closed-source SDKs — like the Qualcomm Neural Processing SDL, whose late delivery for Windows meant Arm-based Copilot+ notebooks were on sale first but not useful for developers until months later — with support for common open source projects.

> While Qualcomm doesn’t have the same track record for sustained open source contributions as Arduino, it’s been ramping up its upstream contributions to Linux, Mesa, U-boot and open source AI projects…

And while Qualcomm doesn’t have the same track record for sustained open source contributions as Arduino, it’s been ramping up its upstream contributions to Linux, Mesa, U-boot and open source AI projects that can use its chips.

What runs on the Dragonwing is standard Debian Linux, chosen to appeal to developers (for prototyping if not for production use). In a first for Qualcomm, [the project was built on upstream Debian](https://github.com/arduino/arduino-deb-images/tree/428f37ea60bcc8ff87bc1e438554485a3691b0fd), continually rebasing the latest kernel and submitting their patches as they went along, which means the patch quality has to be good enough to get accepted upstream while the project is in progress, rather than waiting until the end and hoping it happens quickly.

That’s a developer-friendly approach that’s on track to become the norm for all Qualcomm’s Linux-enabled devices, where developers don’t need to ask Qualcomm for information, let alone permission: they can just pick it up and make any changes they need.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://cdn.thenewstack.io/media/2023/12/e2700739-maryb.jpg)

After completing an MSc in Intelligent Knowledge Based Systems in 1990, Mary Branscombe was convinced that promising as the AI techniques she’d been studying were, they weren’t even close to being ready. Since then, she’s been a technology journalist for...

Read more from Mary Branscombe](https://thenewstack.io/author/marybranscombe/)