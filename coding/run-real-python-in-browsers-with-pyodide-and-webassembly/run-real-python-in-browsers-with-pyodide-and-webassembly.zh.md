有许多方法可以将 [Python](https://thenewstack.io/what-is-python/) 带到浏览器（感谢 [WebAssembly](https://thenewstack.io/webassembly/webassembly-when-you-hate-rust-but-love-python/)）。但只有一种方法能将 Python 的全部功能（真正不打折扣）带到浏览器：[Pyodide](https://pyodide.com/)。Pyodide 是一个编译到 WebAssembly 的完整 Python 运行时，它允许你直接在浏览器中运行标准 Python 代码。是的，存在其他工具，但其功能比 Pyodide 更受限制。

Pyodide 之所以强大，是因为它是 [CPython](https://thenewstack.io/guido-van-rossums-ambitious-plans-for-improving-python-performance/) 解释器到 WebAssembly (Wasm) 的一个移植。Pyodide 采用标准的 CPython 引擎，并对其进行重新工程，使其能在浏览器的 WebAssembly 沙箱内运行。这使得浏览器能够高速执行复杂的、真实的 Python 库，而无需任何外部服务器或本地安装。这意味着，与较小的 Python 变体或转译方法不同，使用 Pyodide 时，你可以：

*   在浏览器中运行完整的 Python。
*   在客户端支持 Pandas、NumPy 和 Matplotlib 等 C 扩展库。
*   完全在客户端运行 Python，无需任何后端。
*   在客户端动态执行 Python。

而使用其他专注于 Python 的 Wasm 工具，你则无法做到。一个小的技术澄清：[PyScript](https://thenewstack.io/how-to-use-pyscript-to-create-python-web-apps/) 将相同的功能带到浏览器。PyScript 是一个使用 Pyodide 作为其后端的框架。它为 Pyodide 运行时添加了一个 HTML/模板层。

Pyodide 的美妙之处在于它不需要复杂的构建系统或专门的环境。如果你能编写一个标准的 HTML 文件，你就能运行 Pyodide。

*   **零安装：** 你无需安装 Python、管理虚拟环境或通过 pip 安装任何东西。一切都在你加载页面时直接在浏览器中发生。
*   **最少设置：** 你可以通过 CDN 链接将 Pyodide 引入你的项目。加载后，只需一个函数调用即可执行 Python 逻辑：`pyodide.runPython()`。
*   **直接通信：** Pyodide 包含一个强大的 Python 和 JavaScript 之间的桥梁。你可以在两种语言之间无缝传递数据结构——例如，使用 JavaScript 获取数据，并使用专门的库通过 Python 进行分析。

Pyodide 是一个全功能的运行时。它直接在你的设备上下载并执行整个 CPython 引擎，而不是使用“精简版”或将代码发送到服务器进行处理。这使其成为隐私优先的数据工具、分析、数据处理和离线应用程序等应用的可靠选择。

为了向你展示如何开始使用 Pyodide，我们将构建一个应用程序，它：

*   使用 Pyodide 在浏览器中加载 Python 和 Pandas。
*   接受上传的 CSV 文件。
*   使用 Python 来：
    *   显示数据集的前几行。
    *   填充列选择器。
    *   生成摘要统计信息。

所有这些都发生在客户端！

我认为重要的是要说明，你不需要在你的机器上安装任何项目特定的工具或库就能成功完成本教程。你只需要以下内容：

*   现代浏览器
*   互联网连接
*   文本编辑器或 IDE
*   CSV 文件（仅当你希望看到项目的所有功能时才需要）

因为我们是在浏览器中工作，所以项目代码包括 HTML、CSS 和 JavaScript，以及我们的 Pyodide 和 Python 代码。我们所有的代码都将位于一个文件中，即 `index.html`。我将首先分享完整的代码文件，然后提供 Pyodide 部分的详细解释及其工作原理（HTML、CSS 和 [JavaScript](https://thenewstack.io/introduction-to-javascript/) 不在本教程的范围之内）。

`index.html`

## 使用 Pyodide

我们第一次在 `index.html` 中遇到 Pyodide 是下面这行代码：

```html
<script src="https://cdn.jsdelivr.net/pyodide/v0.25.0/full/pyodide.js"></script>
```

上述代码下载了 Python 的 Wasm 版本。它还在浏览器标签页中安装了一个 Python 解释器。最后，它暴露了一个与解释器交互的 JavaScript API (`loadPyodide`)。

没有这行代码，你就无法在浏览器中执行 Python。

### Pyodide 启动 Python 并安装 Python 包

接下来我们需要 Pyodide 做的是初始化 Python 解释器、创建 Python 执行环境，并下载/安装编译好的 [Python 包](https://thenewstack.io/the-top-5-python-packages-and-what-they-do "Python 包")到该环境中。下面的代码实质上取代了 `python -m venv`、`pip install pandas` 以及运行 Pandas 所需的任何后端服务。可以将其视为在浏览器中加载 Python。

```html
<script type="text/javascript">
  async function main() {
    // Initialize Pyodide
    let pyodide = await loadPyodide();
    console.log('Pyodide loaded successfully.');

    // Load Pandas and other packages
    await pyodide.loadPackage(["pandas", "micropip"]);
    console.log('Pandas and micropip loaded.');
    return pyodide;
  }

  let pyodideReadyPromise = main();
</script>
```

### Pyodide 连接 JavaScript 和 Python 内存

现在我们需要 JavaScript 像函数一样调用 Python。如果没有 Pyodide，你将需要 API 请求、后端端点或其他变通方法。这就是 Pyodide 使 JavaScript 和 Python 互操作的地方。

在下面的代码中，Pyodide 将一个 JavaScript 字符串复制到 Python 的全局命名空间中。这使得浏览器数据无需使用序列化 API 或通过 HTTP 发送即可供 Python 使用。

```javascript
// JavaScript function to handle CSV upload and pass data to Python
async function handleFileUpload(event) {
  const file = event.target.files[0];
  if (!file) {
    console.log("No file selected.");
    return;
  }
  const reader = new FileReader();
  reader.onload = async function(e) {
    const csvData = e.target.result;
    const pyodide = await pyodideReadyPromise;
    // Make CSV data available in Python
    pyodide.globals.set("csv_data", csvData);
    console.log("CSV data transferred to Python.");
    await pyodide.runPythonAsync(`
      import pandas as pd
      import io
      from js import document, csv_data

      # Read CSV data into a Pandas DataFrame
      df = pd.read_csv(io.StringIO(csv_data))
      print("DataFrame loaded successfully.")

      # Display first few rows
      head_html = df.head().to_html()
      document.getElementById("output-head").innerHTML = head_html
      print("Head displayed.")

      # Populate column selector
      column_select = document.getElementById("column-selector")
      column_select.innerHTML = '<option value="">Select a column</option>' # Clear previous options
      for col in df.columns:
          option = document.createElement("option")
          option.value = col
          option.text = col
          column_select.appendChild(option)
      print("Column selector populated.")

      # Generate and display summary statistics
      summary_html = df.describe().to_html()
      document.getElementById("output-summary").innerHTML = summary_html
      print("Summary statistics displayed.")
    `);
    console.log("Python script executed with CSV data.");
  };
  reader.readAsText(file);
}

// Attach event listener
document.addEventListener('DOMContentLoaded', (event) => {
  document.getElementById('csv-upload').addEventListener('change', handleFileUpload);
});
```

### 执行 Python 代码

`pyodide.runPython()` 在浏览器中执行 Python 代码。它将 Python 代码作为字符串接收，在执行之间维护 Python 状态，并允许多次 Python 调用共享变量和数据。该字符串由标准 Python 代码组成，而非 Python/JavaScript 混合代码。

下面的代码是将 CSV 读取到 Pandas DataFrame 中，显示前几行，动态填充列下拉菜单并计算摘要统计信息。Pyodide 允许 Python 访问浏览器 DOM，因此所有更新都将直接在页面上发生，无需任何服务器或 API 调用。

```python
import pandas as pd
import io
from js import document, csv_data

# Read CSV data into a Pandas DataFrame
df = pd.read_csv(io.StringIO(csv_data))
print("DataFrame loaded successfully.")

# Display first few rows
head_html = df.head().to_html()
document.getElementById("output-head").innerHTML = head_html
print("Head displayed.")

# Populate column selector
column_select = document.getElementById("column-selector")
column_select.innerHTML = '<option value="">Select a column</option>' # Clear previous options
for col in df.columns:
    option = document.createElement("option")
    option.value = col
    option.text = col
    column_select.appendChild(option)
print("Column selector populated.")

# Generate and display summary statistics
summary_html = df.describe().to_html()
document.getElementById("output-summary").innerHTML = summary_html
print("Summary statistics displayed.")
```

下一个代码块，同样使用 `pyodide.runPython()`，每当用户从下拉菜单中选择一列时，通过 Pyodide 运行 Python。它检查是否选择了列，然后从 DataFrame 中提取该列并在浏览器中显示前几个值。如果没有选择列，它会清除输出。Pyodide 允许 Python 直接更新 HTML，因此用户无需任何服务器请求即可即时看到列数据。

```javascript
async function handleColumnSelection() {
  const pyodide = await pyodideReadyPromise;
  const selectedColumn = document.getElementById("column-selector").value;

  if (selectedColumn) {
    pyodide.globals.set("selected_column", selectedColumn);
    await pyodide.runPythonAsync(`
      from js import document, selected_column
      import pandas as pd # Re-import or ensure df is globally accessible if needed

      # Assuming 'df' is available from the previous run or re-read
      # For simplicity, if df is not globally accessible, you might need to re-read csv_data here
      # For this example, let's assume df is still in Pyodide's scope.
      # A more robust solution might involve storing df in Python's global scope explicitly or returning it from initial load.

      if 'df' in globals():
          column_data = df[selected_column].head().to_html()
          document.getElementById("output-column-data").innerHTML = f"<h3>First 5 rows of '{selected_column}'</h3>{column_data}"
      else:
          document.getElementById("output-column-data").innerHTML = "<p>Error: DataFrame not found in Python scope. Please upload CSV again.</p>"
    `);
  } else {
    document.getElementById("output-column-data").innerHTML = ""; // Clear output if no column is selected
  }
}
// Attach event listener for column selector
document.addEventListener('DOMContentLoaded', (event) => {
    document.getElementById('column-selector').addEventListener('change', handleColumnSelection);
});
```

在两个代码块中都出现的一行重要代码是 `from js import document`。这使得 JavaScript 对象在 Python 中可访问，并允许 Python 直接调用浏览器 API。有了这行代码，Python 可以像一流语言一样与浏览器交互，更新 DOM 并响应操作，而无需任何服务器代码。

### Pyodide 帮助 Python 驱动 UI

Python 字符串中还有一段代码我想指出：

```python
document.getElementById("output-head").innerHTML = head_html
```

这段代码在不切换语言的情况下更新了 UI。它通过将 Python 调用路由到 JavaScript DOM 方法并将 Python 字符串转换为 JavaScript 字符串来实现这一点。

## 结论

Pyodide 彻底改变了传统的前端架构！它在浏览器中嵌入了一个持久的 Python 运行时，并提供了 JavaScript 和 Python 之间的双向桥梁。通过 Pyodide，像 Pandas 这样的 Python 库可以在客户端运行并直接与 DOM 交互。它将以前需要完整 Python 后端的功能直接带到了客户端。你会用 Pyodide 在浏览器中构建什么呢？