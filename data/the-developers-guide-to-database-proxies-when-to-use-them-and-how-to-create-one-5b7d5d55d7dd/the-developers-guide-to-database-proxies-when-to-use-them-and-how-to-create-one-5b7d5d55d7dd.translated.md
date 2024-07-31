# 数据库代理开发人员指南：何时使用以及如何创建
[阅读 packagemain.tech 上的原始文章](https://packagemain.tech/p/the-developers-guide-to-database)
数据库代理是应用程序和底层数据库之间的一层抽象。

想象一个高度依赖数据的复杂分布式系统，其中每个微服务或团队都单独连接到数据库（可以是共享数据库或特定/隔离的数据库）。如此复杂的平台需要集中监控、查询验证、警报、自定义分片以及更好的安全性等等。虽然您可以从数据库服务器获得很多这些功能，但实施数据库代理可能是一个更好的方法（如果您准备投资）。

使用数据库代理的主要优势在于它将数据库拓扑与应用程序层隔离开来，因此开发人员无需了解数据层的集群、节点和内部结构（当然在一定程度上）。

# 数据库代理用例
让我们深入了解数据库代理如何赋能您的开发团队、增强安全性并优化数据库性能的各种方式。

**拦截来自应用程序的 SQL 查询**并将其动态路由到正确的数据库/表（例如自定义分片）。Figma[正在做 exactly that](https://www.figma.com/blog/how-figmas-databases-team-lived-to-tell-the-scale/)使用他们的内部 Postgres 代理。**解析/分析/验证来自开发人员的 SQL 查询**并使用附加信息丰富响应。这可能有助于告诉应用程序哪些表将被弃用。**可扩展性和架构更改不会影响应用程序。**平台/数据库团队可以独立更改架构，而无需重写数百个微服务。能够透明地添加或删除数据库集群中的节点，而无需重新配置或重新启动应用程序。**执行安全策略**并执行身份验证和授权检查，以确保只有授权的客户端才能访问数据库。也可以禁止直接访问数据库。**提高数据库通信的性能**，通过集中管理连接池、利用缓存技术等。**集中式可观察性。**当应用程序使用已弃用的表时收到通知，等等。
# 何时使用数据库代理
并非所有系统都需要数据库代理，尤其是在早期阶段。以下是一般准则，说明何时可能需要它：

- 您有多个由不同学科划分的开发团队：例如多个后端团队、数据工程团队。
- 您有一个平台/数据库团队来拥有它。虽然其他团队也可以拥有它。
- 您的系统是分布式的，并且您维护着许多微服务和许多数据库。
- 您的系统数据量很大。
- 您需要更好的安全性和可观察性。
# 使用数据库代理的成本
使用数据库代理确实会带来成本：

- 数据库代理是基础设施中的一个新元素，它本身具有复杂性。
- 可能是单点故障，因此必须非常稳定且经过实战检验。
- 额外的网络延迟。
# 数据库代理类型
您可以通过几种方式部署数据库代理：

- 自定义代理服务（下面我将提供一个简单的 Go 示例）
- 托管云解决方案，例如
[Amazon RDS Proxy](https://aws.amazon.com/rds/proxy/) - Sidecars，例如
[Cyral](https://cyral.com/) - 商业和开源产品，例如
[ProxySQL](https://proxysql.com/)，或[dbpack](https://github.com/cectc/dbpack)
# 使用 Go 编写自定义数据库代理服务
现在，我们将使用 Go 实现自己的 MySQL 代理。请记住，这只是一个解释想法的实验。

我们的代理将解决一个非常简单的用例：拦截 SQL 查询并在匹配模式时重写表名。

`-- 应用程序生成的查询`
SELECT * FROM orders_v1;
-- 重写的查询
SELECT * FROM orders_v2;
实现分为两个部分：

- 将查询从客户端路由到 MySQL 服务器的基本代理。
- SQL 解析器，具有一些在发送查询之前操作查询的逻辑。
您可以在[此 Github 存储库](https://github.com/plutov/packagemain/tree/master/database-proxy)中查看完整的源代码。

# 从客户端到 MySQL 服务器的 TCP 代理
我们的 TCP 代理采用非常简单的方法实现，绝对不适合生产环境，但足以演示 TCP 传输的工作原理：

- 创建一个代理 TCP 服务器
- 接受连接
- 创建到 MySQL 的 TCP 连接
- 使用管道将字节流从客户端代理到 MySQL 服务器，反之亦然
main.go
`package main`
import (
"fmt"
"io"
"log"
"net"
"os"
)
func main() {
// 代理监听端口 3307
proxy, err := net.Listen("tcp", ":3307")
if err != nil {
log.Fatalf("无法启动代理：%s", err.Error())
}
for {
conn, err := proxy.Accept()
log.Printf("新连接：%s", conn.RemoteAddr())
if err != nil {
```go
package main

import (
	"fmt"
	"io"
	"log"
	"net"
	"os"
	"strings"
)

const (
	COM_QUERY = byte(0x03)
)

func main() {
	listener, err := net.Listen("tcp", ":3307")
	if err != nil {
		log.Fatalf("failed to listen: %s", err.Error())
	}
	defer listener.Close()
	for {
		conn, err := listener.Accept()
		if err != nil {
			log.Fatalf("failed to accept connection: %s", err.Error())
		}
		go transport(conn)
	}
}

func transport(conn net.Conn) {
	defer conn.Close()
	mysqlAddr := fmt.Sprintf("%s:%s", os.Getenv("MYSQL_HOST"), os.Getenv("MYSQL_PORT"))
	mysqlConn, err := net.Dial("tcp", mysqlAddr)
	if err != nil {
		log.Printf("failed to connect to mysql: %s", err.Error())
		return
	}
	readChan := make(chan int64)
	writeChan := make(chan int64)
	var readBytes, writeBytes int64
	// from proxy to mysql
	go pipe(mysqlConn, conn, true)
	// from mysql to proxy
	go pipe(conn, mysqlConn, false)
	readBytes = <-readChan
	writeBytes = <-writeChan
	log.Printf("connection closed. read bytes: %d, write bytes: %d", readBytes, writeBytes)
}

func pipe(dst, src net.Conn, send bool) {
	if send {
		intercept(src, dst)
	}
	_, err := io.Copy(dst, src)
	if err != nil {
		log.Printf("connection error: %s", err.Error())
	}
}

func intercept(src, dst net.Conn) {
	buffer := make([]byte, 4096)
	for {
		n, _ := src.Read(buffer)
		if n > 5 {
			switch buffer[4] {
			case COM_QUERY:
				clientQuery := string(buffer[5:n])
				newQuery := rewriteQuery(clientQuery)
				fmt.Printf("client query: %s\n", clientQuery)
				fmt.Printf("server query: %s\n", newQuery)
				writeModifiedPacket(dst, buffer[:5], newQuery)
				continue
			}
		}
		dst.Write(buffer[0:n])
	}
}

func rewriteQuery(query string) string {
	return strings.NewReplacer("from orders_v1", "from orders_v2").Replace(strings.ToLower(query))
}

func writeModifiedPacket(dst net.Conn, header []byte, query string) {
	newBuffer := make([]byte, 5+len(query))
	copy(newBuffer, header)
	copy(newBuffer[5:], []byte(query))
	dst.Write(newBuffer)
}
```

```dockerfile
FROM golang:1.22 as builder
WORKDIR /
COPY . .
RUN CGO_ENABLED=0 GOOS=linux GOARCH=amd64 go build -o proxy main.go
FROM alpine:latest
COPY --from=builder /proxy .
EXPOSE 3307
CMD ["./proxy"]
```

```yaml
services:
  proxy:
    restart: always
    build:
      context: .
    ports:
      - 3307:3307
    environment:
      - MYSQL_HOST=mysql
      - MYSQL_PORT=3306
    links:
      - mysql
  mysql:
    restart: always
    image: mysql:5.7
    platform: linux/amd64
    ports:
      - 3306:3306
    environment:
      - MYSQL_ROOT_PASSWORD=root
    command: --init-file /data/application/init.sql
    volumes:
      - ./init.sql:/data/application/init.sql
```

```sql
CREATE DATABASE IF NOT EXISTS packagemain;
CREATE TABLE IF NOT EXISTS packagemain.orders_v2 (
  id INT AUTO_INCREMENT PRIMARY KEY,
  name VARCHAR(255) NOT NULL
) ENGINE=InnoDB;
INSERT INTO packagemain.orders_v2 (name) VALUES ('order1');
```

# SQL 解析
我们的 **intercept** 函数已经可以获取字节包。了解 MySQL 包的结构很有帮助。我不会深入细节，但你可以 [在这里阅读](https://www.oreilly.com/library/view/understanding-mysql-internals/0596009577/ch04.html)。

在我们的 intercept 函数中，我们执行以下操作：

- 查找 **COM_QUERY** 客户端命令，其数字代码为 3。
- 获取原始查询。
- 进行非常基本的表重命名。

有一个很棒的包 [sqlparser](https://github.com/vitessio/vitess/tree/main/go/vt/sqlparser) 来自 YouTube 的 Vitess 项目，我们可以用它来解析 SQL 查询。但是，为了简化演示，我们将使用字符串匹配和替换。

# 运行代理并连接到它
在这里，我们连接到运行在端口 3307 上的代理，而不是 MySQL 服务器本身（端口 3306）。如你所见，我们可以使用常规的 MySQL 客户端，这简化了代理的使用。

这意味着 **orders_v1** 表被重定向到 **orders_v2**。代理日志：

`client query: select * from orders_v1;`
server query: select * from orders_v2;

# 结论
总之，数据库代理在应用程序和底层数据库之间提供了一个强大的抽象层。它通过隔离数据库复杂性来简化开发，使数据库团队能够独立进行模式更改，并通过集中式访问控制来增强安全性。虽然存在基础设施开销和潜在延迟等额外成本，但对于具有多个团队和数据密集型需求的复杂分布式系统，数据库代理可能是一项值得的投资。