# Python’s Collection Module for Specialized Data Structures
![Featued image for: Python’s Collection Module for Specialized Data Structures](https://cdn.thenewstack.io/media/2024/03/debf09cc-heather-m-edwards-tac5veacyia-unsplash-1024x747.jpg)
The
[Python programming language](https://thenewstack.io/an-introduction-to-python-for-non-programmers/) includes a number of built-in container data types, such as [lists](https://thenewstack.io/python-for-beginners-lists/), [tuples](https://thenewstack.io/python-for-beginners-when-and-how-to-use-tuples/) and [dictionaries](https://thenewstack.io/python-the-many-ways-to-merge-a-dictionary/). Think of containers as [objects that contain other objects](https://thenewstack.io/python-oop/). For example, a list is an object, and it might contain objects like orange, apple, banana, peach. A dictionary is an object that contains * key:value* pairs, like “fruit”: “Apple”, “vegetable”: “Tomato”, “season”: “Salt”.
For the most part, the built-in containers will be enough for you. But when you need to be able to manipulate specialized data structures, you’ll want to turn to the collections module. Those basic containers don’t need to be imported. But when you need something a bit more complicated, you’ll turn to the collections module, which adds the following containers:
**Counter** **—**a subclass of the dictionary container; used to count the occurrences of an element as an iterable. **NamedTuple** **—**similar to a class, but without having to define a full class, and creates a subclass of Tuples with named fields. **OrderedDict** **—**dictionary subclass that returns a default value, should a requested key be missing. **Deque** **—**a double-ended queue that supports the adding and removing of elements from either the beginning or the end.
There are other containers (
*ChainMap*, *UserDict*, *UserList* and *UserString*), but we’ll focus on the four above.
Now that you know what the collections module offers, let’s see how each container works.
## Counter
The counter container makes it possible to count objects in a container. Let’s say you need to count the instances of letters in a specific word. We’ll use the word subbookkeeper (because it’s fun to say and has a lot of repeating letters).
Before we use counter, we have to import collections like this:
|
1
|
import collections
Next, we’ll define two variables:
|
1
2
|
word = subbookkeeper
counter = {}
With counter
*= {}* we’ve defined a dictionary without a value so it will serve as a placeholder.
Okay, now we’re going to create a for loop to iterate through our defined variable using a counter to count the objects in a container.
The for loop looks like this:
|
1
2
3
4
|
for letter in word:
if letter not in counter:
counter[letter] = 0
counter[letter] += 1
What the for loop does is iterate through the counter, adding the number of instances of each object.
Finally, we use the
* print()* function like this:
|
1
|
print(counter)
Our entire application looks like this:
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
import collections
word = "subbookkeeper"
counter = {}
for letter in word:
if letter not in counter:
counter[letter] = 0
counter[letter] += 1
print(counter)
Run the above and the output will be:
|
1
|
{'s': 1, 'u': 1, 'b': 2, 'o': 2, 'k': 2, 'e': 3, 'p': 1, 'r': 1}
## NamedTuple
With NamedTuple, we can create data structures that are similar to a class but without having to define a full class. This can be very handy when dealing with details about an object. For instance, say you’re creating an app that adds details for a student and you don’t want to create a full-blown class. For that, you can make use of NamedTuple.
Before you use it, you must import it from collections like this:
|
1
|
from collections import namedtuple
Next, we define Student with the namedtupule container and then create a tuple with fname, name, major and birthday like this:
|
1
|
Student = namedtuple('Student', ['fname', 'lname', 'major', 'birthday'])
We’ll now define S and inject data into the tuple like so:
|
1
|
S = Student('Jack', 'Wallen', 'theatre', '10311967')
Finally, we’ll print the first name using the index position 0 with these two lines:
|
1
2
|
print("First name using the index is : ", end="")
print(S[0])
We then print the major using the keyname like so:
|
1
2
|
print("Major using keyname is : ", end="")
print(S.major)
Our entire app looks like this:
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
from collections import namedtuple
Student = namedtuple('Student', ['fname', 'lname', 'major', 'birthday'])
S = Student('Jack', 'Wallen', 'theatre', '10311967')
print("First name using the index is : ", end="")
print(S[0])
print("Major using keyname is : ", end="")
print(S.major)
## OrderedDict
The OrderedDict container will always preserve the order of a sequence during iteration. Let’s say you have a dictionary of keypairs that look like letter = name and you always wanted the order in which they are defined to be preserved. For example, you might have:
a = Camille
b = Colette
c = Aaron
d = Clara
You might want to change out one name without changing the a, b, c, d order. This key value change is inherent in OrderedDict and is used like this:
From collections import OrderedDict.
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
|
print("Original:\n")
dict = OrderedDict()
dict['a'] = "Camille"
dict['b'] = "Colette"
dict['c'] = "Aaron"
dict['d'] = "Clara"
for key, value in dict.items():
print(key, value)
print("\nChanged:\n")
dict['c'] = "Jean"
for key, value in dict.items():
print(key, value)
If you were to run the above, the output would be:
Original:
a Camille
b Colette
c Aaron
d Clara
Changed:
a Camille
b Colette
c Jean
d Clara
As you can see, we retained the key order, even when the value of c changed.
## Deque
Deque can be very helpful because it allows you to append a value to a collection either on the beginning or end.
Let’s say we have the following code:
|
1
2
3
4
5
|
from collections import deque
queue = deque(['name','age','major'])
print(queue)
Run that app and you get:
deque([‘name’, ‘age’, ‘major’])
Awesome.
Now, let’s say you want to add minor to the right of the collection. That could be achieved with the following addition:
|
1
2
3
4
|
queue.append('minor')
print("\nThe container after appending to the right is: ")
print(queue)
If we run the app now, we get:
|
1
|
deque(['name', 'age', 'major'])
The container after appending to the right is:
|
1
|
deque(['name', 'age', 'major', 'minor'])
Let’s append year to the left of the container with this addition to our code:
|
1
2
3
4
|
queue.appendleft('Senior')
print("\nThe container after appending to the left is: ")
print(queue)
Our output would now be:
|
1
|
deque(['name', 'age', 'major'])
The container after appending to the right is:
|
1
|
deque(['name', 'age', 'major', 'minor'])
The container after appending to the left is:
|
1
|
deque(['Senior', 'name', 'age', 'major', 'minor'])
There you go. Four very cool ways to manipulate collections, thanks to the collections module. Although you might not work with these early on, eventually you’ll find them invaluable for manipulating data within a collection.
[
YOUTUBE.COM/THENEWSTACK
Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.
](https://youtube.com/thenewstack?sub_confirmation=1)