<script type="text/javascript" async src="https://cdn.mathjax.org/mathjax/latest/MathJax.js?config=TeX-MML-AM_CHTML"> </script>

本文是对Arthur Juliani在Medium平台发布的强化学习系列教程的个人中文翻译。（This article is my personal translation for the tutorial written and posted by Arthur Juliani on Medium.com。）

[原文链接（URL for original article)](https://medium.com/emergent-future/simple-reinforcement-learning-with-tensorflow-part-0-q-learning-with-tables-and-neural-networks-d195264329d0)

**纯属自愿翻译，只为学习与分享知识。所以如果本系列教程对你有帮助，麻烦不吝在[github的项目](https://github.com/bluemapleman/MapleAI)上点个star吧！非常感谢！**

***

[toc]

![](http://tech-blog-pictures.oss-cn-beijing.aliyuncs.com/2018/强化学习/强化学习之二：Q-Learning原理及表与神经网络的实现/1.jpeg)

我们将学习如何解决OpenAI的冰湖（FrozenLake）问题。不过我们的冰湖版本和上图呈现的图片可不太一样~

作为本强化学习教程系列的第一章，我们将一同探索强化学习算法的一个大家庭——Q-Learning算法。它们和后面章节基于策略的算法（Policy-based algorithms）（1-3 part）有些不一样。相对于用一个复杂而臃肿的深度神经网络，我们将以实现一个简单的查阅表（lookup-table）版本的算法为初始目标，然后再展示如何用Tensorflow框架来实现一个等价的神经网络版本的算法。考虑到我们将回归基础知识，所以本教程可以视作系列教程的第0部分。希望本教程能够帮助你理解Q-Learning的工作原理，基于此，我们将最终结合策略梯度（Policy Gradient）和Q-Learning来构造最先进的强化学习代理（Agents）。（如果你对策略网络（Policy Networks）更感兴趣，或者早就掌握了Q-Learning，你可以直接从[这里](https://medium.com/@awjuliani/super-simple-reinforcement-learning-tutorial-part-1-fd544fab149)开始。）

不像策略梯度方法那样试图学习到可以将一个**观察（Observation）**与一个**动作（action）**直接映射的函数，Q-Learning会尝试去学习给定一个**状态（State）**下，采取某个具体动作的值。虽然这两种方式最终都可以实现在给定情况下的智能行为决策，但是如何最终完成行为选择的过程是非常不一样的。你可能听说过[可以玩Atari游戏的深度Q网络（Deep Q-Networs）](http://www.nature.com/nature/journal/v518/n7540/full/nature14236.html)，而它其实本质上也就是更复杂的Q-Learning算法的实现。

# 表环境下的表方法（Tabular Approaches for Tabular Environments）

![](http://tech-blog-pictures.oss-cn-beijing.aliyuncs.com/2018/强化学习/强化学习之二：Q-Learning原理及表与神经网络的实现/2.png)

冰湖环境的规则：

在这个教程里，我们将试图解决[OpenAI的gym](https://gym.openai.com/)项目中包含的冰湖[FrozenLake](https://gym.openai.com/envs/FrozenLake-v0)问题。对于不熟悉gym项目的人来说，OpenAI gym提供了一种能方便简易地在一系列游戏中，对**学习代理（learning agents）**进行各类实验或测试的方式。而其中之一的冰湖环境是一个4*4的网格。格子包含三种类型：起始格，目标格，安全的冰格和危险的冰洞。我们的目标是让一个agent能够自己从起点到终点，并且不会在中途掉入洞中。在任何时候，agent都可以选择从上，下，左，右四个中选择一个方向进行一步移动。而后会使问题变复杂的是，在冰湖环境中，还有**风**会偶尔把agent吹得偏离到一个并非它移动目标的格子上。因此，在这种环境下agent就不太可能每次都能表现完美，但是学习如何去避免掉入洞中并达到目标格还是可以做到的。agent每走一步的**回报（reward）**都是0，除了在达到目标时为1。因此，我们需要一个算法可以学习到**长期期望回报**。这也就是Q-Learning发挥用处的地方。


在这个算法最简单的实现中，Q-Learning会以一个**表（table）**的形式呈现。这个表的行代表不同的状态（所在方格的坐标），列代表不同的可采取的行动（上、下、左、右移动一步）。在冰湖环境中，我们有16个状态（每个方格算一个），以及四种动作，因此我们将得到一个16*4的Q值表，这个表的每一个具体值的含义是：**该状态下，采取该行为的长期期望回报**。我们从初始化一个一致的Q值表（全部赋值为0）开始，再根据我们观察得到的对各种行动的回报来更新Q值表的对应值。

我们对Q值表的更新准则是**[贝尔曼方程（Bellman Equation）](https://en.wikipedia.org/wiki/Bellman_equation)**。贝尔曼方程告诉我们：**一个给定行动的期望长期回报等于【当前回报】加上【下一个状态下，采取期望中所能带来最优未来长期回报的行为对应的回报】**。因此，我们可以在Q表上估计如何对未来行动的Q值进行更新。贝尔曼方程用数学公式表示如下：

$$Q(s,a) = r + γ(max(Q(s’,a’))$$

这个公式的描述了一个给定状态s下，采取行动a的Q值等于当即获得的回报r加上一个折现因子y乘以能够最大化的在下一状态s'采取时能获得的最大长期回报的动作a'对应的长期回报。折现因子y允许我们决定相对于当前就可以获得的回报，未来的可能回报的相对重要性。通过这种方式，Q表会慢慢开始获得更准确的任一给定状态下，采取任意动作所对应的期望未来回报值。以下是Python版的对于Q表版本的冰湖环境解决方案的完整实现：


```python
import gym
import numpy as np


env = gym.make('FrozenLake-v0')

# Implement Q-Table learning algorithm
# 实现Q表学习算法
# Initialize table with all zeros
# 初始化Q表为全0值
Q = np.zeros([env.observation_space.n,env.action_space.n])
# Set learning parameters
# 设置学习参数
lr = .8
y = .95
num_episodes = 2000
# create lists to contain total rewards and steps per episode
# 创建列表以包含每个episode的总回报与总步数
#jList = []
rList = []
for i in range(num_episodes):
    # Reset environment and get first new observation
    # 初始化环境并获得第一个观察
    s = env.reset()
    rAll = 0
    d = False
    j = 0
    # The Q-Table learning algorithm
    # Q表学习算法
    while j < 99:
        j+=1
        # Choose an action by greedily (with noise) picking from Q table
        # 基于Q表贪婪地选择一个最优行动（有噪音干扰）
        a = np.argmax(Q[s,:] + np.random.randn(1,env.action_space.n)*(1./(i+1)))
        # Get new state and reward from environment
        # 从环境中获得回报和新的状态信息
        s1,r,d,_ = env.step(a)
        
        #Update Q-Table with new knowledge
        # 用新的知识更新Q表
        Q[s,a] = Q[s,a] + lr*(r + y*np.max(Q[s1,:]) - Q[s,a])
        rAll += r
        s = s1
        if d == True:
            break
    #jList.append(j)
    rList.append(rAll)

print("Score over time: " +  str(sum(rList)/num_episodes))

print("Final Q-Table Values")
print(Q)
```

[Github源代码](https://gist.github.com/awjuliani/9024166ca08c489a60994e529484f7fe/raw/0e4e70d3c2dce58bdba3d7136af6dc253ac58750/Q-Table%20Learning-Clean.ipynb)

**(感谢[Praneet D](https://github.com/PraneetDutta)找到了该实现方法对应的最优的超参数）**

# 基于神经网络的Q-Learning（Q-Learning with Neural Networks）

现在你可能认为：表格方法挺好的，但是它不能规模化（scale），不是吗？因为对一个简单的网格世界建立一个16*4的表是很容易的，但是在任何一个现在的游戏或真实世界环境中都有无数可能的状态。对于大多数有趣的问题，表格都无法发挥出作用。因此，我们需要一些代替性的方案来描述我们的状态，并生成对应动作的Q值：这也就是**神经网络（Neural Network，简称NN）**可以大展身手的地方。NN可以作为一个动作估计器（function approximator），我们能够输入任意多的可能状态，因为所有状态都可以被编码成一个个向量，并把它们和各自对应的Q值进行对应（map）。

在冰湖例子中，我们将使用一个一层的NN，它接受以one-hot形式编码的状态向量（1*16），并输出一个含有4个Q值的向量，每个分量对应一个动作的长期期望回报。这样一个简单的NN就像一个强化版的Q表，而网络的权重就发挥着曾经的Q表中的各个单元格的作用。关键的不同时我们可以方便简易地扩充Tensorflow网络，包括加新的层，激活函数以及不同的输出类型，而这些都是一个一般的表格无法做到的。于是，更新的方法也发生了一点变化。相比于之前直接更新表格，我们现在将使用**逆传播（backpropagation）和**损失函数（loss function）**来完成更新。我们的损失函数采取平方和损失的形式，即加总当前预测的Q值与目标值间的差值的平方，并以梯度形式在网络中传播。这种情况下，所选行动的目标Q值依然采用上面提到的贝尔曼方程中的计算方法。

$$Loss = \Sigma(Q-target - Q)^2$$

以下是用Tensorflow实现简单Q网络的完整代码：

```python
# Q-Network Learning
# Q网络学习

import gym
import numpy as np
import random
import tensorflow as tf
import matplotlib.pyplot as plt
%matplotlib inline

# Load the environment
# 加载环境

env = gym.make('FrozenLake-v0')


# The Q-Network Approach
# Q网络方法
# Implementing the network itself
# 实现网络

tf.reset_default_graph()

# These lines establish the feed-forward part of the network used to choose actions
# 下面的几行代码建立了网络的前馈部分，它将用于选择行动
inputs1 = tf.placeholder(shape=[1,16],dtype=tf.float32)
W = tf.Variable(tf.random_uniform([16,4],0,0.01))
Qout = tf.matmul(inputs1,W)
predict = tf.argmax(Qout,1)

# Below we obtain the loss by taking the sum of squares difference between the target and prediction Q values.
# 下面的几行代码可以获得预测Q值与目标Q值间差值的平方和加总的损失。
nextQ = tf.placeholder(shape=[1,4],dtype=tf.float32)
loss = tf.reduce_sum(tf.square(nextQ - Qout))
trainer = tf.train.GradientDescentOptimizer(learning_rate=0.1)
updateModel = trainer.minimize(loss)

# Training the network
# 训练网络
init = tf.initialize_all_variables()

# Set learning parameters
# 设置学习参数
y = .99
e = 0.1
num_episodes = 2000
#create lists to contain total rewards and steps per episode
# 创建列表以包含每个episode对应的总回报与总步数。
jList = []
rList = []
with tf.Session() as sess:
    sess.run(init)
    for i in range(num_episodes):
        # Reset environment and get first new observation
        # 初始化环境并获得第一个观察
        s = env.reset()
        rAll = 0
        d = False
        j = 0
        # The Q-Network
        # Q网络
        while j < 99:
            j+=1
            #Choose an action by greedily (with e chance of random action) from the Q-network
            # 基于Q网络的输出结果，贪婪地选择一个行动（有一定的概率选择随机行动）
            a,allQ = sess.run([predict,Qout],feed_dict={inputs1:np.identity(16)[s:s+1]})
            if np.random.rand(1) < e:
                a[0] = env.action_space.sample()
            # Get new state and reward from environment
            # 从环境中获得回报以及新的状态信息
            s1,r,d,_ = env.step(a[0])
            # Obtain the Q' values by feeding the new state through our network
            # 通过将新的状态向量输入到网络中获得Q值。
            Q1 = sess.run(Qout,feed_dict={inputs1:np.identity(16)[s1:s1+1]})
            # Obtain maxQ' and set our target value for chosen action.
            # 获得最大的Q值，并为所选行为设定目标值
            maxQ1 = np.max(Q1)
            targetQ = allQ
            targetQ[0,a[0]] = r + y*maxQ1
            # Train our network using target and predicted Q values
            # 用目标和预测的Q值训练网络
            _,W1 = sess.run([updateModel,W],feed_dict={inputs1:np.identity(16)[s:s+1],nextQ:targetQ})
            rAll += r
            s = s1
            if d == True:
                # Reduce chance of random action as we train the model.
                # 随着训练的进行，主键减少选择随机行为的概率
                e = 1./((i/50) + 10)
                break
        jList.append(j)
        rList.append(rAll)
print("Percent of succesful episodes: " + str(sum(rList)/num_episodes) + "%")

# Percent of succesful episodes: 0.352%
# 成功的episode比例：0.352%
```

```python
# Some statistics on network performance
# 一些网络性能的统计量
# We can see that the network beings to consistently reach the goal around the 750 episode mark.
# 我们可以看到，当网络训练了750个episode左右的时候，agent就可以比较稳定地到达目标了。


plt.plot(rList)
```
![](http://tech-blog-pictures.oss-cn-beijing.aliyuncs.com/2018/强化学习/强化学习之二：Q-Learning原理及表与神经网络的实现/3.png)


```python
# It also begins to progress through the environment for longer than chance aroudn the 750 mark as well.
#  在750个episode之后，agent也一般需要更长的步数以到达目标。

plt.plot(jList)
```

![](http://tech-blog-pictures.oss-cn-beijing.aliyuncs.com/2018/强化学习/强化学习之二：Q-Learning原理及表与神经网络的实现/4.png)

虽然网络学会了解决冰湖问题，但是结果表明它似乎比如Q表方法那么高效。即虽然神经网络在Q-Learning问题上提供了更高的灵活性，但它也牺牲了一定的稳定性。还有很多可能的对我们的简单Q网络进行扩展的办法，这些扩展可以让NN获得更好的性能并实现更稳定的学习过程。两种需要提到的特别技巧分别是**经验重放（Experience Replay）**和**冰冻目标网络（Freezing Target Networks）**。这些改进方式或者其它的一些技巧都是让DQN可以玩Atari游戏的关键所在，并且我们也将在后面探索这些相关知识。对于有关Q-Learning的更多理论，可以看Tambet Matiisen的[这篇博文](http://neuro.cs.ut.ee/demystifying-deep-reinforcement-learning/)，希望本教程可以帮助对实现简单Q-Learning算法的人们一些帮助！

***

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