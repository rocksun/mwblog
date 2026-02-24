About two years ago, I developed a small “family” bot. Its main purpose is to coordinate various aspects of our household life, including:

* **Daily Briefings:** Starting the day with a summary of the family agenda.
* **Smart Shopping:** Managing and organizing a collective grocery list.
* **Quick Reminders:** Handling fast and easy-to-set alerts.
* **Weather Forecasts:** Providing weather updates, including solar radiation forecasts tailored to our solar panel system.

The assistant operates as a **Telegram bot**, ensuring easy access from anywhere without the need for custom interfaces or dedicated apps.

### The Intelligence Behind the Assistant

Over the last two years, I’ve experimented with various Cloud AI models (ChatGPT, Claude, Gemini). The results were satisfactory across the board, partly because the task’s complexity is relatively low. The prompt and tool definitions total about **2,300 tokens**. My switching between models was primarily driven by the search for better pricing.

The more useful the assistant becomes, the more we use it—and obviously, higher usage leads to higher costs. In some months, API expenses exceeded **€12**. This is largely because the bot is **autonomous**; it doesn’t just wait for user input—it acts proactively. While this proactivity is a crucial feature, it translates into significantly higher token consumption.

I wouldn’t say €12 is “expensive,” but when you’re already paying for various AI subscriptions elsewhere, it was a cost I wanted to eliminate. More importantly, I found myself hesitating to expand its features because I was constantly thinking about the mounting API bills.

While cheaper models (DeepSeek, Qwen, GLM) have emerged recently—and platforms like **OpenRouter** offer competitive pricing—I preferred not to send personal family data to unknown servers. My goal was always to eventually use a **Local AI** as the assistant’s brain.

### The Day of Local AI Has Arrived

The bot’s code runs on a personal VPS at Hetzner, which hosts my other projects. It’s a standard setup: **4 vCPUs and 8GB of RAM**.

I ran several tests with various small, open-source models to find the “sweet spot” between response quality and enough speed to keep the experience fluid. Eventually, I decided to upgrade the VPS slightly for a few extra euros, moving to **8 vCPUs and 16GB of RAM**.

This allowed me to use larger models. While it might seem counterintuitive to want larger models on a system without a GPU (where speed is already a bottleneck), this is where the magic of **MoE (Mixture of Experts)** models comes in. They require more memory but offer significantly higher inference speeds.

The **GPT-OSS-20B** model turned out to be the perfect solution. With **Q4 quantization**, it fits into about 12GB of RAM, leaving 4GB for the OS and other applications—which is more than enough.

### Optimizing for Faster Inference

When running your own models on limited hardware, every optimization counts. It quickly became clear that the way the assistant built dynamic prompts and message history wasn’t optimized for **KV caching**. These are the types of inefficiencies that remain invisible when you’re using lightning-fast cloud models.

After several iterations and code optimizations, I reached a “good enough” solution. The prompt and tools remain at ~2,300 tokens, but processing is now much more efficient. On average, the generation speed sits at **22 tokens/sec**, which is very acceptable given the hardware and the project’s needs.

### The Trade-off

I’ve lost the “instant” responses of the cloud, but in exchange, I’ve gained **privacy, autonomy, and unlimited free tokens**. Now, I can finally focus on expanding the assistant’s capabilities without worrying about the monthly bill.

### The Future

I don’t think this is “the end” for my local AI plans with my assistant. I’m now saving every conversation to files, logging all interactions.

My plan is wait 2-3 months, clean it up a bit, and then use this as training data to fine-tune an even smaller model. Perhaps I will be able to achieve faster speed while downscaling VPS again 🙂