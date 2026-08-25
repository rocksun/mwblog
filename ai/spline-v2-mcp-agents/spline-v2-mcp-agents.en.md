Spline released V2 on Thursday, a complete rebuild of its 3D editor that enables external coding agents to work directly on live, editable scenes.

The key new addition, Spline MCP Server, opens the editor to Claude Code, Cursor, Codex, Google Antigravity and VS Code. Through a local server bundled with the desktop app, those tools can work directly within a live Spline project, changing the scene and its behavior while keeping the result fully editable.

Spline V2 also includes its own AI agent, which can build and edit a scene from a prompt. MCP lets developers access the same design environment from a coding agent that already understands the codebase and the work in progress, without having to rebuild that context in a separate Spline conversation.

> Through a local server bundled with the desktop app, those tools can work directly within a live Spline project, changing the scene and its behavior while keeping the result fully editable.

## MCP calls hit live scenes

The MCP server is bundled directly into Spline’s rebuilt desktop application for macOS and Windows; it does not work in the browser, and there is no standalone server package to install.

When the desktop app opens, it looks for supported clients and registers the server in their configuration files. The developer then restarts the AI client and prompts it normally. If someone asks Claude Code to create a floating island, for example, Claude turns that request into structured MCP tool calls. Spline then routes those calls to an open 3D editor tab, where they run against the live document. If no suitable file is open, the application can create one.

The model can see what is already happening in the scene before it starts making changes, which lets it move between the visual design and the code running over the canvas, use Spline’s AI tools when it needs a new model or image, and keep working on the interface or game logic around it.

Everything it changes stays inside the Spline project, so the designer gets the live scene back instead of a flattened image or static mesh and can continue editing as soon as the agent is done.

Spline says its internal AI agent follows the same approach, with each change treated as a normal editor operation that appears in the undo history and syncs to everyone else working in the file. Spline isn’t the only creative platform handing MCP keys to external agents. ElevenLabs recently [opened its voice-agent infrastructure to Claude through an MCP server](https://thenewstack.io/elevenlabs-mcp-voice-agents/) — letting a chat window manage production voice agents the same way Spline now lets a coding agent manage a 3D scene.

> Everything it changes stays inside the Spline project, so the designer gets the live scene back instead of a flattened image or static mesh and can continue editing as soon as the agent is done.

## Agents cross the canvas gap

The setup becomes more useful when an agent needs to move between the application and its interface, since Spline V2 puts the 3D editor and Hana behind the same MCP connection and handles the handoff automatically, directing scene work to the 3D editor and interface changes to Hana.

In Hana, the agent can turn an existing component into an editable frame and then carry any visual changes back into the application code, using stable references on exported elements to find the right place in the source.

That round trip has limits because Hana supports only a subset of HTML and CSS built around flexbox, so complex markup and framework-specific components may need to be reconciled with the existing code rather than replaced directly.

For 3D work, a developer can build or change a scene through Claude Code, refine it visually in Spline and export it for the web in formats ranging from Vanilla JavaScript and Three.js to React, Next.js and React Three Fiber. Those exports use WebGPU by default and fall back to WebGL when necessary.

Spline’s runtime API can control a published scene, but the company does not document a way for changes made to the exported code to flow back into the original 3D file. If the agent needs to revise that source, it has to return through MCP and work in the live editor.

Google Antigravity, only recently [expanded beyond its own IDE](https://thenewstack.io/google-antigravity-ide-extensions/) with extensions for VS Code and JetBrains — Spline now gives it yet another surface to work on. OpenAI’s Codex, another supported client, recently gained the ability to [keep coding while it waits for a developer’s answer](https://thenewstack.io/codex-async-developer-messaging/).

## Editing before export matters

Spline already offers a Code API that lets a web application use JavaScript to control the state and behavior of a published scene while it is running.

The MCP server comes into play while the scene is still being built, giving the agent direct access to the editable document so it can understand its structure and make changes before export. Here, MCP serves as a control interface for the editor, while Spline continues to manage the visual project and render the changes as they happen.

## Local server, scoped access

The connection stays on the developer’s machine, with the server bound to `127.0.0.1` and protected by an origin allowlist that blocks arbitrary web pages. Developers can choose which clients have access through Spline’s MCP settings.

According to Spline, the prompts and scene data exchanged with its MCP server stay between the desktop app and the connected client. If the agent uses one of Spline’s AI generation features, however, that work still runs in the cloud just as it would if started manually from the editor.

Several agent sessions can connect to the same editor, but Spline’s documentation does not explain how teams can attribute or review individual MCP changes before publishing a shared file.

> Several agent sessions can connect to the same editor, but Spline’s documentation does not explain how teams can attribute or review individual MCP changes before publishing a shared file.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://thenewstack.io/wp-content/uploads/2026/06/c176528b-cropped-54a705ce-amandacaswellheadshot_4-600x600.jpeg)

Amanda Caswell is an AI journalist, certified prompt engineer, and technology commentator whose work and expertise have been featured on Fox News and CBS News. She covers artificial intelligence, developer tools, foundation models, and emerging technologies, with a particular focus...

Read more from Amanda Caswell](https://thenewstack.io/author/amanda-caswell/)