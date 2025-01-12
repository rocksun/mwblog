# Getting Started With CodeGate, an Intermediary for LLM Devs
![Featued image for: Getting Started With CodeGate, an Intermediary for LLM Devs](https://cdn.thenewstack.io/media/2025/01/f814f7a3-kent-tupas-u7scebzs57q-unsplashb-1024x576.jpg)
I suspect that the idea of being an intermediary between a remote LLM and an end user is a strong idea in itself, which is why I think [looking at CodeGate](https://thenewstack.io/codegate-open-source-tool-secures-ai-coding-assistants/) will be valuable whatever your current plans for AI coding. [CodeGate](https://codegate.ai/) is a security solution that, according to its homepage, “encrypts secrets in your prompts to protect your privacy and augments an LLM’s knowledge base with up-to-date risk insight to protect your code.”

You can obviously tell a lot of things about anybody from what and how they query — that is why Google will always be successful. Developers can give away a lot of information from their “exhaust,” which includes their public queries. This does not imply anyone is actively looking at this, but it is sensible to get into the habit of filtering your output.

Many things can be sensitive to an organization, like the name of internal suppliers, internal project names, and the obvious things like keys and passwords. Not all of these are necessarily evident to a development team.

## Local Defence
[CodeGate](https://codegate.ai/) is an open source framework that provides a “local prompt gateway”, and will clearly have more content and policy options as time goes on — think of it as as a live service game that has only just started.
From [https://docs.codegate.ai/#what-is-codegate](https://docs.codegate.ai/#what-is-codegate)

So this does not come as a ready and complete solution. I would imagine that CodeGate will eventually sit in front of a team, not an individual computer (as it stands now). The two actions that CodeGate currently looks for are suggestions of insecure packages in code examples from the remote LLM, and exposing internals through the AI Assistant. I’ll look at an example from the second later in this article.

## Setting Up
I’ll follow [the example](https://docs.codegate.ai/quickstart), which uses GitHub Copilot and Visual Studio. There are a few other combinations you could use via [Continue](https://www.continue.dev/), and all these configurations will be fluffed out over time and community use. Before we dig in, here is what we will do, so that you can check if it’s in your dev comfort zone:

- GitHub Copilot. You will need a GitHub account to use Copilot.
- Visual Studio Code. As
[GitHub Copilot is free in Visual Studio Code](https://code.visualstudio.com/docs/copilot/overview)(VS Code) this example path is fine, even though there are now a lot of IDE + AI combinations. (I’d like to see Zed AI and CodeGate). I’ll assume you know how to call the Command Palette on your system. - Docker: we will host CodeGate locally on Docker, which means sending the prompt to Docker and Codegate sending the enhanced code off to (in this case) Copilot.
- Certificate: given this is a security solution, we want to ensure what we are talking to.
## Getting Started
I’m doing this on my MacBook M4. First, let’s make sure we have a VS Code that is ready for Copilot.

I’ll just start a VS Code in an empty project:

Then I’ll install the GitHub Copilot extension and sign in:

Then make sure Docker Desktop is up and running.

Now we’ll go and use CodeGate’s signature installation line:

123 |
docker run --name codegate -d -p 8989:8989 -p 9090:9090 -p 8990:8990 --mount type=volume,src=codegate-volume,dst=/app/codegate_volume --restart unless-stopped ghcr.io/stacklok/codegate:latest |
This is a bit of a mouthful. This pulls the latest CodeGate image from the registry and starts it in the background. There is some port forwarding. Then the script starts a volume for persistent data storage.
Now we have a certificate to add. Why do we need this? As we have made CodeGate a [“man-in-the-middle”](https://en.wikipedia.org/wiki/Man-in-the-middle_attack) on purpose, we had better make sure we are definitely talking to the right person. With the port forwarding, the Docker container has already made your local website available at [http://localhost:9090](http://localhost:9090), so go there and download your certificate.

I then followed the Mac instructions for adding the cert to my chain via the Macbook’s UI:

Open the freshly added cert from the Keychain Access, in the login keychain, and make sure the two entries “SSL” and “X.509” are “Always trust”:

It should now appear on the cert list like this:

And yes, of course you can add it from the terminal with:

1 |
security add-trusted-cert -r trustRoot -k ~/Library/Keychains/login.keychain ~/Downloads/codegate.crt |
OK, so now all we need to do is inform VS Code to talk to our intermediary. Using the Command Palette, open **“Preferences: Open User Settings (JSON)”**.
Add the following settings:

12345678910 |
"http.proxy": "https://localhost:8990", "http.proxyStrictSSL": true, "http.proxySupport": "on", "http.systemCertificates": true, "github.copilot.advanced": { "debug.useNodeFetcher": true, "debug.useElectronFetcher": true, "debug.testOverrideProxyUrl": "https://localhost:8990", "debug.overrideProxyUrl": "https://localhost:8990" } |
As we have just re-engineered the underlying proxy pipework, you will need to restart VS Code.
Now let’s play with Codegate’s examples in repo. Let’s clone them into our project folder:

These are in Python, and I’m set for C#, but that won’t matter for now.

If we look at the conf.ini file, you can see it has keys and secrets in it.

Now, if we got the Copilot window, which has already loaded conf.ini for context, we could innocently prepare to ask about this file. The developer is just asking the LLM for a reminder of what the key-value pairs mean, probably because they haven’t used AWS for a while.

The problem is that while asking GPT 4o questions about why we are using it, you don’t want to send your private keys directly to Sam Altman. It would be embarrassing if they ended up as training data.

So, while CoPilot appears to answer this as expected, if you look carefully, you can see the note that CodeGate left as it intervened:

If we go to the CodeGate panel we can see what has actually happened.

(In fact, CodeGate is a little unclear in timings here and has also not quite got the references correct. As the timings are in minutes, I’m not entirely sure about the order. The trigger headings are also inconsistent — you might have spotted these. Technically, it should REDACT all three lines.)

First of all, CodeGate detects that one of the keys is an AWS_ACCESS_KEY_ID, redacts the original value and places an encrypted value in its stead:

It then decrypts the key as it returns that data from Copilot:

Obviously, to double-check this thoroughly, we would need to run our own LLM and see what came through.

While the logging of triggers is not quite accurately labeled (it will probably be fixed by the time you read this — poke them on their Discord if not), the operation cycle is working. I think this is just the current output from this release version of CodeGate.

## Conclusion
There will be an interesting moment when the LLM providers will have to make a decision. The standard ecosystem play means that (even anonymously) knowing what end users are doing increases the value of the provider platform — just ask Amazon. When what a user tells an LLM provider is hidden, inevitably, the platform’s value will be worth a little less. So either the providers will give users their own versions of an intermediary, or they will move to suppress it.

So now is the time to increase your understanding of what an intermediary can do for you and your security.

[
YOUTUBE.COM/THENEWSTACK
Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.
](https://youtube.com/thenewstack?sub_confirmation=1)