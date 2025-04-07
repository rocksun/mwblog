<!--
title: 如何以最糟糕的方式编写后端：GoREST的诞生
cover: https://mostafaqanbaryan.com/static/9f5b64c8f1cfd8c12a0a9dfaaa239893/b53df/featured.png
summary: 避坑指南！PHP转Go血泪史：用Go和TDD构建RESTful API后端，我经历了什么？框架选型：Gorm、Chi、Echo，最终选择了Echo！项目结构从Golang Standard Project Layout到DDD，踩坑无数。放弃go-migrate，拥抱goose。测试从service到handler，真香！内含sqlc、docker-compose、air等云原生技术实践。
-->

避坑指南！PHP转Go血泪史：用Go和TDD构建RESTful API后端，我经历了什么？框架选型：`Gorm`、`Chi`、`Echo`，最终选择了`Echo`！项目结构从`Golang Standard Project Layout`到DDD，踩坑无数。放弃`go-migrate`，拥抱`goose`。测试从`service`到`handler`，真香！内含`sqlc`、`docker-compose`、`air`等云原生技术实践。

> 译自：[How to Write a Backend the Worst Way﹕ Creation of GoREST | by Mostafa Qanbaryan](https://mostafaqanbaryan.com/how-to-write-a-backend-the-worst-way-creation-of-go-rest/)
> 
> 作者：None



创建 [GoREST](https://github.com/mostafaqanbaryan/go-rest) 到目前为止花了一个月左右的时间（虽然我没有全职工作——我从第一次提交开始算起）。

因此，我写了这篇文章，以防止其他人犯同样的错误，这些错误花费了大量的时间和精力来修复。

## 介绍

您可能知道我是一名拥有几年经验的 PHP 开发人员。像许多 PHP 开发人员一样，我一直在使用 Laravel 并且很喜欢它。但现在我正在改变方向转向 Golang。

我预计在开始学习 Golang 时会遇到一些文化冲击，因为与使用 Laravel 的 PHP 不同，没有一个占主导地位的框架是每个人都使用的，也没有普遍接受的标准方式来构建应用程序（或者至少这是我的印象）。

因此，我将在本文中解释我是如何以最糟糕的方式使用 Go 创建 RESTful API 后端的。

如果您不想阅读整篇文章，这里是存储库：

[https://github.com/mostafaqanbaryan/go-rest](https://github.com/mostafaqanbaryan/go-rest)

## 最糟糕的方式！

正如我之前所说，我对 Go 相当陌生。显然，许多概念对我来说并不清楚。我也是第一次编写测试，因为我以前没有这样做过。

所以我决定用 Golang 和 TDD（测试驱动开发）编写一个 RESTful API 后端，以一石二鸟；天啊，我真后悔！

## 框架、路由器还是原始方式？

来自 Laravel，我最初认为我的后端需要一个框架。但是，在阅读 Golang 文档并咨询社区后，我注意到许多 Go 开发人员倾向于避免使用框架。

我以前用 PHP 编写过没有框架的不同项目，这并不糟糕。但是，PHP 缺乏许多像 Go 这样的现代语言提供的内置工具，这解释了为什么 Laravel 如此受欢迎，因为它填补了这些空白。

但是在 Golang 中，框架不是必需的。您可以轻松地编写一个没有框架的 RESTful API 后端。但我不想错过检查其中一些框架的机会。

### Gorm

[Gorm](https://gorm.io/) 是我检查的第一个框架。它是一个易于使用的 ORM，可以为您处理很多事情。

我重构了一个用 Gorm 编写的项目，我真的很喜欢它。但是在重构时，我意识到测试代码并不容易。所以，看来我未能一石二鸟。

我在骗谁呢？我更喜欢使用 `SQL`
而不是查询构建器！它更容易阅读和编写。

### Chi

[Chi](https://github.com/go-chi/chi) 是一个轻量级的、符合语言习惯的路由器，用于构建 Go HTTP 服务，是框架的理想替代品。

一开始，我实际上是从 Chi 开始的。几天后，经过一番搜索，我意识到它与 Golang 中的标准 `http` 包非常相似，并且 `Chi` 的大部分代码都合并到了 Golang 项目的核心中，这真的很棒！

但是，似乎使用 `Chi` 与标准 `http` 包相比没有任何大的优势了（[当然有中间件和分组](https://www.reddit.com/r/golang/comments/1avn6ih/is_chi_relevant_anymore/)）。

所以我决定使用其他东西。

### Echo

[Echo](https://echo.labstack.com/) 是一个高性能、可扩展、极简主义、相对较新的框架，我以前对此一无所知。
Echo 有一些我不想自己编写的功能，例如：

- 响应更容易处理。更容易编写：

```
return c.String(http.StatusOK, "Welcome")
```
  
- 而不是：

```go
w.Write([]byte("Welcome"))
return
```

- 它有很多[中间件](https://echo.labstack.com/docs/category/middleware) - 因为它与标准 `http` 包一起使用，所以编写测试很容易。只需要创建 `context` 就可以了：

```go
req := httptest.NewRequest(http.MethodPost, "/", strings.NewReader(userJSON))
req.Header.Set(echo.HeaderContentType, echo.MIMEApplicationJSON)
rec := httptest.NewRecorder()
c := e.NewContext(req, rec)
```

- Echo 包含更多我尚未检查的功能，因此请务必[阅读文档](https://echo.labstack.com/docs)。

*当然，还有其他很棒的框架和路由器，如 fiber 和 gin，并且标准 http 包也适用于这样的项目。但我决定暂时使用 Echo。*

## 项目结构

如果您使用过 Laravel，您就会知道它强制执行特定的项目结构。但是在 Go 中（或者实际上任何不使用框架的语言中），您可以随意构建您的项目……这实际上可能存在问题！

当我在重构我拥有的 `Gorm`
项目时，我找到了 [Golang 标准项目布局](https://github.com/golang-standards/project-layout)，它非常漂亮和独特，并被各种项目所遵循。

但是，存在一个问题。尽管它很棒，但它没有说明如何使用 TDD 和存储库模式编写 REST-API 后端。
一开始，我像这样创建了我的项目：

```
cmd/
web/
main.go
internal/
  entities/
    user.go
  errors/
  ...
  handlers/
  ...
  repositories/
  ...
  services/
  ...
```

我当时很开心。问题出在我想要将 repositories 注入到我的 services 中时。

如果所有的 services 都在同一个 package 中，这意味着我不能为每个 service 设置单独的 `repo` structs。

此时，你知道我没有在我的项目中实现 TDD，但我正在努力！我知道我必须改变我的项目结构。所以我决定让它更像 [DDD](https://en.wikipedia.org/wiki/Domain-driven-design)：

```
cmd/
    web/
        main.go
internal
    auth
        errors\
            ...
        http\
            ...
        repository\
            ...
        service\
            ...
    user\
        errors\
            ...
        http\
            ...
        repository\
            ...
        service\
            ...
```

现在像样了！现在我可以将具有重复名称的 repositories 注入到 services 中，并轻松地测试它们。

## 测试… 1, 2, 3?

正如我所说，我想尝试 TDD，因为当我读到 [@quii](https://twitter.com/quii) 的 [Learn Go with tests](https://quii.gitbook.io/learn-go-with-tests/) 时，我就爱上了它！我已经读过几次了，而且我永远不会厌倦阅读它。它真的很好！

但我仍然没有学会如何使用 TDD 开始编写 RESTful API 后端（因为我没有意识到 [@quii 已经在书中谈到了](https://quii.gitbook.io/learn-go-with-tests/build-an-application/http-server)）

所以我决定从基础开始。我创建了一个简单的 `main.go`、 `repository.go` 和一个 `service.go`，然后为 `service.go` 编写了一个单元测试。

这是第一个示例的样子：

```go
// user_repository_mock.go
type UserRepositoryMock struct { }
func NewUserRepositoryMock() UserRepositoryMock {
	return UserRepositoryMock{}
}
func (r UserRepositoryMock) FindByUsername(username string) (*entities.User, error) {
	return nil, errors.UserNotFound{}
}
```

```go
// service.go
type UserRepository interface {
	FindByUsername(string) (entities.User, error)
}
type UserService struct {
	repo UserRepository
}
func NewUserService(userRepository UserRepository) UserService {
	return UserService{
		repo: userRepository,
	}
}
func (s UserService) Login(username, password string) (*entities.User, error) {
	user, err := s.repo.FindByUsername(username)
	if err != nil {
		return nil, err
	}
	if password != user.Password {
		return nil, errors.PasswordIsWrong{}
	}
	return user, nil
}
```

```go
// service_test.go
func TestUserService(t *testing.T) {
	t.Run("Login not found", func(t *testing.T) {
		userRepository := repositories.NewUserRepositoryMock()
		userService := NewUserService(userRepository)
		_, err := userService.Login("test", "test")
		if !errors.Is(err, UserNotFound{}) {
			t.Fatalf("want <%v>, got: <%v>", UserNotFound{}, err)
		}
	})
}
```

我认为这是一个好的开始，但是我在 `UserRepositoryMock` 中应该做什么呢？ 在真正的 `UserRepository` 中，我针对 `database` 检查了用户。但我不知道是否应该对 `UserRepositoryMock` 做同样的事情并模拟一个 `database`？

通过在查询构建器中单独模拟每个方法，测试会很容易。例如，我可以轻松地模拟 `select` 或 `insert` 方法。但是在使用 `sqlc` 时，我在编写测试时遇到了一些挑战。

所以我不得不决定：

- 我想测试我所有的查询吗？
- 还是我想测试我的 services？

### 测试查询

永远不要这样做！测试查询或查询构建器（或者在这种情况下，`sqlc`）是一个坏主意。你可能会问为什么？以下是一些原因：

- 你正在测试一个第三方 package，而不是你的代码。
- 对于测试查询，你需要一个实际的 `database`，这使它成为一个集成测试。
- 运行集成测试很慢。

我很自豪地说，我确实为 [sqlc 创建了一个 mock driver](https://github.com/mostafaqanbaryan/go-rest/commit/864ca86d266825383151ce52f5d5c19c69831bb7#diff-47417e701aa4c04563c04211b28e891ffa5592f0ea2046e8d4c8a8cbf9aa0313)，在此之前，[为 database/mysql 创建了一个 mock driver](https://github.com/mostafaqanbaryan/go-rest/commit/89268a3153f6e9022196fb9d73b7c45305ac6d07#diff-17182578d392c41d39095ed310494918bbfd5168347d249e164804e114e291e9)…… 那是在浪费我的时间。

### 测试 services

鉴于其严重的缺点，测试一个 `service` 比测试一个 `query` 更好。你可以创建 mock/stub repositories 并针对它们测试你的 services。

所以现在我知道我在 `UserRepositoryMock` 中应该做什么了：我应该有一个 stub 并使用它。

`UserRepositoryMock` 应该像真正的 `UserRepository` 一样，但没有 `database` 逻辑：

```go
// user_repository_mock.go
type MockUserRepository struct {
	List map[int64]*entities.User
}
func (r MockUserRepository) FindByUsername(username string) (entities.User, error) {
	for _, user := range r.List {
		if username == user.Username {
			return *user, nil
		}
	}
	return entities.User{}, driverErrors.ErrRecordNotFound
}
```

通过此更改，`service_test.go` 的工作方式完全符合预期。

## 那么，这是 TDD 吗？
好吧，不是的。如果我想使用 TDD，一开始就不应该使用 Repository Pattern 编写我的 RESTful API 后端。相反，我应该创建一个简单的 `main_test.go` 并逐步完善它。

因为这是我第一次使用 Golang 做类似的事情（[之前我用 Go 编写过一些服务](/golang-vs-php/)），所以我需要为我的项目创建一个结构并预先选择一些工具。

但在那之后，我稍微修改了项目的结构 *（再次）*，删除了所有的 `service_test.go` 文件，将测试移动到 `http_test.go`，并测试了处理程序。我有一些很好的理由从测试 `service` 切换到测试处理程序：

- 虽然测试 `service` 是测试业务逻辑的好方法，但它不适合测试 RESTful API 后端。
- 像用户一样测试请求会导致测试处理程序中的验证和模型绑定。
- 为了单独测试处理程序，我不得不在 `http_test.go` 和 `service_test.go` 文件之间复制大量的测试，并且需要有人来维护它们。
- 目前，这些服务非常简单，没有很大的逻辑在其中。所以没有必要单独测试它们。

所以项目的最终结构是这样的：

```
cmd/
    web/
        main.go
internal/
    auth/
        errors/
            errors.go
        http/
            handler.go
        service/
            service.go
    database/
        queries/
    http/
        http.go
        http_test.go
    testutils/
        mock/
            auth_repository.go
            user_repository.go
    user/
        errors/
            errors.go
        http/
            handler.go
        service/
            service.go
```

## 迁移

迁移是任何项目的重要组成部分。

最初，我选择了 `go-migrate` 来进行迁移。但我意识到它不是完成这项工作的最佳工具。

问题是 `go-migrate` 只能与 `SQL` 一起使用，并且无法在代码中创建任何东西。

例如，为了在 `users` 表中为我的 `admin` 创建一条记录，我需要使用 `argon2` 为密码生成哈希值。因此，我要么必须预先生成哈希值，要么可以使用代码中已定义的函数。

因此，我决定改用 [goose](https://github.com/pressly/goose)。

`goose` 允许你选择要使用的迁移类型。例如，我可以创建一个用于在 `SQL` 中创建表的迁移（因为 `sqlc` 需要它的 schema 才能工作），并创建另一个作为 `.go` 文件。它非常强大。

过了一段时间，我在 `cmd/cli` 中添加了另一个 `main.go`，并创建了一个单独的可执行文件来处理命令。目前，它仅用于通过 `goose` 进行迁移。但它也可以用于其他事情，如 cronjobs 或脚本。

## 结论

这就是 `GoREST` 的构建方式。当然，这里完成的工作比说的要多得多，比如 [validation](https://github.com/go-playground/validator)，配置 `sqlc` 以与验证器一起工作，使用 `docker-compose` 启动 `MySQL` 和 `Redis`，`air` 用于热重载等等。

目前，它只有几个端点，包括 `/auth/login` 和 `/auth/register` 以及一个简单的 `/me` 端点。所有这些代码都存在于 [我在 GitHub 上的 GoREST 仓库](https://github.com/mostafaqanbaryan/go-rest) 中，但这不会是该项目的最终版本。我将 [添加更多功能](https://github.com/mostafaqanbaryan/go-rest#-todo-roadmap)，例如：

- OpenAPI specs
- An auth middleware
- A rate limiter
- More general endpoints
- Handling Logger
- A mechanism for cron jobs
- Separating services into instances and implementing (g)rpc
- …

所以，我希望你发现我的挣扎具有教育意义，因为我确实从中学习了。