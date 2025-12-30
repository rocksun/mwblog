So far in my review of agentic development over the past year and heading into 2026, I’ve looked at some of the trends [shaping LLM services](https://thenewstack.io/from-agi-hype-to-engineering-reality-the-future-of-llms/). In this post, I’ll focus on what to expect for AI development tools in the new year.

As Cory Doctorow points out in his [Reverse Centaur summary](https://pluralistic.net/2025/12/05/pop-that-bubble/#u-washington), tech companies always want to be “growth stocks” — and for that reason they have to continually prove there is a new vision with untapped potential. This works against teams just improving on existing offerings — heaven forbid the company’s stock is marked as “mature.” But that is really what 2026 *should* be about: improving on the plethora of new things that developers are trying to get to grips with.

## 1. Improving Visibility and Management of Model Context Protocol (MCP)

Since Model Context Protocol (MCP) has quickly become the accepted way agents interact with external tools, there will have to be more effort to keep the MCP servers under control — either with central management or clearer dashboards. While developers have enjoyed the improved workflows that connectivity brings, the management of these has been a bit ad hoc. The success of MCP seems to work across silos, as non-technical staff want their agent requests to talk to Slack, etc. These internal connections kind of answer the “whats going on in my own business?” queries. Which means developers will be busy setting up MCP servers.

If there will be a lot of active MCP servers in an organisation, then management of them will start to become more significant. The more things people find to do with MCP, the more concerns will appear.

## 2. Supporting Parallel Task Execution for Senior Engineers

This year I looked at two apps ([Conductor](https://thenewstack.io/a-hands-on-review-of-conductor-an-ai-parallel-runner-app/) and [Verdent AI](https://thenewstack.io/first-look-at-verdent-an-autonomous-coding-agent-from-china/)) that explicitly support running tasks in parallel — that is, effectively defining a task and just leaving an LLM to execute it in the background while starting a new task. While you can generally ask any Agentic CLI to run a task in the background, more apps will support parallel running as a workflow in 2026.

One thing to note about executing these: to work on the same codebase, the target code needs to be isolated. This usually means making a new branch for each task and then putting the code into a fresh folder, which is what git worktrees does. You then merge the work back into the main branch. All this git fiddling plays slightly against the “vibe coding” moniker — but as I’ve pointed out, LLM tools will always gravitate towards being most useful to senior developers.

It is also only devs with solid experience who can quickly evaluate whether a change is safe enough to entrust to an agent… or not. And it is the senior developers who are already used to interruptions throughout the day, in this case coming from agents completing tasks at different times.

## 3. Clarifying the Roles of Agentic CLI vs. Desktop Applications

When we first saw [Claude Code](https://thenewstack.io/claude-opus-4-with-claude-code-a-developer-walkthrough/) running in a terminal session, it immediately got developers to define tasks in English instructions. Hence the term Agentic Command Line Interface (CLI). This was in sharp relief to using an IDE like VS Code.

Built in TypeScript and React, Claude Code ran in any terminal shell, allowing it to share an immediate environment and start in the same directory as the project to be worked on. This felt comfortable for many developers. There have been quite a few similar CLI apps released since then. The ability to also pass shell commands on the same prompt (implemented most cleanly [in Warp](https://thenewstack.io/warp-code-gets-closer-to-an-emacs-for-the-modern-ai-era/)) helped to reduce the friction of app swapping.

But many desktop versions were also released, such as [Claude Desktop](https://thenewstack.io/give-claude-ai-full-access-to-your-local-filesystem-with-mcp/), which offered the advantages of UI honed on MacOS or Windows. For example, you get nice file and folder views, along with more control over the request and response UI components. From an enterprise point of view, managing a desktop app is a bit easier too. However, exactly how the desktop app compares to the CLI version can still be unclear.

In 2026, I expect all major providers to make it clearer how they will support both their CLI and desktop versions of LLM products. Each version may have different communities, but they shouldn’t be treated as separate entities.

## 4. Integrating Paid Services and Agent-Driven Commerce

How agents successfully request paid services — i.e. agent-driven commerce — has to pop up at some stage. There isn’t a screaming demand for this, but eventually an agent will need to call upon a paid service in the background — or use a more expensive model in a task that the caller doesn’t have an explicit payment plan for. Most of us are simultaneously suspicious and accepting of the “machine-to-machine economy.” There is no point in autonomy that has to stop at the till. There may be various attempts to start addressing this over the year; especially for products that can use multiple models. This is especially true for developers running local LLMs who only want to call cloud LLMs for the deeper tasks.

## 5. Addressing the Challenges of VS Code Forks in AI Development

The [Microsoft Visual Studio Code forking problem](https://thenewstack.io/agentic-coding-and-the-weakness-of-extensions-for-ides/) has to be addressed a little more closely. We have seen quite a few non-Microsoft apps that are actually forks of VS Code under the covers — [Cursor](https://thenewstack.io/using-cursor-ai-as-part-of-your-development-workflow/) was an early example. While using the extension model within VS Code isn’t really good enough to support LLMs, forks have limitations too. The problem with finding other extensions in a less secure independent marketplace will probably remain an issue. In some respects Microsoft has successfully captured the market, leaving the competition to join or fragment. I don’t think anything broke inside me when Google launched its own VS Code fork, [Antigravity](https://thenewstack.io/hands-on-with-antigravity-googles-newest-ai-coding-experiment/), but it did bring the whole issue to a head again.

Too many product teams have seen a VS Code fork as a quick win, without ever really asking themselves if they have serious plans to buy their own home — or whether they will rent forever. Then they forget that their rental contract prevents them from hammering nails into the wall. But there are likely to be new approaches to get around this in 2026.

## Conclusion

This has been the breakout year for Agentic AI tools, especially the Agentic CLI, and I would expect 2026 will be about securing that ground. Developers don’t need to be convinced about what LLMs can achieve, but they do need to be convinced that the available products can be trusted to support their workflows over time.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://cdn.thenewstack.io/media/2022/09/2e2ac7a2-cropped-a46bbf33-photo.png)

David has been a London-based professional software developer with Oracle Corp. and British Telecom, and a consultant helping teams work in a more agile fashion. He wrote a book on UI design and has been writing technical articles ever since....

Read more from David Eastman](https://thenewstack.io/author/david-eastman/)