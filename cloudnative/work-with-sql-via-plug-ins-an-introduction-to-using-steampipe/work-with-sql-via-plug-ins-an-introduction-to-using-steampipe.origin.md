# Work With SQL via Plug-Ins: An Introduction To Using Steampipe
![Featued image for: Work With SQL via Plug-Ins: An Introduction To Using Steampipe](https://cdn.thenewstack.io/media/2024/06/131147fd-aakash-dhage-kmyqhzxvmte-unsplash-1024x576.jpg)
SQL has always been a data
*lingua franca*, allowing hard data to be extracted from different domains. This is why I was specifically intrigued by the way [Steampipe can read app data through SQL](https://thenewstack.io/sql-based-pipelines-steampipe-makes-all-the-world-a-database/). It has many plug-ins to convert internal app data to nice SQL tables.
In this post, I’ll look at the
[Slack plug-in](https://hub.steampipe.io/plugins/turbot/slack), which I’ll connect and then use on a live workspace. However, we know before we start that there will be quite a bit of effort to prepare the access to what is a third-party app from Slack’s viewpoint. This is the downside of attempting to open up an application’s data.
What I like about Steampipe is that you can prepare a sensible query before you attach it to a system. This is useful for consultants who may have limited access to systems, so they need to bring a reasonably wide set of tools around with them.
There is a
[CLI available](https://steampipe.io/downloads) for my version of macOS, and I’m quite happy to use its interface.
As usual, I use
[Warp](https://www.warp.dev/) for my shell, though Steampipe has its own CLI that will take precedence later on. After three minutes of updating Homebrew, I installed Steampipe directly:
Then, a quick version check to make sure the installation worked:
Then, I installed the Slack plug-in:
## Preparing To Interrogate Slack
There are several reasons why you might want to quiz an organization’s Slack, especially if you are dropping in on a team and need to establish a
[community of practice (CoP)](https://thenewstack.io/developers-need-a-community-of-practice-and-wikis-still-work/), or simply want to get a feel for which users are most active, or whether certain issues (or ticket numbers) are being discussed.
But first of all, how do we connect to it? Fortunately, Slack has a way of granting tokens within scopes for apps to use. I used this method way back when I looked at
[Dark, the serverless backend tool](https://thenewstack.io/how-to-get-started-building-serverless-backends-with-dark/). It was somewhat tricky then, so I was hoping it had become a little simpler. However, this process was only slightly smoother.
I tried to do this using the Mac version of the Slack app, but couldn’t. However, it is a straightforward process from the website. Check in to your target Slack workspace, then go to
[api.slack.com/apps](https://api.slack.com/apps).
From here, we can create a new app, select “from scratch,” and then give it a name. The “app” is what Slack is referring to as the third-party access service from Steampipe:
We can then select permissions and gain our scoped token access. I’m avoiding any admin-related scopes, and making sure to include “team,” “users,” “groups,” etc.:
You can always return to this section, add any missing scopes and reinstall the app.
This will allow the app to retrieve basic information from Slack. Finally, we’ll install our new tool and its OAuth tokens to the workspace. Be sure to make a copy of your long User OAuth Token:
As usual, Slack will show you its warning that it is requesting access (or a reason that it cannot).
Make sure you see the tick next to “Install your app” on the progress list:
Now go back to your shell and add that token into Steampipe’s Slack configuration file:
## Querying the Data
Now we are finally ready to see what we can do in Steampipe itself. Yay!
We’ll access the CLI’s query mode, and immediately will want to review the list of available tables (note that autocompletion suggestions are provided):
(Press Ctrl+D on a blank line, or use the
.exit command.)
Here is the result:
|
1
2
3
4
5
6
7
8
9
10
11
12
13
|
==> slack
+---------------------------+---------------------------------------------------------+
| table | description |
+---------------------------+---------------------------------------------------------+
| slack_access_log | Logins to Slack, grouped by User, IP and User Agent. |
| slack_connection | Information about the connection to the Slack workspace.|
| slack_conversation | Unified interface to all conversation like things.. |
| slack_conversation_member | Retrieve members of a conversation. |
| slack_emoji | Slack emoji installed in the workspace. |
| slack_group | Slack workspace user groups. |
| slack_search | Search slack for anything using a query. |
| slack_user | Slack workspace users. |
+---------------------------+---------------------------------------------------------+
To get information about the columns in a table, run
.inspect {connection}.{table}.
Before continuing on, try this command to confirm whether you have a connection:
|
1
|
> select * from slack_user;
Make sure you get some useful data back. If not, check that the installation is complete or whether the access tokens are sufficient.
Before we query in anger, let’s take a quick look at the
slack_user table:
|
1
|
> .inspect slack_user
First, I want to see which users are not bots and are not deleted, as well as who has updated their account to use two-factor authentication:
For some reason, the Slackbot is not a bot! But I can see that two people may need a security reminder, if that was my concern.
Now let’s look at
slack_search table, which can zoom in more accurately on information:
Note that
channel is a JSON type, which at first would seem a bit problematic. However, you can use the
->> operator to extract text. You must specify the query in the
where clause to query this table.
Here is a quick search for mentions of “ChatGPT” in the workspace’s channels:
But we might want a bit more information on when that was mentioned:
Using the
slack_conversation table, we can find out about popular channels by counting the members:
|
1
2
3
4
|
select name,num_members from slack_conversation where
num_members is not null
order by num_members desc
limit 5;
Because we are using SQL, we can of course get much more focused queries between tables, depending on what you need to find out.
Hopefully, you can see that Steampipe is a useful tool for retrieving valuable data, and that this Slack plug-in provides a good example of what we can get out. Having a prepared list of useful SQL queries can save you time if you only have limited access to a system — a good way to get the data you need in a flexible format of your choice.
[
YOUTUBE.COM/THENEWSTACK
Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.
](https://youtube.com/thenewstack?sub_confirmation=1)