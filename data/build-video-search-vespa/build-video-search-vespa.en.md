Video is everywhere in today’s world, and more video content is being pumped out than ever before. It is estimated that more than 500 hours of footage are uploaded to YouTube every minute.

Businesses and organizations are starting to see the value in being able to search the rich data available in video content. From detecting products for e-commerce discovery to tapping into the large volumes of high-quality information found in conference recordings and university lectures, or searching through site-surveying footage, Video Management Systems are becoming valuable assets for surfacing information locked in video files. Instead of having to ignore video footage or look for it separately, wouldn’t it be nice if it could be retrieved alongside your other relevant documents, whilst pinpointing exactly where in the video the information lives?

> “Instead of having to ignore video footage or look for it separately, wouldn’t it be nice if it could be retrieved alongside your other relevant documents, whilst pinpointing exactly where in the video the information lives?”

Extracting information from video opens new opportunities. Universities can provide students with fast search through lectures, maybe the lecturer from six years ago was really good at explaining the Laplace transform or options pricing? Video streaming providers might be interested in selling partnerships with E-commerce platforms for detecting similar items to what is shown in the films on the platform: *that watch James Bond was wearing looked very nice, where can I find that*? Insurance companies might need to go through a bunch of security or dashcam footage to see what really happened at that red light. Or maybe we are curious how many times a certain bird was spotted on a wildlife camera monitoring population health?

## The challenge

So why is video still largely unsearchable? One issue is that video is an inherently difficult data type to process. Firstly, the visual data in a video is not so straightforward to analyze. Most video formats rely on key frames (or I-frames, for Intra-coded frames) and predicted frames (P-frames). I-frames are complete images and thus easy to analyze, but most frames are P-frames, which cleverly encode only the difference between the previous and next frames.

These P-frames exploit the fact that there is often little difference in visual information from one frame to the next, which is why a 10-minute 1080p@30fps video can be 150 MB instead of 11.2 GB. However, the P-frames are often not useful in isolation and need processing before meaningful content can be extracted.

Another issue is that audio data and visual data are handled in fundamentally different ways. Video formats are not data types in which video and audio exist as a unified representation; rather, they are two separate tracks, aligned and synced.

This means that, at some level, processing the full video modality requires separate pipelines for audio and video. To preserve information from the video file, the separate pipelines must include logic to ensure that the audio stays aligned with the video, which is not necessarily trivial.

Because of the complex, multimodal nature of video, there is no single right way to process it. Some videos focus on the visual element (e.g., stock footage), while others focus more on the audio aspect (e.g., podcast or lecture recordings). The way you handle the video thus depends on what the purpose of your video retrieval is and the type of content you have.

Here, I will focus on the visual elements of videos to show how visual content can be searched within them.

## The tech stack

There are two key elements needed to enable search within and through videos.

1. Video preprocessing
2. A retrieval engine that can accommodate and index the processed data

## Preprocessing

This preprocessing pipeline is designed to support the use case of finding visual moments in videos, akin to finding stock videos. In practice, this means we will treat the video as a series of images. There are several ways to go about this, and also several layers of optimization that need to be done to make the approach practical.

For searching through the video, I recommend a hybrid-search approach that uses image embeddings and generated text descriptions. A naive implementation would be to extract all the frames from a video, embed them (the CLIP open-source embedding model is still a good way to get started, though it is getting old), generate a description with an LLM, and search through the results.

This would, however, be enormously expensive to process and query; for each second of 30fps footage, we would need to generate 30 embeddings and descriptions. A slightly more practical method would be to take snapshots at predetermined intervals. Although we lose accuracy, this greatly reduces the amount of processing needed; even at one snapshot per second, we have reduced it 30-fold.

However, a better approach is to detect significant scene changes in the video and take snapshots only when the visual content has meaningfully changed.

Some videos might have scenes that span multiple seconds, if not minutes or even hours, without a notable change in the visual content. It would be a waste to store 100s of frames in a row where no meaningful information is to be found beyond the first frame in the sequence. Luckily, this kind of analysis is well-suited to image embeddings. We can first take snapshots at a set interval where information loss is minimal (e.g., 3 per second), and then prune the snapshots based on their vector similarity to the previous snapshot.

