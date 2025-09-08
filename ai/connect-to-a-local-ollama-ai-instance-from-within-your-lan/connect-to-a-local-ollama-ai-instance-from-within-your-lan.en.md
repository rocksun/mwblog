I’ve become a big fan of using a locally installed instance of [Ollama AI](https://thenewstack.io/how-to-set-up-and-run-a-local-llm-with-ollama-and-llama-2/), a tool to run large language models (LLMs) on your own computer. Part of the reason for that is because of [how much energy AI consumes](https://thenewstack.io/ai-consumes-lots-of-energy-can-it-ever-be-sustainable/) when it’s used via the standard methods.

For a while, I was using [Ollama](https://ollama.com/) on my desktop machine, but discovered there were a few reasons why that wasn’t optimal. First, Ollama was consuming too many resources, which led to slowdowns on my desktop. Second, I was limited to only using Ollama on my desktop — unless I wanted to [SSH into my desktop](https://thenewstack.io/linux-ssh-and-key-based-authentication/) and start the AI from there.

Then, I discovered a better method: I could install Ollama on a server and then connect to it from any machine on my network.

I want to show you two different methods for doing this, one from the command line and the other via a graphical user interface (GUI). It’s much easier than you might think and only requires a minimal configuration on the server end.

With that said, let’s make this happen.

## Install Ollama

The first thing you must do is to install Ollama on the server. I would suggest deploying an instance of Ubuntu Server for this because I’ve had very good luck with running Ollama on Ubuntu.

With that said, log in to your Ubuntu Server instance and run the following command to install Ollama:

```
curl -fsSL https://ollama.com/install.sh | sh
```

Once the installation completes, Ollama has been successfully installed. You can then pull an LLM to your local machine with a command like:

```
ollama pull llama3.2
```

Or, if you want the gpt-oss model:

```
ollama pull gpt-oss
```

Once you’ve taken care of that, you’re ready to configure Ollama to accept remote connections.

## Configure Ollama for Remote Connections

Open the Ollama systemd configuration file with the command:

```
sudo nano /etc/systemd/system/ollama.service
```

Under the [service] section, add the following:

```
Environment="OLLAMA_HOST=0.0.0.0"
```

Save and close the file.

The above line opens Ollama to connections from any location. Do keep in mind that you’ll want to make sure your LAN is secure; otherwise, some bad actor could sneak into your LAN and do things with Ollama.

If you want to be able to access your Ollama instance from outside the LAN, you would need to configure your router to direct incoming traffic on port 11434 to the hosting server.

Reload the systemctl daemon with the command:

```
sudo systemctl daemon-reload
```

Restart Ollama with the command:

```
sudo systemctl restart ollama
```

You’re now ready to connect from your LAN.

## Connecting via the Terminal

Open a terminal window on the local machine to which you want to connect to the Ollama server. On that machine, enter the following command:

```
OLLAMA_HOST=IP_ADDERES ollama run llama3.2:latest
```

Where IP\_ADDRESS is the IP address of the Ollama server.

You should be greeted by the Ollama text prompt, where you can start running your own queries. When you’re finished, exit the Ollama prompt with:

```
/bye
```

This will end not only your Ollama session, but the remote connection.

## Connecting to Your Remote Ollama Instance via a GUI

We’ll now connect to our remote Ollama instance via a GUI. The GUI in question is Msty because it makes doing this very easy. You should be able to connect to a remote Ollama instance via the official GUI, but I’ve yet to succeed at making that work.

Instead, we’ll use Msty, which is a superior GUI anyway. Msty has tons of features, can run on all three of the major platforms (Linux, macOS, and Windows) and is free to use.

If you’ve not already installed Msty, head to the [official site](https://msty.ai) and download the version for your operating system. Installing Msty is fairly straightforward, so you shouldn’t have any problems with it.

With Msty installed, open the GUI app. From the main window, click the Remote Model Providers icon in the left sidebar and then click Add Remote Model Provider. In the resulting window (Figure 1), fill out the information as such:

* Provider: Select Ollama Remote from the drop-down.
* Give the remote a memorable name.
* Enter the server endpoint in the form of http://SERVER\_IP:PORT, where SERVER\_IP is the IP address of the Ollama hosting server and PORT is the port you’ve configured (default is 11434).

[![Screenshot](https://cdn.thenewstack.io/media/2025/09/7ad7facf-ollamaremote.png)](https://cdn.thenewstack.io/media/2025/09/7ad7facf-ollamaremote.png) Figure 1: Configuring a remote Ollama server is fairly straightforward.

When prompted, click Fetch Models, select the model(s) you want (from the Model drop-down) and then click Add.

## Using the Remote Instance With Msty

Back at the Msty main window, start a new chat. From the Model drop-down (Figure 2), you should now see a Remote section with the model(s) you added.

[![Screenshot](https://cdn.thenewstack.io/media/2025/09/20f5b4df-ollamamenu.png)](https://cdn.thenewstack.io/media/2025/09/20f5b4df-ollamamenu.png) Figure 2: Selecting the newly added remote Ollama instance.

Select that entry and type your query. This time, the query will be answered by the remote instance of Ollama. Because you’re running Ollama on a server, your query responses should be faster than they are when running them directly from your desktop.

I’ve now started using Ollama strictly with this type of setup to avoid CPU/RAM bottlenecks on my desktop PCs. I’ve found using Ollama remotely to be faster and more reliable.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://cdn.thenewstack.io/media/2023/12/d7cbfb14-cropped-6e7d5ccd-jack_wallen.jpg)

Jack Wallen is what happens when a Gen Xer mind-melds with present-day snark. Jack is a seeker of truth and a writer of words with a quantum mechanical pencil and a disjointed beat of sound and soul. Although he resides...

Read more from Jack Wallen](https://thenewstack.io/author/jack-wallen/)