<!--
# Web 开发者软件注册介绍
https://cdn.thenewstack.io/media/2023/09/a6db2386-belinda-fewings-tfnqbkedrqi-unsplash-1024x768.jpg
Image via Unsplash.
-->


注册是一种设计模式，允许开发者在运行时将组件添加到正式列表中。本文展示了这种模式的用处。

译自 [An Introduction to Software Registration for Web Developers](https://thenewstack.io/an-introduction-to-software-registration-for-web-developers/) 。

开发就像代码和数据之间的舞蹈，我们想要数据描述的灵活性，但又想要编码方案的确定性。对象之间的关系很丰富，但依赖会引起问题。

**注册(Registration)** 是一种常见的模式，它允许开发者在运行时将组件添加到正式列表中，从而允许动态数据参与代码。

所以 **注册表(register)** 就是一个应用程序将之视为规范的对象列表，但有一些注意事项。我们几乎肯定不想要重复，这意味着我们需要某种主键。这也意味着存在某种原始的数据列表来提供这个注册表。和许多模式一样，使用注册的优势在于它是分离关注点的好方法。本文展示了这个模式虽简单但相对有用。你可以跟随 C# 代码，或从 [GitHub](https://github.com/eastmad/TheNewStack3) 克隆它。

![](https://cdn.thenewstack.io/media/2023/09/b7787d8c-paul-downey-illustration-of-registers.png)
*来自 Paul Downey，英国[政府数字服务](https://gds.blog.gov.uk/2015/09/01/registers-authoritative-lists-you-can-trust/)*

硬件寄存器(register)的概念有点掩盖了软件注册表的更简单概念。但当使用 API 时，我们确实常见注册，例如，在编程 UI 按钮时，你通常必须注册事件侦听器。

本文不需要对注册表做更正式的描述，但为完整起见，看看 [Paul Downey 这里写的](https://gds.blog.gov.uk/2015/09/01/registers-authoritative-lists-you-can-trust/)，还有 [Ade Adewummi](https://gds.blog.gov.uk/2016/03/11/getting-from-data-to-registers/) 为著名的英国[政府数字服务](https://www.gov.uk/government/organisations/government-digital-service)写的。重复一些有用的原则：每个注册对象都有一个唯一标识符；应避免数据复制；允许注册表与其他注册表对话；将注册表视为可信数据。

我希望许多读者有机会这个夏天去度假，我给出的注册的简单示例只是关于配对假期参与者(party)与合适大小的小屋(cabin)。所以我们有两个注册表：小屋和假期参与者。

让我们看看详细信息：

- 一个“小屋”有一个门牌号(主键)和一个代表睡眠空间的容量。它还有可用的日期范围。
- 一个“参与者”代表一个领队旅客名称下的一些假期参与者。
- 一个参与者只能在小屋空置且可用时预订(即注册)小屋。
- 由于一个参与者只能注册空置小屋，这个模型中有一个自然**依赖**。
- 如果你取消注册一个参与者，他们的小屋变为空置。因此，如果有参与者还在屋里，你不能取消注册小屋。

要表示所有小屋，我们使用一个叫做 “allcabins.json” 的 JSON 列表。我们遍历这个列表，只注册在我们感兴趣的日期可用的小屋。

类似地，我们有一个可能的参与者列表；我们遍历这些度假者，只在我们能给他们分配小屋时注册参与者。我们应该在他们到达之前做这个，以避免失望。

另一个有意思的事是，注册对象与其他注册对象交互，当参与者检查可用的注册小屋时。我们通常更喜欢**取消注册**一个对象，而不是对一个注册对象做更改。

## 小屋

位于我们野外度假村的小屋在一个 JSON 文件 allcabins.json 中表示：

```json
[
  {
    "Number": 6,
    "Name": "Hill View",
    "Capacity": 5,
    "From": "2023/01/01",
    "To": "2023/12/21"
  },
  {
    "Number": 3,
    "Name": "Summerholme",
    "Capacity": 2,
    "From": "2023/06/01",
    "To": "2023/08/31"
  },
  {
    "Number": 4,
    "Name": "Dunroamin",
    "Capacity": 4,
    "From": "2023/03/01",
    "To": "2023/10/31"
  },
  ...
]
```

注意我们将使用小屋号码作为主键。可用日期格式作为字符串表示，因为 JSON 必须如此。

在将 JSON 数据吸入自己的 CabinData 结构后，我们从它创建 Cabin 对象，在将字符串日期转换为 C# 日期并添加 **guestParty** 变量记录住客(如果有)后：

```cs
//Cabin.cs
 
namespace HolidayCabins
{
  public struct CabinData
  {
    public short Number { get; set; }
    public string? Name { get; set; }
    public short Capacity { get; set; }
    public string? From { get; set; }
    public string? To { get; set; }
  }
 
  public class Cabin
  {
     private static List<Cabin> registeredCabins = new List<Cabin>();
 
     private Party? guestParty;
     private CabinData data;
     private DateOnly from;
     private DateOnly to;
 
     public Cabin(CabinData record)
     {
        data = record;
        if (DateOnly.TryParse(data.From, out DateOnly result))
        {
          from = result;
        }
        else Console.WriteLine($"Not a valid date {data.From}");
 
        if (DateOnly.TryParse(data.To, out result))
        {
           to = result;
        }
        else Console.WriteLine($"Not a valid date {data.To}");
     }
     ...
  }
}
```

JSON 文件在其他地方处理。但结果是我们可以从原始数据制作小屋。

那么我们在哪里注册它们？

```cs
//Cabin.cs
 
public static void RegisterCabin(Cabin cabin, DateOnly date)
{
  if (registeredCabins.Exists(cb => cabin.data.Number == cb.data.Number))
  {
    Console.WriteLine($"{cabin.data.Name} is already registered");
    return;
  }
 
 
  if (cabin.from <= date && date <= cabin.to)
  {
    registeredCabins.Add(cabin);
    Console.WriteLine($"Cabin \"{cabin.data.Name}\" registered");
   }
   else Console.WriteLine($"(Cabin \"{cabin.data.Name}\" not available at the moment)");
}
 
public static void UnregisterCabin(Cabin cabin)
{
  if (cabin.guestParty != null)
    throw new Exception($"Cannot unregister \"{cabin.data.Name}\" as it is not vacant");
 
  registeredCabins.Remove(cabin);
 
  Console.WriteLine($"Cabin \"{cabin.data.Name}\" unregistered.");
}
```

这主要只是 **registeredCabins** 列表的门卫。我们满足两个要求：我们不允许具有相同编号的小屋出现两次，并检查小屋在给定日期是否可用。取消注册小屋时，我们检查是否已经有客人入住。

## 假期参与者

现在来看另一个注册表：客人假期参与者。JSON 数据只有参与者的名称和大小。所以它导致一个更简单的对象:

```cs
//Party.cs
 
public struct PartyData
{
  public string? PartyName { get; set; }
  public short Size { get; set; }
}
 
public class Party
{
  private static List<Party> registeredParties = new List<Party>();
 
  private Cabin cabin;
  private PartyData data;
 
  public Party(PartyData record)
  {
    data = record;
  }
 
  ...
 
}
```

尽管小屋可能空置，但一旦注册，Party 对象必须与小屋相关联 - 因此我们不建议使其可空。

```cs
//Party.cs
 
public static void RegisterParty(Party party)
{
  if (registeredParties.Exists(py => party.data.PartyName == py.data.PartyName))
  {
    Console.WriteLine($"{party.data.PartyName} is already registered");
    return;
  }
 
  Cabin cabin = Cabin.FindSuitableCabin(party.data.Size);
  if (cabin != null)
  {
    party.cabin = cabin;
    cabin.SetGuestParty(party);
    registeredParties.Add(party);
    Console.WriteLine($"\"{party.data.PartyName}\" party registered in {cabin}. Happy Holidays!");
  }
  else Console.WriteLine($"No available cabins suitable for the \"{party.data.PartyName}\" party");
}
 
public static void UnregisterParty(Party party)
{
  party.cabin.SetGuestParty(null);
  registeredParties.Remove(party);
 
  Console.WriteLine($"Party \"{party.data.PartyName}\" unregistered.");
}
```

同样，注册只是作为门卫，这次确保参与者有合适大小的可用小屋住。

最后，这里是主程序中的控制台响应调用:

```cs
//Program.cs
 
List<CabinData> cabindata = JsonServices.ReadAllCabinsFromFile();
DateOnly todaysdate = DateOnly.FromDateTime(nw);
foreach (CabinData cb in cabindata)
{
    Cabin.RegisterCabin(new Cabin(cb), todaysdate);
}
/* Console Output:
 
    Holiday bookings for 9/15/2023
    Cabin "Hill View" registered
    (Cabin "Summerholme" not available at the moment)
    Cabin "Dunroamin" registered
    Cabin "Hobbit Hole" registered
    Cabin "Bear Crescent" not available at the moment)
    Cabin "Fat Cottage" registered
 
*/
 
List<PartyData> partydata = JsonServices.ReadProspectiveGuestsFromFile();
foreach (PartyData pd in partydata)
{
    Party.RegisterParty(new Party(pd));
}
/* Console Output:
 
"Smith" party registered in Hill View. Happy Holidays!
"Shah" party registered in Dunroamin. Happy Holidays!
"Lebowski" party registered in Hobbit Hole. Happy Holidays!
 
*/
 
//New party appears!
Party iverson = new Party("Iverson", 7);
Party.RegisterParty(iverson);
/* Console Output:
 
"Iverson" party registered in Fat Cottage. Happy Holidays!
 
*/
 
//The Shahs go home
Party party = Party.FindRegisteredParty("Shah");
if (party != null)
{
    Party.UnregisterParty(party);
}
/* Console Output:
 
Party "Shah" unregistered.
 
*/
 
//If the Shahs left, lets close Dunroamin
Cabin cabin = Cabin.FindRegisteredCabin(4);
if (cabin != null)
{
    Cabin.UnregisterCabin(cabin);
}
/* Console Output:
 
Cabin "Dunroamin" unregistered.
 
*/
 
//Confirm state of the registerd cabins.
Cabin.ReportRegisteredCabins();
/* Console Output:
 
The "Smith" party are staying in "Hill View"
The "Lebowski" party are staying in "Hobbit Hole"
The "Iverson" party are staying in "Fat Cottage"
 
*/
```

项目代码在 GitHub [这里](https://github.com/eastmad/TheNewStack3)可用。如果你想提高代码的功能，也许你可以更好地配合参与者的大小与可用小屋的容量。
