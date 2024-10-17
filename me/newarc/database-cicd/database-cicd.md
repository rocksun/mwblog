
<!--
title: 通过Migrate实现数据库的CI/CD
cover: ./cover.jpg
-->

这个 [NewArc](https://yylives.cc/tag/newarc/) 系列中我会分享一些新一代企业应用系统中的可以采用的框架、架构和工具。在前一篇”[无处安放的代码-重读《企业应用架构模式》](https://yylives.cc/2024/09/11/code-without-a-place-to-be-put/)“我聊了一下企业架构模式的意义。今天先从一个简单的话题，介绍一个可以帮助我们实现数据库 CI/CD 的工具 Golang Migrate。

这里先说一下我选择工具的一些策略。首先，我会选择开源许可证比较宽松的工具。这样我们可以有更大的发挥空间。第二，我会尽量选择 Go 语言开发的工具。这是因为 Go 语言几乎成为云原生工具开发的标准语言，选择 Go 语言开发的工具，工具的部署会更加精简，也有可能轻松的组合出我们自己的工具。第三，我会尽量避免选择那些对流程限制比较多的工具。这些工具因为固化了许多流程，虽然会带来一定的便利，但是无法适应更多的场景。关于这个话题，以后可能会有更多的分享。

市场上已经有了许多数据库迁移的工具，有老牌的 [flyway](https://github.com/flyway/flyway) 和 [Liquibase](https://github.com/liquibase/liquibase)，这两个工具都有 10 几年的历史，使用 Java 开发。

随着 DevOps 的发展，新一代的工具引入了一些的理念，例如数据库的 CI/CD、Schema as Code 和 Database as Code 等等，这些工具包括 [Bytebase](https://github.com/bytebase/bytebase) 和 [Atlas](https://github.com/ariga/atlas)， 这两个工具都是使用 Go 语言开发的，非常的强大，但是这两个工具的许多实用功能只存在于商业版或者云版，对于规模比较大的企业来说，完全采用这两个工具以后可能会面临比较多的限制。所以，我们考虑先从 [golang migrate](https://github.com/golang-migrate/migrate) 开始，以后有机会再介绍其他工具。

## 安装 golang-migrate

可以到 migrate 的官网下载对应平台的二进制文件：

- [https://github.com/golang-migrate/migrate/releases](https://github.com/golang-migrate/migrate/releases) 

然后将压缩包中的 migrate 文件复制系统 PATH 中。执行 `migrate -version` 命令可以看到安装成功。

## 创建迁移文件

下面我们来演示一下 migrate 的使用流程。首先是创建迁移文件。

在我们的测试目录中，使用以下命令创建迁移文件：

```bash
migrate create -ext sql -dir migrations create_users_table
migrate create -ext sql -dir migrations add_products_table
migrate create -ext sql -dir migrations add_orders_table
```

> 如果我们不使用 -seq 参数，会使用时间戳数字作为文件名前缀，这个用法可能会更方便。

这将在 `migrations` 目录下创建六个文件：

- 20241017145536_create_users_table.up.sql
- 20241017145536_create_users_table.down.sql
- 20241017145543_add_products_table.up.sql
- 20241017145543_add_products_table.down.sql
- 20241017145546_add_orders_table.up.sql
- 20241017145546_add_orders_table.down.sql

## 编写迁移脚本

编辑创建的文件，添加相应的 SQL 语句：

`20241017145536_create_users_table.up.sql`:

```sql
CREATE TABLE users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(255) NOT NULL,
    email VARCHAR(255) NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```

`20241017145536_create_users_table.down.sql`:

```sql
DROP TABLE IF EXISTS users;
```

`20241017145543_add_products_table.up.sql`:

```sql
CREATE TABLE products (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    price DECIMAL(10, 2) NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```

`20241017145543_add_products_table.down.sql`:

```sql
DROP TABLE IF EXISTS products;
```

`20241017145546_add_orders_table.up.sql`:
```sql
CREATE TABLE orders (
    id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT,
    product_id INT,
    quantity INT NOT NULL,
    total_price DECIMAL(10, 2) NOT NULL,
    order_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (user_id) REFERENCES users(id),
    FOREIGN KEY (product_id) REFERENCES products(id)
);
```

`20241017145546_add_orders_table.down.sql`:

```sql
DROP TABLE IF EXISTS orders;
```

## 执行迁移

为了测试，我们可以使用 Docker 或 Podman 启动一个 MySQL：

```bash
docker run --rm -d --name migrate-demo -p 3306:3306 -e MYSQL_ROOT_PASSWORD=pass -e MYSQL_DATABASE=migrate mysql
```

使用以下命令应用迁移：

```bash
migrate -path ./migrations -database "mysql://root:pass@tcp(localhost:3306)/migrate" up
```

执行以下命令，可以显示创建的表：

```bash
docker exec -it migrate-demo mysql -u root -ppass -e "USE migrate; SHOW TABLES;"
```

这个命令将按顺序应用所有迁移。如果您只想应用特定数量的迁移，可以在 `up` 后面加上数字，例如：

```bash
migrate -path ./migrations -database "mysql://root:pass@tcp(localhost:3306)/migrate" up 1
```

这将只应用第一个迁移。

## 查看迁移状态

要查看当前的迁移状态，使用：

```bash
migrate -path ./migrations -database "mysql://root:pass@tcp(localhost:3306)/migrate" version
```

这将显示当前应用的迁移版本。

## 回退迁移

如果需要回退迁移，可以使用 `down` 命令：

```bash
migrate -path ./migrations -database "mysql://root:pass@tcp(localhost:3306)/migrate" down
```

这将回退最后一个应用的迁移。如果要回退多个迁移，可以在 `down` 后面加上数字，例如：

```bash
migrate -path ./migrations -database "mysql://root:pass@tcp(localhost:3306)/migrate" down 2
```

这将回退最后两个迁移。

## 其他命令说明

前面的 up 和 down 命令都是指定更新的数量，我们可能用的更多的是更新到特定版本，这时使用 goto 命令：

```bash
migrate -path ./migrations -database "mysql://root:pass@tcp(localhost:3306)/migrate" goto 20241017145543
```

## 注意事项

1. 始终在应用到生产环境之前在测试环境中测试你的迁移脚本。
2. 使用版本控制系统（如 Git）来管理你的迁移脚本。
3. 在执行迁移之前备份数据库是一个好习惯。
4. 如果在生产环境中使用，请确保有适当的权限控制和安全措施。
5. golang-migrate 工具会在数据库中创建一个 `schema_migrations` 表来跟踪已应用的迁移。

通过使用 golang-migrate，您可以更方便地管理和应用数据库迁移，特别是在团队协作的环境中。

## 总结

最后，可以看到，golang-migrate 工具还比较简单，还需要自己编写 SQL 脚本，但是它的优点是非常的轻量级，可以很方便的组合成自己的工具。下一篇文章中，我会介绍一下如何结合 migrate 和 atlas，实现 SQL 变更脚本的自动生成。





