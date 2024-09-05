# Introduction to Datasette, a Frontend to Tabulated Data
![Featued image for: Introduction to Datasette, a Frontend to Tabulated Data](https://cdn.thenewstack.io/media/2024/09/70364e29-nat-zfx_claru9s-unsplash-1024x683.jpg)
Like all larger open source projects, the best way to approach [Simon Willison’s](https://thenewstack.io/datasette-a-developer-a-shower-and-a-data-inspired-moment/) [Datasette](https://datasette.io/) is to play with it a bit to get an idea of what you could achieve. Aimed to be used by “data journalists, museum curators, archivists, local governments, scientists, researchers,” it is a functional interactive frontend to tabulated data, whether a CSV file or a database schema. Just like [Tiddlywiki](https://thenewstack.io/tiddlywiki-an-open-source-alternative-to-notion-or-obsidian/), it has an [ecosystem](https://docs.datasette.io/en/stable/ecosystem.html#) around it and a loyal following.

What I want to do here for developers is to introduce the tool, and see if you can use it internally in your own organization — in this case, as a dashboard for folks not likely to be using SQL queries directly. Building corporate dashboards is something most developers need to do at some point in their careers.

I’ll hit a quick example with data from my last post, before hosting Datasette with my own table data.

Let’s use [Datasette lite](https://lite.datasette.io/), which is hosted in your browser by [WebAssembly](https://thenewstack.io/webassembly/). Give it a few seconds to appear:

We will load it up with [this link](https://raw.githubusercontent.com/plotly/datasets/master/gapminder_unfiltered.csv) to some “population by time” data, which you may have seen in my previous post about [Plotly Dash](https://thenewstack.io/introduction-to-plotly-dash-the-most-popular-ai-data-tool/); just hit “Load CSV” and we can drill down quickly into the data:

One of the nice tools in Datasette is the ability to use “facets” to summarize multiple-entry data. In the lite version, we can’t make a facet out of any column as we can in the full version; but we can use the suggested facets, like “continent” above:

(Note: “FSU” is Former Soviet Union.)

This gives us a very useful summary. Datasette lets you browse the data, and try out SQL as well if you want to — in fact it probably isn’t a bad way to [learn SQL](https://datasette.io/tutorials/learn-sql), as you can always view and edit the SQL on any page.

Each page has a unique URL, so you can pass it around. It also can show you the given data in CSV or JSON format. Whereas Plotly Dash was all about graphing, Datasette was mostly about working directly with the table data. However, there are data visualizations, as you can see from the cluster map[ in this instance](https://congress-legislators.datasettes.com/legislators/offices).

Now that you’ve had a quick look at Datasette with tabulated data in a CSV file, let’s [install it](https://docs.datasette.io/en/stable/installation.html) and target a simple database.

I’m using my old Macbook, so I can just use Homebrew:

As usual, I have lots of kegs to pour. The version checks out:

Now that Datasette is sitting on my Macbook, I’ll install that simple [books schema](https://www.db-fiddle.com/f/6Fj2vw8bFhzVADG4UFUjD6/0) from my post about [AI schema generation](https://thenewstack.io/sql-schema-generation-with-large-language-models/), trying to use a SQLite3 dialect. I’ll start SQLite3 with a new empty “books” schema:

There are three tables: authors, publishers and books.

12345 |
CREATE TABLE authors ( author_id INTEGER PRIMARY KEY NOT NULL, name VARCHAR(255) NOT NULL, birthday DATE NOT NULL ); |
12345 |
CREATE TABLE publishers ( publisher_id INTEGER PRIMARY KEY NOT NULL, name VARCHAR(255) NOT NULL, address VARCHAR(255) NOT NULL ); |
123456789 |
CREATE TABLE books ( name VARCHAR(255) NOT NULL, author_id INTEGER, publisher_id INTEGER, published_date DATE NOT NULL, PRIMARY KEY (name, published_date), FOREIGN KEY (author_id) REFERENCES authors(author_id), FOREIGN KEY (publisher_id) REFERENCES publishers(publisher_id) ); |
Then we insert some lines of data:
123456 |
INSERT INTO authors (name, birthday) VALUES ('Iain Banks', '1954-02-16'); INSERT INTO authors (name, birthday) VALUES ('Iain M Banks', '1954-02-16');INSERT INTO publishers (name, address) VALUES ('Abacus', 'London'); INSERT INTO publishers (name, address) VALUES ('Orbit', 'New York'); INSERT INTO books (name, author_id, publisher_id, published_date) VALUES ('The Wasp Factory', 1, 1, '1984-02-16'); INSERT INTO books (name, author_id, publisher_id, published_date) VALUES ('Consider Phlebas', 2, 3, '1988-04-14'); |
You may well have spotted the error with the last insert — we’ll come to that later.
You should now have a books database file:

Now target the books database with Datasette just by using that filename:

Your fresh Datasette frontend is on the URL mentioned:

I hadn’t noticed the error initially, but I can see it clearly now as we browse the books table:

I need to alter my first book entry so that the publisher_id is updated to 2. I’ll do that in SQLite3:

Refreshing the page, we see the correction:

Note the little cog above the columns; these allow you to make facets from any column data.

## Conclusion
I note there is a [SaaS platform](https://www.datasette.cloud/) built on Datasette that will allow SQL DDL commands. Another interesting addition is [enrichments](https://simonwillison.net/2023/Dec/1/datasette-enrichments/), that trigger scripting against rows — which feels like a sensible way to extend the framework.

As with Tiddlywiki, Datasette is more functional than pretty — because it is designed to be used, not sold. But the code is available, and the plugins should allow you to mold the frontend to your needs.

[
YOUTUBE.COM/THENEWSTACK
Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.
](https://youtube.com/thenewstack?sub_confirmation=1)