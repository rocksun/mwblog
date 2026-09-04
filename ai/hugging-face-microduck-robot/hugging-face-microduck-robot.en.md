You could have a mechanical duck waddling through your home before Christmas.

[Hugging Face](https://thenewstack.io/how-hugging-face-positions-itself-in-the-open-llm-stack/)‘s Pollen Robotics on Thursday opened pre-orders for the [Microduck](https://pollen-robotics.com/microduck/), a $399 (introductory) bipedal duck-adjacent robot that can walk, waddle, and use roller-skates(!), with a beak to pick up objects. And when it falls, it can get back up, too.

The company expects to make the first deliveries of the Microduck before Christmas. It’s [available](https://store.pollen-robotics.com/products/microduck) in North America and Europe.

Microduck is the follow-up to [Reachy Mini](https://pollen-robotics.com/reachy-mini/), the desktop robot Hugging Face and Pollen launched last year, which was stationary and focused on interacting with humans. Pollen also still sells Reachy 2, a far larger and pricier humanoid aimed at research labs. Microduck, the team writes in its [announcement](https://pollen-robotics.com/microduck/blog/introducing-microduck/), is meant to focus on action.

![](https://cdn.thenewstack.io/media/2026/08/ebeaca03-screenshot-2026-08-27-at-9.18.34-am-1024x582.png)

Credit: Pollen Robotics.

“How do you teach a robot to move? How do you train a behavior in simulation, transfer it to real hardware, see what went wrong, and try again? What changes when the robot can leave the desk, carry something, fall over, and recover? It is an ideal platform for developers who want to train physical behaviors, experiment with reinforcement learning, and test how AI moves from simulation into the real world,” the team writes.

## Not just a toy

And indeed, Microduck is not just a 25cm-tall toy. It’s an open-source platform with an SDK, virtual training environment, and reinforcement learning scripts to help developers train the robot to perform new tasks. The code is Apache 2.0, though the hardware design files are licensed non-commercially, so nobody is building and selling a clone.

There’s also a full [simulator](https://huggingface.co/spaces/pollen-robotics/microduck-simulator) for those of us who just want to play with a duck robot, but if you do buy one, you’ll also get a game controller to control the robot on the fly, too.

![](https://cdn.thenewstack.io/media/2026/08/1a8ae475-microduck-kickabout-1024x577.jpg)

Credit: Pollen Robotics.

But if you want to go deep, you can use the physics simulator to teach the robot new movements. On the project’s [GitHub page](https://github.com/pollen-robotics/microduck_rl), the team notes how to train the duck’s walking policy across 4,096 virtual ducks in parallel, for example, which results in a usable gait in one to two hours. The repo registers 13 task families in all, including a forward roll and six built around a set of passive wheels that go under the feet.

To train the robot, you’ll need an Nvidia GPU, or you can train it on Hugging Face’s own infrastructure. That’s not incidental. The simulator the ducks run in is MuJoCo Warp, built on Nvidia’s Warp framework, and [mjlab](https://github.com/mujocolab/mjlab), the training framework underneath, reimplements the API of Nvidia’s own Isaac Lab.

Out of the box, the robot comes with seven trained moves, including walking, sitting and standing, kicking, grabbing objects with its beak, roller skating, and getting back up off the ground.

## Inside the hardware

As for the hardware, the robot will weigh in at about 800 grams and will be powered by a Rockchip RK3566 with AI accelerator. That’s basically a quad-core Arm Cortex-A55 with a Mali GPU. But now that Nvidia is [reportedly in talks](https://techcrunch.com/2026/08/26/nvidia-closes-in-on-hugging-face-acquisition/) to acquire Hugging Face, in a deal first reported by The Information, I would expect a future version to use a slightly more powerful Nvidia-made chip.

![](https://cdn.thenewstack.io/media/2026/08/c45c4606-sim2real.gif)

Credit: Pollen Robotics.

It features 1GB of on-board memory and 32 GB of storage.

What’s more important, though, is its set of sensors. There’s a single front camera, a small LiDAR sensor with an 8×8 time-of-flight matrix, and 2 inertial measurement units. The camera and LiDAR let it see and place objects around it, while the IMUs keep track of its orientation and balance.

The team is still working out what the final camera resolution and LiDAR range will be.

Pollen Robotics will sell a few accessories as well, including, for example, a Charger Pack for $39 with two batteries and a charger, and a Dev Pack for $119 with three spare motors, five motor cables, two batteries, a dual charger, ten NFC tags, Hugging Face credit, screws, and a screwdriver.

![](https://cdn.thenewstack.io/media/2026/08/f73a203c-634210931-50c3d537-8db2-4005-9d9c-3472faeec4d0.gif)

Credit: Pollen Robotics.

The robot also comes with microphones and a speaker. One interesting note here: when you first turn the robot on, it generates its own signature sound that is different from any other Microduck. The robot doesn’t speak, though, as the team notes, the Microduck “communicates through weird little sounds, closer to a creature than an assistant.”

## Everything is better with more ducks

The team says having several of them together is what really makes the robots come alive. “Races, football, or simply robots reacting to one another immediately make the experience feel more alive. For developers, it also creates a practical way to explore multi-robot behaviors without a room full of expensive hardware,” they write.

At the end of the day, this is also just a fun project, and in this depressing world, we all deserve some ducking fun every now and then.


[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://thenewstack.io/wp-content/uploads/2025/03/15a7eb12-cropped-4e88ac40-frederic-profile-2-600x600.jpg)

Before joining The New Stack as its senior editor for AI, Frederic was the enterprise editor at TechCrunch, where he covered everything from the rise of the cloud and the earliest days of Kubernetes to the advent of quantum computing....

Read more from Frederic Lardinois](https://thenewstack.io/author/frederic-lardinois/)