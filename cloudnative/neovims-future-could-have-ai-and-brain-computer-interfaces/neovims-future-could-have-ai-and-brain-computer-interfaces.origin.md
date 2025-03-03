# Neovim’s Future Could Have AI and Brain-Computer Interfaces
![Featued image for: Neovim’s Future Could Have AI and Brain-Computer Interfaces](https://cdn.thenewstack.io/media/2025/03/53f8c39d-novim-1024x768.jpg)
Berlin-based Neovim maintainer [Justin M. Keyes](https://github.com/justinmk) shared a strange phrase to open his traditional “[State of Neovim](https://www.youtube.com/watch?v=TUzdcB_PFJA)” keynote at the annual Vim conference in Tokyo. ([Neovim](https://neovim.io/) is a modern refactoring of the [Vim text editor](https://thenewstack.io/vim-after-bram-a-core-maintainer-on-how-theyve-kept-it-going/).) It was something he’d overheard a random sports fan saying that seemed to hold “some sort of symbolism”:

“The Giants Have No Timeouts.”

“He’s giving us a memo,” Keyes told his audience. “He’s telling us that we need to move fast.” So the driving question now, as Keyes sees it, is not just how to be the best [Vim-like](https://thenewstack.io/a-look-at-vim-a-text-editor-for-the-ages/) modal text editor, but how does Neovim compete with other projects like VS Code and Zed?

So as thousands of Neovim fans watched, Keyes shared his chart of what’s been propelling the project over the years. It started with Neovim’s technical architecture (and multithreading support), and as it gained momentum, there was more conscious project management for “channeling energy into useful directions.”

But by 2024, Neovim was ready to survey the larger market of all text editors, “looking for signals from — you know, what is the world telling us, what is the universe telling us.”

And for Keyes that means “thinking about brain-computer interfaces, thinking about the architecture of other projects like VS Code and Zed, thinking about how we could maybe leverage Zig and things like that.”

With mind-boggling ambition, Keyes offered his audience a forward-looking assessment of Neovim — but also some wide-ranging thoughts on the computing landscape in general. Eyes on the future, he shared not only his thoughts on new features and coming changes for Neovim, but also on the role of AI in text editors, and even the possibility of a [WebAssembly](https://thenewstack.io/top-5-uses-of-webassembly-for-web-developers/)-based Neovim artifact that could be used in other software.

And yes, brain-computer interfaces kept coming up.

## A World Beyond Keyboards
“In 10 years, probably, brain-computer interfaces will be not uncommon,” Keyes said matter-of-factly, “and keyboards are going to be more of a fallback input method.

“This is kind of interesting to think about, not only for Vim and Neovim, but Zed and [VS Code](https://thenewstack.io/how-to-use-vs-code-for-python-and-why-you-should/) and other types of development tools.”

Even in that far-away future, Keyes thinks Vim-like editors, with their macro-friendly programmability and logically structured interfaces, will remain relevant “for at least the first couple of generations of brain-computer interfaces, even if the literal keys on a keyboard are no longer relevant!”

And in this world with brain-computer interfaces, “buttons and menus are going to be even more outdated than keyboard-driven interfaces.” So while Vim-like editors let users choose different “[modes](https://www.warp.dev/terminus/vim-modes)” for text editing — like “visual” for selecting text chunks — Keyes is surprised modes don’t seem to exist in Zed and VS Code.

Which they’ll need when brain-computer interfaces come along.

## AI in IDEs
Keyes is aware that rival editors like VS Code and Cursor are including some AI features, but he’s already looking ahead to the future. “Eventually, it’ll find its way hopefully into Neovim, if we set things up in the way that we should. And that’s our job, is to see what the gaps are, so we can help either third-party extensions give the kind of context that is needed to AI extensions, or possibly build some primitives into our standard library if it comes to that for that.” (Keyes also believes that AI “is a feature; it’s not a product.”)

I desperately want neovim to win the AI race.

— Benjamin Scott (@TheBenzend)

[February 21, 2025]
But Keyes described himself as “excited about AI,” and even put up an example of a prompt he’d used that successfully generated a first pass at a Neovim function. “That’s useful,” he said, “And that is why our documentation is important.”

One slide finished the thought:

“If you don’t explain/document things for humans, the AI will also be weaker.”

Keyes added thoughtfully that AI is “an extra brain.” And he’s excited about AI.

## Coming Soon
Looking to Neovim’s more immediate future, Keyes presented his proposals for next year, “the things that I really, really, really want to solve next year.” And top of his list? “Press-Enter needs to go away,” he said, referring to a combination of keys that need to be hit to confirm exceptions. Keyes called these mandatory confirmations “evil,” and “the reason that people think other projects are more stable.” He added: “When exceptions get thrown in VS Code, VS Code does not, like, send you an email and print out a fax, or whatever. It just logs it. That’s what we should do.”

things you can, and should, do with Neovim:

cursor trails[https://t.co/351IF6pCFT][pic.twitter.com/Zsg8Mym55i]— Justin M. Keyes (@justinmk)

[December 4, 2024]
Another coming feature was inspired by tmux, the terminal multiplexer. “Now soon what will land is that you can just hit one Ctrl+Z and detach your UI from any Neovim session.”

Keyes also put up a list of “stuff that is relatively easy to do, that we should just do. It just makes the editor a complete answer, a complete application.” For example, when users drag and drop a file into Neovim, or paste in an image or a URL, “it should do something useful.” He also wants to get started on an API for images. And there should be profiling and debugging for the Lua scripting language.

Keyes described much of his list as “aspirational … except for presentation mode.” When Neovim opens a file that’s been formatted with [Markdown](https://en.wikipedia.org/wiki/Markdown), Keyes wants to see an easy way to toggle between formatted and unformatted text. “I propose maybe Z+Tab or Backspace as the keys,” Keyes said. “Maybe even Help docs, and I don’t know what else — but at least Markdown. Markdown is the JSON of the docs world. It’s just … it’s everywhere. You need to support it.”

## What If?
Keyes reminded the audience of his [favorite site for downloading Neovim plug-ins](https://dotfyle.com/neovim/plugins/trending), while adding as another aside that there could even be some kind of Neovim package format “hopefully next year.”

He returned to it later with a slide with just one line:

“**Future**: *packspec pkg.json*”

It referred to the new packaging format Keyes is working on.

“I do think that we should get around to trying out this package format and seeing what happens with it. It’s a low-cost thing to try out. There’s like 5% remaining to do on the spec that I just need to finish, and then we can see where that goes.”

But Keyes also took a moment for some what-if scenarios. What if Vim’s modal text editing became a library, allowing it to be integrated into projects? Keyes’ response? “That’s one way things could go,” but another direction would be if Neovim itself became “consumable” by other projects. Maybe Neovim could have its own WebAssembly artifact offering speedy modal-text-editing functionality, “and just text editing in general.”

And this leads Keyes to an interesting aside. “You need interactive commands, and any project that doesn’t start out with this ends up adding it in some kind of limp form later on.”

## No Data-Science Witch Doctors
Keyes reminded his audience that VS Code’s documentation [acknowledges](https://code.visualstudio.com/docs/getstarted/telemetry) it “collects telemetry data, which is used to help understand how to improve the product.” But Neovim is popular “even though we never hired any data-science witch doctors to tell us what the users want.

“Actually it turns out you can get a pretty good signal about that from the issue tracker, social media and also your own intuition.”

And as proof, Keyes shared that Neovim had reached another milestone. “We have doubled the number of GitHub downloads since last year. That’s some sort of signal.”

“It could even be from bots, or whatever. It doesn’t matter, because guess what? We have twice as many bots as we did last year downloading from GitHub!”

And for the Homebrew installer, “for the first year ever we have more installs than Vim itself.” Keyes’ slide shows 373,000 downloads for Neovim and 296,000 for Vim — where in 2023, Vim’s 238,000 downloads were 20,000 more than Neovim.

It all seemed to prove that the state of Neovim is strong. In perhaps the ultimate sign of health, even its contributor count is growing. “And for the fourth year in a row, we were ‘Most Loved’ on Stack Overflow,” Keyes added. “Whatever that means. We have no idea, but we’re winning it every year, and so it’s very important. Until we stop winning it!”

“This is all you need. You don’t need telemetry.”

[
YOUTUBE.COM/THENEWSTACK
Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.
](https://youtube.com/thenewstack?sub_confirmation=1)