本文是对Arthur Juliani在Medium平台发布的强化学习系列教程的个人中文翻译，该翻译是基于个人分享知识的目的进行的，欢迎交流！（This article is my personal translation for the tutorial written and posted by Arthur Juliani on Medium.com. And my work is completely based on aim of sharing knowledges and welcome communicating!）

[原文地址（URL for original article）](https://medium.com/@awjuliani/simple-reinforcement-learning-with-tensorflow-part-3-model-based-rl-9a6fe0cce99)

***

[toc]

从本系列的上一篇博客算起，已经有一段时间没更新了。上篇博客讲的是如何设计一个策略梯度强化学习agent，它能解决CartPole任务。在本教程里，我将重新审视CartPole问题，但这一次，我会引入**环境模型**的概念，agent将可以利用这个环境模型来改善它的性能。

![](http://tech-blog-pictures.oss-cn-beijing.aliyuncs.com/2018/强化学习/强化学习之五：基于模型的强化学习/1.png)

什么是模型，以及为什么我们要用一个模型？在这个情境下，一个模型将会是一个神经网络，它会尝试去学习真实环境的动态（dynamics）。比如，在CartPole中，我们想要一个模型可以在考虑了之前的位置以及当时选择的行动后，预测Cart下一个位置。通过学习到一个精准的模型，我们可以训练我们的agent使用这个模型，而不是每次都要求真实的环境来给它反馈。这可能看起来不是那么有用，但是实际上环境模型可以带来巨大的优势，尤其是在尝试学习在物理世界里的行动策略时非常有用。

不像在计算机模拟中的样子，物理环境需要时间来摸清，而且世界的物理法则会避免出现像简单的环境重置这样不合理的事情出现。于是，我们可以通过建立环境模型来节省时间和精力。有了一个环境模型，一个agent可以**想象（imagine）**在真实环境中进行四处移动的感觉，并且我们可以在这个想象的环境中让agent也学会足够好的策略，就和能在真实世界中学到的一样。如果我们有了一个足够好的环境模型，agent就完全可以基于这个模型来进行训练，并且当把agent第一次放入真实环境中时，它也能表现得足够好。

那我们怎么用TensorFlow来实现环境模型呢？如我之前所提到的，我们将用一个神经网络来实现，它可以学习之前的观察和动作的组合，到所预期的新的观察与回报之间的迁移动态（transition dynamics）。我们的训练过程将包括在用真实环境来训练模型，和用模型环境来训练agent的策略之间不断切换。通过用这种方法，我们将有可能学习到一个策略，使我们的agent可以解决CartPole任务，而不需要实际在真实环境中进行训练。读一下下面的iPython notebook，看一下实现细节。

**源代码太长，就不在这里放了...**

[代码Github链接](https://github.com/awjuliani/DeepRL-Agents/blob/master/Model-Network.ipynb)


现在已经有两个神经网络了，还有很多超参数可以调，以使整体模型的性能和效率都能更高。我强烈推荐你去自己多尝试一下以发现更好地组装这些模型的方式。在Part 4，我将探索如何利用卷积神经网络来学习更复杂环境的表征，如Atari游戏。



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