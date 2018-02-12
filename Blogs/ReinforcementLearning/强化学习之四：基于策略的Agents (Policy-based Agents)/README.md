本文是对Arthur Juliani在Medium平台发布的强化学习系列教程的个人中文翻译，该翻译是基于个人分享知识的目的进行的，欢迎交流！（This article is my personal translation for the tutorial written and posted by Arthur Juliani on Medium.com. And my work is completely based on aim of sharing knowledges and welcome communicating!）

[原文地址（URL for original article）](https://medium.com/@awjuliani/super-simple-reinforcement-learning-tutorial-part-2-ded33892c724)

***

[toc]


![](http://tech-blog-pictures.oss-cn-beijing.aliyuncs.com/2018/强化学习/强化学习之四：基于策略的Agents/1.gif)

在休息了一周后，我又带着我的强化学习系列教程的part 2回来了！在part 1，我已经展示了如何组装一个agent可以学会去在两种可能的选择中回报更多的那个。在本篇博文中，我将准备描述我们如何从之前那个简单的agent出发，让它进一步学会吸收从环境中获得的观察（Observation），并采取可以让它获得长期最优回报的行动，而不仅仅是当下回报最优的行动。意即，我们将获得一个完备的agent。

将完整问题暴露给一个agent的环境（Environments）一般称作**马尔科夫决策过程（Markov Decision Processes (MDPs)）**。这些环境不只提供给定行动的回报和状态迁移，而且这些回报也是基于（condition on）环境的状态（state）以及agent在那个状态下所采取的行动的。这些动态(dynamics)也是暂时(temporal)的，并且也会在时间上有所延迟。

说得更正式一点，我们可以像这样定义马尔科夫决策过程：一个MDP有一个所有可能的状态集合S，我们的agent随时随刻都处在集合中的某个状态s。还有一个所有可能的行动集合A，我们的agent随时随刻都将从中选择一个行动来执行。给定一个状态行动对（s,a），转移到新状态s'的概率由T(s,a)定义，而回报r由R(s,a)定义。如此，在一个MDP的任意时刻，一个agent都在一个状态s中，采取了行动a，并到达新状态s‘同时获得回报r。

虽然听起来相对比较简单，但是我们可以把几乎任何任务都考虑成一个MDP架构。比如，想象打开一个门，状态就是我们视觉中的门，以及我们身体的位置还有真实世界的门对象。行动集合是任意时刻我们身体可以采取的行动。而回报则是门可以被成功地打开。某些行动，像走向门这个行为是为了解决这个问题而比较必要的，但是它们本身没有回报，因为只有打开门本身才能提供回报。在这种情况下，一个agent需要学习分配值（value）到各个最终可以导向回报的行为，这也就导向了我们对**时序动态性（temporal dynamics）**的介绍。

# Cart-Pole任务（Cart-Pole Task）

为了完成这个任务，我们将需要一个比双臂赌博机更复杂的挑战给agent。为了满足这个需求，我们将用到OpenAI的gym，它是一系列强化学习环境的集合。我们将使用其中最经典的任务之一，Cart-Pole。想了解更多有关OpenAI的gym的内容，以及这个具体任务相关的知识，可以看一下它们的[教程](https://gym.openai.com/docs)。本质上，我们将让我们的agent学习如何尽可能长时间地平衡一个杆子（pole），使其不倒下。不像双臂赌博机，这个任务要求：

- 观察-agent需要知道杆子当前在哪，以及它现在的角度如何。为了实现这一点，我们的神经网络需要获得观察，并在生成采取各种行动的相应概率时参考观察的情况。
- 延迟回报-让杆子尽可能地保持不倒下意味着要一直移动杆子，使得它在现在和未来都尽量不倒下。为了实现这一点，我们将调整每个观察-行动对的回报，这需要用到一个给行动赋权的函数（using a function that weighs actions over time）。

为了将各个时间的回报都考虑进来，我们之前的教程里用到的策略梯度将需要做一点调整。第一个调整是，我们现在需要用超过一回一次的经验来更新agent。为了实现这一点，我们将把经验都收集在一个缓存中，并偶尔地将它们一次性地更新到agent上。这些经验的序列有时候称为“首次展示”（rollouts），或者叫“经验痕迹”（experience trace）。然而我们不能只是用这些rollouts本身，我们将需要保证回报是由折现因子进行了恰当地调整的。

直觉上，这使得每个行动的考虑都不仅包括当下的即时回报，还有所有未来的回报。我们现在用这个稍作修改的回报作为损失方程中的优势的估计值。做出这些改变后，我们已经准备好来解决CartPole问题了！


我们开始吧！


```

'''
Simple Reinforcement Learning in Tensorflow Part 2-b:
Vanilla Policy Gradient Agent
This tutorial contains a simple example of how to build a policy-gradient based agent that can solve the CartPole problem. For more information, see this Medium post. This implementation is generalizable to more than two actions.

For more Reinforcement Learning algorithms, including DQN and Model-based learning in Tensorflow, see my Github repo, DeepRL-Agents.
'''

import tensorflow as tf
import tensorflow.contrib.slim as slim
import numpy as np
import gym
import matplotlib.pyplot as plt
%matplotlib inline

try:
    xrange = xrange
except:
    xrange = range

    
    
env = gym.make('CartPole-v0')

# Making new env: CartPole-v0
The Policy-Based Agent



gamma = 0.99

def discount_rewards(r):
    """ take 1D float array of rewards and compute discounted reward """
    discounted_r = np.zeros_like(r)
    running_add = 0
    for t in reversed(xrange(0, r.size)):
        running_add = running_add * gamma + r[t]
        discounted_r[t] = running_add
    return discounted_r



class agent():
    def __init__(self, lr, s_size,a_size,h_size):
        #These lines established the feed-forward part of the network. The agent takes a state and produces an action.
        self.state_in= tf.placeholder(shape=[None,s_size],dtype=tf.float32)
        hidden = slim.fully_connected(self.state_in,h_size,biases_initializer=None,activation_fn=tf.nn.relu)
        self.output = slim.fully_connected(hidden,a_size,activation_fn=tf.nn.softmax,biases_initializer=None)
        self.chosen_action = tf.argmax(self.output,1)

        #The next six lines establish the training proceedure. We feed the reward and chosen action into the network
        #to compute the loss, and use it to update the network.
        self.reward_holder = tf.placeholder(shape=[None],dtype=tf.float32)
        self.action_holder = tf.placeholder(shape=[None],dtype=tf.int32)
        
        self.indexes = tf.range(0, tf.shape(self.output)[0]) * tf.shape(self.output)[1] + self.action_holder
        self.responsible_outputs = tf.gather(tf.reshape(self.output, [-1]), self.indexes)

        self.loss = -tf.reduce_mean(tf.log(self.responsible_outputs)*self.reward_holder)
        
        tvars = tf.trainable_variables()
        self.gradient_holders = []
        for idx,var in enumerate(tvars):
            placeholder = tf.placeholder(tf.float32,name=str(idx)+'_holder')
            self.gradient_holders.append(placeholder)
        
        self.gradients = tf.gradients(self.loss,tvars)
        
        optimizer = tf.train.AdamOptimizer(learning_rate=lr)
        self.update_batch = optimizer.apply_gradients(zip(self.gradient_holders,tvars))
        
        
# Training the Agent

tf.reset_default_graph() #Clear the Tensorflow graph.

myAgent = agent(lr=1e-2,s_size=4,a_size=2,h_size=8) #Load the agent.

total_episodes = 5000 #Set total number of episodes to train agent on.
max_ep = 999
update_frequency = 5

init = tf.global_variables_initializer()

# Launch the tensorflow graph
with tf.Session() as sess:
    sess.run(init)
    i = 0
    total_reward = []
    total_lenght = []
        
    gradBuffer = sess.run(tf.trainable_variables())
    for ix,grad in enumerate(gradBuffer):
        gradBuffer[ix] = grad * 0
        
    while i < total_episodes:
        s = env.reset()
        running_reward = 0
        ep_history = []
        for j in range(max_ep):
            #Probabilistically pick an action given our network outputs.
            a_dist = sess.run(myAgent.output,feed_dict={myAgent.state_in:[s]})
            a = np.random.choice(a_dist[0],p=a_dist[0])
            a = np.argmax(a_dist == a)

            s1,r,d,_ = env.step(a) #Get our reward for taking an action given a bandit.
            ep_history.append([s,a,r,s1])
            s = s1
            running_reward += r
            if d == True:
                #Update the network.
                ep_history = np.array(ep_history)
                ep_history[:,2] = discount_rewards(ep_history[:,2])
                feed_dict={myAgent.reward_holder:ep_history[:,2],
                        myAgent.action_holder:ep_history[:,1],myAgent.state_in:np.vstack(ep_history[:,0])}
                grads = sess.run(myAgent.gradients, feed_dict=feed_dict)
                for idx,grad in enumerate(grads):
                    gradBuffer[idx] += grad

                if i % update_frequency == 0 and i != 0:
                    feed_dict= dictionary = dict(zip(myAgent.gradient_holders, gradBuffer))
                    _ = sess.run(myAgent.update_batch, feed_dict=feed_dict)
                    for ix,grad in enumerate(gradBuffer):
                        gradBuffer[ix] = grad * 0
                
                total_reward.append(running_reward)
                total_lenght.append(j)
                break

        
            #Update our running tally of scores.
        if i % 100 == 0:
            print(np.mean(total_reward[-100:]))
        i += 1

'''
16.0
21.47
25.57
38.03
43.59
53.05
67.38
90.44
120.19
131.75
162.65
156.48
168.18
181.43
'''

```



[代码的github链接](https://github.com/awjuliani/DeepRL-Agents/blob/master/Vanilla-Policy.ipynb)

现在，我们已经有了一个功能齐全的强化学习agent了。不过我们的agent还远没有达到最先进的水平。当我们在用神经网络来表示策略时，这个网络还不像大多数比较先进的网络那么深或复杂。在下一篇博客里，我将展示如何用深度神经网络来创造可以学习复杂环境，并且可以玩比平衡杆更有意思的游戏的agent。用这样的方法，我们将接触到可以用一个网络从复杂环境中学到的那类表征（representations）。


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