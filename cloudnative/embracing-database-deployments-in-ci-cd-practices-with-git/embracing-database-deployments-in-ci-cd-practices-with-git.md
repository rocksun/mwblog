<!--
# 拥抱 CI/CD 实践中的数据库部署与 Git
https://cdn.thenewstack.io/media/2023/10/2179b395-workflows-1024x682.jpg
Image from Monster Ztudio on Shutterstock
 -->

译自 [Embracing Database Deployments in CI/CD Practices with Git](https://thenewstack.io/embracing-database-deployments-in-ci-cd-practices-with-git/) 。

数据库一直未能很好地集成到 CI/CD 的工具环境中，但是应用类似 Git 的概念可以提供帮助。

想象你正在星巴克最繁忙的时候在柜台工作。柜台后的每个区域都被设计用来优化不同商品的制作：食物、冷饮和热饮。但是太多流动的环节，你经常会遗失订单票据，整个过程明显混乱。

这让我想起数据库 DevOps 和 CI/CD 的工具环境。像 Jenkins、GitHub Actions、CircleCI 和 Spinnaker 等工具的出现使代码变更的构建、测试和部署过程变得顺畅。同时，像 [Kubernetes](https://roadmap.sh/kubernetes) 和 Docker 这样的容器和编排技术使隔离你的应用、推送变更以及按需扩展而不影响其他环境变得更简单。

即使有这些进步，数据库仍未能很好地集成到 [CI/CD](https://thenewstack.io/ci-cd/) 的工具环境中。

这是因为将[数据库](https://thenewstack.io/data/)纳入模式部署不同于应用代码管理。由于数据库的有状态特性，您面临不可逆的数据损坏和一致性问题的风险。

一些工具专门设计用于使数据库变更管理更顺畅。然而，为数据库管理额外的 CI/CD 工具以及为前端代码管理设计的工具会带来复杂性。由于这种复杂性，您很可能会遇到版本问题、复杂的回滚机制，具有讽刺意味的是，这与 CI/CD 的目的相反，会导致缓慢和有风险的部署。

## 数据库、版本控制和 Git

对于数据库变更管理，应用 Git 类似的理念可以帮助团队避免 CI/CD 工具环境的复杂度，同时将数据库融入持续集成和持续交付管道。

以下是关于现代数据库应如何设计以集成 Git 组件到 CI/CD 工作流程中的一些观察。

### 为数据库创建测试环境和分支功能

在 Git 中，分支用于管理对应用程序代码的更改。但是数据库模式部署通常不纳入这种版本控制。因此，开发和运维团队需要投入额外精力来管理模式变更，或者创建测试环境以在部署前测试变更。

以下是一些现有的做法:

- 使用 Flyway 或 Liquibase 等工具来管理模式版本。
- 使用蓝绿部署，旋转一个隔离的(绿色)实例来测试模式变更，不影响生产(蓝色)环境。
- 从概念上，旋转整个应用程序的隔离实例，包括数据库和模式。
- 使用一组自定义脚本来管理不同版本的数据库。

但是这些做法往往都会带来运维管理的额外开销。随着需要更多的编排，它们引入了比预期更高的复杂度。分阶段环境通常会过时，需要频繁重建。尽管对某些用例来说可以接受，但对许多团队来说维护起来昂贵且乏味。

但是存在另一种选择。在 Git 中，分支用来简化团队对单个代码库的协同修改。如果数据库也能利用这种分支功能该多好？

类似 [PlanetScale](https://planetscale.com/docs/concepts/branching) for MySQL 这样的数据库为分支提供了开箱即用的功能，无需额外的编排或维护开销。模式变更成为一个更贴近数据库的流程，不再需要配置和管理另一个工具或启动全新的环境进行测试。

这种功能通常是通过生成与生产环境模式镜像的隔离数据库实例实现的，有时也会镜像数据。就像 Git 分支在中心代码库中创建新的部署路径，生产数据库在生产分支上，可以作为开发和测试分支的基础。测试分支的变更通过后，可以安全地合并回生产分支。

![](https://cdn.thenewstack.io/media/2023/10/9c4e86df-image1a-e1696272123577.jpg)

数据库分支最大限度地减少了额外资源启动测试环境的需要，同时加速了构建/测试过程。

### 自动化模式部署和 Git

应用程序变更通常需要对应的数据模式变更。如果可以通过简单地合并相关应用变更的拉取请求(Pull Request)来自动化部署模式变更，那该多好啊？

通过 [GitHub Actions](https://docs.github.com/en/actions/quickstart) 或其他 CI/CD 提供商，可以实现利用 Git 的自动化方案。

利用这个 GitHub 原生工具，可以创建自定义工作流，更轻松地构建、测试和部署代码变更。在代码部署的基础上，可以创建自定义工作流程来简化代码和模式变更过程。例如，一旦创建拉取请求，可以启动 GitHub Actions workflow，创建数据库分支，应用模式变更，并在数据库分支上运行测试，确保变更符合预期。

执行这一流程的 YAML 文件大概如下：

```
name: Automate Schema Deployment
on:
  pull_request:
    types: [opened， reopened]

jobs:
  build:
    runs-on: ubuntu-latest
    env:
      DB_SERVICE_TOKEN_ID: ${{ secrets.DB_SERVICE_TOKEN_ID }}
      DB_SERVICE_TOKEN: ${{ secrets.SERVICE_TOKEN }}

    steps:
    - name: Checkout
      uses: actions/checkout@v3

    - name: Deploy to production
      run: npm run deploy
```

需要配置工作流程，定义作业，设置数据库连接权限，并随时间维护。

另一方面，数据库提供商也可以创建预定义的 GitHub Actions 以便于集成到 CI 流程。能够内在地与自动化集成的数据库，可以使这些流程更贴近现代软件交付实践。

假设这样的场景：

应用由 Rails 开发，运行在 PlanetScale 的 MySQL 数据库上。需要在用 `users` 表加入一个新字段 `address`，并有一个包含代码修改的拉取请求。该请求包含后端迁移和模式变更文件。大致如下:

```ruby
# db/migrate/20230830123456_add_address_to_users.rb

class AddAddressToUsers < ActiveRecord::Migration[6.0]
  def change
    add_column :users， :address， :string
  end
end
```

当创建这个拉取请求时，GitHub Actions 会启动 workflow，创建分支，并在 PlanetScale 的 MySQL 打开一个匹配的部署请求。团队审查后，接受变更，并在 GitHub 中合并拉取请求。

通过在 GitHub 中简单合并拉取请求，功能就可以构建并部署到应用，数据库模式也跟着变更。模式差异会作为评论添加到 GitHub 拉取请求中进行审查，PlanetScale 也准备好帮助回滚此次模式迁移，防止出现问题。

将模式变更流程最小化到这一程度，可以显著简化与推送应用代码变更相符的模式变更流程:

1. 在 GitHub 中打开拉取请求
2. 在迁移文件中定义模式变更
3. 在 GitHub 中合并拉取请求以应用变更到应用和数据库

在数据库提供商的维护和指导下，这种全面的工作流可以平滑模式变更所带来的困难。可以利用现有的工具(GitHub 和集成的数据库)开箱即用地获得这种功能。

### 版本控制、回滚和在线模式变更

我们都经历过在不小心删除或错误修改表、列或索引后感到害怕的时刻。如果无法轻松恢复这些变更，特别是引入了重大问题时，那就非常可怕了。从备份恢复可能需要数小时或数天。

和 Git 代码回滚类似，数据库模式也应该可以回滚，以修复引入的错误、性能问题等。如果不正确的模式变更被合并，模式回滚可以恢复模式到之前的版本。理想情况下，即使数据库活跃运行也可以执行这种回滚。

可以通过第三方工具获得部分这种功能。但是数据库内置在线模式变更实际上可以提供解决方案。

简而言之，在线模式变更逻辑是:

1. 创建空的影子表映射生产环境模式
2. 在影子表上应用模式变更
3. 从生产表同步数据到影子表
4. 用影子表替换生产表

[在线模式变更](https://planetscale.com/docs/learn/how-online-schema-change-tools-work)可以在不锁表的情况下测试和合并变更。有不同的开源命令行工具可以实现，但并非都支持回滚变更。

可以用 `gh-ost`(GitHub 开发)或 `pt-online-schema-change`(Percona Toolkit) 实现通用的在线模式变更。但是这两者在迁移完成后都会终止，丢失关于迁移的信息，无法在不损失数据的情况下回滚已部署的变更。

[Vitess](https://vitess.io/) 可能是解决方案。它是一个 YouTube 开发的开源数据库管理和中间件技术。通过 Vitess，可以使用“在线”策略运行 DDL 模式变更。这是通过 Vitess 的 [VReplication](https://vitess.io/docs/17.0/reference/vreplication/vreplication/) 特性实现的。这样就可以进行带回滚功能的在线模式变更，提供比替代方案更好的版本控制。

VReplication 使用 [MySQL GTID](https://dev.mysql.com/doc/refman/8.0/en/replication-gtids-concepts.html) 来精确记录所有迁移。即使迁移完成后，它也可以通过持续的数据更新保持旧版本的模式同步。因此，使用 SQL 接口可以在完成后的 24 小时内轻松回滚最后的成功迁移:

```
REVERT VITESS_MIGRATION <uuid>;
```

这样可以快速创建回滚迁移，不需要复制表数据。模式变更可以回滚到原始状态，通常不会丢失数据。

这需要实现和维护 Vitess，且特定于 MySQL。[PlanetScale](https://planetscale.com/) 的 MySQL 数据库都内置在 Vitess 上运行，可以开箱即用地获得这种功能。

对于非 MySQL 用户，一些数据库也提供了部分在线模式变更和数据恢复功能，但是可能需要从备份恢复，存在额外资源消耗和潜在停机时间。

人为错误不可避免。回滚功能对数据库 CI/CD 流程至关重要。选择具备此功能的数据库，可以避免长时间停机，对用户无感知地平滑进行部署。

## 投资前沿的数据库解决方案

有远见的公司正在投资前沿的数据库解决方案。能够将 Git 的理念集成到数据库变更管理中的数据库，可以显著简化团队对数据的管理。未来不是一组复杂的 DevOps 工具隔离出数据库，而应与开发者熟悉的 Git 工作流程集成，实现平稳的变更管理过程。
