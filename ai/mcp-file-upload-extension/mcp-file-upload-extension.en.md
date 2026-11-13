![Arrows pointing up and down, depicting the concept of file uploads and downloads.](https://cdn.thenewstack.io/media/2026/11/b857591d-alex-shuper-ehko-zsjnoi-unsplash-1024x576.jpg)

The [Model Context Protocol](https://thenewstack.io/model-context-protocol-a-primer-for-the-developers/) (MCP) has played an instrumental part in connecting AI assistants to external tools and data since [Anthropic launched the project some two years ago](https://www.anthropic.com/news/model-context-protocol). Want to have a coding agent check the status of a bug? Give it access to your issue tracker through an MCP server. Or ask an assistant how many orders your company shipped last week? Connect it to a tool that can query your database.

Part of the Agentic AI Foundation [since last December](https://thenewstack.io/anthropic-donates-the-mcp-protocol-to-the-agentic-ai-foundation/), MCP [has a roadmap](https://thenewstack.io/model-context-protocol-roadmap-2026/) that reflects the demands of running the protocol in production. For instance, maintainers have been working to make servers easier to deploy without keeping track of individual client sessions, and to let companies manage access through their existing identity systems.

But a perennial problem developers have faced is how to pass a file from an AI app to an MCP tool. For example, say you attach a PDF to a chat and ask the assistant to save it to cloud storage — the assistant can call a tool to save the file, but developers *still* have to work out how to get the PDF from the chat app to the tool. That can mean issuing a temporary upload link, or perhaps sending the user to a separate upload page.

To address this gap, the folks at the MCP project have outlined a [draft extension](https://github.com/modelcontextprotocol/experimental-ext-file-uploads/blob/main/specification/draft/file-uploads.md) that gives clients and tools a common way to handle uploads and downloads.

![MCP's finally tackling the file-upload problem](https://cdn.thenewstack.io/media/2026/11/688112ca-file-transfer-round-trip.gif)

*MCP’s finally tackling the file-upload problem*

## Why MCP needs a way to move files

In a [blog post](https://blog.modelcontextprotocol.io/posts/exploring-file-uploads-and-downloads-in-mcp/) published on Tuesday, [Den Del](https://den.dev/about/)[i](https://www.linkedin.com/in/dendeli/)[marsky](https://den.dev/about/), lead maintainer of MCP and member of technical staff at Anthropic, and Google software engineer [Wil St. Charles](https://www.linkedin.com/in/wilstcharles/), lay out the rationale for the new extension, noting that developers’ needs have changed as they’ve started asking agents to do more with the tools MCP connects them to.

> “Many of those MCP server projects now need to work with files — often driven by increasing agent capabilities and autonomy.”

“Over the past two years, the things people build with the protocol have become more ambitious. *Much* more ambitious,” they write. “Many of those MCP server projects now need to work with files — often driven by increasing agent capabilities and autonomy.”

This demand has shown up in the community more or less since MCP’s inception. In [December 2024](https://github.com/modelcontextprotocol/modelcontextprotocol/discussions/1197), a developer building a tool to process files asked on GitHub how to get a file from the client to the server. An Anthropic team member [acknowledged](https://github.com/modelcontextprotocol/modelcontextprotocol/discussions/1197#discussioncomment-11450043) the difficulty and said they were exploring how a tool could send a file back to an AI app. Other community members subsequently chipped in with advice, with [one noting that they had built](https://github.com/modelcontextprotocol/modelcontextprotocol/discussions/1197#discussioncomment-12708679) their own way to send files from the AI app to the MCP server. Their MCP client uploaded the file directly to the server before calling the tool, with the upload itself happening outside the protocol.

Developers [have been looking for ways](https://www.reddit.com/r/Anthropic/comments/1o2982x/file_uploads_through_an_mcp_server_anyone_doing/) to hack around the gap ever since. In one [Reddit thread](https://www.reddit.com/r/mcp/comments/1w1jtu9/file_uploads_with_mcp_what_are_people_doing/) a few months back, one user said a temporary S3 upload link worked in Claude once outbound access was enabled, but they couldn’t get the same approach working in ChatGPT, so they built a separate web app and upload page. Another developer [said they had built](https://www.reddit.com/r/mcp/comments/1w1jtu9/comment/p6ldrsd/) a drag-and-drop interface to an MCP App, which let users submit files themselves but still left the agent without a way to initiate the upload on its own.

There are packaged options, too. [FastMCP offers](https://gofastmcp.com/docs/apps/providers/file-upload) a drag-and-drop upload component for developers building MCP Apps, while Box [recently launched secure file upload and download](https://support.box.com/hc/en-us/articles/52446938146067-Upload-and-download-PDFs-PowerPoint-Word-and-Excel-files-via-Box-MCP-server) support for PDFs and Office documents through its own MCP server.

The folks at the MCP project, for their part, have been slowly working toward a common standard. Delimarsky [opened an exploratory upload proposal](https://github.com/modelcontextprotocol/modelcontextprotocol/issues/1306) in August 2025, and a File Uploads Working Group, initially made up of members from Anthropic and OpenAI, [followed in April](https://modelcontextprotocol.io/community/working-groups/file-uploads). In October, the group [added file downloads](https://modelcontextprotocol.io/community/working-groups/file-uploads#changelog) to its remit.

Now, a [draft specification](https://github.com/modelcontextprotocol/experimental-ext-file-uploads/blob/main/specification/draft/file-uploads.md) sets out how transfers in both directions could work.

> “While we have the shape outlined, we’re not sure yet that what we started with is what we’ll end up with.”

“While we have the shape outlined, we’re not sure yet that what we started with is what we’ll end up with,” the authors write. “The best way to find out is, you guessed it — contact with reality.”

## How MCP would move files

The experimental file-transfer extension builds on the framework for extensions [MCP introduced in July](https://blog.modelcontextprotocol.io/posts/2026-07-28/) to let clients and servers opt into new features without changing the core protocol. The [experimental stage](https://modelcontextprotocol.io/extensions/overview#experimental-extensions) gives developers a place to prototype and refine an idea before, or alongside, a formal Specification Enhancement Proposal (SEP).

> Either way, the file itself bypasses the model.

Under the extension, if you ask an assistant to save an attached PDF to cloud storage, for example, the model calls the tool and the MCP client handles the upload. The client can send a small file within the tool request, and for a larger file, the client uploads it separately and calls the tool again to finish the job. Either way, the file itself bypasses the model.

For downloads, a tool that exports a CSV, for example, can include a download URL once it’s finished producing the file. The client can then fetch the CSV directly, and the model gets a message telling it what the tool produced.

One of the big [security implications](https://github.com/modelcontextprotocol/experimental-ext-file-uploads/blob/main/specification/draft/file-uploads.md#security-implications) centres around *how much* control the host should have over where files go. As things stand, the proposed extension limits when a client can send its MCP credentials to an upload destination. The host asks the user to approve the upload before the MCP server supplies that destination, so the user may not know where the file will go when they approve it.

“These safeguards control where the client’s MCP credential is sent, but they don’t by themselves control where the file goes,” the authors write.

So a user who thinks they’re saving a confidential PDF to company storage could end up sending it to an endpoint controlled by a malicious server operator. The authors recommend limiting external uploads to approved destinations, and are asking whether hosts should be required to enforce that restriction.

It’s worth noting that developers can prototype against the draft today by implementing the proposed transfer on a test client and server. However, there’s no formal reference implementation yet.

“That’s because we expect that a lot of the inner workings will, in fact, be quite different once we start integrating our experiment with third-party file services, such as cloud storage, database import/export, and many others that require file input and output,” the authors add.

The MCP maintainers say they are targeting a stable release by year-end, and support will remain optional — developers who choose to skip the extension won’t need to change their existing MCP clients or servers.

The post [Developers have been hacking around MCP’s file-upload problem for two years. A fix is taking shape.](https://thenewstack.io/mcp-file-upload-extension/) appeared first on [The New Stack](https://thenewstack.io).