We’ve done quite a bit of talking about [Model Context Protocol](https://thenewstack.io/mcp-the-missing-link-between-ai-agents-and-apis/) (MCP), an open source standard that streamlines how AI models interact with APIs, but with [Claude Desktop](https://www.claude.com/download) you can really see it in action. As a developer, some of your workflow might move across your laptop file system. In terms of area of effect, you would typically want to focus your development on Claude Code and ask simple queries via the web on mobile. But the Desktop product can be made aware of files on your machine, which has benefits that I will explore in this post.

Claude Desktop is a bit smarter today than when it first appeared. For a start, you no longer need to write the server code yourself. Claude Desktop provides prebuilt connecters to other services, although the basic pattern is to use an LLM to find documents and transform the information within them in a useful way. What we always want is a system that the LLM understands, so that we can just let it figure things out.

## Installation and Initial Setup of Claude Desktop

I downloaded the 200MB .dmg for my M4, and installed it:

[![](https://cdn.thenewstack.io/media/2025/11/c46daaef-image.png)](https://cdn.thenewstack.io/media/2025/11/c46daaef-image.png)

I signed in and was immediately moved to a web page. These pages were managed properly by the app, but you can see why users are wondering why they are using an app that immediately wants to use the web.

Next we see some immediate and useful hints about using Claude on your actual desktop, where it will be available when you need it:

[![](https://cdn.thenewstack.io/media/2025/11/82836941-image-1.png)](https://cdn.thenewstack.io/media/2025/11/82836941-image-1.png)

I’m not sure hijacking the caps lock is a great plan — but if you think of your Mac as a dictation device, perhaps we won’t be typing much at all in the future?

I was then given the option to “update” to [Claude Opus 4.5](https://thenewstack.io/anthropics-new-claude-opus-4-5-reclaims-the-coding-crown-from-gemini-3/), which I took. But remember we aren’t necessarily focusing on straight coding for this app, so other models might be more suitable for your use case.

## Understanding Payment Plans and Integrations

You then get confronted with the payment plans (although without showing usage limits), and naturally there is a free plan. I might already be part of a plan, but this interface didn’t tell me. According to Anthropic Console (now Claude Console) I might be on the API plan and have some credit. One day all this confusion will be gone, but for now we are in the innovation storm of the token economy.

[![](https://cdn.thenewstack.io/media/2025/11/a52a1a71-image-2-1024x402.png)](https://cdn.thenewstack.io/media/2025/11/a52a1a71-image-2-1024x402.png)

Before I move on from payment plans, the first thing I noticed was this small discreet hint:

[![](https://cdn.thenewstack.io/media/2025/11/677771e7-image-3-1024x46.png)](https://cdn.thenewstack.io/media/2025/11/677771e7-image-3-1024x46.png)

Now, I do want check the Slack integration. A few years ago, I tried [Slack integration](https://thenewstack.io/how-to-get-started-building-serverless-backends-with-dark/) with a web tool and it was fairly tricky. Unfortunately, the Slack connector seems only available from a specific tier of subscription model, for Claude Team and Enterprise plan customers who have installed Claude in the Slack app. This might well be a sensible business offering.

## Configuring the Fileserver MCP for Local File Access

But we are not limited to pre-figured connectors; we can roll our own. [Claude recognises skills](https://www.claude.com/blog/how-to-create-skills-key-steps-limitations-and-examples), and we can make MCP servers to talk to our local apps. This is actually a good reason to use Opus 4.5. You will need to be on a a paid plan to use skills too. But our ambition is just to let Claude work with the files on your local drive.

Right now, I don’t have any connectors up and running. So let’s check whether Claude can see our local files:

[![](https://cdn.thenewstack.io/media/2025/11/470069a4-image-5-1024x703.png)](https://cdn.thenewstack.io/media/2025/11/470069a4-image-5-1024x703.png)

In order to change this, we are going to change the settings to allow the [Fileserver MCP](https://modelcontextprotocol.io/docs/develop/connect-local-servers) to fiddle with a limited set of files. At some point the server will need Node.js, so open a terminal and make sure you can do this:

[![](https://cdn.thenewstack.io/media/2025/11/58d82025-image-6.png)](https://cdn.thenewstack.io/media/2025/11/58d82025-image-6.png)

Now we will work with Claude Desktop’s settings directly (through the App’s Mac menu, or from the App settings) and go to the Developers section:

[![](https://cdn.thenewstack.io/media/2025/11/3798c7c3-image-7-1024x453.png)](https://cdn.thenewstack.io/media/2025/11/3798c7c3-image-7-1024x453.png)

Hitting “Edit Config” will open up the MCP config JSON file. You can see that mine is empty:

[![](https://cdn.thenewstack.io/media/2025/11/680eeb13-image-8-1024x350.png)](https://cdn.thenewstack.io/media/2025/11/680eeb13-image-8-1024x350.png)

Remember, Claude Desktop is the “host” and the Fileserver is an MCP server that Claude can call. So you want to have something like this:

|  |
| --- |
| An error has occurred. Please try again later. |

I’m *eastmad* but you probably are not; so obviously, use your name instead. I’ve given the server access to my Downloads folder to underline that this works in general — and you can carry on adding specific directories in that array. You can see we are using npx (hence you need Node) and this server is known as “filesystem.” This will give Claude full access, as I’ve explained — though confirmation will be required.

OK, these are starting configs, so close Claude Desktop and restart it.

Immediately on restart, Claude Desktop knows a little bit more:

[![](https://cdn.thenewstack.io/media/2025/11/79462823-image-9-1024x755.png)](https://cdn.thenewstack.io/media/2025/11/79462823-image-9-1024x755.png)

But does Claude know what it knows? Let’s try that initial question again. Go back to that query and refresh it:

[![](https://cdn.thenewstack.io/media/2025/11/8fd3a817-image-10-1024x799.png)](https://cdn.thenewstack.io/media/2025/11/8fd3a817-image-10-1024x799.png)

Once you allow the action:

[![](https://cdn.thenewstack.io/media/2025/11/1ad8b86c-image-11-1024x414.png)](https://cdn.thenewstack.io/media/2025/11/1ad8b86c-image-11-1024x414.png)

That’s great, although it doesn’t mention writing to the disk, so let’s check it can:

[![](https://cdn.thenewstack.io/media/2025/11/849ae01e-image-12-1024x611.png)](https://cdn.thenewstack.io/media/2025/11/849ae01e-image-12-1024x611.png)

Finder assures me this is no hallucination:

[![](https://cdn.thenewstack.io/media/2025/11/8b0de423-image-13-1024x690.png)](https://cdn.thenewstack.io/media/2025/11/8b0de423-image-13-1024x690.png)

And yes, a classic haiku is not only 5-7-5 syllables, it should also mention a season.

## Security Implications and Permissions

Now before you start witnessing the firepower of your fully armed and operational MCP server, make sure you understand the security implications. We are only working locally, but we are still sending information back and forth from Anthropic, so ensure that documents you read don’t tie identity information to any sensitive stuff. You can also give Claude access to other tools to allow it to work locally — indeed, this is where the true power lies.

At the moment, Claude will ask you permission for each access request. So I asked Claude to read the details of one email file; it stops twice to check permissions.

[![](https://cdn.thenewstack.io/media/2025/11/cdc8712e-image-14-1024x211.png)](https://cdn.thenewstack.io/media/2025/11/cdc8712e-image-14-1024x211.png)

Once you learn a bit more, you will be able to bypass these checks (if you truly wish to do so).

## Final Thoughts on Using Claude With MCP

Claude Desktop can use a range of prebuilt MCP servers to connect to certain services — but remember, you will still have to engineer the permissions, credentials and any other admin things with third parties.

Payment plan and token usage systems remain murky, even though actual transactions are perfectly transparent. On the one hand, it is obvious that these systems will become federated and streamlined over time — although when that happens, the token economy may well be targeted for national taxation. So mild chaos does have some advantages for now.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://cdn.thenewstack.io/media/2022/09/2e2ac7a2-cropped-a46bbf33-photo.png)

David has been a London-based professional software developer with Oracle Corp. and British Telecom, and a consultant helping teams work in a more agile fashion. He wrote a book on UI design and has been writing technical articles ever since....

Read more from David Eastman](https://thenewstack.io/author/david-eastman/)