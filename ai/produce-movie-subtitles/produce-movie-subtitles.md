
<!--
title: 使用AI翻译电影字幕
cover: ./cover.png
-->

本文介绍了如何使用 Python 调用 ffmpeg 和 Gemini 实现电影字幕的翻译。效果可以看“效果展示”部分。

## 背景

不久前离开上家公司了，又恢复了自由身，之前的几个工作都几乎是无缝切换，少了一些思考，这一次决定先好好想想，可以放松的搞一点自己觉得好玩的东西。买了个 NAS，发现工作中的 IT 技能终于用到了生活中，其中首先是关于电影的中文字幕。

拿到 NAS 的第一步就是开始疯狂的下载 4K 电影，这些电影都自带字幕，不过有些不带中文字幕，或者翻译的不好。再加上我买的 NAS 软件功能不全，中文字幕下载比较麻烦，所以我希望有一个自动化的方案。经过评估，我觉得可以利用现在的 ChatGPT 和 Gemini 之类的 AI 翻译英文字幕，应该会有不错的效果。

## 使用 Poetry 管理项目

这几年没怎么搞过 Python 项目，但是看到有一些项目用到了 [poetry](https://python-poetry.org/) ，所以决定这个项目用起来。试用感觉很不错，远超之前用过的 pipenv 。

我的 pyproject.toml 文件内容如下：

```ini
[tool.poetry]
name = "upbox"
version = "0.1.0"
description = ""
authors = ["rocksun <daijun@gmail.com>"]
readme = "README.md"

[tool.poetry.dependencies]
python = "^3.10"
ffmpeg-python = "^0.2.0"
llama-index = "^0.10.25"
llama-index-llms-gemini = "^0.1.6"
pysubs2 = "^1.6.1"
# yt-dlp = "^2024.4.9"
# typer = "^0.12.3"
# faster-whisper = "^1.0.1"


[build-system]
requires = ["poetry-core"]
build-backend = "poetry.core.masonry.api"

```

关于 poetry 的使用我这里就不多说了，大家自行学习。这里引用了 ffmpeg 的包装库（需要路径里有 ffmpeg 命令）；然后就是 llama-index 和 对应的 Gemini 库，其实用不用 llama-index 区别不大，本文并没有使用太多 llama-index 的功能；最后是字幕处理库 pysubs2，曾经考虑是否直接解析字幕，后来发现用 pysubs2 还是能节省不少时间。

## 英文字幕提取

通过 ffmpeg 提取视频中内嵌的字幕很容易，执行以下命令即可：

```bash
ffmpeg -i my_file.mkv outfile.vtt
```

但实际上一个视频里会有多个字幕，这样并不准确，所以还是要确认下。我还是考虑用一个 ffmpeg 的库，也就是 [ffmpeg-python](https://github.com/kkroening/ffmpeg-python)，用这个库提取英文字幕的代码如下：

```python
def _guess_eng_subtitle_index(video_path):
    probe = ffmpeg.probe(video_path)
    streams = probe['streams']
    for index, stream in enumerate(streams):
        if stream.get('codec_type') == 'subtitle' and stream.get('tags', {}).get('language') == 'eng':
            return index
    for index, stream in enumerate(streams):
        if stream['codec_type'] == 'subtitle' and stream.get('tags', {}).get('title', "").lower().find("english")!=-1 :
            return index
    return -1

def _extract_subtitle_by_index(video_path, output_path, index):
    return ffmpeg.input(video_path).output(output_path, map='0:'+str(index)).run()

def extract_subtitle(video_path, en_subtitle_path):
    # get the streams from video with ffprobe
    index = _guess_eng_subtitle_index(video_path)
    if index == -1:
        return -1
    
    return _extract_subtitle_by_index(video_path, en_subtitle_path, index)
```

增加了 `_guess_eng_subtitle_index` 方法来确定英文字幕的 index，这是因为虽然大多数视频都的字幕 tags 还是比较规范的，但是也确实有一些视频的字幕根本没有 tags，所以只能猜，我估计在实践中还有其他情况，只能根据实际情况应对。

## 英文字幕处理

一开始我以为就直接将字幕抛给 Gemini ，然后保存结果就行，但实际上并不行，有几个问题：

1. 许多英文字幕中有许多标签，翻译时会影响效果
2. 一个字幕太大，全部抛给 Gemini 处理不了，而且上下文太长其实也容易出问题。
3. 字幕中的时间戳太长，让 prompt 变得太长。

为此，我只好增加了一个字幕类 UpSubs 用来处理上面的问题：

```python
class UpSubs:
    def __init__(self, subs_path):
        self.subs = pysubs2.load(subs_path)

    def get_subtitle_text(self):
        text = ""
        for sub in self.subs:
            text += sub.text + "\n\n"
        return text

    def get_subtitle_text_with_index(self):
        text = ""
        for i, sub in enumerate(self.subs):
            text += "chunk-"+str(i) + ":\n" + sub.text.replace("\\N", " ") + "\n\n"
        return text
    
    def save(self, output_path):
        self.subs.save(output_path)

    def clean(self):
        indexes = []
        for i, sub in enumerate(self.subs):
            # remove xml tag and line change in sub text
            sub.text = re.sub(r"<[^>]+>", "", sub.text)
            sub.text = sub.text.replace("\\N", " ")

    def fill(self, text):
        text = text.strip()
        pattern = r"\n\s*\n"
        paragraphs = re.split(pattern, text)
        for para in paragraphs:
            try:
                firtline = para.split("\n")[0]
                countstr = firtline[6:len(firtline)-1]
                # print(countstr)
                index = int(countstr)
                p = "\n".join(para.split("\n")[1:])
                self.subs[index].text = p
            except Exception as e:
                print(f"Error merge paragraph : \n {para} \n with exception: \n {e}")
                raise(e)
    
    def merge_dual(self, subspath):
        second_subs = pysubs2.load(subspath)
        merged_subs = SSAFile()
        if len(self.subs.events) == len(second_subs.events):            
            for i, first_event in enumerate(self.subs.events):
                second_event = second_subs[i]
                if first_event.text == second_event.text:
                    merged_event = SSAEvent(first_event.start, first_event.end, first_event.text)
                else:
                    merged_event = SSAEvent(first_event.start, first_event.end, first_event.text + '\n' + second_event.text)
                merged_subs.append(merged_event)
            return merged_subs
        
        return None
```

`clean` 方法可以简单的清理字幕；save 方法可以用来保存字幕；`merge_dual` 用来合并双语字幕。这些都比较简单，后面重点说说字幕文本的处理。

原始 srt 文件形式如下：

```s
12
00:02:30,776 --> 00:02:34,780
Not even the great Dragon Warrior.

13
00:02:43,830 --> 00:02:45,749
Oh, where is Po?

14
00:02:45,749 --> 00:02:48,502
He was supposed to be here hours ago.
```

经过 `get_subtitle_text_with_index` 方法会变成：

```s
chunk-12
Not even the great Dragon Warrior.

chunk-13
Oh, where is Po?

chunk-14
He was supposed to be here hours ago.
```

这样做是为了减少文字数量，减少 chunk 数量。而且，依然能跟踪每一段字幕的编号，通过 `fill` 方法，我们可以从翻译后的文本还原回字幕。

## 调用 Gemini 

调用 Gemini 有几个问题：

* 需要访问密钥
* 国内访问需要走合适的代理
* 要有一定的容错能力
* 还有要规避 Gemini 的安全机制

所以，针对这些问题，专门写了个 `complete` 方法：

```py
def complete(prompt, max_tokens=32760):
    prompt = prompt.strip()
    if not prompt:
        return ""
    
    safety_settings = [
        {
            "category": "HARM_CATEGORY_HARASSMENT",
            "threshold": "BLOCK_NONE"
        },
        {
            "category": "HARM_CATEGORY_HATE_SPEECH",
            "threshold": "BLOCK_NONE"
        },
        {
            "category": "HARM_CATEGORY_SEXUALLY_EXPLICIT",
            "threshold": "BLOCK_NONE"
        },
        {
            "category": "HARM_CATEGORY_DANGEROUS_CONTENT",
            "threshold": "BLOCK_NONE"
        },
    ]

    retries = 3
    for _ in range(retries):
        try:
            return Gemini(max_tokens=max_tokens, safety_settings=safety_settings, temperature = 0.01).complete(prompt).text
        except Exception as e:
            print(f"Error completing prompt: {prompt} \n with error: \n ")
            traceback.print_exc()
    return ""
```

`safety_settings` 很重要，电影字幕中经常出现一些特别敏感的语言，必须告知 Gemini 尽量多容忍。虽然据文档说只有收费账号才能 `BLOCK_NONE` ，但好像对于我翻译电影上述配置没有遇到太多问题，偶尔会遇到一些，但是重试都会消失。

然后是增加了 3 次重试，调用会偶尔有失败，重试能解决一些问题。

最后，可以通过 [Google AI Studio](https://aistudio.google.com/app/apikey) 获取 API Key。然后在项目增加一个 .env 文件：

```env
http_proxy=http://192.168.0.107:7890
https_proxy=http://192.168.0.107:7890
GOOGLE_API_KEY=[your-api-key]
```

程序就可以读取到 API Key 和代理的设置。

## 调用流程

先看一下最外层 `tran_subtitles` 方法

```py
def tran_subtitles(fixed_subtitle, zh_subtitle=None, cncf = False, chunk_size=3000):
    subtitle_base = os.path.splitext(fixed_subtitle)[0]
    video_base = os.path.splitext(subtitle_base)[0]
    if zh_subtitle is None:
        zh_subtitle = video_base + ".zh-fixed.vtt"
    if os.path.exists(zh_subtitle):
        print(f"zh subtitle {zh_subtitle} already translated, skip to translate.")
        return 1

    prompt_tpl = MOVIE_TRAN_PROMPT_TPL
    opts = { }

    srtp = UpSubs(fixed_subtitle)
    text = srtp.get_subtitle_text_with_index()

    process_text(srtp, text, prompt_tpl, opts, chunk_size = chunk_size)
    srtp.save(zh_subtitle)

    return zh_subtitle
```

这个逻辑比较简单，读取英文字幕，使用 `get_subtitle_text_with_index` 方法转化为待翻译的文本，然后执行 process_text 方法，完成翻译。提示词模板 prompt_tpl 直接引用了 MOVIE_TRAN_PROMPT_TPL，其中内容为：

```py
MOVIE_TRAN_PROMPT_TPL = """你是个专业电影字幕翻译，你需要将一份英文字幕翻译成中文。
[需要翻译的英文字幕]:

{content}

# [中文字幕]:"""
```

可以看到这个提示还是相当简单的。

然后可以关注下 `process_text` 方法：

```py
def process_text(subs, text, prompt_tpl, opts, chunk_size=2500):
    # ret = ""
    chunks = _split_subtitles(text, chunk_size)
    for(i, chunk) in enumerate(chunks):
        print("process chunk ({}/{})".format(i+1,len(chunks)))
        # if i==4:
        #     break
        # format string with all the field in a dict 
        opts["content"] = chunk
        prompt = prompt_tpl.format(**opts)

        print(prompt)
        out = complete(prompt, max_tokens=32760)
        subs.fill(out)
        print(out)
```

通过 `_split_subtitles` 方法拆分字幕文本为多个 chunk ，然后分别扔给前面说的 `complete` 方法。

## 效果展示

一开始对字幕的翻译并没有太多的期待，不过最终的效果还是出乎意料的好，以功夫熊猫4为例，这是部分翻译的对比：

英文字幕：

```
10
00:02:22,184 --> 00:02:27,606
Let it be known from the highest mountain
to the lowest valley that Tai Lung lives,

11
00:02:27,606 --> 00:02:30,776
and no one will stand in his way.

12
00:02:30,776 --> 00:02:34,780
Not even the great Dragon Warrior.

13
00:02:43,830 --> 00:02:45,749
Oh, where is Po?
```

中文字幕：

```
10
00:02:22,184 --> 00:02:27,606
让最高的山峰和最低的山谷都知道，泰隆还活着，

11
00:02:27,606 --> 00:02:30,776
没人能阻挡他。

12
00:02:30,776 --> 00:02:34,780
即使是伟大的神龙大侠也不行。

13
00:02:43,830 --> 00:02:45,749
哦，阿宝在哪儿？
```

看到结果出奇的好，我的 prmopt 里也没有提供更多的上下文，Gemini 却给出了地道的翻译。

## 总结

针对电影，上述代码运行的还比较稳定。但是当面对一些本身就不太好的字幕，翻译的结果也不会太好，而且出现了许多异常，为此还需要做许多改进。最近我的视频号（云云众生s）分享了一些技术的视频，就是用改进的代码实现的，后面也会跟大家分享。

感觉，能用技术改变生活挺好，希望有更多的改进机会，欢迎大家多多关注交流。

