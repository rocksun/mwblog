<!--
title: 使用MCP Toolbox for Databases访问数据库
cover: https://github.com/googleapis/genai-toolbox/raw/main/docs/en/getting-started/introduction/architecture.png
summary: 本文介绍如何使用开源的 MCP Toolbox for Databases，通过 YAML 配置将其集成到 VSCode Copilot。这使得用户能用自然语言查询数据库，或自定义工具执行精确 SQL，从而简化数据库访问。
-->

本文介绍如何使用开源的 MCP Toolbox for Databases，通过 YAML 配置将其集成到 VSCode Copilot。这使得用户能用自然语言查询数据库，或自定义工具执行精确 SQL，从而简化数据库访问。

使用自然语言访问数据库已经有了许多成功的案例，AI很擅长完成这种自然语言与机器语言的转换工作。随着 MCP 的发展，肯定有不少这样的数据库 MCP Server。

MCP Toolbox for Databases 是一个用于数据库的开源 MCP 服务器。它通过处理连接池、身份验证等复杂性，使您能够更轻松、更快速、更安全地开发工具。

下面是一个简单的试用。

到[下载](https://github.com/googleapis/genai-toolbox/releases)页面直接下载 Toolbox 的二进制包，然后将其路径添加到系统 PATH 环境变量中。

然后，在你的项目根目录下新建一个 `mysql.yaml` 文件，内容为：

```yaml
sources:
  my-mysql-source:
    kind: mysql
    host: your-mysql-host
    port: 3306
    database: mysql
    user: root
    password: your-mysql-password
tools:
  execute_sql_tool:
    kind: mysql-execute-sql
    source: my-mysql-source
    description: Use this tool to execute sql statement.
```

下面我会为我的 VSCode Copilot 中添加一个 MCP Server，即在项目的目录中保存 `.vscode/mcp.json` 为：

```json
{
    "servers": {
    "mysql-mcp-server": {
      "type": "stdio",
      "command": "toolbox",
      "args": [
              "--tools-file",
              "D:\\learns\\ai\\toolbox-mcp\\mysql.yaml",
              "--stdio"
          ]
    }
   }
}
```

然后在 Copilot 的 Chat 界面，选择 Agent 模式，看看有没有加载 mysql-mcp-server，如果没有，可以点击重启，应该可以看到增加了这个 MCP Server。

在 Agent 模式下，我提问：

```
我的数据库实例中哪个数据库的表最少？
```

Copilot 问我是否执行 `execute_sql_tool`，输入为：

```json
{
  "sql": "SELECT table_schema, COUNT(*) AS table_count FROM information_schema.tables WHERE table_type = 'BASE TABLE' GROUP BY table_schema ORDER BY table_count ASC LIMIT 1;"
}
```

我确认执行后结果为：

```json
{"TABLE_SCHEMA":"sys","table_count":1}
```

Copilot 告诉我：

```
你的数据库实例中，表最少的数据库是 sys，只有 1 个表。
```

通过 Toolbox 还可以自定义 Tool， 下面就是官方的一个例子：

```yaml
sources:
  my-pg-source:
    kind: postgres
    host: 127.0.0.1
    port: 5432
    database: toolbox_db
    user: ${USER_NAME}
    password: ${PASSWORD}
tools:
  search-hotels-by-name:
    kind: postgres-sql
    source: my-pg-source
    description: Search for hotels based on name.
    parameters:
      - name: name
        type: string
        description: The name of the hotel.
    statement: SELECT * FROM hotels WHERE name ILIKE '%' || $1 || '%';
```

这样可以精确控制一些查询。