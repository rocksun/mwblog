[Google](https://cloud.google.com/?utm_content=inline+mention) today published a new paper that aims to quantify the environmental impact of its Gemini models. The researchers found that the “median Gemini Apps text prompt” (more about this later) consumes 0.24 watt-hours (Wh) of energy and 0.26 milliliters of water — or the same energy used by watching nine seconds of TV and the equivalent of five drops of water.

A year ago, Google says, the energy usage was still 33x higher (and carbon emission 44x higher). It attributes the gains to its full-stack approach of optimizing everything from its [custom silicon](https://thenewstack.io/google-ai-infrastructure-pm-on-new-tpus-liquid-cooling-and-more/) to the models themselves.

Those energy and water usage numbers seem small at first, but it’s also worth noting that in its most recent [earnings call](https://abc.xyz/2025-q2-earnings-call/), Google said its Gemini mobile app, which is only one surface for using Gemini, now has 450 million monthly active users and that its data centers were now processing close to 1 quadrillion tokens per month.

Google did not provide any data on how this compares to the average search query, nor how much energy its audio, photo and video models consume. The company also did not define the size of the “median Gemini App text prompt” and the number of tokens it generates. It’s unclear why Google couldn’t simply put this data in terms of how much power and water usage per million tokens its data centers consume.

[![](https://cdn.thenewstack.io/media/2025/08/f00c085c-energy-components.png)](https://cdn.thenewstack.io/media/2025/08/f00c085c-energy-components.png)

Image credit: Google.

## Text Prompt Only

When asked a related question about the impact of the power usage of image and video models — or using Gemini’s deep research model — [Savannah Goodman](https://www.linkedin.com/in/savannah-goodman/), the head of Google’s Advanced Energy Labs, said that “the focus of this paper is Gemini Apps text prompts, and part of our reporting strategy is to continuously evaluate how we can improve transparency of these impacts.”

Google also argues that the models and their capabilities have changed a lot in the last year (including the addition of deep research, for example), meaning the median query has changed, too, as has the underlying hardware.

As for why Google wouldn’t provide comparative numbers for the median Gemini query and search query, Google’s [Partha Ranganathan](https://www.linkedin.com/in/partharanganathan/), who heads up the team designing its next-gen systems and data center, argued that this is “comparing apples and oranges.”

“The folks who come to the Gemini app have a very different modality of interaction than people who go to a Google Search,” he said. “And so I don’t think it’s very easy to compare that and given that we had a technical methodology — we tried to be very rigorous about the technical and science behind the methodology — and so it didn’t feel like we could do a proper scientific apples versus apples comparison for that. So we don’t have that number here.”

[![](https://cdn.thenewstack.io/media/2025/08/3e13d5a4-methodologies.png)](https://cdn.thenewstack.io/media/2025/08/3e13d5a4-methodologies.png)

Image credit: Google.

And indeed, it’s been a while since Google provided any data about how much energy a single search query consumes, but in 2009, it was 0.3 Wh. The company never updated this number, and it’s still widely cited, but chances are that if Google was able to make Gemini 33x more energy efficient over the last year, its Search team also made some gains in the last 16 years.

Still, it’s worth noting that Google’s numbers are significantly lower than most of the public estimates we’ve seen in the last two years, but not that far off from [Sam Altman](https://x.com/sama)‘s assertion earlier this year that the average ChatGPT query [consumed 0.34 Wh of energy](https://towardsdatascience.com/lets-analyze-openais-claims-about-chatgpt-energy-use/#:~:text=OpenAI%20CEO%20Sam%20Altman%20recently,about%200.000085%20gallons%20of%20water.) and 0.3 mL of water. It’s unclear how OpenAI arrived at this number and which parts of the system it includes. Google specifically excludes networking, end user devices and the power used to train its models and store data, for example.

While it would be nice to see a different kind of metric than “median Gemini Apps prompt,” in part because that makes it harder to compare text, audio, image and video prompts, as well as API usage and other modalities, it’s still good to see Google release this work and provide some concrete metric and its methodology.

[YOUTUBE.COM/THENEWSTACK

Tech moves fast, don't miss an episode. Subscribe to our YouTube
channel to stream all our podcasts, interviews, demos, and more.

SUBSCRIBE](https://youtube.com/thenewstack?sub_confirmation=1)

Group
Created with Sketch.

[![](https://thenewstack.io/wp-content/uploads/2025/03/15a7eb12-cropped-4e88ac40-frederic-profile-2-600x600.jpg)

Before joining The New Stack as its senior editor for AI, Frederic was the enterprise editor at TechCrunch, where he covered everything from the rise of the cloud and the earliest days of Kubernetes to the advent of quantum computing....

Read more from Frederic Lardinois](https://thenewstack.io/author/frederic-lardinois/)