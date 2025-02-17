# Bram之后的Vim：核心维护者讲述如何延续Vim的生命

![Featued image for: Vim After Bram: A Core Maintainer on How They’ve Kept It Going](https://cdn.thenewstack.io/media/2025/02/fa86b348-albuquerque-sunset-october-2022-photo-by-david-cassel-1-1024x774.png)

在它的创造者[Bram Moolenaar](https://thenewstack.io/bram-moolenaar-author-of-the-open-source-vim-code-editor-has-died/)于2023年8月去世后，[Vim开源文本编辑器](https://thenewstack.io/a-look-at-vim-a-text-editor-for-the-ages/)发生了什么？

它的社区默默地做出了英勇的努力，以确保他的项目继续存在。

Vim维护者[Christian Brabandt](https://github.com/chrisbra)在11月下旬的[VimConf 2024](https://vimconf.org/2024/)上[讲述了这个故事]。这是一个关于韧性、毅力和纪念的真实励志故事。

“你们可以看到的是，基本上开发并没有停止，”Brabandt在东京告诉他的听众。

每天都有新的pull request和issue需要审查，所以“它仍然非常活跃。GitHub上有很多活动。”

在2024年1月，他们发布了Vim 9.1——并将其献给Moolenaar。

## “开发没有停止”

平台顾问[Christian Brabandt](https://github.com/chrisbra)自2006年以来一直活跃于Vim社区，贡献了错误报告、修复程序和一些新功能。他曾参与Vim的正则表达式处理和对加密的支持，以及帮助构建其每日Appimage和“移动主页”。然后在2023年8月，突然“我成为了Vim的主要维护者之一。”

Moolenaar去世的消息“对我们所有人来说都非常震惊”，尽管Vim的邮件列表在前几周已经“非常安静”，并且“人们已经开始怀疑Bram怎么了？他在哪里？”

“我们必须决定我们要做什么。”

Brabandt首先承认他们“失去了很多知识”——不仅仅是Moolenaar的测试脚本。

Moolenaar在30年前开始了Vim，并且在他的脑海中保留了“关于他想要拥有的所有功能的原始Vim的大量知识”。但更重要的是，Moolenaar也是该项目的领导者。“他基本上决定了战略——他希望项目走向何方，他希望包含什么，以及他不喜欢什么。”

“我们必须重组并找到继续的方法。”

从一开始，就出现了一个至关重要的危机。当涉及到Vim的GitHub帐户时，“Bram是所有者。这意味着只有他才能做出某些决定——最终决定，例如为其他维护者设置角色和权限……我们需要拥有这种权力才能继续工作并邀请其他维护者加入该项目。”

幸运的是，GitHub实际上有一个“[已故用户”政策](https://docs.github.com/en/site-policy/other-site-policies/github-deceased-user-policy)，其中包括“[预先指定的继承人](https://docs.github.com/en/account-and-profile/setting-up-and-managing-your-personal-account-on-github/managing-access-to-your-personal-repositories/maintaining-ownership-continuity-of-your-personal-accounts-repositories)。”但不幸的是，Brabandt告诉他的听众，使用该政策“并不像听起来那么容易”，因为在填写完文件后，GitHub帐户“基本上会被停用。这对我们来说不是最好的，因为Bram的家人能够访问他的帐户，而且我不希望他们失去这种能力。”相反，Moolenaar的家人更改了权限，以便可以邀请其他维护者。

在Moolenaar去世后不久，“相当多的pull request”开始在GitHub上积累，Brabandt说。“所以我开始浏览这些并导入它们。”当另一位长期贡献者和核心维护者Charles Campbell决定退休时，“我决定邀请更多的维护者……主要是长期为Vim做出贡献的人。”

但除了源代码之外，他们还必须管理该项目的其他基础设施，但不幸的是，没有记录在案的流程，“所以我不得不找出所有这些——如何管理——基本上，以艰难的方式。”

似乎所有可能出错的事情都出错了。

- 处理Vim漏洞报告的站点是[被一家AI安全公司收购](https://www.businesswire.com/news/home/20230808746694/en/Protect-AI-Acquires-huntr-Launches-World%E2%80%99s-First-Artificial-Intelligence-and-Machine-Learning-Bug-Bounty-Platform)的，Brabandt说该公司“只想专注于AI，并且只专注于AI……开源漏洞报告基本上立即关闭了。”因此，该项目转向GitHub Security Advisory。
- Brabandt了解到Vim主页的基本代码在20年内没有改变。它仍然包含PHP 7代码——尽管对Php 7的支持
[于2022年11月结束](https://www.php.net/releases/index.php)。

- 托管其主页的服务于2023年7月被开源中国收购，并很快开始向访问者提供数据库错误，而支持请求无人回应。因此，在重组Vim项目的过程中，项目团队还必须为Vim的主页找到一个新的主机——但是，“不幸的是，这也意味着我们必须将主页从PHP 7升级到至少PHP 8的支持。”
- FTP服务器仍然由[荷兰Unix用户组](https://en.wikipedia.org/wiki/NLUUG)运行。“这在90年代和可能2000年代初还可以，”Brabandt说，但“现在我认为人们通常只是从GitHub或主页下载所有东西！”荷兰Unix用户组也不愿意给Brabrandt访问权限，并且“没关系……”他说，“因为我们随后决定停用旧的FTP服务器。如果需要进行下载，可以通过Vim主页完成。”

自从停用FTP访问以来，Brabandt说他没有听到任何抱怨。

## ICCF的情况如何？

直到2024年末，他们才意识到帮助页面仍然提到转发到Moolenaar旧电子邮件帐户的电子邮件地址。“就在大约两周前，我更改了这些地址，所以现在它们已被转发到我的地址，”Brabandt在11月告诉他的听众。

Vim以其著名的敦促用户向Moolenaar最喜欢的慈善机构[International Child Care Fund Holland](https://iccf-holland.org/)捐款而闻名，Brabandt说Moolenaar一家仍在维护[Bram的Paypal帐户以接收这些捐款](https://www.paypal.com/donate?token=GuL3qWPYJL3FgOkjPAvH6zDTpScmwWX1L-e_6b58Oj-7yKhpaM9KeyMMGzfgTsICdLw2HDRrLssfR9sS)（仍然从[Vim.org](https://www.vim.org/)链接）。在Moolenaar去世后，很多人向ICCF捐款，2024年又捐了9万欧元。Brabandt还致力于确保这些捐款按预期进行——并表示他不打算在不久的将来创建任何Vim赞助。

做出了一项更改：Bram Moolenaar的功能，该功能允许ICCF捐助者投票决定未来的Vim功能，已被关闭。很难弄清楚哪些ICCF捐款应该链接回Vim.org用户。（“我不确定Bram过去是怎么做的，”Brabandt说，“ICCF的其他人也无法告诉我！”）但实际上，事实证明，大多数新的增强请求和问题已经来自其他来源，如GitHub和Vim自己的待办事项列表。

## “维护模式”

那么未来会怎样呢？Brabandt告诉听众，Vim计划在即将发布的Vim 9.2版本中进行“一些可能更具争议性的更改”。这些包括支持XDG规范的[基本目录规范](https://www.freedesktop.org/wiki/Specifications/basedir-spec/)（“社区至少希望了10年。”）以及更好地支持[Wayland](https://en.wikipedia.org/wiki/Wayland_(protocol))。有一些新的选项和插件以及一些不可避免的错误修复。

因此，虽然正在进行更改，但这促使Brabandt对Vim的未来发表了一个平静而重要的声明。“但是，目前我会说Vim或多或少处于维护模式。我不认为任何维护人员可以全职从事Vim或更大的功能。”例如，他知道Neovim社区一直在进行重大更改，例如支持解析库[Tree-sitter](https://tree-sitter.github.io/tree-sitter/)，但将其添加到Vim将需要“巨大的努力……我不确定我们是否能够实现它，至少在短期内不能。”

但Brabandt宣布了另一个有价值的目标：确保社区的健康。这意味着欢迎新的贡献者，并使他们更容易开始贡献代码。Brabandt甚至导入了一些自动代码格式化工具，因为在Vim的源代码之前使用了一种特殊的格式化风格，Brabandt称之为“奇怪。这基本上是Bram的工作风格，这没关系，但它对新用户没有帮助。”

后面的幻灯片建议人们可以从事的工作包括“Tree-Sitter集成？”以及GTK版本的Vim的GUI界面和更高级的终端功能。例如，Vim的拼写检查代码“已经好几年没有被触及了。”

“如果你正在寻找未来的重大新功能，我们确实依赖社区来帮助我们，”Brabandt说。但他总是建议新的贡献者在第一次熟悉代码库时“从小处着手”。

目前，“已经合并的大部分更改都是相对独立的、小功能集，可以轻松测试，并且对代码的其他部分没有太大影响。”

## 测试、重构，也许可以淘汰Python 2接口
他们仍然在使用“防御性和安全”的C语言编码——Brabandt说，将所有内容重构为像Rust这样的现代编程语言目前还不是一个选择。他正在对所有更改运行一套全面的测试——并且每天他们都会运行代码分析工具[Coverity](https://en.wikipedia.org/wiki/Coverity)。展望未来，他们将重构部分代码，“这些代码相当长、冗长、复杂且难以理解。”（Vim真的还需要一个到Python 2的外部接口吗？既然Python社区多年前已经转向Python 3，Brabandt认为这是一个过时的接口的例子，可以在“未来的某个时候”被淘汰。）

一个重要的政策目标是确保继续Vim的向后兼容性。当然，从过去吸取教训，Brabandt放映了一张题为“新的Vim项目——未来”的幻灯片，其中包括一个关键的“政策”要点：“更好地记录（内部）流程。”

Brabandt说，他在查看Moolenaar积压的未处理的pull request时，提出了这些政策原则。

但他希望看到的另一个改进是对Vim社区有更好的理解——他甚至正在考虑进行用户调查。在他的演讲结束时，Brabandt告诉观众，自从Moolenaar去世后，他学到了什么：维护Vim是*困难的*——而且这是一项全职工作。“这不仅仅是编写代码；而是关于管理社区。”这意味着*倾听*那个社区——“倾听他们的请求，修复出现的错误，并确保我们能够跟上并做社区想做的事情。”

“这是一个开源项目——这意味着社区可以贡献，应该贡献，并且还可以帮助我们引导项目走向未来。”

Brabandt说，已经有一个清晰的信号表明这是一个[健康的社区](https://thenewstack.io/open-source/)：Vim大会本身。

[技术发展迅速，不要错过任何一集。订阅我们的YouTube频道，观看我们所有的播客、访谈、演示等。](https://youtube.com/thenewstack?sub_confirmation=1)