本文是对Arthur Juliani在Medium平台发布的强化学习系列教程的个人中文翻译，该翻译是基于个人分享知识的目的进行的，欢迎交流！（This article is my personal translation for the tutorial written and posted by Arthur Juliani on Medium.com. And my work is completely based on aim of sharing knowledges and welcome communicating!）

[原文地址（URL for original article）](https://medium.com/@awjuliani/super-simple-reinforcement-learning-tutorial-part-1-fd544fab149)

***

[toc]

![](http://tech-blog-pictures.oss-cn-beijing.aliyuncs.com/2018/强化学习/强化学习之三：双臂赌博机/1.jpeg)

# 引入（Introduction）

强化学习不只给我们提供了去教会一个智能agent如何行动的能力，也使得agent可以通过自己与环境的交互去进行学习。通过结合深度神经网络针对一个基于目标驱动的agent学习可以获得的复杂表征（representations），计算机已经实现了一些非常惊人的成果，比如在一系列atari游戏中击败人类玩家，并且在围棋上打败世界冠军。

然而要学会如何建立这么强大的agent需要已经习惯于**有监督学习（Supervised Learning）**的人们转变一下思想，我们现在的做法再也不是简单地让算法去学会对某种刺激和某种响应进行一一匹配了。相反地，强化学习算法必须让agent自己通过使用观察、回报和行动的方式来学会匹配。因为对于agent来说，再也不会有某种给定状态下应该采取的绝对“正确”的行动，所以这就使得这件事情看起来有点困难了。在本博客中，我将带你完整地走一遍强化学习agents的创造和训练过程。最开始的agent和任务（task）的示例都将比较简单，所以相关的概念也都会比较明晰，之后我们再尝试理解更复杂的任务和环境。


# 双臂赌博机（Two-Armed Bandit）

最简单的强化学习问题就是N臂赌博机。本质上来说，N臂赌博机就是由n个槽机器（n-many slot machine），每个槽对应了一个不同的固定回报概率。我们的目标是去发现有最优回报的机器，并且通过一直选取这个机器以获得最大化回报。我们先简化一下这个问题，即只有两个槽机器供我们选择。实际上，这个问题如此简单，它更像是一个强化学习的引导例子而不能称作一个强化学习问题本身。因为一个典型的强化学习任务包含以下方面：

- 不同的行动产生不同的回报。举例来说，当在迷宫中找宝藏时，往左走可能找到宝藏，而往右走可能遇到一群蛇。
- 回报总是在时间上延迟的。这就意味着即使在上面的迷宫例子里，往左走是正确的选择，但是我们不会知道这一点直到我们做出选择并到达新的状态之后。
- 一个行动的回报是基于环境的状态的。仍然是迷宫的例子，在某个分叉往左走可能是理想的，但其他的分叉可能不是这样。

n臂赌博机是一个非常好的入门问题，因为我们不用考虑上述的第二、三方面。我们只需要集中精力去学习对应的每种行动对应的回报，并保证我们总是选择最优的那些行动。在强化学习术语中，这叫做**学习一个策略（Learn a policy）**。我们将使用一种称为**策略梯度（policy gradient）**的方法，即我们将用一个简单的神经网络来学习如何选择行动，它将基于环境的反馈通过梯度下降来调整它的参数。还有另一种解决强化学习问题的方法，这些方法里，agent会学习**价值函数（value function）**。在这种方法里，相比于学习给定状态下的最优行动，agent会学习预测一个agent将处于的给定状态或者采取的行动多么好。而这两种方法都可以让agent表现优异，不过策略梯度方法显得更加直接一点。

# 策略梯度（Policy Gradient）

最简单的理解策略梯度网络的方法就是：它其实就是一个会生成明确输出的神经网络。在赌博机的例子里，我们不需要基于任何状态来说明这些输出。因此，我们的网络将由一系列的权重构成，每个权重都和每一个可以拉动的赌博机臂相关，并且会展现出我们的agent认为拉动每个臂分别会对应多么好的结果。如果我们初始化权重为1，那么我们的agent将会对每个臂的潜在回报都非常乐观。

为了更新我们的网络，我们将简单地基于**e-贪婪策略（e-greedy policy）**尝试每个臂（在Part 7可以看到更多关于行动选择策略的内容）。这意味着大多数时间里，我们的agent将会选择有着预期最大回报值的行动，但偶尔，它也会随机行动。通过这种方式，agent可能尝试到每一个不同的臂并持续地学习到更多知识。一旦我们的agent采取一个行动，它将会收获到一个值为1或-1的回报。基于这个回报，我们就可以使用策略损失函数来对我们的网络进行更新：

$$Loss = -log(\pi)*A$$

A是优越度，也是所有强化学习算法的一个重要部分。直觉上，它描述了一个行动比某个基准线好多少。在未来的算法中，我们将遇到更复杂的用于比较回报的基准线，而现在我们就假设基准线为0，我们也可以简单地把它想成我们采取每个行动对应的回报。

$\pi$是策略。在这个例子中，它和所选行动的权重相关。

直觉上，这个损失函数使我们可以增加那些有望产出正回报行动的权重，而降低那些可能产生负回报的行动的权重。通过这种方式，agent将更有可能或更不可能在未来采取某个行动。通过采取行动，获得回报并更新网络这个过程的循环，我们将很快得到一个收敛的agent，它将可以解决赌博机问题。不要只是听我讲，你应该自己试一试。


```
# Simple Reinforcement Learning in Tensorflow Part 1:
# The Multi-armed bandit
# This tutorial contains a simple example of how to build a policy-gradient based agent that can solve the multi-armed bandit problem. For more information, see this Medium post.
# 简单强化学习的Tensorflow实现 Part 1：
# 多臂赌博机
# 这个教程包含一个简单的，能够解决多臂赌博机问题的建立基于策略梯度的agent的实例

# For more Reinforcement Learning algorithms, including DQN and Model-based learning in Tensorflow, see my Github repo, DeepRL-Agents.
# 对于更多强化学习算法，包括用Tensorflow实现的DQN和基于模型的学习，都可以看我的Github库，DeepRL-Agents。



import tensorflow as tf
import numpy as np

# The Bandits
# Here we define our bandits. For this example we are using a four-armed bandit. The pullBandit function generates a random number from a normal distribution with a mean of 0. The lower the bandit number, the more likely a positive reward will be returned. We want our agent to learn to always choose the bandit that will give that positive reward.
# 赌博机
# 这里我们定义了赌博机。这个例子里我们使用了一个四臂赌博机。pullBandit函数产生了一个服从0均值正态分布的随机数。这个赌博机数值越小，获得一个正回报的可能性越大。我们想让我们的agent学会总是选择正回报的行动。


# List out our bandits. Currently bandit 4 (index#3) is set to most often provide a positive reward.
# 赌博机的列表。当前赌博机4（标号#3）被设置为最常给出正回报的机器。
bandits = [0.2,0,-0.2,-5]
num_bandits = len(bandits)
def pullBandit(bandit):
    # Get a random number.
    # 获得一个随机数
    result = np.random.randn(1)
    if result > bandit:
        # return a positive reward.
        # 返回一个正回报
        return 1
    else:
        # return a negative reward.
        # 返回一个负回报
        return -1

# The Agent
# The code below established our simple neural agent. It consists of a set of values for each of the bandits. Each value is an estimate of the value of the return from choosing the bandit. We use a policy gradient method to update the agent by moving the value for the selected action toward the recieved reward.
# 下面的代码建立了我们的样例神经网络版本的agent，它由一套针对每个赌博机的数值构成。每个数值都是对于选择相应赌博机的回报的估计值。我们使用策略梯度方法来更新我们的agent，即将选择的行动的数值赋给收到的汇报。

tf.reset_default_graph()

# These two lines established the feed-forward part of the network. This does the actual choosing.
# 下面两行简历了网络的前馈部分。这个部分用来做行动决策。
weights = tf.Variable(tf.ones([num_bandits]))
chosen_action = tf.argmax(weights,0)

# The next six lines establish the training proceedure. We feed the reward and chosen action into the network
# to compute the loss, and use it to update the network.
# 下面六行代码建立了训练过程。我们喂给网络回报以及所选行动。
# 计算损失，并用其更新网络。
reward_holder = tf.placeholder(shape=[1],dtype=tf.float32)
action_holder = tf.placeholder(shape=[1],dtype=tf.int32)
responsible_weight = tf.slice(weights,action_holder,[1])
loss = -(tf.log(responsible_weight)*reward_holder)
optimizer = tf.train.GradientDescentOptimizer(learning_rate=0.001)
update = optimizer.minimize(loss)


# Training the Agent
# We will train our agent by taking actions in our environment, and recieving rewards. Using the rewards and actions, we can know how to properly update our network in order to more often choose actions that will yield the highest rewards over time.
# 训练Agent
# 我们将通过在环境中采取行动并接收回报来训练agent。通过回报和行动，我们可以知道如何合适地更新网络，以使得它将随着训练的进行，越来越经常的选择有更高回报的行动。


total_episodes = 1000 #Set total number of episodes to train agent on.  agent将要训练的episodes轮数
total_reward = np.zeros(num_bandits) #Set scoreboard for bandits to 0. 将赌博机的得分全部设为0
e = 0.1 #Set the chance of taking a random action. 设置采取一个随机行动的概率

init = tf.initialize_all_variables()

# Launch the tensorflow graph 
# 启动tensorflow计算图
with tf.Session() as sess:
    sess.run(init)
    i = 0
    while i < total_episodes:
        
        # Choose either a random action or one from our network.
        # 选择一个随机行动，或者让网络来决策
        if np.random.rand(1) < e:
            action = np.random.randint(num_bandits)
        else:
            action = sess.run(chosen_action)
        
        reward = pullBandit(bandits[action]) #Get our reward from picking one of the bandits. 从选择的赌博机上获得回报
        
        # Update the network.
        # 更新网络
        _,resp,ww = sess.run([update,responsible_weight,weights], feed_dict={reward_holder:[reward],action_holder:[action]})
        
        # Update our running tally of scores.
        # 更新运行记分器
        total_reward[action] += reward
        if i % 50 == 0:
            print "Running reward for the " + str(num_bandits) + " bandits: " + str(total_reward)
        i+=1
print "The agent thinks bandit " + str(np.argmax(ww)+1) + " is the most promising...."
if np.argmax(ww) == np.argmax(-np.array(bandits)):
    print "...and it was right!"
else:
    print "...and it was wrong!"
    
```

```
Running reward for the 4 bandits: [ 1.  0.  0.  0.]
Running reward for the 4 bandits: [  0.  -2.  -1.  38.]
Running reward for the 4 bandits: [  0.  -4.  -2.  83.]
Running reward for the 4 bandits: [   0.   -6.   -1.  128.]
Running reward for the 4 bandits: [   0.   -8.    1.  172.]
Running reward for the 4 bandits: [  -1.   -9.    2.  219.]
Running reward for the 4 bandits: [  -1.  -10.    4.  264.]
Running reward for the 4 bandits: [   0.  -11.    4.  312.]
Running reward for the 4 bandits: [   2.  -10.    4.  357.]
Running reward for the 4 bandits: [   2.   -9.    4.  406.]
Running reward for the 4 bandits: [   0.  -11.    4.  448.]
Running reward for the 4 bandits: [  -1.  -10.    3.  495.]
Running reward for the 4 bandits: [  -3.  -10.    2.  540.]
Running reward for the 4 bandits: [  -3.  -10.    3.  585.]
Running reward for the 4 bandits: [  -3.   -8.    3.  629.]
Running reward for the 4 bandits: [  -2.   -7.    1.  673.]
Running reward for the 4 bandits: [  -4.   -7.    2.  720.]
Running reward for the 4 bandits: [  -4.   -7.    3.  769.]
Running reward for the 4 bandits: [  -6.   -8.    3.  814.]
Running reward for the 4 bandits: [  -7.   -7.    3.  858.]
The agent thinks bandit 4 is the most promising....
...and it was right!
```

[Github完整代码](https://gist.github.com/awjuliani/902fe41c3a9efe27299e72aee1b3158c/raw/aa28e71d9c23d2e39261fd5e86d59166778eea25/SimplePolicy.ipynb)

（09/10/2016更新）：我重新为这个教程写了iPython代码。之前的损失函数不太直观，我已经用一个更标准和具备解释性的版本来替代了，而且对于那些非常有兴趣应用策略梯度方法到更复杂的问题上的人也更有参考价值。）




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