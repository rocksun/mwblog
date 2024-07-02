# 开发者使用 AI 的 5 种创意方式

![Featued image for: 5 Creative Ways Developers Are Using AI](https://cdn.thenewstack.io/media/2024/07/4b855ebb-bruce-mars-fwvmhua_wby-unsplash-1024x683.jpg)

随着 AI 在科技领域的广泛应用，以及随之而来的人工智能驱动的编码平台、工具和服务的数量不断增加，开发者们正在努力寻找最佳方式利用 AI 来帮助他们完成编程任务和目标，利用 AI 来提高效率，同时处理一些更繁重和耗时的编程任务。

为此，我与几位开发者进行了交谈，了解他们使用 AI 的一些创意方式。虽然许多人使用 [GitHub Copilot](https://github.com/features/copilot)、[Claude 3 Opus](https://www.anthropic.com/news/claude-3-family)、[Pieces for Developers](https://pieces.app/) 和 [Codeium](https://codeium.com/) 等工具来帮助生成代码和自动化任务，但开发者们一直在探索 AI 可以帮助他们提高效率的其他方式。

**1. 代码测试和 PR 审查**

“我知道有人使用 AI 来编写他们编写的代码的单元测试，”资深软件工程师兼 [Audiofeed](https://audiofeed.ai/) 联合创始人 Shane Thomas 说。“这为他们节省了大量时间，不必一遍又一遍地编写相同类型的测试。他们仍然需要验证结果，但他们似乎从中获得了良好的结果。”

虽然使用 AI 进行单元测试有其优势，但其他专家（如 [Tia](https://asktia.com/) 的技术主管 [Swizec Teller](https://www.linkedin.com/in/swizec/)）[建议谨慎](https://swizec.com/blog/why-you-shouldnt-use-ai-to-write-your-tests/)依赖 AI 进行测试。在 [X 上发布的笔记](https://x.com/Swizec/status/1793006221630533813) 中，Teller 建议开发者在某些情况下使用 AI 进行测试，例如使用 AI 生成大量“多样化的生产级输入”。

开发者们还使用 AI 来模拟代码审查，这可以帮助开发者为与人类同事的审查做好准备。“我知道有人使用 AI 作为其团队成员拉取请求审查的第一步，”Thomas 说。“他告诉我，他收到了其他工程师关于他的 PR 审查的全面性的评论……但他的许多笔记最初是由 AI 标记的。”

**2. 学习路径**

教育和学习是开发者将 AI 用于好处的另一个领域。

“[Bekah Hawrot Weigel](https://www.linkedin.com/in/bekah-hawrot-weigel/)，[OpenSauced](https://opensauced.pizza/) 的技术 AI 倡导者说：“我一直使用 ChatGPT 为我创建学习路径，以便我能够更深入地了解提示。我给了它关于我们每天应该做什么的指示，并要求它想出一个我们可以讨论的活动。”

**3. 自动化重复性任务**

开发者使用 AI 的另一种创意方式是自动化一些最繁重和耗时的开发任务，例如通过分析复杂的代码来帮助进行代码维护和跟踪难以捉摸的错误。在 [最近发表在 The New Stack 上的一篇文章](https://thenewstack.io/5-software-development-skills-ai-will-render-obsolete/) 中，[Tabnine](https://www.tabnine.com/) 的首席技术官兼联合创始人 [Eran Yahav](https://www.linkedin.com/in/eranyahav/) 建议 AI 将有助于消除一些枯燥乏味的工作。

Yahav 写道：“AI 编码工具自动化了如此多的任务，开发者可能会发现他们获得的一些技能将不再需要。但这没关系，因为许多技能都涉及开发者乐于放弃的枯燥乏味的工作。”

**4. 面向程序员的 AI 驱动的搜索**

虽然所有开发者都依赖搜索和 AI 工具来帮助他们解决代码问题，但有些人一直在使用新的 AI 驱动的工具来帮助找到人类专业知识。

Weigel 说：“我在这里有偏见，因为我在 OpenSauced 工作，但我们创建了一个名为 [StarSearch](https://app.opensauced.pizza/star-search) 的工具，它允许你通过索引各种形式的开发者活动（包括 git 历史记录）来找到开源领域的‘明星’。例如，你可以要求它帮助你找到既了解 Rust 又了解 Tailwind 的开发者。这是一个很好的例子，说明 AI 如何能够超越代码补全，并提供对开源的更深入见解，从而增强开发者发现和协作。”

**5. 生成文档和数据模型**

“[Pieces for Developers](https://pieces.app/) 的首席技术官兼创始工程师 [Mark Widman](https://www.linkedin.com/in/mark-widman/) 说：“我经常使用的一些非常棒的 [例子] 是 [使用 AI 来] 编写单元测试、文档，以及帮助进行数据模型和名称生成。”
The New Stack contributor [Jon Udell](https://www.linkedin.com/in/jon-udell-45915/) also [wrote about using AI to improve documentation](https://thenewstack.io/code-in-context-how-ai-can-help-improve-our-documentation/), detailing his experience using LLM-powered tools like [Unblocked](https://getunblocked.com/) to enhance code documentation creation and maintenance.

“Writing documentation from scratch is as rare as writing code from scratch. More often, you’re updating, extending, or refactoring existing documentation,” Udell wrote. “My expectation was that an LLM-powered tool pretrained on code and documentation could provide powerful assistance, and Unblocked delivers.”

**Caveats and Concerns**
While Widman is excited about all the progress OpenAI has made overall (especially the OpenAI API) — particularly how the latter is getting closer to developer workflows — he cautions that there’s still a lot of work to be done to improve upon what’s already been achieved. “I think they have a long way to go in terms of data privacy, additional operating system support, [and lowering the huge] latency costs.”

I’ve touched on the work that AI vendors haven’t done yet in terms of data privacy — see the “Drawbacks and Considerations” section in my previous article on [AI-powered development tools](https://thenewstack.io/favorite-ai-tools-of-developers-and-tips-for-using-them/) — but developers should have other concerns when considering the creative uses of AI. One danger is becoming overly reliant on AI to do too much, which could lead to a decline in code quality and developers being unable to perform development tasks without AI assistance.

In 2023, [GitClear published a study](https://www.gitclear.com/coding_on_copilot_data_shows_ais_downward_pressure_on_code_quality) that showed AI-assisted development is putting “downward pressure on code quality,” creating “a disturbing trend for maintainability,” and highlighting “ … the percentage of lines of code that are reverted or updated within two weeks of being written — projected to double in 2024 compared to the pre-AI baseline in 2021.”

**AI-Assisted Programming: Is the Best Yet to Come?**
Despite the caveats and potential drawbacks, the unstoppable march of technology means that more AI-powered development is on the horizon, which programmers can look forward to and creatively adapt to their custom needs. [Kristian Ranstrom](https://www.linkedin.com/in/redapollos/), owner of [Rainstorm Technologies](https://www.rainstormtech.com/) and a seasoned software developer, pointed to upcoming tools like [GitHub Copilot Workspace](https://github.blog/2024-04-29-github-copilot-workspace/) as a way to take developer productivity to new heights.

“It’s not open to the public yet, but I’m very excited about Copilot Workspace,” Ranstrom said. “I’m on the waitlist, and I’m eager to see how it will accelerate my work.”

Widman encourages developers to look at other ways AI is being used outside of software development for inspiration, then adapt and apply those examples to developer use cases. He also believes that more creative use cases will emerge thanks to the groundbreaking work of AI researchers and developers.

“One of the most important principles I live by is that we stand on the shoulders of giants, so there’s no harm in looking at what’s out there and applying it to your domain to help improve processes, save time [and] money, and do more amazing things!”

[
YOUTUBE.COM/THENEWSTACK
Technology is moving fast, don’t miss a beat. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.
](https://youtube.com/thenewstack?sub_confirmation=1)