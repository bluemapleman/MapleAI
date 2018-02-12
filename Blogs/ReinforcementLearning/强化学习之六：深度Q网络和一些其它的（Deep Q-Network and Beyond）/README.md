本文是对Arthur Juliani在Medium平台发布的强化学习系列教程的个人中文翻译，该翻译是基于个人分享知识的目的进行的，欢迎交流！（This article is my personal translation for the tutorial written and posted by Arthur Juliani on Medium.com. And my work is completely based on aim of sharing knowledges and welcome communicating!）

[原文地址（URL for original article）](https://medium.com/@awjuliani/simple-reinforcement-learning-with-tensorflow-part-4-deep-q-networks-and-beyond-8438a3e2b8df)

***

[toc]

![](http://tech-blog-pictures.oss-cn-beijing.aliyuncs.com/2018/强化学习/强化学习之六：深度Q网络和一些其它的/1.jpeg)

> 一个聪明的agent会学会避免地面上的危险坑洞。



欢迎来到我的强化学习系列教程的最新部分，我们将经历一次创造一个深度Q网络的全过程。它将基于[Part 0](https://medium.com/@awjuliani/simple-reinforcement-learning-with-tensorflow-part-0-q-learning-with-tables-and-neural-networks-d195264329d0#.a5pppei4l)中我们已经创造过的简单单层Q网络，所以如果你对于强化学习还很陌生，强烈建议你先读一下之前的章节。虽然在相同的简单游戏环境中，我们普通的Q网络比较勉强地才能达到和Q表一样的效果，但是深度Q网络就强大多了。为了把普通的Q网络转换成一个DQN，我们将做以下改进：


1. 从单层网络到多层卷积网络。
2. 实现**经验回放（Experience Replay ）**，这将使我们的网络能够用来自自身经验中的记忆来训练自己。
3. 启用另一个“目标”网络，我们将在更新过程中用它来计算目标Q值。

就是这三个改进使得[Google DeepMind团队能够在几十个Atari游戏中用它们的agent实现超人的表现](http://www.davidqiu.com:8888/research/nature14236.pdf)。我们将逐一看这每条改进，并向你展示如何实现它。然而我们也不会止步于此。深度学习研究的进步速度非常快，2014年的DQN技术早就不是最先进的agent类型了。我将介绍两个简单的额外DQN架构改进方法，**双子DQN（Double DQN）**和**竞争DQN（Dueling DQN）**，它们可以达到更好的表现，稳定性和更快的训练时间。最后，我们将获得一个可以搞定一系列具有挑战性的Atari游戏的网络，并且我们将阐释如何训练DQN去学习一个基本的导航任务。

# 从Q网络到深度Q网络（Getting from Q-Network to Deep Q-Network）

![](http://tech-blog-pictures.oss-cn-beijing.aliyuncs.com/2018/强化学习/强化学习之六：深度Q网络和一些其它的/2.png)

## 改进1：卷积层（Addition 1: Convolutional Layers）

既然我们的agent将要学习玩电脑游戏，它就需要能够理解游戏在屏幕上的输出，而且至少应该以和人类或者其它智能动物相近的方式来做到。相比于独立考虑每个像素，卷积层使我们能够考虑一个图片的某个区域范围，并且在我们把信息传输到网络更后面的层时，也能维持图像中的物体在空间上的联系。通过这种方式，它们能表现得和人类相近。确实有一些研究表明卷积神经网络学习到了和[原始视觉皮层相似的表征](http://journals.plos.org/ploscompbiol/article?id=10.1371/journal.pcbi.1003963)。如此，卷积神经网络就有理由成为我们网络最开始的构成元素之一。

在Tensorflow里面，我们可以用tf.contrib.layers.convolution2d函数来轻松地构造一个卷积层，调用方法如下：

```
convolution_layer = tf.contrib.layers.convolution2d(inputs,num_outputs,kernel_size,stride,padding)
```

这里的num_outs指的是要对前一层使用多少过滤器（filters）。kernel_size指的是我们要用多大的窗口来在前一层上进行滑动。stride指的是每一次我们在层上滑动窗口时跳过多少个像素。最后，padding指定的是我们是否让我们的窗口只在底层（“VALID”）进行滑动，还是在周围加上“衬垫（padding）”以保证卷积层和之前的层有相同的维度。更多信息请参照[Tensorflow文档](https://www.tensorflow.org/versions/r0.10/api_docs/python/contrib.layers.html#convolution2d)。



## 改进2：经验回放（Addition 2: Experience Replay）

第二个让DQN能够运行起来的主要改进是**经验回放**。这个做法的基本思想是：通过存储agent的经验，并随机从中提取一部分（batches）来训练网络，我们可以学到如何更稳健地在解决任务。通过存储经验，我们避免了网络只学习到它当前在这个环境中正在做的相关知识，并使得它能从各种各样的过去经验中也学习一些东西出来（所谓“温故而知新”）。这些经验都在<state,action,reward,next state>为元素的元组储存起来。经验回放缓冲区存放了固定数量的最近记忆，当新的记忆进来，旧的记忆就会溢出。当到达训练时机，我们就简单地从缓冲区中提取出一单位的批（a uniform batch）随机记忆，并用它们训练网络。对DQN来说，我们相当于为它建立了一个类来处理存储和检索记忆。


## 改进3：分离目标网络（Addition 3: Separate Target Network）

第三个使得DQN独一无二的改进是对于训练过程中的第二个网络的启用。这个网络用来生成目标Q值，这个目标Q值将用来在在训练过程中，针对每个行动计算相应的损失。为什么不只用一个网络来进行两种估计呢（状态对应当前Q值的估计和目标Q值的估计）？问题关键在于在训练的每一步，Q网络的值都在变，如果我们用一直在保持变化的一系列值来调整我们的网络值，那么值估计很有可能轻易失去控制。网络可能无法工作，因为它掉进了目标Q值和估计Q值之间的反馈循环。为了消除这个风险，目标网络的权重是固定的，只会周期性地或者很慢地对主要Q网络的值进行更新。训练得此能够以更稳定的方式进行。

相比于周期性且一次性地更新目标网络，我们将更频繁地更新它，但是是比较慢地。这种技术在[今年伊始的DeepMind一篇论文](https://arxiv.org/pdf/1509.02971.pdf)中提到，论文中谈到发现这样可以使训练过程更稳定。



# 超越DQN（Going Beyond DQN）

有了以上的改进，我们已经具备了重现2014年的DQN所需要的一切。但是世界总是日新月异的，早就有一堆针对DQN的改进被DeepMind提出，使得DQN的性能与稳定性越来越强。在你最喜欢的Atari游戏上训练你的DQN之前，我会建议先看一下更新的一些已经公布的改进。我将给你简单介绍一下其中两种改进成果：双子DQN与竞争DQN。这两个都很容易实现，并且如果结合这两种技术，我们可以在更快的训练基础上，实现更强的性能。


## 双子DQN（Double DQN）

双子DQN的主要直觉是：一般的DQN总是高估了在给定状态下采取潜在行动的Q值，而如果所有的行动都被同等级别地高估，这也不算什么问题，但是事实并不是这样。你可以很容易想象到如果某个次优的行动总是比最优的行动被给予更高的Q值，agent将很难学习到理想的策略。为了纠正这个问题，DDQN论文的作者提出了一个简单的技巧：相比于为了训练的每一步都计算目标Q值时都选择最大值，我们用我们的主要网络来选择一个行动，而我们的目标网络来生成那个行动对应的Q值。通过分离行动选择与目标Q值生成，我们得以相当程度上减弱过度估计的问题，并且使训练更快更可信。下面是新的DDQN更新目标值时所用的方程。

$$Q-Target = r +\gamma Q(s',argmax(Q(s',a,\theta),\theta'))$$

Q-Target = r + γQ(s’,argmax(Q(s’,a,ϴ),ϴ’))


## 竞争DQN（Dueling DQN）

![](http://tech-blog-pictures.oss-cn-beijing.aliyuncs.com/2018/强化学习/强化学习之六：深度Q网络和一些其它的/3.png)

>上图：常规的单一Q值流动的DQN。下图：竞争DQN，*值*和*优势*是分开计算，并在最后一层结合为Q值。

为了解释竞争DQN在架构上做的变化，我们需要首先解释一些额外的强化学习术语。我们到目前一直所讨论的Q值的含义都是：**在给定状态下，采取一个行动有多么好**。这可以写作Q(s,a)。这个给定状态下的行动实际上可以分解成值的两个方面。第一方面是值函数V(s)，它简单地给出在一个给定状态下有多么好。第二个是优势函数A(a)，它给出采取某个行动相比其它的行动会有多么更好。我们可以将Q视作V和A的结合。更标准化来表示：

$$Q(s,a) =V(s) + A(a)$$

竞争DQN的目标是让一个网络分离地计算优势函数和值函数，并只在最后一层将两者结合。乍看起来，这样做貌似没什么意义。为什么要把一个我们之后要组装起来的函数分离呢？关键是认识到这样做的好处是：能够认识到我们的强化学习agent可能不需要在任何时候同同时关注值和优势。比如说，想想在一个户外公园里坐着看日落。日落很美，坐在这里感觉很享受，回报很大。不需要采取任何行动，基于任何你所在的环境状态以外的东西去考虑你坐在那里的价值看起来也没什么意义。我们可以完成更稳健的状态值估计，只要把它和与特定行动绑定的必要性分离就行。



# 全部组装（Putting it all together）

![](http://tech-blog-pictures.oss-cn-beijing.aliyuncs.com/2018/强化学习/强化学习之六：深度Q网络和一些其它的/4.png)

>简单的方块世界环境，目标是移动蓝色方块到绿色方块的位置，过程中不能碰到红色方块。

现在我们已经知道了所有创造DQN所需的技巧，让我们在一个游戏环境中来实际尝试一下！我们在上面描述的DQN可以在训练足够时间后玩Atari游戏，让网络能够在那些游戏上表现不错需要在一个性能好的机器上训练至少一天。为了教学目的，我已经建立了一个简单的游戏环境，在这个环境中，我们的DQN在一个中等强劲性能的机器上（GTX970）训练几个小时。在环境当中，agent控制蓝色方块，它的目标是去向绿色方块（回报+1）并避免红色方块（回报-1）。在每一轮开始的时候，agent被随机放入5*5的网格世界里。agent只能再50步内尝试实现最大化的汇报。因为是随机放置，agent需要做的不只仅仅学习一个简单的固定路线（在Tutorial 0的FrozenLake环境中，就这么简单）。相反，agent必须学习方格之间的空间关系。而事实上，它也确实可以做到。



[Github代码链接](https://github.com/awjuliani/DeepRL-Agents/blob/master/Double-Dueling-DQN.ipynb)


游戏环境会生成一个84*84*3的彩色图片，并且用尽可能和OpenAI gym相似的方式调用函数。通过这样做，将会比较容易调整代码使其适配到任何OpenAI的atari游戏上。我鼓励有时间和计算资源的小伙伴们一定要试一下让agent玩好Atari游戏。超参数可能要花点功夫调，但是绝对是有可能实现的。好运！








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