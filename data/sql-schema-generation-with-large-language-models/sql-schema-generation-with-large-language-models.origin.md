# SQL Schema Generation With Large Language Models
![Featued image for: SQL Schema Generation With Large Language Models](https://cdn.thenewstack.io/media/2024/05/834e66d0-getty-images-4aw2worpv5o-unsplash-1-1024x690.jpg)
I’ve looked at both
[regex](https://thenewstack.io/using-ai-to-help-developers-work-with-regular-expressions/) and [JSON persistence](https://thenewstack.io/coding-test-for-llama-3-implementing-json-persistence/) generation with LLMs, but it is Structured Query Language (SQL) that many believe is [handled well by AI](https://thenewstack.io/the-future-of-sql-conversational-hands-on-problem-solving/). To help celebrate SQL’s [50th birthday](https://www.dataversity.net/sql-at-50-a-lesson-in-how-to-stay-relevant-around-data/), let’s talk tables, introducing technical terminology as we need it. However, I don’t want to simply [test queries against existing tables](https://thenewstack.io/how-to-write-sql-queries/). The world of **relational databases** starts with the **schema**.
A schema describes a group of tables that interact to allow SQL queries to answer questions about real world system models. We use various
**constraints** to control how the tables relate to each other. In this example, I’ll develop a schema about books, authors and publishers. Then we’ll see if an LLM can reproduce the work.
We start with the
**relationships** between our things. A book is written by an author and published by a publisher. Indeed, the publication of a book defines the relationship between author and publisher.
So in concrete terms, we want to produce a result like this:
|Book
|Author
|Publisher
|Release Date
|The Wasp Factory
|Iain Banks
|Abacus
|16 February 1984
|Consider Phlebas
|Iain M. Banks
|Orbit
|14 April 1988
This reads nicely (we will return to it later), but the table itself would be a poor way to maintain more information.
If the publisher’s name is just a string, it might need to be entered many times — which is both inefficient and error prone. The same for author. Those of a literary bent will know that the author (Iain Banks) is the same for both books, but he used a slightly altered pseudonym when writing science fiction.
What if the book was released again later by a different publisher? To be certain to distinguish between the two publication events, we would need both the book’s titles and the release date — so our
**primary key** or unique identification must include both. We want the system to reject any attempts to enter two books with the same title and publication date.
Instead of using one big table, let’s use three tables and references to them where needed. One for authors, one for publishers, and one for books. We write the details of the author in the Authors table, and then reference them in the Books table using a
**foreign key.**
So here are the schema tables written in Data Definition Language (
**DDL**). I’m using the MySQL variant — annoyingly, all the vendors still maintain slightly different dialects.
First, the authors table. We add an automatic ID column index as a primary key. We don’t actually solve the pseudonym problem (I’ll leave that for readers):
|
1
2
3
4
5
6
|
CREATE TABLE Authors (
ID int NOT NULL AUTO_INCREMENT,
Name varchar(255) not null,
Birthday date not null,
PRIMARY KEY (ID)
);
The publishers table follows the same pattern. The “NOT NULL” is another constraint to prevent data being added without content.
|
1
2
3
4
5
6
|
CREATE TABLE Publishers (
ID int NOT NULL AUTO_INCREMENT,
Name varchar(255) not null,
Address varchar(255) not null,
PRIMARY KEY (ID)
);
The Books table will refer to the foreign keys, which leaves it logical but slightly unreadable. Note that we respect that the title of the book together with its publication date makes up the primary key.
|
1
2
3
4
5
6
7
8
|
CREATE TABLE Books (
Name varchar(255) NOT NULL,
AuthorID int, PublisherID int,
PublishedDate date NOT NULL,
PRIMARY KEY (Name, PublishedDate),
FOREIGN KEY (AuthorID) REFERENCES Authors(ID),
FOREIGN KEY (PublisherID) REFERENCES Publishers(ID)
);
To see a neat table like the one at the top, we need a
**view**. This is just a way of sewing together tables so that we can pick out the information we need to display, while leaving the schema untouched. Now that we have the schema written down, we can construct our view:
|
1
2
3
4
5
|
CREATE VIEW ViewableBooks AS
SELECT Books.Name 'Book', Authors.Name 'Author', Publishers.Name 'Publisher', Books.PublishedDate 'Date'
FROM Books, Publishers, Authors
WHERE Books.AuthorID = Authors.ID
AND Books.PublisherID = Publishers.ID;
Let’s see if we can produce our schema in an online playground so that we don’t have to install a database.
[DB Fiddle](https://www.db-fiddle.com/f/6Fj2vw8bFhzVADG4UFUjD6/0) should do the job.
If you enter the DDL and then add the actual data:
|
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
|
INSERT INTO Authors (Name, Birthday)
VALUES ('Iain Banks', '1954-02-16');
INSERT INTO Authors (Name, Birthday)
VALUES ('Iain M Banks', '1954-02-16');
INSERT INTO Publishers (Name, Address)
VALUES ('Abacus', 'London');
INSERT INTO Publishers (Name, Address)
VALUES ('Orbit', 'New York');
The results of looking at the view is shown below as ‘Query 3’ in DB Fiddle, and it is the data we wanted to see all along:
## Can an LLM Also Create Schemas?
OK, so now we want to ask an LLM about creating schemas. To summarize how we want to guide the LLM:
- When asked in English for a schema, we want it to generate the DDL for three tables, with indexes and constraints.
- We can also hint at the need for constraints (primary keys, foreign keys, etc.) if we need to.
- We can ask for a view.
- We can nudge it toward MySQL syntax, if needed.
I’ll use
[Llama 3](https://thenewstack.io/coding-test-for-llama-3-implementing-json-persistence/), but I also looked at OpenAI’s LLMs and got much the same results.
Our first query: “Create a relational database schema to describe books, publishers and authors.”
And the results:
So far so good. It hasn’t created the DDL, but we can ask that separately. It has in some ways done better by describing the schema in English. Let’s look at the rest of the reply:
It has described foreign key constraints and added the ISBN, which I didn’t think of. Also “PublicationDate” is better English than my “PublishedDate.” And it made one more table:
This solves the problem for multiple authors for one book — not a problem I was thinking about. The term
**bridge table** indicates the joining of the two tables (books and authors) via foreign keys.
Let’s ask for the DDL: “Show me the data definition language for this schema.”
These came back correctly, including the NOT NULLs to ensure no empty entries. It also noted that the DDL was in some ways “generic” due to differences between vendor SQLs in the real world.
Finally, let’s ask for a view:
This is a much more complicated version than mine; however, when adapted for my schema naming, it works just fine in DB Fiddle. The table
**alias** naming seen here doesn’t really help with comprehension.
## Conclusion: LLMs Can Indeed Do Schemas
I’d say this was a big win for LLMs, as they turned my English description into a well-constrained schema and then executable DDL, while also providing explanations (although those slipped into more technical relationship details). I didn’t even use a specialist LLM or service, so this worked out well.
To some degree, this is a mapping of one domain (the publishing world) into another (the domain-specific language of SQL), and this works heavily to an LLM’s strengths. Each domain is well-defined and deep with detail.
So, happy birthday SQL, and hopefully LLMs will keep you relevant for a few decades more!
[
YOUTUBE.COM/THENEWSTACK
Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.
](https://youtube.com/thenewstack?sub_confirmation=1)