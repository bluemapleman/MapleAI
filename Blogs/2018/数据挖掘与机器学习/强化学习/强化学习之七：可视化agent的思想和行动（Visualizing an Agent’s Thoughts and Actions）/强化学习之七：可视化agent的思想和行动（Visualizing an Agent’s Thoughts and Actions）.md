本文是对Arthur Juliani在Medium平台发布的强化学习系列教程的个人中文翻译，该翻译是基于个人分享知识的目的进行的，欢迎交流！（This article is my personal translation for the tutorial written and posted by Arthur Juliani on Medium.com. And my work is completely based on aim of sharing knowledges and welcome communicating!）

[原文地址（URL for original article）]()

***

[toc]

![](1.jpeg)

在本篇博客里，我想更深入地探讨我们的神经agent在训练过程中所学到的表征。当得到一个高分，或者完成一个特定的任务就是我们对于我们的神经agent的要求的时候，同样我们也应该理解如何，以及更重要的，为什么agent会以某种方式表现。为了使得学习过程更透明，我建立了一个d3.js驱动的网络接口，它可以在学习过程中展示各种各样的有关agent的信息。我称之为强化学习控制中心。在这篇博客里，我会用它来提供一些有关强化学习agent如何以及为什么等相关的信息。



# 控制中心接口（The Control Center Interface）

![](2.png)

>强化学习控制中心接口

控制中心是为了让用户可以实时追踪agent在学习如果解决一个任务的过程中的性能变化。在接口的左边，每一轮的长度还有各时间的回报都会被追踪以及动态更新。右边展示了一个简单训练轮的动画gif，还有一轮中每一步的优势以及值函数的计算结果。

这个接口目前只适配我的博客中所描述的神经网络和任务。它是一个**双子竞争DQN(Double-Dueling-DQN)**，环境则是一个简单的网格世界。网格世界的规则如下：agent的目标是尽快地到达绿色方块，过程中要避免红色方块。绿色方块提供+1的回报，红色方块提供-1的回报。每一步都有-0.1的回报。在每一轮开始的时候，三个方格被随机放到网格上。

<div style='position:relative; padding-bottom:94%'><iframe src='https://gfycat.com/ifr/MajorCoordinatedGoldfish?referrer=https%3A%2F%2Fmedium.com%2Fmedia%2F583c3de27949a283ed0cb6b28b8500b9%3FpostId%3D4f27b134bb2a' frameborder='0' scrolling='no' width='100%' height='100%' style='position:absolute;top:0;left:0;' allowfullscreen></iframe></div>

Display of a neural agent’s actions and thoughts during an episode of training.
The DD-DQN neural agent processes two separate streams of information as it experiences the gridworld: an advantage stream and a value stream. The advantage stream represent how good the network thinks it is to take each action, given the current state it is in. The value stream represents how good the network thinks it is to be in a given state, regardless of possible action. With the Control Center, we can watch as the network learns to correctly predict the value of its state and actions over time. As the training process proceeds, it goes from seemingly random values to accurately interpreting certain actions as the most advantageous. We can think of this visualization as providing a portal into the “thought process” of our agent. Does it know that it is in a good position when it is in a good position? Does it know that going down was a good thing to do when it went down? This can give us the insights needed to understand why our agent might not be performing ideally as we train it under different circumstances in different environments.

Getting Inside Our Agent’s Head
Not only can we use the interface to explore how the agent does during training, we can also use it for testing and debugging our fully trained agents. For example, after training our agent to solve the simple 3x3 gridworld described above, we can provide it with some special test scenarios it had never encountered during the training process to evaluate whether it really is representing experience as we would expect it to.

Below is an example of the agent performing a modified version of the task with only green squares. As you can see, as the agent gets closer to the green squares the value estimate increases just as we would expect. It also has high estimates of the advantage for taking actions that get it closer to the green goals.


For the next test we can invert the situation, giving the agent a world in which there were only two red squares. It didn’t like this very much. As you can see below, the agent attempts to stay away from either square, resulting in behavior where it goes back and forth for a long period of time. Notice how the value estimate decreases as the agent approaches the red squares.


Finally, I provided the agent with a bit of an existential challenge. Instead of augmenting the kind of goals present, I removed them all. In this scenario, the blue square is by itself in the environment, with no other objects. Without a goal to move towards, the agent moves around seemingly at random, and the value estimates are likewise seemingly meaningless. What would Camus say?


Taken together, these three experiments provide us with evidence that our agent is indeed responding to the environment as we would intuitively expect. These kinds of checks are essential to make when designing any reinforcement learning agent. If we aren’t careful about the expectations we built into the agent itself and the reward structure of the environment, we can easily end up with situations where the agent doesn’t properly learn the task, or at least doesn’t learn it as we’d expect. In the gridworld for example, taking a step results in a -0.1 reward. This wasn’t always the case though. Originally there was no such penalty, and the agent would learn to move to the green square, but do so after an average of about 50 steps! It had no “reason” to hurry, to the goal, so it didn’t. By penalizing each step even a small amount, the agent is able to quickly learn the intuitive behavior of moving directly to the green goal. This reminds us of just how subconscious our own reward structures as humans often are. While we may explicitly only think of the green as being rewarding and the red as being punishing, we are subconsciously constraining our actions by a desire to finish quickly. When designing RL agents, we need ensure that we are making their reward structures as rich as ours.

Using the Control Center
If you want to play with a working version of the Control Center without training an agent yourself, just follow this link (currently requires Google Chrome). The agent’s performance you will see was pretrained on the gridworld task for 40,000 episodes. You can click the timeline on the left to look at an example episode from any point in training. The earlier episodes clearly show the agent failing to properly interpret the task, but by the end of training the agent almost always goes straight to the goal.

The Control Center is a piece of software I plan to continue to develop as I work more with various Reinforcement Learning algorithms. It is currently hard-coded to certain specifics of the gridworld and DD-DQN described in Part 4, but if you are interested in using the interface for your own projects, feel free to fork it on Github, and adjust/adapt it to your particular needs as you see fit. Hopefully it can provide new insights into the internal life of your learning algorithms too!







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