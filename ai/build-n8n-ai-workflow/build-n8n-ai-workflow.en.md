n8n is one of the most powerful workflow automation platforms available today, and the fastest way to learn it is to build something real.

In this article, you will build a complete AI workflow from end to end. We will use a content publishing pipeline as our example. Still, the concepts you learn here: triggers, AI agents, conditional routing, human approvals, and API calls, apply to any workflow you build next.

No theory dumps. You build as you read.

## What you will learn

You will build one real automation project. The skills you pick up along the way will open the door to endless automations moving forward.

> “No theory dumps. You build as you read.”

By the end, you will know how to:

* Install and set up n8n
* Pick the correct trigger to start the workflow
* Fetch the data from external services and handle failure
* Integrate AI into your workflow to make it a smart workflow
* Route data with conditions and logic
* Send notifications on any platform like Gmail, Slack, or Teams
* Test, debug, and extend the workflows professionally

These are the building blocks of every serious n8n workflow. Once you learn, you will be able to use them again and again.

## The project: an article submission workflow

We will [build a real content automation workflow](https://thenewstack.io/building-multiagent-systems-for-workflow-automation-with-crewai/).

**The problem:** Publishing a single article requires extensive manual coordination. The writer submits a draft. A reviewer reads it and sends feedback. Someone else publishes it on the CMS. Finally, the finance team processes the payment. That requires four handoffs and a lot of back-and-forth via email.

We will automate this entire workflow using n8n.

There are six stages. Each one teaches a core concept.

1. **Submission:** The writer drafts an article in Google Docs and submits it through a form.
2. **Document fetch:** n8n pulls the Google Docs content and verifies the link is valid and accessible.
3. **AI Review:** An AI agent reviews the draft against a set of rules. Failed drafts are emailed back to the writer with specific feedback.
4. **Editor approval:** The editor approves or rejects the draft in Slack.
5. **Publication:** Approved drafts are published to a CMS (Hashnode, WordPress, etc.).

**Success email and payment alerts:** The writer gets a confirmation email. The finance team gets a Slack ping to release payment.

## Before you start: get n8n running

Before we build anything, you need n8n running.

### Option 1: Cloud (fastest to start)

Sign up at <https://n8n.io/>. A free trial covers everything in this tutorial.

### Option 2: Self-hosted (free and unlimited)

This is free and unlimited, but you need Docker installed. If you don’t have it, download it from the [official Docker website](https://www.docker.com/products/docker-desktop/), then run:

```

docker volume create n8n_data

docker run -d --restart unless-stopped \
  --name n8n -p 5678:5678 \
  -v n8n_data:/home/node/.n8n \
  docker.n8n.io/n8nio/n8n

```

Now, open <http://localhost:5678>. Create your account, and you’re done.

**Note:** If you’re self-hosting, your n8n instance must be reachable from the internet for webhook-based steps to work. Use a tunnel like ngrok or Cloudflare Tunnel and set the WEBHOOK\_URL environment variable to your public URL.

Use option 1 for this tutorial. Once everything works, you can migrate to a self-hosted instance for free.

With n8n running, let’s build.

## Stage 1: the trigger

Every workflow starts with a trigger. It defines what kicks off the workflow. n8n offers many triggers: scheduled triggers run at fixed intervals, email triggers fire on new mail, webhook triggers respond to HTTP requests, and so on.

For our workflow, we will use the Form Trigger. Writers fill a form with their Google Docs link. When they submit it, the workflow fires.

In your n8n, create a new workflow by clicking on the “Create Workflow” button.

This will create an empty workflow on the canvas.

![Screenshot of the empty n8n canvas with the "Add first step" prompt in the center and the left sidebar showing workflow settings.](https://cdn.thenewstack.io/media/2026/05/0e6fe844-1-1024x487.png)

*Screenshot: The empty n8n canvas with the “Add first step” prompt in the center and the left sidebar showing workflow settings.*

Now, in the top-left corner, click the “+” icon and search for “Form Trigger”. Select “On form submission” inside the trigger section.

![Screenshot: The node picker opens with "Form Trigger" search results showing. Highlight the "On form submission" event.](https://cdn.thenewstack.io/media/2026/05/e7c7b90c-2.png)

*Screenshot: The node picker opens with “Form Trigger” search results showing. Highlight the “On form submission” event.*

Add these fields to your form:

* Name (text, required)
* Email (email, required)
* Title (text, required)
* Google Docs link (text, required)

You can also add HTML blocks to customize the form, but that is optional for this tutorial.

Click “Execute workflow” at the bottom. The form opens in a new tab.

![Screenshot: The rendered form in a new browser tab, showing the Name, Email, Title, and Google Docs link fields.](https://cdn.thenewstack.io/media/2026/05/391414d7-3.png)

*Screenshot: The rendered form in a new browser tab, showing the Name, Email, Title, and Google Docs link fields.*

Your first trigger is ready.

You can share the workflow’s public URL with the writers so they can submit their article draft for review.

## Stage 2: validating the Google Docs link

You have collected the writer’s details and their Google Docs link, but keep in mind that the link may be broken or the doc may not be shared. You need to validate it before passing it to the AI.

Click the “+” icon after your trigger node and search for “Google Docs”.

Select the “Get a document” operation. Authenticate with your Google account when prompted.

In the “Document URL” field, drag the “Google Docs link” field from the Form Trigger node. n8n inserts the expression for you.

Now, open the node’s Settings tab and switch On Error to Continue (using error output). This adds a second output on the Google Docs node for the error path. If the doc is private or the link is broken, data flows down the error branch instead of halting the workflow.

Next, add an IF node after the Google Docs node’s main (success) output. The IF node routes your workflow based on a condition. Here, we confirm that we actually received a document.

In the IF node, add this condition:

* Value 1: {{ $json.content }}
* Operation: Exists (or “Is Not Empty”)

If the Google Docs node succeeded, content will be populated, and the TRUE branch fires. On failure, the node sends data down its error output instead, which you will wire to the Gmail rejection node.

Once this condition is created, here’s how your workflow should look:

![Screenshot: The canvas showing four nodes connected in sequence - Form Trigger, Google Docs node, IF node, with the IF node's TRUE and FALSE branches visible.](https://cdn.thenewstack.io/media/2026/05/440f8fbc-4-1024x337.png)

*Screenshot: The canvas showing four nodes connected in sequence – Form Trigger, Google Docs node, IF node, with the IF node’s TRUE and FALSE branches visible.*

If the doc loads, the workflow continues down the TRUE branch.

Connect the Google Docs node’s error output directly to a Gmail node to email the writer that their link is broken. (You can also use the IF node’s FALSE branch as a backup path for edge cases where the doc loads but is empty.)

Add a Gmail node. Select the “Send an email” operation and authenticate with your Google account.

In the “To” field, drag the Email field from the Form Trigger. Add a subject line and paste this body:

|  |
| --- |
| Hi {{ $(‘Article Submission Form’).item.json.Name }},  We could not access the Google Doc you submitted.  Please check that the doc sharing is set to “Anyone with the link.”(Viewer) or shared with our review account, then resubmit.  Regards, Workflow Team |

Notice, {{ $(‘Article Submission Form’).item.json.Name }}. That is how you reference data from the earlier node. You will use this pattern a lot.

This is how the Gmail node would look:

![Screenshot: The Gmail "Send Email" node configuration panel, showing the To field populated with the expression, the subject line, and the body text.](https://cdn.thenewstack.io/media/2026/05/ab11017c-5-1024x478.png)

*Screenshot: The Gmail “Send Email” node configuration panel, showing the To field populated with the expression, the subject line, and the body text.*

This is how the workflow would look so far:

![Screenshot: The canvas with five nodes now connected, including the Gmail node on the failure branch of the IF node.](https://cdn.thenewstack.io/media/2026/05/e2c9a715-6-1024x388.png)

*Screenshot: The canvas with five nodes now connected, including the Gmail node on the failure branch of the IF node.*

## Stage 3: the AI review

This is the heart of the workflow, and the step that turns a plain automation into an AI-powered one.

> “This is the heart of the workflow, and the step that turns a plain automation into an AI-powered one.”

Drop an AI Agent node. Connect it to the TRUE output of the IF node.

![Screenshot: The canvas with the AI Agent node added on the TRUE branch. No chat model or output parser attached yet.](https://cdn.thenewstack.io/media/2026/05/5d1d92b8-7.png)

*Screenshot: The canvas with the AI Agent node added on the TRUE branch. No chat model or output parser attached yet.*

### Attach a Chat Model

The agent needs a brain to operate. To give it one, click on the “Chat Model” option and connect to the OpenAI Chat Model. You can change this model to any other model of your choice, like Anthropic’s Claude or Gemini. For this tutorial, we will use the OpenAI model.

You will need an OpenAI API key. Grab one from your OpenAI dashboard and paste it into n8n’s credentials panel when prompted.

Pick any model your account has access to. For this tutorial, a small, inexpensive model works fine (for example, *gpt-4o-mini* or whatever the current small-tier model is in your account). You can always swap it out later.

### The prompt

This is how we tell the AI agent what we want it to do. We want our agent to review the submitted article against the set of rules. Here’s the prompt you can copy and paste for this project.

|  |
| --- |
| You are a strict, rule-based article reviewer. Evaluate ONLY against the rules below. Do not rewrite. If unsure, mark as PASS. Output valid JSON only.  Rules: 1. Word count: 500 to 2000 2. Headings: sentence case, no ALL CAPS, no duplicates 3. No paragraph over 120 words 4. No sentence over 30 words 5. Prohibited phrases: “game-changing”, “revolutionary”,   “next-gen”, “cutting-edge”, “leverage” 6. Code safety: no hardcoded secrets, no SQL concatenation, no eval( 7. Structure: 3+ headings, intro before first heading,   conclusion after last  If all passes, status = SUCCESS and message = friendly success email.If any fail, status = FAIL and message = email listing eachfailed rule with reason.  Article Content to Review:””” {{ $(‘Get a document’).item.json.content }} |

Now adjust these rules as needed.

### Attach a Structured Output Parser

AI would, by default, reply with a message style, but we only want a JSON structure so that we can use it in our workflow. Click on the output parser in the AI node and select “Structured Output Parser.” In this section, select “Define using JSON Schema.” In the body, add the schema:

```

{
  "type": "object",
  "required": ["status", "message"],
  "properties": {
    "status": {
      "type": "string",
      "enum": ["SUCCESS", "FAIL"]
    },
    "message": {
      "type": "string",
      "description": "Email-style draft explaining review result and listing issues if any"
    }
  },
  "additionalProperties": false
}

```

Now, every AI response has a status (SUCCESS or FAIL) and a message body.

This is it. Now the agent will review the workflow and share its verdict.

Now, the workflow should look something like this:

![Screenshot: The full canvas with Form Trigger, Google Docs, IF, Gmail (failure), AI Agent with Chat Model and Output Parser sub-nodes attached.](https://cdn.thenewstack.io/media/2026/05/8d1aa96b-8.png)

*Screenshot: The full canvas with Form Trigger, Google Docs, IF, Gmail (failure), AI Agent with Chat Model and Output Parser sub-nodes attached.*

Before proceeding to the next stage, run your workflow to ensure everything up to this point works smoothly.

## Stage 4: editor approval (send and wait)

So far, the AI has reviewed the draft and given its verdict. Now we [need a human](https://thenewstack.io/github-ceo-on-why-well-still-need-human-programmers/) editor to sign off before anything goes live. This pattern is called human-in-the-loop.

Drop the IF node into the canvas. Add a condition with Value 1 set to {{ $json.output.status }}, Operation set to “Equals” (String), and Value 2 set to SUCCESS

If it is false, add the Gmail node to inform the author about the changes.

Subject: Action Required: Your Article Failed Review Checks

Body: {{ $json.output.message }}

Here’s what a failure message would look like.

![Screenshot: The received rejection email in a mail client, showing the subject "Action Required: Your Article Failed Review Checks" and the body listing the failed rules.](https://cdn.thenewstack.io/media/2026/05/954593d2-9-1024x435.png)

*Screenshot: The received rejection email in a mail client, showing the subject “Action Required: Your Article Failed Review Checks” and the body listing the failed rules.*

If the article passes the AI review, we will use Slack to take the final review from the editor.

Drop a Slack node into the canvas. Set Operation to Send and Wait for Response. This node posts a message to Slack and pauses the workflow until someone clicks a button. When the editor clicks Approve or Reject, n8n resumes the workflow and makes the response available on the next node.

Now, you must first authenticate your Slack credentials. Click the “Connect to Slack” button to go to your Slack settings.

Note that you must have sufficient privilege access to provide Slack access to n8n.

Next, configure your Slack options. Select resource as “Message”. From the channels dropdown menu, add your channel. And in the message, paste the formatted message.

|  |
| --- |
| \*📄 Article Ready for Final Review\*  \*Title:\* {{ $(‘Article Submission Form’).item.json.Title }} \*Author:\* {{ $(‘Article Submission Form’).item.json.Name }} \*Draft:\* {{ $(‘Article Submission Form’).item.json[‘Google docs link’] }}  Please review and confirm if it’s ready for release. |

Please select the response type as “Approval,” and select both “Approve” and “Reject” options. This will allow members in the Slack channel to approve or reject the article.

![Screenshot: The Slack node configuration with "Send and Wait for Response" operation selected, channel picked, and both "Approve" and "Reject" response options enabled.](https://cdn.thenewstack.io/media/2026/05/c39b858e-10-1024x459.png)

*Screenshot: The Slack node configuration with “Send and Wait for Response” operation selected, channel picked, and both “Approve” and “Reject” response options enabled.*

Now, your workflow should look like this.

![Screenshot: The full canvas showing the new IF branch splitting into Gmail (rejection) and Slack Send-and-Wait.](https://cdn.thenewstack.io/media/2026/05/a813deff-11.png)

*Screenshot: The full canvas showing the new IF branch splitting into Gmail (rejection) and Slack Send-and-Wait.*

Before proceeding with the next step, make sure to run your workflow.

You should see a Slack message, something like this.

![Screenshot: The actual Slack message in a channel showing the title, author, draft link, and the Approve/Reject buttons.](https://cdn.thenewstack.io/media/2026/05/42aa0e98-12-1024x388.png)

*Screenshot: The actual Slack message in a channel showing the title, author, draft link, and the Approve/Reject buttons.*

## Stage 5: publish to CMS (Hashnode)

Based on the editors’ feedback, we can send a rejection email to the author. If the article is approved, we can publish it to a CMS.

So far, you have learned about the IF node. It’s time to test that knowledge. Drop the IF node to the canvas and check whether the article was approved or rejected.

Here’s the condition:

* Value 1: {{ $json.approval\_status }},
* Operation: Equals (String),
* Value 2: approved

The Slack Send-and-Wait node returns a data.approved boolean based on which button the editor clicked. If the shape looks different in your n8n version, open the previous node’s output panel and copy the correct path from there.

In the false branch, drop the Gmail node to send the rejection email. Here’s a failure message that you can use.

|  |
| --- |
| Hi {{ $(‘Article Submission Form’).item.json.Name }},  Thank you for submitting your article titled “{{ $(‘Article Submission Form’).item.json.Title }}”.  Your piece cleared our automated review and reached the editorial team, which is a solid achievement on its own. After careful consideration, our editors have decided not to publish it at this time.  This is not a reflection of your effort or skill. Editorial decisions weigh many factors, including current content calendar, audience fit, and topic timing. Pieces that are not a fit today often find a home elsewhere or work well with a different angle later.  We genuinely appreciate you sharing your work with us and hope you will consider submitting again in the future.  Regards, Workflow Team |

If the article is approved, we need to publish it to a CMS.

For this workflow, we will use the Hashnode platform, but you can use any CMS you prefer.

Add an HTTP Request node to the canvas. This node calls external APIs.

First, set up credentials the right way. In n8n, go to Credentials > New > Header Auth and create a credential with:

* Name: Authorization
* Value: Bearer YOUR\_HASHNODE\_TOKEN

Now configure the HTTP Request node:

* Method: POST
* URL: <https://gql.hashnode.com>
* Authentication: Generic Credential Type > Header Auth > (select the credential you just made)
* Send Headers: ON, add Content-Type: application/json
* Send Body: ON
* Body Content Type: JSON
* Specify Body: Using JSON

Paste this into the JSON field:

```

{
"query": "mutation PublishPost($input: PublishPostInput!) { publishPost(input: $input) { post { url title } } }",
"variables": {
"input": {
"title": "{{ $('Article Submission Form').item.json.Title }}",
"contentMarkdown": "{{ $('Get a document').item.json.content }}",
"publicationId": "YOUR_PUBLICATION_ID"
}
}
}

```

Replace YOUR\_PUBLICATION\_ID with your Hashnode publication ID (you can find it in your Hashnode dashboard URL).

Using n8n Credentials instead of hard-coding the token in a header means your token never leaks when you export or share the workflow.

Now the workflow should look like this:

![Screenshot: The full canvas with the HTTP Request node added on the approval branch, connected after the approval IF.](https://cdn.thenewstack.io/media/2026/05/f961eb35-13-1024x447.png)

*Screenshot: The full canvas with the HTTP Request node added on the approval branch, connected after the approval IF.*

Now, when your workflow runs, if all approvals are in place, it will publish to the Hashnode platform.

We are almost done — just two more notifications to set up.

## Stage 6: success email and payment alert

The core workflow is done. Two things remain: tell the writer their article is live and ping the finance team to release the payment.

Drop another Gmail node and connect it to the HTTP Request node.

Use the body below in the Gmail node:

|  |
| --- |
| Congratulations! Your article “{{ $(‘Article Submission Form’).item.json.Title }}” is live.  Read it here: {{ $json.data.publishPost.post.url }}  You will get a separate email with payment details. |

![Screenshot: The received success email in a mail client.](https://cdn.thenewstack.io/media/2026/05/87d8b821-1231-1024x415.png)

*Screenshot: The received success email in a mail client*

Drop the Slack node and connect it to the HTTP Request node.

Here, you need to select the finance team’s channel.

You can use the following message:

|  |
| --- |
| :newspaper: \*New article published – payment due\*  \*Author:\* {{ $(‘Article Submission Form’).item.json.Name }} \*Email:\* {{ $(‘Article Submission Form’).item.json.Email }} \*URL:\* {{ $json.data.publishPost.post.url }}  Please process the payment. |

Here’s what a Slack message would look like:

![Screenshot: The Slack message in the finance channel showing the newspaper emoji, author name, email, and article URL.](https://cdn.thenewstack.io/media/2026/05/21cc4e93-14-1024x324.png)

*Screenshot: The Slack message in the finance channel showing the newspaper emoji, author name, email, and article URL.*

This is it!  Here’s what your final AI workflow should look like:

![Screenshot: The complete canvas showing all nodes - Form Trigger, Google Docs, IF (validation), Gmail (invalid link), AI Agent, IF (AI verdict), Gmail (AI rejection), Slack Send-and-Wait, IF (editor decision), Gmail (editor rejection), HTTP Request, Gmail (success), Slack (finance alert).](https://cdn.thenewstack.io/media/2026/05/4fc32a26-15-1024x495.png)

*Screenshot: The complete canvas showing all nodes – Form Trigger, Google Docs, IF (validation), Gmail (invalid link), AI Agent, IF (AI verdict), Gmail (AI rejection), Slack Send-and-Wait, IF (editor decision), Gmail (editor rejection), HTTP Request, Gmail (success), Slack (finance alert).*

Congratulations, you have just built an entire content automation AI workflow.

## One more thing: error handling

Your workflow will run unattended. Things will break. APIs go down, tokens expire, and Slack rate limits may be hit.

> “Your workflow will run unattended. Things will break.”

Before you put this in production, set up **Error Workflow.** In n8n, go to your workflow’s Settings, scroll to Error Workflow, and select (or create) a workflow that fires whenever this one fails. A simple error workflow that just posts the failure details to a Slack channel will save you hours of debugging later.

## Where to go from here

This was just one example of building a complete AI end-to-end workflow. You can automate almost any workflow in any domain.

For this project, we chose Gmail, but you can choose Outlook. We chose Slack as the messaging platform, but you can use Microsoft Teams instead. You can make use of all the tools at your disposal.

A few ideas to build next:

1. [**GitHub PR**](https://thenewstack.io/what-github-pull-requests-reveal-about-your-teams-dev-habits/) **reviewer:** Trigger on a pull request, send the diff to an AI agent, and post a review comment with findings on security, bugs, and best practices.
2. **Lead scoring pipeline:** Capture leads from a form, enrich with Clearbit or Apollo, score them with AI based on your ICP, and push qualified ones to your CRM.
3. **Meeting action extractor:** Trigger on a Zoom or Fireflies transcript, extract action items with AI, and post them to the relevant Slack channels.

Pick one. Build it this weekend. That is how you actually learn n8n.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://cdn.thenewstack.io/media/2024/10/6698ac9e-cropped-4739937e-vinod-pal.jpg)

Vinod Pal is a full-stack developer and a member of the Andela network, a private global talent marketplace. With an eight-year track record of building end-to-end products, he specializes in .NET, NodeJs, React and Angular. He has developed microservices using...](https://thenewstack.io/author/vinod-pal/)