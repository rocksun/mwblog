At one point, the frontend framework landscape had three big players: [React](https://thenewstack.io/react-router-new-governance-and-react-server-component-apis/), [Vue](https://thenewstack.io/a-peek-at-whats-next-for-vue/) and [Angular](https://thenewstack.io/angular-v20-advances-zoneless-adds-support-for-ai-development/). Knowing all three was basically the golden ticket when it came to job hunting. Then came the rise of lightweight apps, server-side rendering, and the desire to never build a webpack bundle again. Suddenly, the big three became many. And when it came to choosing which technology to use, the question of “do you know how to use X?” shifted to “which technology works best for this project?”

One of the many options today is [Enhance](https://enhance.dev/), a modern full-stack framework designed for simplicity and speed. If you’re looking for rapid prototyping or you’re doing a backend-first small project, Enhance is a solid choice. Enhance gives you a lightweight approach with minimal setup, letting you wire up APIs and a database quickly.

## Enhance vs. Astro

Other lightweight frameworks, [like Astro](https://thenewstack.io/astros-journey-from-static-site-generator-to-next-js-rival/), tend to be frontend-first. Astro’s main focus is building static sites or server-rendered pages, where the HTML, CSS and JavaScript you deliver to the browser is the main focus. You can add backend logic, but it’s not the core workflow.

Enhance is backend first. The app logic, API endpoints and database interactions come first. You don’t have to think about static HTML or page components right away. You can also use one of “the big three” frameworks as the frontend, making use of those skills.

If you can’t decide between Astro and Enhance, here’s a way to approach it.

When building with Astro, your priorities are:

* Optimizing frontend rendering and page load performance.
* Structuring components for layouts for static or server-rendered pages.
* Minimizing client-side JavaScript and managing hydration.

When building with Enhance, your priorities are:

* Designing backend logic, API endpoints, and server-side functions.
* Easy setup and interactivity with a database.
* Rapidly prototyping full-stack features without boilerplate.

## Building an Enhance App

Now that we’ve covered the basics, let’s build a tiny full-stack application complete with a SQL database. Since frontend isn’t the focus, we’ll build a simple CRUD (create, read, update, delete) app where you can add a vote via a text box on the screen. You will be able to edit and delete the notes. Since we’ll have a fully working database, refreshing the page will not impact the notes you’ve already saved.

### Getting Started: Files and Installs

Create and open a new project folder.

```
mkdir notes-app
cd notes-app
```

Initialize a Node.js project (this will create a package.json).

```
npm init -y
```

Install Enhance and SQLite dependencies.

```
npm install enhance better-sqlite3
```

Now we’re going to create our project files. These are going to be pretty basic. The structure will look like this:

```
notes-app/
├─ db.js          Handles SQLite connection and setup
├─ api.js         Defines functions to create, read, update, delete notes
├─ server.js      Minimal HTTP server to serve the front-end and endpoints
└─ index.html     Front-end HTML + JavaScript for interacting with the app
```

Make sure you’re in the `notes-app` folder before doing the next step.

Once you’ve confirmed that you’re in the right folder, we can create all the files we’ll need.

```
touch db.js api.js server.js index.html
```

You can confirm you’ve done this correctly by opening the main `notes-app` folder.

Now we’re ready to build.

### Building the SQLite Database

The first thing we’re going to set up is the database, `db.js`.

The database file will connect to a file-based SQLite database (`myapp.db`). It will also create a `notes` table with `id`, `title`, and `content`. This file is why you can refresh the page without erasing the notes.

You may notice that we use the term `require` rather than `import` in this code. We will continue doing this for the remainder of the tutorial, because we’re using CommonJS syntax rather than ES Modules. You can switch to ES Modules if your `package.json` includes `”type”: “module”`. Note that Enhance’s examples and docs often show CommonJS because it’s the simplest setup.

```
const Database = require('better-sqlite3');
const db = new Database('myapp.db');


db.prepare(`
  CREATE TABLE IF NOT EXISTS notes (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT,
    content TEXT
  )
`).run();


module.exports = db;
```

### Adding CRUD Functionality

This page, `api.js` is the meat of the application. The functions are:

`getNotes()`

This is a GET request. It’s main purpose is to fetch all notes from the database.

`addNotes()`

This is a POST request because it adds a new request to the database.

`editNote()`

This is the PUT request. It will update a note when specified by the user (via an edit button we’ll add later).

`deleteNote()`

This is a DELETE request and will delete a note using its `id` when specified by the user (another button we’ll add later).

We’re going to build `async` code to keep our code clean and non-blocking.

```
const db = require('./db');


async function getNotes() {
  return db.prepare('SELECT * FROM notes').all();
}


async function addNote({ title, content }) {
  const info = db.prepare('INSERT INTO notes (title, content) VALUES (?, ?)').run(title, content);
  return { id: info.lastInsertRowid, title, content };
}


async function editNote({ id, title, content }) {
  db.prepare('UPDATE notes SET title = ?, content = ? WHERE id = ?').run(title, content, id);
  return { id, title, content };
}


async function deleteNote({ id }) {
  db.prepare('DELETE FROM notes WHERE id = ?').run(id);
  return { success: true };
}


module.exports = { getNotes, addNote, editNote, deleteNote };
```

### Building the Server

Our `server.js` file is going to include the build for a basic HTTP server. There’s nothing unique to Enhance on this server.

```
const http = require('http');
const fs = require('fs');
const path = require('path');
const { getNotes, addNote, editNote, deleteNote } = require('./api');


const server = http.createServer(async (req, res) => {
  // Serve index.html
  if (req.url === '/' && req.method === 'GET') {
    const html = fs.readFileSync(path.join(__dirname, 'index.html'), 'utf-8');
    res.writeHead(200, { 'Content-Type': 'text/html' });
    res.end(html);
    return;
  }


  // GET /notes
  if (req.url === '/notes' && req.method === 'GET') {
    const notes = await getNotes();
    res.writeHead(200, { 'Content-Type': 'application/json' });
    res.end(JSON.stringify(notes));
    return;
  }


  // POST /notes
  if (req.url === '/notes' && req.method === 'POST') {
    let body = '';
    req.on('data', chunk => body += chunk);
    req.on('end', async () => {
      const note = await addNote(JSON.parse(body));
      res.writeHead(200, { 'Content-Type': 'application/json' });
      res.end(JSON.stringify(note));
    });
    return;
  }


  // PUT /notes/:id
  if (req.url.startsWith('/notes/') && req.method === 'PUT') {
    let body = '';
    req.on('data', chunk => body += chunk);
    req.on('end', async () => {
      const id = parseInt(req.url.split('/')[2]);
      const note = await editNote({ id, ...JSON.parse(body) });
      res.writeHead(200, { 'Content-Type': 'application/json' });
      res.end(JSON.stringify(note));
    });
    return;
  }


  // DELETE /notes/:id
  if (req.url.startsWith('/notes/') && req.method === 'DELETE') {
    const id = parseInt(req.url.split('/')[2]);
    await deleteNote({ id });
    res.writeHead(200, { 'Content-Type': 'application/json' });
    res.end(JSON.stringify({ success: true }));
    return;
  }


  // Fallback for unrecognized routes
  res.writeHead(404);
  res.end('Not found');
});


server.listen(3000, () => console.log('Server running on http://localhost:3000'));
```

### The Frontend

Finally, let’s build our `index.html`. For this tutorial, we’ll just use HTML — but you can connect a more robust frontend framework to this backend for additional functionality.

Since our `notes-app` is using Node’s built-in `http` module, you can run the dev server with this simple command:

```
node server.js
```

When you head over to http://localhost:3000/, you should see the homepage with two text boxes, where you can add notes.

Go ahead, add a note. Once you click ‘add note’, you’ll see the note with the edit and delete buttons pop up.

### Accessing the Database

None of these database commands are unique to Enhance. You can use the same SQL you’d use for another app.

You can access the database in your terminal with the following commands:

```
#open database
sqlite3 myapp.db


#view notes
.tables


#edit
UPDATE notes SET title = 'New Title', content = 'Updated content' WHERE id = 1;


#delete 
DELETE FROM notes WHERE id = 2;


#exit
.quit


```

It’s as simple as that!

## Conclusion

Enhance has other more advanced features not covered in this tutorial. Here’s a non-exhaustive list:

* Serialization of JSON: Enhance automatically handles request/ response serialization, letting you return plain JavaScript objects that get converted into JSON.
* Functions as endpoints: you can write plain JavaScript functions that act as API endpoints rather than needing a separate server or framework.
* Zero-JavaScript by default: you can layer JavaScript where needed, but pages are functional and accessible without requiring client-side JavaScript.

Now you have the foundation to build and scale real applications with Enhance. What will you build?

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![]()

Jessica Wachtel is a developer marketing writer at InfluxData where she creates content that helps make the world of time series data more understandable and accessible. Jessica has a background in software development and technical journalism.

Read more from Jessica Wachtel](https://thenewstack.io/author/jessica-wachtel/)