
<!--
title: 使用数据库编程在PostgreSQL上构建石头剪刀布游戏
cover: https://cdn.thenewstack.io/media/2024/08/c473610a-fingers-149295_1280.png
-->

多年来，数据库编程已成为一种失传的艺术。

> 译自 [Build a Rock, Paper, Scissors Game on PostgreSQL With Database Programming](https://thenewstack.io/build-a-rock-paper-scissors-game-on-postgresql-with-database-programming/)，作者 Rotem Tamir。

现代[数据库](https://thenewstack.io/data/) 是持久、高效且可编程的数据存储库，使它们成为构建应用程序的[超级强大环境](https://thenewstack.io/how-to-run-databases-in-kubernetes/)。然而，近年来，许多数据库功能，如函数、触发器和物化视图，已经过时。

本文重新审视了这种范式，鉴于新的发展，并展示了如何通过创建一个在[PostgreSQL](https://thenewstack.io/postgresql-takes-a-new-turn/) 实例上运行的完全可用的“[石头剪刀布](https://en.wikipedia.org/wiki/Rock_paper_scissors)”游戏，来构建一个以数据库为中心的应用程序，而不会牺牲现代软件工程原则。

## 为什么函数、触发器和视图很少使用？

现代数据库不仅仅是一个带有附加查询引擎的存储层。使用[触发器](https://en.wikipedia.org/wiki/Database_trigger)、[函数](https://en.wikipedia.org/wiki/User-defined_function#Databases)、[存储过程](https://en.wikipedia.org/wiki/Stored_procedure)、[约束](https://en.wikipedia.org/wiki/Relational_database#Constraints) 和[视图](https://en.wikipedia.org/wiki/View_(SQL))，可以构建整个应用程序，而无需离开数据库。那么为什么现代软件工程团队通常只使用其中的一小部分呢？

作为一个年轻的开发者，我周围的人都告诉我，使用这些功能是一种过时的做法，属于 DBA 自由漫游和单体架构统治世界的古代时代。我被教导说，现代软件应该有明确的关注点分离——业务逻辑属于应用程序，存储层应该被视为一个“存储库”——负责提供持久存储和满足查询。

此外，测试[数据库逻辑](https://thenewstack.io/heres-when-to-use-write-ahead-log-and-logical-replication-in-database-systems/) 是一件痛苦的事情，它会降低我们获得良好测试覆盖率和从 CI 管道中获益的努力。部署这些更改也会很丑陋，降低我们使用 CD 自动化交付的努力。

简而言之，数据库编程被许多人视为几乎与我们行业中现代敏捷和 DevOps 运动正在酝酿的创新背道而驰。

## 将所有内容推送到应用程序的隐藏成本

将所有业务逻辑推送到应用程序层并将数据库视为纯粹的“数据存储库”有其优势，这是肯定的。但是，让我们考虑一下这种设计原则的一些（并不那么）隐藏的成本：

### 延迟和资源利用率

后端服务器端点通常执行多个查询以满足用户请求。每个这样的请求都涉及序列化请求、进行网络调用、等待数据库处理它、从网卡读取结果、解析结果，以及通常将每个记录映射到内存中的对象。

将应用程序逻辑推回到数据库中可以消除代价高昂的往返行程，从而降低整体资源利用率和端点延迟。

### 原子性和一致性的损失

现代数据库，如 PostgreSQL，非常擅长使用其[ACID 属性](https://en.wikipedia.org/wiki/ACID) 来维护操作的原子性和结果数据的 一致性。

一旦您的应用程序被拆分为两个通过网络通信的组件（例如服务器和数据库），您就必须处理在*分布式系统*中维护正确性的挑战，从而有效地放弃了现代关系数据库免费提供的许多功能。

一个典型的例子是维护数据库更改的一致、正确和持久的审计日志。这项任务使用[触发器函数](https://wiki.postgresql.org/wiki/Audit_trigger) 可以轻松实现，但在应用程序层实现时会变得更加困难。

为了维护正确性，请确保数据库写入仅来自应用程序（包括可能没有审计逻辑的旧版本）。其次，为了确保一致性，请确保写入审计表始终与写入主实体表在同一个事务中完成。

当然，这里的主要成本是结果系统和代码库的复杂性，可以使用触发器（本机数据库解决方案）大大降低。

### 安全性

现代应用程序通常需要执行复杂的访问控制规则，以确保敏感数据仅供授权用户访问。传统上，此责任落在应用程序层，在执行任何数据操作之前，都会检查用户权限。但是，这种方法会导致安全漏洞，并增加代码库的复杂性，因为访问控制逻辑必须在所有应用程序部分中认真实施和维护。

PostgreSQL 和 Microsoft SQL Server 提供类似的 [行级安全 (RLS)](https://wiki.postgresql.org/wiki/Row-security) 功能，提供了一种强大的解决方案来应对这一挑战，允许您直接在数据库中执行访问控制策略。RLS 使您能够定义安全策略，根据用户的角色或其他属性过滤用户可以访问的行，确保未经授权的用户无法读取或修改他们不应该访问的数据。

通过将访问控制策略执行转移到数据库，我们可以消除应用程序开发的复杂性和维护成本，降低安全风险，并实现更好的合规性。

## 数据库编程正在卷土重来

近年来，我观察到我们行业中的许多工程师和架构师越来越意识到完全避免数据库编程的成本。许多人正在寻找更好的方法将高级数据库功能集成到他们的应用程序中。

这种趋势最明显的例子是两个广受欢迎的开源项目的成功：Hasura 和 Supabase。

**Hasura** 是一款实时 GraphQL 引擎，它可以立即在新的或现有的 Postgres 数据库上为您提供 GraphQL API。利用触发器、函数和 RLS（行级安全），Hasura 使开发人员能够构建高性能、可扩展且安全的应用程序，而无需编写样板后端代码。它与您的数据库模式无缝集成，允许您直接在数据库中定义复杂的业务逻辑，并简化维护。

**Supabase** 提供了一个使用 PostgreSQL 的开源 Firebase 替代方案，并利用 PostgREST 提供即时 API、身份验证和实时功能。通过将逻辑推送到数据库，Supabase 使开发人员能够轻松地创建功能强大的应用程序，而无需付出太多努力。PostgreSQL 的复杂查询、数据转换和访问控制功能确保了性能和安全性。

Hasura 和 Supabase 都展示了拥抱数据库编程的力量和效率。为组织提供基于数据库的“即时”后端 API，可以实现将应用程序业务逻辑推回到数据库的架构，从而无需自定义数据库样板代码。

当然，您不必选择将应用程序逻辑专门放在应用程序或数据库中。在某些情况下，完全“无后端”应用程序可能有效。但是，在实践中，将某些逻辑构建到纯应用程序/后端代码中，并将责任委托给数据库来处理其他部分，这完全是可以的。出于这个原因，Supabase 提供了 [边缘函数](https://supabase.com/docs/guides/functions) 作为其平台的一部分，就像 Hasura 提供 [操作和远程模式](https://hasura.io/learn/graphql/hasura/custom-business-logic/) 一样。

## 数据库模式即代码：数据库代码需要合适的工具

回顾一下反对将业务逻辑推送到数据库的论点，其中许多论点归结为缺乏足够的工具和既定策略，将它们与现代软件工程实践（如自动化测试、CI/CD 等）集成。

有人认为，使用数据库不像使用代码那样健壮。但如果它可以呢？

近年来，我们的行业似乎认为“X 即代码”是一个好主意。简而言之，“X 即代码”运动是关于以声明方式描述系统的期望状态（无论是基础设施、配置还是模式），然后让工具强制执行该状态。

那么，为什么将事物描述为代码如此棒呢？以下是一些原因：

- 代码可以进行版本控制。这意味着您可以跟踪系统随时间的变化，轻松比较状态，并在需要时回滚。
- 机器可以理解代码。作为正式语言，机器可以处理、分析和执行代码。
- 代码可以进行测试和验证。通过使用软件测试范式，您可以确保您的系统以自动化的方式按预期运行。
- 代码可以共享和重用，使我们能够在项目和团队之间传递成功的想法和实现。
- 代码拥有庞大的生产力工具生态系统。通过使用代码，您可以利用软件工程师多年来开发的工具和实践。


[Atlas](https://atlasgo.io) 是一款数据库 Schema-as-Code 工具（完全披露：我是其作者之一），旨在使工程师能够将现代软件工程原理应用于数据库设计。Atlas 有时被称为“数据库的 Terraform”，它提供了一个声明式 API 用于管理数据库资源，以及一个用于编写和运行测试的测试框架。

在下一节中，我将展示 Atlas 如何弥合可能阻止某些团队充分利用数据库编程来处理其工作负载的差距。

## 在您的 PostgreSQL 上玩石头剪刀布

### 设置

为了演示如何使用数据库 Schema-as-Code 将现代软件工程原理应用于数据库编程，让我们构建一个有趣的示例应用程序——一个石头剪刀布游戏（以下简称 RPS），它将在 PostgreSQL 数据库上直接运行。

让我们从运行一个本地 Postgres docker 容器开始，该容器将充当我们的目标数据库：

```
docker run --rm -e POSTGRES_PASSWORD=pass --name rps -p 5432:5432 -d postgres:16
```

接下来，下载最新版本的 Atlas：

```
curl -sSf https://atlasgo.sh | sh
```

创建一个名为 atlas.hcl 的文件来存储我们的项目配置：

```
env "local" {
  url = "postgres://postgres:pass@localhost:5432/postgres?search_path=public&sslmode=disable"
  src = "file://schema.sql"
  dev = "docker://postgres/16/dev?search_path=public"
}
```

此文件定义了一个“local”环境，该环境将用于开发我们的应用程序和管理我们的本地数据库（在 url 属性中定义）。此外，我们定义了项目的 [开发数据库](https://atlasgo.io/concepts/dev-database)，这是一个本地、空的 Postgres 实例，Atlas 用于各种计算。

### 我们的业务逻辑

让我们开始构建我们的应用程序！

创建一个名为 schema.sql 的文件；此文件将包含我们所有数据库资源和逻辑：

```sql
-- Create enum type "move"
CREATE TYPE "move" AS ENUM ('rock', 'paper', 'scissors');
 
-- Create enum type "result"
CREATE TYPE "result" AS ENUM ('win', 'lose', 'draw');
```

首先定义业务域的核心部分，一个 move 枚举，对应于玩家可以执行的不同动作（石头、剪刀或布），以及一个 result 枚举，包含任何特定游戏回合的各种可能结果。

让我们通过运行以下命令将我们的模式应用于我们的本地数据库：

```
atlas schema apply --env local
```

Atlas 将连接到我们的本地数据库，并将期望状态（在 schema.hcl 中定义）与当前状态（一个空的 Postgres）进行比较，并发出一个计划：

```
-- Planned Changes:
-- Create enum type "move"
CREATE TYPE "move" AS ENUM ('rock', 'paper', 'scissors');
-- Create enum type "result"
CREATE TYPE "result" AS ENUM ('win', 'lose', 'draw');
 
? Are you sure?: 
  ▸ Apply
    Lint and edit
    Abort
```

让我们批准该计划以将其应用于数据库。

为了确认一切正常，请重新运行 atlas schema apply –env local：

```
Schema is synced, no changes to be made
```

Atlas 报告模式已同步，我们可以继续开发。

接下来，让我们定义游戏中逻辑的核心部分，决定谁赢得任何特定回合。使用 Postgres 函数来封装此逻辑。将以下行添加到 schema.sql：

```sql
-- Create "turn_result" function
CREATE FUNCTION "turn_result" ("player" "move", "opponent" "move") RETURNS "result" LANGUAGE plpgsql AS $$
BEGIN
  RETURN
    CASE
      WHEN player = 'rock' AND opponent = 'scissors' THEN 'win'
      WHEN player = 'rock' AND opponent = 'paper' THEN 'lose'
      WHEN player = 'paper' AND opponent = 'rock' THEN 'win'
      WHEN player = 'paper' AND opponent = 'scissors' THEN 'lose'
      WHEN player = 'scissors' AND opponent = 'paper' THEN 'win'
      WHEN player = 'scissors' AND opponent = 'rock' THEN 'lose'
      ELSE 'draw'
    END;
END;
$$;
```

### 测试我们的代码

在将此函数应用于我们的目标数据库之前，请验证它是否正常工作。Atlas 具有一个内置的数据库代码测试框架，可以为 turn_result 函数编写单元测试。创建一个名为 rps.test.hcl 的新文件：

```
test "schema" "turn_result" {
  parallel = true
  for_each = [
    {player: "rock", opponent: "rock", expected: "draw"},
    {player: "rock", opponent: "paper", expected: "lose"},
    {player: "rock", opponent: "scissors", expected: "win"},
    {player: "paper", opponent: "rock", expected: "win"},
    {player: "paper", opponent: "paper", expected: "draw"},
    {player: "paper", opponent: "scissors", expected: "lose"},
    {player: "scissors", opponent: "rock", expected: "lose"},
    {player: "scissors", opponent: "paper", expected: "win"},
    {player: "scissors", opponent: "scissors", expected: "draw"},
  ]
  log {
    message = "Testing ${each.value.player}, ${each.value.opponent} -> ${each.value.expected}"
  }
  exec {
    sql = "SELECT turn_result('${each.value.player}', '${each.value.opponent}')"
    output = each.value.expected
  }
}
```

定义一个名为 turn_result 的模式测试用例来验证我们的逻辑。请注意此测试的一些有趣之处：

- 使用 `for_each` 属性创建表格测试风格的测试用例，定义我们想要检查的不同用例。
- 为每个测试用例记录一条消息，包含输入（玩家/对手）和预期结果。
- 然后，使用来自 `for_each` 用例的值执行动态填充的 SQL 语句，并验证输出是否符合预期。
运行以下内容进行测试：

```
atlas schema test --env local
```

Atlas 打印输出：

```
-- PASS: turn_result/9 (378µs)
    rps.test.hcl:14: Testing scissors, scissors -> draw
-- PASS: turn_result/5 (4ms)
    rps.test.hcl:14: Testing paper, paper -> draw
-- PASS: turn_result/7 (4ms)
    rps.test.hcl:14: Testing scissors, rock -> lose
-- PASS: turn_result/8 (4ms)
    rps.test.hcl:14: Testing scissors, paper -> win
-- PASS: turn_result/1 (5ms)
    rps.test.hcl:14: Testing rock, rock -> draw
-- PASS: turn_result/3 (5ms)
    rps.test.hcl:14: Testing rock, scissors -> win
-- PASS: turn_result/2 (5ms)
    rps.test.hcl:14: Testing rock, paper -> lose
-- PASS: turn_result/4 (5ms)
    rps.test.hcl:14: Testing paper, rock -> win
-- PASS: turn_result/6 (5ms)
    rps.test.hcl:14: Testing paper, scissors -> lose
PASS
```
### 将结果存储在表格中

接下来，让我们创建一个新的表格来存储我们的游戏历史记录，以便我们以后可以进行一些有趣的操作。将表格定义追加到 schema.sql：

```
-- Create "games" table
CREATE TABLE "games" (
  "id" integer NOT NULL GENERATED ALWAYS AS IDENTITY,
  "player" "move" NOT NULL,
  "opponent" "move" NOT NULL,
  "result" "result" NOT NULL,
  PRIMARY KEY ("id")
);
```

让我们将新表格应用到数据库：

```
atlas schema apply --env local
```

Atlas 为我们规划了模式更改：

```
-- Planned Changes:
-- Create "games" table
CREATE TABLE "games" (
  "id" integer NOT NULL GENERATED ALWAYS AS IDENTITY,
  "player" "move" NOT NULL,
  "opponent" "move" NOT NULL,
  "result" "result" NOT NULL,
  PRIMARY KEY ("id")
);
? Are you sure?: 
  ▸ Apply
    Lint and edit
    Abort
```

选择“应用”以在我们的本地数据库上执行这些更改。

### 总结逻辑

有了 games 表格，让我们创建一个辅助函数，该函数将向用户呈现特定游戏的結果：

```

6
7
8
9
10
11
12
13
14
15
16
17
18
-- Create "render_result_text" function
CREATE FUNCTION "render_result_text" ("opponent" "move", "result" "result") RETURNS text LANGUAGE plpgsql AS $$
DECLARE
  result_text text;
BEGIN
  -- Initialize result text with opponent's move
  result_text := format('Opponent played: %s. ', opponent);
  -- Determine the result and append to result text
  IF result = 'win' THEN
    result_text := result_text || 'Result: You WIN';
  ELSIF result = 'lose' THEN
    result_text := result_text || 'Result: You LOSE';
  ELSE
    result_text := result_text || 'Result: DRAW';
  END IF;
  RETURN result_text;
END;
$$;
```

此函数将向玩家提供有关其移动、计算机的移动和结果的反馈。

为了确保此函数正常工作，让我们为其添加一个测试用例：

```
test "schema" "render_result_text" {
  parallel = true
  for_each = [
    {player: "rock", opponent: "scissors", result: "win", expected: "Opponent played: scissors. Result: You WIN"},
    {player: "rock", opponent: "paper", result: "lose", expected: "Opponent played: paper. Result: You LOSE"},
    {player: "rock", opponent: "rock", result: "draw", expected: "Opponent played: rock. Result: DRAW"},
  ]
  log {
    message = "Rendering ${each.value.player}, ${each.value.opponent}, ${each.value.result}."
  }
  exec {
    sql    = "SELECT render_result_text('${each.value.opponent}', '${each.value.result}')"
    output = each.value.expected
  }
}
```

在此测试中，我们采用了一些可能的输入组合，并确保输出正确打印出来。为了验证一切按计划进行，我们可以运行以下测试：

```
atlas schema test --env local --run render_result_text
```

请注意 `–run render_result_text` 标志，用于运行特定的一组测试，而不是整个套件。Atlas 运行测试并打印出结果：

```
-- PASS: render_result_text/3 (613µs)
&nbsp;&nbsp;&nbsp;&nbsp;rps.test.hcl:30: Rendering rock, rock, draw.
-- PASS: render_result_text/1 (6ms)
&nbsp;&nbsp;&nbsp;&nbsp;rps.test.hcl:30: Rendering rock, scissors, win.
-- PASS: render_result_text/2 (6ms)
&nbsp;&nbsp;&nbsp;&nbsp;rps.test.hcl:30: Rendering rock, paper, lose.
```

太好了，我们的代码很棒！让我们继续实现游戏的最后部分。将以下资源追加到您的 schema.hcl 文件：

```
-- Create "random_move" function
CREATE FUNCTION "random_move" () RETURNS "move" LANGUAGE sql AS $$ SELECT move FROM unnest(enum_range(NULL::move)) move ORDER BY random() LIMIT 1; $$;
-- Create "play" function
CREATE FUNCTION "play" ("player" "move") RETURNS text LANGUAGE plpgsql AS $$
DECLARE
  opponent_move public.move;
  game_result public.result;
  result_text text;
BEGIN
  -- Ensure opponent_move is assigned properly
  SELECT random_move() INTO opponent_move;
  -- Calculate the result using the turn_result function
  SELECT turn_result(player, opponent_move) INTO game_result;
  -- Insert the result into the games table
  INSERT INTO games (player, opponent, result) VALUES (player, opponent_move, game_result);
  -- Render the result text using the render_result_text function
  SELECT render_result_text(opponent_move, game_result) INTO result_text;
  RETURN result_text;
END;
$$;
```

声明一个名为 random_move 的新辅助函数，该函数代表我们的电脑对手选择一个随机的动作，以及我们游戏的首要函数：play。简而言之，当我们的用户调用 play 时，会发生以下情况：

- 对手选择一个随机的动作。
- 使用 turn_result 计算回合的结果。
- 将结果插入 games 表。
- 使用 render_result_text 函数向我们的用户返回一些优秀的反馈。

让我们编写另一个测试用例来验证我们的逻辑是否有效：

```
test "schema" "play" {
  exec {
    sql = "select play('rock')"
  }
  assert {
    sql = "select exists(select 1 from games where player = 'rock' and opponent in ('rock', 'paper', 'scissors') and result in ('win', 'lose', 'draw'))"
  }
}
```

使用 atlas schema test –env local –run play 运行测试：

```
-- PASS: play (1ms)
PASS
```

太好了，我们的逻辑有效！让我们将它应用到我们的本地数据库并试用一下。运行 atlas schema apply –env local：

```

1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
21
22
23
24
25
26
27
28
29
-- Planned Changes:
-- Create "random_move" function
CREATE FUNCTION "random_move" () RETURNS "move" LANGUAGE sql AS $$ SELECT move FROM unnest(enum_range(NULL::move)) move ORDER BY random() LIMIT 1; $$;
-- Create "play" function
CREATE FUNCTION "play" ("player" "move") RETURNS text LANGUAGE plpgsql AS $$
DECLARE
  opponent_move public.move;
  game_result public.result;
  result_text text;
BEGIN
  -- Ensure opponent_move is assigned properly
  SELECT random_move() INTO opponent_move;
 
  -- Calculate the result using the turn_result function
  SELECT turn_result(player, opponent_move) INTO game_result;
 
  -- Insert the result into the games table
  INSERT INTO games (player, opponent, result) VALUES (player, opponent_move, game_result);
  
-- Render the result text using the render_result_text function
  SELECT render_result_text(opponent_move, game_result) INTO result_text;
 
  RETURN result_text;
END;
$$;
? Are you sure?: 
  ▸ Apply
    Lint and edit
    Abort
```

### 试玩游戏

在批准计划后，让我们现在在数据库上创建一个交互式会话来试玩我们的游戏，运行：

```
docker exec -it rps psql -U postgres
```

出现一个交互式 psql 会话：

```
postgres=# select play('rock'); 
                play                 
-------------------------------------
 Opponent played: rock. Result: DRAW
(1 row)
```

太接近了。让我们再试一次：

```
postgres=# select play('rock'); 
                    play                    
--------------------------------------------
 Opponent played: scissors. Result: You WIN
(1 row)
```

太棒了，我们赢了！现在，你拥有一个完全可用的石头剪刀布游戏，它运行在你的 Postgres 数据库上。

### 使用 Schema as Code 实现现代 CI/CD

一个可以运行自动化测试并从代码中声明性地应用（即 *部署*）模式到你的数据库的工具，是构建 CI/CD 管道以自动化我们应用程序的软件交付过程的坚实基础。

为了简洁起见，我们今天不会演示 Git（或其他源代码控制系统）和 CI/CD 管道如何集成到其中。

首先，为了享受将数据库模式 *作为代码* 管理的好处，我们应该将我们的模式定义和测试文件放在源代码控制下。通过放在源代码控制下，我们的模式现在有了版本控制，并且有一个清晰的审计跟踪记录了它们是如何演变的。

其次，在 CI 阶段，我们应该使用各种自动化检查来确保任何提议的更改都能正常工作，并且不会破坏任何现有行为。一个显而易见的检查是在每次提交时运行模式测试命令。

此外，测试任何计划的模式更改是否能够成功应用至关重要。这可以通过使用现有模式的副本（直接从数据库或从我们主分支的最新提交中的模式）启动一个数据库，并将我们最近的模式应用到其中来完成，确保一切顺利运行。

最后，在部署阶段，我们可以使用 schema apply 命令自动部署我们最新的模式，就像我们在本地开发中所做的那样。

Atlas 预先打包了一套全面的 [GitHub Actions](https://atlasgo.io/integrations/github-actions)，帮助您自动化此流程。当然，现代数据库 CI/CD 是一个广泛的主题——如果您想了解更多关于 Atlas 对此问题的解决方法，请参考 [相关指南](https://atlasgo.io/guides/modern-database-ci-cd)。

## 结论

这个简短的示例演示了像 Atlas 这样的数据库模式即代码工具如何将经过验证的软件工程实践（例如将资源作为代码管理和测试）应用于数据库编程。

总之，利用现代数据库和像 Atlas 这样的工具，我们可以将强大的数据库编程集成到我们的开发工作流程中，以提高性能和安全性，同时简化我们的代码库。即使这是一个人为的例子，我希望我们的小游戏能说明拥抱数据库编程的一些好处。

多年来，数据库编程已经成为一种失落的艺术，因此我认为值得投资我们的数据库手册，以了解更多关于它们隐藏的力量。

在本文中，我们展示了 Atlas 功能的概览，这绝不是一个全面的指南。如果您想了解更多关于数据库模式即代码和 Atlas 的信息，可以在 [Atlas 文档网站](https://atlasgo.io) 上找到更完整的“Atlas 入门”指南。
