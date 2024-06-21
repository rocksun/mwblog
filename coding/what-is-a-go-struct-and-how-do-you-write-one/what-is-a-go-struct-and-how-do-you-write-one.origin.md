# What Is a Go Struct and How Do You Write One?
![Featued image for: What Is a Go Struct and How Do You Write One?](https://cdn.thenewstack.io/media/2024/06/a7bd071c-buttons-3448899_1280-1024x682.jpg)
In the [Go programming language](https://thenewstack.io/golang-co-creator-rob-pike-what-go-got-right-and-wrong/), a struct (aka “[structure](https://go.dev/tour/moretypes/2)”) is a composite data type that makes it possible to group values of different types into a single entity. Structs are handy when you want to group data into a single unity, instead of having to declare separate values.

For example, you could create a struct that collects information on a person like first name, last name and age. You could declare them as individual items, like so:

123 |
var fname stringvar lname stringvar age int |
Now, imagine you have to declare a large number of variables. Your code could quickly become a mess and far from efficient to read/understand.
Instead, you could employ a struct to bring those related [variables](https://thenewstack.io/golang-variables-and-data-types-an-introduction/) together.

There are a few points you should understand about structs:

- Structs are defined using the type keyword.
- Fields are accessible using the dot operator followed by the field name.
- Structs are initialized by providing values for each field in the order they are defined.
- You can define methods on structs to perform operations on or provide specific behavior to the struct.
- You can compose a struct with other structs.
- You can either pass a struct to a function or assign it to a new variable, both of which create a copy of the struct. To avoid this, you can use pointers to structs.
First, let me show you how to create a struct. Our example will be named *Employee* and will contain* firstName*,* lastName*, *age* and *pay.* Remember, we start by defining the struct with the [type keyword](https://thenewstack.io/understanding-golang-type-system/), which looks like this:

1 |
type Employee struct { |
Next, we add our fields, which are* firstName (string)*, *lastName (string)*, *age (int)* and *pay (int)*. That looks like this:
12345 |
firstName stringlastName stringage intpay int } |
The struct looks like this:
123456 |
type Employee struct { firstName string lastName string age int pay int } |
Now, we’ll create a main function that will specify data for our struct using field names. This is a good way to start because there’s a parallel that’s easy to follow. Let’s define employee1 like this:
123456 |
employee1 := Employee{ firstName: "Olivia", lastName: "Nightingale", age: "31", pay: "1000",} |
We could also define the struct without using the field names. This method is faster and cleaner but for those new to Go, it’s less obvious. This method would look like so:
1 |
employee1 := Employee{"Olivia", "Nightingale", "31", "1000"} |
What’s important about the above line is the fields must be in the same order as they were declared in the struct. That is the other complication with this type of struct definition. If you were to omit a field or place fields in the wrong order, it could wreak havoc on the app or the output of the app. Because of this, it’s probably best if you stick with the field name definition.
We’ve essentially done the same thing, only one method is quicker.

Let’s roll this struct into an app that will print out the information about our employee. The app looks like this:

123456789101112131415161718192021222324 |
package mainimport ( "fmt")type Employee struct { firstName string lastName string age int pay int}func main () {employee1 := Employee { firstName:"Olivia", lastName: "Nightingale", age: 31, pay: 1000,}fmt.Println("Employee 1 details:", employee1)} |
Run the above application and the results will be:
*Employee 1 details: {Olivia Nightingale 31 1000}*
We could also define a second employee. Let’s do it without using field names. That code looks like this:

12345678910111213141516171819202122232425262728 |
package mainimport ( "fmt")type Employee struct { firstName string lastName string age int pay int}func main () {employee1 := Employee { firstName:"Olivia", lastName: "Nightingale", age: 31, pay: 1000,}employee2 := Employee {"Nathan", "Gage", 32, 900}fmt.Println("Employee 1 details:", employee1)fmt.Println("Employee 2 details:", employee2)} |
Run the above application and the results will be:
*Employee 1 details: {Olivia Nightingale 31 1000}*
*Employee 2 details: {Nathan Gage 32 900}*
## Anonymous structs
You can also declare structs without first creating a new data type. Remember how, in the above struct, we first created the struct with type *Employee* struct and then defined the struct with *employee1 := Employee?* With anonymous structs, we can combine those into a single function. Let’s define a third employee in this manner. First, we define* employee3* with:

1 |
employee3 := struct { |
You should see where this is going. In the next lines, add the fields like so:
12345 |
firstName string lastName string age int pay int} |
So far, this looks like so:
123456 |
employee3 := struct { firstName string lastName string age int pay int} |
We then jump right into defining the fields like this:
123456 |
} firstName: "Aaron", lastName: "Kennedy", age: 40, pay: 1100,} |
The entire anonymous struct looks like this:
1234567891011 |
employee3 := struct { firstName string lastName string age int pay int}{ firstName: "Aaron", lastName: "Kennedy", age: 40, pay: 1100,} |
The entire application looks like this:
12345678910111213141516171819202122232425262728293031323334353637383940 |
package mainimport ( "fmt")type Employee struct { firstName string lastName string age int pay int}func main () {employee1 := Employee { firstName:"Olivia", lastName: "Nightingale", age: 31, pay: 1000,}employee2 := Employee {"Nathan", "Gage", 32, 900}employee3 := struct { firstName string lastName string age int pay int}{ firstName:"Aaron", lastName: "Kennedy", age: 40, pay: 1100,}fmt.Println("Employee 1 details:", employee1)fmt.Println("Employee 2 details:", employee2)fmt.Println("Employee 3 details:", employee3)} |
As you probably expect, the output of the app looks like this:
*Employee 1 details: {Olivia Nightingale 31 1000}*
*Employee 2 details: {Nathan Gage 32 900}*
*Employee 3 details: {Aaron Kennedy 40 1100}*
## Accessing Individual Fields
One final point about structs is that it’s possible to access only a single field. Remember how our output was kind of nondescript? What if we wanted to make it a bit more detailed? We can do that from within the *fmt.Println* section by accessing individual fields for each printed line. This can be done like so:

1234 |
fmt.Println("First Name: ", employee1.firstName)fmt.Println("Last Name: ", employee1.lastName)fmt.Println("Age: ", employee1.age)fmt.Println("Pay: ", employee1.pay) |
Now, our output is more structured and looks like this:
*First Name: Olivia*
*Last Name: Nightingale*
*Age: 31*
*Pay: 1000*
And that, my friends, is how you create a struct in Go. This handy feature can help not only keep your code cleaner and more flexible but also easier to write.

[
YOUTUBE.COM/THENEWSTACK
Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.
](https://youtube.com/thenewstack?sub_confirmation=1)