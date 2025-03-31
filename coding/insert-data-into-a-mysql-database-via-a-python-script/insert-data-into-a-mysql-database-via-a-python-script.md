<!--
title: 通过 Python 脚本将数据插入 MySQL 数据库
cover: https://cdn.thenewstack.io/media/2021/11/ab06a958-pythonlogo.png
summary: Python脚本轻松搞定MySQL数据插入！告别手动，用mysql-connector-python库，几行代码实现数据库交互。更有input()函数加持，用户自定义数据，灵活高效！连接池、超时设置、错误排查，常见问题一网打尽。sqlalchemy、pymysql等多种连接方式等你探索！
-->

Python脚本轻松搞定MySQL数据插入！告别手动，用`mysql-connector-python`库，几行代码实现数据库交互。更有`input()`函数加持，用户自定义数据，灵活高效！连接池、超时设置、错误排查，常见问题一网打尽。`sqlalchemy`、`pymysql`等多种连接方式等你探索！

> 译自：[Insert Data into a MySQL Database via a Python Script](https://thenewstack.io/insert-data-into-a-mysql-database-via-a-python-script/)
> 
> 作者：Jack Wallen

我想向你展示 [Python](https://thenewstack.io/what-is-python/) 可以做的一件非常酷的事情：将数据插入 MySQL 数据库表。

想象一下，能够将数据注入到表中，而无需先登录到 MySQL 控制台——并且从 Python 应用程序中注入数据可能非常灵活和方便。更棒的是，这并不是一个很大的挑战。

让我告诉你它是如何完成的。

## 你需要什么

我将在 Ubuntu Server 22.04.3 的实例上演示这一点。如果你使用的是不同的 Linux 发行版（或者你使用的是 MacOS 或 Windows），你必须更改安装命令。 也就是说，你需要一个支持 Python3 的操作系统和一个具有 *sudo* 权限的用户。

而且，为了好玩，我将向你展示如何安装 MySQL 并创建一个用户和数据库。

太棒了。让我们创造一些 Python/数据库的魔法。

## 安装 MySQL 和 Python

我们要做的第一件事是安装 MySQL 数据库服务器。为此，请登录到你的 Ubuntu Server 实例并准备安装。

```bash
sudo apt-get install mysql-server -y
```

完成后，你需要启用该服务，以便它在启动时运行。为此，请发出以下命令：

```bash
sudo systemctl enable --now mysql
```

### 安装 Python MySQL 连接器

在继续之前，你还必须安装 Python3 MySQL 连接器，它允许 Python 与你的 MySQL 数据库交互。这可以通过以下命令完成：

```bash
sudo apt-get install python3-mysql.connector -y
```

如果你的 Ubuntu 实例尚未安装 Python，你可以使用以下命令进行安装：

```bash
sudo apt-get install python3 -y
```

这就是安装的全部内容。

## 在 MySQL 中创建数据库和用户

### 创建一个 MySQL 数据库

接下来，我们需要创建一个数据库。使用以下命令登录到 MySQL 控制台：

```bash
sudo mysql
```

进入后，使用以下命令创建一个名为“staff”的数据库：

```sql
CREATE DATABASE staff;
```

### 创建一个 MySQL 用户

现在，我们可以创建一个用户（我们将其命名为“jack”），并授予该用户使用新数据库的权限。使用以下命令创建用户：

```sql
CREATE USER 'jack'@'localhost' IDENTIFIED BY 'PASSWORD';
```

确保 PASSWORD 是一个强而唯一的密码。
使用以下命令授予该用户访问我们的 staff 数据库的权限：

```sql
GRANT ALL PRIVILEGES ON staff.* TO 'jack'@'localhost';
```

## 创建一个表

我们现在必须创建一个表。首先，使用以下命令切换到 staff 数据库：

```sql
USE staff;
```

现在，我们可以在我们的新数据库上创建一个表。让我们保持简单，创建一个名为“editorial”的表，其中包含两列（name 和 email）。该命令将是：

```sql
CREATE TABLE editorial (id INT, name VARCHAR(30), email VARCHAR(30));
```

我们现在有一个数据库、一个用户和一个准备好操作的表。

**创建 Python 应用程序**

这就是乐趣开始的地方。我们将创建一个 Python 应用程序，将数据注入到 editorial 列的 name 和 email 列中。

使用以下命令创建脚本：

```bash
nano insert.py
```

在该文件中，粘贴以下内容：

```python
import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="jack",
  password="PASSWORD",
  database="staff"
)

mycursor = mydb.cursor()

sql = "INSERT INTO editorial (name, email) VALUES (%s, %s)"
val = ("NAME", "EMAIL")

mycursor.execute(sql, val)

mydb.commit()

print(mycursor.rowcount, "record inserted.")
```

PASSWORD 是你为 MySQL 用户 jack 创建的密码，NAME 是你要插入到 name 列中的名称，EMAIL 是你要插入到 email 列中的地址。

以下是更多解释：

- 第一行导入所需的函数，该函数允许 Python 连接到 MySQL。
- mydb 部分配置数据库的信息。
- mydb.cursor() 是允许将数据插入数据库的函数。
- sql 行是我们的第一个 MySQL 查询。
- val 行定义数据库的列。
- mycursor.execute 执行上述操作。
- mydb.commit() 确认 mycursor.execute 所做的更改。
- print 行打印输出以指示成功或失败。

使用 Ctrl+X 组合键保存并关闭文件。

**运行应用程序**

我们现在可以运行新的 Python 应用程序，该应用程序会将数据注入到你在脚本中指定的表中。此运行命令将是：

```bash
python3 insert.py
```

你应该收到注入成功的确认。你可以使用以下命令验证这一点：

```sql
SELECT * FROM editorial;
```

你应该看到你的第一个数据已添加到表中。

## 接受来自用户的输入
将数据注入数据库的这种方法效率不高，因为您每次都必须编辑脚本。幸运的是，我们可以使用 Python 中的变量来接受将被插入的输入。

为此，我们必须使用 `input()` 函数，该函数允许脚本接受来自用户的输入。我们的新脚本如下所示：

```python
import mysql.connector

name = input("Type a name: ")
email = input("Type an email: ")

mydb = mysql.connector.connect(
  host="localhost",
  user="jack",
  password="PASSWORD",
  database="staff"
)

mycursor = mydb.cursor()
sql = "INSERT INTO editorial (name, email) VALUES (%s, %s)"
val = (name, email)
mycursor.execute(sql, val)
mydb.commit()
```

`PASSWORD` 是您为 MySQL 用户设置的密码。
保存并关闭文件。以相同的方式运行应用程序，只是这次系统会提示您输入姓名，然后输入电子邮件。

这就是您可以使用 Python 将数据注入 MySQL 表的方式。尝试一下，看看你能多有创意。

## Python/MySQL 连接常见问题解答

**问：使用 Python 连接到 MySQL 数据库的最常见方法是什么？**

答：最常见的方法是使用 `mysql-connector-python` 库，它提供了一个简单高效的接口来与 MySQL 数据库交互。

**问：如何在我的 Python 环境中安装 `mysql-connector-python` 库？**

答：您可以通过 pip 使用命令 `pip install mysql-connector-python` 安装它，或者像这样使用 conda `conda install -c anaconda mysql-connector-python`.

**问：什么是 MySQL 连接池，以及如何设置一个？**

答：连接池是一种允许多个连接在应用程序之间共享的机制。Python 中用于此目的的最流行的库是 `mysql-connection-pooling`。

**问：有哪些常见的 MySQL 连接错误，以及如何排除这些错误？**

答：常见的连接错误包括：

- `mysql-connector-python.errors.Error`：常规数据库错误消息。
- `mysql.connector.exceptions.OperationalError`：连接问题（例如，超时）。
- `mysql.connector.exceptions.ProgrammingError`：语法或 SQL 相关错误。

要排除这些错误，请检查您的 MySQL 配置文件（`my.cnf` 等），确保提供了正确的用户名和密码，并验证数据库连接详细信息是否准确。


**问：我可以使用其他库来连接到 Python 中的 MySQL 数据库吗？**

答：是的。一些流行的替代方案包括：

- `sqlalchemy`：一个用于处理 SQL 数据库的 ORM 库。
- `pymysql`：另一个连接器库，提供与 `mysql-connector-python` 类似的功能。
- `PyMySQL` (no module)：与上面的类似。

**问：什么是 MySQL 中的连接超时，以及如何调整它？**

答：连接超时是允许连接尝试成功的时间段。默认情况下，可以通过配置文件（`my.cnf` 等）调整此值。