本文是对Arthur Juliani在Medium平台发布的强化学习系列教程的个人中文翻译，该翻译是基于个人分享知识的目的进行的，欢迎交流！（This article is my personal translation for the tutorial written and posted by Arthur Juliani on Medium.com. And my work is completely based on aim of sharing knowledges and welcome communicating!）

[原文地址（URL for original article）]()

***

[toc]

![](http://tech-blog-pictures.oss-cn-beijing.aliyuncs.com/2018/强化学习/强化学习之七：可视化agent的思想和行动/1.jpeg)

在本篇博客里，我想更深入地探讨我们的神经agent在训练过程中所学到的表征。当得到一个高分，或者完成一个特定的任务就是我们对于我们的神经agent的要求的时候，同样我们也应该理解如何，以及更重要的，为什么agent会以某种方式表现。为了使得学习过程更透明，我建立了一个d3.js驱动的网络接口，它可以在学习过程中展示各种各样的有关agent的信息。我称之为强化学习控制中心。在这篇博客里，我会用它来提供一些有关强化学习agent如何以及为什么等相关的信息。



# 控制中心接口（The Control Center Interface）

![](http://tech-blog-pictures.oss-cn-beijing.aliyuncs.com/2018/强化学习/强化学习之七：可视化agent的思想和行动/2.png)

>强化学习控制中心接口

控制中心是为了让用户可以实时追踪agent在学习如果解决一个任务的过程中的性能变化。在接口的左边，每一轮的长度还有各时间的回报都会被追踪以及动态更新。右边展示了一个简单训练轮的动画gif，还有一轮中每一步的优势以及值函数的计算结果。

这个接口目前只适配我的博客中所描述的神经网络和任务。它是一个**双子竞争DQN(Double-Dueling-DQN)**，环境则是一个简单的网格世界。网格世界的规则如下：agent的目标是尽快地到达绿色方块，过程中要避免红色方块。绿色方块提供+1的回报，红色方块提供-1的回报。每一步都有-0.1的回报。在每一轮开始的时候，三个方格被随机放到网格上。

<div style='position:relative; padding-bottom:94%'><iframe src='https://gfycat.com/ifr/MajorCoordinatedGoldfish?referrer=https%3A%2F%2Fmedium.com%2Fmedia%2F583c3de27949a283ed0cb6b28b8500b9%3FpostId%3D4f27b134bb2a' frameborder='0' scrolling='no' width='100%' height='100%' style='position:absolute;top:0;left:0;' allowfullscreen></iframe></div>
>对agent在一个epoch的训练过程中行动与思想的展示


双子竞争DQN的agent在它探索网格世界时，会同时接受两个分离的信息流：一个优势流（advantage stream）和一个价值流（value stream）。优势流代表了网络所认为的，在给定当前它所在的状态下，采取每个行动分别的有多么好。价值流则代表了在不考虑可能的行动的情况下，任一给定所在状态分别有多么好。有了控制中心，我们可以观察网络如何逐渐学习正确地预测状态和行动的价值。随着训练过程的进行，它会从乍看起来的随机值，逐渐演变为能准确地指出哪个行动是最有优势的。我们可以认为这种可视化提供了一个我们观察agent的“思考过程”的入口。它是否知道它正处在一个好的位置？是否知道在它往下走一格是好的选择？这可以让我们更深刻地理解为什么我们的agent可以表现不错，不管是在什么情况或环境中对它进行训练。

# 进入agent的大脑

我们不只可以用接口来探索agent如何进行训练，我们也能用它测试和调试我们已经经过完全训练的agent。例如，在训练了我们的agent如何解决上述的3*3的网格世界问题后，我们可以提供它一些特别的测试情景，这些情景是它从来没在训练过程中遇见过的，借此我们可以评估它是否真的具备了我们希望它所具备的经验。

下面是一个agent如何在修改版（只有绿色方块）的任务中表现的实例。如你所见，随着agent逐渐靠近绿色方块，价值估计值如我们所期望地逐渐上升。它也给出了对于采取行动的优势的高估计值，这引导着agent不断靠近绿色目标。

<iframe src='https://gfycat.com/ifr/WideUnrulyAfricanbushviper' frameborder='0' scrolling='no' allowfullscreen width='640' height='584'></iframe>

在下一个测试中，我们颠倒了情况，我们会给agent一个只有两个红色方块的世界。它肯定很不喜欢这个世界。如你接下来所见，agent试图远离每个红色额方块，这导致它长时间内不断地前进又后退。注意价值估计值如何随着agent靠近红色方块时减少。

<iframe src='https://gfycat.com/ifr/WiltedBaggyBaiji' frameborder='0' scrolling='no' allowfullscreen width='640' height='591'></iframe>

最终，我给agent了一个有关存在意义的挑战。我不在在学习目标上做文章，而是把它们都去掉了。在这种情形下，蓝色方块自身在环境中，没有其它的目标。没有一个前行的目标，agent看起来在随意四处移动，并且价值估计值也似乎无意义。[Camus](https://en.wikipedia.org/wiki/Albert_Camus)会怎么说呢？

<iframe src='https://gfycat.com/ifr/MinorOfficialLarva' frameborder='0' scrolling='no' allowfullscreen width='640' height='585'></iframe>

总的来看，这三个实验给我们提供了很多证据，这些证据表明我们的agent是如我们所期望地那样在对环境进行反应。这些检查步骤在设计任何强化学习agent之前都是必要的。如果我们不仔细关注我们将要内置到agent里的期望以及环境回报的结构，我们很有可能最终也不能得到一个可以表现良好的agent，或者至少不如我们所预期的那样进行学习的agent。比如在网格世界中，采取一步行动能导致-0.1的回报。虽然这不是通常的情形。本来是没有所谓的惩罚（penalty）一说的，并且agent也能在平均50步左右到达绿色方块。它没有“理由”去尽快移动到目标位置，所以它也不会这么做。通过对每一步施加一个小的惩罚，agent有可能很快地学习到径直向绿色目标移动的直觉。这提示我们我们人类自身的潜意识中的回报结构也很可能是这样的。尽管我们可能能清楚地认为绿色就是奖励，红色就是惩罚，我们潜意识里会由于想尽快完成任务的欲望而限制自己的行动。当设计强化学习agent时，我们需要确保它们的回报结构和我们的一样丰富（rich）。


# 使用控制中心

如果你想试用一下工作版的控制中心，而无需自己训练你的agent，点击这个[链接](http://awjuliani.github.io/Center/)即可（要求浏览器是Google Chrome）。你将看到的是一个已经在网格世界中经过40,000轮预训练的agent。你可以点击左边的时间线去查看任一训练过程点中的示例轮。更早的轮清楚地展现了agent如何失败地理解了任务，但训练到最后agent几乎总会能直接到达目标。

控制中心是一个我计划继续开发的软件，因为我也将继续研究各类强化学习算法。现在它是按照[Part 4](https://medium.com/@awjuliani/simple-reinforcement-learning-with-tensorflow-part-4-deep-q-networks-and-beyond-8438a3e2b8df#.i2zpbmre8)中所描述的具体的网格世界以及DD-DQN硬编码而成的，按时如果你想把它适配到自己的项目中，你可以在[github上fork它](https://github.com/awjuliani/RL-CC)，并按照你自己的需求调整它。希望它能提供更多对于你的学习算法的了解渠道。




***

如果这篇博文对你有帮助，你可以考虑捐赠以支持未来更多的相关的教程、文章和实现。对任意的帮助与贡献都表示非常感激！

如果你想跟进我在深度学习、人工智能、感知科学方面的工作，可以在Medium上follow我 @Arthur Juliani，或者推特@awjliani。

用Tensorflow实现简单强化学习的系列教程：

1. [Part 0 — Q-Learning Agents](https://medium.com/emergent-future/simple-reinforcement-learning-with-tensorflow-part-0-q-learning-with-tables-and-neural-networks-d195264329d0)
2. [Part 1 — Two-Armed Bandit](https://medium.com/@awjuliani/super-simple-reinforcement-learning-tutorial-part-1-fd544fab149)
3. [Part 1.5 — Contextual Bandits](https://medium.com/@awjuliani/simple-reinforcement-learning-with-tensorflow-part-1-5-contextual-bandits-bff01d1aad9c)
4. [Part 2 — Policy-Based Agents](https://medium.com/@awjuliani/super-simple-reinforcement-learning-tutorial-part-2-ded33892c724)
5. [Part 3 — Model-Based RL](https://medium.com/@awjuliani/simple-reinforcement-learning-with-tensorflow-part-3-model-based-rl-9a6fe0cce99)
6. [Part 4 — Deep Q-Networks and Beyond](https://medium.com/@awjuliani/simple-reinforcement-learning-with-tensorflow-part-4-deep-q-networks-and-beyond-8438a3e2b8df)
7. [Part 5 — Visualizing an Agent’s Thoughts and Actions](https://medium.com/@awjuliani/simple-reinforcement-learning-with-tensorflow-part-5-visualizing-an-agents-thoughts-and-actions-4f27b134bb2a#.kdgfgy7k8)
8. [Part 6 — Partial Observability and Deep Recurrent Q-Networks](https://medium.com/@awjuliani/simple-reinforcement-learning-with-tensorflow-part-6-partial-observability-and-deep-recurrent-q-68463e9aeefc#.gi4xdq8pk)
9. [Part 7 — Action-Selection Strategies for Exploration](https://medium.com/@awjuliani/simple-reinforcement-learning-with-tensorflow-part-7-action-selection-strategies-for-exploration-d3a97b7cceaf)
10. [Part 8 — Asynchronous Actor-Critic Agents (A3C)](https://medium.com/@awjuliani/simple-reinforcement-learning-with-tensorflow-part-8-asynchronous-actor-critic-agents-a3c-c88f72a5e9f2#.hg13tn9zw)