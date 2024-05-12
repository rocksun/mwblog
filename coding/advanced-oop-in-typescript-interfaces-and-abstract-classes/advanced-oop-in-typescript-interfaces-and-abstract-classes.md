
<!--
title: TypeScript 中的高级 OOP：接口和抽象类
cover: https://cdn.thenewstack.io/media/2024/03/15db2836-abstract-classes.jpg
-->

使用抽象类和面向接口编程可以帮助您设计应用程序，这些应用程序将更加通用、更不容易出错且更容易维护。

> 译自 [Advanced OOP in TypeScript: Interfaces and Abstract Classes](https://thenewstack.io/advanced-oop-in-typescript-interfaces-and-abstract-classes/)，作者 Bob Reselman。

许多开发人员在用 [JavaScript](https://thenewstack.io/javascript/) 编程多年后，才接触到 [TypeScript](https://thenewstack.io/typescript/)。因此，为了急于完成任务，其中一些开发人员没有充分利用 TypeScript 的更高级面向对象特性。

这是可以理解的。将代码投入生产的压力可能是严酷且无情的。花时间充分学习 TypeScript 中的 [面向对象编程 (OOP)](https://thenewstack.io/why-are-so-many-developers-hating-on-object-oriented-programming/) 原理将成为一种奢侈。有很多东西需要了解。

但是，有一些面向对象编程的基本原理不仅可以快速学习，而且在创建和维护应用程序时都可以节省时间。其中一组原则是使用接口和抽象类来促进代码重用、安全性和多功能性。

在这里，我将介绍如何以将接口和抽象类置于设计过程最前沿的方式创建面向对象应用程序。此外，我将演示 TypeScript 中一种以该语言特有的方式使用接口的技术。可以在此 [GitHub 存储库](https://github.com/reselbob/AdvancedOop01_TS/) 中找到所提供的所有代码。

为了充分利用本教程，你应该有 JavaScript 编程经验，了解面向对象编程中类和继承的工作原理，以及使用 [TypeScript 和 Node.js](http://node.js) 的一些经验。

## 编程到接口

TypeScript 提供的重要面向对象特性之一是对接口的支持。接口是面向对象编程的基本组成部分，在 [Java](https://thenewstack.io/we-can-have-nice-things-upgrading-to-java-21-is-worth-it/)、C# 和 C++ 等语言中也有。JavaScript 中没有明确提供接口。

你可以将接口视为一个模板，它定义类的字段和方法签名。接口描述类的结构，但不描述其工作方式。“工作方式”部分由实现接口的类提供。根据编程语言和用例，一些接口只定义字段，一些接口只定义方法签名，一些接口既描述字段又描述方法签名。

下面的清单 1 显示了使用 TypeScript 语法的两个接口 [IAddress](https://github.com/reselbob/AdvancedOop01_TS/blob/main/src/document/interfaces/IAddress.ts) 和 [IPerson](https://github.com/reselbob/AdvancedOop01_TS/blob/main/src/document/interfaces/IPerson.ts) 的代码。

**清单 1**：描述地址和人员的接口。

```typescript
// gistfile1.txt
export interface IAddress {
  address1: string;
  address2: string;
  city: string;
  stateProvince: string;
  postalCode: string;
  country: string;
}

// gistfile1.txt
export interface IPerson {
  firstName: string;
  lastName: string;
  email: string;
  phoneNumber: string;
  address: IAddress;
}

```

为清单顶部的 `IAddress` 定义的所有字段都必须返回一个字符串值。但是，请注意，底部的 `IPerson` 接口在第 7 行定义了一个名为 `address` 的字段。`address` 字段必须返回一个实现 `IAddress` 接口的对象。该对象可能具有 `IAddress` 接口定义的字段和方法之外的其他字段和方法。

但是，当开发人员编写调用 `address` 字段的代码时，他们只会得到 `IAddress` 定义的方法和字段的实现。采用这种以接口为中心的方法称为编程到接口。这种方法在使用 TypeScript 编程时尤其强大。

请看下面的清单 2。它是 [演示 TypeScript](https://github.com/reselbob/AdvancedOop01_TS/blob/5effbd298df912c39f7cb1faa3a0f7472069694e/src/randomizer/Randomizer.ts#L25) 代码的摘录，该代码随本文一起提供。该代码使用 [Faker NPM 库](https://www.npmjs.com/package/@faker-js/faker) 生成随机数据。请注意，方法 [getRandomAddress()](https://github.com/reselbob/AdvancedOop01_TS/blob/5effbd298df912c39f7cb1faa3a0f7472069694e/src/randomizer/Randomizer.ts#L25) 的返回类型是 `IAddress` 接口。但是，请注意，方法的实际返回类型是一个动态创建的 JavaScript 对象，它具有 `IAddress` 定义的 `address1`、`address2`、`city`、`stateProvince`、`postalCode` 和 `country` 字段。


```typescript
// gistfile1.txt 
public static getRandomAddress(): IAddress {
    return {
      address1: faker.location.streetAddress(),
      address2: faker.location.secondaryAddress(),
      city: faker.location.city(),
      stateProvince: faker.location.state(),
      postalCode: faker.location.zipCode(),
      country: 'USA',
   };
}
```


**清单 2**： `getRandomAddress()` 方法使用演示应用程序的自定义随机生成器来返回一个实现 `IAddress` 接口的 JavaScript 对象。

在 TypeScript 中，创建动态支持预定义接口中定义的字段的 JavaScript 对象是实现接口的一种完全可接受的方式。事实上，使用 JavaScript 对象动态实现接口是 TypeScript 的一个有吸引力的特性。

在下面第 3 则代码清单中所示的演示应用程序中的 [getRandomPerson()](https://github.com/reselbob/AdvancedOop01_TS/blob/5effbd298df912c39f7cb1faa3a0f7472069694e/src/randomizer/Randomizer.ts#L7) 方法是动态创建 JavaScript 对象的另一个示例，以实现一个接口，在这种情况下，代码实现 IPerson 接口。

```
// gistfile1.txt
public static getRandomPerson(): IPerson {
  const firstName = faker.person.firstName();
  const lastName = faker.person.lastName();

  return {
    firstName,
    lastName,
    email: `${firstName}.${lastName}@${faker.internet.domainName()}`,
    phoneNumber: faker.phone.number(),
    address: this.getRandomAddress(),
  };
}
```

**清单 3**：动态创建 JSON 对象以实现 IPerson 接口。

请注意，在上面的清单 3 中，分配给 address 字段的值是 IAddress 接口，该接口由方法 getRandomAddress() 返回。这是面向接口编程的一个示例。

方法 getRandomAddress() 预计会返回一个支持 IAddress 接口的对象。该对象可能具有许多不属于 IAddress 接口的方法和字段，但只要实现了预期字段，这并不重要。

## 使用抽象类

在面向对象编程中，抽象类是一个不能直接实例化的类。相反，抽象类被实现为派生类的基类。抽象类的重要特征是它可以声明抽象方法。抽象方法是一个在从抽象类派生的类中定义其行为的方法。

清单 4 展示了在 TypeScript 语法中声明和使用抽象类的示例。请注意清单顶部的名为 foo 的抽象类。类 foo 定义了一个方法 getMessage(): string 为抽象。没有为该方法提供行为。相反，getMessage() 的行为由右侧名为 bar 的类提供。正如您所看到的 bar 继承自 foo。

```ts
// gistfile1.txt
export abstract class foo {
  protected abstract getMessage(): string;
}

```

```ts
// gistfile1.txt
export class bar extends foo {
  protected getMessage(): string {
    return 'Hi there';
  }
}

```

*清单 4：声明和使用抽象类。*


抽象类提供的好处是，您可以在抽象类中编写代码，这些代码不仅使用在抽象类中定义的逻辑，还使用由其抽象方法定义的“稍后命名的逻辑”。

下面的清单 5 说明了这个概念。清单 5 增强了清单 4 中上面显示的抽象类 foo。

```ts
// gistfile1.txt
export abstract class foo {
  protected abstract getMessage(): string;

  public printMessage():void {
    const message = this.getMessage();
    console.log(`Secret message: ${message}
  }
}
```

*清单 5：在运行时调用抽象方法的抽象类。*

清单 5 中的类
foo 现在有一个名为
printMessage(); void 的方法。请注意
printMessage() 在第 5 行调用抽象方法
getMessage()。然而，由于
getMessage() 是抽象的，因此根据定义，它没有行为。该行为必须由派生类提供。然而，抽象方法仍然可以在抽象类的编程逻辑中使用。

能够对“稍后定义的行为”进行编码，扩大了开发人员编程工作的强大功能和灵活性。这种面向对象的应用程序设计方法在 JavaScript 中是不可能的。在 TypeScript 中，这是可能的。而且，正如您将在下一部分中看到的，将抽象类与面向接口的编程技术结合使用，将应用程序设计提升到了一个全新的水平。

## 实践教程
本节的目的是提供一个应用程序设计的详细示例，采用“面向接口的编程”方法，并结合使用抽象类。下图 1 是
[统一建模语言](https://en.wikipedia.org/wiki/Unified_Modeling_Language) (UML) 中的一个图表，描述了一个对象模型，该模型支持创建和使用两种类型的文档，即硬拷贝文档和网络文档。![统一建模语言中绘制的演示应用程序的对象模型。](https://cdn.thenewstack.io/media/2024/03/e4d0b2da-advanced-oop-ts-blue-2.png)

**图 1：**统一建模语言中绘制的演示应用程序的对象模型。

本文附带的演示应用程序是上面显示的对象模型的 TypeScript 代码。以下部分描述了代码的详细信息。

我们将从接口开始。

### 定义接口
构成演示用例的接口如下。首先是
和
[IAddress](https://github.com/reselbob/AdvancedOop01_TS/blob/main/src/document/interfaces/IAddress.ts)
清单 6 中显示的接口。这两个接口将用于描述文档的作者。
[IPerson](https://github.com/reselbob/AdvancedOop01_TS/blob/main/src/document/interfaces/IPerson.ts) **清单 6：**
IAddress 和
IPerson 接口。

IAddress 接口用于描述
IPerson 中定义的物理地址。

接下来是
接口，如清单 7 所示。此接口描述了构成文档的字段和方法。请注意，
[IDocument](https://github.com/reselbob/AdvancedOop01_TS/blob/main/src/document/interfaces/IDocument.ts)
author 字段的类型被声明为接口
IPerson。此外，请注意
IDocument 接口只有一个方法，
print()。

**清单 7：**描述文档的 TypeScript 接口。
### Corrected Markdown Format

**Interfaces for Logging**

Finally, there is a set of interfaces that describe logging, as shown in Listing 8.
The structure of a log entry is described by the
[ILogEntry](https://github.com/reselbob/AdvancedOop01_TS/blob/main/src/document/interfaces/ILogEntry.ts)
interface. Another interface,
ILogger, has no fields but defines a method named
getLogEntries(). The
getLogEntries() method returns an array of elements of type
ILogEntry. An interesting point to note is that the
IDocument shown earlier in Listing 7 uses neither the
ILogEntry nor the
ILogger interfaces.

**Listing 8:** Interfaces describing logging.

Where and how the logging interfaces will be used will become clear when we create the abstract class
AbstractDocument.

### Implementing Interfaces in an Abstract Class

Listing 9 below shows the code for the abstract class
AbstractDocument. Notice that
AbstractDocument implements both the
IDocument and
ILogger interfaces, as indicated on line 1 of the listing. This means that
AbstractDocument must implement all the fields and methods defined in both of these interfaces, which it does.

**Listing 9:** An abstract class implementing two interfaces.

However, notice that the
print() method required by the
IDocument interface is implemented as an abstract method on line 29. This means that the actual printing behavior will be provided by classes that inherit from
AbstractDocument.

Also, notice on line 6 that
AbstractDocument declares a class variable named
logEntries, which is an
Array<ILogEntry>. This variable is initialized in the class constructor on line 13. Also on line 16,
AbstractDocument provides a method
getLogEntry(), which returns an
ILogEntry interface.

This method is special to
AbstractDocument.
getLogEntry() returns an instance of the
ILogEntry interface by dynamically creating a JavaScript object that conforms to the
ILogEntry specification.

The reason that
AbstractDocument needs to provide the class variable
logEntries and the method
getLogEntry() is that, although the
ILogger interface requires support for the
getLogEntries() method, it does not specify how log entries are to be created and stored. This job is left to the abstract class, hence the declaration of the
logEntires class variable and the
getLogEntry() method.

But where does the actual logging occur? This is done in classes that inherit from
AbstractDocument.

Listing 10 below shows the code for the concrete classes
HardCopyDocument and
WebDocument. Both of these classes inherit from
AbstractDocument. They both implement the logic for the abstract method
print(), but each class has a specialized implementation, as indicated by the specialized string for the given class that is output by
console.log().

**Listing 10:** These two classes implement the abstract class
AbstractDocument.

Also, notice that the
print() methods in both of these classes call the
getLogEntries() method. As you may recall, the behavior of
getLogEntries() is defined in the
AbstractDocument class. The result is that each class now has both printing and logging capabilities.

The next step is to use these classes.

### Programming to Interfaces

Listing 11 below shows code that uses the
HardCopyDocument and
WebDocument classes. Although the program is only 18 lines of code, there is a lot to discuss, especially in terms of the concept of programming to interfaces that we described earlier.

As you can see, the code creates an
author variable on line 2, using a custom method from the demo code to assign a value to the author variable. The method
[Randomizer.getRandomPerson()](https://github.com/reselbob/AdvancedOop01_TS/blob/5effbd298df912c39f7cb1faa3a0f7472069694e/src/randomizer/Randomizer.ts#L7)
Randomizer.getRandomPerson() returns an
IPerson interface.

A variable named
document is created on line 4 and assigned an instance of
WebDocument using the class constructor.

Then, something noteworthy happens.

The code “extracts” the
IDocument interface from the document object on line 6 and calls the interface’s
print() method. (The formal term is that the document object is “cast to” the IDocument interface.)

Then, on line 7, a variable named
logEntries of type Array<ILogEntry> is created and assigned the log entries created in the
document object. Notice that the code casts document to the
ILogger interface and then calls the interface’s
getLogEntries() method.

Remember that
WebDocument supports both the
IDocument and
ILogger interfaces because its base class
AbstractDocument declares implementations for both the
IDocument and
ILogger interfaces.

**Listing 11:** An example of programming to interfaces.

After the document object has done its work as an instance of the
WebDocument class, it is reassigned to be an instance of the
HardCopyDocument class, using the same
author but a different title. (See line 10.)

The same casting pattern is then performed on the
document object. First, the object is cast to the
IDocument interface, and the
print() method is called. Then, it is cast to the
## ILogger 接口调用
`getLogEntries()` 方法。

如您所见，清单 11 中的应用程序代码是面向接口编程的一个示例。在任何时候都不会调用类上的方法。相反，所有调用都针对给定的接口进行。

运行代码的输出如下所示，见清单 12。

**清单 12：**运行演示代码的结果。

请注意，输出显示了调用
`IDocument.print()` 和
`ILogger.getLogEntries()` 的结果。

## 将所有内容放在一起

本文的目的是演示 TypeScript 中面向对象编程的两个强大概念。第一个概念是面向接口编程。第二个概念是使用抽象类来提高创建类时的多功能性，并使其更容易支持面向对象编程的一个基本原则：不要重复自己（称为 DRY）。

抽象类可以将打算在派生类之间共享的逻辑与“稍后命名”的逻辑一起包含在内。这是一种优雅而强大的编程方法。

当然，本文中描述的用例很简单。但是，它确实提供了一种很好的方法来理解如何在日常编程工作中使用这些概念。使用抽象类和面向接口编程可能需要您对设计应用程序的方式进行不同的思考，但结果将是多功能性更强、更不容易出错且更容易维护的代码。

[YOUTUBE.COM/THENEWSTACK](https://youtube.com/thenewstack?sub_confirmation=1)

技术发展迅速，不要错过任何一集。订阅我们的 YouTube 频道以流式传输我们所有的播客、访谈、演示等。