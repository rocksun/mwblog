
<!--
title: 在 Python 中如何处理日期和时间
cover: https://cdn.thenewstack.io/media/2024/09/d8198a9e-fabian-albert-vjlpdzvlz-u-unsplash.jpg
-->

本教程向 Python 开发人员展示如何使用 `datetime` 模块轻松访问系统时钟。

> 译自 [How To Work With Date and Time in Python](https://thenewstack.io/how-to-work-with-date-and-time-in-python/)，作者 Jessica Wachtel。

我们希望我们的应用程序和服务始终按时运行。自动化、[数据收集](https://thenewstack.io/why-its-time-to-decouple-data-collection-from-monitoring-analytics/)、调度、安全和 [物联网集成](https://thenewstack.io/building-an-iot-weather-station-with-micropython-or-arduino/) 等任务，如果没有精确计时带来的信心，将完全不同。如果每个开发人员都根据自己的手表构建应用程序和函数，世界将完全不同。幸运的是，我们有系统时钟，它为所有编程语言和硬件提供了一个通用参考。在 [Python](https://thenewstack.io/python-mulls-a-change-in-version-numbering/) 中，您可以使用 `datetime` 模块轻松访问此时钟。

`datetime` 模块引用系统时钟。系统时钟是计算机中跟踪当前时间的硬件组件。它计算自称为“纪元”的固定点以来的秒数，在大多数系统上，纪元是 1970 年 1 月 1 日。

操作系统提供了一个接口，供应用程序通过系统调用或 [API](https://thenewstack.io/api-management/) 访问系统时钟。这些系统调用和 API 返回当前日期和时间。此时间的准确性和精度取决于硬件和操作系统的计时机制，但它们都始于同一个地方。

Python 的时间接口是 `datetime` 模块。它调用系统 API 来检索当前日期和时间。

## `datetime` 如何工作？

首先要使用日期和时间，您需要导入 `datetime` 模块。该模块会将 `datetime` 对象的所有方法和属性导入您的应用程序。使用 `datetime` 对象将遵循面向对象编程语法。

```py
from datetime import datetime
```

要获取当前日期和时间，可以使用 `datetime.now()` 方法。它将返回包含当前日期和时间的完整 `datetime` 对象，精确到纳秒。

```py
datetime_now = datetime.datetime.now()
print("Current date and time:", datetime_now)
```

格式为：2024-07-30 08:59:46.989846

如果您只需要日期或只需要时间，也可以将其拆分。调用以下两种方法将从 `datetime` 对象中提取更有限的信息。

要打印今天的日期，请使用 `date.today()` 方法：

```py
date_today = datetime.date.today()
print("Today's date:", date_today)
```

要仅为您的应用程序提取当前时间，您需要从 `datetime` 对象中提取时间。

```py
time_now = datetime.now().time()
print("Current time:", time_now)
```


## 格式化

您可以使用 `strftime()` 方法将日期和时间重新格式化为字符串。这允许您使用格式代码指定您喜欢的格式。以下是一个常见的格式代码：

– `%Y` 更新年份

以下代码将指定时间更新为零填充的十进制数（例如，01）：

– `%m` 更新月份
– `%d` 更新日期
– `%H` 更新 24 小时制
– `%M` 更新分钟
– `%S` 更新秒

使用这些格式代码的完整代码块可能如下所示：

```py
date_formatted = time_now.strftime("%Y-%m-%d")
time_formatted = time_now.strftime("%H:%M:%S")
print("Formatted date:", date_formatted) 
print("Formatted time:", time_formatted)
```

## 使用时区

您可以使用 `pytz` 库调整 `datetime` 对象以反映不同的时区。在使用它之前，您需要导入它：

```py
import pytz
```

您不需要先获取 UTC 时间，但这是最佳实践，因为 UTC 从不改变（包括在夏令时期间），因此它是一个强大的参考点。

```py
# Get the current time in UTC
utc_time = datetime.now(pytz.utc)
print("UTC:", utc_time)

# Define the  timezone
local_tz = pytz.timezone('America/New_York')

# Convert the UTC time to the timezone
local_time = utc_time.astimezone(local_tz)
print("New York:", local_time)
```

Python 的 `datetime` 模块保存了日期！


`datetime` 模块简化了在 Python 中使用计时。它消除了与同步应用程序相关的许多复杂性，并确保它们以准确一致的计时运行。