By setting a reasonable threshold for similarity between snapshots, we get an effective gauge for when the current visual content is sufficiently different from the last snapshot to warrant adding it as a new scene. We can even add more specific rules, such as requiring a snapshot to be visually distinct from the last 5 snapshots, to avoid quick back-and-forth cuts in a scene being flagged as separate scenes.

This way, we can greatly minimize the data needed to pinpoint exact visual moments in a video. For example, with “Bruce Li the Invincible”, a 90min film from the *Bruceploitation* genre (it is worth reading about!), I was able to condense it to 1,167 separate visual snapshots, or an average of one snapshot every 4.6 seconds.

To enrich the context for retrieval, we can also create textual image descriptions by feeding our selected snapshots to a VLM. This is a computationally expensive operation that requires either good hardware or an API, but since we have greatly optimized the amount of visual content that needs to be processed, this operation becomes much less time-consuming and expensive.

## Retrieval engine

We now have a working process for preparing videos for search, but that only solves half the problem. What remains is the infrastructure to serve this data.

To enable search over our videos, we need to store the list of embeddings for each video, along with its textual descriptions and metadata.

For this, I would recommend using a retrieval platform such as the open-source Vespa [search platform](https://thenewstack.io/why-ai-search-platforms-are-gaining-attention/). It allows us to store multiple vectors per video and the corresponding textual descriptions alongside them. This means we can treat each snapshot as a separate scorable moment while keeping the video as a single entity in the data layer.

Having native multivector and [tensor capabilities](https://thenewstack.io/beyond-vector-search-the-move-to-tensor-based-retrieval/) greatly simplifies the infrastructure required to retrieve data across multiple signals and modalities. Instead of several different systems and management logic for gluing them together, Vespa provides an all-in-one solution for feeding, searching, and multi-stage ranking. Scalability is another common pain point for glued-together architectures, which a unified architecture such as this helps with a lot.

But perhaps the most exciting thing Vespa lets us do is easily rank our video snapshots based on all available information.

> “The ranking expressions give us limitless flexibility for tuning what results we want to emphasize.”

We don’t need to rely on just [vector search](https://thenewstack.io/why-developers-need-vector-search/) on our embeddings or just keyword search from the descriptions; we can combine both signals in a single ranking expression. The ranking expressions give us limitless flexibility for tuning what results we want to emphasize. Maybe we want to rely more on the embeddings, or perhaps the textual descriptions should be weighted more heavily? It is also easy to include metadata in the ranking. Should we aim for shorter videos to rank higher? Adding such functionality would be a simple matter of including the video length in the ranking function.

## Further improvements

This article demonstrates one way to implement video search, but there are many layers we could add to change and improve its use. Some embedding models and VLMs now natively understand video, and some even understand the audio content, which would give us a richer context in the embeddings. It would also be possible to transcribe the audio from the video and include the BM-25 score for the transcript in our ranking expression.

As long as we transcribe the audio with timestamps, the audio information can be aligned with the image embeddings and descriptions, ensuring that the information is synchronized and kept together.

Since we are using a flexible search platform, adding a new model or signal to the retrieval pipeline is trivial. It is easy to update it if we want to add better embedding models, and changing the ranking expression can be done in a couple of lines of code. For multimodal retrieval systems in a quickly evolving scene, this flexibility is a great benefit!

Check out the example application of [Vespa’s Video Search Demo](https://video-search.vespa-demos.ai/), which showcases how Vespa can quickly search through multimodal data.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://cdn.thenewstack.io/media/2025/07/d6ac6c60-cropped-9cae470c-kai-borgen.jpeg)

Kai Borgen is a technical product engineer working at Vespa AI. With a background in both business and engineering, his focus lies in bringing technical expertise to business functions, ensuring that organizations stay aligned, effective and ahead of the curve.

Read more from Kai Borgen](https://thenewstack.io/author/kai-borgen/)