## TL;DR

不要直接从未打包的 Helm 图表安装/模板，因为 Helm CLI 在打包和依赖项方面存在许多错误，尤其是错误号 [helm/helm #11484](https://github.com/helm/helm/issues/11484)，这会导致意外行为。

此外，如果您的用户使用您打包的 Helm 图表，那么您应该测试打包的 Helm 图表，反之亦然。

## 目录

## 简介

经验法则：

`您的测试环境应尽可能接近生产环境`

以确保软件正常运行。

当您将软件作为 SaaS 运行时，这条规则至关重要，当您向客户交付产品工件时，这条规则更加重要。

您可能知道这条规则，但有时您会想，

`这只是一点偏差。会有什么影响呢？` 实际上，它

可能会产生很大影响 😁

## 问题

在我的案例中，我使用的是 [基于主干的开发](https://trunkbaseddevelopment.com/)，

并且每次拉取请求都会构建更改并将其部署到测试

环境。

我维护一个上游 Helm 图表，我的错误是在 CI 管道中部署了未打包的 Helm 图表（直接从图表目录部署，跳过打包步骤）。这基本上违反了上述规则。

后来，我发现客户报告了一些意外行为，经过调查，我发现 Helm CLI 在打包步骤中存在许多错误。

好吧，Helm CLI 在打包步骤中处理依赖项时存在很多错误。例如 [#11484](https://github.com/helm/helm/issues/11484)，[#12954](https://github.com/helm/helm/issues/12954)，[#13214](https://github.com/helm/helm/issues/13214) 等等。

我同时遇到了两个错误，Helm 会 `合并` 来自同一存储库的相同图表，即使它们位于不同的别名下！

## 示例

让我们看看实际情况... 以下是一个示例（使用 Helm CLI 版本 [v3.15.1](https://github.com/helm/helm/releases/tag/v3.15.1) 执行，该版本于 2024 年 5 月发布）：

```yaml
# my-chart/Chart.yaml
name: my-chart
version: 1.0.0
appVersion: 1.0.0
dependencies:
- name: postgresql
  alias: psql-14
  repository: https://charts.bitnami.com/bitnami
  version: 14.x.x
- name: postgresql
  alias: psql-13
  repository: https://charts.bitnami.com/bitnami
  version: 13.x.x
```

如果您从未打包的目录安装/模板化该图表，一切都会按预期工作：

```bash
$ helm dependency update
$ helm dependency build
$ helm template . | grep -o "Source: my-chart/charts/psql-../" | sort | uniq
Source: my-chart/charts/psql-13/
Source: my-chart/charts/psql-14/
```

但是，如果您尝试打包它，您将看到一个名为 `postgres` 的单个

**弗兰肯斯坦** 包，其中包含来自 Bitnami 图表 `postgresql/13.x.x` 和

`postgresql/14.x.x` 的一些文件 🤯

在许多情况下（取决于图表，它甚至可能无法渲染并显示错误）。

```bash
$ helm dependency update
$ helm dependency build
$ helm package .
$ helm template my-chart-1.0.0.tgz | grep -o "Source: my-chart/charts/psql-../" | sort | uniq
Error: template: my-chart/charts/postgresql/templates/networkpolicy-egress.yaml:6:18: executing "my-chart/charts/postgresql/templates/networkpolicy-egress.yaml" at <.Values.networkPolicy.enabled>: nil pointer evaluating interface {}.enabled Use --debug flag to render out invalid YAML
```

## 解决方法

在 Helm CLI 中修复该问题（问题号 [#11484](https://github.com/helm/helm/issues/11484)）之前，唯一

可用的解决方法是为每个依赖项使用不同的名称或不同的存储库。

```yaml
dependencies:
- name: postgresql
  alias: psql-14
  repository: https://charts.bitnami.com/bitnami
  version: 14.x.x
# 我在这里创建了 PostgreSQL v13 Helm 图表的本地副本。
- name: postgresql
  alias: psql-13
  repository: "file://../postgresql-13"
  version: 13.x.x
```

## 结论

这篇文章并没有告诉您不要使用未打包的 Helm 图表，而是强调了测试用户将使用什么的重要性。如果您的用户使用您打包的 Helm 图表，那么您应该测试打包的 Helm 图表，反之亦然。

这很烦人，但至少比 [#12488](https://github.com/helm/helm/issues/12488) 中的错误要好，该错误

已经存在两年多（该问题是在 2022 年报告的，

Helm 维护人员进行了部分修复，另一半在 [#12488](https://github.com/helm/helm/issues/12488) 中）。

无论如何... 祝您 Helm 使用愉快！（但我仍然更喜欢 [Kustomize](https://tech.aabouzaid.com/search/label/Kustomize)

TBH 😂)