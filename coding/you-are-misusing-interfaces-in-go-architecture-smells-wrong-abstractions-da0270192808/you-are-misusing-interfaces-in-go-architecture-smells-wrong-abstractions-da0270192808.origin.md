# You Are Misusing Interfaces in Go - Architecture Smells: Wrong Abstractions
Interfaces are playing crucial role in software architectures. What makes them very strong tenet of the architecture is lies its abstraction capabilities.

One of the customary concept that software engineers faced in interviews is SOLID principles. Interfaces are cover most of the implementation parts of the SOLID. When you try to follow open-closed principle or try to inverse your dependencies, **you need an** **interface**.

As a rule remember that, when you want to abstract some implementation details from the caller/client side, you probably use interface.

As a necessary inference of this logical reasoning, we can conclude that if we want to abstract some package from another package, we need to use interface.

So let’s dive into the issues of interface usage in Go applications.

While reviewing Go codes I usually facing with a coding convention of using interfaces as shown in the following example. An interface that defines methods and a single concrete private struct that implements the interface just below of it.

As you know, we emphasized the importance and the role of interfaces which is: abstraction. Now, look that code again and ask yourself the following question: “What it the abstraction here?”. Is that prevent exposing the functionality of the struct? No. Contraversly, thats the hole point.

There might be an argument like “hiding the structs itself from the outside of the package”. But, what is the point? Why do we want to hide a struct if we expose the struct’s functionality anyway?

Usually we do not want to hide the struct, we want “encapsulation” which is hiding the internal state of the struct (the struct variables). We probably do not want anyone to make uncontrolled changes on the struct’s state. But in this case, we just need to make the struct variables private and access them via struct methods.

Another argument might be about unit testing. The interface provides testing the struct functionality. But this brings another question, who we need to test? We probably want to test the caller/client of this struct. Because we can test that struct every functionality in the same package independent of defining an interface. So we want to test the caller side, we need an interface to mock external dependencies of caller. Here, we find the requirement: Testing the caller side independent of external dependencies.

After this clarification we are left with the same question: “What is the point of this interface/abstraction here?”.

The answer is obvious: It is mostly pointless‼️

This is kind of a premature optimization which is a bad practice. We do not have and (mostly) will not have concrete type implementation of the same interface (even if we have, this does not mean that we need to define an interface).

Okay we see the problem, putting interface in front of every struct definition is wrong, but what do we need to do? What is the best practice to use interfaces? What is the right way to do abstractions?

You need to ask yourself:

📌 Can I live without an interface?
📌 Which part do I need to abstract?
📌 In which direction should my dependencies go?
📌 What do I want to test?

Usually, unit testing itself is not enough to be a strong reason for creating an interface (unless we have external dependencies).

But, most of the time, to avoid deep and hard mocking processes, we can create an interface to easily mock a type.

Apart from unit testing, answers of the previous questions give us a huge insight about abstraction requirements, hence we can easily decide where to put our interface.

Now take the first code example and decide where to put our interface/abstraction.

Let’s say we have following Consumer code and it’s caller. Suppose that the Consumer exist in the “**infrastructure**” package:

And Caller exists in the “**application**” layer:

There is a strong coupling between Caller and Consumer because Caller directly depends on Consumer concrete type. Also, this brings coupling between layers too. If we want to get rid away the Consumer details **we need an abstraction: interface**.

Currently, we could not easily unit test Caller because the consumer.Consume() method will be called and we can not prevent it to happen. So we need to **create an abstraction using an interface**.

Now let’s create that abstraction to overcome those issues. To achieve this, in Go, we just need to write an appropriate interface that contains contract, methods that we use.

We will modify the Caller code by defining a Consumer interface:

By creating an interface on the Caller side, we will simply create an abstraction for it’s dependency. Also, we cut the direct coupling between layers/packages too (thanks to Go’s duck typing interface implementations). Now we can easily write unit tests for our Caller by creating a mock struct for the Consumer interface in the same package with the Caller.

We do not need to change any other parts of the application, the composition root (usually main) will remain same, it still creates concrete types and passes them as parameters to constructors/functions in same way.

By following this simple approach, we are able to create loose coupled, testable, well behaved packages without unnecessary abstractions and interface definitions.

This technique is used mostly while implementing Ports&Adapters architecture. Ports are defined by the layer that is used by. Remember, primary (driver) adapters uses/wraps ports and secondary (driven) adapters implements ports.

We are shown when and how interfaces should be used for abstraction. Thanks for reading so far, see you on the next time 🚀