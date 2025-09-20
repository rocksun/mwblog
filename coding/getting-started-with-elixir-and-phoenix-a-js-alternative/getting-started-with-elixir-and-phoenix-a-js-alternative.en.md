[Elixir](https://elixir-lang.org/install.html) is an [alternative to JavaScript-based web development](https://thenewstack.io/elixir-an-alternative-to-javascript-based-web-development/) that claims to offer faster development and lower costs. In this developer walkthrough, we try out Elixir and its [Phoenix](https://www.phoenixframework.org/) web framework.

Elixir was created by Josè Valim back in 2011, in response to the challenges of web development. Valim aimed to combine the reliability and scalability of [Erlang](https://thenewstack.io/why-erlang-joe-armstrongs-legacy-of-fault-tolerant-computing/) with the goals of modern developers. Elixir is a programming language built on the Erlang VM, known for concurrency and fault-tolerance. Elixir can handle thousands of simultaneous connections, which makes it well-suited for distributed, fault-tolerant systems. It uses the functional programming paradigm.

Phoenix is a web framework built on top of Elixir. Phoenix handles routing, database integration and standard web conventions. It’s a recommended option for developers looking to build web apps or APIs in Elixir.

A strong use case for using Phoenix and Elixir is apps that require thousands of simultaneous connections without slowing down. Think chat apps, live dashboards, multiplayer games. Phoenix has a live view where you can push updates to the browser without writing a single line of JavaScript.

This isn’t a catch-all, though; there are a lot of instances where JavaScript remains the optimal tool. If you need rich client-side interactivity, are quickly prototyping or building small-scale apps, or want integration with full-stack JavaScript environments, JavaScript and its tools are still a better choice than Elixir.

Let’s get to the rough part: in my short experience with Elixir and Phoenix, I found this software unintuitive and frustrating to work with. I say that knowing this probably represents my skill as a developer as much as the software itself (sorry). That said, I’ve written more of these articles than I could quickly count. This is the first time I almost posted a tutorial with bugs in it. Why? When Phoenix scaffolds the pages, the boilerplate code includes incorrect routes. Yes, it’s solvable, but I’ve built many of these basic CRUD apps. Working with Phoenix was the most frustrating one.

## Requirements

*Note: I had to update my OS to Sequoia before I could install Elixir.*

## Create a New Phoenix Project

```
mix phx.new notes_app
cd notes_app
```

This creates a project with the following directory structure:

* Controllers `lib/notes_app_web/controllers`
* HTML templates `lib/notes_app_web/templates`
* Routes `lib/notes_app_web/router.ex`
* Context note for business logic `lib/notes_app/notes.ex`

## Set Up the Database

Setting up the database will allow you to store notes long after you refresh the page.

```
mix ecto.create
mix ecto.migrate
```

## Scaffolding a CRUD Interface

Phoenix has a generator command that will create a full CRUD web interface for a resource.

```
mix phx.gen.html Notes Note notes title:string body:text mix ecto.migrate
```

This creates the notes context, schema, table, and columns for the table. The context is helper functions to create, update, delete, and list notes. The schema is the blueprint of the notes. The migration instructions build the table in the database. The controller handles all requests. Views and templates display the app on your browser. And then we have the router, which ensures `/notes` works at the end of a URL.

We’re ready to start the dev server. This can run throughout the development process. We don’t have to start and stop it.

```
mix phx.server
```

Go to this URL in your browser: http://localhost:4000/notes

You will see that there are a lot of folders and files. I didn’t love this, which might have been the start of my challenges.

We are going to focus on the following pages:

* Index page
* Show page
* New and Edit pages
* Controller
* Routers

## Index Page

You’ll find the index page in the `notes_app_web/templates/note/index.html.heex`.

This is the homepage and it shows all your notes. It’s the central navigation page, plus it’s the page we’ll need to keep going back to after deleting or editing a note.

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

## Show Page

This page will show you one note in detail. The goal of this page is to help the user read or review a specific note in detail. You can find it here: `notes_app_web/templates/note/show.html.heex`

```
<h1><%= @note.title %></h1>
<p><%= @note.body %></p>


<a href={Routes.note_path(@conn, :edit, @note)}>Edit</a>
<a href={Routes.note_path(@conn, :index)}>Back to all notes</a>
```

## New and Edit Pages

These are our form pages, where we build and edit the notes.

Here’s the partial form: `_form.html.heex`.

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

Create a new note: `new.html.heex`

```
<h1>New Note</h1>
<%= render "form.html", Map.put(assigns, :action, Routes.note_path(@conn, :create)) %>
<a href={Routes.note_path(@conn, :index)}>Back</a>
```

This is where you can edit a note: `edit.html.heex`

```
<h1>Edit Note</h1>
<%= render "form.html", Map.put(assigns, :action, Routes.note_path(@conn, :update, @note)) %>
<a href={Routes.note_path(@conn, :show, @note)}>Back</a>
```

Before we build the controller, let’s talk about debugging. When Phoenix scaffolds the boilerplate for your Notes resource, it still includes old-style routers. The older style routers (which will not work with the latest install) look like the code below and you’ll find them in the controller:

```
redirect(to: Routes.note_index_path(conn, :index))
redirect(to: Routes.note_show_path(conn, :show, note))
```

Those were replaced by verified routes that use the `~p` syntax. If you don’t manually go through and replace the old code, you will see errors when you edit or delete notes in your browser. I use Chrome, and it happened to me during the making of this tutorial… a lot.

There is a simple fix, though: Replace the old routes with this code:

```
redirect(to: ~p"/notes")
redirect(to: ~p"/notes/#{note.id}")
```

## We’re Ready to Build the Controller

Here’s where the action of the application takes place. We’re going to build our full CRUD functionality into this one file. The controller connects the templates to the database. It handles business logic, validation, and navigation (redirects). You can find this file here: `notes_app_web/controllers/note_controller.ex`.

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

## Routes

Routes tell Phoenix which controller action to call for each URL. `resources` generates all standard CRUD routes automatically. You can find this file here: `notes_app_web/router.ex`.

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

And there you have it! You may find this software more intuitive and easier to work with than I did. Give it a try.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://thenewstack.io/wp-content/uploads/2023/04/d55571c0-cropped-b09ca100-image1-600x600.jpg)

Jessica Wachtel is a developer marketing writer at InfluxData where she creates content that helps make the world of time series data more understandable and accessible. Jessica has a background in software development and technical journalism.

Read more from Jessica Wachtel](https://thenewstack.io/author/jessica-wachtel/)