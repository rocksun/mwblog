
<!--
title: Podman 5.0重大改进详解
cover: ./cover.png
-->

Podman 5.0 已发布，其中也包含一些重大更改，但不必担心；除非您使用 podman machine，否则您甚至不会注意到它们。

> 译自 [Podman 5.0 breaking changes in detail](https://blog.podman.io/2024/03/podman-5-0-breaking-changes-in-detail/)，作者 Paul Holzinger。

## Podman Machine

最大的重大变更是对 podman machine 配置文件进行重大重构。旧格式无法迁移到新格式。在 MacOS 上，还移除了对 qemu 提供程序的支持，转而支持性能更高的 Apple 虚拟机管理程序。有关机器变更的更多详细信息，请参阅[此博文](https://blog.podman.io/2024/03/migration-of-podman-4-to-podman-5-machines/)，作者为 Brent Baude。

## 删除 CNI

在 Podman 4.0 中，我们引入了新的网络后端 netavark 来配置容器网络，从那时起，我们默认使用 netavark 而非 CNI。但是，从 3.X 及更早版本更新的用户并未迁移到 netavark，因此他们继续使用 CNI。在 5.0 中，由于尝试使用两个工具会增加支持负担，因此我们只会支持 netavark。CNI 支持仍受构建标记 (cni) 保护，并且我们仍然需要在依赖它的发行版（例如 RHEL 9 和 FreeBSD）上启用，但如果 CNI 集成出现问题，请不要指望上游维护人员提供任何帮助。

用户可以使用 `podman info --format {{.Host.NetworkBackend}}` 命令检查他们使用的后端，它将打印 netavark 或 cni。如果是 netavark，您无需担心任何事情。一切都将像以前一样继续工作。对于 cni，可能需要手动干预。如果您不关心您的容器，您可以运行 `podman system reset`，它会删除所有内容。否则，请使用 `podman network ls` 检查您是否定义了任何自定义网络。如果没有，则更新不应导致太多问题，尽管强烈建议重新启动以防止任何旧的临时网络接口/防火墙规则干扰 netavark。如果您确实有自定义网络，它们都将在升级时丢失，因此需要手动迁移。

假设网络仅通过 `podman network create` 创建，那么一种迁移方法是使用此单行命令将所有旧 cni 配置保存在新的 netavark 格式中：

```
for name in $(podman network ls -q); do podman network inspect --format "{{json .}}" "$name" > "$name.json"; done
```

此命令必须在仍使用 Podman 4.* 时执行。它将在您的当前目录中创建一堆 .json 文件，一旦您更新到 Podman 5.0，您只需将文件移动到网络配置文件目录即可。作为 root 的默认值为 `/etc/containers/networks/`，作为 rootless 的默认值为 `~/.local/share/containers/storage/networks/`。然后确认 `podman network ls` 显示网络。或者，您只需使用 `podman network create` 命令重新创建网络。

## 废弃 Cgroups v1

对具有 cgroups v1 的系统的支持已弃用，并将在未来版本中删除。请迁移到 cgroups v2。大多数发行版已经这样做，因此我们预计不会有太多用户受到此影响。在 cgroups v1 系统上，将为每个 podman 命令打印警告。要关闭警告，请设置 `PODMAN_IGNORE_CGROUPSV1_WARNING` 环境变量。

## Pasta 作为 rootless 网络的默认值

默认的 rootless 网络工具已从 [slirp4netns](https://github.com/rootless-containers/slirp4netns) 切换到 [pasta](https://passt.top/passt/about/#pasta-pack-a-subtle-tap-abstraction)。它应该提供更好的性能和更多功能。因此，如果您使用具有网络功能的 rootless 容器，则需要确保已安装 pasta（passt 包的一部分）。虽然我不认为这对许多人来说一定是重大变更，但对某些用户来说可能是重大变更。在 4.X 上使用默认网络选项创建的 rootless 容器在升级后仍将继续使用 slirp4netns 作为网络工具，因为网络模式是在创建容器时设置的，因此如果您想让旧容器继续工作，则需要确保 slirp4netns 在这种情况下升级后仍已安装。

默认情况下，Pasta 不执行网络地址转换 (NAT)，并将主接口中的 IP 地址复制到容器命名空间中。为此，pasta 将选择具有默认路由的接口。如果 pasta 找不到具有默认路由的接口，它将在只有一个接口具有有效路由的情况下选择一个接口。如果您没有默认路由，并且多个接口已定义路由，pasta 将无法找出正确的接口，并且它将无法启动。在这种情况下，用户需要使用 `-i` 选项为 pasta 指定要使用的接口，因为 Podman 启动 pasta，所以用户无法直接执行此操作。可以在 `containers.conf` 中设置一组默认的 pasta 选项，`pasta_options` 键接受一系列选项（它们对应于 pasta cli 选项，请参阅 pasta(1) 手册页）。

```
[network]
pasta_options = ["-i", "eth0"]
```

默认情况下，无法通过 eth0（或任何称为主接口的接口）ip 连接到主机，因为容器中使用了完全相同的 ip，因此不会路由到外部。这可能会给 host.containers.internal 名称条目的用户带来问题，因为我们依赖于主机 ip 可达。对于 Podman 5.0.0，此条目很可能包含无效的 ip，但我们正在为 Podman 5.0.1 修复此问题。但是，如果您只有一个主机 ip（不包括 localhost），则基础问题将继续存在，因为如果容器始终使用相同的 ip，则无法路由到该容器。一种解决方法是告诉 pasta 在容器中使用不同的地址。在这种情况下，在 containers.conf 中设置类似以下内容：

```
pasta_options = ["-a", "10.0.2.0", "-n", "24", "-g", "10.0.2.2", "--dns-forward", "10.0.2.3"]
```

此外，可以在 [network] 部分下的 containers.conf 中选择默认的无根网络工具，该工具可以设置为 pasta 或 slirp4netns。因此，如果您遇到错误，您可以随时恢复到 slirp4netns。

```
[network]
default_rootless_network_cmd = "slirp4netns"
```

## Podman Inspect

podman inspect JSON 输出中的一些字段已更改，以更好地匹配 Docker 输出。Config.Entrypoint 字段已从字符串更改为数组，因为它可以容纳多个参数。以前，这些参数将以空格分隔，这不利于解析。Config.StopSignal 字段现在是一个字符串，而不是一个整数。因此，它不再返回信号号，而是返回信号名称。这更便于我们人类阅读，并且更利于跨平台兼容性，因为信号号在不同平台之间可能有所不同。最后，如果容器没有定义健康检查，则不再显示 State.Health 字段。相同的更改适用于 libpod REST API。两个版本之间的差异如下所示：

```
23,27d22
<                "Health": {
<                     "Status": "",
<                     "FailingStreak": 0,
<                     "Log": null
<                },
145c140,142
<                "Entrypoint": "sh",
---
>                "Entrypoint": [
>                     "sh"
>                ],
149c146
<                "StopSignal": 15,
---
>                "StopSignal": "SIGTERM",
```

## Podman Pod Inspect

podman pod inspect 命令现在总是输出一个数组，而不是一个对象。这样做是为了提高与执行相同操作的其他 inspect 命令的一致性。如果您解析 `podman pod inspect` JSON，您必须更新它以使用第一个数组元素。

## 容器统计信息 API

libpod 统计信息 API 已更改为按接口返回网络统计信息。包含所有接口总和的单个 NetInput 和 NetOutput 字段已删除，而添加了一个 Network 字段，其中包含一个映射/对象，其中接口名称作为键，每个接口统计信息作为值。

```
"Network":{"eth0":{"RxBytes":3740,"RxDropped":0,"RxErrors":0,"RxPackets":42,"TxBytes":3036,"TxDropped":0,"TxErrors":0,"TxPackets":34}}
```

这为用户提供了更多信息。

## Podman 命令行标志

已更改解析多个 Podman CLI 选项（接受数组）的方式，不再接受字符串分隔的列表。

这些选项是：

- --annotation for podman manifest annotate and podman manifest add
- --configmap, --log-opt and --annotation for podman kube play
- --pubkeysfile for podman image trust set
- --encryption-key and --decryption-key for podman create, podman run, podman push and podman pull
- --env-file for podman exec
- --bkio-weight-device, --device-read-bps, --device-write-bps, --device-read-iops, --device-write-iops, --device, --label-file, --chrootdirs, --log-opt and --env-file for podman create and podman run
- --hooks-dir and --module as global podman options.

进行此更改的原因是为了允许在其值中使用逗号，而不是将其解释为分隔符。因此，例如，如果我的注释包含逗号设置 `--annotation key=val,withcomma`，它将导致错误，因为它尝试解析 `withcomma` 作为第二个注释。因此，除非您依赖逗号作为分隔符，否则此更改不应影响您。否则，您需要为每个值多次提供选项，即 `--annotation key1=val1 --annotation key2=val2`。
