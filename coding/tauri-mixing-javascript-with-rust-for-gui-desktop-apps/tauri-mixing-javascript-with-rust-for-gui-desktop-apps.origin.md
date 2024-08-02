# Tauri: Mixing JavaScript With Rust for GUI Desktop Apps
![Featued image for: Tauri: Mixing JavaScript With Rust for GUI Desktop Apps](https://cdn.thenewstack.io/media/2024/07/a75b38c0-tengyart-7puyvaygtta-unsplashb-1024x682.jpg)
In [my first review of Tauri](https://thenewstack.io/how-tauri-turns-web-designs-into-compact-native-apps/) in January 2022, I noted that it is a framework to build desktop applications with any frontend framework and a Rust core. Since the Rust language has [significantly advanced in popularity](https://thenewstack.io/rust-the-future-of-fail-safe-software-development/) over the past two and half years, I thought it was worth revisiting Tauri again — especially since [it recently introduced version 2](https://v2.tauri.app/blog/tauri-2-0-0-beta/).

Tauri’s elevator pitch to **“build an optimized, secure, and frontend-independent application for multiplatform deployment” **is recognizable from before, but more deployment targets makes it more in line with the [other](https://thenewstack.io/introduction-to-omakub-a-curated-ubuntu-environment-by-dhh/) [products](https://thenewstack.io/introduction-to-moonbit-a-new-language-toolchain-for-wasm/) I’ve posted about recently. The bonus is the ability to build desktop and mobile apps using only familiar web methods.

We get the security of Rust but the familiarity and flexibility of web development.

We’ll try and see if the path has gotten a bit smoother to building a UI app that I can run fully packaged on my Mac. Tauri still refers to itself a ‘toolkit’, which is still true.

Conceptually, Tauri acts as a static web host. So Tauri works with Rust crates and the system’s native web view to output a modest-sized executable application. In theory, we get the security of Rust but the familiarity and flexibility of web development.

The [getting started](https://v2.tauri.app/start/) route is looking a bit fresher, with the now popular single line start. Before we do, I suspect that I have an old Rust installation, so I should update this. Using the [prerequisite instructions](https://v2.tauri.app/start/prerequisites/#rust):

At the end, it reminds you to start a new shell or to source the env file. I note a new friendlier accent to all this — as if, maybe, Rust is now popular!

Ok, now I should be able to use the Tauri one-liner:

Note that we are already going into the beta for Tauri 2.0.

The template install options recognize the more varied nature of the toolkit. I could use .NET, but I’ll use JavaScript for a more general-purpose view. Obviously, Rust is also available.

I kept my slightly old npm / node combination and built my template:

Then we run the template within the dev environment:

This builds all the packages we need to start with and the first time takes a few minutes. These will be how Rust talks to your OS windowing. And eventually, it launches the application:

So we have an app started and popping up, appearing in my tray as a standard Mac app.

OK, let’s take a look at how this is made up. Before we dive in, note that hitting the icons starts a browser page, and entering your name in the text box and pressing the button displays a greeting:

This will help us work out the bit of Rust later on. The code structure is what one would expect for a web app:

I chose vanilla JavaScript, so we get a very vanilla **index.html** in our template:

12345678910111213141516171819202122232425262728293031323334 |
<!doctype html> <html lang="en"> <head> <meta charset="UTF-8" /> <link rel="stylesheet" href="styles.css" /> <meta name="viewport" content="width=device-width, initial-scale=1.0" /> <title>Tauri App</title> <script type="module" src="/main.js" defer></script> </head> <body> <div class="container"> <h1>Welcome to Tauri!</h1> <div class="row"> <a href="https://tauri.app" target="_blank"> <img src="/assets/tauri.svg" class="logo tauri" alt="Tauri logo" /> </a> <a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript" target="_blank" > <img src="/assets/javascript.svg" class="logo vanilla" alt="JavaScript logo" /> </a> </div> <p>Click on the Tauri logo to learn more about the framework</p> <form class="row" id="greet-form"> <input id="greet-input" placeholder="Enter a name..." /> <button type="submit">Greet</button> </form> <p id="greet-msg"></p> </div> </body> </html> |
The central `div`
displays an image in an anchor, which deals with the link behavior. Note that the JavaScript is in **main.js**, and that the app title on the window itself is not that which is defined here. And we have a very old school `form`
for entering the input text. So we know that we will have to process that form to extract the entered name, and place the result in the final `p`
. This is the content of** main.js:**
123456789101112131415161718 |
const { invoke } = window.__TAURI__.core; let greetInputEl; let greetMsgEl; async function greet() { // Learn more about Tauri commands at https://tauri.app/v1/guides/features/command greetMsgEl.textContent = await invoke("greet", { name: greetInputEl.value }); } window.addEventListener("DOMContentLoaded", () => { greetInputEl = document.querySelector("#greet-input"); greetMsgEl = document.querySelector("#greet-msg"); document.querySelector("#greet-form").addEventListener("submit", (e) => { e.preventDefault(); greet(); }); }); |
After selecting the active elements and adding an event listener to the form button, we run a function to process the input and stick it into that output paragraph. This is where a bit of Rust is called for, so we get an idea of how that works.
If we go back into our main directory in the generated area, we note there is src-tauri:

And in that we have some Rust code within **src**, in **main.rs:**

1234567891011121314 |
// Learn more about Tauri commands at https://tauri.app/v1/guides/features/command #[tauri::command] fn greet(name: &str) -> String { format!("Hello, {}! You've been greeted from Rust!", name) } fn main() { tauri::Builder::default() .plugin(tauri_plugin_shell::init()) .invoke_handler(tauri::generate_handler![greet]) .run(tauri::generate_context!()) .expect("error while running tauri application"); } |
We are able to see how the invoke call in JavaScript reaches to a Rust **greet** function that deals with the string. This is nice, as we have access to Rust functions that Tauri is managing for us. (We also need to tell the builder about the **greet** function too.)
The final file to show is a JSON configuration which controls the window itself, **tauri.conf.json**:

12345678910111213141516171819202122 |
{ "productName": "thenewstack", "version": "0.0.0", "identifier": "com.tauri.dev", "build": { "frontendDist": "../src" }, "app": { "withGlobalTauri": true, "windows": [ { "title": "thenewstack", "width": 800, "height": 600 } ], "security": { "csp": null } }, "bundle": { "active": true, "targets": "all", "icon": [ "icons/32x32.png", "icons/128x128.png", ... ] } } |
Just to ensure we have understood everything, let’s make an identifiable target, and call a nice new greeter.
We change the target above to make it smaller, with a unique identifier:

12345678910111213141516 |
{ ... "identifier": "io.thenewsatck", ... "app" : { "windows": [ { "title": "Welcome to TheNewStack", "width": 600, "height": 200 } ... }, ... }} |
Then we alter the message code appropriately. This will force the build to check for changes.
Finally, we run the full build, to see what it does with the executable.

This also takes time, since it is the first time. The result is a dmg and an app file. Once we move the app into the application folder, we can execute it as a normal Mac app:

The app size is still a little chubby (10.7 MB), but I have done nothing to pare down the crates that would automatically get added to the template.

## Conclusion
I think we get from zero to hero very quickly with the template, although the flexibility of allowing for a range of JavaScript frameworks does make everything a little more complex. I wonder if a more opinionated approach might be better. But overall I think Tauri is still a very solid solution to creating desktop apps without worrying about window internals.

[
YOUTUBE.COM/THENEWSTACK
Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.
](https://youtube.com/thenewstack?sub_confirmation=1)