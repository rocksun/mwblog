[Rust](https://thenewstack.io/rust/) 不再是“新手”。它已成为[开发者技术栈的重要组成部分](https://thenewstack.io/rust-programming-language-guide/)，助力驱动性能关键型系统，并因其[内存安全](https://thenewstack.io/survey-memory-safe-rust-gains-45-of-enterprise-development/)、零成本抽象和富有表现力的类型系统而受到技术专家的信任。如果你使用过 [JavaScript](https://thenewstack.io/javascript-kung-fu-elegant-techniques-to-master-the-language/) 并想探索既具有表现力又达到系统级水平的语言，那么 Rust 将是完美的下一步，尤其是在我们这个 [Linux 驱动](https://training.linuxfoundation.org/training/programming-in-rust-lfd480/)的世界中。

在本教程中，我将向你展示如何编写“地道”的 Rust 代码，即简洁并遵循 Rustaceans（Rust 社区的名称）已建立的风格和实践的代码。我将专注于最佳实践、安全性和性能，同时拥抱 Rust 的环境和工具。我还将解释 Rust 开发者常犯的一些错误及其影响。

那么，为什么要选择 Rust 进行 [Linux 开发](https://thenewstack.io/introduction-to-linux-operating-system/)? 无论是构建命令行工具、守护进程，甚至是内核级软件，Rust 的设计都非常适合 Linux 环境。它速度快、性能可预测、具有强大的编译器检查、出色的类型系统以及无需垃圾收集器的内存安全。它的包管理器 [Cargo](https://github.com/rust-lang/cargo) 也是一个很大的优势。你基本上可以获得 C 语言级别的速度，而没有段错误或缓冲区溢出的风险。

## 安装 Rust

在 macOS 上，你可以使用 `rustup` 安装 Rust，这是官方安装程序，用于处理版本和工具链：

```
curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh
```

而在 Windows 上，请访问 [Rust 安装页面](https://www.rust-lang.org/tools/install) 下载 `rustup-init.exe`，然后按照安装程序中的命令行提示操作（对于大多数用户来说，默认设置就足够了）。

安装完成后，你可以使用 `cargo` 命令行界面来创建和管理项目。使用以下命令创建并运行一个新项目：

```
cargo new hello_rust 
cd hello_rust
cargo run
```

[![创建一个新的 Rust 项目](https://cdn.thenewstack.io/media/2025/07/2ddd82b7-rust_new-project1.png)](https://cdn.thenewstack.io/media/2025/07/2ddd82b7-rust_new-project1.png)

来源：Zziwa Raymond Ian

注意：我使用 VS Code 作为我的文本编辑器，并安装了 `rust-analyzer` 扩展。

## 编写和使用地道的 Rust 代码

现在开始介绍编写地道 Rust 代码的关键原则。

首先，Rust 通过 `Option` 和 `Result` 来保证安全。有了这种能力，Rust 可以帮助你避免空值。相反，它使用 `Option<T>` 和 `Result<T, E>` 来显式地处理缺失或失败的数据。

看一看下面的代码。

[![Rust 代码执行除法功能](https://cdn.thenewstack.io/media/2025/07/be89c8f4-rust_division.png)](https://cdn.thenewstack.io/media/2025/07/be89c8f4-rust_division.png)

来源：Zziwa Raymond Ian

在 `main` 函数中，使用 `divide` 函数执行两个除法运算。第一个将 10.0 除以 2.0，并对结果进行匹配：如果它返回 `Some(value)`，则打印结果；如果它返回 `None`，则打印一条错误消息，指示除数为零。第二次尝试将 10.0 除以 0.0，这会触发 `None` 的情况并输出错误消息。这演示了 `divide` 函数如何安全地执行两个 `f64` 数字之间的除法，方法是返回一个 `Option<f64>`，这有助于防止运行时错误，如除以零。如果除数 `b` 为 0.0，则该函数返回 `None` 以指示无效操作；否则，它返回 `Some(a / b)` 并带有结果。

这种方法使用 Rust 的 `Option` 类型以一种受控和类型安全的方式处理潜在的失败，鼓励开发者显式地处理结果不存在的可能性。

### Rust 中的 Crates

在 Rust 中，**crates** 是代码编译和共享的基本单元 —— 它们可以是库或可执行包。Rust 生态系统拥有丰富的高质量 crates，可以轻松快速且安全地构建健壮的应用程序。

请看下面的代码片段，了解如何通过项目的 `Cargo.toml` 文件使用 crates：

[![在 Rust 中使用 crates](https://cdn.thenewstack.io/media/2025/07/b2593f05-rust_crates.png)](https://cdn.thenewstack.io/media/2025/07/b2593f05-rust_crates.png)

来源：Zziwa Raymond Ian

此配置添加了以下 crates 作为依赖项：

* **`serde`** → 一个用于**序列化和反序列化**数据格式（如 JSON、YAML、TOML 等）的框架。`derive` 功能允许通过宏自动生成样板代码。
* **`tokio`** → 一个**异步运行时**，用于使用 async/await 语法编写并发程序，通常用于网络应用程序。
* **`clap`** → 一个强大且符合人体工程学的 crate，用于**解析命令行参数**，可以轻松构建用户友好的 CLI 工具。

添加完成后，你可以运行 `cargo build` 或 `cargo run`，Cargo 将自动下载、编译这些 crates 并将其链接到你的项目，如下图所示。

[![使用 cargo 在 Rust 中添加依赖项](https://cdn.thenewstack.io/media/2025/07/bad3f24a-rust_cargo.png)](https://cdn.thenewstack.io/media/2025/07/bad3f24a-rust_cargo.png)

来源：Zziwa Raymond Ian

### Rust 中的迭代器

Rust 通过其强大而灵活的**迭代器系统**鼓励函数式编程风格。你可以使用迭代器直接在集合上**链接操作**，例如 `map`、`filter` 和 `fold`，而不是依赖于传统的 `for` 循环。这通常会使代码更简洁、更具表现力且更有效率。

#### **例如：**

```
let nums = vec![1, 2, 3, 4, 5];
let doubled: Vec<_> = nums.iter().map(|x| x * 2).collect();
```

#### **发生了什么：**

* `nums` 是一个包含整数 1 到 5 的向量。
* `nums.iter()` 返回一个迭代器，用于**引用**每个元素 (`&i32`)。
* `.map(|x| x * 2)` 应用一个函数，该函数将每个项目乘以 2。由于 `x` 是一个引用，Rust 会在操作期间自动对其进行解引用。
* `.collect()` 将转换后的项目收集到一个新的 `Vec` 中，该 `Vec` 被分配给 `doubled`。

#### 为什么要使用迭代器？

* **惰性求值**：迭代器在需要时才计算值，从而提高了性能。
* **内存安全**：迭代器避免了常见的错误，例如越界访问。
* **循环融合**：编译器可以将链式操作优化为对数据的单次遍历。
* **可读性和可维护性**：通常可以使用链式迭代器方法更清楚地表达复杂的逻辑。

Rust 的迭代器系统是一个关键特性，使你能够以最小的努力编写高性能、干净且安全的代码。

### 模式匹配

模式匹配在 Rust 中非常强大，因为它提供了一种清晰、简洁和详尽的方式来处理不同的情况。它可以确保考虑到所有可能的输入，减少错误，并使代码更具可读性和可维护性，尤其是在使用枚举、范围和复杂数据结构时。

下面屏幕截图中的代码说明了模式匹配的强度。

[![Rust 中的模式匹配](https://cdn.thenewstack.io/media/2025/07/d59fe1b0-rust_pattern-matching.png)](https://cdn.thenewstack.io/media/2025/07/d59fe1b0-rust_pattern-matching.png)

来源：Zziwa Raymond Ian

这个 Rust 函数 `describe` 接受一个 `i32` 值，并返回一个字符串切片，该字符串切片基于模式匹配描述该值。它使用 `match` 表达式将 `value` 与多个模式进行比较：

* 如果是 `0`，则返回 `Zero`。
* 如果在 `1..=10` 范围内，则返回 `Between 1 and 10`。
* 对于所有其他值（由通配符 `_` 处理），它返回 `Greater than 10`。

返回类型 `&'static str` 表示该函数返回一个具有静态生命周期的字符串，例如字符串字面量。

## 在 Rust 中运行测试

在 Rust 中运行测试很容易：

[![在 Rust 中运行测试](https://cdn.thenewstack.io/media/2025/07/0f0cf221-rust_tests.png)](https://cdn.thenewstack.io/media/2025/07/0f0cf221-rust_tests.png)

来源：Zziwa Raymond Ian

这段 Rust 代码使用 `#[cfg(test)]` 定义了一个测试模块，它告诉编译器仅在运行测试时才包含该模块。在 `tests` 模块中，`use super::*;` 将父模块（如 `divide` 函数）中的项引入作用域。它包含两个单元测试：

* `it_divides_correctly` 检查 10.0 除以 2.0 是否返回 `Some(5.0)`。
* `it_handles_divide_by_zero` 验证除以零是否返回 `None`。

`#[test]` 属性将每个函数标记为测试用例。

使用这种方法可以让你自动验证代码的行为是否符合预期，从而更容易捕获错误并确保代码在一段时间内的正确性。

使用以下命令运行测试：

```
cargo test
```

你可以通过运行以下命令来添加 linter 和格式化程序：

```
cargo fmt # 格式化你的代码
cargo clippy # 捕获潜在问题
```

## 使用 Rust 构建计算器

为了演示 Rust 的工作原理，我将使用 `clap` 构建一个微型命令行计算器。

```
use clap::Parser;

/// 简单的计算器
#[derive(Parser)]
struct Args {
#[arg(short, long)]
a: i32,

#[arg(short, long)]
b: i32,
}

fn main() {
let args = Args::parse();
println!("{} + {} = {}", args.a, args.b, args.a + args.b);
}
```

这使用 `clap` crate 创建一个简单的命令行计算器，用于将两个整数相加。`Args` 结构使用 `#[derive(Parser)]` 进行注释，该注释会自动生成代码来解析命令行参数。每个字段（`a` 和 `b`）都标有 `#[arg(short, long)]`，允许用户使用短标志（如 `-a`）或长标志（如 `--a`）指定它们。在 `main` 函数中，`Args::parse()` 从命令行读取并解析参数，然后程序打印 `a` 和 `b` 的和。

## 调试错误

作为初学者，深入研究 Rust 既令人兴奋又充满挑战。Rust 强烈强调安全性、性能和正确性，这意味着编译器很严格，但这种严格性是你的盟友，而不是你的敌人。

不过，在 Rust 中很容易犯错误。修复以下常见错误是你成为一名自信的 Rustacean 的垫脚石。

### 1. 移动后使用值

```
let v = vec![1, 2, 3];
let moved = v;
// println!("{:?}", v); // ❌ 错误：移动后使用值
```

此代码创建一个包含值 `[1, 2, 3]` 的向量 `v`，然后将所有权分配给 `moved`。在 Rust 中，大多数类型（如 `Vec<T>`）没有实现 `Copy` trait，因此将它们分配给另一个变量会转移所有权，而不是复制数据。

因此，在移动后尝试访问 `v`（例如使用 `println!("{:?}", v)`）会导致编译时错误：`value used after move`。此行为强制执行 Rust 的所有权规则，该规则确保内存安全，而无需垃圾回收器。

为了解决这个混乱，你可以在需要时克隆或引用。

```
let v = vec![1, 2, 3];
let cloned = v.clone();
println!("{:?}", v); // ✅ OK
```

这会创建一个包含值 `[1, 2, 3]` 的向量 `v`，然后使用 `v.clone()` 创建它的一个深层副本，并将该副本存储在 `cloned` 中。与移动不同，克隆会显式复制内存中的数据，因此 `v` 和 `cloned` 都拥有相同值的单独副本。这允许 `v` 在克隆操作后保持有效和可访问，因此调用 `println!("{:?}", v)` 可以正常工作，而不会出错。

当你需要保留原始数据，同时在其他地方传递或存储副本时，克隆非常有用，尽管与移动相比，它在性能方面可能会更昂贵。

### 2. 克隆所有内容以修复所有权

```
fn print_length(v: Vec<i32>) {
println!("{}", v.len());
}

let v = vec![1, 2, 3];
// print_length(v.clone()); // ❌ 不必要的克隆
```

此代码定义了一个函数 `print_length`，该函数获取 `Vec<i32>` 的所有权并打印其长度。当调用 `print_length(v.clone())` 时，它会创建一个向量的完整副本，只是为了将其传递给该函数，这通常是不必要且效率低下的。

相反，由于 `print_length` 只需要读取长度，而不需要修改或保留向量，因此最好将其参数更改为接受引用 (`&Vec<i32>`)，以便可以在不克隆的情况下借用原始向量。

此处的克隆是不必要的性能成本，因为 Rust 允许安全的、非拥有的引用，当只需要读取访问时，可以避免复制数据。

要解决此问题，请使用借用。

```
fn print_length(v: &Vec<i32>) {
println!("{}", v.len());
}
print_length(&v); // ✅ OK
```

这定义了一个函数 `print_length`，该函数接受对 `Vec<i32>` 的不可变引用，而不是获取所有权。当调用 `print_length(&v)` 时，向量 `v` 被借用，而不是被移动，允许函数读取其长度而不获取所有权。这意味着 `v` 在函数调用后仍然可用，并且没有数据被克隆或复制，使其既高效又安全。

当你只需要从一个值读取时，像这样使用引用在 Rust 中是很常见的，因为它避免了不必要的内存分配并保留了所有权。

### 3. 误解生命周期

```
fn get_str<'a>() -> &'a str {
let s = String::from("hello");
&s // ❌ 错误：返回对局部变量的引用
}
```

返回的此引用指向 `s`，该 `s` 在函数结束时被删除，因此该引用无效。

有两种选择可以解决此问题。第一种是返回一个拥有的字符串。

```
fn get_str() -> String {
String::from("hello")
}
```

或者，你可以接受一个输入引用并返回一个与输入相关的引用。

```
fn get_str<'a>(input: &'a str) -> &'a str {
input
}
```

### 4. 阴影混淆

```
let x = 5;
let x = x + 1;
println!("{}", x); // 打印 6
```

变量阴影在 Rust 中是被允许和常见的。如果初学者期望重新赋值，但没有意识到阴影会创建一个新变量，他们可能会感到困惑。

这不一定是错误，但请注意，阴影会创建一个新变量，并且可以有目的地使用它。

### 5. 使用 `&String` 而不是 `&str`

```
fn print_str(s: &str) {
println!("{}", s);
}

let s = String::from("hello");
print_str(&s); // 工作正常

// 但是...

fn print_string(s: &String) {
println!("{}", s);
}

print_string(&s); // 有效但灵活性较差
```

使用 `&str` 比 `&String` 更灵活。除非你需要所有权或特定的 `String` 方法，否则请对函数参数使用 `&str`。

### 6. 需要时未使用带有 `mut` 的 `for` 循环

```
let mut v = vec![1, 2, 3];
for x in v {
x += 1; // ❌ 错误：无法赋值给 `x`，因为它不是可变的
}
```

在上面的代码中，循环变量 `x` 默认是不可变的。

要解决此问题，请使用 `mut` 关键字使 `x` 成为可变引用。

```
let mut v = vec![1, 2, 3];
for x in &mut v {
*x += 1; // 有效，因为 x 是一个可变引用
}
```

### 7. 未导入方法的 trait

```
fn main() {
let v = vec![3, 1, 2];
v.sort(); // ❌ 错误：无法将不可变局部变量 `v` 借用为可变的
}
```

某些方法需要 trait 导入。例如，`.sort()` 要求向量是可变的并且在作用域内。

```
let mut v = vec![3, 2, 1];
v.sort(); // 在可变向量上正常工作
```

### 8. 修改变量时忘记使用 `mut`

```
let x = 5;
x = 6; // ❌ 错误：无法对不可变变量赋值两次
```

变量在 Rust 中默认是不可变的。但是，`mut` 关键字允许你修改变量。

```
let mut x = 5;
x = 6; // 工作正常
```

### 9. 不使用 `Result` 处理错误

```
use std::fs::File;

fn main() {
let f = File::open("hello.txt"); // ❌ 警告：未使用的 Result
}
```

`File::open` 返回一个 `Result`。忽略它可以隐藏错误，并且会导致编译器警告。

使用以下方法解决上述问题：

```
use std::fs::File;

fn main() {
let f = match File::open("hello.txt") {
Ok(file) => file,
Err(e) => panic!("Error opening file: {}", e),
};
}
```

此代码尝试使用 `File::open` 打开一个名为 `hello.txt` 的文件，该函数返回一个 `Result` 类型，指示成功 (`Ok`) 或失败 (`Err`)。它使用 `match` 表达式来处理这两种情况：如果文件成功打开，则文件句柄存储在变量 `f` 中；如果发生错误（例如，文件不存在），则程序立即调用 `panic!`，这会使程序崩溃并打印错误消息。

此方法对于基本错误处理非常有用，尤其是在文件访问至关重要且程序无法在没有它的情况下继续进行时。但是，在生产代码中，通常首选更优雅的错误处理（如日志记录或回退行为）而不是 panic。

### 10. 使用没有帮助信息的 `.expect()`

```
let v: Vec<i32> = Vec::new();
println!("{}", v[0]); // 在运行时 panic

v.get(0).expect("Oops"); // 使用通用消息 panic
```

使用没有描述性消息的 `.expect()` 会使调试更加困难。

```
v.get(0).expect("Index 0 should exist in vector");
```

### 11. 需要 `.into_iter()` 或 `.iter_mut()` 时使用 `.iter()`

```
let mut v = vec![1, 2, 3];
for x in v.iter() {
*x += 1; // ❌ 错误：无法赋值给 `*x`
}
```

上面的代码会导致错误，因为 `.iter()` 给出不可变引用。使用 `.iter_mut()` 解决此错误。

```
for x in v.iter_mut() {
*x += 1;
}
```

## 如何提高你的 Rust 技能

从借用问题到生命周期混淆，每个错误都表明 Rust 如何迫使你深入思考内存、所有权和正确性。这种思考会带来更安全、更快且更易于维护的软件。虽然一开始可能会令人沮丧，但你遇到的每个编译时错误都是编写更好、更可靠代码的机会。

为了不断进步：

* **彻底阅读编译器错误。**：Rust 的编译器非常有用。花时间阅读它给出的建议，因为它们通常会直接指向解决方案。
* **使用诸如 `clippy` 和 `rust-analyzer` 之类的工具。** 这些工具可以帮助你捕获细微的错误并改进你的代码风格。
* **向社区学习。** Rust 社区热情友好，并且拥有大量的学习资源。阅读博客，关注 [Rust 用户论坛](http://users.rust-lang.org/) 上的讨论，或者在 Rust Discord 上寻求帮助。
* **构建项目。** 内化 Rust 原则的最佳方法是构建实际项目。从小处着手，然后逐渐增加复杂性。
* **为开源做贡献**。阅读开源 Rust 项目并为其做出贡献可以帮助你了解经验丰富的开发人员如何构建和编写地道的 Rust 代码。

进一步深入研究 Rust。阅读 Andela 的指南，了解如何[使用 AWS ECR 和 GitHub Actions 对 Rust 应用程序进行 Docker 化](https://www.andela.com/blog-posts/dockerize-a-rust-application-with-aws-ecr-and-github-actions/?utm_medium=contentmarketing&utm_source=&utm_campaign=brand-global-the-new-stack&utm_content=rust-docker&utm_term=writers-room)。