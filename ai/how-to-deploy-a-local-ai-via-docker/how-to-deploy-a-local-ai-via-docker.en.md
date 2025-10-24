If you’re tired of worrying about your [AI queries](https://thenewstack.io/why-ai-and-sql-go-together-like-peanut-butter-and-jelly/) or the data you share within them being used to either [train large language models (LLMs)](https://thenewstack.io/meeting-the-operational-challenges-of-training-llms/) or to create a profile of you, there are always local AI options you can use. I’ve actually reached the point where the only AI I use is local. For me, it’s not just about the privacy and security, but also the toll AI takes on the energy grids and the environment. If I can do my part to prevent an all-out collapse, you bet I’m going to do it.

Most often, I deploy local AI directly on my machine. There are, however, some instances where I want to quickly deploy a local AI to a remote server (either within my [LAN](https://thenewstack.io/connect-to-a-local-ollama-ai-instance-from-within-your-lan/) or a server beyond it). When that need arises, I have two choices:

* Install a local AI service in the same way I install it on my desktop.
* Containerize it.

The benefit of containerizing it is that the locally installed AI is sandboxed from the rest of the system, giving me even more privacy. Also, if I want to stop the locally installed AI, I can do so with a quick and easy [Docker command](https://thenewstack.io/how-to-use-the-docker-exec-command/).

I would go so far as to say that containerizing your local AI is the fastest and easiest way to get it up and running.

Thanks to Docker.

That’s right, we’re going to deploy a local AI service as a Docker container.

Let me show you how this is done.

## What You Need

First off, you need an operating system that supports Docker, which can be [Linux](https://thenewstack.io/introduction-to-linux-operating-system/), macOS or Windows. You’ll also need enough space on the system to pull whatever LLM you want to use. Finally, you’ll need a user with admin privileges and a network connection. I’m going to demonstrate this on Ubuntu Server 24.04.

## Install Docker

The first thing we have to do is install Docker. Here’s how.

First, you’ll need to add the official Docker GPG key with the commands:

This file contains hidden or bidirectional Unicode text that may be interpreted or compiled differently than what appears below. To review, open the file in an editor that reveals hidden Unicode characters.
[Learn more about bidirectional Unicode characters](https://github.co/hiddenchars)








|  |  |
| --- | --- |
|  | sudo apt-get update |
|  | sudo apt-get install ca-certificates curl |
|  | sudo install -m 0755 -d /etc/apt/keyrings |
|  | sudo curl -fsSL https://download.docker.com/linux/ubuntu/gpg -o /etc/apt/keyrings/docker.asc |
|  | sudo chmod a+r /etc/apt/keyrings/docker.asc |

Next, add the required Docker repository with the command:

This file contains hidden or bidirectional Unicode text that may be interpreted or compiled differently than what appears below. To review, open the file in an editor that reveals hidden Unicode characters.
[Learn more about bidirectional Unicode characters](https://github.co/hiddenchars)








|  |  |
| --- | --- |
|  | echo \ |
|  | "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.asc] https://download.docker.com/linux/ubuntu \ |
|  | $(. /etc/os-release && echo "${UBUNTU\_CODENAME:-$VERSION\_CODENAME}") stable" | \ |
|  | sudo tee /etc/apt/sources.list.d/docker.list > /dev/null |
|  | sudo apt-get update |

Install the required software with the following command:

This file contains hidden or bidirectional Unicode text that may be interpreted or compiled differently than what appears below. To review, open the file in an editor that reveals hidden Unicode characters.
[Learn more about bidirectional Unicode characters](https://github.co/hiddenchars)








|  |  |
| --- | --- |
|  | sudo apt-get install docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin git -y |

To run the Docker command as a standard user, you’ll need to add that user to the Docker group. This is done so you can run the Docker command without sudo privileges. Add your user to the Docker group with:

This file contains hidden or bidirectional Unicode text that may be interpreted or compiled differently than what appears below. To review, open the file in an editor that reveals hidden Unicode characters.
[Learn more about bidirectional Unicode characters](https://github.co/hiddenchars)








|  |  |
| --- | --- |
|  | sudo usermod -aG docker $USER |

Log out and log back in so the changes take effect.

## Deploying a Local AI With Docker

There are three different methods of deploying the local AI with Docker.

### Without a GPU

The first method of deployment is for a machine without an [NVIDIA GPU](https://thenewstack.io/nvidia-gpu-dominance-at-a-crossroads/), which means the local AI will run solely off the CPU. For that, the command is:

This file contains hidden or bidirectional Unicode text that may be interpreted or compiled differently than what appears below. To review, open the file in an editor that reveals hidden Unicode characters.
[Learn more about bidirectional Unicode characters](https://github.co/hiddenchars)








|  |  |
| --- | --- |
|  | docker run -d -v ollama:/root/.ollama -p 11434:11434 --name ollama ollama/ollama |

That’s the easy method.

### With an NVIDIA GPU

If you have an NVIDIA GPU on your machine, there are several steps you must take.

The first thing you must do is add the necessary repository for the NVIDIA Container Toolkit with the following commands:

This file contains hidden or bidirectional Unicode text that may be interpreted or compiled differently than what appears below. To review, open the file in an editor that reveals hidden Unicode characters.
[Learn more about bidirectional Unicode characters](https://github.co/hiddenchars)








|  |  |
| --- | --- |
|  | curl -fsSL https://nvidia.github.io/libnvidia-container/gpgkey \ |
|  | | sudo gpg --dearmor -o /usr/share/keyrings/nvidia-container-toolkit-keyring.gpg |
|  | curl -s -L https://nvidia.github.io/libnvidia-container/stable/deb/nvidia-container-toolkit.list \ |
|  | | sed 's#deb https://#deb [signed-by=/usr/share/keyrings/nvidia-container-toolkit-keyring.gpg] https://#g' \ |
|  | | sudo tee /etc/apt/sources.list.d/nvidia-container-toolkit.list |
|  | sudo apt-get update |

You can now install the NVIDIA Container Toolkit with:

This file contains hidden or bidirectional Unicode text that may be interpreted or compiled differently than what appears below. To review, open the file in an editor that reveals hidden Unicode characters.
[Learn more about bidirectional Unicode characters](https://github.co/hiddenchars)








|  |  |
| --- | --- |
|  | sudo apt-get install -y nvidia-container-toolkit -y |

You’ll then have to configure Docker to work with the NVIDIA toolkit with the following two commands:

This file contains hidden or bidirectional Unicode text that may be interpreted or compiled differently than what appears below. To review, open the file in an editor that reveals hidden Unicode characters.
[Learn more about bidirectional Unicode characters](https://github.co/hiddenchars)








|  |  |
| --- | --- |
|  | sudo nvidia-ctk runtime configure --runtime=docker |
|  | sudo systemctl restart docker |

You can now deploy the [Ollama](https://thenewstack.io/how-to-set-up-and-run-a-local-llm-with-ollama-and-llama-2/) container with the command:

This file contains hidden or bidirectional Unicode text that may be interpreted or compiled differently than what appears below. To review, open the file in an editor that reveals hidden Unicode characters.
[Learn more about bidirectional Unicode characters](https://github.co/hiddenchars)








|  |  |
| --- | --- |
|  | docker run -d --gpus=all -v ollama:/root/.ollama -p 11434:11434 --name ollama ollama/ollama |

### With an AMD GPU

If you have an [AMD GPU](https://thenewstack.io/gunslinging-amd-tough-on-software-as-developers-balk/), the command is:

This file contains hidden or bidirectional Unicode text that may be interpreted or compiled differently than what appears below. To review, open the file in an editor that reveals hidden Unicode characters.
[Learn more about bidirectional Unicode characters](https://github.co/hiddenchars)








|  |  |
| --- | --- |
|  | docker run -d --device /dev/kfd --device /dev/dri -v ollama:/root/.ollama -p 11434:11434 --name ollama ollama/ollama:rocm |

## Accessing the Local AI

With everything up and running, we now have to access the AI prompt. Let’s say you want to pull the Llama 3.2 LLM. You can pull it and access the prompt with the following command:

This file contains hidden or bidirectional Unicode text that may be interpreted or compiled differently than what appears below. To review, open the file in an editor that reveals hidden Unicode characters.
[Learn more about bidirectional Unicode characters](https://github.co/hiddenchars)








|  |  |
| --- | --- |
|  | docker exec -it ollama ollama run llama3.2 |

The above command will land you at the Ollama prompt, where you can run your first query.

And that’s all there is to deploying a local AI via a Docker container.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://cdn.thenewstack.io/media/2023/12/d7cbfb14-cropped-6e7d5ccd-jack_wallen.jpg)

Jack Wallen is what happens when a Gen Xer mind-melds with present-day snark. Jack is a seeker of truth and a writer of words with a quantum mechanical pencil and a disjointed beat of sound and soul. Although he resides...

Read more from Jack Wallen](https://thenewstack.io/author/jack-wallen/)