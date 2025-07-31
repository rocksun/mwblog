<!--
title: Python时间戳与时间字符串导论
cover: https://cdn.thenewstack.io/media/2025/07/e2a92eea-chris-santi-svaadidohu0-unsplash.jpg
summary: 时间戳是自Unix纪元以来的秒数，时间字符串是时间的字符表示。Python的datetime模块可将时间戳转换为时间字符串，并格式化时间。time模块提供时间相关功能，tzinfo函数处理时区转换。
-->

时间戳是自Unix纪元以来的秒数，时间字符串是时间的字符表示。Python的datetime模块可将时间戳转换为时间字符串，并格式化时间。time模块提供时间相关功能，tzinfo函数处理时区转换。

> 译自：[Python: Introduction to Timestamps and Time Strings](https://thenewstack.io/python-introduction-to-timestamps-and-time-strings/)
> 
> 作者：Jack Wallen

一个时间戳可以被认为是一个数值记录，它精确地[捕捉](https://thenewstack.io/convert-timestamps-to-strings-like-a-python-pro/)了某事发生的时间。这些时间戳以自1970年1月1日Unix纪元以来的累积秒数存储。该日期之后的所有内容都根据从起点开始经过的秒数来计算。例如，2025年7月23日将是1753280905 —— 因为这是自纪元以来经过的秒数。

另一方面，时间字符串是代表时间点的字符集合，例如“2025年7月23日”。

这两者截然不同。

## 使用Python将时间戳转换为时间字符串

大多数人很难知道或计算时间戳。因此，在你的[Python脚本或应用程序](https://thenewstack.io/native-python-tutorial/)中使用时间戳会非常具有挑战性。最重要的是，由于时间戳的长度和复杂性，硬编码时间戳并不是一个好的编码实践。

幸运的是，[Python](https://thenewstack.io/decode-any-python-code-with-this-5-step-method/)内置了将时间戳转换为时间字符串的能力，而无需你先计算当前时间戳。这是通过[datetime模块](https://docs.python.org/3/library/datetime.html)完成的。

datetime模块为你计算当前时间戳，其使用方式如下：

```py
import datetime

current_timestamp = datetime.datetime.now()
print(current_timestamp)
```

使用 `datetime.datetime.now()`，Python会自动计算时间戳，然后自动将其转换为时间字符串。例如，刚才运行的输出打印：

```py
2025-07-23 10:39:23.952357
```

你不必坚持上述格式，因为Python允许你随意格式化时间。这是通过 `strtime()` 函数实现的，并使用 `%Y`、`%m`、`%d`、`%H` 和 `%D` 来实现格式化。

这是一个格式化时间字符串的示例。假设你希望输出包括月、日、年、小时和分钟（这将是 `%m-%d-%Y %H:%M`）。Python代码如下所示：

```py
from datetime import datetime

timestamp = datetime.now()
formatted_string = timestamp.strftime('%m-%d-%Y %H:%M')
print(formatted_string)
```

## datetime.fromtimestamp() 的语法

还有另一种转换时间的方法，它接受一个时间戳，将其转换为一个datetime对象，然后存储Python的日期时间信息。

其语法如下所示：

```py
from datetime import datetime

timestamp = int(your_timestamp_value)
dt_object = datetime.fromtimestamp(timestamp)
```

以下是对上述代码的解释：

*   **`datetime`**: 这是导入处理日期和时间所需的类[Python的内置库](https://thenewstack.io/5-python-libraries-every-data-engineer-should-know/)的函数。
*   **`int(your_timestamp_value)`**: 将任何占位符替换为实际的时间数据。这可以是表示时间的字符串（例如，“2025-07-23”）或时间戳数组。
*   **`datetime.fromtimestamp(timestamp)`**: 这会将数字转换为datetime对象，从而为你提供时间的精确表示。

你可以将 `datetime.fromtimestamp()` 与时间戳一起使用。当然，要做到这一点，你必须知道确切的时间戳。

假设我们使用2025年7月23日的时间戳，即1753280905。我们如何将它与 `timestamp()` 一起使用？像这样：

```py
import datetime

timestamp = int(1700845200)
dt_object = datetime.fromtimestamp(timestamp)
print("Timestamp:", dt_object, "Type:", type(dt_object))
```

使用 `datetime.fromtimestamp()` 的主要好处是，它可以无缝地创建时间戳的结构化表示，以便可以在你的Python代码块中使用它们。

## 使用Python Time模块

time模块提供了处理Python中与时间相关[函数](https://thenewstack.io/so-much-more-python-for-beginners-functions/)的必要工具。使用time模块，你可以轻松地获取当前的系统时间，如下所示：

```py
import time

current_time = time.time()
print(f"Current Time: {current_time}")
```

上述代码的输出将是当前的Unix Epoch，例如：

```py
1753283419.3007143
```

还有 `sleep()` 函数，它允许在代码中添加暂停。你可能希望在Python脚本中添加暂停，以便进程以特定的间隔执行，或者在执行时间敏感的操作时执行。以下是 `sleep()` 函数的示例：

```py
import time

print("Waiting for 5 seconds...")
time.sleep(5)
```

上面的脚本将打印“Waiting for 5 seconds…”，暂停，然后返回你的提示符。或者，你可以添加以下内容：

```py
import time  # Import 'time' module
print("Waiting for 5 seconds...")
time.sleep(5)

print("Five seconds have passed.")
```

这将打印“Waiting for five seconds…”，暂停五秒钟，然后打印“Five seconds have passed.”

## 处理时区

时区为你的代码增加了另一层复杂性。在处理跨越不同区域设置的数据时，你需要管理时区。否则，时间可能不正确，具体取决于代码的运行位置。

使用Python datetime模块，可以使用 `tzinfo` 函数，该函数允许你使用时区。这是一个例子：

```py
import datetime

from datetime import timezone
now = datetime.datetime.now(timezone.utc)
print(f"Current Time (UTC): {now}")
```

运行上面的代码，结果如下所示：

```py
Current Time (UTC): 2025-07-23 15:18:54.854103+00:00
```

你也可以从一个时区转换为另一个时区，如下所示：

```py
import datetime

import pytz

dt = datetime.datetime(2025, 07, 23, 11, 39, 30)
tz = pytz.timezone('America/New_York')
dt = tz.localize(dt)

new_tz = pytz.timezone('America/Los_Angeles')

converted = dt.astimezone(new_tz)

print(converted)
```

上述代码的输出将是（在当前时间运行）：

```py
2025-07-23 08:39:30-07:00
```

这就是你如何从Python时间戳和时间字符串开始的。