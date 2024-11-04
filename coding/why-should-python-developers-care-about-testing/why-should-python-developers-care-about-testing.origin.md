# Why Should Python Developers Care About Testing
![Featued image for: Why Should Python Developers Care About Testing](https://cdn.thenewstack.io/media/2024/11/d6f8348e-testing-1024x574.png)
Ever heard the old poem *“Tick says the clock.. .Tick tick. What you have to do, do quick.”?*

Well, imagine this instead: “*Please test the code… test first. What you want to push, test first.*” That line literally jumped into my head while writing this article.

July 19 will go down in history as one of the major blackouts in the history of the internet era. On that day, cybersecurity provider Crowdstrike pushed a single update to [Microsoft ](https://news.microsoft.com/?utm_content=inline+mention)Windows users around the world that crashed their systems with the dreaded blue screen of death. This happened [due to an out-of-bounds memory read](https://en.wikipedia.org/wiki/2024_CrowdStrike_incident) and affected approximately 8.5 million users. In reality, any of us could have been responsible for pushing the code to production. However, after reading through the lessons from this incident, it falls back to a timeless [preventive measure](https://www.crowdstrike.com/falcon-content-update-remediation-and-guidance-hub/#:~:text=How%20Do%20We%20Prevent%20This%20From%20Happening%20Again): Test your code.

**What Is Testing**
Though we will focus on testing [Python](https://thenewstack.io/python-3-13-blazing-new-trails-in-performance-and-scale/) code, the core concepts also apply to other standard programming languages.

Testing in software development simply involves validating that your application does what it is supposed to do. This means that your code should satisfy the [expectations](https://en.wikipedia.org/wiki/Software_testing) based on what you designed it to do. While [building either software or data pipelines in Python](https://thenewstack.io/an-introduction-to-python-for-non-programmers/), you would either have a combination of functions or classes performing some business logic. These functions typically expect an input to process and produce an expected output or even raise an exception, hence they need to be tested to ensure they do.

Let’s assume an e-commerce application is being built for a retail business to sell items to customers online. A full version of the source code can be cloned from [here](https://github.com/VICIWUOHA/python-tests-tutorial).

**Types of Tests**
In [Python programming](https://thenewstack.io/what-is-python/), the most common tests you may need for your application include but are not limited to:

- Static tests
- Unit tests
- Integration tests
**Static Tests**
Static checks ensure that our code would be compiled correctly before execution. This involves format checks and syntax checks, some of which might automatically be caught by your IDE. For our e-commerce application, we may have an Item class that looks as follows:

12345678910 |
from dataclasses import dataclass, fieldimport uuid@dataclassclass Item: name: str description: str price int sku: str = field(default_factory=lambda: str(uuid.uuid4())) |
Static checks would help us identify that we are missing a colon “:” in the price field of our Item class. So, this would never work in production. A detailed [Item class may look like this](https://github.com/VICIWUOHA/python-tests-tutorial/blob/main/src/item.py). Static checks can be done before merging Python code into production using modules like Flake8**, **Pylintand, and most recently, Ruff, which is built on Rust and used for validating Python code. It was used for this tutorial.
**Unit Tests**
Unit tests are arguably the most important type of tests assuming a developer has already written good code free of syntax errors. Unit tests ensure that the individual components of an application (classes and methods/functions) work as expected on their own. They ensure that application/business logic is not violated. Two popular frameworks used in unit testing are unittest and pytest. Our unit test example will use the unittest module.

Both libraries work similarly, but with slight differences. These modules work using assertions that should typically result in True or False results. While pytest uses raw asserts, the unittest module has its own assertion methods like `assertEquals`
, `assertIn`
, `assertRaises`
, etc. The unittest module also requires that we create our test case class by subclassing `unittest.TestCase`
**.**

### Unit Tests With the unittest Module
In our e-commerce application, a simple test for our Item class is to validate that Items created never have negative prices. This can result in a terrible loss for a retail business. See an example of this test below.

123456 |
import unittestclass TestItem(unittest.TestCase): def test_item_price_cannot_be_negative(self): # our item class should raise a ValueError if the price is below zero with self.assertRaises(ValueError): Item("External SSD", "High-speed storage for data transfer", -5.0) |
Defining such a test before business logic is part of a term called [test-driven development (TDD](https://en.wikipedia.org/wiki/Test-driven_development)). The test above being run with the unittest module, simply asserts that a `ValueError`
is raised if our Item class contains a negative price. Let’s see how to make the above test case pass.
12345678910 |
class Item: """Represents a sample item in an e-commerce system.""" name: str description: str price: int sku: str = field(default_factory=lambda: str(uuid.uuid4())) # Added to ensure our items never have a -ve price. def __post_init__(self): if self.price < 0: raise ValueError(f"Item Price cannot be a negative value: {self.price}") |
**Running the Test**
To run our unittest test in Python , we simply type the command as shown.

When we run this command, the unittest module automatically looks for any folder that has a parent class of `unittest.TestCase`
and treats its functions as tests to be validated. Tests would pass if the assertions are met and fail otherwise.

Other common CLI commands include:

python -m unittest test_module to run all tests in a module.
In our example this would be:

`python -m unittest unit_tests/test_item.py `
(pointing to the file path in the unit_tests folder) OR `python -m unittest unit_tests.test_item`
Other specific examples can be found in the [project repository](https://github.com/VICIWUOHA/python-tests-tutorial/tree/main/unit_tests#running-tests). Note that tests built with pytest are also executed in a similar manner.

**Integration Tests**
Integration tests ensure that the different components of our application work together seamlessly.

This is useful because [functionalities are usually implemented or enhanced incrementally during software development](https://thenewstack.io/how-to-define-and-use-your-own-functions-in-python/).

In the case of our e-commerce application, we built a ShoppingCart class to allow users to shop for Items. Our first method may obviously be the ability to add an item followed by a method to delete an item. A minimalistic version of our class is shown below, but a full version has been implemented [here](https://github.com/VICIWUOHA/python-tests-tutorial/blob/main/src/shopping_cart.py).

1234567891011121314151617181920212223242526272829303132 |
from datetime import datetime as dtfrom src.item import Itemimport uuidimport jsonclass ShoppingCart: """Shopping Cart Class (shortened)""" def add_item(self, item: Item, quantity: int): # check if item exists in cart , then update if self.__item_in_cart(item): self.increase_cart_item_quantity(item, quantity) else: # add new item using it's __dict__ property for easy access self.cart_obj[f"{item.sku}"] = { "item": item.__dict__, "quantity": quantity, "added_at": dt.now().strftime("%Y-%m-%d %H:%M:%S.%f"), "updated_at": dt.now().strftime("%Y-%m-%d %H:%M:%S.%f"), } print(f"==>> `{item.name}` Added to Cart.") return json.dumps( { "status": ShoppingCartStatus.CART_ITEM_ADDED.value, f"{item.name}": self.cart_obj[f"{item.sku}"], }, indent=4, ) |
**Running Tests with pytest**
We can validate that the method above works using a unit test with the command:

`python -m pytest -k test_add_items_to_cart -v`
(where -k searches for a test/file that matches the pattern following it and -v helps us get more verbose outputs. More details [here.](https://github.com/VICIWUOHA/python-tests-tutorial/tree/main/pytest_tests#running-tests))
12 |
def test_add_items_to_cart(shopping_cart: ShoppingCart, item: Item): shopping_cart.add_item(item, 40) |
**Integration Test With pytest**
While the above test works on its own, it would be necessary to test that adding a `remove_cart_item`
function to our ShoppingCartcan work alongside the `add_item`
method without issues.

We can write this test assuming we have a `cart_size`
property that shows us the unique item count in our cart.

123456 |
def test_single_item_cart_size_is_zero_after_removal( shopping_cart: ShoppingCart, item: Item): shopping_cart.add_item(item, 40) shopping_cart.remove_cart_item(item) assert shopping_cart.cart_size == 0 |
The test above validates that after a single item is added to and removed from the cart, the cart size should reduce to zero. This validates that the interaction between our ShoppingCart and its methods yields the expected behavior.
We can now run all our test cases using the simple command below.

python -m pytest
**Notes About pytest**
- By running the command above, note that without explicitly telling pytest which folder, file or pattern to use for its test discovery, it would run all tests in your directory including test cases that are subclasses of
`unittest.TestCase`
. - Pytest does not require us to define classes for our test cases. Unittest on the other hand requires classes because it was originally inspired by the JUnit testing framework used for Java applications.
- More information on configuring tests have been provided in the
[source repository](https://github.com/VICIWUOHA/python-tests-tutorial/)for this project.
**Conclusion**
Testing in Python helps to reduce or totally avoid unwanted failures in production. It is important to note that tests can be automated to run on code bases using continuous integration platforms like GitHub Actions.

As with any programming paradigm, it is nearly impossible to test all future edge cases that may arise in real-life scenarios. Therefore, deployment of software that has been battle-tested should still have a rollback plan and be done in phases where possible, just in case things go wrong.

Are you looking for skilled Python specialists to help take your projects to the next level? Then check out Andela’s guide, [“How to Hire Python Developers](https://www.andela.com/blog-posts/how-to-hire-a-python-developer-a-guide-to-finding-the-right-fit/?utm_medium=contentmarketing&utm_source=tns&utm_campaign=brand-global-python-testing-blog&utm_content=how-to-hire-python-developers).”

[
YOUTUBE.COM/THENEWSTACK
Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.
](https://youtube.com/thenewstack?sub_confirmation=1)