# Advanced OOP in TypeScript: Interfaces and Abstract Classes
![Featued image for: Advanced OOP in TypeScript: Interfaces and Abstract Classes](https://cdn.thenewstack.io/media/2024/03/15db2836-abstract-classes-1024x576.jpg)
Many developers come to
[TypeScript](https://thenewstack.io/typescript/) after having programmed in [JavaScript](https://thenewstack.io/javascript/) for years. As a result, in a haste to get things done, some of these developers don’t take full advantage of the more advanced object-oriented features of TypeScript.
It’s understandable. The pressure to get code into production can be harsh and unrelenting. Having time to fully learn the principles of
[object-oriented programming (OOP)](https://thenewstack.io/why-are-so-many-developers-hating-on-object-oriented-programming/) in terms of TypeScript becomes a luxury. There’s a lot to know.
However, there are some essential principles of object-oriented programming that can not only be learned quickly, but will save time both when creating and maintaining an application. One set of principles is promoting code reuse, safety and versatility using interfaces and abstract classes.
Here I’ll describe how to create object-oriented applications in a way that puts interfaces and abstract classes at the forefront of the design process. In addition, I’ll demonstrate a technique in TypeScript for using interfaces in a way that is special to the language. All the code presented can be found in this
[GitHub repository](https://github.com/reselbob/AdvancedOop01_TS/).
To get full benefit from this tutorial, you should have experience programming in JavaScript, an understanding of how classes and inheritance work in object-oriented programming, and some experience using
[TypeScript and Node.js](http://node.js).
## Programming to the Interface
One of the important object-oriented features that TypeScript provides is support for Interfaces. An interface is a fundamental component of object-oriented programming that’s also available in languages such as
[Java](https://thenewstack.io/we-can-have-nice-things-upgrading-to-java-21-is-worth-it/), C#, and C++. Interfaces are not explicitly available in JavaScript
You can think of an interface as a template that defines the fields and methods signatures of a class. The interface describes the structure of the class, but not how it works. The “how it works” part is provided by the class implementing the interface. Depending on the programming language and use case, some interfaces will define fields only, some interfaces will define method signatures only, some interfaces will describe both fields and method signatures.
Listing 1 below shows the code for two interfaces,
[IAddress](https://github.com/reselbob/AdvancedOop01_TS/blob/main/src/document/interfaces/IAddress.ts) and [IPerson](https://github.com/reselbob/AdvancedOop01_TS/blob/main/src/document/interfaces/IPerson.ts), using TypeScript syntax. **Listing 1:** The interfaces that describe an Address and a Person.
All the fields defined for
IAddress, which is the top of the listing, must return a
string value. However, notice that the interface
IPerson, on the bottom, defines a field named
address at Line 7. The address field must return an object that implements the
IAddress interface. That object might have other fields and methods besides those defined by the
IAddress interface.
But, when developers write code that calls the
address field, they’ll only get back implementations of the methods and fields defined by
IAddress. Taking this interface-centric approach is called programming to the interface. This approach is particularly powerful when programming in TypeScript.
Take a look at Listing 2 below. It’s
[an excerpt from the demonstration TypeScript](https://github.com/reselbob/AdvancedOop01_TS/blob/5effbd298df912c39f7cb1faa3a0f7472069694e/src/randomizer/Randomizer.ts#L25) code that accompanies this article. The code uses the [Faker NPM library](https://www.npmjs.com/package/@faker-js/faker) to generate random data. Notice that the return type of the method [getRandomAddress()](https://github.com/reselbob/AdvancedOop01_TS/blob/5effbd298df912c39f7cb1faa3a0f7472069694e/src/randomizer/Randomizer.ts#L25) is an
IAddress interface. However, notice that the actual return type by the method is a dynamically created JavaScript object that has the
address1,
address2,
city,
stateProvince,
postalCode and
country fields that are defined by
IAddress.
**Listing 2:** The
getRandomAddress() method uses the demonstration application’s custom randomizer to return a JavaScript object that implements the
IAddress interface.
Creating a JavaScript object on the fly that supports the fields defined in a predefined interface is a perfectly acceptable way to implement an interface in TypeScript. In fact, dynamic implementation of an interface using a JavaScript object is one of the attractive features of TypeScript.
The
method from the demonstration application as shown in Listing 3 below is another example of creating a JavaScript object on the fly to implement an interface, in this case, the code is implementing the
[getRandomPerson()](https://github.com/reselbob/AdvancedOop01_TS/blob/5effbd298df912c39f7cb1faa3a0f7472069694e/src/randomizer/Randomizer.ts#L7)
IPerson interface.
**Listing 3:** Dynamically creating a JSON object to implement the
IPerson interface.
Notice in Listing 3, above, that the value assigned to the
address field at Line 10 is an
IAddress interface that’s returned from method
getRandomAddress(). This is an example of programming to the interface.
The method
getRandomAddress() is expected to return an object that supports the
IAddress interface. That object might have a number of methods and fields that are not part of the
IAddress interface, but it doesn’t matter as long as the expected fields are implemented.
## Working with Abstract Classes
In object-oriented programming an abstract class is a class that can not be instantiated directly. Rather, the abstract class is realized as a base class for a derived class. An important feature of an abstract class is that it can declare abstract methods. An abstract method is a method whose behavior is defined in the class derived from the abstract class.
Listing 4 shows an example of declaring and using an abstract class in TypeScript syntax. Notice the abstract class named
foo at the top of the listing. The class
foo defines a method
getMessage(): string as abstract. There is no behavior provided for the method. Rather the behavior for
getMessage() is provided by the class named bar on the right. As you can see
bar inherits from
foo.
**Listing 4:** Declaring and using an abstract class.
The benefit provided by abstract classes is that you can write code in the abstract class that not only uses logic defined in the abstract class, but also uses the “logic to be named later” that’s defined by its abstract methods.
Listing 5 below illustrates the concept. Listing 5 enhances the abstract class
foo shown above in Listing 4.
**Listing 5:** An abstract class that calls an abstract method at run time.
The class
foo in Listing 5 now has a method named
printMessage(); void. Notice that
printMessage() calls the abstract method
getMessage() at Line 5. However, because
getMessage() is abstract, by definition, it has no behavior. That behavior must be provided by the derived class. Yet, the abstract method can still be used within the programming logic of the abstract class.
Being able to code to “behavior to be defined later’’ broadens the power and flexibility of a developer’s programming efforts. This object-oriented approach to application design is not possible under JavaScript. Under TypeScript, it is. And, as you’ll see in the next section, using abstract classes along with the programming to the interface technique takes application design to a whole new level.
## A Hands-on Tutorial
The purpose of this section is to provide a detailed example of application design taking a “programming to the interface” approach in combination with working with an abstract class. The illustration in Figure 1 below is a diagram in
[ Unified Modeling Language](https://en.wikipedia.org/wiki/Unified_Modeling_Language) (UML) that describes an object model that supports creating and using two types of documents, a hard copy document and a web document. ![The object model for the demonstration application diagrammed in Unified Modeling Language.](https://cdn.thenewstack.io/media/2024/03/e4d0b2da-advanced-oop-ts-blue-2.png)
**Figure 1:** The object model for the demonstration application diagrammed in Unified Modeling Language.
The demonstration application that accompanies this article is the TypesScript code for the object model shown above. The following sections describe the details of the code.
We’ll start with the interfaces.
### Defining the Interfaces
The interfaces that make up the demonstration use case are as follows. First there is the
and
[IAddress](https://github.com/reselbob/AdvancedOop01_TS/blob/main/src/document/interfaces/IAddress.ts)
interfaces shown in Listing 6. These two interfaces will be used to describe the author of a document.
[IPerson](https://github.com/reselbob/AdvancedOop01_TS/blob/main/src/document/interfaces/IPerson.ts) **Listing 6:** The
IAddress and
IPerson interfaces.
The
IAddress interface is used to describe the physical address defined in
IPerson.
Next is the
interface as shown in Listing 7. This interface describes the fields and methods that make up a document. Notice that the type of the
[IDocument](https://github.com/reselbob/AdvancedOop01_TS/blob/main/src/document/interfaces/IDocument.ts)
author field is declared as the interface
IPerson. Also, notice that the
IDocument interface has only one method,
print().
**Listing 7:** The TypeScript interface that describes a document.
Finally, there is a set of interfaces that describe logging as shown in Listing 8.
describes the structure of a log entry. The other interface,
[ILogEntry](https://github.com/reselbob/AdvancedOop01_TS/blob/main/src/document/interfaces/ILogEntry.ts)
ILogger, has no fields, but defines a method named
getLogEntries().
The method
getLogEntries() returns an array of type
ILogEntry elements. The interesting thing to notice is that the
IDocument shown above in Listing 7 does not use either the
ILogEntry or the
ILogger interfaces.
**Listing 8:** The interfaces that describe logging.
Where and how the logging interfaces are used will be revealed when we create the abstract class,
AbstractDocument.
### Implementing the Interfaces in an Abstract Class
Listing 9 below shows the code for the abstract class
AbstractDocument. Notice that
AbstractDocument implements both the
IDocument and
ILogger interfaces as shown at Line 1 in the listing. This means that
AbstractDocument needs to implement all the fields and methods defined in both interfaces, which it does.
**Listing 9:** An abstract class that implements two interfaces.
However, notice that the
print() method that’s required by the
IDocument interface is implemented as an abstract method at Line 29. This means that actual printing behavior will be provided by classes that inherit from
AbstractDocument.
Also, notice at Line 6 that
AbstractDocument declares a class variable named
logEntries that’s an
Array<ILogEntry>. The variable is initialized in the class’s constructor at Line 13. Also at Line 16,
AbstractDocument provides a method
getLogEntry() that returns an
ILogEntry interface.
This method is special to
AbstractDocument.
getLogEntry() returns an instance of an
ILogEntry interface by dynamically creating a JavaScript object that conforms to the
ILogEntry specification.
The reason that
AbstractDocument needs to provide the class variable
logEntries and the method
getLogEntry() is because, although the
ILogger interface requires support for the method
getLogEntries(), it does not specify how a log entry is created and stored. This work is done by the abstract class, hence the declaration of the
logEntires class variable and the method
getLogEntry().
But, still, where does the actual logging happen? This is done in the classes that inherit from
AbstractDocument.
Listing 10 below shows the code for the concrete classes
HardCopyDocument and
WebDocument. Both of these classes inherit from
AbstractDocument. They both implement logic for the abstract method
print(), but each class has a special implementation, which is indicated by the given class’s special string outputted by
console.log().
**Listing 10:** The two classes realize the abstract class
AbstractDocument.
Also, notice that the
print() method in both classes calls the
getLogEntries() method. As you might recall, the behavior for
getLogEntries() is defined in the
AbstractDocument class. The result is that each class now has printing and logging capabilities.
The next step is to use the classes.
### Programming to the Interface
Listing 11 below shows code that uses the
HardCopyDocument and
WebDocument classes. Even though the program only has 18 lines of code, there’s a lot going on that’s worth discussing, particularly in terms of the notion of programming to the interface as we described earlier.
As you can see, the code creates an
author variable at Line 2, using the demonstration code’s custom
method to assign a value to the author variable. The return value of the method
[Randomizer.getRandomPerson()](https://github.com/reselbob/AdvancedOop01_TS/blob/5effbd298df912c39f7cb1faa3a0f7472069694e/src/randomizer/Randomizer.ts#L7)
Randomizer.getRandomPerson() is an
IPerson interface.
A variable named
document is created at Line 4 and assigned an instance of
WebDocument using the class’s constructor.
Then, something worth noticing happens.
The code “extracts” the
IDocument interface from the document object at Line 6 and calls the interface’s
print() method. (The formal term is, the document object is “cast” to an IDocument interface.)
Then, at Line 7, a variable named
logEntries of type Array<ILogEntry> is created and assigned the log entries created in the
document object. Notice that the code casts the
document to an
ILogger interface and then calls the interface’s
getLogEntries() method.
Remember, the
WebDocument supports both the
IDocument and
ILogger interface because its base class,
AbstractDocument, declares implementations for both
IDocument and
ILogger interfaces.
**Listing 11:** An example of programming to the interface.
After the document object does its work as an instance of a
WebDocument class, it is reassigned an instance of a
HardCopyDocument class using the same
author but with a different title. (See Line 10.)
Then, the same casting pattern is executed on the
document object. First, the object is cast to an
IDocument interface, calling the
print() method. Then, it’s cast to an
ILogger interface calling the
getLogEntries() method.
As you can see, the application code in Listing 11 is an example of programming to the interface. At no time are methods on a class called. Rather, all calls are made to a given interface.
The output from running the code is shown below in Listing 12.
**Listing 12:** The results of running the demonstration code.
Notice that the output shows both the result of calling
IDocument.print() and
ILogger.getLogEntries().
## Putting It All Together
The purpose of this article is to demonstrate two powerful concepts of object-oriented programming available in TypeScript. The first is the notion of programming to the interface. The second is using abstract classes to increase versatility when creating classes and to make it easier to support a prime principle of OOP: Don’t Repeat Yourself (known as DRY).
Abstract classes make it possible to include logic that’s intended to be shared among derived classes alongside logic that is “to be named later.” It’s an elegant and powerful approach to programming.
Granted, the use case described in this article is simple. However, it does provide a good way to understand how to use these concepts in your day-to-day programming efforts. Using abstract classes and programming to the interface might entail thinking differently about the way you design applications, but the result will be code that’s more versatile, less error-prone and easier to maintain.
[
YOUTUBE.COM/THENEWSTACK
Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.
](https://youtube.com/thenewstack?sub_confirmation=1)