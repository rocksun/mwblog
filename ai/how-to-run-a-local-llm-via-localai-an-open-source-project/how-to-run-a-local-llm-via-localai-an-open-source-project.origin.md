# How to Run a Local LLM via LocalAI, an Open Source Project
![Featued image for: How to Run a Local LLM via LocalAI, an Open Source Project](https://cdn.thenewstack.io/media/2024/04/643fba12-erik-mclean-ox72sudwbea-unsplash-1024x683.jpg)
Earlier this year I wrote about
[how to set up and run a local LLM with Ollama and Llama 2](https://thenewstack.io/how-to-set-up-and-run-a-local-llm-with-ollama-and-llama-2/). In this article, I’ll look at an alternative option for running large language models locally. While Ollama is a private company, [LocalAI](http://Localai.io) is a community-maintained open source project.
On the face of it, they each offer the user something slightly different. From Ollama, I effectively get a platform with an LLM to play with. However, LocalAI offers a drop-in replacement to OpenAI’s API. In practice, that means I can use OpenAI URIs but just point to the container.
Another difference is in how the two products deal with containers. LocalAI leverages Docker — and that is its main method — but it also allows you to build the container or the binary by hand. Ollama recommends using Docker to get GPU acceleration but otherwise works without it.
Let’s get started. Note that I have Docker Desktop installed on my Mac.
LocalAI offers an all-in-one (AIO) setup that is close to Ollama’s offering. This is smart, as I can specialize where I need to later while starting with a full setup.
I opened my
[Warp command line](https://thenewstack.io/a-review-of-warp-another-rust-based-terminal/) and ran the docker prompt below from the docs. I’ll pace this walkthrough at a moderate speed, but I do assume the reader is [comfortable with Docker](https://thenewstack.io/tutorial-create-a-docker-image-from-a-running-container/). I left it to pull, and as you can see, it took about an hour:
At completion, you can see the model services it offers with the AIO pack:
More explicitly, the response to the curl
http://localhost:8080/v1/models gave:
|
1
2
3
4
5
6
7
8
9
|
{"object":"list","data":[
{"id":"text-embedding-ada-002","object":"model"},
{"id":"whisper-1","object":"model"},
{"id":"stablediffusion","object":"model"},
{"id":"gpt-4-vision-preview","object":"model"},
{"id":"tts-1","object":"model"},{"id":"gpt-4","object":"model"},
{"id":"MODEL_CARD","object":"model"},
{"id":"bakllava-mmproj.gguf","object":"model"},
{"id":"voice-en-us-amy-low.tar.gz","object":"model"}]}
A model card is a metadata container.
Cranking the handle in Docker desktop got us running:
The documentation does leave you alone a bit here, but fortunately the first steps are given by the test curl in the final message as the image is verified:
It is worth noting that I stopped and started the installation a few times, and the above message was caught when I restarted the container in Docker desktop. Both Docker Desktop and Warp have sufficiently good log handling to allow you to peruse these messages later. There are similar tests in the documentation.
This is the test I would have tried, given that LocalAI is a drop-in replacement for OpenAI, as I’ve mentioned. We know what
[temperature means](https://thenewstack.io/what-temperature-means-in-natural-language-processing-and-ai/), and I did a similar curl with a JSON payload when first looking at [AI wrappers](https://thenewstack.io/the-promise-of-riches-from-ai-wrappers/). Note the model name is not the same as the chat interface model.
I wasn’t able to get the chat client working because of errors (more on that later), but I did test the image recognition service using a similar curl example given to me in the Docker message:
|
1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
21
22
23
24
25
26
27
28
29
30
31
32
33
34
35
36
|
curl http://localhost:8080/v1/chat/completions -H "Content-Type: application/json"
-d '{
"model": "gpt-4-vision-preview",
"messages": [
{"role":"user",
"content": [
{ "type":"text",
"text": "What is in the image?"
},
{ "type": "image_url",
"image_url": {"url":"https://upload.wikimedia.org/wikipedia/commons/thumb/d/dd/Gfp-wisconsin-madison-the-nature-boardwalk.jpg/2560px-Gfp-wisconsin-madison-the-nature-boardwalk.jpg"}
}
],
"temperature": 0.9
}
]
}'
>>response
{
"created":1711995490,
"object":"chat.completion",
"id":"f78380ca-fbcd-455f-9834-ddffcefd6b03",
"model":"gpt-4-vision-preview",
"choices":
[
{"index":0,
"finish_reason":"stop",
"message":
{"role":"assistant",
"content":"The image features a wooden walkway or boardwalk that is surrounded by lush grass and green foliage, creating a serene and picturesque scene."
}
}
],
"usage":{"prompt_tokens":0,"completion_tokens":0,"total_tokens":0}}%
The container log confirmed that things were working:
|
1
|
2024-04-02 14:16:53 1:16PM INF Loading model 'bakllava.gguf' with backend llama-cpp
On my pre-Apple Silicon 2015 MacBook Pro, this took 12 mins.
“The image features a wooden walkway or boardwalk that is surrounded by lush grass and green foliage, creating a serene and picturesque scene.” Here is the test image being described:
The response text needed quite a high temperature (0.9) to produce the narrative quality (i.e. uses of “lush,” “serene,” “picturesque”). The strength of LLMs is their apparent ability to “intelligently” riff on a theme, using other sources. But the outcome is good.
To test both the model and the theory, let’s change that temperature (to 0.1) to confirm that we get a balder description. And we do: “The image features a wooden path or boardwalk that is surrounded by tall grass, flowers and weeds. The boardwalk appears to be in the middle of a large field or a prairie.”
Perfect, just the facts. This took 26 mins!
While it won’t make for good copy, I also tried the transcription service interface, and that worked rapidly. I downloaded a well-known somber speech:
I then sent the request to the model and got the lengthy reply back:
Within Docker, we can see what kicked into action:
|
1
|
2024-04-02 15:39:51 2:39PM INF Loading model 'ggml-whisper-base.bin' with backend whisper
The full text is sewn together from the segments at the end:
I don’t know enough about the algorithm to comment on the handful of unseparated words, but I am impressed by the use of speech marks to note a quote within the text. However, we are not here to consider the models themselves in detail.
LocalAI is not offering the user a platform as such, and this shows in the error surfacing which requires full developer rectitude to follow. Because there are more options (all in one, handling GPU, etc.) and people like me using old spec machines, the maintainers have their hands full keeping the quality of the experience high. There were instructions on building the model by hand if errors occurred — and that is a reasonable route to take if you expect to work with the project over time.
I’ve tried to keep part of this post as a shoulder-to-shoulder comparison between Ollama and LocalAI with my low spec MacBook, but as this field expands the user can expect a richer variety of options. Although a little rough right now, LocalAI gives a more direct route to the model and brings you a bit closer to the system. For those who need a one-off, simpler experience, Ollama is probably right for you. As you dig into putting models in your workflow, LocalAI will provide the more transparent option to work with — providing the error-handling is more effective.
[
YOUTUBE.COM/THENEWSTACK
Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.
](https://youtube.com/thenewstack?sub_confirmation=1)