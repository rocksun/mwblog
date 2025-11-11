To help a team member get up to speed on a project, I had to learn and then document how to set up a Mac environment with both Node.js and the .NET runtime. I had never used .NET on a Mac, so the first customer for this piece of documentation was me.

Naturally, I tapped my team of AI assistants who collectively hold a lot of knowledge about the topic. They wrote instructions, I followed along and reported problems, and we iterated toward the solution.

Then the penny dropped: These AI assistants can not only help write the instructions, but they can also read them and help me reproduce them. I’ve decided to call this **the flywheel effect**. It’s not automatic; I’ve yet to have the kind of hands-off experience that others report with AI, but that’s not my goal. I don’t want to be out of the loop; I want to be in it efficiently: Start the flywheel spinning, then tap it strategically to build momentum.

## The Role of an MCP Server in the AI Workflow

A key enabler for this scenario was a filesystem MCP server that enables agents like Claude and Cursor to read and write files. Anthropic’s [reference implementation](https://github.com/modelcontextprotocol/servers/tree/main/src/filesystem) granted the access required to read and write the evolving document. It did not grant access to run the necessary system commands, so I was firmly in the loop: Copy/paste the commands they suggested, run them, copy/paste the output, and discuss next steps.

> I don’t want to be out of the loop, I want to be in it efficiently: Start the flyweel spinning, then tap it strategically to build momentum.

This worked beautifully, modulo the ongoing struggle to manage MCP configuration across a team of assistants. Each has its own configuration file, and although the MCP protocol itself is standard, the locations and formats of these config files are not.

In [How LLMs Guide Us to a Happy Path for Configuration and Coding](https://thenewstack.io/how-llms-guide-us-to-a-happy-path-for-configuration-and-coding/), I observed that configuration is the new hard problem — one that eclipses cache invalidation, naming, and off-by-one errors. You can enlist AI assistants to debug their own configurations, but I wish people who run [our own MCP server](https://github.com/xmlui-org/xmlui-mcp) didn’t have to; it’s a buzzkill. Is there a better way to handle this? If so, please let me know, I’m all ears.

You can also do this kind of thing in a more direct way using Claude Code or Codex. To test that approach, I nuked the installation and asked Claude Code to read the instructions, follow the steps, run all the necessary commands with my permission, evaluate outputs, and produce a final report. Everything got installed, the backend server started, and the frontend app ran successfully. Here’s the report.

```
  1. Verify Node.js/npm prerequisites

  node --version && npm --version
  Output: v20.19.0 and 10.8.2 ✅ (meets v20+ requirement)

  ---
  2. Install .NET 9.0 SDK on macOS

  brew install dotnet
  Output:
  - Successfully installed to /opt/homebrew/Cellar/dotnet/9.0.8
  - Note about potentially needing DOTNET_ROOT environment variable
  - Installation completed without errors ✅

  ---
  3. Verify .NET SDK installation

  dotnet --version
  Output: 9.0.109 ✅ (confirms SDK, not just runtime, was installed)

  ---
  4. Install frontend dependencies

  npm install
  Output:
  - Installed 895 packages in 12 seconds
  - Deprecation warnings (as expected per guide)
  - Completed successfully ✅

  ---
  5. Start backend API server

  npm run start:backend
  Output evaluated:
  - Compilation warnings (expected C# nullable reference warnings)
  - Key success message: "Starting MWD Mock Server:"
  - "Now listening on: http://localhost:5001"
  - "Application started. Press Ctrl+C to shut down." ✅

  ---
  6. Start frontend development server

  npm run start
  Output evaluated:
  - Starting with options: { withMock: false, withProxy: undefined }
  - "➜  Local:   http://localhost:5173/"
  - CJS deprecation warning (informational, not blocking) ✅

  ---
  7. Copy test files

  cp tests/fixtures/* ~/mwd/shares/Documents/
  Verification:
  ls -lh ~/mwd/shares/Documents/
  Output evaluated:
  - test.jpeg (58K) ✅
  - test.pdf (3.8K) ✅
  - test.xlsx (8.1K) ✅
  - Plus additional pre-existing files

  ---
  8. Test backend API endpoint

  curl -H "Authorization: SessionID 12345" "http://localhost:5001/api/v3/ListFolder?path=:sh:Documents:/"
  Output evaluated:
  - Received valid JSON array with 9 file objects
  - Each object contains: name, path, created, modified, attributes, size
  - Test files present with correct sizes:
    - test.jpeg: 59,276 bytes
    - test.pdf: 3,908 bytes
    - test.xlsx: 8,337 bytes
  - HTTP 200 response ✅

  ---
  Key Validation Points:

  1. Installation process: brew install dotnet worked without manual PATH configuration
  2. Build process: Backend compiled with warnings but ran successfully
  3. Server startup: Both servers started and listened on expected ports
  4. File system: Backend correctly created ~/mwd/shares/Documents/ structure
  5. API authentication: Hardcoded SessionID 12345 worked as documented
  6. Data flow: Files copied to filesystem were accessible via API

  Documentation Accuracy:

  All steps executed successfully in order without modifications or workarounds.

```

View the code on [Gist](https://gist.github.com/judell/815a9b81cec4f37aac756e307beb8588).

We’ve long imagined documentation as a first-class software engineering discipline, but it hasn’t been clear exactly what that would mean. Now the picture is coming into focus. AI assistants can help us not just [create documentation](https://thenewstack.io/code-in-context-how-ai-can-help-improve-our-documentation/), but also [test it](https://thenewstack.io/how-llms-guide-us-to-a-happy-path-for-configuration-and-coding/) — just as we test our code. If you’ve ever struggled to write reproducible docs, or been frustrated by installation instructions that don’t work as described, you’ll appreciate the power of this flywheel effect.

## Iterating on an MCP Server With AI Feedback

When I used Claude to help build the first version of the [XMLUI MCP server](https://github.com/xmlui-org/xmlui-mcp), I was amazed to find that since Claude was also a client of that server, I could ask it to reflect on the responses it got from the tools provided by the MCP server and then adjust the server code to improve those responses. A major priority was to [anchor agents to ground truth](https://thenewstack.io/how-to-upgrade-your-mcp-server-with-context-engineering/), so we arranged for all responses to include dire warnings: invent no syntax, use and recommend only techniques backed by docs that include working examples, always cite the URLs of those docs.

> An agent-to-agent architecture may lie in the future.

With that guidance, coding agents behave better than they did before, but they often still ignore the guidance and require interactive reminders to follow it. Yelling louder at them won’t help. The root of the problem is that an MCP server has no independent agency. It can try to influence how an agent selects and uses its tools, but ultimately has no control over that selection and use. My hunch is that the MCP server needs to become more agent-like, so it can work with coding assistants’ agents on a more equal footing. An agent-to-agent architecture may lie in the future.

Meanwhile, when I recruited my team of assistants to evaluate the MCP server, they all agreed that the verbose guidance was wasting tokens. Sample feedback: “The MANDATORY” guidance block is repetitive and uses ~2k tokens per failure.” A related issue was that search results could be too verbose and were also chewing into the token budget.

I picked Kiro to streamline the responses, then I rebuilt the server and asked it to re-evaluate the sample queries that had produced unwieldy responses. Here’s what it saw.

*-Failure messages are now concise: Only three bullet points instead of 20+ “MANDATORY” warnings (saves ~1.5k tokens per failure)*

*-Result truncation working: Successful searches show 20 results with “… X more results omitted …” message (cleaner than the old “use JSON for full list”)*

*– Snippet truncation: Long lines are truncated at 200 chars with “…”*

*– All tools affected: The improvements apply to xmlui\_search, xmlui\_search\_howto, and xmlui\_examples*

Because this is a team effort, I then asked Cursor to do the same evaluation. Here’s what it noticed:

*Issue: When there are no results, the code always includes base rule reminders that aren’t useful:*

*“Cite sources with file paths and URLs” (no sources to cite)*

*“Provide URLs from documentation\_urls when available” (no URLs available)*

*These reminders are useful for successful searches, not failures.*

Good point! I relayed the feedback to Kiro, it made the implied changes, and I verified them with a round of feedback from the whole team.

## The Human Dev’s Role in the Virtuous Cycle

While I suspect that the nascent [agent-to-agent protocol](https://thenewstack.io/googles-agent2agent-protocol-helps-ai-agents-talk-to-each-other/) will enable this kind of thing to happen more autonomously, I’m happy to be the coordinator and I don’t think I’d ever want to fully abandon that role.

I’m reminded of the old adage about building a plane while you are flying it. In this case, weirdly and remarkably, the pilot who senses problems is also the mechanic who fixes them. Who am I in this scenario? To torture the metaphor, I guess I am the manager of the airline who sets goals, builds teams, starts the flywheel spinning, and taps it at the right times and in the right ways to accelerate a virtuous cycle of improvement.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://cdn.thenewstack.io/media/2025/02/9d121cd7-cropped-f95c0bac-jonudell-2025.png)

Jon Udell is an author and software developer who explores software tools and technologies and explains them in writing, audio, and video. He is the author of the cult classic Practical Internet Groupware. Past gigs include Lotus, BYTE magazine, Safari...](https://thenewstack.io/author/jon-udell/)