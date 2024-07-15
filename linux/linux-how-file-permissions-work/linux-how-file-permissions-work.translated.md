# Linux：文件权限工作原理

![关于 Linux：文件权限工作原理的特色图片](https://cdn.thenewstack.io/media/2024/07/0984e8d2-getty-images-2wamii-zo8o-unsplash-1024x682.jpg)

[Linux：Linux 技能模块库的配套实验室](https://thenewstack.io/tns-linux-sb00-2-companion-lab-for-linux-skill-blocks-repository/)文章。在本系列文章中，我们还介绍了
[如何选择发行版](https://thenewstack.io/choosing-a-linux-distribution/)、Linux 内核
[如何与硬件交互](https://thenewstack.io/linux-how-the-kernel-interacts-with-hardware/)以及如何
[Linux 管理系统服务](https://thenewstack.io/linux-skills-manage-system-services/)、
[存储](https://thenewstack.io/how-to-manage-linux-storage/)和
[用户和组权限](https://thenewstack.io/linux-user-and-group-management/)。
权限控制用户对文件和目录的访问。例如，权限决定用户是否可以读取文件 sales.txt。它们还决定用户是否可以编辑或更改该文件的内容。权限还指定用户是否可以运行程序或脚本。

如果您已经熟悉 Windows 权限，您会发现 [Linux](https://thenewstack.io/linux/) 权限要简单得多。

本文介绍了标准 Linux 权限可用的身份和访问级别，解释了绝对模式与符号模式，并展示了 [chmod](https://linux.die.net/man/3/chmod) 和 [chown](https://linux.die.net/man/3/chown) 命令的语法。

我将从一个简短的命令参考部分开始，演示如何创建一些用户、组、文件和目录，您可以在设置权限时使用它们。

查看我之前的帖子，“[了解 Linux 命令行](https://thenewstack.io/tns-linux-sb00-3-understand-the-linux-command-line/)”，以更好地使用这些命令。

## 设置用户和资源

创建一些用户帐户，以便您可以使用以下示例为不同的人设置不同的权限：

1 |
$ sudo useradd fsmith |
![](https://cdn.thenewstack.io/media/2024/03/632e2155-useradd-fsmith.png)

使用相同的方法创建 slee 和 mgarcia。

注意：以 root（管理员）用户身份登录 Linux 系统是一种糟糕的 [安全实践](https://thenewstack.io/lynis-run-a-security-audit-on-linux-for-free/)。大多数系统强制您以普通用户身份登录，然后使用 [sudo](https://linux.die.net/man/8/sudo)（超级用户执行）命令提升您的权限。使用 sudo 时，系统可能会提示您输入密码。

查看用户管理命令：

命令 |
描述 |
useradd 用户名 | 创建新用户。 |
usermod 用户名 | 修改现有用户。 |
userdel 用户名 | 删除现有用户。 |

也创建一些组。以下是一个示例：

1 |
$ sudo groupadd IT |

创建
HR 和
PR 组，使用相同的语法。

查看组管理命令：

命令 |
描述 |
groupadd 组名 | 创建新组。 |
groupmod 组名 | 修改现有组。 |
groupdel 组名 | 删除现有组。 |

您可以在我最近的 [Linux 用户和组文章](https://thenewstack.io/linux-user-and-group-management/) 中找到更多详细信息。

现在您已经拥有了一些用户和组，请创建一些资源，以便您可以使用权限控制对它们的访问。

切换到 /home/fsmith 主目录。使用 mkdir 命令创建以下目录：

- departments
- departments/it_dept
- departments/hr_dept
- departments/pr_dept
![](https://cdn.thenewstack.io/media/2024/03/c100e35a-ls-depts-dirs.png)

这些代表您管理 Linux 服务器的模拟公司中的三个部门。

使用 touch 命令在指定目录中创建这些文件：

- 在 it_dept 目录中，创建 password-reset.txt
- 在 hr_dept 目录中，创建 policies.txt
- 在 pr_dept 目录中，创建 press-releases.txt

在 [此处](https://thenewstack.io/primer-get-to-know-linux-files-and-directories/) 找到有关 [管理 Linux 文件和目录的更多信息](https://thenewstack.io/primer-get-to-know-linux-files-and-directories/)。

用户、文件和权限都是单个较大主题的一部分：[访问控制](https://thenewstack.io/role-based-access-control-five-common-authorization-patterns/)。用户帐户是身份，文件是资源。权限根据身份控制对资源的访问。例如，权限控制 fsmith 是否可以读取
fileA.txt 和
slee 是否可以更改
fileB.txt 的内容。

您可能会认为用户和组管理、文件管理和文件权限教程的内容是一个相关的主题集合——控制对文件的访问。

## 了解权限和身份

设置权限需要您了解可用的访问级别并管理这些访问级别适用于谁。本节介绍管理 Linux 权限所需的权限和身份。

### 了解访问级别

Linux 权限提供三种访问级别：读、写和执行。它们的行为在应用于文件或目录时略有不同。

下表解释了读、写和执行权限在应用于文件时的含义。

| 权限 | 字符 | 描述 |
|---|---|---|
| 读 | r | 查看文件内容 |
| 写 | w | 修改文件内容 |
| 执行 | x | 如果文件是程序或脚本，则运行它 |

此表显示了读、写和执行权限如何应用于目录。

| 权限 | 字符 | 描述 |
|---|---|---|
| 读 | r | 列出和复制目录内容 |
| 写 | w | 在目录中添加或删除文件（也需要 x） |
| 执行 | x | 使用 cd 进入目录 |

一个重要的区别是，需要在目录上拥有执行权限才能使用 cd 命令进入该目录。需要在文件上拥有执行权限才能将其作为程序或脚本运行。

## 了解身份

Linux 识别三种用于访问控制的身份：

- 拥有文件或目录的一个用户。
- 与文件或目录关联的一个组。
- 所有不是该用户或组成员的其他人。

| 身份 | 字符 | 描述 |
|---|---|---|
| 用户（所有者） | u | 文件或目录的创建者或关联身份。 |
| 组 | g | 与文件或目录关联的一个组。 |
| 其他 | o | 所有不是用户或组的帐户。 |

三种访问级别（rwx）可以应用于三种身份（ugo）。

## 显示和解释权限

显示目录内容的命令是 ls（“list”的缩写）。添加 -l 选项以显示文件和目录权限。在这些示例中使用 ls -l 来显示对权限的更改。

![](https://cdn.thenewstack.io/media/2024/03/c631867a-ls-l-depts.png)
![](https://cdn.thenewstack.io/media/2024/03/284ea07f-ls-l-depts-explain.png)

上图用颜色编码来解释哪些权限适用于哪些身份。黄色框（rwx）中的权限适用于用户 fsmith。绿色框显示 IT 组的权限（rw-）。其他身份只有读权限（r--），如红色框所示。破折号表示未授予权限。

## 了解权限模式

Linux 管理员有两种不同的设置权限的方法：绝对模式和符号模式。您的系统识别这两种模式，因此使用对您最简单的模式。您可能会发现自己在不同的时间点使用这两种模式。

### 了解绝对模式

绝对模式使用数字八进制值来表示权限级别。

| 权限 | 八进制值 |
|---|---|
| r（读） | 4 |
| w（写） | 2 |
| x（执行） | 1 |

绝对模式将数字权限值相加以表示整体访问级别。值的总和按特定顺序排列：用户、然后是组、然后是其他人。

**示例 1**: 读、写和执行访问 = r (4) + w (2) + x (1) = 7
- 所有访问级别的绝对模式值为 7 (4+2+1)

**示例 2**: 读和写（但不能执行） = r (4) + w (2) = 6
- 对文件的读写但不能执行访问的绝对模式值为 6。

**示例 3**: 仅读（无写和无执行） = r (4)
- 仅读访问的绝对模式值为 4。

绝对模式还按特定顺序使用三个身份，始终是用户、组、其他人（ugo）。

**示例 1**: 用户拥有 rwx，组拥有 r-x，其他人没有访问权限 = 750
- 用户拥有 7（读+写+执行的值），组拥有 5（读+执行），其他人拥有 0（没有值）。

**示例 2**: 用户拥有 rw-，组拥有 r–，其他人拥有 r– = 644
- 用户拥有 6 (r+w)，组和其他人拥有 4 (读)。

绝对模式听起来非常复杂，但一旦您习惯了这些值，它比符号模式更简单、更快。我几乎总是使用绝对模式在 Linux 上工作。

### 了解符号模式

符号模式将身份字母（ugo）、权限字母（rwx）和数学运算符（+，-，=）组合起来以配置权限。

以下是一些示例：

- 授予用户对文件的读权限如下所示：u+r（为用户添加读权限）。
- 为组授予读写权限为 g+rw（为组添加读写权限）。
- 从其他人那里删除读写权限为 o-rw（从其他人那里减去读写权限）。

符号模式的优点是能够逻辑地推断出您想要什么，而不是仅仅应用数学结果。您可能会对自己说，“我想为用户和组添加读写权限。” 这看起来很合乎逻辑：ug+rw。

## 使用 `chmod`

命令

现在您已经可以解释标准的 Linux 权限，是时候使用 chmod（“更改模式”）命令来设置权限。您将在这里使用绝对模式或符号模式。

无论您喜欢哪种模式，chmod 语法如下所示：

$ chmod PERMISSION filename

文件名值是命令的参数（它所作用的对象）。在以下示例中，我将对 fileA.txt 应用各种权限。

绝对模式示例：

**示例 1**：将用户权限设置为 u = rwx、group = r-x 和 others = —。
$ chmod 760 fileA.txt

![](https://cdn.thenewstack.io/media/2024/03/29b81dcf-chmod760-filea.png)
**示例 2**：将 user = rw-、group = r–、others = r–
$ chmod 644 fileA.txt

此方法要求您使用三个身份的总和来声明所需的实际权限级别。

注意：本教程末尾有一个关于这些概念的练习。

### 符号模式示例
符号模式不同，因为它从现有值中添加或减去所需的权限。如果用户已经对文件具有读取权限，但您还想授予写入权限，那么您只需将写入权限添加到现有值中：

1 |
$ chmod u+w fileA.txt |
![](https://cdn.thenewstack.io/media/2024/03/49be134a-chmoduplusw-filea.png)
此示例保留了用户现有的读取权限，并且根本没有修改组或其他权限。

授予组读取和写入权限如下所示：

1 |
$ chmod g+rw fileA.txt |
同样，这会保留现有的用户和其他人权限。
本教程末尾有一个关于这些概念的练习。

语法回顾：

- 绝对模式使用表示 rwx 权限的值之和。这些值按表示用户、组和其他的顺序列出。
- 符号模式将三个身份的首字母缩写（ugo）与三个访问级别的首字母缩写（rwx）结合使用 + 和 - 来添加或删除权限。
### 应该使用哪种模式？
那么，在日常 Linux 任务中应该使用哪种模式？您应该了解并识别这两种模式，原因如下：

- 认证考试会测试您对这两种方法的掌握程度。
- 文档可能使用任一方法编写，因此您必须能够理解每种方法。
但是，您可以随意使用对您最有意义的模式。我更喜欢绝对模式，因为它需要更少的输入并且更直接。其他人则乐于使用符号模式。只要确保您理解这两种方法即可。

## 管理文件和目录所有权
chmod 命令允许您设置权限，但 chown 命令会更改权限适用的对象。您可以更改用户（所有者）和组关联，将各种目录和文件重新分配给系统中的任何人。

### 使用 `chown`
命令
您可能希望进行三种所有权更改：更改所有者（用户）、更改关联的组或同时更改两者。

要更改文件或目录的所有者，请键入：

1 |
$ chown user FILE |
要更改分配给文件或目录的组，请键入：
1 |
$ chown :group FILE |
要同时更改这两个值，请键入：
1 |
$ chown user:group FILE |
考虑以下示例，您需要将
fsmith 帐户设置为
password-reset.txt 文本文件的所有者，您是在本教程开始时创建的：
1 |
$ chown fsmith password-reset.txt |
接下来，将
HR 组与
hr_dept 目录关联。
1 |
$ chown :HR hr_dept |
也许您需要将
mgarcia 设置为所有者，并将
PR 组与
pr_dept 目录同时关联：
1 |
$ chown mgarcia:PR pr_dept |
使用
-R 选项更改目录及其所有内容的所有权。
-R 选项代表“递归”。要将
IT 组与
it_dept 目录中的任何目录和文件关联，请键入：
1 |
$ chown -R :IT it_dept |
## 实践机会
我编写了一些基本练习，以帮助您练习使用 chmod 和 chown。

如果您没有在文章开头创建用户、组、目录和文件，请现在返回并创建它们。您可以根据需要修改用户名、组、目录和文件。通过匹配以下要求，练习使用本教程中的命令。

### 实践设置所有权
使用 chown 命令设置部门目录的所有权和组关联：

- 将 fsmith 设置为 it_dept 目录的所有者（使其递归）。
- 将 mgarcia 设置为 pr_dept 目录的所有者（使其递归）。
- 将 slee 设置为 hr_dept 目录的所有者（使其递归）。
- 将 IT、HR 和 PR 组递归地与匹配的部门目录关联。
![](https://cdn.thenewstack.io/media/2024/03/48a4e10b-set-owner-grp.png)
### 实践目录权限
使用绝对模式设置以下访问级别：

- 将 mgarcia 的递归权限设置为 rwx，PR 组的权限设置为 rwx，其他人的权限设置为 r-x，应用于 pr_dept 目录。
- 将 slee 的递归权限设置为 rwx，HR 组的权限设置为 rwx，其他人的权限设置为 r-x，应用于 hr_dept 目录。
- 将 fsmith 的递归权限设置为 rwx，IT 组的权限设置为 rwx，其他人的权限设置为 rwx，应用于 it_dept 目录。
![](https://cdn.thenewstack.io/media/2024/03/27fc32a4-perms-results-abs.png)
### 实践文件权限

- 将 fsmith 的权限设置为 rwx，IT 组的权限设置为 r-x，其他人的权限设置为 —，应用于 password-reset.txt 文件。
- 将 mgarcia 的权限设置为 rw-，PR 组的权限设置为 r–，其他人的权限设置为 r–，应用于 pr_dept 目录中的 pr_report.txt 文件。
- 将 slee 的权限设置为 rwx，HR 组的权限设置为 rwx，其他人的权限设置为 —，应用于 hr_dept 目录中的 hr_report.txt 文件。
![](https://cdn.thenewstack.io/media/2024/03/6962014c-perms-results-abs-files.png)
### 实践符号模式
使用符号模式设置以下访问级别：

- 将 mgarcia 的权限设置为 rwx，PR 组的权限设置为 rwx，其他人的权限设置为 r-x，应用于 pr_dept 目录。
- 将 slee 的权限设置为 rwx，HR 组的权限设置为 rwx，其他人的权限设置为 r-x，应用于 hr_dept 目录。
- 将 fsmith 的权限设置为 rwx，IT 组的权限设置为 rwx，其他人的权限设置为 rwx，应用于 it_dept 目录。
![](https://cdn.thenewstack.io/media/2024/03/57343974-perms-results-sym.png)
### 实践文件权限

- 将 fsmith 的权限设置为 rwx，IT 组的权限设置为 r-x，其他人的权限设置为 —，应用于 password-reset.txt 文件。
- 将 mgarcia 的权限设置为 rw-，PR 组的权限设置为 r–，其他人的权限设置为 r–，应用于 pr_dept 目录中的 pr_report.txt 文件。
- 将 slee 的权限设置为 rwx，HR 组的权限设置为 rwx，其他人的权限设置为 —，应用于 hr_dept 目录中的 hr_report.txt 文件。
![](https://cdn.thenewstack.io/media/2024/03/6962014c-perms-results-abs-files.png)
### 实践符号模式
使用符号模式设置以下访问级别：

- 将 mgarcia 的权限设置为 rwx，PR 组的权限设置为 rwx，其他人的权限设置为 r-x，应用于 pr_dept 目录。
- 将 slee 的权限设置为 rwx，HR 组的权限设置为 rwx，其他人的权限设置为 r-x，应用于 hr_dept 目录。
- 将 fsmith 的权限设置为 rwx，IT 组的权限设置为 rwx，其他人的权限设置为 rwx，应用于 it_dept 目录。
![](https://cdn.thenewstack.io/media/2024/03/57343974-perms-results-sym.png)
### 实践文件权限

- 将 fsmith 的权限设置为 rwx，IT 组的权限设置为 r-x，其他人的权限设置为 —，应用于 password-reset.txt 文件。
- 将 mgarcia 的权限设置为 rw-，PR 组的权限设置为 r–，其他人的权限设置为 r–，应用于 pr_dept 目录中的 pr_report.txt 文件。
- 将 slee 的权限设置为 rwx，HR 组的权限设置为 rwx，其他人的权限设置为 —，应用于 hr_dept 目录中的 hr_report.txt 文件。
![](https://cdn.thenewstack.io/media/2024/03/6962014c-perms-results-abs-files.png)
### 实践符号模式
使用符号模式设置以下访问级别：

- 将 mgarcia 的权限设置为 rwx，PR 组的权限设置为 rwx，其他人的权限设置为 r-x，应用于 pr_dept 目录。
- 将 slee 的权限设置为 rwx，HR 组的权限设置为 rwx，其他人的权限设置为 r-x，应用于 hr_dept 目录。
- 将 fsmith 的权限设置为 rwx，IT 组的权限设置为 rwx，其他人的权限设置为 rwx，应用于 it_dept 目录。
![](https://cdn.thenewstack.io/media/2024/03/57343974-perms-results-sym.png)
### 实践文件权限

- 将 fsmith 的权限设置为 rwx，IT 组的权限设置为 r-x，其他人的权限设置为 —，应用于 password-reset.txt 文件。
- 将 mgarcia 的权限设置为 rw-，PR 组的权限设置为 r–，其他人的权限设置为 r–，应用于 pr_dept 目录中的 pr_report.txt 文件。
- 将 slee 的权限设置为 rwx，HR 组的权限设置为 rwx，其他人的权限设置为 —，应用于 hr_dept 目录中的 hr_report.txt 文件。
![](https://cdn.thenewstack.io/media/2024/03/6962014c-perms-results-abs-files.png)
### 实践符号模式
使用符号模式设置以下访问级别：

- 将 mgarcia 的权限设置为 rwx，PR 组的权限设置为 rwx，其他人的权限设置为 r-x，应用于 pr_dept 目录。
- 将 slee 的权限设置为 rwx，HR 组的权限设置为 rwx，其他人的权限设置为 r-x，应用于 hr_dept 目录。
- 将 fsmith 的权限设置为 rwx，IT 组的权限设置为 rwx，其他人的权限设置为 rwx，应用于 it_dept 目录。
![](https://cdn.thenewstack.io/media/2024/03/57343974-perms-results-sym.png)
### 实践文件权限

- 将 fsmith 的权限设置为 rwx，IT 组的权限设置为 r-x，其他人的权限设置为 —，应用于 password-reset.txt 文件。
- 将 mgarcia 的权限设置为 rw-，PR 组的权限设置为 r–，其他人的权限设置为 r–，应用于 pr_dept 目录中的 pr_report.txt 文件。
- 将 slee 的权限设置为 rwx，HR 组的权限设置为 rwx，其他人的权限设置为 —，应用于 hr_dept 目录中的 hr_report.txt 文件。
![](https://cdn.thenewstack.io/media/2024/03/6962014c-perms-results-abs-files.png)
### 实践符号模式
使用符号模式设置以下访问级别：

- 将 mgarcia 的权限设置为 rwx，PR 组的权限设置为 rwx，其他人的权限设置为 r-x，应用于 pr_dept 目录。
- 将 slee 的权限设置为 rwx，HR 组的权限设置为 rwx，其他人的权限设置为 r-x，应用于 hr_dept 目录。
- 将 fsmith 的权限设置为 rwx，IT 组的权限设置为 rwx，其他人的权限设置为 rwx，应用于 it_dept 目录。
![](https://cdn.thenewstack.io/media/2024/03/57343974-perms-results-sym.png)
### 实践文件权限

- 将 fsmith 的权限设置为 rwx，IT 组的权限设置为 r-x，其他人的权限设置为 —，应用于 password-reset.txt 文件。
- 将 mgarcia 的权限设置为 rw-，PR 组的权限设置为 r–，其他人的权限设置为 r–，应用于 pr_dept 目录中的 pr_report.txt 文件。
- 将 slee 的权限设置为 rwx，HR 组的权限设置为 rwx，其他人的权限设置为 —，应用于 hr_dept 目录中的 hr_report.txt 文件。
![](https://cdn.thenewstack.io/media/2024/03/6962014c-perms-results-abs-files.png)
### 实践符号模式
使用符号模式设置以下访问级别：

- 将 mgarcia 的权限设置为 rwx，PR 组的权限设置为 rwx，其他人的权限设置为 r-x，应用于 pr_dept 目录。
- 将 slee 的权限设置为 rwx，HR 组的权限设置为 rwx，其他人的权限设置为 r-x，应用于 hr_dept 目录。
- 将 fsmith 的权限设置为 rwx，IT 组的权限设置为 rwx，其他人的权限设置为 rwx，应用于 it_dept 目录。
![](https://cdn.thenewstack.io/media/2024/03/57343974-perms-results-sym.png)
### 实践文件权限

- 将 fsmith 的权限设置为 rwx，IT 组的权限设置为 r-x，其他人的权限设置为 —，应用于 password-reset.txt 文件。
- 将 mgarcia 的权限设置为 rw-，PR 组的权限设置为 r–，其他人的权限设置为 r–，应用于 pr_dept 目录中的 pr_report.txt 文件。
- 将 slee 的权限设置为 rwx，HR 组的权限设置为 rwx，其他人的权限设置为 —，应用于 hr_dept 目录中的 hr_report.txt 文件。
![](https://cdn.thenewstack.io/media/2024/03/6962014c-perms-results-abs-files.png)
### 实践符号模式
使用符号模式设置以下访问级别：

- 将 mgarcia 的权限设置为 rwx，PR 组的权限设置为 rwx，其他人的权限设置为 r-x，应用于 pr_dept 目录。
- 将 slee 的权限设置为 rwx，HR 组的权限设置为 rwx，其他人的权限设置为 r-x，应用于 hr_dept 目录。
- 将 fsmith 的权限设置为 rwx，IT 组的权限设置为 rwx，其他人的权限设置为 rwx，应用于 it_dept 目录。
![](https://cdn.thenewstack.io/media/2024/03/57343974-perms-results-sym.png)
### 实践文件权限

- 将 fsmith 的权限设置为 rwx，IT 组的权限设置为 r-x，其他人的权限设置为 —，应用于 password-reset.txt 文件。
- 将 mgarcia 的权限设置为 rw-，PR 组的权限设置为 r–，其他人的权限设置为 r–，应用于 pr_dept 目录中的 pr_report.txt 文件。
- 将 slee 的权限设置为 rwx，HR 组的权限设置为 rwx，其他人的权限设置为 —，应用于 hr_dept 目录中的 hr_report.txt 文件。
![](https://cdn.thenewstack.io/media/2024/03/6962014c-perms-results-abs-files.png)
### 实践符号模式
使用符号模式设置以下访问级别：

- 将 mgarcia 的权限设置为 rwx，PR 组的权限设置为 rwx，其他人的权限设置为 r-x，应用于 pr_dept 目录。
- 将 slee 的权限设置为 rwx，HR 组的权限设置为 rwx，其他人的权限设置为 r-x，应用于 hr_dept 目录。
- 将 fsmith 的权限设置为 rwx，IT 组的权限设置为 rwx，其他人的权限设置为 rwx，应用于 it_dept 目录。
![](https://cdn.thenewstack.io/media/2024/03/57343974-perms-results-sym.png)
### 实践文件权限

- 将 fsmith 的权限设置为 rwx，IT 组的权限设置为 r-x，其他人的权限设置为 —，应用于 password-reset.txt 文件。
- 将 mgarcia 的权限设置为 rw-，PR 组的权限设置为 r–，其他人的权限设置为 r–，应用于 pr_dept 目录中的 pr_report.txt 文件。
- 将 slee 的权限设置为 rwx，HR 组的权限设置为 rwx，其他人的权限设置为 —，应用于 hr_dept 目录中的 hr_report.txt 文件。
![](https://cdn.thenewstack.io/media/2024/03/6962014c-perms-results-abs-files.png)
### 实践符号模式
使用符号模式设置以下访问级别：

- 将 mgarcia 的权限设置为 rwx，PR 组的权限设置为 rwx，其他人的权限设置为 r-x，应用于 pr_dept 目录。
- 将 slee 的权限设置为 rwx，HR 组的权限设置为 rwx，其他人的权限设置为 r-x，应用于 hr_dept 目录。
- 将 fsmith 的权限设置为 rwx，IT 组的权限设置为 rwx，其他人的权限设置为 rwx，应用于 it_dept 目录。
![](https://cdn.thenewstack.io/media/2024/03/57343974-perms-results-sym.png)
### 实践文件权限

- 将 fsmith 的权限设置为 rwx，IT 组的权限设置为 r-x，其他人的权限设置为 —，应用于 password-reset.txt 文件。
- 将 mgarcia 的权限设置为 rw-，PR 组的权限设置为 r–，其他人的权限设置为 r–，应用于 pr_dept 目录中的 pr_report.txt 文件。
- 将 slee 的权限设置为 rwx，HR 组的权限设置为 rwx，其他人的权限设置为 —，应用于 hr_dept 目录中的 hr_report.txt 文件。
![](https://cdn.thenewstack.io/media/2024/03/6962014c-perms-results-abs-files.png)
### 实践符号模式
使用符号模式设置以下访问级别：

- 将 mgarcia 的权限设置为 rwx，PR 组的权限设置为 rwx，其他人的权限设置为 r-x，应用于 pr_dept 目录。
- 将 slee 的权限设置为 rwx，HR 组的权限设置为 rwx，其他人的权限设置为 r-x，应用于 hr_dept 目录。
- 将 fsmith 的权限设置为 rwx，IT 组的权限设置为 rwx，其他人的权限设置为 rwx，应用于 it_dept 目录。
![](https://cdn.thenewstack.io/media/2024/03/57343974-perms-results-sym.png)
### 实践文件权限

- 将 fsmith 的权限设置为 rwx，IT 组的权限设置为 r-x，其他人的权限设置为 —，应用于 password-reset.txt 文件。
- 将 mgarcia 的权限设置为 rw-，PR 组的权限设置为 r–，其他人的权限设置为 r–，应用于 pr_dept 目录中的 pr_report.txt 文件。
- 将 slee 的权限设置为 rwx，HR 组的权限设置为 rwx，其他人的权限设置为 —，应用于 hr_dept 目录中的 hr_report.txt 文件。
![](https://cdn.thenewstack.io/media/2024/03/6962014c-perms-results-abs-files.png)
### 实践符号模式
使用符号模式设置以下访问级别：

- 将 mgarcia 的权限设置为 rwx，PR 组的权限设置为 rwx，其他人的权限设置为 r-x，应用于 pr_dept 目录。
- 将 slee 的权限设置为 rwx，HR 组的权限设置为 rwx，其他人的权限设置为 r-x，应用于 hr_dept 目录。
- 将 fsmith 的权限设置为 rwx，IT 组的权限设置为 rwx，其他人的权限设置为 rwx，应用于 it_dept 目录。
![](https://cdn.thenewstack.io/media/2024/03/57343974-perms-results-sym.png)
### 实践文件权限

- 将 fsmith 的权限设置为 rwx，IT 组的权限设置为 r-x，其他人的权限设置为 —，应用于 password-reset.txt 文件。
- 将 mgarcia 的权限设置为 rw-，PR 组的权限设置为 r–，其他人的权限设置为 r–，应用于 pr_dept 目录中的 pr_report.txt 文件。
- 将 slee 的权限设置为 rwx，HR 组的权限设置为 rwx，其他人的权限设置为 —，应用于 hr_dept 目录中的 hr_report.txt 文件。
![](https://cdn.thenewstack.io/media/2024/03/6962014c-perms-results-abs-files.png)
### 实践符号模式
使用符号模式设置以下访问级别：

- 将 mgarcia 的权限设置为 rwx，PR 组的权限设置为 rwx，其他人的权限设置为 r-x，应用于 pr_dept 目录。
- 将 slee 的权限设置为 rwx，HR 组的权限设置为 rwx，其他人的权限设置为 r-x，应用于 hr_dept 目录。
- 将 fsmith 的权限设置为 rwx，IT 组的权限设置为 rwx，其他人的权限设置为 rwx，应用于 it_dept 目录。
![](https://cdn.thenewstack.io/media/2024/03/57343974-perms-results-sym.png)
### 实践文件权限

- 将 fsmith 的权限设置为 rwx，IT 组的权限设置为 r-x，其他人的权限设置为 —，应用于 password-reset.txt 文件。
- 将 mgarcia 的权限设置为 rw-，PR 组的权限设置为 r–，其他人的权限设置为 r–，应用于 pr_dept 目录中的 pr_report.txt 文件。
- 将 slee 的权限设置为 rwx，HR 组的权限设置为 rwx，其他人的权限设置为 —，应用于 hr_dept 目录中的 hr_report.txt 文件。
![](https://cdn.thenewstack.io/media/2024/03/6962014c-perms-results-abs-files.png)
### 实践符号模式
使用符号模式设置以下访问级别：

- 将 mgarcia 的权限设置为 rwx，PR 组的权限设置为 rwx，其他人的权限设置为 r-x，应用于 pr_dept 目录。
- 将 slee 的权限设置为 rwx，HR 组的权限设置为 rwx，其他人的权限设置为 r-x，应用于 hr_dept 目录。
- 将 fsmith 的权限设置为 rwx，IT 组的权限设置为 rwx，其他人的权限设置为 rwx，应用于 it_dept 目录。
![](https://cdn.thenewstack.io/media/2024/03/57343974-perms-results-sym.png)
### 实践文件权限

- 将 fsmith 的权限设置为 rwx，IT 组的权限设置为 r-x，其他人的权限设置为 —，应用于 password-reset.txt 文件。
- 将 mgarcia 的权限设置为 rw-，PR 组的权限设置为 r–，其他人的权限设置为 r–，应用于 pr_dept 目录中的 pr_report.txt 文件。
- 将 slee 的权限设置为 rwx，HR 组的权限设置为 rwx，其他人的权限设置为 —，应用于 hr_dept 目录中的 hr_report.txt 文件。
![](https://cdn.thenewstack.io/media/2024/03/6962014c-perms-results-abs-files.png)
### 实践符号模式
使用符号模式设置以下访问级别：

- 将 mgarcia 的权限设置为 rwx，PR 组的权限设置为 rwx，其他人的权限设置为 r-x，应用于 pr_dept 目录。
- 将 slee 的权限设置为 rwx，HR 组的权限设置为 rwx，其他人的权限设置为 r-x，应用于 hr_dept 目录。
- 将 fsmith 的权限设置为 rwx，IT 组的权限设置为 rwx，其他人的权限设置为 rwx，应用于 it_dept 目录。
![](https://cdn.thenewstack.io/media/2024/03/57343974-perms-results-sym.png)
### 实践文件权限

- 将 fsmith 的权限设置为 rwx，IT 组的权限设置为 r-x，其他人的权限设置为 —，应用于 password-reset.txt 文件。
- 将 mgarcia 的权限设置为 rw-，PR 组的权限设置为 r–，其他人的权限设置为 r–，应用于 pr_dept 目录中的 pr_report.txt 文件。
- 将 slee 的权限设置为 rwx，HR 组的权限设置为 rwx，其他人的权限设置为 —，应用于 hr_dept 目录中的 hr_report.txt 文件。
![](https://cdn.thenewstack.io/media/2024/03/6962014c-perms-results-abs-files.png)
### 实践符号模式
使用符号模式设置以下访问级别：

- 将 mgarcia 的权限设置为 rwx，PR 组的权限设置为 rwx，其他人的权限设置为 r-x，应用于 pr_dept 目录。
- 将 slee 的权限设置为 rwx，HR 组的权限设置为 rwx，其他人的权限设置为 r-x，应用于 hr_dept 目录。
- 将 fsmith 的权限设置为 rwx，IT 组的权限设置为 rwx，其他人的权限设置为 rwx，应用于 it_dept 目录。
![](https://cdn.thenewstack.io/media/2024/03/57343974-perms-results-sym.png)
### 实践文件权限

- 将 fsmith 的权限设置为 rwx，IT 组的权限设置为 r-x，其他人的权限设置为 —，应用于 password-reset.txt 文件。
- 将 mgarcia 的权限设置为 rw-，PR 组的权限设置为 r–，其他人的权限设置为 r–，应用于 pr_dept 目录中的 pr_report.txt 文件。
- 将 slee 的权限设置为 rwx，HR 组的权限设置为 rwx，其他人的权限设置为 —，应用于 hr_dept 目录中的 hr_report.txt 文件。
![](https://cdn.thenewstack.io/media/2024/03/6962014c-perms-results-abs-files.png)
### 实践符号模式
使用符号模式设置以下访问级别：

- 将 mgarcia 的权限设置为 rwx，PR 组的权限设置为 rwx，其他人的权限设置为 r-x，应用于 pr_dept 目录。
- 将 slee 的权限设置为 rwx，HR 组的权限设置为 rwx，其他人的权限设置为 r-x，应用于 hr_dept 目录。
- 将 fsmith 的权限设置为 rwx，IT 组的权限设置为 rwx，其他人的权限设置为 rwx，应用于 it_dept 目录。
![](https://cdn.thenewstack.io/media/2024/03/57343974-perms-results-sym.png)
### 实践文件权限

- 将 fsmith 的权限设置为 rwx，IT 组的权限设置为 r-x，其他人的权限设置为 —，应用于 password-reset.txt 文件。
- 将 mgarcia 的权限设置为 rw-，PR 组的权限设置为 r–，其他人的权限设置为 r–，应用于 pr_dept 目录中的 pr_report.txt 文件。
- 将 slee 的权限设置为 rwx，HR 组的权限设置为 rwx，其他人的权限设置为 —，应用于 hr_dept 目录中的 hr_report.txt 文件。
![](https://cdn.thenewstack.io/media/2024/03/6962014c-perms-results-abs-files.png)
### 实践符号模式
使用符号模式设置以下访问级别：

- 将 mgarcia 的权限设置为 rwx，PR 组的权限设置为 rwx，其他人的权限设置为 r-x，应用于 pr_dept 目录。
- 将 slee 的权限设置为 rwx，HR 组的权限设置为 rwx，其他人的权限设置为 r-x，应用于 hr_dept 目录。
- 将 fsmith 的权限设置为 rwx，IT 组的权限设置为 rwx，其他人的权限设置为 rwx，应用于 it_dept 目录。
![](https://cdn.thenewstack.io/media/2024/03/57343974-perms-results-sym.png)
### 实践文件权限

- 将 fsmith 的权限设置为 rwx，IT 组的权限设置为 r-x，其他人的权限设置为 —，应用于 password-reset.txt 文件。
- 将 mgarcia 的权限设置为 rw-，PR 组的权限设置为 r–，其他人的权限设置为 r–，应用于 pr_dept 目录中的 pr_report.txt 文件。
- 将 slee 的权限设置为 rwx，HR 组的权限设置为 rwx，其他人的权限设置为 —，应用于 hr_dept 目录中的 hr_report.txt 文件。
![](https://cdn.thenewstack.io/media/2024/03/6962014c-perms-results-abs-files.png)
### 实践符号模式
使用符号模式设置以下访问级别：

- 将 mgarcia 的权限设置为 rwx，PR 组的权限设置为 rwx，其他人的权限设置为 r-x，应用于 pr_dept 目录。
- 将 slee 的权限设置为 rwx，HR 组的权限设置为 rwx，其他人的权限设置为 r-x，应用于 hr_dept 目录。
- 将 fsmith 的权限设置为 rwx，IT 组的权限设置为 rwx，其他人的权限设置为 rwx，应用于 it_dept 目录。
![](https://cdn.thenewstack.io/media/2024/03/57343974-perms-results-sym.png)
### 实践文件权限

- 将 fsmith 的权限设置为 rwx，IT 组的权限设置为 r-x，其他人的权限设置为 —，应用于 password-reset.txt 文件。
- 将 mgarcia 的权限设置为 rw-，PR 组的权限设置为 r–，其他人的权限设置为 r–，应用于 pr_dept 目录中的 pr_report.txt 文件。
- 将 slee 的权限设置为 rwx，HR 组的权限设置为 rwx，其他人的权限设置为 —，应用于 hr_dept 目录中的 hr_report.txt 文件。
![](https://cdn.thenewstack.io/media/2024/03/6962014c-perms-results-abs-files.png)
### 实践符号模式
使用符号模式设置以下访问级别：

- 将 mgarcia 的权限设置为 rwx，PR 组的权限设置为 rwx，其他人的权限设置为 r-x，应用于 pr_dept 目录。
- 将 slee 的权限设置为 rwx，HR 组的权限设置为 rwx，其他人的权限设置为 r-x，应用于 hr_dept 目录。
- 将 fsmith 的权限设置为 rwx，IT 组的权限设置为 rwx，其他人的权限设置为 rwx，应用于 it_dept 目录。
![](https://cdn.thenewstack.io/media/2024/03/57343974-perms-results-sym.png)
### 实践文件权限

- 将 fsmith 的权限设置为 rwx，IT 组的权限设置为 r-x，其他人的权限设置为 —，应用于 password-reset.txt 文件。
- 将 mgarcia 的权限设置为 rw-，PR 组的权限设置为 r–，其他人的权限设置为 r–，应用于 pr_dept 目录中的 pr_report.txt 文件。
- 将 slee 的权限设置为 rwx，HR 组的权限设置为 rwx，其他人的权限设置为 —，应用于 hr_dept 目录中的 hr_report.txt 文件。
![](https://cdn.thenewstack.io/media/2024/03/6962014c-perms-results-abs-files.png)
### 实践符号模式
使用符号模式设置以下访问级别：

- 将 mgarcia 的权限设置为 rwx，PR 组的权限设置为 rwx，其他人的权限设置为 r-x，应用于 pr_dept 目录。
- 将 slee 的权限设置为 rwx，HR 组的权限设置为 rwx，其他人的权限设置为 r-x，应用于 hr_dept 目录。
- 将 fsmith 的权限设置为 rwx，IT 组的权限设置为 rwx，其他人的权限设置为 rwx，应用于 it_dept 目录。
![](https://cdn.thenewstack.io/media/2024/03/57343974-perms-results-sym.png)
### 实践文件权限

- 将 fsmith 的权限设置为 rwx，IT 组的权限设置为 r-x，其他人的权限设置为 —，应用于 password-reset.txt 文件。
- 将 mgarcia 的权限设置为 rw-，PR 组的权限设置为 r–，其他人的权限设置为 r–，应用于 pr_dept 目录中的 pr_report.txt 文件。
- 将 slee 的权限设置为 rwx，HR 组的权限设置为 rwx，其他人的权限设置为 —，应用于 hr_dept 目录中的 hr_report.txt 文件。
![](https://cdn.thenewstack.io/media/2024/03/6962014c-perms-results-abs-files.png)
### 实践符号模式
使用符号模式设置以下访问级别：

- 将 mgarcia 的权限设置为 rwx，PR 组的权限设置为 rwx，其他人的权限设置为 r-x，应用于 pr_dept 目录。
- 将 slee 的权限设置为 rwx，HR 组的权限设置为 rwx，其他人的权限设置为 r-x，应用于 hr_dept 目录。
- 将 fsmith 的权限设置为 rwx，IT 组的权限设置为 rwx，其他人的权限设置为 rwx，应用于 it_dept 目录。
![](https://cdn.thenewstack.io/media/2024/03/57343974-perms-results-sym.png)
### 实践文件权限

- 将 fsmith 的权限设置为 rwx，IT 组的权限设置为 r-x，其他人的权限设置为 —，应用于 password-reset.txt 文件。
- 将 mgarcia 的权限设置为 rw-，PR 组的权限设置为 r–，其他人的权限设置为 r–，应用于 pr_dept 目录中的 pr_report.txt 文件。
- 将 slee 的权限设置为 rwx，HR 组的权限设置为 rwx，其他人的权限设置为 —，应用于 hr_dept 目录中的 hr_report.txt 文件。
![](https://cdn.thenewstack.io/media/2024/03/6962014c-perms-results-abs-files.png)
### 实践符号模式
使用符号模式设置以下访问级别：

- 将 mgarcia 的权限设置为 rwx，PR 组的权限设置为 rwx，其他人的权限设置为 r-x，应用于 pr_dept 目录。
- 将 slee
使用 `chown` 命令设置所有权，并使用符号模式的 `chmod` 命令添加和删除权限，直到它们满足以下要求：

- 授予 fsmith 对 password-reset.txt 文件的 rw- 权限，授予当前组 rw- 权限，授予其他人 rw- 权限。
- 授予 mgarcia 对 press-releases.txt 文件的 rwx 权限，授予当前组 r-- 权限，授予其他人无访问权限。
- 授予 slee 对 policies.txt 文件的 rw- 权限，授予当前组 rw- 权限，授予其他人 r-- 权限。

![](https://cdn.thenewstack.io/media/2024/03/b002a44b-perms-results-sym.png)

随意创建其他用户、组、目录和文件以练习权限。

## 总结

控制对资源的访问是管理员的一项关键技能。它始于创建正确的用户和组帐户来代表用户。接下来，创建和组织文件和目录，并牢记安全性。最后，为所有者 (u)、组 (g) 和所有其他人 (o) 设置适当的权限。这种身份、资源和权限的组合是控制数据访问的基本组成部分。

本教程介绍了标准的 Linux 权限，但还有一些额外的特殊权限可以修改它们的工作方式。额外的 Linux 访问控制列表提供了更强大的控制文件安全性的方法。

花时间练习管理对文件和目录的访问非常值得，方法是创建一些示例资源和用户，然后设置各种权限和所有权。

[YOUTUBE.COM/THENEWSTACK](https://youtube.com/thenewstack?sub_confirmation=1)

技术发展迅速，不要错过任何一集。订阅我们的 YouTube 频道以流式传输我们所有的播客、访谈、演示等。