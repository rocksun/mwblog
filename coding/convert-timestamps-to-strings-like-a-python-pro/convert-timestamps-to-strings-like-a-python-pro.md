
<!--
title: 像Python专家一样转换时间戳为字符串
cover: https://cdn.thenewstack.io/media/2025/07/91b41ba3-joshua-olsen-4xz_vih1x3m-unsplash-1.jpg
summary: 时间戳是机器可读的数字，而时间字符串是人类可读的日期和时间格式。Python的datetime模块可以将时间戳转换为时间字符串，并使用strftime()进行格式化。处理时区时，应先转换为UTC时间。
-->

时间戳是机器可读的数字，而时间字符串是人类可读的日期和时间格式。Python的datetime模块可以将时间戳转换为时间字符串，并使用strftime()进行格式化。处理时区时，应先转换为UTC时间。

> 译自：[Convert Timestamps To Strings Like a Python Pro](https://thenewstack.io/convert-timestamps-to-strings-like-a-python-pro/)
> 
> 作者：Jessica Wachtel

思考[时间戳与时间字符串](https://thenewstack.io/how-to-convert-a-timestamp-to-a-string-in-python/)的一个简单方法是，一个是为了机器可读，另一个是为了人类可读。计算机最擅长处理简单的数字表示，就像它们最终将一切处理为 0 和 1 一样。时间戳就像那样：一个干净、高效的数字，程序可以存储、排序和计算。

但人类需要上下文、文字、格式和图像才能理解世界。这就是[时间字符串](https://thenewstack.io/pythons-built-in-string-tools-every-developer-needs/)的用武之地。将时间戳转换为可读的日期和时间，可以将机器代码转换为我们可以一目了然地解释的内容。

这样想：

时间戳是为计算机准备的。时间字符串是为我们准备的。

## 理解 Python 时间戳

时间戳是一个浮点数或整数，表示自 [Unix](https://thenewstack.io/fosdem-24-can-the-unix-shell-be-improved-hell-yes/) 纪元以来经过的时间（以秒为单位计数）。什么？Unix 纪元发生在 1970 年 1 月 1 日。早在 Unix 设计者创建系统时，他们就需要一个固定的时间点来开始计数。他们还需要一个不会与重要的历史日期冲突，并且足够近以便在现代计算中开始计数的日期。

### 什么是时间戳？

自 Unix 纪元以来，每过去一秒，该数字就会 +1。1970 年 1 月 1 日 00:00:00 UTC 为 0。2000 年 1 月 1 日 00:00:00 为 946,684,800。2025 年 1 月 1 日 00:00:00 UTC 为 1,735,689,600，这意味着自 Unix 纪元以来已经过去了 1,735,689,600 秒。

### Python 中的时间戳示例

首先，我们需要导入 `time` 模块，因为这是 [Python](https://thenewstack.io/python/) 内置的用于处理日期、时间和时间戳的方法。我们可以使用 `time.time()` 来获取当前时间戳。

```py
import time


current_timestamp = time.time()
print("Current timestamp:", current_timestamp)
```

您将看到的输出是自 1970 年 1 月 1 日以来经过的确切秒数。

## 在 Python 中将时间戳转换为时间字符串

对于那些无法使用秒计数器引用时间的人，我们有 Python `datetime` 模块。`datetime` 模块将这些秒转换为我们可以理解的时间格式。

### 使用 `datetime` 模块

`datetime` 是一个内置的 Python 库，它提供了用于操作日期的类。通过使用 `datetime` 模块，我们可以使用相同的起始日期 1970 年 1 月 1 日，但将输出转换为日期（日历日期）、一天中的时间、执行时间算术、格式化和解析字符串，以及（正如我们上面所看到的）访问时间戳。

### `datetime.fromtimestamp()` 的语法

`fromtimestamp()` 是 `datetime` 类的类方法。它是您调用以从时间戳创建 `datetime` 对象的方法。

在下面的代码中，`timestamp` 是分配给从 `time.time()` 返回的数值的变量。该函数返回 `datetime` 对象。

```py
from datetime import datetime
import time


timestamp = time.time()


datetime_object = datetime.fromtimestamp(timestamp)


print("Current timestamp:", timestamp)
print("Corresponding datetime:", datetime_object)
```

### 使用 `datetime` 的转换示例

您不必每次都打印完整的 `datetime` 对象。这是一个打印较小信息块的示例。

```py
from datetime import datetime


timestamp = time.time()
datetime_object = datetime.fromtimestamp(timestamp)


print("Year:", datetime_object.year)
print("Month:", datetime_object.month)
print("Day:", datetime_object.day)
print("Hour:", datetime_object.hour)
print("Minute:", datetime_object.minute)
print("Second:", datetime_object.second)
```

## 在 Python 中格式化时间字符串

我们为什么需要时间字符串？提取 `datetime` 对象会为您提供比时间戳更易读的结果，但我们可以做得更好。格式化时间字符串允许您将时间自定义为在全球范围内更易读的方式（即，不同的国家/地区以不同的方式格式化时间，存在时区等）。

### 使用 `strftime()` 进行格式化

与 `fromtimestamp()` 类似，`strftime()` 是 `datetime` 类中的一个类方法。`strftime()` 允许您创建自定义的日期/时间字符串格式。

以下是一些格式化代码：

* `%Y` 是 4 位数的年份 (2025)
* `%m` 是零填充的月份 (06)
* `%d` 是月份中的日期 (01)
* `%H` 是 24 小时制的小时 (13)
* `%M` 是分钟 (23)
* `%S` 是秒 (16)

### 常见的时间字符串格式

```py
from datetime import datetime
import time


timestamp = time.time()
datetime_object = datetime.fromtimestamp(timestamp)


print(datetime_object.strftime("%Y-%m-%d"))
print(datetime_object.strftime("%d/%m/%Y %H:%M"))  
print(datetime_object.strftime("%I:%M %p")) 
```

## 替代方法

`datetime` 是将日期和时间引入应用程序的最常用方法。但这不是唯一的方法。Python 的 `time` 方法（我们一直在使用它来生成时间戳）也可以进行转换。

### 使用 `time` 模块

`time` 模块将时间戳转换为可读的结构，但被认为有点低级且不太灵活（稍后会详细介绍）。如果您只需要简单的格式或需要与旧的 Python 代码兼容，您会更喜欢使用 `time` 模块。

```py
import time


timestamp = time.time()
time_struct = time.localtime(timestamp)
time_string = time.strftime("%Y-%m-%d %H:%M:%S", time_struct)


print("Time string:", time_string)
```

### `datetime` 和 `time` 模块之间的比较

`datetime` 模块于 2003 年在 Python 2.3 中发布，晚于 `time` 模块。`time` 模块可以追溯到 20 世纪 90 年代。`time` 模块更简单但更有限，尤其是在日期算术或识别时区等方面。

`datetime` 带来了额外的功能，例如：

* 丰富的属性（`year`、`month` 等）
* `timedelta`，用于处理日期数学
* 更好的格式化和解析
* 更清晰的时区处理

`datetime` 没有取代 `time`（正如您所看到的，我们的编码示例中都使用了它），但 `datetime` 是显示日期和时间的推荐方式。

`time` 仍然是将时间戳作为浮点数获取的最快方法。您可以从 `datetime` 获取时间戳，但正如您所看到的，它需要更多的代码（因此 `time` = 更简单）：

```
from datetime import datetime
timestamp = datetime.now().timestamp()
```

## 处理时区

默认情况下，`datetime.fromtimestamp()` 使用运行代码的机器的本地时区。如果您在纽约的笔记本电脑上运行此代码，它将显示东部时间。在德国的服务器上运行相同的脚本将显示中欧时间。

### 使用统一时区

假设您想为应用程序的每个用户显示东部时间，无论他们身在何处。您可以使用 `pytz` 库来做到这一点。在使用它之前，请确保 `pip install pytz`。

### 转换为 UTC

在我们可以指定时区之前，我们需要将时间戳转换为 UTC。

```py
from datetime import datetime
import time


timestamp = time.time()


datetime_utc = datetime.utcfromtimestamp(timestamp)


print("UTC Time:", datetime_utc.strftime("%Y-%m-%d %I:%M %p %Z"))
```

在我们将时间戳转换为 UTC 后，我们可以使用 `pytz` 将 UTC 时间转换为东部时间。

```py
from datetime import datetime
import pytz
import time


timestamp = time.time()


# convert the timestamp to a UTC datetime object
datetime_utc = datetime.utcfromtimestamp(timestamp)


# define the US Eastern Time timezone
eastern = pytz.timezone('US/Eastern')


# localize the UTC datetime and convert to eastern time
datetime_eastern = pytz.utc.localize(datetime_utc).astimezone(eastern)


print("Eastern Time:", datetime_eastern.strftime("%Y-%m-%d %I:%M %p %Z"))
```

## 最佳实践和常见陷阱

很多内容已经根据我们在示例中实践的方式进行了介绍（即，在指定时区之前转换为 UTC）。其余的非常简单，并遵循通常的编码最佳实践，例如在使用新代码时使用 `datetime` 而不是 `time`。在整个项目中也使用一致的格式非常重要。

## 错误处理和故障排除

与最佳实践类似，在使用 `datetime` 和 `time` 时，错误处理和故障排除没有什么特别之处，只需确保变量名称正确，在进行转换时使用正确的类型，并在使用 `strftime()` 时小心使用格式化代码。

您也可以使用类似的错误处理：

```py
from datetime import datetime


try:
    timestamp = "not_a_timestamp"
    datetime_obj = datetime.fromtimestamp(float(timestamp))
except (TypeError, ValueError) as e:
    print("Error converting timestamp:", e)
```

## 结论

使用 Python 可以轻松地将时间戳转换为可读的日期。使用 `datetime` 模块，您可以快速将时间戳转换为 Python 开发人员信任的日期字符串。借助 `strftime()`，Python 时间戳格式化允许您自定义时间字符串。

将纪元时间转换为人类可读的日期很简单，而像 `pytz` 这样的工具可以帮助管理时区。掌握这些技术意味着可以自信地处理时间数据，从而使 Python datetime 时间戳到字符串的转换变得轻而易举。

开始转换，看看将 Unix 时间戳转换为清晰、可读的时间字符串有多么简单！