While code and data interplay with each other to form running programs, we still tend to concern ourselves more with how code is presented than how data is presented. While masses of streaming data can often move unseen and is truly meaningless, [JavaScript Object Notation (aka JSON)](https://thenewstack.io/an-introduction-to-json/) was specifically designed as a standard text-based format for representing small amounts of human-readable structured data.

The first time you might come across the need for this type of representation is when you want to persist or save state from a program. Typically, a game developer might want to “save” the position of a game to restart later — that is, to save the state of all the objects that represent the current state of the game. We use the term “marshaling” or “serialization” when referring to turning an in-memory format of an object to a standard storage format. While most languages will have an internal binary way to persist state, using JSON keeps your data open and interchangeable.

This post explores JSON from a fairly simple level, but hopefully you will appreciate that its form on the page is quite important.

## Why JSON Is Better than XML for Data Marshalling

While it is a subset of JavaScript, JSON was initially seen as a welcome replacement to the much-maligned XML (eXtensible Markup Language), which was both verbose and complex to parse. That was because it was doing more self-description than was necessary for mere marshalling.

But XML was at least human-readable. This meant it could be reviewed by non-programmers, and it helped to expand the development world. (As a heavy [Ruby](https://thenewstack.io/why-ruby-on-rails-is-still-worth-your-while-as-a-developer/) user, I was also familiar with another format called [YAML](https://thenewstack.io/with-yamlscript-yaml-becomes-a-proper-programming-language/), which is still favoured for configuration files today.)

The idea of “readable” data needs a little explanation. In this case, it does not really mean, “I want to read the data.” It means, “I want to be able to understand the shape of things.” There is a sweet spot where small amounts of data can be viewed efficiently, but in a structure that helps the reader parse it naturally.

So JSON data is ideal for readable data that’s intended to be stored in files or with code. JSON is often used in configuration files, as new data can be read in without touching code. Slightly different versions of the same structure (e.g., extra or missing keys) are quite easy for language parsers to manage. You can ignore new keys, or mark keys as “optional.”

The crux of the matter is that if you are working with people who are focusing on content, you rely on tools to let them contribute directly. JSON is good for that.

## A Practical Example of JSON: Describing a Cat

I asked ChatGPT to “describe an average cat in JSON”. It replied with the following:

```
{
  "species": "Felis catus",
  "average_age_years": 4,
  "average_weight_kg": 4.5,
  "body_length_cm": 46,
  "tail_length_cm": 30,
  "fur": {
    "length": "short",
    "texture": "soft",
    "common_colors": ["black", "white", "gray", "brown", "orange"],
    "patterns": ["solid", "tabby", "bicolor", "calico"]
  },
  "eyes": {
    "shape": "round",
    "colors": ["green", "yellow", "blue", "amber"]
  },
  "ears": {
    "shape": "triangular",
    "position": "upright"
  },
  "temperament": {
    "independence": "moderate",
    "affection": "selective",
    "playfulness": "moderate",
    "curiosity": "high"
  },
  "activity_level": "medium",
  "sleep_hours_per_day": 14,
  "diet": "obligate carnivore",
  "vocalization_level": "low to moderate",
  "lifespan_years": {
    "indoor": 15,
    "outdoor": 8
  }
}
```

JSON doesn’t require the previous definition of cat before helping ChatGPT proceed to showing us a cat. In fact, this feels like a reasonable format to describe any small mammalian pet.

Even if you had not seen JSON before (but had dabbled with some programming), this is very readable. There are a bunch of key/value pairs. Strings use quotes, otherwise there are floating point numbers. You could guess (correctly) that it also recognises `true` and `false` for binary. There are substructures and arrays. There are, for example, effectively four attributes of “temperament.” Eye colour has four possible values. The keys within “temperament” already seem cat-like, even without the actual values.

And I have no idea what a “medium activity” level is. But the large language model (LLM) was happy to participate in my slightly whimsical request, because JSON is fine with this. In fact, JSON is quite useful in LLM prompts, as it is a sharp way of introducing design nomenclature without writing any code.

I made the same request for XML, but the result was approximately 75% bigger because it has to repeat opening and closing tags to parse properly. (A version of JSON also exists with comments, but that isn’t quite standard.)

## How to Parse JSON Data in Your Code

Most languages have common libraries for parsing JSON, which means I could write a bit of Ruby to read the cat back into memory. I’ll allow ChatGPT to do the honors, and write the parsing code for Ruby. This assumes that I saved our previously mentioned JSON generic cat in a file called “cat.json”:

[![](https://cdn.thenewstack.io/media/2026/01/7d8aabe8-image-1024x834.png)](https://cdn.thenewstack.io/media/2026/01/7d8aabe8-image-1024x834.png)

After saving this code as “cats.rb”, I run it in my terminal (assuming that I have a Ruby installation):

[![](https://cdn.thenewstack.io/media/2026/01/9e736528-image-1.png)](https://cdn.thenewstack.io/media/2026/01/9e736528-image-1.png)

Thus, the cat is revived.

## Using FracturedJson to Improve Readability

I recently heard about a nice library called [FracturedJson](https://github.com/j-brooke/FracturedJson), which is “a JSON formatter that produces human-readable but fairly compact output.” I think this moves us a bit nearer to that sweet spot.

This doesn’t actually have a Ruby library yet, so first we’ll put it through its paces initially with the [browser](https://j-brooke.github.io/FracturedJson/). Let’s see how it shapes our persisted cat:

[![](https://cdn.thenewstack.io/media/2026/01/2b99aad1-image-2-1024x644.png)](https://cdn.thenewstack.io/media/2026/01/2b99aad1-image-2-1024x644.png)

It only makes a few choices, including fixing the space formatting and keeping attributes on the same line where it can.

We could also use this in VS Code, as there is a NuGet library for FracturedJson. As usual, I started VS Code in my terminal, created a console project and added the NuGet library. Then I added the handful of lines to reshape the cat:

[![](https://cdn.thenewstack.io/media/2026/01/cac59c3f-image-3-1024x819.png)](https://cdn.thenewstack.io/media/2026/01/cac59c3f-image-3-1024x819.png)

You can see from the code that the heavy lifting is done by .NET `System.Text.Json` services, and that FracturedJson is just a formatter. It also has extra options to explore, as you can see from the browser example.

## The Importance of Readable JSON in Development

Parsing JSON data quickly by eye is still a very useful skill in the information-dense forest of computing. And any tool that helps form a quiet glade is welcome.

Small amounts of JSON also work well in LLM prompts, to steer tasks without programming. FractureJson tries to get your JSON string data nearer the sweet spot of readability and compactness, helping us to admire that persisted cat a little more easily.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://cdn.thenewstack.io/media/2022/09/2e2ac7a2-cropped-a46bbf33-photo.png)

David has been a London-based professional software developer with Oracle Corp. and British Telecom, and a consultant helping teams work in a more agile fashion. He wrote a book on UI design and has been writing technical articles ever since....

Read more from David Eastman](https://thenewstack.io/author/david-eastman/)