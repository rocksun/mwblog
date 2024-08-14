# How To Use Inheritance in Python
![Featued image for: How To Use Inheritance in Python](https://cdn.thenewstack.io/media/2024/07/2e411f9b-getty-images-tngwwfmfhnq-unsplash-1024x683.jpg)
In [object-oriented programming](https://thenewstack.io/python-oop/), there’s a feature called inheritance that allows a new class to inherit the attributes and methods of an existing class. By using inheritance, you don’t have to always reinvent the wheel, which also means your code will be more concise and easier to read and debug.

First, what is a class?

Think of a class as a blueprint for creating objects, and also for defining the properties (attributes) and behaviors (methods) that will be associated with the objects created from the class. A class is like a template you can use and reuse within your code.

Inheritance requires two types of classes:

**Base class**(aka**parent class**): This is the class whose attributes and methods will be inherited.**Derived class**(aka**child class**): This is the class that inherits the attributes and methods.
There are five types of inheritance:

**Single inheritance**: A derived class inherits from a single base class.**Multiple inheritance**: A derived class inherits from multiple base classes.**Multilevel inheritance**: A class is derived from a class, which is derived from another class.**Hierarchical inheritance**: Multiple classes are derived from a single base class.**Hybrid inheritance**: A combination of two or more types of inheritance.
The benefits of using inheritance include:

[Code reusability](https://thenewstack.io/coding-from-scratch-creates-new-risks/)[Extensibility](https://thenewstack.io/webassembly-could-be-the-key-for-cloud-native-extensibility/)- Better code organization
The basic syntax of class inheritance looks like this:

12345 |
class baseClass: # Base class attributes and methodsclass derivedClass(baseClass) # Derived class attributes and methods |
Let’s first create a base class. This will make use of several concepts I’ve outlined throughout this [Python](https://thenewstack.io/python-mulls-a-change-in-version-numbering/) series.
We’ll create a base class that defines a person’s name and looks like this:

1234567 |
class Person: def __init__(fullName, fname, lname): fullName.firstname = fname fullName.lastname = lname def printname(fullName): print(fullName.firstname, fullName.lastname) |
Now that we’ve created our class, we then use it to create an object and print the object like so:
12 |
x = Person("Jack", "Wallen")x.printname() |
Put all of that together and it looks like this:
12345678910 |
class Person: def __init__(fullName, fname, lname): fullName.firstname = fname fullName.lastname = lname def printname(fullName): print(fullName.firstname, fullName.lastname)x = Person("Jack", "Wallen")x.printname() |
Run the above command and it will print “Jack Wallen”.
That’s the base class. We’ve create a derived class that inherits the attributes and methods from the base class (Person). This is the easy part. We’ll create a new class, named Staff, which inherits from Person. The class looks like this:

12 |
class Staff(Person) pass |
By using pass, we inform Python that we’re not adding any new attributes or methods to the new class.
We can then create a new object from the derived class like so:

1 |
x = Staff("Olivia", "Nightingale") |
Print the new object with:
1 |
x.printname() |
The entire code now looks like this:
12345678910111213141516 |
class Person: def __init__(fullName, fname, lname): fullName.firstname = fname fullName.lastname = lname def printname(fullName): print(fullName.firstname, fullName.lastname)x = Person("Jack", "Wallen")x.printname()class Staff(Person): passx = Staff("Olivia", "Nightingale")x.printname() |
Run the above code and it will print:
Jack Wallen
Olivia Nightingale

Remember that we previously used pass because we didn’t want to add any new attributes or methods to the new class. Now, we’re going to add new attributes and methods to a new class. We’ll stick with something similar to our original — our base class. This time around the base class is:

12345678910 |
class Person(object): def __init__(fullName, name): fullName.name = name def getName(fullName): return fullName.name def isEmployee(fullName): return False |
We’ve added two new functions above, `getName`
(to return the full name of the person) and `isEmployee`
(assuming `isEmployee`
equals false).
Next, we’ll create a derived class to define that `isEmployee`
equals True, which looks like this:

1234 |
class Employee(Person): def isEmployee(fullName): return True |
So far, we have a class called Person and one called Employee. As you might assume, Person is not an employee, whereas Employee is. You’ll see that in action below with:
12345 |
emp = Person("Jack Wallen")print(emp.getName(), emp.isEmployee())emp = Employee("Olivia Nightingale")print(emp.getName(), emp.isEmployee()) |
You should be able to guess what’s going to happen. Since Jack Wallen is an object of the Person class, they’ll not be listed as an employee, whereas Olivia Nightingale, who is an object of the Employee class, is.
The entire code looks like this:

123456789101112131415161718192021 |
class Person(object): def __init__(fullName, name): fullName.name = name def getName(fullName): return fullName.name def isEmployee(fullName): return Falseclass Employee(Person): def isEmployee(fullName): return Trueemp = Person("Jack Wallen")print(emp.getName(), emp.isEmployee())emp = Employee("Olivia Nightingale")print(emp.getName(), emp.isEmployee()) |
Run the above and the output will be:
Jack Wallen False
Olivia Nightingale True

Pretty nifty, eh?

## Using the super() Function
There’s also the `super()`
function, which forces the derived class to inherit all attributes and methods from the base class. This time around, we’re going to focus on students and their graduation year.

The `super()`
function is used like this:

1234 |
class Student(Person): def __init__(fullName, fname, lname, year): super().__init__(fname, lname) fullName.graduationyear = year |
The explanation of the `super()`
function (in the above example) is:
`super()`
: Returns a temporary object of the superclass that allows the calling of its methods`__init__()`
: The Python constructor method used for initializing new objects`(fname, lname)`
: Parameters passed to the superclass constructor
Our entire code looks like this:

123456789101112131415161718 |
class Person: def __init__(fullName, fname, lname): fullName.firstname = fname fullName.lastname = lname def printname(fullName): print(fullName.firstname, fullName.lastname)class Student(Person): def __init__(fullName, fname, lname, year): super().__init__(fname, lname) fullName.graduationyear = year def welcome(fullName): print("Welcome", fullName.firstname, fullName.lastname, "to the class of", fullName.graduationyear)x = Student("Jack", "Wallen", 2026)x.welcome() |
Run the above code and the output would be:
Welcome Jack Wallen to the class of 2026

And that’s the basics of Python inheritance. To learn more about inheritance, check out the [official Python documentation on the subject](https://docs.python.org/3/tutorial/classes.html#inheritance).

[
YOUTUBE.COM/THENEWSTACK
Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.
](https://youtube.com/thenewstack?sub_confirmation=1)