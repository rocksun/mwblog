Creating [GoREST](https://github.com/mostafaqanbaryan/go-rest) has taken about a month so far (though I haven’t worked on it full-time - I’m counting from the first commit).

Because of that, I’ve written this article to prevent others from making the same mistakes that took a considerable amount of time and effort to fix.

## Introduction
You may know I’m a PHP developer with a few years of experience under my belt. Like many PHP developers, I’ve been working with Laravel and been enjoying it. But right now I’m changing course to Golang.

I expected to experience some culture shock when starting to learn Golang, because unlike PHP with Laravel, there’s no single dominant framework that everyone uses, and no universally accepted standard way to structure applications (or at least that was my impression).

So I’m going to explain in this article how I created a RESTful API backend with Go in the worst way possible.

If you don’t want to read the whole article, here is the repository for you:

[https://github.com/mostafaqanbaryan/go-rest](https://github.com/mostafaqanbaryan/go-rest)
## The Worst Way Possible!
As I said before, I’m fairly new to Go. Obviously, many concepts are not clear to me. I’m also new to writing tests, as I didn’t before.

So I decided to write a RESTful API backend with Golang and TDD (Test Driven Development) to kill two birds with one stone; and boy, am I gonna regret that!

## Frameworks, Routers, or Raw?
Coming from Laravel, I initially assumed I needed a framework for my backend. However, reading the Golang documentation and consulting the community, I’ve noticed that many Go developers tend to avoid using frameworks.

I’ve coded different projects with PHP without frameworks before, and it wasn’t terrible. However, PHP lacks many built-in tools that modern languages like Go provide, which explains why Laravel became so popular as it filled those gaps.

But in Golang, frameworks are not necessary. You could easily write a RESTful API backend without a framework. But I didn’t want to miss the opportunity to check a few of them.

### Gorm
[Gorm](https://gorm.io/) is the first framework that I’ve checked out. It’s an easy-to-use ORM that handles a lot of stuff for you.
I refactored a project that was written with Gorm and I really enjoyed it. But while refactoring, I realized that testing the code wasn’t easy. So, It seems like I failed to kill both birds with one stone.

And who am I kidding? I prefer to work with `SQL`
instead of query builders! It’s easier to read and write.

### Chi
[Chi](https://github.com/go-chi/chi) is a lightweight, and idiomatic router for building Go HTTP services and an ideal alternative for a framework.
In the beginning, I actually started with Chi. After a few days and a little search, I realized that it’s really similar to the standard `http`
package in Golang, and most of `Chi`
’s code is merged to the core of Golang project, and that’s really great!

However, it seems using `Chi`
doesn’t have any big advantages over the standard `http`
package anymore ([of course there is middleware and grouping](https://www.reddit.com/r/golang/comments/1avn6ih/is_chi_relevant_anymore/)).

So I decided to use something else.

### Echo
[Echo](https://echo.labstack.com/) is a high performance, extensible, minimalist, relatively new framework that I had no former knowledge of.
Echo has a few features that I didn’t want to write myself, for example:

- Responses are easier to handle. It’s easier to write:
`return c.String(http.StatusOK, "Welcome")`
than:
```
w.Write([]byte("Welcome"))
return
```
- It has a lot of
[middlewares](https://echo.labstack.com/docs/category/middleware) - Because it works with the standard
`http`
package, writing tests is easy. Just need to create the`context`
and you’re good to go:
```
req := httptest.NewRequest(http.MethodPost, "/", strings.NewReader(userJSON))
req.Header.Set(echo.HeaderContentType, echo.MIMEApplicationJSON)
rec := httptest.NewRecorder()
c := e.NewContext(req, rec)
```
- Echo includes more features that I didn’t check out yet, so be sure to
[read the documentation](https://echo.labstack.com/docs).
*Of course there are other great frameworks and routers out there like fiber and gin, and the standard http package also works great for a project like this. But I’ve decided to use Echo for now.*
## Project structure
If you’ve worked with Laravel, you know it enforces a specific project structure. But in Go (or any language without using a framework actually), you can structure your project however you want… which can actually be problematic!

When I was refactoring the `Gorm`
project that I had, I found the [Golang Standard Project Layout](https://github.com/golang-standards/project-layout) which was beautiful and unique, followed by various projects.

However, there was a problem. Despite being great, It didn’t say anything about writing REST-API backends with TDD and the Repository Pattern.

So at first, I created my project like this:

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
And I was happy. The problem started when I wanted to inject repositories into my services.

Having all the services in the same package meant that I couldn’t have for example, separate `repo`
structs for each service.

At this point, you know that I’ve failed to implement TDD in my project, but I was trying! I knew I had to change the structure of my project. So I decided to make it more like [DDD](https://en.wikipedia.org/wiki/Domain-driven_design):

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
Now we’re talking! Now I can inject the repositories into the services with duplicate names and test each of them easily.

## Testing… 1, 2, 3?
As I said, I wanted to try TDD because the minute I read [Learn Go with tests](https://quii.gitbook.io/learn-go-with-tests/) by [@quii](https://twitter.com/quii), I fell in love with it! I’ve read it a few times, and I’m never tired of reading it. It’s really good!

But I still didn’t learn how to start writing a RESTful API backend with TDD (because I didn’t realize that [@quii already talked about in the book](https://quii.gitbook.io/learn-go-with-tests/build-an-application/http-server))

So I decided to start with the basics. I created a simple `main.go`
, `repository.go`
and a `service.go`
and after that, wrote a unit test for `service.go`
.

Here is what the first sample looked like:

```
// user_repository_mock.go
type UserRepositoryMock struct { }
func NewUserRepositoryMock() UserRepositoryMock {
return UserRepositoryMock{}
}
func (r UserRepositoryMock) FindByUsername(username string) (*entities.User, error) {
return nil, errors.UserNotFound{}
}
```
```
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
```
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
I thought that was a good start, but what the hell should I do in `UserRepositoryMock`
?
In the real `UserRepository`
, I checked the user against a `database`
. But I had no idea whether I should do the same thing for `UserRepositoryMock`
and mock a `database`
or not?

By mocking each method separately in query builders, testing would be easy. For example I could easily mock `select`
or `insert`
method. But while working with `sqlc`
, I faced some challenges in writing tests.

So I had to decide:

- Do I want to test all my queries?
- Or do I want to test my services?
### Testing queries
Don’t ever do this! Testing queries or query builders (or in this case, `sqlc`
) is a bad idea. Why you may ask? Here are some of the reasons:

- You’re testing a 3rd party package, not your code.
- For testing queries, you need an actual
`database`
, and that makes it an integration test. - Running integration tests is slow.
I’m proud to say that I did create a [mock driver for sqlc](https://github.com/mostafaqanbaryan/go-rest/commit/864ca86d266825383151ce52f5d5c19c69831bb7#diff-47417e701aa4c04563c04211b28e891ffa5592f0ea2046e8d4c8a8cbf9aa0313) and before that, [for database/mysql](https://github.com/mostafaqanbaryan/go-rest/commit/89268a3153f6e9022196fb9d73b7c45305ac6d07#diff-17182578d392c41d39095ed310494918bbfd5168347d249e164804e114e291e9) too, and… that was a waste of my time.

### Testing services
Testing a `service`
is a better method than testing a `query`
given its serious downsides. You can create mock/stub repositories and test your services against them.

So now I know what should I do in my `UserRepositoryMock`
: I should have a stub and work with that.

The `UserRepositoryMock`
should be like the real `UserRepository`
, but without the `database`
logic:

```
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
With this change, `service_test.go`
worked exactly as intended.

## So, Is This TDD?
Well, no. If I wanted to use TDD, I shouldn’t have written my RESTful API backend with the Repository Pattern at first. Instead, I should have created a simple `main_test.go`
and worked it up.

Since it was my first time using Golang for something like this ([I have written some services with Go before](/golang-vs-php/)), I needed to create a structure for my project and select some tools beforehand.

But after that, I changed the structure of the project a little *(again)*, removed all the `service_test.go`
files, moved the tests to `http_test.go`
, and tested the handlers. I had a few good reasons for switching from testing a `service`
to testing handlers:

- Although testing a
`service`
is a great way to test the business logic, it’s not good for testing a RESTful API backend. - Testing requests like a user lead to testing validations and model bindings in the handlers.
- For testing the handlers separately, I would have to duplicate a lot of tests between the
`http_test.go`
and the`service_test.go`
files, and somebody would have to maintain them. - Currently, the services are really thin and don’t have big logics in them. So there is no need to test them separately.
So the final structure of the project is like this:

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
## Migrations
Migrations are a significant part of any project.

Originally, I selected `go-migrate`
to do the migrations. But I realized that it wasn’t the best tool for the job.

The problem was that `go-migrate`
only worked with `SQL`
, and it was not possible to create something in the code.

For instance, to create a record for my `admin`
in the `users`
table, I needed to generate a hash for the password using `argon2`
. So either I had to generate the hash beforehand, or I could use the function already defined in my code.

Because of that, I’ve decided to use [goose](https://github.com/pressly/goose) instead.

`goose`
lets you choose what kind of migration you want to work with.
For example, I could have a migration for creating tables in `SQL`
(because `sqlc`
needs its schema to work), and create another one as a `.go`
file. It’s really powerful.

After some time, I added another `main.go`
to `cmd/cli`
and created a separate executable for handling commands. Currently, it’s only used for migrations via `goose`
. But it could be used for other things like cronjobs or scripts as well.

## Conclusion
So that’s how `GoREST`
is built. Of course, there is much more done here than said, like [validation](https://github.com/go-playground/validator), configuring `sqlc`
to work with the validator, using `docker-compose`
for launching `MySQL`
and `Redis`
, `air`
for hot-reload, and so on.

Currently, it only has a few endpoints, including `/auth/login`
and `/auth/register`
and a simple `/me`
endpoint. All this code exists at the [GoREST repository in my GitHub](https://github.com/mostafaqanbaryan/go-rest), but it’s not going to be the final version of the project. I’m going to [add more features](https://github.com/mostafaqanbaryan/go-rest#-todo-roadmap) to it, such as:

- OpenAPI specs
- An auth middleware
- A rate limiter
- More general endpoints
- Handling Logger
- A mechanism for cron jobs
- Separating services into instances and implementing (g)rpc
- …
So, I hope you find my struggles educational as I certainly learned from them.