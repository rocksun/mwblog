Whenever I use AI, I always opt to go with a locally installed instance. The reason for that is twofold. First, when I’m using locally installed AI, I’m not drawing power off an electric grid already in massive demand. Second, I can always trust my locally installed AI with my [privacy](https://thenewstack.io/will-data-privacy-die-in-the-age-of-genai/).

When using a local instance of AI, your information (including your queries) isn’t shared with a third party. It’s 100 percent private.

You might think that setting up a local AI server in your home lab might be a big challenge. It’s not. Actually, it’s quite easy, and I’m going to show you how it’s done. In the end, you’ll have an AI server that can be accessed either via a web browser or by connecting your favorite [AI GUI](https://thenewstack.io/generative-ui-for-devs-more-than-ai-assisted-design/) (such as [Ollama](https://thenewstack.io/connect-to-a-local-ollama-ai-instance-from-within-your-lan/), Alpaca, or [Msty](https://msty.ai/)) to the server.

So, without further ado, let’s get to the setup.

## What you’ll need

The only things you’ll need for this are a running instance of either [Debian](https://thenewstack.io/check-out-debian-the-mother-of-all-linux-distributions/) or [Ubuntu](https://thenewstack.io/10-reasons-to-choose-ubuntu-server-over-the-competition/) Server and a user with sudo privileges.

## Adding your Debian user to sudo

By default, your standard user isn’t a member of the sudo group on Debian. To successfully use [Docker](https://thenewstack.io/docker-basics-how-to-use-dockerfiles/) (for deploying the [WebUI](https://thenewstack.io/how-microsoft-edge-is-replacing-react-with-web-components/)), you must make this change.

To add your user to the Docker group on Debian, first change to the root user with:

```

sudo su-
```

Once you’ve changed to the root user, add your standard user to the Docker group with:

```

usernmod -aG docker USER
```

Where USER is the name of the user to be added.

Exit from the root user with the command:

```

exit
```

Log out of your standard user account and log back in, so the changes take effect.

## Installing Ollama

Next, we’re going to install Ollama, which can be done with the command:

```

curl -fsSL https://ollama.com/install.sh | sh
```

Once that finishes, let’s download a smallish LLM (for testing purposes). You can always download a larger LLM later. We’ll pull the llama3.2 model with the command:

```

ollama pull llama3.2
```

After the model has successfully pulled, make sure it’s working by running the model with:

```

ollama run llama3.2
```

If you see the Ollama prompt, you’re good to go. Exit from the prompt with the command:

```

/bye
```

### Configure Ollama

Next, we need to configure Ollama to accept remote connections. We’ll do this via systemd. Open the Systemd Ollama init file with:

```

sudo nano /etc/systemd/system/ollama.service
```

At the bottom of the [Service] section, add the following:

```

Environment="OLLAMA_HOST=0.0.0.0:11434"
```

Save and close the file.

Reload the Systemd daemon with:

```

sudo systemctl daemon-reload
```

Restart the Ollama service with:

```

sudo systemctl restart ollama
```

At this point, Ollama can be accessed from a remote machine on your LAN by using the IP address of the server. How you make the connection will depend on the app you use.

## Deploying WebUI with Docker

Next, we’ll deploy WebUI, so you can interact with your [LLMs](https://thenewstack.io/introduction-to-llms/) via a web browser. To do that, we’re going to make use of WebUI. Before we can do that, we have to install Docker. Here are the steps for installing Docker CE:

Add the necessary GPG key with the following commands:

1. *sudo apt-get update*
2. *sudo apt-get install ca-certificates curl*
3. *sudo install -m 0755 -d /etc/apt/keyrings*
4. *sudo curl -fsSL https://download.docker.com/linux/ubuntu/gpg -o /etc/apt/keyrings/docker.asc*
5. *sudo chmod a+r /etc/apt/keyrings/docker.asc*

Add the official Docker repository with the following:

1. *echo “deb [arch=$(dpkg –print-architecture) signed-by=/etc/apt/keyrings/docker.asc] https://download.docker.com/linux/ubuntu $(. /etc/os-release && echo “${UBUNTU\_CODENAME:-$VERSION\_CODENAME}”) stable” | sudo tee /etc/apt/sources.list.d/docker.list > /dev/null*
2. *sudo apt-get update*

Install Docker using the command:

```

sudo apt-get install docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin git -y
```

Test to make sure you can use Docker with:

```

docker ps -a
```

You should see an empty list of Docker containers; if so, you’re ready to deploy.

To deploy WebUI with Docker, the command is:

```

docker run -d -p 3000:8080 -v open-webui:/app/backend/data --name open-webui ghcr.io/open-webui/open-webui:main
```

Keep in mind that if your machine is already using port 3000, you’ll want to change that.

Give the container a moment to finish deploying. In my instance, it took around two minutes. You can check the deployment status with:

```

docker ps -a
```

When the container Status is listed as *healthy*, it’s ready to access.

## Accessing WebUI

To access the WebUI instance of Docker, open a web browser and point it to http://SERVER:3000 (where SERVER is the IP address of the hosting server). You should be presented with the WebUI main page (**Figure 1**).

![](https://cdn.thenewstack.io/media/2026/03/f677f438-webui1.jpg)

**Figure 1:** You’re ready to start using WebUI.

Click the right-pointing arrow at the bottom center and, in the resulting page (**Figure 2**), enter the required information to create an admin account.

![](https://cdn.thenewstack.io/media/2026/03/1f7d13a7-webui2.jpg)

**Figure 2:** Just a bit of info, and you’re ready to query.

You will then be presented with the query page. On that page, you’ll find that the LLM you pulled with Ollama isn’t available. Because of that, click the model drop-down in the upper left corner and then you’ll need to disable the OpenAI instance and then change the local address to http://SERVER:11434 (where SERVER is the IP address of your server).

You can now go to the New Chat tab and run your first query.

Congratulations, you now have a local AI instance that is accessible from any machine on your home lab LAN.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://cdn.thenewstack.io/media/2023/12/d7cbfb14-cropped-6e7d5ccd-jack_wallen.jpg)

Jack Wallen is what happens when a Gen Xer mind-melds with present-day snark. Jack is a seeker of truth and a writer of words with a quantum mechanical pencil and a disjointed beat of sound and soul. Although he resides...

Read more from Jack Wallen](https://thenewstack.io/author/jack-wallen/)