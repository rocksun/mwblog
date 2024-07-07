# 5 Clean Code Tips for Reducing Cognitive Complexity
![Featued image for: 5 Clean Code Tips for Reducing Cognitive Complexity](https://cdn.thenewstack.io/media/2024/07/6f4145ce-scrubbing-1024x576.jpg)
You probably understand the frustration that comes with trying to understand someone else’s old code — or even your own. Time away has messed with your memory, and now you’re losing the thread of the code.

Creating code you and others can actually understand is imperative. Reducing cognitive complexity is key to helping you write secure, maintainable and reliable [clean code](https://www.sonarsource.com/solutions/clean-code/) that makes other developers, including yourself, happier in the long run. Here’s how you can take a disciplined approach.

## 1. Write Code Your Team Will Love You For
[Software development is very much a team sport](https://thenewstack.io/managing-software-development-team-dynamics-from-within/). It’s critical to understand how the code you write will fit into an overall project and be understood by the other developers who need to be able to read it.
Cyclomatic complexity was first brought onto the scene as a way to gauge the ease of testing and maintaining a module’s control flow. This formula can help with assessing how much testing is needed based on counting the number of branches in the code. It won’t give a good view of how hard it will be for you or your teammates to understand and maintain the code in the future.

## 2. Life Isn’t All Full-Speed Ahead
Linear code is your friend. If all code was a chain of commands with one following the next — no looping or meandering — you’d have no problem keeping everything straight in your head. Adding loops and branches to your code makes it increasingly difficult to understand and work on.

The cognitive complexity of the code increases incrementally every time you do that. The problem is that developers need to be able to [write code that loops and branches](https://thenewstack.io/bad-code-stalls-developer-velocity/), including code that uses if/else statements, to create software. What’s key here is mindfulness. Know what you’re using and be clear about whether or not your code is doing too much. If it is, consider refactoring. Understanding the cognitive complexity of your code can help you determine when and where you need to simplify.

## 3. Nesting Can Create Chaos Quickly
Nested code, for instance, loops inside loops, is difficult to understand. And the deeper you nest code, the more effort it’s going to take to straighten things out in your head and understand every piece of code you’re dealing with.

Take a look at your code and see which nested components are causing the greatest headache. Then, find a different way to write the code. Understanding the cognitive complexity each component adds will help guide you down the right path.

## 4. Useful Things Don’t Increase Complexity
Plenty of constructs exist that make code clearer and easier to understand. Switch statements are a good way to help eliminate a series of nested if or if/else statements that make code murky and muddled, and they don’t add to the cognitive complexity of the code. Continue or break statements that help you jump out of a loop can also help with writing clearer code, and once again won’t increase the complexity. These are only a few of the different kinds of constructs that can help reduce cognitive complexity.

## 5. Use the Right Tools and Write Clean Code
Tools like [SonarLint, SonarQube, and SonarCloud](https://www.sonarsource.com/lp/products/all/) have built-in cognitive complexity measurement features that can help you write code that is written not just to run well, but also to be understood and built upon. They can help you take a better, closer look at your code so you can understand where you’re making things more complicated than they need to be. Focus on writing code that is easy to understand and your team and your future self will thank you!

Developers should always focus on writing [clean code](https://www.sonarsource.com/solutions/clean-code/) — code that is secure, reliable, readable and maintainable, saving all who use it major migraines in their software projects. With the right mindset and tools in place, you can ensure that your code is a help and not a hindrance to the [quality of your software](https://thenewstack.io/5-takeaways-from-smartbears-state-of-software-quality-report/).

[
YOUTUBE.COM/THENEWSTACK
Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.
](https://youtube.com/thenewstack?sub_confirmation=1)