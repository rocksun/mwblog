# How (and When) to Use a Python While Loop
![Featued image for: How (and When) to Use a Python While Loop](https://cdn.thenewstack.io/media/2024/04/32cec1d4-etienne-girardet-chp1itgplka-unsplash-1-1024x768.jpg)
While loops are an essential aspect of
[programming](https://thenewstack.io/why-literate-programming-might-help-you-write-better-code/). What a while [loop](https://thenewstack.io/how-to-use-loops-in-python/) does is continue executing a statement (or set of statements) until a specific condition has been met. An obvious example (that many will understand) could be something like this: *While my bank account has money, I can buy things.*
The statement is
*I can buy things* and the condition is *While my bank account has money*. When you’ve spent all of your money, you can no longer buy things (or pay bills).
While loops are a great option for when you need to execute a statement (or multiple statements) repeatedly. The difference between
* for* and *while* loops is that the *for* loop simply iterates through a collection (or an iterative object) and is finished, whereas the *while* loop continues until the specific condition is met.
The
*for* loop is easier to use but there will be instances when a *while* loop is required. For example, you might not know when the number of times the statement has to be repeated.
Let’s take a look at basic examples of
[Python](https://thenewstack.io/python/) loops that do the same thing. First, a for loop that will print out numbers of a range. That loop could look like this:
|
1
2
|
for i in range(11):
print (i)
We’ve set the for loop to print i for a range of 11. The output of that code would look like this:
*0*
*1*
*2*
*3*
*4*
*5*
*6*
*7*
*8*
*9*
*10*
Remember, in programming, numbering starts at 0, so a range of 11 would go from 0-10.
Now, let’s do the same thing with a
*while* loop. The first thing we must do is define *i* with:
|
1
|
i = 1
Next, we create the lop that states while i is less than 11, print i in increments of 1. That loop looks like:
|
1
2
3
|
while i < 11:
print(i)
i += 1
The entire code is:
|
1
2
3
4
|
i = 1
while i < 11:
print(i)
i += 1
If we run the above code, we get the same output that we did from the
*for* loop.
But what about running the
*while* loop when the condition is unknown? Say, for example, you want to accept input of names from a user and allow them to keep typing names until they’re finished. When they’ve typed all of the names, they can type *end* to exit the loop. Quit is the condition and accepting names from input is the statement.
The first thing we do is define
*names* as an empty list like this:
|
1
|
names = []
Next, we’ll define
*new_name* as anything but quit. In this case, we’ll define it as empty like so:
|
1
|
new_name = ' '
We can now write our loop that will accept input from the user as such:
|
1
2
3
4
|
while new_name != 'end':
new_name = input("Type the names to be added and end with 'end: ")
names.append(new_name)
We’re using the append function to take on the new names typed after the previous name.
Finally, we print names with:
|
1
|
print(names)
The entire code looks like:
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
|
names = []
new_name = ''
while new_name != 'end':
new_name = input("Type the names to be added and end with 'end': ")
names.append(new_name)
print(names)
Run the above code and it will instruct the user to type names and end the run by typing
*end*. The output might look something like this: *[‘Aaron Kennedy’, ‘Camile St. Joan’, ‘Anton Frank’, ‘Jean Barber’, ‘Clara Beach’, ‘end’]*
The problem with the above is that the output includes
*end*, which isn’t a name. We can fix that with a *for* loop that defines *new_name* as anything but *end* like so:
|
1
2
|
if new_name != 'end':
names.append(new_name)
Now, our code looks like this:
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
names = []
new_name = ''
while new_name != 'end':
new_name = input("Type the names to be added and end with 'end': ")
if new_name != 'end':
names.append(new_name)
print(names)
If we type the same names as we did above and end by typing end (and hitting enter), the output will now look like:
*[‘Aaron Kennedy’, ‘Camile St. Joan’, ‘Anton Frank’, ‘Jean Barber’, ‘Clara Beach’]*
Fixed.
Here’s another example that accepts user input but offers them a menu from which to choose. We’ll offer different types of food. First, we instruct the user what to do with the statement:
|
1
|
print("\nWelcome to the food ordering center. What would you like to eat today?")
Next, we define
*choice* as an empty variable with:
|
1
|
choice = ' '
Next comes our while look that will inform the user of the options, accept input, output text based on their input, and end if the user types
*q*. The loop looks like this: *while choice != ‘q’:* * print(“\n[1] Enter 1 to order Thai.”)*
* print(“[2] Enter 2 to order Indian.”)*
* print(“[3] Enter 3 to order Mexican.”)*
* print(“[4] Enter 4 to order Chinese.”)*
* print(“[q] Enter q to quit.”)* * choice = input(“\nWhat kind of food would you like to order? “)*
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
12
|
if choice == '1':
print("\nEnjoy your Thai food!\n")
elif choice == '2':
print("\nEnjoy your Indian food!!\n")
elif choice == '3':
print("\nEnjoy your Mexican food!\n")
elif choice == '3':
print("\nEnjoy your Chinese food!\n")
elif choice == 'q':
print("\nThanks for ordering. Have a great day.\n")
else:
print("\nI don't understand that choice, please try again.\n")
Notice the last statement informs the user they’ve typed something beyond the scope of the app.
Finally, we print a goodbye message with:
|
1
|
print("Thank you and have a wonderful day.")
The entire code looks like this:
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
|
print("\nWelcome to the food ordering center. What would you like to eat today?")
choice = ''
while choice != 'q':
# Give all the choices in a series of print statements.
print("\n[1] Enter 1 to order Thai.")
print("[2] Enter 2 to order Indian.")
print("[3] Enter 3 to order Mexican.")
print("[4] Enter 4 to order Chinese.")
print("[q] Enter q to quit.")
choice = input("\nWhat kind of food would you like to order? ")
if choice == '1':
print("\nEnjoy your Thai food!\n")
elif choice == '2':
print("\nEnjoy your Indian food!!\n")
elif choice == '3':
print("\nEnjoy your Mexican food!\n")
elif choice == '3':
print("\nEnjoy your Chinese food!\n")
elif choice == 'q':
print("\nThanks for ordering. Have a great day.\n")
else:
print("\nI don't understand that choice, please try again.\n")
print("Thank you and have a wonderful day.")
When you run the app, it will print out:
*Welcome to the food ordering center. What would you like to eat today?* *[1] Enter 1 to order Thai.*
*[2] Enter 2 to order Indian.*
*[3] Enter 3 to order Mexican.*
*[4] Enter 4 to order Chinese.*
*[q] Enter q to quit.* *What kind of food would you like to order? *
The next output will be based on the users’ input. For example, if the user types
* 2*, the output would be: *Enjoy your Indian food!!*
The program ends when the user types
*q*.
And that’s the gist of Python
*while* loops. These loops are an essential programming aspect that you will use quite often in your code. [
YOUTUBE.COM/THENEWSTACK
Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.
](https://youtube.com/thenewstack?sub_confirmation=1)