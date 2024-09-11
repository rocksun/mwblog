
<!--
title: 无处安放的代码-重读《企业应用架构模式》
cover: ./cover.jpg
-->

作者在多年后重读《企业应用架构模式》一书，并结合自己维护的一个企业级应用的经历，对书中的模式有了更多的认识。

> 因缘巧合，在一个早就应该毕业的年龄，我回到了我IT生涯的起点，又来到了一个做企业级应用开发的公司。这么多年来，与这个公司忽近忽远，如今进来了，颇有些感慨。我想，我的经历应该可以带来一些不太一样的认识，后面我会分享一些我对新的框架、架构和工具的看法。

我一直以重度 Kindle 爱好者和读书人自居，不过我并不是一直保持非常高的阅读量，而是有几个明显的高峰。第一个高峰就是大学毕业后的两三年，那两年我刷成了 China Pub 的某级别的会员，应该是消费 5000 元以上。想想那时的收入和现在抠抠搜搜的我，有点不理解那时的自己。

当时应该是将许多经典书籍都买到了，例如《设计模式》、《重构》、《测试驱动开发》、《Java 安全》、《编写有效用例》等等，其中就包括了这本《企业应用架构模式》。有几本书对我影响深远，例如《重构》和《测试驱动开发》，让我养成了写单元测试的习惯，不管使用何种编程语言。还有一些就像是学会了屠龙之技，例如《Java 安全》，一直只用些皮毛，直到七八年后在 IBM 从事 WebSphere 产品支持工作时，我才终于发现当年所学有了用武之地。真的，很少有软件会像 WebSphere 这样用到了 Java 各个层面的安全机制。

回到本文的重点，当年我是匆匆读过《企业应用架构模式》，最深的印象是，突然意识到了我那个宝洁（还是雅芳）归来的领导那些怪异的程序好像都能在这本书中找到原型。可惜，之后还没来得及太多的实践，我便离开了企业级开发市场。

此后的很多年，虽然我还在广义的企业级应用市场，但是我更多的是从更“底层（中间件、JDK和OS）”去提供支持，偶尔会帮助客户“不专业的”现场程序员，但是很少会去关心“企业应用架构模式”了。

直到最近，我又有机会审视一个"积累"多年的企业级应用，一种无力感突然涌向心头，我很想有人告诉我，我看到的是什么？此刻，突然想起之前有一位推友提到重读《企业应用架构模式》，是不是我也可以？

效果出人意料地好，果然我早就知道了答案，只是在潜意识里等待被唤醒。原来，这个企业级应用竟然是一份《企业应用架构模式》的百科全书，书中的每一种模式，以及各种模式的组合都能在其代码中找到鲜活的实例。恍惚间我似乎有了一种读《旧约》的感觉，自摩西以来，面对犹太人的苦难，一代代的士师不断的反思，用各种方式在《旧约》中寻求信仰的解释，不仅没有让犹太人沉沦，反而塑造了不同一般的犹太人。同样，一代代的程序员，也努力用自己的代码在这个应用中寻求答案，终于也成了这个应用的一部分。

> 虽然继续拓展这个隐喻很有意思，不过这里就不继续解读了。这里还是奉劝各位在严肃的工作中应该避免轻易的使用隐喻。你觉得精妙的隐喻，别人很有可能无法共情。更重要的是，几乎所有的隐喻都会被错误的拓展。

还是回到主题，我们看看这个应用中用到了模式。很明显，我们的代码中有着大量的“交易脚本（Transaction Scripts）”:

