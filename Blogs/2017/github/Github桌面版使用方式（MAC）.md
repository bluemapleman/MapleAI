Github是一个流行的代码管理网站，同时也是全球最大的同性交友网站（滑稽）。Github网页上你可以自由地托管自己的项目，也可以fork别人的项目过来玩耍，非常之方便，今天笔者就来介绍一下github桌面版程序上，针对常见需求的那些相关使用方法，此处以Mac版本的为例，win上的基本类似。

[TOC]

# 将仓库中的代码down到本地
首先，当你不想每次都打开github网站去对你的项目文件做编辑时，你可以选择把它们down下来到本地磁盘上。而从此以后，你在本地上对项目文件的任何修改都会被记录下来，并且只要通过github桌面程序就可以把这些修改同步到对应的github网站仓库上，非常方便。

## 步骤

1. 假设我们在github上有一个名为Tech-Learning-Notes的项目。

![这里写图片描述](http://img.blog.csdn.net/20170823110007255?watermark/2/text/aHR0cDovL2Jsb2cuY3Nkbi5uZXQvcXFfMzI2OTA5OTk=/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70/gravity/SouthEast)

2. 接下来，打开github桌面版，点击左上角的“+”按钮，选择clone，你可以看到你在github上存放的（尚未down到本地的）项目列表。选中Tech-Learning-Notes项目，选择clone Repository，然后选择本地路径以存放项目文件夹。

 ![这里写图片描述](http://img.blog.csdn.net/20170823110154466?watermark/2/text/aHR0cDovL2Jsb2cuY3Nkbi5uZXQvcXFfMzI2OTA5OTk=/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70/gravity/SouthEast)
 
 3. 稍等一会儿，待clone完成后，到之前选择的对应路径下，就可以看到你的项目文件夹了。

![这里写图片描述](http://img.blog.csdn.net/20170823110510935?watermark/2/text/aHR0cDovL2Jsb2cuY3Nkbi5uZXQvcXFfMzI2OTA5OTk=/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70/gravity/SouthEast)
 
 当然，你可以随意挪动文件夹的位置，因为github桌面程序已经锁定了文件夹本身，不会因为你挪动了文件夹的位置与之前保存的位置不一样就失去关联。
 
 然后就可以愉快地在本地随意编辑你的项目了。

# 在本地提交新的代码版本到仓库

问题来了，我们在本地对我们的项目做了一些新的修改，比如改了一些文件的源代码，新增了和删除了一些文件，我们怎么把这些变化同步到github仓库呢？

##步骤
1.当你对本地的项目文件夹下的文件做了任何改动后，打开github桌面程序，你会发现，你的项目页面变成了这样：

![这里写图片描述](http://img.blog.csdn.net/20170823112328992?watermark/2/text/aHR0cDovL2Jsb2cuY3Nkbi5uZXQvcXFfMzI2OTA5OTk=/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70/gravity/SouthEast)

这里出现的所有新条目都是你对项目文件做过的改动，包括修改代码，增加或删除文件，而你可以通过勾选条目前的复选框去选定将那些改动提交到仓库。

2.选择好改动后，在下面的注释框里填写改动的相关信息，以方便后续回溯。（不填写改动注释的标题的话是无法提交改动的。）

![这里写图片描述](http://img.blog.csdn.net/20170823112616026?watermark/2/text/aHR0cDovL2Jsb2cuY3Nkbi5uZXQvcXFfMzI2OTA5OTk=/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70/gravity/SouthEast)

3.commit后，你会发现你的项目历史结点上多了一个新的环，代表你的上一次commit记录。

![这里写图片描述](http://img.blog.csdn.net/20170823112800346?watermark/2/text/aHR0cDovL2Jsb2cuY3Nkbi5uZXQvcXFfMzI2OTA5OTk=/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70/gravity/SouthEast)

4.但是commit后只是将你的改动信息保存了下来，如果要让仓库现在也变成和本地完全一样的状态，还需要点击一下右上角的sync按钮。
5.待sync完成后，小环变成了一个点，代表同步完成，然后打开github的网站，进入到项目下，就会发现改动都同步了（新增了一个测试文件夹）。

![这里写图片描述](http://img.blog.csdn.net/20170823113309878?watermark/2/text/aHR0cDovL2Jsb2cuY3Nkbi5uZXQvcXFfMzI2OTA5OTk=/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70/gravity/SouthEast)

还有建立Branch，Pull请求等功能按钮都在github桌面版的界面上，后面有时间继续给大家更新。