# Python 考虑更改版本编号

![Python 考虑更改版本编号的特色图片](https://cdn.thenewstack.io/media/2024/06/c2a2c9f1-nick-hillier-yd5rv8_wzxa-unsplash-1024x683.jpg)

一位 Python 核心维护者正在游说更改 [Python 编程语言](https://thenewstack.io/what-is-python/) 的版本发布编号方式。[Hugo van Kemenade](https://github.com/hugovk) 将担任即将发布的 Python 3.14 和 3.15 版本的发布经理，他撰写了提案 PEP 2026，即“ [Python 的日历版本控制](https://peps.python.org/pep-2026/)”，以确定所有未来版本的编号方式。

简而言之，此提案建议 Python 版本将编号为 3.YY.micro，其中：

* 3 是主版本号 - 始终为 3。
* YY 是次要版本号 - 是短年份号：{年份} - 2000。
* micro 是微版本号 - 每次进行错误修复或安全版本发布时都会递增。

他指出，永远不会有 Python 4。“Python 3”将成为未来的品牌。

因此，Python 3.15 实际上将是 3.26，“26”代表发布年份（“2026”）。

## Python 生命周期结束

van Kemenade 写道：“这旨在通过便于查看版本首次发布的时间，以及更轻松地计算其何时达到生命周期结束 (EOL) 来明确支持生命周期。”每个 Python 版本都支持五年。

自 2019 年以来，主要的 [Python 更新](https://thenewstack.io/how-python-is-evolving/) 每年都会进行一次，按照 [Pep 603](https://peps.python.org/pep-0693/) 设定的发布计划进行。他写道，这种编号方式可以更好地反映节奏。

许多人认为 Python 遵循 [语义版本控制](https://semver.org/) 的行业标准。SemVer 标准 [规定](https://www.joabj.com/Writing/Tech/Dev/1509-Software-Versioning.html) 版本号的格式为 MAJOR.MINOR.PATCH，其中 MAJOR 将是一次重大更新（可能会破坏 API 向后兼容性），MINOR 将是一个没有重大更改的版本，而 PATCH 将仅用于补丁。

由于 Python 3 的许多年度版本实际上破坏了向后兼容性，因此 Python 采用语义版本控制的这一假设导致了一些挫败感，尽管用户认为并非如此，因为所有新版本都在 3.XX 树中。但是，主版本号在第一个点之后递增，即 [当前版本为 3.12](https://devguide.python.org/versions/)，今年晚些时候的下一个主版本将为 3.13。

这些版本中的任何一个都可能带来重大更改，违反 SemVer 惯例（Python 实际上比语义版本标准早了大约 15 年）。

Van Kemenade 撰写并 [提出了他的提案](https://pyfound.blogspot.com/2024/06/python-language-summit-2024-should-python-adopt-calver.html) [Pycon 2024 会议](https://thenewstack.io/why-python-is-so-slow-and-what-is-being-done-about-it/)，该会议于上个月在匹兹堡举行。

van Kemenade 建议，Python 不应采用 SemVer，而应采用越来越常见的 [日历版本控制](https://calver.org/) (CalVer)，其中包括格里高利历年中的一些元素。

![使用 JavaScript 和其他语言的 CalVer 编号示例](https://cdn.thenewstack.io/media/2024/06/552d4a83-calver-examples.jpg)

摘自 Hugo van Kemenade（Python 基金会）的演示文稿

例如，Canonical 使用日历友好的 YY.0M.micro，其中年份由 YY 表示，月份由 oM 表示，补丁版本由 micro 表示。因此，当前的 Ubuntu 版本为 [24.02](https://ubuntu.com/download/server)。

未来，Python 版本将采用这种方式：

* 3.15.0 将于 2026 年发布（3.26）
* 3.16.0 将于 2027 年发布（3.27）
* 3.17.0 将于 2028 年发布（3.28）
* 3.18.0 将于 2029 年发布（3.29）
* 3.19.0 将于 2030 年发布（3.30）
依此类推…

Slashdot 上持怀疑态度的观察者指出，这种两位数方法在世纪之交会出现问题，其中两位数年份表示法会产生歧义，这使得构建系统难以自动更新到编程语言的最新版本，以及其他问题。

在 2100 年，Python v3.00 将紧随 Python v3.99 之后？

“难道 [Y2K](https://thenewstack.io/how-the-y2k-bug-returned-on-jan-1-2020/) 没有教会我们任何东西吗？”一位读者 [打趣道](https://developers.slashdot.org/story/24/06/15/0642232/python-language-summit-2024-security-workflows-calendar-versioning-transforms-and-lightning-talks)。

[
YOUTUBE.COM/THENEWSTACK
技术发展迅速，不要错过任何一集。订阅我们的 YouTube 频道，以流式传输我们所有的播客、访谈、演示等。
](https://youtube.com/thenewstack?sub_confirmation=1)