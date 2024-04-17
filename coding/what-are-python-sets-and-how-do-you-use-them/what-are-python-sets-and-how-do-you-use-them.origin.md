# What Are Python ‘Sets’ and How Do You Use Them?
![Featued image for: What Are Python ‘Sets’ and How Do You Use Them?](https://cdn.thenewstack.io/media/2024/04/d6b02580-libby-penner-qw5xllbdeao-unsplash-1-1024x684.jpg)
A
[Python](https://thenewstack.io/what-is-python/) Set is a collection [data type](https://thenewstack.io/python-for-beginners-data-types/) that is iterable, mutable, and cannot be duplicated. This data type can come in very handy. Say, for example, you need to store information for employee IDs. You certainly don’t want those IDs to be duplicated within the application, as that could lead to issues.
For example, you have the following employee IDs:
- 001
- 002
- 003
- 004
- …
You might attach specific information to each of those IDs, such as names, emails, phone numbers, birthdays, etc. Should the IDs get duplicated, the cross-pollination of data could lead to confusion or an application that doesn’t function as expected.
Sets can contain as many items as needed and can even be of different types, such as
[strings](https://thenewstack.io/what-are-python-f-strings-and-how-do-you-use-them/), integers, [tuples](https://thenewstack.io/python-for-beginners-when-and-how-to-use-tuples/), float, etc.).
The primary use cases for sets include removing duplicate entries, checking set membership, and performing certain mathematical operations (such as union, intersection, difference, and symmetric difference).
Python includes the built-in set() function that makes it simple to create Sets like so:
|
1
|
set1 set([2, 2, 2, 4, 4, 4, 6, 8, 8, 10])
What you see above is a set that includes a list of numbers, some of which repeat. What if we wanted to ensure those repeated numbers are removed? Thanks to set(), that functionality is built in. For example, we can print set1 with the line:
|
1
|
print('Set1: ', set1)
Our entire block of code looks like this:
|
1
2
|
set1 = set([2, 2, 2, 4, 4, 4, 6, 8, 8, 10])
print('Set1: ', set1)
If we run the about, set() would remove all duplicate numbers so the output would be:
|
1
|
Set1: {2, 4, 6, 8, 10}
Remember, Sets can also include mixed types, so we could have a set that looks like this:
|
1
|
set2 = set((1, 1, 3, 5, 'cat', 'dog', 'mouse', 'mouse'))
The above Set uses a tuple instead of a list. We could add a print line for that Set like so:
|
1
|
print('Set2: ', set2)
Our entire block of code now looks like this:
|
1
2
3
4
|
set1 = set([2, 2, 2, 4, 4, 4, 6, 8, 8, 10])
set2 = set((1, 1, 3, 5, 'cat', 'dog', 'mouse', 'mouse'))
print('Set1: ', set1)
print('Set2: ', set2)
The output would then be:
|
1
2
|
Set1: {2, 4, 6, 8, 10}
Set2: {1, 3, 'dog', 5, 'cat', 'mouse'}
All duplicates have been removed.
Another method of enclosing a set is with {}, like this:
|
1
|
set3 = {2, 2, 4, 6, 6, 'cat', 'dog', 'mouse', 'mouse', 3.14, (3, 2, 1)}
The output for the final set would be:
|
1
|
Set3: {'cat', 2, 3.14, 'dog', 4, 6, (3, 2, 1), 'mouse'}
One thing to notice is that we do have a duplicated element… 2. How did that happen? Because (1, 2, 3) is an element unto itself. If we duplicated that element only one instance would print. That set might look like this:
|
1
|
set3 = {2, 2, 4, 6, 6, 'cat', 'dog', 'mouse', 'mouse', 3.14, (3, 2, 1), (3, 2, 1)}
Run the app and the Set3 output will remain:
|
1
|
Set3: {'cat', 2, 3.14, 4, 6, 'mouse', (3, 2, 1), 'dog'}
So the (3, 2, 1) duplicate was also removed.
It is also to check if an element is present or not within a Set. This is accomplished with the in keyword. The results of the check will be either True or False.
For instance, we want to check to see if cat is found within set3, from within the print() statement, which can be done like so:
|
1
|
print('cat' in set3)
We can add that to our full block of code like this:
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
set1 = set([2, 2, 2, 4, 4, 4, 6, 8, 8, 10])
set2 = set((1, 1, 3, 5, 'cat', 'dog', 'mouse', 'mouse'))
set3 = {2, 2, 4, 6, 6, 'cat', 'dog', 'mouse', 'mouse', 3.14, (3, 2, 1), (3, 2, >
print('cat' in set3)
print('Set1: ', set1)
print('Set2: ', set2)
print('Set3: ', set3)
If we run the above, the output would look like this:
*True
* *Set1: {2, 4, 6, 8, 10}*
*Set2: {1, 3, 5, ‘cat’, ‘mouse’, ‘dog’}*
*Set3: {2, 3.14, 4, 6, ‘cat’, (3, 2, 1), ‘mouse’, ‘dog’}*
We can run the opposite check like this:
|
1
|
print('cat' not in set3)
Our output would now look like this:
*True
* *False*
*Set1: {2, 4, 6, 8, 10}*
*Set2: {1, 3, 5, ‘cat’, ‘mouse’, ‘dog’}*
*Set3: {2, 3.14, 4, 6, ‘cat’, (3, 2, 1), ‘mouse’, ‘dog’}*
We can also create empty sets, like this:
|
1
|
empty_set1 = set()
We can then run a test for the data type of our new set, like this:
|
1
|
print('Data type of our empty set = ', type(empty_set1))
The output of the above would be:
*Data type of our empty set = <class ‘set’>*
If you need to add or update items within a set, that’s also possible. Say our Set is:
|
1
|
set1 = {21, 12, 21, 42, 33}
Let’s print that Set with:
|
1
|
print('Initial Set:',set1)
The output would be:
*Initial Set: {33, 42, 12, 21}*
Again, set() drops the duplicated 21.
We can add to the set with the add() function, like so:
|
1
|
set1.add(32)
Add another print line for the update that looks like this:
|
1
|
print('Updated Set:', set1)
The new output would be:
|
1
2
|
Initial Set: {33, 42, 12, 21}
Updated Set: {32, 33, 42, 12, 21}
We can also use update() for the Set. Let’s say we have two sets that are:
|
1
2
|
set1 = {'Tom Sawyer', 'Analog Kid', 'Between The Wheels'}
set2 = {'La Villa Strangiato', 'YYZ', 'Main Monkey Business'}
We then use the update() function like so:
|
1
|
set1.update(set2)
Add a print statement like so:
|
1
|
print(set1)
The output for this block of code would be:
*{‘Tom Sawyer’, ‘Main Monkey Business’, ‘YYZ’, ‘Analog Kid’, ‘Between The Wheels’, ‘La Villa Strangiato’}*
Finally, we’ll remove an element from a Set using the
*discard()* function, like so:
|
1
|
removedValue = set1.discard('Between The Wheels')
Our code will look like:
|
1
2
3
4
5
6
7
|
set1 = {'Tom Sawyer', 'Analog Kid', 'Between The Wheels'}
print('Initial Set:',set1)
removedValue = set1.discard('Between The Wheels')
print('Set after discard:', set1)
Our output is now:
*Initial Set: {‘Tom Sawyer’, ‘Between The Wheels’, ‘Analog Kid’}*
*Set after discard: {‘Tom Sawyer’, ‘Analog Kid’}*
And that’s the basics of Sets in Python. This feature will come in handy when you need to remove duplicates or check for elements from various data types. To find out more about what you can do with Sets, make sure to check out the
[official documentation](https://docs.python.org/2/library/sets.html). [
YOUTUBE.COM/THENEWSTACK
Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.
](https://youtube.com/thenewstack?sub_confirmation=1)