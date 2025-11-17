[NotebookLM](https://notebooklm.google/) is an AI research and note-taking tool created by [Google](https://cloud.google.com/?utm_content=inline+mention) that uses [large language models (LLMs)](https://thenewstack.io/introduction-to-llms/) that make it possible for users to add their own sources and then, with the help of AI, understand and connect information between those sources.

NotebookLM is like a personalized AI assistant that only works on uploaded documents, PDFs, websites and videos to generate summaries, answer questions, brainstorm ideas and transform content into other formats.

NotebookLM is proprietary and is enjoying incredible popularity at the moment, but did you know that there’s an open source take on this technology?

[Open Notebook](https://www.open-notebook.ai/) is just as powerful and useful as NotebookLM. The big difference is that Open Notebook is self-hosted. Although both can use local AI models, only Open Notebook can be installed locally. If you’re concerned about privacy and security, having your AI tools isolated to your local network can be a real bonus. Unlike Open Notebook, NotebookLM is hosted on Google’s third-party cloud servers, which can raise questions about privacy and security.

Open Notebook supports over 16 AI providers, so you can select which LLM to use for your needs, budget and privacy requirements.

If that sounds appealing to you, read on because I’m going to show you how to deploy Open Notebook on a machine within your LAN.

## What You’ll Need

To make this work, you’ll need a computer that supports [Docker](https://thenewstack.io/docker-basics-how-to-use-dockerfiles/). If you want to use one of the proprietary AI services (such as [Google Gemini](https://thenewstack.io/googles-gemini-models-go-deeper/) or OpenAI), you’ll need an API key for the service in question.

I’m going to show you how to deploy Open Notebook on Ubuntu Server 24.04. If you’re using a different OS, you’ll need to alter the Docker installation method, but that’s it.

## Installing Docker

The first step is to install Docker. Here’s how:

### **1. Add the Official Docker GPG Key**

To add the official Docker GPG key, use the following commands:

This file contains hidden or bidirectional Unicode text that may be interpreted or compiled differently than what appears below. To review, open the file in an editor that reveals hidden Unicode characters.
[Learn more about bidirectional Unicode characters](https://github.co/hiddenchars)








|  |  |
| --- | --- |
|  | sudo apt-get update |
|  | sudo apt-get install ca-certificates curl |
|  | sudo install -m 0755 -d /etc/apt/keyrings |
|  | sudo curl -fsSL https://download.docker.com/linux/ubuntu/gpg -o /etc/apt/keyrings/docker.asc |
|  | sudo chmod a+r /etc/apt/keyrings/docker.asc |

### **2. Add the Docker Repository**

Next, you need to add the Docker repository, which is done with the following command:

This file contains hidden or bidirectional Unicode text that may be interpreted or compiled differently than what appears below. To review, open the file in an editor that reveals hidden Unicode characters.
[Learn more about bidirectional Unicode characters](https://github.co/hiddenchars)








|  |  |
| --- | --- |
|  | echo \ |
|  | "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.asc] |
|  | https://download.docker.com/linux/ubuntu \ |
|  | $(. /etc/os-release && echo "${UBUNTU\_CODENAME:-$VERSION\_CODENAME}") stable" | \ |
|  | sudo tee /etc/apt/sources.list.d/docker.list > /dev/null |

Update apt with:

This file contains hidden or bidirectional Unicode text that may be interpreted or compiled differently than what appears below. To review, open the file in an editor that reveals hidden Unicode characters.
[Learn more about bidirectional Unicode characters](https://github.co/hiddenchars)

### **3. Install the Required Software**

You’ll now need to install all of the necessary software with the command:

This file contains hidden or bidirectional Unicode text that may be interpreted or compiled differently than what appears below. To review, open the file in an editor that reveals hidden Unicode characters.
[Learn more about bidirectional Unicode characters](https://github.co/hiddenchars)








|  |  |
| --- | --- |
|  | sudo apt-get install docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin git -y |

### **4. Add Your User to the Docker Group**

You’ll need to add that user to the Docker group, so you can avoid running Docker with admin privileges. Add your user to the Docker group with:

This file contains hidden or bidirectional Unicode text that may be interpreted or compiled differently than what appears below. To review, open the file in an editor that reveals hidden Unicode characters.
[Learn more about bidirectional Unicode characters](https://github.co/hiddenchars)








|  |  |
| --- | --- |
|  | sudo usermod -aG docker $USER |

Log out and log back in so the changes take effect.

## Deploying Open Notebook

It’s now time to deploy. First, clone the necessary Git repository with:

This file contains hidden or bidirectional Unicode text that may be interpreted or compiled differently than what appears below. To review, open the file in an editor that reveals hidden Unicode characters.
[Learn more about bidirectional Unicode characters](https://github.co/hiddenchars)








|  |  |
| --- | --- |
|  | git clone https://github.com/lfnovo/open-notebook.git |

Change into the newly created directory with:

This file contains hidden or bidirectional Unicode text that may be interpreted or compiled differently than what appears below. To review, open the file in an editor that reveals hidden Unicode characters.
[Learn more about bidirectional Unicode characters](https://github.co/hiddenchars)

In that folder, you’ll need to copy and rename a couple of files with the commands:

This file contains hidden or bidirectional Unicode text that may be interpreted or compiled differently than what appears below. To review, open the file in an editor that reveals hidden Unicode characters.
[Learn more about bidirectional Unicode characters](https://github.co/hiddenchars)








|  |  |
| --- | --- |
|  | cp docker-compose.full.yml docker-compose.yml |
|  | cp .env.example docker.env |

You won’t have to edit the docker-compose.yml file, but you do need to work with the docker.env file.

In the docker.env file, you’ll need to edit a few lines. How many depends on what AI services you want to use. Let’s say you want to use [Ollama](https://thenewstack.io/connect-to-a-local-ollama-ai-instance-from-within-your-lan/) (which must be installed on the local machine) and Google Gemini.

The first thing to do is locate the line:

This file contains hidden or bidirectional Unicode text that may be interpreted or compiled differently than what appears below. To review, open the file in an editor that reveals hidden Unicode characters.
[Learn more about bidirectional Unicode characters](https://github.co/hiddenchars)








|  |  |
| --- | --- |
|  | API\_URL=http://127.0.0.1:5055 |

Change 127.0.0.1 to the IP address of your hosting server.

Next, locate the line:

This file contains hidden or bidirectional Unicode text that may be interpreted or compiled differently than what appears below. To review, open the file in an editor that reveals hidden Unicode characters.
[Learn more about bidirectional Unicode characters](https://github.co/hiddenchars)

You’ll want to uncomment that line (remove the #) and paste your Google Gemini API key such that it looks like this:

This file contains hidden or bidirectional Unicode text that may be interpreted or compiled differently than what appears below. To review, open the file in an editor that reveals hidden Unicode characters.
[Learn more about bidirectional Unicode characters](https://github.co/hiddenchars)








|  |  |
| --- | --- |
|  | GOOGLE\_API\_KEY=AIzaSyCOLZUi8h3wwjfhdSEViQXi9olWUoGKNE |

Make sure you use the API key you create from [Google’s API Studio](https://aistudio.google.com/app/api-keys).

Next, locate the line:

This file contains hidden or bidirectional Unicode text that may be interpreted or compiled differently than what appears below. To review, open the file in an editor that reveals hidden Unicode characters.
[Learn more about bidirectional Unicode characters](https://github.co/hiddenchars)








|  |  |
| --- | --- |
|  | OLLAMA\_API\_BASE="http://10.20.30.20:11434" |

You’ll want to substitute the above IP address with that of the hosting server, such as:

This file contains hidden or bidirectional Unicode text that may be interpreted or compiled differently than what appears below. To review, open the file in an editor that reveals hidden Unicode characters.
[Learn more about bidirectional Unicode characters](https://github.co/hiddenchars)








|  |  |
| --- | --- |
|  | OLLAMA\_API\_BASE="http://192.168.1.26:11434" |

You can go through the rest of the file and add other AI APIs that you require. Once you’ve done that, save and close the file.

You can learn more about the various models and what they’re best used for in [this official Open Notebook document](https://github.com/lfnovo/open-notebook/blob/main/docs/features/ai-models.md).

It’s now time to deploy the Open Notebook container, which is done with:

This file contains hidden or bidirectional Unicode text that may be interpreted or compiled differently than what appears below. To review, open the file in an editor that reveals hidden Unicode characters.
[Learn more about bidirectional Unicode characters](https://github.co/hiddenchars)

Give the container time to spin up and then point your browser to http://SERVER:8502 (where SERVER is the IP address of the hosting server).

You’ll be prompted to create an account (which is free and all information remains on the local server). After logging in, you’ll be greeted by the Open Notebook main page (Figure 1), where you can start configuring it to serve your needs.

[![](https://cdn.thenewstack.io/media/2025/11/c70c64f9-screenshot-2025-11-12-at-10.43.37%E2%80%AFam.png)](https://cdn.thenewstack.io/media/2025/11/c70c64f9-screenshot-2025-11-12-at-10.43.37%E2%80%AFam.png)

Figure 1: The Open Notebook UI is very user-friendly.

Make sure to first go to the Models section, where you define which models are to be used for specific tasks. Once you’ve done that, you can then create your first Notebook and get to work.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://cdn.thenewstack.io/media/2023/12/d7cbfb14-cropped-6e7d5ccd-jack_wallen.jpg)

Jack Wallen is what happens when a Gen Xer mind-melds with present-day snark. Jack is a seeker of truth and a writer of words with a quantum mechanical pencil and a disjointed beat of sound and soul. Although he resides...

Read more from Jack Wallen](https://thenewstack.io/author/jack-wallen/)