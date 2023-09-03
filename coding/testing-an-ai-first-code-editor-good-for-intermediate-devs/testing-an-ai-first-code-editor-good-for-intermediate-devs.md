# AI 优先代码编辑器测试：适合中级开发者

David Eastman 尝试了一下 Cursor AI。他发现它在某些中级任务上很有用，而且他在思考这是否是代码编辑器的未来。

翻译自 [Testing an AI-First Code Editor: Good for Intermediate Devs](https://thenewstack.io/testing-an-ai-first-code-editor-good-for-intermediate-devs/) 。

![](https://cdn.thenewstack.io/media/2023/09/0adee66a-screenshot-2023-09-01-at-17.09.32-1024x529.png)
*Cursor AI 的图片*

在之前的帖子中，我曾经看过[运行 Copilot 的 Visual Studio](https://thenewstack.io/the-changing-role-of-human-developers-in-an-ai-and-llm-world/)，但那时候还有关于大型语言模型（LLM）的炒作，那是在遥远的 2023 年 4 月。现在炒作已经有所退却，我们可以看看基于 LLM 的助手实际可以为软件开发者提供什么了。

一方面，编写一个专门用于使用人工智能的编辑器是有道理的，这就是 [Cursor AI](https://www.cursor.so/) 的用武之地。我已经听说过开发者推荐这个工具。Cursor 自称是“一款基于人工智能的代码编辑器，可以帮助您更快地进行编辑。您可以使用 Cursor 以自然语言编辑代码，修复运行时错误并找到难以找到的代码。”

但是，明显存在一个依赖 OpenAI 的问题，而 Cursor AI 正是如此。当您查看[定价计划](https://www.cursor.so/pricing)并意识到它们混淆了“慢”和“快”的 GPT-4 调用以及 GPT-3.5 调用时，这一问题就暴露出来了。从技术角度来看，这可以更改或放在应该的后台，但他们仍然不得不将他们的路线图与 OpenAI 提供给他们的访问联系起来。

我从他们的网站上下载了 Mac 版本 0.8.6 。您可以注册或使用自己的 OpenAI 密钥。Cursor AI 本身是 VSCode 的一个分支，它引入了语言扩展，以允许它与多种风格的多个代码库一起工作，尽管它不是一个集成开发环境（IDE）。窗口的设置就像您所期望的一样，但右侧有一个聊天窗口。

它附带了一个内置的教程，包括示例，我从一个带有错误的 rust 文件开始。执行代码后，我很高兴解决运行时错误，但这给了我一个机会来查看一些 rust 代码。我发现了这个错误，但无法说服 Cursor AI 实际编译代码。（VS Code 对于环境帮助不大，但如果我是一位常规的 Rust 开发者，这就不是问题了。）

当我最初要求它找到代码中的错误时，它找到了缺少的 crate。但我更感兴趣的是基本的设计缺陷：

```rust
use std::io::{self, Write};
use std::collections::HashSet;

const MAX_TRIES: u8 = 7;
const WORDS: [&str; 3] = ["openai", "chatgpt", "hangman"];

fn main() {
    let word = WORDS[rand::random::<usize>() % WORDS.len()];
    let mut guessed_chars: HashSet<char> = HashSet::new();
    let mut tries_left = MAX_TRIES;

    while tries_left > 0 {
        println!("You have {} tries left.", tries_left);
        print!("Guessed characters: ");
        for ch in &guessed_chars {
            print!("{} ", ch);
        }
        print!("nWord: ");
        let mut found = false;
        for ch in word.chars() {
            if guessed_chars.contains(&ch) {
                print!("{}", ch);
                found = true;
            } else {
                print!("_");
            }
        }
        println!();

        if found {
            println!("Congratulations, you've won!");
            return;
        }

        ...
    }

    println!("You've lost! The word was '{}'", word);
}
```

虽然我没有注意到缺少的 crate（或库），但我确实发现了与 Rust 无关的问题。原本应该是一个类似 “hangman” 的猜词游戏，但只要猜对一个字母，你就能赢。

第二次我要求 Cursor AI 找到错误时，它正确地找到了它：

> “是的，这段代码有一个错误。问题出在 **found** 变量及其用法上。**found** 变量在任何字符被猜对时都会设置为 **true**。然而，只有在检查完单词中的所有字符后，**found** 为 **true** 时才宣布游戏获胜。这意味着只要玩家至少猜对一个字符，而不一定是所有字符，游戏就会被宣布获胜。”

尽管这只是提供的示例中的一个孤立问题，但这仍然是一个很好的发现。摘要描述足以指导对游戏或代码不熟悉的人。虽然最好通过编写单元测试来找到 bug，这也会防止你编写像上面那样的代码，但如果你被给予一些要考虑的代码，这将为你节省一些时间。

我收到了一封来自 Cursor 的友好电子邮件，其中包括示例以及使用 AI “需要一些学习和努力”的警告。这是一个公平的观点。我使用这些示例进行了进一步的探索。

## C 语言示例

“`选择 20 行代码，然后按 Cmd+K 提示进行编辑`”。我使用了 C 语言示例，其中包括一个链接列表和使用它的方法。当我隔离一部分代码并要求进行编辑时，它提出了一些明智的建议，还将解释文本写入了编辑器窗格。更合适的是，它使用了绿色和红色的添加/删除界面，您可能在合并对话框中看到这种变化：

![](https://cdn.thenewstack.io/media/2023/09/56b47b87-untitled-1024x427.png)

我不太明白这与“撤消”功能如何配合使用，所以偶尔会在过程中有点迷失。建议本身，旨在避免经典的空指针错误，足够可靠。

“在聊天中点击 ‘with codebase’ 以查找代码片段”。在我复制链接列表 C 代码中的 `b->prev` 并将其添加到聊天窗口后，我点击了 “with codebase” 。然后，它对示例中使用的双链表提供了非常好的描述。它没有因为 b 只是一个局部变量而感到困惑。

这让我稍微想起了那些你只有在看完电影后才能完全欣赏的电影评论。然而，对于一个中级开发者来说，如果给了一段新代码，这可以很快地使他们适应。

“在聊天中使用‘@’提出关于库的问题”。我从 C 示例中选择了 `#include <unistd.h>` 行并将其添加到聊天中，然后要求聊天聊一下它。它做了重要的事情，就是解释了库在代码中的使用位置以及用途。再次强调，这对于绝对初学者来说可能不太好，但对于使用新语言的人来说，这比不断在 Stack Overflow 上进行检查更高效。然而，那个论坛上经常有争论的观点往往更加深入。

## Rust 翻译

最后，我进行了一次翻译。毫无疑问，这是一个强大的功能，该工具非常适合此用途。我从示例文件中选择了一个小的 Python 函数并将其翻译成了 Rust。再次强调，我正在使用给定的示例，因为它们似乎是完全有效的：

![](https://cdn.thenewstack.io/media/2023/09/9714c883-untitled-1.png)

供您检查的代码如下：

```python
def generate_random_number(output):
    # Simple pseudorandom number generator using system time
    random_number = time.time() - float(str(time.time()).split('.')[0])
    random_number = int(random_number * (10**6))

    # Ensure the number is different for different processes by adding the process id
    random_number += os.getpid()

    output.put(random_number)
```

响应是：

![](https://cdn.thenewstack.io/media/2023/09/810c7ae4-untitled-2-716x1024.png)

底部的简短解释更注重功能而不是实用性。

生成的代码如下：

```rust
use std::time::{SystemTime, UNIX_EPOCH};
use std::process;
use std::sync::mpsc::Sender;

fn generate_random_number(output: Sender<u64>) {
    // Simple pseudorandom number generator using system time
    let start = SystemTime::now();
    let since_the_epoch = start.duration_since(UNIX_EPOCH)
        .expect("Time went backwards");
    let in_ms = since_the_epoch.as_secs() * 1000 +
        since_the_epoch.subsec_nanos() as u64 / 1_000_000;
    let random_number = in_ms - in_ms / 1000 * 1000;

    // Ensure the number is different for different processes by adding the process id
    let random_number = random_number + process::id();

    // Send the random number to the output channel
    output.send(random_number).unwrap();
}
```

虽然我不专业使用这两种语言，但我们可以看到，如果当前日期早于 1970 年，这段代码添加了一个有趣的警告！

我不禁想到，这可能是一个工具，位于专业开发者和初学者之间。但它似乎非常适合用于翻译等中级任务。

我不太喜欢在我的编辑器中看到聊天窗口，但我也见过有人从准备好的 ChatGPT 解决方案中构建代码。在开发中使用 AI 的 UI 支持仍然很新，所以现在说它还不太自然可能不公平。目前它还不能完全与“撤消”功能配合使用，而且解释文本绝不应该进入编辑器窗格。

然而，未来可能已经来临。当汽车首次出现时，即使启动发动机也需要对燃烧有亲密的了解和一个曲柄手柄。虽然软件行业仍然尊崇大师级的工匠，但我们肯定已经进入了一个平均而言，代码操作将由经验较少的工程师来处理的时代。从技术上讲，对于这个工具的真正大规模受众可能还需要几年的时间。
