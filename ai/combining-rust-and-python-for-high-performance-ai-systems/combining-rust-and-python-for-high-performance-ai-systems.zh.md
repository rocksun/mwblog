Python 为大多数人工智能 (AI) 和机器学习 (ML) 提供动力。凭借其丰富的生态系统——从 TensorFlow 和 PyTorch 到 scikit-learn 和 Hugging Face Transformers——[Python](https://thenewstack.io/what-is-python/) 已成为研究人员、数据科学家和工程师的首选语言。但 Python 有一个众所周知的局限性：速度。它的[全局解释器锁 (GIL)](https://thenewstack.io/pythons-gil-multithreading-and-multiprocessing/) 限制了并发性，而其解释型特性使其比 C++ 或 Rust 等编译语言慢几个数量级。

另一方面是 [Rust](https://thenewstack.io/rust-vs-c-a-modern-take-on-performance-and-safety/)：一种系统编程语言，它提供 C++ 级别的性能、无需垃圾回收的内存安全性以及现代开发人员工程学。Rust 旨在处理高性能、并发的工作负载——这正是 AI 应用在生产环境中通常需要的工作负载类型。

那么，为什么不将两者的优点结合起来呢？

*   利用 Python 成熟的 ML 生态系统，在 Python 中进行模型原型设计和训练。
*   将性能关键型组件（数据处理、推理内核、并行工作负载）推到 Rust，并从 Python 中无缝调用它们。

这种混合方法不仅仅是理论上的，它已经为当今一些最流行的 AI 库提供了支持：

*   Hugging Face Tokenizers 用 Rust 编写，以实现极快的速度，并提供 Python 绑定以提高可用性。
*   Polars，一个由 Rust 提供支持的 DataFrame 库，在保持熟悉的 Python 接口的同时，其性能通常优于 pandas。

在本文中，我们将探讨如何结合 Rust 和 [Python 构建高性能 AI 系统](https://thenewstack.io/building-autonomous-systems-in-python-with-agentic-workflows/)。您将了解到：

1.  为什么 Rust 在 AI/ML 中补充了 Python。
2.  如何使用 PyO3 和 Maturin 等工具将 Rust 集成到 Python 中。
3.  编写 Rust 函数、将它们公开为 Python 模块并在 AI 工作流中使用的实际示例。
4.  预示混合 AI 开发未来的真实案例研究。

到最后，您将看到 Rust 如何帮助克服 Python 的性能瓶颈——同时又不放弃使 Python 不可或缺的灵活性和生态系统。

Python 因其简单性和庞大的生态系统而在 AI 和 ML 领域占据主导地位。从 NumPy 到 PyTorch 和 scikit-learn，大多数前沿模型和研究代码都始于 Python。但随着项目从研究转向生产，Python 的弱点开始显现。

这就是 Rust 的闪光点。让我们来分解一下互补性。首先也是最重要的是：为什么 Rust 在 AI/ML 中补充了 Python。

## **1. 规模化性能**

*   Python 是解释型语言，即使有 NumPy 或 Cython 等工具，它在原始计算吞吐量方面也存在困难。
*   Rust 编译为原生机器码，提供 C++ 级别的性能和现代工具。
*   繁重的数值内核、矩阵运算或自定义 ML 层可以用 Rust 实现，并从 Python 中调用，从而在不重写整个管道的情况下实现大规模加速。

示例：Hugging Face 的 `tokenizers` 库通过用 Rust 重写核心部分，比其纯 Python 版本实现了显著的性能提升。

## **2. 没有全局解释器锁的并发性**

*   Python 的 GIL 阻止了 Python 字节码的真正多线程执行。
*   这在处理大型数据集或运行并行推理工作负载时是一个瓶颈。
*   Rust 具有无畏的并发性：它的所有权和借用系统确保了跨线程的内存安全性，从而实现了高效的多线程数据加载器、并行预处理或分布式工作负载——这些是 Python 独自难以应对的。

## **3. 没有垃圾回收的内存安全性**

*   C++ 传统上用于提高速度，但它也伴随着风险，例如段错误和内存泄漏。
*   Rust 在编译时通过零成本抽象保证内存安全——没有运行时开销，没有悬空指针，没有空指针解引用。
*   对于在生产环境中全天候运行的 AI 系统（例如云推理服务或边缘设备）来说，这种可靠性至关重要。

## **4. 生态系统协同效应**

Python 拥有成熟的 AI/ML 库，但 Rust 的生态系统在互补领域不断发展，包括：

*   Polars (DataFrames) 用于高性能数据处理。
*   Burn (Rust 中的深度学习框架)。
*   tch-rs (用于训练和推理的 LibTorch 绑定)。
*   许多 Rust 库开箱即用地提供 Python 绑定，让开发人员无需离开 Python 的舒适区即可集成它们。

## **5. 生产级 AI 服务**

*   训练通常在 Python 中完成。然而，大规模模型服务需要速度、稳定性和效率。
*   Rust 越来越多地用于构建推理服务器和 API（通过 Axum、Actix-web 或 gRPC）。
*   这使得团队可以将训练管道保留在 Python 中，同时部署精简、安全且快速的 Rust 支持的服务。

## **如何使用 PyO3 和 Maturin 将 Rust 集成到 Python 中**

有几种方法可以连接 Rust 和 Python（FFI、cffi、ctypes 等），但目前最方便开发人员的方法是使用：

*   [PyO3](https://github.com/PyO3/pyo3)，一个用于编写 Python 绑定的 Rust 库。
*   [Maturin](https://github.com/PyO3/maturin)，一个将 Rust 代码编译成 Python 包（wheels）的构建工具。

这种组合让您可以：

1.  [编写 Rust 代码](https://thenewstack.io/how-to-write-rust-code-like-a-rustacean/)。
2.  将其编译成 Python 模块。
3.  像任何普通的 Python 包一样，使用 `import my_rust_module` 导入它。

### **第一步：安装依赖项**

确保您已安装：

`curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh`

*   Python（推荐 ≥3.8）。
*   Maturin（通过 pip 安装）：

`pip install maturin`

### **第二步：创建一个新的 Rust 项目**

创建一个新的 Rust 库项目：

```
cargo new --lib rust_python_demo
cd rust_python_demo
```

接下来，更新 `Cargo.toml` 以包含 PyO3：

```
[package]
name = "rust_python_demo"
version = "0.1.0"
edition = "2021"

[lib]
name = "rust_python_demo"
crate-type = ["cdylib"]

[dependencies]
pyo3 = { version = "0.22", features = ["extension-module"] }
```

### **第三步：编写 Rust 代码（带 Python 绑定）**

打开 `src/lib.rs` 并替换其内容：

```
use pyo3::prelude::*;
use pyo3::wrap_pyfunction;

/// A simple function to add two numbers.
#[pyfunction]
fn add_numbers(a: i32, b: i32) -> i32 {
    a + b
}

/// A function that computes dot product of two vectors.
#[pyfunction]
fn dot_product(vec1: Vec<f64>, vec2: Vec<f64>) -> PyResult<f64> {
    if vec1.len() != vec2.len() {
        return Err(pyo3::exceptions::PyValueError::new_err(
            "Vectors must be of the same length",
        ));
    }
    Ok(vec1.iter().zip(vec2.iter()).map(|(x, y)| x * y).sum())
}

/// Define the Python module
#[pymodule]
fn rust_python_demo(_py: Python, m: &PyModule) -> PyResult<()> {
    m.add_function(wrap_pyfunction!(add_numbers, m)?)?;
    m.add_function(wrap_pyfunction!(dot_product, m)?)?;
    Ok(())
}
```

### **第四步：构建 Python 包**

在开发模式下运行 Maturin（以便您可以在本地导入）：

`maturin develop`

这将把 Rust 代码编译成一个 Python 模块 (`rust_python_demo`) 并将其安装到您当前的 Python 环境中。

### **第五步：在 Python 中使用**

现在，打开一个 Python shell 或脚本：

```
import rust_python_demo

print(rust_python_demo.add_numbers(5, 7))  
# Output: 12

print(rust_python_demo.dot_product([1.0, 2.0, 3.0], [4.0, 5.0, 6.0]))  
# Output: 32.0
```

它的工作原理与任何其他 Python 模块一样，但核心逻辑以 Rust 的速度运行。

**实际示例：Python AI 工作流中的 Rust 函数**

## **使用 Rust 进行快速数据预处理**

数据预处理通常是 ML 管道中的瓶颈。在 Python 中，要标准化数据集（将值缩放到 0 和 1 之间），可以使用循环或 NumPy 编写。以下是如何在 Rust 中实现它并从 Python 中调用它。

**Rust** (`src/lib.rs`)**：**

```
use pyo3::prelude::*;
use pyo3::wrap_pyfunction;

/// Normalize a list of floats between 0 and 1
#[pyfunction]
fn normalize(data: Vec<f64>) -> PyResult<Vec<f64>> {
    if data.is_empty() {
        return Ok(vec![]);
    }
    let min = data.iter().cloned().fold(f64::INFINITY, f64::min);
    let max = data.iter().cloned().fold(f64::NEG_INFINITY, f64::max);
    if (max - min).abs() < f64::EPSILON {
        return Ok(vec![0.0; data.len()]); // all values the same
    }
    Ok(data.iter().map(|x| (x - min) / (max - min)).collect())
}

#[pymodule]
fn rust_python_demo(_py: Python, m: &PyModule) -> PyResult<()> {
    m.add_function(wrap_pyfunction!(normalize, m)?)?;
    Ok(())
}
```

#### **Python：**

```
import rust_python_demo
import numpy as np

data = np.random.rand(1_000_000).tolist()

normalized = rust_python_demo.normalize(data)
print(f"First 5 normalized values: {normalized[:5]}")
```

对于大型数据集，Rust 版本比纯 Python 循环快得多。

## **真实世界案例研究**

这种混合方法已在生产中得到证实：

*   Hugging Face Tokenizers。
*   最初用 Python 编写，对于大规模自然语言处理 (NLP) 预处理来说太慢。
*   用 Rust 重写，并带有 Python 绑定。
*   实现了显著的加速。

Polars DataFrame

PyTorch + 自定义操作

*   研究人员用 C++ 实现自定义张量操作以提高性能。
*   Rust 绑定 (`tch-rs`) 为更安全、更现代的低级操作打开了新大门。

## **混合 AI 开发的未来**

我们正在看到一个清晰的趋势：

*   Python 仍然是研究、原型设计和编排的接口语言。
*   Rust 正在成为 AI 系统中用于数据处理、推理和部署的性能层。
*   Burn 和 Linfa 等新的 Rust 原生 ML 框架表明，Rust 最终可能会与 Python 库正面竞争。

在不久的将来，预计：

1.  更多由 Rust 支持的 Python 库（遵循 Hugging Face / Polars 模型）。
2.  Rust 在生产推理服务器中的使用增加，而训练仍留在 Python 中。
3.  AI 边缘设备和 WebAssembly 部署严重依赖 Rust 的可移植性和效率。

底线是：AI 依赖于 Python 的灵活性和庞大的库生态系统而蓬勃发展。但正如我们所见，Python 独自在性能瓶颈、并发限制和生产级系统的需求方面存在困难。这就是 Rust 成为完美伴侣的地方。

通过将 Rust 集成到 Python 工作流中：

*   您在保持 Python 表现力和生态系统的同时，获得了接近 C++ 的性能。
*   您通过 Rust 无畏的并发性克服了 GIL。
*   您部署了更安全、更可靠的 AI 服务，这些服务可以在不发生内存泄漏或运行时崩溃的情况下大规模运行。

这些实际示例——从数据标准化到点积基准测试——展示了使用 PyO3 和 maturin 将 Rust 函数公开为 Python 模块是多么容易。这些不仅仅是学术练习；它们反映了行业领导者已经采用的真实世界用例。Hugging Face、Polars 等公司正在证明混合的 Rust + Python 模型在现实世界中是可行的。

展望未来，我们可能会看到：

*   更多由 Rust 支持的 Python 库，它们使 Python 处于研究前沿，但悄悄地用极快的 Rust 实现取代了缓慢的 Python 核心。
*   Rust 在生产推理服务中得到越来越多的采用，特别是在边缘设备和实时 AI 领域。
*   Rust 原生 ML 框架逐渐兴起，它们有一天可能会与 TensorFlow 和 PyTorch 匹敌。

AI 开发的未来不是 Python *或* Rust。它是 Python 和 Rust 的结合，这种伙伴关系结合了两者的优点：Python 的易用性与 Rust 毫不妥协的性能和安全性。

对于开发人员和团队来说，信息很明确：您无需放弃 Python 来构建高性能 AI。相反，在最重要的领域——堆栈中性能关键、并行和安全敏感的层——拥抱 Rust。