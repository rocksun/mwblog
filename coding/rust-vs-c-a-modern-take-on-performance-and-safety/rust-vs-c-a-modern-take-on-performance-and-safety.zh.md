如果你曾编写过底层代码，那么你很有可能与 C++ 打过交道。四十多年来，它一直是构建从游戏引擎和操作系统到金融交易系统和嵌入式设备等一切事物的首选语言。

它的强大之处在于赋予开发者对内存、性能和硬件近乎完全的控制，但这种强大也伴随着代价。一个错误的指针，你的整个程序就可能崩溃，或者更糟，为安全漏洞打开大门。

[Rust](https://thenewstack.io/rust-programming-language-guide/) 是系统编程领域的新星。它由 Mozilla 支持，并根据现代需求设计，承诺提供 [C++](https://thenewstack.io/introduction-to-c-programming-language/) 的速度和灵活性，同时避免内存安全隐患。Rust 不依赖运行时垃圾回收，而是通过其独特的所有权和借用模型在编译时强制执行 [安全规则](https://thenewstack.io/feds-critical-software-must-drop-c-c-by-2026-or-face-risk/)。

结果呢？一门旨在让崩溃、数据竞争和未定义行为成为历史的语言，同时仍然能生成极快的二进制文件。

但 [Rust 真的名副其实吗](https://thenewstack.io/code-wars-rust-vs-c-in-the-battle-for-billion-device-safety/)，它真的能取代 C++ 这样的巨头吗？还是它只是在一个本已拥挤的编程语言领域中又一个利基工具？

本文中，我们将把 Rust 和 C++ 并列比较，不是为了选出普遍的赢家，而是为了探讨它们各自的亮点、缺点，以及现代开发者如何为工作选择合适的工具。从内存管理和并发到工具链、性能和实际采用，让我们仔细看看系统编程的这两个巨头。

## 内存管理

### C++ 中的手动内存管理

C++ 在内存方面将控制权完全交给了开发者。你可以根据需要，在栈上或堆上精确地分配内存。这种控制级别是 C++ 最大的优势之一，但也是其最大的风险之一。

在经典的 C++ 中，你通常使用 `new` 和 `delete` 手动管理堆内存。这可行，但很容易忘记释放内存或不小心释放两次，这可能导致内存泄漏、悬空指针甚至安全漏洞。

```
#include <iostream>

struct Data {
int value;
Data(int v) : value(v) {}
};

int main() {
// Manual allocation on heap
Data* ptr = new Data(42);

std::cout << "Value: " << ptr->value << "\n";

delete ptr; // Free memory manually

// Uncommenting this would cause undefined behavior
// std::cout << ptr->value << "\n"; // Dangling pointer access
}
```

为了降低风险，现代 C++ 鼓励使用 RAII（资源获取即初始化）和智能指针，如 `std::unique_ptr` 和 `std::shared_ptr`，它们在超出作用域时自动释放内存。

```
#include <iostream>
#include <memory>

int main() {
auto ptr = std::make_unique<int>(42);
std::cout << "Value: " << *ptr << "\n";
// Memory is automatically freed when ptr goes out of scope
}
```

尽管智能指针有所帮助，但它们仍然依赖开发者选择正确的类型并始终如一地使用它。所有权设计中的错误仍然可能导致微妙的 bug。

### Rust 中的所有权和借用

Rust 以截然不同的哲学处理内存管理：在编译时使不安全的内存操作成为不可能。

Rust 系统的核心是所有权模型：

*   每段数据都有一个唯一的“所有者”。
*   当所有者超出作用域时，数据会自动释放——无需 `delete` 或垃圾回收器。
*   你可以借用数据的引用，但编译器会强制执行严格的规则，以防止数据竞争和悬空引用。

```
struct Data {
value: i32,
}

fn main() {
let d = Data { value: 42 }; // Ownership by `d`
println!("Value: {}", d.value); // Valid use

// Move ownership to `d2`
let d2 = d;
// println!("{}", d.value); // ❌ Compile error: value moved

println!("Value in d2: {}", d2.value);
} // d2 goes out of scope, memory freed automatically
```

借用允许你暂时使用数据而无需取得所有权，编译器会检查引用是否始终有效：

```
struct Data {
value: i32,
}

fn print_data(data: &Data) { // Immutable borrow
println!("Value: {}", data.value);
}

fn main() {
let d = Data { value: 42 };
print_data(&d); // Pass reference
print_data(&d); // Still valid, multiple immutable borrows allowed
}
```

对于可变借用，Rust 强制在任何给定时间只能存在一个可变引用，即使在多线程程序中也能防止数据竞争：

```
fn main() {
let mut x = 10;

let r1 = &mut x; // Mutable borrow
*r1 += 5;

// let r2 = &mut x; // ❌ Compile error: cannot borrow `x` mutably more than once
println!("{}", r1);
}
```

#### **主要区别**

*   在 C++ 中，你拥有对内存的完全自由，但这也意味着你负责防止内存泄漏、悬空指针和其他陷阱。
*   在 Rust 中，编译器是你的安全网。它在编译时强制执行内存安全规则，而不会增加运行时开销，在程序运行之前就消除了整类错误。

## 安全保障

### C++ 中的未定义行为

在 C++ 中，未定义行为（UB）指的是 C++ 标准不对其结果做任何保证的程序状态。一旦发生 UB，任何事情都可能发生——你的程序可能崩溃，产生不正确的结果，或者看起来工作正常，直到在生产环境中失败。危险在于 UB 在开发过程中通常不被注意，但可能在以后导致灾难性故障。

以下是一些导致 UB 的常见原因：

**解引用空指针**

```
#include <iostream>

int main() {
int* ptr = nullptr;
std::cout << *ptr << "\n"; // ❌ UB: dereferencing null
}
```

这可能在一台机器上崩溃，但在另一台机器上悄悄地损坏内存。

**缓冲区溢出**

```
#include <iostream>

int main() {
int arr[3] = {1, 2, 3};
arr[5] = 10; // ❌ UB: writing outside array bounds
std::cout << arr[5] << "\n"; // May overwrite other memory
}
```

C++ 不在运行时检查数组边界，因此越界访问可能会覆盖不相关的内存，导致难以发现的 bug 或安全漏洞。

**使用已释放的内存（Use-after-Free）**

```
#include <iostream>

int main() {
int* ptr = new int(42);
delete ptr; // Memory freed
std::cout << *ptr; // ❌ UB: accessing freed memory
}
```

**数据竞争**

在多线程 C++ 程序中，在没有适当同步的情况下从多个线程访问共享数据是 UB。

```
#include <thread>
#include <iostream>

int counter = 0;

void increment() {
for (int i = 0; i < 100000; ++i) {
counter++; // ❌ UB: data race
}
}

int main() {
std::thread t1(increment);
std::thread t2(increment);
t1.join();
t2.join();
std::cout << counter << "\n"; // Result is unpredictable
}
```

### Rust 的编译时保证

Rust 旨在在代码编译之前消除这些类别的未定义行为。它的借用检查器和类型系统强制执行严格的安全规则，而无需垃圾回收器。

**没有空指针**

在 Rust 中，变量不能为 null。如果某个值可能不存在，它会使用 `Option<T>` 明确表示。

```
fn main() {
let maybe_value: Option<i32> = None;

// Must explicitly check before using
if let Some(val) = maybe_value {
println!("Value: {}", val);
} else {
println!("No value");
}
}
```

**边界检查**

Rust 在运行时对数组执行边界检查，防止缓冲区溢出。

```
fn main() {
let arr = [1, 2, 3];
// println!("{}", arr[5]); // ❌ Compile error: index out of bounds at runtime
}

If you *really* want unchecked indexing for performance, you must explicitly use `unsafe`:

fn main() {
let arr = [1, 2, 3];
unsafe {
println!("{}", *arr.get_unchecked(1)); // Allowed, but you take responsibility
}
}
```

**没有使用已释放的内存（No Use-after-Free）**

Rust 的所有权模型确保内存只被释放一次，并且不存在对已释放内存的引用。

```
struct Data(i32);

fn main() {
let d = Data(42);
let d2 = d; // Move ownership
// println!("{}", d.0); // ❌ Compile error: value moved
println!("{}", d2.0);
} // d2 goes out of scope, memory freed safely
```

**数据竞争预防**

编译器强制执行以下规则之一：

*   存在多个不可变引用，或
*   存在一个可变引用——两者绝不能同时存在。

```
use std::thread;

fn main() {
let mut counter = 0;
let r1 = &mut counter;

// let r2 = &mut counter; // ❌ Compile error: already mutably borrowed
*r1 += 1;
println!("{}", r1);
}
```

对于多线程，你必须使用安全的并发原语，如 `Mutex` 或 `Arc<Mutex<T>>`。

```
use std::sync::{Arc, Mutex};
use std::thread;

fn main() {
let counter = Arc::new(Mutex::new(0));

let mut handles = vec![];
for _ in 0..2 {
let c = Arc::clone(&counter);
handles.push(thread::spawn(move || {
for _ in 0..100000 {
*c.lock().unwrap() += 1;
}
}));
}

for h in handles {
h.join().unwrap();
}

println!("Counter: {}", *counter.lock().unwrap()); // Always consistent
}
```

**主要区别**

*   在 C++ 中，安全性掌握在开发者手中，错误很容易溜走。
*   在 Rust 中，编译器强制执行安全规则，因此在安全代码中根本不会发生整类错误——而且不增加运行时性能开罚。

## 并发

并发是系统编程中最棘手的领域之一，因为它引入了依赖于时间差的 bug，这些 bug 通常难以重现。C++ 和 Rust 都为你提供了多线程工具，但它们在安全性方面采取了截然不同的方法。

### C++ 中的线程和竞争条件

C++ 提供了一个标准线程库 (`std::thread`, `std::mutex`, `std::lock_guard` 等)，允许你创建线程并同步对共享数据的访问。

然而，C++ 不在编译时强制执行线程安全。确保共享资源得到适当保护是程序员的责任。如果你忘记同步访问，很容易创建数据竞争，导致不可预测的结果。

```
#include <thread>
#include <iostream>

int counter = 0;

void increment() {
for (int i = 0; i < 100000; ++i) {
counter++; // ❌ Unsafe: no synchronization
}
}

int main() {
std::thread t1(increment);
std::thread t2(increment);

t1.join();
t2.join();

std::cout << "Counter: " << counter << "\n"; // Result is unpredictable
}
```

上面的代码说明了 C++ 中的数据竞争。在某些运行中，你可能会得到 200,000（正确），但由于竞争条件，更常见的是得到一个较小的数字。

但是，我们可以用 `mutex` 来解决这个问题。

```
#include <thread>
#include <iostream>
#include <mutex>

int counter = 0;
std::mutex mtx;

void increment() {
for (int i = 0; i < 100000; ++i) {
std::lock_guard<std::mutex> lock(mtx);
counter++;
}
}

int main() {
std::thread t1(increment);
std::thread t2(increment);

t1.join();
t2.join();

std::cout << "Counter: " << counter << "\n"; // Always 200000
}
```

虽然 `std::mutex` 有效，但很容易忘记锁定它，如果忘记了，C++ 在编译时不会给你任何警告。

### Rust 中的无畏并发

Rust 的所有权模型和类型系统也适用于并发。这意味着：

*   在没有明确同步的情况下，你无法在线程之间共享可变数据。
*   编译器在编译时防止数据竞争。对共享可变状态的不安全访问根本无法编译。

```
use std::thread;

fn main() {
let mut counter = 0;

let handle = thread::spawn(|| {
// ❌ Compile error: `counter` is borrowed by multiple threads mutably
counter += 1;
});

handle.join().unwrap();
}
```

前面的代码说明了编译时预防。在这里，Rust 拒绝编译，因为 `counter` 在没有同步的情况下被多个线程可变访问。

### **使用 Arc 和 Mutex 的安全并发**

要在 Rust 中在线程之间共享可变数据，你必须使用线程安全包装器，如 `Arc`（原子引用计数指针）和 `Mutex`。

```
use std::sync::{Arc, Mutex};
use std::thread;

fn main() {
let counter = Arc::new(Mutex::new(0));
let mut handles = vec![];

for _ in 0..2 {
let counter_clone = Arc::clone(&counter);
let handle = thread::spawn(move || {
for _ in 0..100000 {
let mut num = counter_clone.lock().unwrap();
*num += 1;
}
});
handles.push(handle);
}

for handle in handles {
handle.join().unwrap();
}

println!("Counter: {}", *counter.lock().unwrap()); // Always 200000
}
```

这里：

*   `Arc` 允许多个线程拥有相同的数据。
*   `Mutex` 确保一次只有一个线程访问数据。
*   如果你尝试在没有 `Arc/Mutex` 的情况下使用数据，编译器将拒绝。

#### **主要区别**

*   C++ 提供了强大的线程工具，但将所有安全检查留给你。数据竞争是运行时 bug，可能在为时已晚之前不被注意。
*   Rust 强制你在编译时安全地处理并发。不安全的模式根本无法编译，除非你明确将它们标记为不安全。

## 性能

当比较 Rust 和 C++ 时，原始性能是关键的战场。两种语言都编译为本地机器代码，都可以进行激进的优化，并且都赋予开发者对内存和 CPU 使用的底层控制。
在许多情况下，Rust 的性能与 C++ 相当——有时甚至超越它——这得益于其零成本抽象和在编译时而非运行时发生的安全检查。

### 编译速度和二进制文件大小

#### **C++**

*   对于小型项目通常编译速度更快。
*   大型项目由于头文件包含和模板实例化而导致构建时间长。
*   二进制文件大小可以更小，因为开发者对编译内容有更直接的控制。

#### **Rust**

*   由于借用检查器和优化器的繁重分析，编译时间较慢。
*   没有头文件——模块系统和 Cargo 依赖管理避免了 C++ 风格的编译级联。
*   二进制文件大小通常具有竞争力，但有时会更大，因为调试信息和单态化（泛型）会增加输出大小。

### 运行时基准测试

#### **示例 1：排序大数组**

#### **C++：**

```
#include <algorithm>
#include <vector>
#include <random>
#include <iostream>

int main() {
std::vector<int> data(1'000'000);
std::mt19937 gen(42);
std::uniform_int_distribution<> dist(0, 1'000'000);

for (auto &x : data) x = dist(gen);

std::sort(data.begin(), data.end());

std::cout << "First: " << data[0] << "\n";
}
```

#### **Rust：**

```
use rand::{Rng, SeedableRng};
use rand::rngs::StdRng;

fn main() {
let mut rng = StdRng::seed_from_u64(42);
let mut data: Vec<i32> = (0..1_000_000).map(|_| rng.gen_range(0..1_000_000)).collect();

data.sort();

println!("First: {}", data[0]);
}
```

结果：在优化构建中（C++ 为 -O3，Rust 为 –release），两者在大致相同的时间内完成（现代 CPU 上约 100-120 毫秒）。

#### **示例 2：并行计算（平方和）**

#### **带有 OpenMP 的 C++**：

```
#include <vector>
#include <numeric>
#include <omp.h>
#include <iostream>

int main() {
std::vector<long long> v(1'000'000, 3);

long long sum = 0;
#pragma omp parallel for reduction(+:sum)
for (size_t i = 0; i < v.size(); i++) {
sum += v[i] * v[i];
}

std::cout << sum << "\n";
}
```

#### **带有 Rayon 的 Rust**：

```
use rayon::prelude::*;

fn main() {
let v = vec![3_i64; 1_000_000];
let sum: i64 = v.par_iter()
.map(|x| x * x)
.sum();

println!("{}", sum);
}
```

结果：在四核机器上，两者都在约 20-30 毫秒内完成。Rust 的 Rayon crate 提供了符合人体工程学的安全并行性，无需显式锁或指令。

### 为什么 Rust 可以匹敌 C++ 性能

*   **零成本抽象**：Rust 的高级特性（迭代器、闭包、特性）编译成紧密的循环，没有额外开销。
*   **激进的编译器优化**：LLVM 后端对两者进行类似优化。
*   **安全性而无运行时开销**：当证明不必要时，编译器通常可以消除边界检查。

### C++ 仍有优势的地方

*   小型迭代构建的编译时间。
*   极度受限于大小的环境（闪存小于 64KB 的嵌入式系统）。
*   更多地控制避免边界检查（尽管 Rust 可以在不安全代码中做到这一点）。

## 工具和生态系统

语言的语法和性能很重要，但工具和生态系统通常决定了你日常工作的效率。

在这里，Rust 和 C++ 采取了截然不同的方法：一个是数十年来工具和标准的拼凑，另一个是统一的、功能齐全的体验。

### 构建系统

#### **C++**

*   没有官方构建系统。
*   大多数项目使用 CMake、Make 或 Ninja。
*   功能强大且灵活，但学习曲线陡峭。
*   构建文件可能冗长，跨平台兼容性通常需要自定义脚本。
*   最小 `CMakeLists.txt` 示例：

```
cmake_minimum_required(VERSION 3.10)
project(MyApp)
set(CMAKE_CXX_STANDARD 17)
add_executable(myapp main.cpp)
```

#### **Rust**

*   使用 Cargo，官方构建系统和包管理器。
*   用一个工具处理编译、测试、基准测试和文档。
*   默认跨平台。

```
cargo new myapp
cd myapp
cargo run
```

Cargo 自动创建项目结构，构建并运行它，无需任何外部配置。

### 依赖管理

#### **C++**

*   没有标准包管理器；开发者依赖 Conan 或 vcpkg 等工具。
*   通常需要手动下载和编译第三方库。
*   在大型项目中，依赖版本控制和兼容性可能是一个令人头疼的问题。

#### **Rust**

*   Cargo 与 Rust 的官方包注册表 [crates.io](http://crates.io/) 集成。
*   添加依赖项就像编辑 `Cargo.toml` 一样简单：

```
[dependencies]
rand = "0.8"
```

Cargo 自动获取、构建和链接依赖项，并进行适当的版本解析。

### 测试和文档

#### **C++**

*   没有内置测试框架；开发者使用 GoogleTest 或 Catch2 等库。
*   文档通常通过 Doxygen 或手动 README 文件处理。

#### **Rust**

```
#[test]
fn it_works() {
assert_eq!(2 + 2, 4);
}
```

使用以下命令运行测试：

`cargo test`

从文档注释自动生成文档：

`cargo doc --open`

### 生态系统成熟度

#### **C++**

*   经过数十年构建的庞大生态系统。
*   几乎所有领域——游戏、金融、嵌入式、科学计算——都有深厚的 C++ 库支持。
*   成熟的调试和分析工具（GDB、Valgrind、Visual Studio）。

#### **Rust**

*   快速增长的生态系统，尤其是在系统编程、CLI 工具和 Web 后端领域。
*   在非常专业的领域存在一些空白（某些图形或科学库仍然依赖 C++）。
*   强大的工具文化：`rustfmt` 用于格式化，`clippy` 用于 linting。

#### **主要区别**

*   C++ 工具功能强大但分散——你选择自己的构建系统、包管理器和测试工具。
*   Rust 工具统一且一致，使得启动和维护项目变得容易，甚至跨团队。

## 用例和采用

### C++ 仍然占据主导地位的领域

*   AAA 游戏引擎（如 Unreal Engine、CryEngine）。
*   重写成本过高的遗留系统。
*   硬件限制极度严格的实时嵌入式系统。
*   现有 C++ 库深度优化的科学计算领域。

### Rust 正在取代 C++ 的领域

*   **Web 浏览器**：Rust 为 Firefox 的主要组件（Servo 引擎）提供支持，以提高安全性和稳定性。
*   **命令行工具**：许多现代 CLI 应用程序（ripgrep、fd、bat）都是用 Rust 编写的，以实现速度和安全性。
*   **分布式系统和云基础设施**：Dropbox、Cloudflare 和 [Amazon](https://aws.amazon.com/?utm_content=inline+mention) 等公司将 Rust 用于网络服务。
*   **安全关键代码**：[Microsoft](https://news.microsoft.com/?utm_content=inline+mention) 将 Rust 用于 Windows 的某些部分，以减少内存安全漏洞。
*   **嵌入式开发**：Rust 在微控制器项目中越来越受欢迎，以实现可预测的性能和安全性。

### 主要区别：

Rust 不太可能在短期内完全取代 C++，但它已经成为新系统编程项目的默认选择，在这些项目中，安全性、可维护性和并发正确性至关重要。

## 互操作性

Rust 最实用的优势之一是它能够与现有的 C 和 C++ 代码库集成。这使得团队可以逐步采用 Rust，而无需重写数百万行遗留代码。

示例：从 Rust 调用 C 函数

```
C code ( math.c ):
int add_numbers(int a, int b) {
return a + b;
}
```

Rust code:

```
extern "C" {
fn add_numbers(a: i32, b: i32) -> i32;
}

fn main() {
unsafe {
println!("3 + 4 = {}", add_numbers(3, 4));
}
}
```

这种方法允许 Rust 使用安全的 Rust 接口封装现有的 C++ API，防止不安全的模式泄露到 Rust 代码库的其余部分。

### 从 Rust 调用 C/C++

Rust 可以使用其外部函数接口 (FFI) 通过 `extern "C"` 关键字调用 C 和 C++ 函数。你只需在 Rust 中声明外部函数并链接到编译后的 C++ 库即可。

示例：从 C++ 调用 Rust 库

```
Rust code:

#[no_mangle]
pub extern "C" fn multiply_numbers(a: i32, b: i32) -> i32 {
a * b
}
```

编译成库：

```
cargo build --release
C++ code:

extern "C" int multiply_numbers(int a, int b);

#include <iostream>

int main() {
std::cout << multiply_numbers(3, 4) << "\n";
}
```

这非常适合逐步将 C++ 项目迁移到 Rust——关键模块可以用 Rust 重写以提高安全性，而应用程序的其余部分则保留在 C++ 中。

## 学习曲线和开发者体验

### 错误消息和调试

#### **C++**

*   功能强大，但以神秘的编译器错误而闻名，尤其是在模板和元编程方面。例如：

error: no matching function for call to ‘foo(double)’

这可能会扩展成难以理解的页面模板实例化消息。

#### **Rust**

*   编译器错误清晰、详细，并且通常会给出修复建议。例如：

error[E0502]: cannot borrow x as mutable because it is also borrowed as immutable help: consider changing this borrow to be mutable

编译器更像是一个老师，而不是一个守门人。

### 社区和文档

#### **Rust**

*   非常强大，对初学者友好的社区。
*   官方指南（“[The Rust Programming Language](https://doc.rust-lang.org/book/)”，也称为“Rust Book”）全面且免费。
*   活跃的论坛、Discord 频道和频繁的会议演讲。

#### **C++**

*   庞大、全球性的开发者基础和数十年的知识积累。
*   资源丰富但分散——从 Stack Overflow 帖子到学术论文。
*   没有单一的“规范”初学者资源；学习路径差异很大。

总而言之，在系统编程方面，C++ 和 Rust 都无疑功能强大，但它们迎合了略有不同的理念。

C++ 是经验丰富的老将：成熟、久经考验，并深深植根于游戏、嵌入式系统、高性能计算和金融等行业。其生态系统范围无与伦比，与现有平台和工具链的集成使其在维护和扩展大型、成熟的代码库方面不可或缺。如果你正在处理遗留系统或在久经考验的几十年历史库至关重要的领域工作，C++ 仍然占据主导地位。

另一方面，Rust 代表着系统编程的新时代，在这个时代，安全性和性能并非互斥。它的所有权模型在程序运行之前就消除了整类错误，而 Cargo 及其现代生态系统使开发变得顺畅和可预测。对于新项目，尤其是在内存安全、并发正确性和开发者生产力是首要任务的情况下，Rust 提供了一个引人注目的、面向未来的选择。

实际上，许多团队不必选择唯一的赢家。混合方法通常最有意义：将关键的遗留代码保留在 C++ 中，但用 Rust 编写新组件以受益于其安全性和工具链。通过 FFI，两种语言都能够相互通信，这种互操作性允许你逐步演进代码库而不会牺牲稳定性。

最终，“正确”的工具不是在网络辩论中获胜的工具，而是适合你的项目需求、团队专业知识和长期维护目标的工具。Rust 和 C++ 都将继续存在；最聪明的开发者将学会利用它们各自的优势。