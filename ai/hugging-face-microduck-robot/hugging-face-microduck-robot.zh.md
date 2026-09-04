你可以在圣诞节前让一只机械鸭子在家里摇摇晃晃地走动。

[Hugging Face](https://thenewstack.io/how-hugging-face-positions-itself-in-the-open-llm-stack/) 旗下的 Pollen Robotics 周四开启了 [Microduck](https://pollen-robotics.com/microduck/) 的预购，这是一款售价 399 美元（早鸟价）的双足鸭形机器人。它能走路、摇摆，甚至还能使用轮滑（！），并能用嘴捡起物体。当它摔倒时，还能自己爬起来。

该公司预计在圣诞节前完成 Microduck 的首次发货。目前在北美和欧洲[有售](https://store.pollen-robotics.com/products/microduck)。

Microduck 是 Hugging Face 和 Pollen 去年推出的桌面机器人 [Reachy Mini](https://pollen-robotics.com/reachy-mini/) 的后续产品。Reachy Mini 是一款固定式机器人，专注于与人类交互。Pollen 目前仍在销售 Reachy 2，那是一款面向研究实验室的更大、更昂贵的人形机器人。该团队在[公告](https://pollen-robotics.com/microduck/blog/introducing-microduck/)中写道，Microduck 旨在专注于“行动”。

![](https://cdn.thenewstack.io/media/2026/08/ebeaca03-screenshot-2026-08-27-at-9.18.34-am-1024x582.png)

图片来源：Pollen Robotics。

“你如何教机器人移动？你如何训练仿真环境中的行为，将其转移到真实硬件上，查看哪里出了问题，然后再次尝试？当机器人可以离开桌面、携带东西、摔倒并恢复时，会发生什么变化？对于想要训练物理行为、试验强化学习并测试 AI 如何从仿真走向现实世界的开发者来说，这是一个理想的平台，”该团队写道。

## 不仅仅是玩具

事实上，Microduck 不仅仅是一个 25 厘米高的玩具。它是一个带有 SDK、虚拟训练环境和强化学习脚本的开源平台，可以帮助开发者训练机器人执行新任务。代码采用 Apache 2.0 协议，不过硬件设计文件是商业非许可的，所以没人能制造并销售其克隆品。

对于那些只想玩玩鸭子机器人的用户，我们还提供了一个完整的[模拟器](https://huggingface.co/spaces/pollen-robotics/microduck-simulator)；如果你真的购买了一台，你还会得到一个游戏手柄来实时操控机器人。

![](https://cdn.thenewstack.io/media/2026/08/f73a203c-634210931-50c3d537-8db2-4005-9d9c-3472faeec4d0.gif)

图片来源：Pollen Robotics。

但如果你想深入研究，可以使用物理模拟器来教机器人新的动作。例如，在该项目的 [GitHub 页面](https://github.com/pollen-robotics/microduck_rl)上，该团队详细介绍了如何并行训练 4,096 只虚拟鸭子的行走策略，这通常在一到两个小时内就能产生可用的步态。该仓库共记录了 13 个任务系列，包括前滚翻和六个围绕脚下被动轮设计的任务。

要训练该机器人，你需要一块 Nvidia GPU，或者你也可以使用 Hugging Face 自己的基础设施进行训练。这不是偶然的。鸭子运行的模拟器是 MuJoCo Warp，它构建在 Nvidia 的 Warp 框架之上，而底层的训练框架 [mjlab](https://github.com/mujocolab/mjlab) 重新实现了 Nvidia 自家 Isaac Lab 的 API。

开箱即用，该机器人自带七种预训练动作，包括行走、坐下和站立、踢球、用嘴抓取物体、轮滑以及从地面爬起。

## 硬件内部

至于硬件，该机器人的重量约为 800 克，由带有 AI 加速器的 Rockchip RK3566 驱动。这基本上是一个四核 Arm Cortex-A55 处理器，配备 Mali GPU。不过，由于据报道 Nvidia [正在洽谈收购](https://techcrunch.com/2026/08/26/nvidia-closes-in-on-hugging-face-acquisition/) Hugging Face（该交易首先由 The Information 报道），我预计未来的版本可能会使用性能更强的 Nvidia 自研芯片。

![](https://cdn.thenewstack.io/media/2026/08/c45c4606-sim2real.gif)

图片来源：Pollen Robotics。

它拥有 1GB 的板载内存和 32GB 的存储空间。

不过，更重要的是它配备的传感器。它有一个前置摄像头、一个带有 8×8 飞行时间矩阵的小型激光雷达传感器，以及 2 个惯性测量单元 (IMU)。摄像头和激光雷达让它能够观察并定位周围物体，而 IMU 则负责跟踪其方向和平衡。

该团队仍在完善最终的摄像头分辨率和激光雷达量程。

Pollen Robotics 还将销售一些配件，例如售价 39 美元的充电包（含两块电池和一个充电器），以及售价 119 美元的开发包（含三个备用电机、五根电机线、两块电池、一个双充电器、十个 NFC 标签、Hugging Face 点数、螺丝和一把螺丝刀）。

机器人还配有麦克风和扬声器。这里有一个有趣的细节：当你第一次打开机器人时，它会生成自己独特的标志性声音，这与任何其他 Microduck 都不同。不过正如团队所指出的，机器人并不会说话，Microduck “通过奇怪的小声音进行交流，更像是一个生物而不是助手。”

## 更多的鸭子，更多的乐趣

该团队表示，将多只机器人放在一起才能让它们真正变得生动。“比赛、足球，或者仅仅是机器人之间互相反应，都能让体验变得更加鲜活。对于开发者来说，这也是在没有一屋子昂贵硬件的情况下探索多机器人行为的实用方式，”他们写道。

归根结底，这也就是一个有趣的项目。在这个令人沮丧的世界里，我们时不时都需要一些可爱的鸭子乐趣。