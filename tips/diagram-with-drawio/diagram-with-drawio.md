<!-- 
# 使用 draw.io 来画 CNCF 架构图
https://yylives.cc/wp-content/uploads/2023/11/cncf-icons.jpg
 -->


其实，已经用了很长时间的 [draw.io](https://github.com/jgraph/drawio) 了。开始是在网页端，不过作为 VS Code 重度用户，自然转向了[插件版](https://marketplace.visualstudio.com/items?itemName=hediet.vscode-drawio)了。

> `云众享`是我开的一个小栏目，主要是分享我在云原生和平台工程领域发现的小工具和收获，以后会不定期发布。

![](https://yylives.cc/wp-content/uploads/2023/11/vscode-drawio.jpg)

最近画一个 Kubernetes 架构图，可能会用到许多 CNCF 组件，需要插入许多产品的图标。以前都是一个个找，或者在某个图标库上搜。但是这次太多了，我的需求一定也是别人的需求，于是搜索了一下，果然找到了这个[项目](https://github.com/jkroepke/draw-io-cncf-shape)。于是 Import 一下，就实现了这个效果：

![](https://yylives.cc/wp-content/uploads/2023/11/cncf-icons.jpg)

好吧，图标也不是那么全，不过网上有许多其他人分享的库，可以根据自己的需求来添加。

## 导入方法

简单的方法是下载图形库 XML 文件，然后点击 File -> Import 选中文件。

如果想设置为默认配置，可以通过配置，在 settings.json 中增加以下配置：

```json
  "hediet.vscode-drawio.customLibraries": [
    {"file": "E:\\profiles\\rocksun\\draw.io\\CNCF Graduated Projects.xml","libName": "CNCF Graduated",},
    {"file": "E:\\profiles\\rocksun\\draw.io\\CNCF Incubating Projects.xml","libName": "CNCF Incubating",},
    {"file": "E:\\profiles\\rocksun\\draw.io\\CNCF Member Products-Projects.xml","libName": "CNCF Member",},
    {"file": "E:\\profiles\\rocksun\\draw.io\\Non-CNCF Member Products-Projects.xml","libName": "Non-CNCF member",},
    {"file": "E:\\profiles\\rocksun\\draw.io\\CNCF Sandbox Projects.xml","libName": "CNCF Sandbox",},
  ],
```

然后在 `More Shapes` 启用即可。

## 相关资源

* Draw.io VS Code Integration: https://marketplace.visualstudio.com/items?itemName=hediet.vscode-drawio
* draw-io-cncf-shape: https://github.com/jkroepke/draw-io-cncf-shape