![](https://github.com/jaysonzanarias/patterns-of-enterprise-application-architecture/raw/master/images/TransactionScript.jpg)

这是一个显然的模式。在我们的这个企业级应用中，一个接口对应一个 Flow 类的 run 方法，领域逻辑就写在这个方法里。这个企业级应用有大量这样的方法，很多都非常的长。

如果要复用代码怎么办，最简单的方法就是写方法，但是 Flow 类再去调用其他 Flow 类的方法似乎不是很合适。那还有个办法就是使用继承，为相似的接口建一个父 Flow 类，编写一些不同接口都需要的方法，然后在各个接口的 Flow 类中调用。这样复用会好一些，但是显然也有人觉得使用继承可能并不直观，不如直接加个 if else 来的轻松。因此，某个子类的方法越来越膨胀，变成了另一个交易脚本。

这些“脚本”中还存在许多这样的代码：

```java
...
//自动结清账户校验
if ((BusiUtil.isEqualY(subMobel.getAutoSettleFlag()))&&(Busiutil.isEqualN(autosettle0k))) {
  if (BusiUtil.isNotNull(mainModel.getBaseAcctNo())){
  ...
```

是不是看的挺累，满屏幕这样的代码确实头大。有注释让这段代码略微好读了一点，但是其他问题依然存在。

如果另外一段逻辑也需要执行这个判断，应该复制这段代码吗？如果以后判断逻辑有变化，我还需要找到所有的判断去修改吗？复制代码显然是不合适的。

既然这是判断 subModel 的一个状态，是否可以给 subMobel 增加一个判断方法？似乎应该可以。不过我们这个企业级应用中，许多类似 subMobel 的对象实际是 Row Data Gateway，也就是说对应的是数据库的一条记录，而这个对象对应的类是框架自动生成的，是不能修改的。

再加一个 subMobelUtil 类来附加这样的方法吗？这样会让代码更丑，而且其他开发者很有可能不知道有这样的类存在？等等，这好像就是《企》中的一个解决方案？

其实并不是，《企》所说的第二种“领域逻辑模式” 是领域模型（Domain Model）：

![](https://github.com/jaysonzanarias/patterns-of-enterprise-application-architecture/raw/master/images/DomainModel.jpg)

图上的 Contract, Product, RecognitionStrategy 都是领域模型，即包含了数据，也包含了业务逻辑。《企》给的代码示例中，这些类完全不涉及数据库操作，不仅仅是因为数据库操作很繁琐，也是明确告诉我们，领域模型不应该与数据库操作紧密耦合，这样做有一个很大的好处，就是我们可以单独测试领域模型，这在企业级应用中无疑非常的重要。

在我们的企业级应用中，我们在业务逻辑上直接操纵 Row Data Gateway 对象，这样很直接，但是这些对象不是领域模型。面对复杂的业务时，直接操纵  Row Data Gateway 对象会让问题复杂，因此，还是应该新建一些领域模型，而通过其他方式来访问数据库。

在《企》中，当使用领域模型时，对数据库的访问推荐使用 Data Mapper ：

 ![](https://github.com/jaysonzanarias/patterns-of-enterprise-application-architecture/raw/master/images/DataMapper.png)

为了更清楚的理解，我咨询 Claude 给了我一份代码：

```java
// Domain Model
public class User {
    private int id;
    private String username;
    private String email;

    // 构造函数、getter和setter方法省略

    public void validateEmail() {
        if (!email.contains("@")) {
            throw new IllegalArgumentException("Invalid email format");
        }
    }
}

// Data Mapper
public class UserMapper {
    public User findById(int id) {
        // 模拟从数据库获取用户
        return new User(id, "user" + id, "user" + id + "@example.com");
    }

    public void save(User user) {
        // 模拟保存用户到数据库
        System.out.println("Saving user: " + user.getUsername());
    }
}

// Service
public class UserService {
    private UserMapper userMapper;

    public UserService(UserMapper userMapper) {
        this.userMapper = userMapper;
    }

    public User registerUser(String username, String email) {
        User newUser = new User(0, username, email);
        newUser.validateEmail();  // 调用Domain Model的业务逻辑

        userMapper.save(newUser);  // 使用Data Mapper持久化数据
        return newUser;
    }

    public User getUserById(int id) {
        return userMapper.findById(id);
    }
}
```

User 包含了数据和一个领域逻辑方法 validateEmail；而 UserMapper 负责数据库；UserService 负责调用 User 和 UserMapper。如果需要增加领域逻辑，直接在 User 上增加就行了。

这个例子很简单，但是正如《企》所说，简单的例子似乎无法展现领域模型模式的威力，但是我们讲东西通常希望简单明了。

回过头来看我们的企业应用。编写代码时经常会有那种无处安放的感觉，当我们不知道怎么安放时，只好就近处理，或者自己设计一种方法，但是别人又不知道你的安排，后果就是越来越乱。

《企》给我们的答案似乎相当简单，引入 Domain Model 和 Data Mapper 模式，其中 Domain Model 中编写领域逻辑，Data Mapper 负责数据库操作，而原来的 Flow 负责协调。这样我们那些复杂的判断和逻辑就有了归处，当然还需要让团队都知道这样的设计。

