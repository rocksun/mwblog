
<!--
title: 使用 Python 掌握计算机视觉基础知识
cover: https://cdn.thenewstack.io/media/2024/08/4129f28e-computervision.jpg
-->

计算机视觉为创新和解决问题提供了机会，使我们能够创建能够解释视觉信息的应用程序。

> 译自 [Mastering the Fundamentals of Computer Vision With Python](https://thenewstack.io/mastering-the-fundamentals-of-computer-vision-with-python/)，作者 Zziwa Raymond Ian。

计算机视觉是计算机科学的一个领域，它 [使用 AI](https://thenewstack.io/ai/) 使计算机能够理解和识别图像和视频中的人和 [物体](https://thenewstack.io/the-power-and-ethical-dilemma-of-ai-image-generation-models/)。计算机视觉可以通过分析图像并确定看起来像人的东西来识别照片中的人。让我们一起完成一个简单但详细的项目，我们将向计算机提供我的照片，看看它是否能认出我。但首先，让我们了解一些需要理解的重要术语。

**边界框**：计算机在图像或视频中识别出的物体周围绘制的矩形边框。为了识别照片中的人，计算机将在检测到的每个人周围绘制一个边界框。我们将在后面看到它的实际应用。

**交并比 (IoU)**：此指标衡量预测的边界框与实际物体（称为真实值）的匹配程度。真实值指的是我们想要识别的真实物体。IoU 帮助我们确定计算机的预测与这个真实物体有多接近。

IoU 值介于 0 到 1 之间。如果预测的边界框与真实值完全重叠，则 IoU 为 1。相反，如果没有任何重叠，则 IoU 为 0。对于部分重叠，IoU 使用以下公式计算：IoU = 预测边界框和真实值的交集面积 / 并集面积。

还有许多其他对计算机视觉至关重要的术语，但你可以 [在这里熟悉它们](https://encord.com/blog/computer-vision-terms/)。你也可以 [在这里](https://github.com/RaymondZziwa/cv-python) 找到此项目的完整代码。

## 先决条件

在开始之前，请确保你拥有以下内容：

1. **已安装 Python**：本文使用 Python 3.12.4。你可以通过运行以下命令检查你的 Python 版本：
  ```bash
  python --version
  ```
  如果遇到错误，请确保 Python 正确安装。你可以从 [官方网站](https://www.python.org/downloads/) 下载 Python。

2. **文本编辑器**：本教程使用 Visual Studio Code (VS Code) 作为文本编辑器。你可以 [在这里](https://code.visualstudio.com/) 下载 VS Code。但是，你可以随意使用你选择的任何文本编辑器。

在深入我们的项目之前，必须设置一个干净的工作环境。以下是逐步操作方法：

1. **创建项目文件夹**：首先，选择项目文件夹的位置。在本教程中，我们将在桌面上创建它。

在 macOS 上：

* 导航到你的桌面。
* 创建一个名为“facial-recognition”的新文件夹。
* 通过单击该文件夹并按 `Ctrl + Cmd + C` 在该文件夹中打开终端。

在 Windows 上：

* 导航到你的桌面。
* 创建一个名为“facial-recognition”的新文件夹。
* 右键单击该文件夹，然后选择“在终端中打开”或“在此处打开 PowerShell 窗口”。

2. **创建并激活虚拟环境**：这有助于将项目依赖项与全局 Python 安装隔离开来。

* 创建虚拟环境：
    
在你的终端中，运行以下命令在项目文件夹中创建一个名为 `venv` 的虚拟环境：

```bash
python -m venv venv
```

* 激活虚拟环境：

要激活虚拟环境，请根据你的操作系统使用以下命令：

```bash
source venv/bin/activate //activate virtual environment on mac

.\venv\Scripts\activate //activate virtual environment on windows
```

激活虚拟环境后，你的终端将显示如下。

![图 1：激活的虚拟环境的插图](https://cdn.thenewstack.io/media/2024/08/53a317f6-image1.png)

*图 1：激活的虚拟环境的插图*

注意：如上图所示，我使用 `python3` 创建了一个虚拟环境。这是必要的，因为我的计算机上有两个不同的 Python 安装，因此我需要指定我正在使用的版本。

设置完成后，我们现在可以创建我们的 `main.py` 文件，我们将在其中逐步编写代码。此外，我们将把图像放在同一个目录中的名为“images”的文件夹中。这张图像将在后面用于从网络摄像头馈送中识别我。

我们现在将安装一个名为 OpenCV 的库。这是一个重要的库，因为它大大减少了我们需要编写的代码量。OpenCV 提供了许多预构建的函数，我们可以使用它们，而无需重新编写底层逻辑。运行以下命令安装 OpenCV：

```bash
pip install opencv-python
#import open cv
import cv2
import time
 
#here, we load the pre-built Haar Cascade model
face_classifier = cv2.CascadeClassifier(
   cv2.data.haarcascades + "haarcascade_frontalface_default.xml"
)
 
def detect_faces():
   # Access the webcam
   cap = cv2.VideoCapture(0)
   if not cap.isOpened():
       print("Error: Could not open webcam.")
       return
  
   # Allow the webcam some time to initialize
   time.sleep(2)
  
   while True:
       # Read the frame from the webcam
       ret, frame = cap.read()
      
       # Check if the frame was read successfully
       if not ret:
           print("Error: Failed to capture image from webcam")
           break
      
       # Check if the frame is empty
       if frame is None:
           print("Error: Received empty frame from webcam")
           continue
      
       try:
           # Convert the frame to grayscale
           gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
          
           # Detect faces in the grayscale frame
           faces = face_classifier.detectMultiScale(gray, 1.1, 5)
          
           # Draw rectangles around the faces
           for (x, y, w, h) in faces:
               cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)
          
           # Display the frame with face detections
           cv2.imshow("Face Detection", frame)
 
       except cv2.error as e:
           print(f"OpenCV Error: {e}")
           break
 
       # Exit loop if 'q' key is pressed
       if cv2.waitKey(1) & 0xFF == ord('q'):
           break
  
   # Release the webcam and close all OpenCV windows
   cap.release()
   cv2.destroyAllWindows()
 
# Call the function to start the webcam feed
detect_faces()
```

在你的项目文件夹中，创建一个名为 `main.py` 的新文件。

在 `main.py` 文件中，导入以下库：

```python
import cv2
```

**加载图像**

使用 `cv2.imread()` 函数加载图像。确保图像位于名为“images”的文件夹中，该文件夹与 `main.py` 文件位于同一目录中。

```python
image = cv2.imread("images/your_image.jpg")
```

**显示图像**

使用 `cv2.imshow()` 函数显示图像。

```python
cv2.imshow("Image", image)
```

**等待用户输入**

使用 `cv2.waitKey()` 函数等待用户按下任何键。

```python
cv2.waitKey(0)
```

**关闭窗口**

使用 `cv2.destroyAllWindows()` 函数关闭所有打开的窗口。

```python
cv2.destroyAllWindows()
```

**完整代码**

```python
import cv2

# 加载图像
image = cv2.imread("images/your_image.jpg")

# 显示图像
cv2.imshow("Image", image)

# 等待用户输入
cv2.waitKey(0)

# 关闭窗口
cv2.destroyAllWindows()
```

**运行代码**

在你的终端中，运行以下命令运行代码：

```bash
python main.py
```

这将显示你加载的图像。

**下一步**

现在你已经成功地加载并显示了图像，你可以继续学习更多关于计算机视觉的知识，例如：

* **人脸检测**：使用 OpenCV 的 `cv2.CascadeClassifier()` 函数检测图像中的人脸。
* **物体识别**：使用预先训练的模型识别图像中的物体。
* **图像分割**：将图像分割成不同的区域。

**结论**

在本教程中，你学习了如何使用 Python 和 OpenCV 加载和显示图像。这只是计算机视觉的入门，还有很多东西需要学习。通过继续学习和实践，你可以使用计算机视觉来构建各种有趣的应用程序。
```python
pip install opencv-python
# 导入 open cv
import cv2
import time
# 这里，我们加载预构建的 Haar 级联模型
face_classifier = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")

def detect_faces():
    # 访问网络摄像头
    cap = cv2.VideoCapture(0)
    if not cap.isOpened():
        print("错误：无法打开网络摄像头。")
        return
    # 允许网络摄像头初始化一段时间
    time.sleep(2)
    while True:
        # 从网络摄像头读取帧
        ret, frame = cap.read()
        # 检查是否成功读取帧
        if not ret:
            print("错误：无法从网络摄像头捕获图像")
            break
        # 检查帧是否为空
        if frame is None:
            print("错误：从网络摄像头接收到的帧为空")
            continue
        try:
            # 将帧转换为灰度
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            # 在灰度帧中检测人脸
            faces = face_classifier.detectMultiScale(gray, 1.1, 5)
            # 在人脸周围绘制矩形
            for (x, y, w, h) in faces:
                cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)
            # 显示带有面部检测的帧
            cv2.imshow("人脸检测", frame)
        except cv2.error as e:
            print(f"OpenCV 错误：{e}")
            break
        # 如果按下“q”键，退出循环
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    # 释放网络摄像头并关闭所有 OpenCV 窗口
    cap.release()
    cv2.destroyAllWindows()

# 调用函数以启动网络摄像头馈送
detect_faces()
```

将上面的代码复制粘贴到您的 `main.py` 文件中。现在，让我们分解代码以了解正在发生的事情。

在第 1 行，我们导入之前安装的 OpenCV 库。这使我们能够访问其预构建的函数和分类器。我们还导入 `time` 实用程序来处理程序中的延迟。

接下来，我们加载一个名为 `haarcascade_frontalface_default.xml` 的预构建 Haar 级联分类器。此分类器专门 [设计用于在视觉输入中检测正面人脸](https://thenewstack.io/how-next-js-12-connects-to-low-code-and-visual-design-tools/)。

加载模型后，我们定义一个名为 `detect_faces` 的函数。在此函数中，我们首先访问网络摄像头馈送并使用 `cap = cv2.VideoCapture(0)` 将其分配给名为 `cap` 的变量。然后，我们使用 `if not cap.isOpened():` 检查网络摄像头流是否打开。如果未打开，我们将打印错误消息并停止执行。

为了确保网络摄像头正确初始化，我们在进入 `while True` 循环之前使用 `time.sleep(2)` 添加延迟。在此循环中，只要 `cap` 打开，我们就会不断从网络摄像头馈送中读取帧并执行一些检查。如果成功读取帧 (`if ret:`)，我们将继续。如果帧未打开 (`if frame is None:`)，我们将打印错误消息；否则，我们将继续执行。

进入 `try` 块后，我们的第一步是将每个帧转换为灰度。随后，使用之前定义的分类器，我们检测灰度图像中存在的所有人脸。在此之后，`for` 循环遍历每个检测到的人脸，在其周围绘制一个蓝色边界框。然后显示这些带有面部检测的注释帧。如果在此过程中发生错误，它将被打印出来以供查看。该循环旨在在按下“q”键时退出。最后，我们在调用 `detect_faces()` 以再次启动面部检测过程之前，释放网络摄像头资源并关闭所有活动的 OpenCV 窗口。

解释完代码后，以下是您可以预期的结果：

![图 2：我的脸被检测到的插图](https://cdn.thenewstack.io/media/2024/08/67ab42d8-image4-1024x640.png)

*图 2：我的脸被检测到的插图*

现在成功实现了面部检测，下一步是将检测到的人脸与之前存储在“images”文件夹中的图像进行比较。如果匹配，我的姓名将与边界框一起显示；否则，将不会显示任何其他信息。

为了实现这一点，我们需要对代码进行一些修改。首先，安装一个名为 `face_recognition` 的库及其所需的模型。接下来，将参考图像的路径分配给一个变量并加载图像。然后，我们将对参考人脸进行编码。在 `for` 循环中，我们将调整人脸区域的大小以进行人脸识别，虽然可选，但建议这样做。调整大小后，我们将对检测到的人脸进行编码。为了处理错误，我们将包括一个检查以确保 `encoded_face` 数组至少包含一个项目。如果数组不为空，我们将将其与参考图像人脸编码进行比较。如果找到匹配项，我们将显示“Raymond”在边界框旁边；否则，将不会打印任何内容。

```python
pip install face_recognition
pip install git+https://github.com/ageitgey/face_recognition_models 
pip install distribute //to solve the bug of face_recognition_models not being recognized as installed
import cv2
import os
import face_recognition
import time
 
# Path to the reference image in the images folder
reference_image_path = 'images/profile-headshot.jpg'
 
# Load the reference image
reference_image = face_recognition.load_image_file(reference_image_path)
reference_encoding = face_recognition.face_encodings(reference_image)[0]
 
# Load the pre-built Haar Cascade model for face detection
face_classifier = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
 
def accessWebcam():
   # Access the webcam
   cap = cv2.VideoCapture(0)
   if not cap.isOpened():
       print("Error: Could not open webcam.")
       return
  
   # Allow the webcam some time to initialize
   time.sleep(2)
  
   while True:
       # Read the frame from the webcam
       ret, frame = cap.read()
      
       # Check if the frame was read successfully
       if not ret:
           print("Error: Failed to capture image from webcam")
           break
      
       # Convert the frame to grayscale for face detection
       gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
      
       # Detect faces in the grayscale frame
       faces = face_classifier.detectMultiScale(gray, 1.1, 5)
      
       # Process each detected face
       for (x, y, w, h) in faces:
           # Extract the face region from the frame
           face_region = frame[y:y+h, x:x+w]
          
           # Resize the face region for face recognition (optional but recommended)
           face_region_resized = cv2.resize(face_region, (128, 128))
          
           # Encode the detected face
           face_encoding = face_recognition.face_encodings(face_region_resized)
          
           # Compare the detected face encoding with the reference face encoding
           if len(face_encoding) > 0:
               match = face_recognition.compare_faces([reference_encoding], face_encoding[0], tolerance=0.5)
              
               # If match is found, display the name on the bounding box
               if match[0]:
                   cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
                   cv2.putText(frame, "Raymond", (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (36,255,12), 2)
               else:
                   cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)
           else:
               cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)
      
       # Display the frame with face detections
       cv2.imshow("Face Detection", frame)
 
       # Break the loop on 'q' key press
       if cv2.waitKey(1) & 0xFF == ord('q'):
           break
  
   # Release the webcam and close all OpenCV windows
   cap.release()
   cv2.destroyAllWindows()
 
# Call the function to start the webcam feed
accessWebcam()
```

如果你遇到了运行时错误 RuntimeError: 不受支持的图像类型，必须是 8 位灰度或 RGB 图像，可以通过将 NumPy 降级到 1.26.4 版本来解决。此问题与 NumPy 2.0 有关。要降级，只需运行以下命令：

```
pip install numpy==1.26.4
```

接下来，让我演示我们的工作成果。您会注意到，当识别出我的脸部时，边框变为绿色，并且我的名字会显示在边框旁边。如果无法识别出人脸，则边框保持为蓝色。此外，我通过在我的手机上显示另一张面孔来测试系统。虽然模型检测到了该面孔，但它并没有识别出该面孔，因此该面孔的边框始终为蓝色，而我的面孔由于模型已熟悉而被突出显示为绿色边框。

![](https://cdn.thenewstack.io/media/2024/08/f3b2addd-image5-1024x640.png)

*图 3：展示如何检测和识别我的脸部的插图*

![](https://cdn.thenewstack.io/media/2024/08/7dfa9115-image3-1024x640.png)

*图 4：由于头部倾斜而导致面部被遮挡及错认的示例*

![](https://cdn.thenewstack.io/media/2024/08/b4801bbe-image2-1024x640.png)

*图片 5：演示面部识别（仅识别我的脸）*

计算机视觉为创新和问题解决提供了丰富的机遇，使我们能够[创建能够以有意义的方式解释和响应视觉信息的应用程序](https://thenewstack.io/apache-hop-harnesses-metadata-to-create-visual-data-pipelines/)。从通过面部识别增强安全性到启用自主系统，可能性既广泛又令人兴奋。随着技术的不断进步，计算机视觉在各个领域的融合无疑将产生突破性发展和新的应用。我鼓励您进一步探索并尝试这些技术，因为它们有望改变我们与周围世界互动的方式。

了解您如何获取熟练的 python 开发人员来帮助推动您的数字化转型，请参阅“[如何聘请 Python 开发人员：寻找合适人选指南](https://www.andela.com/blog-posts/how-to-hire-a-python-developer-a-guide-to-finding-the-right-fit/?utm_medium=contentmarketing&utm_source=blog&utm_campaign=brand-global-the-new-stack-computer-vision&utm_content=hire-python-developers)。”



