# Insert Data into a MySQL Database via a Python Script
![Featued image for: Insert Data into a MySQL Database via a Python Script](https://cdn.thenewstack.io/media/2021/11/ab06a958-pythonlogo.png)
I want to show you something pretty cool that [Python](https://thenewstack.io/what-is-python/) can do: Insert data into a MySQL database table.

Imagine being able to inject data into a table without having to log into the MySQL console first — and injecting that data from a Python application can be incredibly flexible and handy. Even better, it’s not all that much of a challenge.

Let me show you how it’s done.

## What You Need
I’m going to demonstrate this on an instance of Ubuntu Server 22.04.3. If you’re using a different Linux distribution (or if you’re using either MacOS or Windows), you’ll have to alter the installation commands. With that said, you’ll need an OS that supports Python3 and a user with* sudo* privileges.

And, just for fun, I’m going to show you how to install MySQL and create a user and database.

Groovy. Let’s make some Python/database magic.

## Installing MySQL and Python
The first thing we’re going to do is install the MySQL database server. To do that, log into your instance of Ubuntu Server and prepare to install.

1 |
sudo apt-get install mysql-server -y |
### Installing MySQL on Ubuntu
When that finishes, you’ll want to enable the service, so it runs at boot. To do that, issue the command:

1 |
sudo systemctl enable --now mysql |
### Install the Python MySQL Connector
Before you continue, you must also install the Python3 MySQL Connector, which allows Python to interact with your MySQL databases. This can be accomplished with the command:

1 |
sudo apt-get install python3-mysql.connector -y |
If your Ubuntu instance doesn’t already have Python installed, you can do so with the command:
1 |
sudo apt-get install python3 -y |
That’s it for the installation.
## Creating a Database and User in MySQL
### Create a MySQL database
Next, we need to create a database. Log into the MySQL console with the command:

1 |
sudo mysql |
Once there, create a database named “staff” with the command:
1 |
CREATE DATABASE staff; |
### Create a MySQL user
Now, we can create a user (we’ll name it “jack”) and give that user permission to use the new database. Create the user with:

1 |
CREATE USER 'jack'@'localhost' IDENTIFIED BY 'PASSWORD'; |
Make sure PASSWORD is a strong, unique password.
Give that user access to our staff database with the command:

1 |
GRANT ALL PRIVILEGES ON staff.* TO 'jack'@'localhost'; |
## Create a Table
We now have to create a table. First, change to the staff database with:

1 |
USE staff; |
Now, we can create a table on our new database. Let’s keep it simple and create a table called “editorial” with two columns (name and email). The command for that would be:
1 |
CREATE TABLE editorial (id INT, name VARCHAR(30), email VARCHAR(30)); |
We now have a database, a user, and a table ready for action.
**Creating the Python Application**
This is where the fun starts. We’re going to create a Python application that injects data into the name and email columns of the editorial columns.

Create the script with the command:

1 |
nano insert.py |
In that file, paste the following content:
123456789101112131415 |
import mysql.connectormydb = mysql.connector.connect( host="localhost", user="jack", password="PASSWORD", database="staff")mycursor = mydb.cursor()sql = "INSERT INTO editorial (name, email) VALUES (%s, %s)"val = ("NAME", "EMAIL")mycursor.execute(sql, val)mydb.commit()print(mycursor.rowcount, "record inserted.") |
PASSWORD is the password you created for the MySQL user jack, NAME is the name you want to insert into the name column and EMAIL is the address you want to insert into the email column.
Here’s a bit more explanation:

- The first line imports the required function that allows Python to connect to MySQL.
- The mydb section configures the information for the database.
- mydb.cursor() is the function that allows the insertion of data into the database.
- The sql line is our first MySQL query.
- The val line defines our columns for the database.
- The mycursor.execute executes the above operations.
- The mydb.commit() confirms the changes made by mycursor.execute.
- The print line prints output to indicate success or failure.
Save and close the file with the Ctrl+X key combination.

**Running the App**
We can now run our new Python app that will inject the data into the table that you specified in the script. The run command for this would be:

1 |
python3 insert.py |
You should receive confirmation that the injection was successful. You can verify this with the command:
1 |
SELECT * FROM editorial; |
You should see your first data added to the table.
## Accept Input from a User
That’s not a very efficient method of injecting data into a database because you’d have to edit the script every time. Fortunately, we can use variables in Python to accept input that will then be inserted.

To do this, we have to make use of the input() function, which allows the script to accept input from a user. Our new script would look like this:

12345678910 |
import mysql.connectorname = input("Type a name: ")email = input("Type an email: ")mydb = mysql.connector.connect( host="localhost", user="jack", password="PASSWORD", database="staff") |
1234567 |
mycursor = mydb.cursor()sql = "INSERT INTO editorial (name, email) VALUES (%s, %s)"val = (name, email)mycursor.execute(sql, val)mydb.commit() |
PASSWORD is the password you set for the MySQL user.
Save and close the file. Run the app in the same way, only this time you’ll be prompted to input a name and then an email.

And that’s how you can use Python to inject data into a MySQL table. Play around with this and see how creative you can get.

## Python/MySQL Connectivity FAQ
### Q: What is the most common way to connect to a MySQL database using Python?
A: The most common method is by using the mysql-connector-python library, which provides a simple and efficient interface for interacting with MySQL databases.


### Q: How do I install the mysql-connector-python library in my Python environment?
A: You can install it via pip with the command *pip install mysql-connector-python*, or use conda like so *conda install -c anaconda mysql-connector-python.*

### Q: What is a MySQL connection pooler, and how do I set one up?
A: A connection pooler is a mechanism that allows multiple connections to be shared between applications. The most popular library for this purpose in Python is mysql-connection-pooling.


### Q: What are some common MySQL connection errors, and how do I troubleshoot them?
A: Common connection errors include:


- mysql-connector-python.errors.Error: General database error messages.
- mysql.connector.exceptions.OperationalError : Connection issues (e.g., timeout).
- mysql.connector.exceptions.ProgrammingError : Syntax or SQL-related errors.

To troubleshoot these errors, check your MySQL configuration files (my.cnf, etc.), ensure that the correct username and password are provided, and verify that the database connection details are accurate.


### Q: Can I use other libraries to connect to a MySQL database in Python?
A: Yes. Some popular alternatives include:


- sqlalchemy : An ORM library for working with SQL databases.
- pymysql: Another connector library that provides similar functionality to mysql-connector-python.
- PyMySQL (no module): Similar to the one above.

### Q: What is a connection timeout in MySQL, and how do I adjust it?
A: A connection timeout is the time period allowed for a connection attempt to succeed. By default, this value can be adjusted via configuration files (my.cnf, etc.).

[
YOUTUBE.COM/THENEWSTACK
Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.
](https://youtube.com/thenewstack?sub_confirmation=1)