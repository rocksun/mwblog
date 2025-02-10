# Developer’s Introduction to the Replicate AI Playground
![Featued image for: Developer’s Introduction to the Replicate AI Playground](https://cdn.thenewstack.io/media/2025/01/04e22e8b-zdenek-machacek-9o9nkvr8c6y-unsplashb-1024x576.jpg)
Right now, there is a whirling gyre around what to look at next within the LLM world. Should a developer be playing with existing models, extending existing models, or creating those models from scratch? After updating my post about [using local models with Ollama](https://thenewstack.io/how-to-set-up-and-run-a-local-llm-with-ollama-and-llama-2/), I thought I’d switch to looking at a cloud-based framework for this post.

[Replicate](https://thenewstack.io/simplify-ai-development-with-machine-learning-containers/) is a cloud platform that allows users to easily run and fine-tune various open source AI models. They claim that about 20,000 open source models are available, including (inevitably) DeepSeek. But what is the process for using any of these models?
First of all we need to join Replicate, and maybe stake a bit of cash for running the models. I notice there is a [playground](https://replicate.com/playground), so I will go straight to that. Playgrounds are nearly always a [good sign](https://thenewstack.io/playgrounds-for-developers-uses-and-design-patterns/) for indicating that a framework is trying to make itself accessible.

As is getting increasingly common, you sign in exclusively with GitHub:

Given we are using cloud models, the next important thing is spend control:

Without the above, this would be a harder venture to assess cost-wise. But if you read carefully, you can still get a small overcharge. This is unlikely to exceed the price of a cup of coffee; but instead of monthly spend limits, they should allow one-and-done upfront payment credits.

The playground (which is beta) seems to weigh towards image and video creation right now — and these are actually the hardest things to experiment with.

The fact that mobile devices are even considered tells you how rapidly things are moving.

So, as we are invited to do, let’s get started. There are about 20 video and image models to start with, defaulting to this one:

We’ve all seen plenty of text-to-image solutions, so video is interesting.

I asked for a video of a dolphin stacking crates for some reason. We get to choose the height and width of the video (1280 pixels max). You can also choose the number of frames (up to 200). I’m happy with the 129 default.

You get to choose a denoising level between 1 and 10. At higher values, it becomes more imaginative, ignoring the original image. (Diffusion models generate images by gradually refining noise-based images). Finally, we get to control frames per second (fps), defaulting to 24. By comparison, games like to run at about 60 fps to look smooth.

This can all be represented as the following Python query:

12345678910111213141516 |
import replicateoutput = replicate.run( "tencent/hunyuan-video", input={ "embedded_guidance_scale": 6, "fps": 24, "height": 480, "infer_steps": 50, "prompt": "A dolphin stacking crates", "video_length": 129, "width": 864 })print(output) |
When we ask to run the model, we get a rotating icon, but otherwise, there are no further indications. I got a time of creation and a status of “starting.” But nothing else. In effect, the request is “queued.”
However, when I dug into “full prediction” I got everything I wanted:

We see the server communication logs and percentage-to-complete slider. Finally, I got my 5 seconds of a dolphin playing atop some blue crates. Given that dolphins do not have opposable thumbs, this is a fine representation.

And of course, while not free, this did not break the bank,

The final JSON output is instructive and well-constructed:

123456789101112131415161718192021222324252627282930 |
{ "completed_at": "2025-01-30T15:46:02.616901Z", "created_at": "2025-01-30T15:38:40.721000Z", "data_removed": false, "error": null, "id": "mpnsqxjat5rme0cmpzesjjnhrr", "input": { "fps": 24, "width": 864, "height": 480, "prompt": "A dolphin stacking crates", "infer_steps": 50, "video_length": 129, "embedded_guidance_scale": 6 }, "logs": "[Cut for length]" "metrics": { "predict_time": 123.354543706, "total_time": 441.895901 }, "output": "https://replicate.delivery/xezq/MJwQYO6neiVZXSqvxR9ZGuH4JBUepizHJOrrxFsfAcH0FqUoA/output_48685.mp4", "started_at": "2025-01-30T15:43:59.262358Z", "status": "succeeded", "urls": { "stream": "https://stream.replicate.com/v1/files/bsvm-mwhlz4a7gckbdbosoa4kzxebkplhhoq3ji57bbe7q34tt4qceimq", "get": "https://api.replicate.com/v1/predictions/mpnsqxjat5rme0cmpzesjjnhrr", "cancel": "https://api.replicate.com/v1/predictions/mpnsqxjat5rme0cmpzesjjnhrr/cancel" }, "version": "6c9132aee14409cd6568d030453f1ba50f5f3412b844fe67f78a9eb62d55664f"} |
Note that the job has an associated ID, which is how it is referred to in the UI.
But the important thing is that we are free to tweak the model after making it. I’ll simply ask for orange crates in the tweak run. Now, the interesting thing is how much work will now be done and at what cost. We are told that this model is now in a different version.

The process was indeed shorter, coming in at two minutes:

The completion JSON more accurately states the time spent:

1234567 |
{ "completed_at": "2025-01-31T14:05:41.469428Z", "created_at": "2025-01-31T14:01:32.512000Z", ... "started_at": "2025-01-31T14:03:38.143858Z", ...} |
I think the differentiation between “started” and “created” is when your query is taken off the queue and worked on. Services like [Midjourney](http://midjourney.com) give you a certain amount of “priority” time, which might be a way to demystify this aspect.
While the video did have the dolphin clipping the crates, and the crates look somewhat odd, the basic functionality seems to have worked. My query was very basic.

Checking the billing, the cost was about the same as before:

In fact, they emailed me quickly after the first dollar was spent, which was sensible.

**Conclusion**
I have limited myself to the playground, which is in beta, but Replicate shows signs of being quite a complex system. I like the fact that it shows you how to convert any request you make on the form into Python or Node, etc. The REST-styled JSON output with links to the output looks comprehensive.

Right now, some of the definitions are not entirely clear (whether “tweaking” is “tuning”, what exactly has been versioned, and the relationship between one version and another) and I hope all their multimodal models eventually get into the playground. If they are vigilant, then I suspect keeping the end user apprised of costs will be fine — but fixed credit amounts would still be sensible.

The win here is that you can potentially explore so many models in a controllable fashion while keeping the developer connected to the backend processes and code.

[
YOUTUBE.COM/THENEWSTACK
Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.
](https://youtube.com/thenewstack?sub_confirmation=1)