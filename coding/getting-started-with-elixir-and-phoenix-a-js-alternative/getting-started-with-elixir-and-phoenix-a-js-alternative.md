
<!--
title: Elixir和Phoenix入门：一个JS替代方案
cover: https://cdn.thenewstack.io/media/2025/09/7deb4d9e-mouaadh-tobok-tfg3kqvj554-unsplashb.jpg
summary: 本文介绍了 Elixir 及其 Phoenix Web 框架，用于构建 Web 应用程序。内容涵盖了 Phoenix 项目的创建、数据库设置、CRUD 界面搭建，以及控制器、路由等关键组件的构建。作者分享了使用体验，并指出了潜在的陷阱和解决方法。
-->

本文介绍了 Elixir 及其 Phoenix Web 框架，用于构建 Web 应用程序。内容涵盖了 Phoenix 项目的创建、数据库设置、CRUD 界面搭建，以及控制器、路由等关键组件的构建。作者分享了使用体验，并指出了潜在的陷阱和解决方法。

> 译自：[Getting Started With Elixir and Phoenix, a JS Alternative](https://thenewstack.io/getting-started-with-elixir-and-phoenix-a-js-alternative/)
> 
> 作者：Jessica Wachtel

[Elixir](https://elixir-lang.org/install.html) 是一个 [基于JavaScript的Web开发替代方案](https://thenewstack.io/elixir-an-alternative-to-javascript-based-web-development/)，声称可以提供更快的开发速度和更低的成本。 在此开发者演练中，我们将尝试 Elixir 及其 [Phoenix](https://www.phoenixframework.org/) Web 框架。

Elixir 由 Josè Valim 于 2011 年创建，旨在应对 Web 开发的挑战。 Valim 旨在将 [Erlang](https://thenewstack.io/why-erlang-joe-armstrongs-legacy-of-fault-tolerant-computing/) 的可靠性和可扩展性与现代开发人员的目标相结合。 Elixir 是一种构建在 Erlang VM 上的编程语言，以其并发性和容错性而闻名。 Elixir 可以处理数千个并发连接，这使其非常适合分布式、容错系统。 它使用函数式编程范式。

Phoenix 是构建在 Elixir 之上的 Web 框架。 Phoenix 处理路由、数据库集成和标准 Web 约定。 对于希望在 Elixir 中构建 Web 应用程序或 API 的开发人员来说，这是一个推荐的选择。

使用 Phoenix 和 Elixir 的一个强大的用例是需要数千个并发连接而不会减慢速度的应用程序。 想想聊天应用程序、实时仪表板、多人游戏。 Phoenix 有一个实时视图，您无需编写任何 JavaScript 代码即可将更新推送到浏览器。

但这并不是万能的；在很多情况下，JavaScript 仍然是最佳工具。 如果您需要丰富的客户端交互性，快速原型设计或构建小规模应用程序，或者希望与全栈 JavaScript 环境集成，那么 JavaScript 及其工具仍然是比 Elixir 更好的选择。

让我们来谈谈困难的部分：在我与 Elixir 和 Phoenix 短暂的合作经历中，我发现这款软件不太直观，而且使用起来令人沮丧。 我这么说是因为我知道这可能代表了我作为开发人员的技能，也代表了软件本身（抱歉）。 也就是说，我写过的这类文章比我能快速数清的还要多。 这是我第一次几乎发布了一个带有错误的教程。 为什么？ 当 Phoenix 搭建页面时，样板代码包含不正确的路由。 是的，这是可以解决的，但我已经构建了很多这样的基本 CRUD 应用程序。 使用 Phoenix 是最令人沮丧的一次。

## 要求

*注意：我必须将我的操作系统更新到 Sequoia 才能安装 Elixir。*

## 创建一个新的 Phoenix 项目

```
mix phx.new notes_app
cd notes_app
```

这将创建一个具有以下目录结构的项目：

* 控制器 `lib/notes_app_web/controllers`
* HTML 模板 `lib/notes_app_web/templates`
* 路由 `lib/notes_app_web/router.ex`
* 用于业务逻辑的上下文说明 `lib/notes_app/notes.ex`

## 设置数据库

设置数据库将允许您在刷新页面后很长时间内存储笔记。

```
mix ecto.create
mix ecto.migrate
```

## 搭建 CRUD 界面

Phoenix 有一个生成器命令，它将为一个资源创建一个完整的 CRUD Web 界面。

```
mix phx.gen.html Notes Note notes title:string body:text mix ecto.migrate
```

这将为表创建笔记上下文、模式、表和列。 上下文是创建、更新、删除和列出笔记的辅助函数。 模式是笔记的蓝图。 迁移说明在数据库中构建表。 控制器处理所有请求。 视图和模板在您的浏览器上显示应用程序。 然后我们有了路由器，它确保 `/notes` 在 URL 的末尾工作。

我们已准备好启动开发服务器。 这可以在整个开发过程中运行。 我们不必启动和停止它。

```
mix phx.server
```

在您的浏览器中转到此 URL：http://localhost:4000/notes

您会看到有很多文件夹和文件。 我不喜欢这样，这可能是我挑战的开始。

我们将专注于以下页面：

* 索引页
* 显示页
* 新建和编辑页面
* 控制器
* 路由器

## 索引页

您可以在 `notes_app_web/templates/note/index.html.heex` 中找到索引页。

这是主页，它显示您的所有笔记。 它是中心导航页面，而且是我们删除或编辑笔记后需要不断返回的页面。

```
<h1>All Notes</h1>


<ul>
  <%= for note <- @notes do %>
    <li>
      <strong><%= note.title %></strong> - <%= note.body %>
      [<a href={Routes.note_path(@conn, :show, note)}>Show</a>]
      [<a href={Routes.note_path(@conn, :edit, note)}>Edit</a>]
    </li>
  <% end %>
</ul>


<a href={Routes.note_path(@conn, :new)}>Create a new note</a>
```

## 显示页

此页面将详细显示一个笔记。 此页面的目标是帮助用户详细阅读或查看特定笔记。 您可以在这里找到它：`notes_app_web/templates/note/show.html.heex`

```
<h1><%= @note.title %></h1>
<p><%= @note.body %></p>


<a href={Routes.note_path(@conn, :edit, @note)}>Edit</a>
<a href={Routes.note_path(@conn, :index)}>Back to all notes</a>
```

## 新建和编辑页面

这些是我们的表单页面，我们可以在其中构建和编辑笔记。

这是部分表单：`_form.html.heex`。

```
<%= form_for @changeset, @action, fn f -> %>
  <div>
    <%= label f, :title %>
    <%= text_input f, :title %>
  </div>
  <div>
    <%= label f, :body %>
    <%= textarea f, :body %>
  </div>
  <div>
    <%= submit "Save" %>
  </div>
<% end %>
```

创建一个新笔记：`new.html.heex`

```
<h1>New Note</h1>
<%= render "form.html", Map.put(assigns, :action, Routes.note_path(@conn, :create)) %>
<a href={Routes.note_path(@conn, :index)}>Back</a>
```

这是您可以编辑笔记的地方：`edit.html.heex`

```
<h1>Edit Note</h1>
<%= render "form.html", Map.put(assigns, :action, Routes.note_path(@conn, :update, @note)) %>
<a href={Routes.note_path(@conn, :show, @note)}>Back</a>
```

在我们构建控制器之前，让我们谈谈调试。 当 Phoenix 为您的 Notes 资源搭建样板时，它仍然包含旧样式的路由器。 较旧样式的路由器（与最新安装不兼容）如下面的代码所示，您可以在控制器中找到它们：

```
redirect(to: Routes.note_index_path(conn, :index))
redirect(to: Routes.note_show_path(conn, :show, note))
```

这些已被使用 `~p` 语法的已验证路由替换。 如果您不手动检查并替换旧代码，则在浏览器中编辑或删除笔记时会看到错误。 我使用 Chrome，在制作本教程期间，它发生在我身上很多次。

不过，有一个简单的修复方法：将旧路由替换为以下代码：

```
redirect(to: ~p"/notes")
redirect(to: ~p"/notes/#{note.id}")
```

## 我们已准备好构建控制器

这是应用程序的操作发生的地方。 我们将在此文件中构建完整的 CRUD 功能。 控制器将模板连接到数据库。 它处理业务逻辑、验证和导航（重定向）。 您可以在此处找到此文件：`notes_app_web/controllers/note_controller.ex`。

```
defmodule NotesAppWeb.NoteController do
  use NotesAppWeb, :controller


  alias NotesApp.Notes
  alias NotesApp.Notes.Note


  # GET /notes
  def index(conn, _params) do
    notes = Notes.list_notes()
    render(conn, :index, notes: notes)
  end


  # GET /notes/new
  def new(conn, _params) do
    changeset = Notes.change_note(%Note{})
    render(conn, :new, changeset: changeset)
  end


  # POST /notes
  def create(conn, %{"note" => note_params}) do
    case Notes.create_note(note_params) do
      {:ok, note} ->
        conn
        |> put_flash(:info, "Note created successfully.")
        |> redirect(to: ~p"/notes/#{note.id}")


      {:error, %Ecto.Changeset{} = changeset} ->
        render(conn, :new, changeset: changeset)
    end
  end


  # GET /notes/:id
  def show(conn, %{"id" => id}) do
    note = Notes.get_note!(id)
    render(conn, :show, note: note)
  end


  # GET /notes/:id/edit
  def edit(conn, %{"id" => id}) do
    note = Notes.get_note!(id)
    changeset = Notes.change_note(note)
    render(conn, :edit, note: note, changeset: changeset)
  end


  # PUT /notes/:id
  def update(conn, %{"id" => id, "note" => note_params}) do
    note = Notes.get_note!(id)


    case Notes.update_note(note, note_params) do
      {:ok, note} ->
        conn
        |> put_flash(:info, "Note updated successfully.")
        |> redirect(to: ~p"/notes/#{note.id}")


      {:error, %Ecto.Changeset{} = changeset} ->
        render(conn, :edit, note: note, changeset: changeset)
    end
  end


  # DELETE /notes/:id
  def delete(conn, %{"id" => id}) do
    note = Notes.get_note!(id)
    {:ok, _note} = Notes.delete_note(note)


    conn
    |> put_flash(:info, "Note deleted successfully.")
    |> redirect(to: ~p"/notes")
  end
end
```

## 路由

路由告诉 Phoenix 为每个 URL 调用哪个控制器操作。 `resources` 自动生成所有标准 CRUD 路由。 您可以在此处找到此文件：`notes_app_web/router.ex`。

```
defmodule NotesAppWeb.Router do
  use NotesAppWeb, :router


  pipeline :browser do
    plug :accepts, ["html"]
    plug :fetch_session
    plug :fetch_live_flash
    plug :put_root_layout, html: {NotesAppWeb.Layouts, :root}
    plug :protect_from_forgery
    plug :put_secure_browser_headers
  end


  pipeline :api do
    plug :accepts, ["json"]
  end


  scope "/", NotesAppWeb do
    pipe_through :browser


    get "/", PageController, :home
    resources "/notes", NoteController
  end


  if Application.compile_env(:notes_app, :dev_routes) do
    import Phoenix.LiveDashboard.Router


    scope "/dev" do
      pipe_through :browser


      live_dashboard "/dashboard", metrics: NotesAppWeb.Telemetry
      forward "/mailbox", Plug.Swoosh.MailboxPreview
    end
  end
end
```

就这样！ 您可能会发现这款软件比我更直观且更容易使用。 尝试一下。