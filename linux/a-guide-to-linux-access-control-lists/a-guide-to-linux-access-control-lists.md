
<!--
title: Linux访问控制列表指南
cover: https://cdn.thenewstack.io/media/2024/07/ecabf01c-cornelius-ventures-ak81vc-kcf4-unsplash-linux.jpg
-->

本文介绍了 Linux 访问控制列表 (ACL)，它比标准的 Linux 权限提供了更大的灵活性。

> 译自 [A Guide to Linux Access Control Lists](https://thenewstack.io/a-guide-to-linux-access-control-lists/)，作者 Damon M Garn。

我们这些在 [Linux](https://thenewstack.io/learning-linux-start-here/) 和 [Microsoft Windows](https://news.microsoft.com/?utm_content=inline+mention) 之间快速切换的人，会发现一些根本性的差异。其中之一就是权限。标准的 Linux 权限非常简单：指定一个用户、一个组，然后是所有其他人（称为“其他人”），并根据需要授予读、写和执行权限。Windows 权限要复杂得多，包括嵌套、更多访问级别以及共享权限的混合。但是，在许多方面，Windows 权限在规模上也更灵活、更实用。

本文介绍了 Linux 访问控制列表 (ACL)，它提供了比标准 Linux 权限更灵活的功能。我将讨论如何查看和配置多个个人用户和多个组的 ACL。很有可能，您选择的 [Linux 发行版](https://thenewstack.io/choosing-a-linux-distribution/) 已经启用了 ACL（ACL 实际上是文件系统的功能）。

## 简要回顾标准 Linux 权限

您可以使用 [chmod](https://linux.die.net/man/1/chmod) 命令配置标准 [Linux 权限](https://thenewstack.io/linux-how-file-permissions-work/)。该命令设置三种访问级别的任意组合：读、写和执行。您可以将这些访问级别分配给三个身份：

- 用户（所有者）：拥有该文件的单个用户帐户（默认情况下，这是文件创建者）。
- 组：/etc/group 文件中显示的一个用户组。
- 其他：任何不是用户或分配组成员的人。

![](https://cdn.thenewstack.io/media/2024/09/304daf50-basic-ls-l.png)

*图 1：ls -l 命令显示标准权限、所有权和组关联。*

这种方法在用户和组很少的独立系统上已经足够了。但是，这种方法在共享系统、启用了文件共享功能的系统或具有大量 SSH 远程访问的设备上会变得更加繁琐。

这就是文件系统 ACL 功能派上用场的地方。它允许您为多个用户和/或组配置不同的访问级别。

## ACL 如何提供帮助？

ACL 允许您指定多个用户帐户并为它们提供不同的访问级别。这也意味着您不必将其中一个用户的拥有权授予该文件。它对组提供了相同的灵活性。

ACL 仍然识别读、写和执行这三个标准访问级别，因此您不必重新学习您已经了解的关于 Linux 权限的所有内容。实际上，ACL 与标准权限协同工作，因此您仍然可以使用基本的用户 (u)、组 (g) 和其他 (o) 身份。您是在补充常规权限，而不是替换它们。

### 验证您的发行版是否支持 ACL

当今的现代 Linux 发行版通常开箱即用地支持 ACL。请记住，ACL 是 [文件系统](https://thenewstack.io/how-to-manage-linux-storage/) 的功能，因此从那里开始。标准文件系统是 ext4、XFS 和 Btrfs。这些都支持 ACL。

您可能不需要检查您的 Linux 发行版是否支持 ACL，但如果您想确认，可以使用以下命令：

```
tune2fs -l /dev/sda1 | grep -i "Default mount options"
```

预计在输出中看到 acl。

![](https://cdn.thenewstack.io/media/2024/09/2a9fd946-defaultmountoptions.png)

*图 2：tune2fs 命令会显示文件系统设置，包括是否启用了 ACL。*

请注意，如果在资源上配置了 ACL，则 ls -l 输出将显示一个 + 字符。在以下示例中，ACL 应用于 file1.txt。

![](https://cdn.thenewstack.io/media/2024/09/3e07f113-ls-l-withacl.png)

*图 3：请注意 file1.txt 的权限字符串末尾有一个 + 字符，表示已应用 ACL。*

## 使用 setfacl 命令

ACL 配置命令是 [setfacl](https://linux.die.net/man/1/setfacl)。它依赖于标准的 Linux 命令语法：

```
command -options argument
```

参数将是您要应用访问控制的文件或目录。

setfacl 命令有许多选项。以下列表包含一些最常见的选项：

- m : 修改指定的 ACL。
- x : 从 ACL 中删除条目。
- b : 从 ACL 中删除所有条目。
- d : 为给定目录配置默认 ACL。
- R : 将 ACL 递归应用于所有目录内容。

但是，setfacl 还依赖于其他参数来定义新的访问控制是应用于用户还是组。

```
u:<username>
g:<groupname>
```

结合起来，这些设置允许管理员实施更强大、更实用的权限配置。

以下命令示例简要介绍了如何使用 setfacl。更具体的示例将在下一节中介绍。

要为用户 django 配置 ACL，授予其对 sample.txt 资源的读 (r) 权限，请键入：

```
setfacl -m u:django:r sample.txt
```

类似的组工程示例如下：

```
setfacl -m g:engineering:r sample.txt
```

配置完 ACL 设置后，您需要检查它们是否正确。这就是 `getfacl` 命令发挥作用的地方。

## 使用 `getfacl` 命令

管理 ACL 的另一个相关命令是 [`getfacl`](https://linux.die.net/man/1/getfacl)，它显示当前的 ACL 设置。

基本语法是 `getfacl` 和您要查看的文件或目录名称：

```
getfacl /dev-projects
```

但是，与大多数 Linux 命令一样，`getfacl` 支持许多有用的选项来修改其输出。这些包括：

- `-c`：仅显示 ACL 条目，并丢弃额外的标题信息。
- `-R`：递归显示目录内容。
- `-t`：以更易读的表格格式显示输出。

在审核或配置访问控制时，使用 `getfacl` 来查看 ACL 设置。

![](https://cdn.thenewstack.io/media/2024/09/b9016a72-basic-getfacl.png)

*图 4：getfacl 命令显示标准 ACL 和 ACL 设置。*

## ACL 使用案例

下面您将找到 ACL 的两个使用案例，包括一个场景和相关的命令。考虑类似的情况可能在您的环境中发生。

### 场景 1

我将从一个简单的例子开始：一个销售团队需要对 `/sales` 目录具有 `rwx` 权限，而一个营销团队应该只有 `r-x` 权限。其他人不需要访问。（请记住，这些组需要执行权限才能进入目录。）

首先，将标准 `rwx` 权限授予销售团队：

```
chown -R :sales /sales

chmod -R 770 /sales
```

接下来，为营销团队设置 ACL：

```
setfacl -m g:marketing:r-x /sales
```

使用 `getfacl /sales` 确认您的设置。

请记住，ACL 与标准权限一起工作，因此不要忘记使用 `ls -l` 命令来考虑这两个系统。但是，`getfacl` 命令除了 ACL 条目外，还会显示标准权限。

### 场景 2

想象一下另一种情况，您需要向不同的用户和组授予不同级别的访问权限。假设您有一个 `/dev-projects` 目录，具有以下要求：

- 所有者：root 具有完全访问权限（`rwx`）。
- 组：developers 具有完全访问权限（`rwx`）。
- 额外用户：alex（代码审查者）具有只读访问权限（`r-x`）。
- 额外用户：silas（项目经理）具有只读访问权限（`r-x`）。
- 额外组：contract-dev-team 具有只读访问权限（`r-x`）。

标准权限无法满足这种要求，但 ACL 可以轻松地处理它。

首先设置标准权限：

```
chown -R root:developers /dev-projects

chmod -R 770 /dev-projects
```

接下来，为额外的用户和组配置 ACL 条目：

```
setfacl -R u:alex:r-x /dev-projects

setfacl -R u:silas:r-x /dev/projects

setfacl -R g:contract-dev-team:r-x /dev/projects
```

使用 `getfacl` 和 `ls -l` 检查结果以显示设置。

## 总结

访问控制列表 (ACL) 扩展了 Linux 权限的功能，允许不同的用户和组具有不同的访问级别。虽然这确实使故障排除更加复杂，但额外的灵活性是值得的。

ACL 功能是文件系统的一部分。当今的现代文件系统支持 ACL，并且可能已经启用了它。请务必创建一个有效利用 ACL 的目录基础结构，通过根据访问要求组织资源。一般来说，销售团队的所有内容都应该存在于一个父目录中，而营销团队所需的所有内容都应该存在于另一个目录中。

ACL 在大型部署中变得尤为重要，例如支持许多用户和资源（具有不同的访问要求）的主要文件服务器。今天检查您的大型部署，看看 ACL 是否可以更有效地控制资源访问。在排查看似神秘的访问问题时，不要忘记考虑 ACL。
