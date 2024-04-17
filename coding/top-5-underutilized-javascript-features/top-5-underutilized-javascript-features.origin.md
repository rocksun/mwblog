# Top 5 Underutilized JavaScript Features
![Featued image for: Top 5 Underutilized JavaScript Features](https://cdn.thenewstack.io/media/2024/04/54cf79eb-getty-images-sdayknbkxeg-unsplash-1024x683.jpg)
[JavaScript](https://thenewstack.io/javascript/) is an essential programming language, but often its capabilities are left under-explored. [JS possesses a range of features](https://thenewstack.io/top-5-javascript-tools-for-ai-engineering/) that can be applied to a countless number of use cases, helping developers create efficient, reusable, and adaptable code.
In this article, we will explore the top five under-utilized JavaScript features and their use cases. We will also provide code examples to show how JS can be used for nearly everything, from solving date management issues to chaining functions, and even detecting malicious websites.
## 1. JavaScript Hooking to Detect Malicious Websites
One nifty JS feature is the use of hooks as an effective method of
[telling if a website is fake or not](https://www.identityguard.com/news/how-to-tell-if-a-website-is-fake), all without any particular OpSec or cybersecurity knowledge in general.
Hooks are JS functions that allow a developer to “hook into” state and lifecycle features from the highly popular UI development library, React. This means
[developers can use React](https://thenewstack.io/the-pros-and-cons-of-using-react-today/) without having to write individual classes.
In the following example, we will focus on web pages that are built using static and dynamic components. Static components are always declared as part of the HTML source code and rendered by the browser or its installed plugins. Meanwhile, dynamic components include scripts like JS which modify HTML documents by adding, changing, or removing certain elements, as well as
[utilizing XMLHttpRequest and similar objects](https://developer.mozilla.org/en-US/docs/Web/API/XMLHttpRequest) for server interaction.
### How It Works
An exploit kit (
[a toolkit used by cybercriminals](https://learn.microsoft.com/en-us/microsoft-365/security/defender-endpoint/malware/exploits-malware?view=o365-worldwide)) and malicious websites or web applications typically rely on obfuscation to bypass signature-based protection methods. JS can be used to deobfuscate websites, modifying the code and its elements so it can be read and processed by the browser.
Exploit kits often contain very large chunks of code to hide the exploit and confuse web browsers. Once decoded by JS, new page elements are added — such as new DIV elements, new JS elements, and new Java applet elements that load the exploit.
This means JS hooks can be applied to script functions during the deobfuscation process, issuing alerts if anything unusual is detected, such as the addition of potentially malicious Java applet elements.
To do this, we must first focus on hooking the primary methods of adding elements:
[appendChild](https://developer.mozilla.org/en-US/docs/Web/API/Node/appendChild), [replaceChild](https://developer.mozilla.org/en-US/docs/Web/API/Node/replaceChild), and [document.write](https://developer.mozilla.org/en-US/docs/Web/API/Document/write). The fourth method is slightly more challenging; so instead, the focus should be to hook specific functions such as [document.getElementById()](https://developer.mozilla.org/en-US/docs/Web/API/Document/getElementById), or [document.createElement()](https://developer.mozilla.org/en-US/docs/Web/API/Document/createElement). Objects can then be added to the MutationObserver object, or we can use Mutation Events and monitor for any changes.
Below is an example of a function that registers hooks:
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
|
function jsh_hook_function(object, property, pre_h_func, post_h_func) {
const original = object[property];
object[property] = function(...args) {
if (pre_h_func) {
pre_h_func.apply(this, args);
}
const result = original.apply(this, args);
if (post_h_func) {
post_h_func.apply(this, [args, result]);
}
return result;
};
}
## 2. Generate Reports in Node.js
Reporting and documentation are key elements of a robust cybersecurity strategy, but it can be a tedious and time-consuming process — especially when it comes to more sensitive information, such as pentesting reports, vulnerability assessments and anything else security-related. Jsreport is a specialized reporting platform that has been developed in the open source JavaScript runtime environment, Node.js. The platform has a range of use cases, including HTML to PDF conversion.
Using just the Chrome browser, you simply need to
[install the jsreport npm package](https://jsreport.net/learn/npm) and call a single function. As well as HTML, the platform can convert all kinds of mediums, making it possible to [generate DOCX files as PDFs with JS alone](https://apryse.com/blog/javascript/generate-docx-and-save-as-pdf-in-javascript) or even entire spreadsheets, formulas included. This means data can be kept on a single platform and converted into reports without third-party tools — ideal for cybersecurity documentation and exporting [pentesting reports](https://www.getastra.com/blog/security-audit/penetration-testing-report/) so that testing, analysis, and data storage are all centralized.
Jsreport is not Google Chrome specific and is compatible with a range of services and technologies to print output. This includes
[Apache FOP](https://xmlgraphics.apache.org/fop/) to render XML files.
### How It Works
Install jsreport npm and call one function:
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
|
const http = require('http');
const jsreport = require('jsreport');
http.createServer(async (req, res) => {
try {
const result = await jsreport.render({
template: {
content: '<h1>Hello world</h1>',
engine: 'handlebars',
recipe: 'chrome-pdf'
}
});
res.setHeader('Content-Type', 'application/pdf');
result.stream.pipe(res);
} catch (e) {
res.writeHead(500, { 'Content-Type': 'text/plain' });
res.end(`Error generating PDF: ${e.message}`);
}
}).listen(1337, '127.0.0.1');
## 3. Control Execution Flow with Generators
Generators are a type of function that can be paused and resumed, helping developers maintain more control over the flow of execution. Generators can be used for backtracking algorithms, infinite sequences, and
[asynchronous operations](https://www.freecodecamp.org/news/async-generators-as-an-alternative-to-state-management/); plus they also allow customer iteration patterns to be created.
It’s a powerful and versatile JavaScript feature that is often under-utilized, with many
[software developers](https://thenewstack.io/software-development/) missing out on the ability to have maximum control over code execution.
### How It Works
Here is a simple code example:
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
function* generatorFunction() {
yield 'Hello';
yield 'World';
}
const generator = generatorFunction();
console.log(generator.next().value); // Output: Hello
console.log(generator.next().value); // Output: World
To specify a generator function, first the generatorFunction should be defined using the function* syntax, Then the yield keyword is used to pause the execution of the function and to return a value. Next, the generator object is created by calling the
[generatorFunction](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/GeneratorFunction), followed by calling the next method on the generator to resume the execution. The value property of the returned object also contains the yielded value.
## 4. Improved Date Management with Temporal
Over the years, many developers have
[complained about poor date management features](https://www.freecodecamp.org/news/how-to-format-a-date-with-javascript-date-formatting-in-js/) in JavaScript. Fortunately, Temporal has provided a native solution, [offering a standard global object to replace the date object](https://docs.temporal.io/temporal) to solve a range of issues. For example, one perplexing problem was poor indexing with months starting at zero, while days started at 1.
Supporting multiple time zones and non-Gregorian calendars, Temporal is an out-of-the-box solution that has an easy-to-use API that simplifies parsing dates from strings. The immutable nature (i.e. cannot be changed) of Temporal objects also means that dates will be immune from bugs that cause unexpected modifications.
### How It Works
Here are several Temporal methods that devs can utilize:
a) PlainDate() – Create a date with no time.
|
1
2
3
|
new Temporal.PlainDate(2024, 7, 26);
Temporal.PlainDate.from('2024-07-26');
// both return a PlainDate object that represents 26th July 2024
b) PlainTime () – Create a time with no date.
|
1
2
3
|
new Temporal.PlainTime(20, 24, 0);
Temporal.PlainTime.from('20:24:00');
// both return a PlainTime object of 20:24
c) PlainMonthDay () – Creates a month and day but does not assign a year. A useful function for days that recur on the same date every year, such as Valentine’s Day.
|
1
|
const valentinesDay = Temporal.PlainMonthDay.from({ month: 2, day: 14 });
## 5. Create Reusable Code with High-Order Functions
In JavaScript, functions are the priority, which allows high-order functions to be created to establish a code hierarchy. High-order functions turn one or multiple functions into arguments or they can be used to return another function. This provides a range of capabilities such as composition,
[currying](https://frontend.turing.edu/lessons/module-3/hof-and-currying.html), and function chainings — ultimately helping developers create streamlined, modular code that can be easily reused on other projects.
### How It Works
Let’s consider function chaining as an example. In this instance, the object is a calculator, and using function chaining there are many ways to alter its internal state and return each modified state seamlessly.
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
|
const calculator = {
value: 0,
add(num) {
this.value += num;
return this;
},
subtract(num) {
this.value -= num;
return this;
},
multiply(num) {
this.value *= num;
return this;
},
getValue() {
return this.value;
},
};
const result = calculator.add(5).subtract(2).multiply(3).getValue();
console.log(result); // Output: 9
[
YOUTUBE.COM/THENEWSTACK
Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.
](https://youtube.com/thenewstack?sub_confirmation=1)