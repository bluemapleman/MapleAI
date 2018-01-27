本文是对Tensorflow官方教程的个人（tomqianmaple@outlook.com）中文翻译，供大家学习参考。

[官方教程链接](https://www.tensorflow.org/get_started/get_started)

[toc]

# tf的扬帆起航（Getting Started With TensorFlow）

这个教程将帮助你开始用tf编程。在使用本教程之前，首先请安装好tf。为了能尽量顺畅地理解该教程，你应该具备以下能力：

- 会用Python编程
- 了解数组(array)的概念
- 最好你已经了解机器学习方面的知识。然而，如果你不知道也没关系，你仍然应该从读本教程开始。

tf提供了各种api。最底层的api--【tf核心】(Tensorflow Core)--提供了你完善的编程控制机制。我们认为机器学习研究者以及希望对模型有全面掌控的人都是用tf核心。而更高级别的API都基于tf核心所实现。这些高级的API一般都比tf核心更容易上手是用。此外，高级API也更易于在不同的用户之间去重复演示相同的任务而保证一致性。一种高级的API像tf.estimator可以帮助你管理数据集，estimators,训练以及推断。

这个教程从一个tf核心的指导开始。然后，我们将解释如何用tf.estimator实现相同的模型。了解了tf核心的原理后，你将清晰地理解更简单、更高级的API的背后工作原理。



# 张量（Tensors）

tf中的核心数据单位就是**张量（tensor）**。一个张量由一系列的原始值以一个任意维数组的形式组织而成。一个张量的秩即它的维度的数目。以下是一些张量的例子：

```
3 # a rank 0 tensor; a scalar with shape []
[1., 2., 3.] # a rank 1 tensor; a vector with shape [3]
[[1., 2., 3.], [4., 5., 6.]] # a rank 2 tensor; a matrix with shape [2, 3]
[[[1., 2., 3.]], [[7., 8., 9.]]] # a rank 3 tensor with shape [2, 1, 3]
```

# tf核心教程（TensorFlow Core tutorial）


## 导入tf（Importing TensorFlow）

tf项目的标准导入语句如下：

```
import tensorflow as tf
```

这使得Python可以直接使用tf的所有类、方法和符号。大多数的后续文档都会假设你已经完成了这一步导入工作。

## 计算图（The Computational Graph）

你可以会认为tf核心项目由以下两个单独的部分构成：

- 建立计算图（Building the computational graph.）
- 运行计算图（Running the computational graph.）

一个计算图就是一系列以图节点形式安排好的的tf操作。我们先来建立一个简单的计算图。每个节点接受0或多个张量作为输入，并产生一个张量作为输出。一种节点类型是constant（常量）。就像所有的tf常量，它不接受输入，并且它会输出一个它内部储存的值。我们可以创建两个tf浮点节点node1和node2：

```
node1 = tf.constant(3.0, dtype=tf.float32)
node2 = tf.constant(4.0) # also tf.float32 implicitly
print(node1, node2)
```

最后的声明语句会输出：

```
Tensor("Const:0", shape=(), dtype=float32) Tensor("Const_1:0", shape=(), dtype=float32)
```

要注意的是，节点可能并不会输出如你所预期的值3.0和4.0，而是被**评估（evaluated）**时才会分别输出3.0和4.0的节点的说明。而为了evaluate节点，我们必须在一个**会话（Session）**中运行计算图。一个会话封装了tf运行时的控制和状态。

接下来的代码创建了一个会话对象，并调用了它的运行方法以推进计算图的运行，继而评估node1和node2：

```
sess = tf.Session()
print(sess.run([node1, node2]))
we see the expected values of 3.0 and 4.0:
```
```
[3.0, 4.0]
```

我们可以通过结合更多的绑定了一些操作（操作（operation）也是一种节点）的tf节点以构造更复杂的计算图。比如，我们可以加上我们的两个常量节点并产生一个新的图：
```
from __future__ import print_function
node3 = tf.add(node1, node2)
print("node3:", node3)
print("sess.run(node3):", sess.run(node3))
```

最后两个print语句将输出：


```
node3: Tensor("Add:0", shape=(), dtype=float32)
sess.run(node3): 7.0
```

tf提供了一个工具TensorBoard用以展示计算图的样貌。这里是一个截屏以示范Tensorflow如何可视化计算图：

![](http://tech-blog-pictures.oss-cn-beijing.aliyuncs.com/2018/强化学习/强化学习之一：【趁手兵器】从TensorFlow开始/1.png)

这个图看起来似乎很简单，因为它总是只能产生一个常量结果。一个图可以被参数化以接受外部输入，这种图称为**placeholders**。一个placeholder是需要在创建后填充进数值的槽位：

```
a = tf.placeholder(tf.float32)
b = tf.placeholder(tf.float32)
adder_node = a + b  # + provides a shortcut for tf.add(a, b)
```

上面的三行代码有点像lambda函数，它定义了两个输入（a和b）并对它们进行了一个操作。我们可以用各种各样的输入来评估这个图，只要使用feed_dict参数并把它传入run方法以将具体值喂给placeholders即可：

```
print(sess.run(adder_node, {a: 3, b: 4.5}))
print(sess.run(adder_node, {a: [1, 3], b: [2, 4]}))
```


输入如下：

```
7.5
[ 3.  7.]
```

在TensorBoard中，计算图看起来像这样：

![](http://tech-blog-pictures.oss-cn-beijing.aliyuncs.com/2018/强化学习/强化学习之一：【趁手兵器】从TensorFlow开始/2.png)

我们可以再加上另一个操作使计算图更复杂。示例如下：

```
add_and_triple = adder_node * 3.
print(sess.run(add_and_triple, {a: 3, b: 4.5}))
```

输出：

```
22.5
```

之前的计算图在TensorBoard中看起来如下：

![](http://tech-blog-pictures.oss-cn-beijing.aliyuncs.com/2018/强化学习/强化学习之一：【趁手兵器】从TensorFlow开始/3.png)

在机器学习中，我们通常都会想要一个可以接受任意输入的模型，比如像上面的那个例子。为了让模型可以训练，我们还需要能够调整修改计算图，以在相同的输入上能够产生新的输出。**Variables（变量）**允许我们在图中加上可训练的参数。它们由类型和初始值两部分定义：

```
W = tf.Variable([.3], dtype=tf.float32)
b = tf.Variable([-.3], dtype=tf.float32)
x = tf.placeholder(tf.float32)
linear_model = W*x + b
```

Constants在你调用tf.constant时就已经完成初始化，并且它们的值不会变。相反，variable在你调用tf.Variable时尚未初始化。为了在tf程序中初始化所有的variables，你必须显示地调用一个特别操作：

```
init = tf.global_variables_initializer()
sess.run(init)
```

要理解init对于tf的子图（sub-graph）来说，就是一种用以初始化所有全局variable的工具。在我们调用sess.run之前，所有的variable都是还没有初始化的。

因为x是一个placeholder，我们可以同时用多个值来评估linear_model：

```
print(sess.run(linear_model, {x: [1, 2, 3, 4]}))
```

输出：
```
[ 0.          0.30000001  0.60000002  0.90000004]
```

我们已经创建了一个模型，但是我们还不知道它能工作得多好。为了在训练数据上评估这个模型，我们需要一个y placeholder来提供所期望的输出值，并且我们需要写一个损失函数：

损失函数衡量了当前模型对于给定输入的输出与期望输出之间的差异度。我们将用一个线性回归的标准损失模型，它会加总所有的模型输出与期望输出的差值的平方。linear_model -y 创造一个向量，向量的每个分量都是相应的样例的误差差值。我们调用tf.square来平方化误差项。然后，我们用tf.reduce_sum加总所有的平方误差来构造一个标量，它集聚了所有样例的误差：

```
y = tf.placeholder(tf.float32)
squared_deltas = tf.square(linear_model - y)
loss = tf.reduce_sum(squared_deltas)
print(sess.run(loss, {x: [1, 2, 3, 4], y: [0, -1, -2, -3]}))
```

输出损失值：
```
23.66
```

我们可以改进一下这个过程，比如重新指定W和b的值为1和-1。一个variable会被初始化为调用构造函数tf.Variable时传入的值，但也可以用tf.assign这样的操作来改变其值。比如，假设W=-1和b=1是我们模型的最优参数，我们就可以对W和b的值进行相应地改变：
```
fixW = tf.assign(W, [-1.])
fixb = tf.assign(b, [1.])
sess.run([fixW, fixb])
print(sess.run(loss, {x: [1, 2, 3, 4], y: [0, -1, -2, -3]}))
```

现在，输出的损失值就变成了0：
```
0.0
```

我们是通过猜得到的W和b的“完美”值，但是机器学习的核心目标就是自动找到正确的模型参数。我们将在接下来展示如何实现这一点。

## tf模型训练api（tf.train API）

对于机器学习知识的完整介绍不在本教程的覆盖范围内。然而，tf提供了优化器（optimizer），它可以逐渐改变variable的值以使损失函数的值最小化。最简单的优化器就是梯度下降（Gradient Descent）。它根据损失函数对每个variable的导数的大小来调整每个variable的值。总体来说，手工计算符号导数是很困难并且容易出错的。而tf则可以根据所给定的对模型的描述自动产生相应导数，只要调用函数tf.gradients即可。更简单而言，优化器本身可以为你做这件事。举例来说：

```
optimizer = tf.train.GradientDescentOptimizer(0.01)
train = optimizer.minimize(loss)
sess.run(init) # reset values to incorrect defaults.
for i in range(1000):
  sess.run(train, {x: [1, 2, 3, 4], y: [0, -1, -2, -3]})

print(sess.run([W, b]))
```

最后模型的参数结果：
```
[array([-0.9999969], dtype=float32), array([ 0.99999082], dtype=float32)]
```

现在我们就是在做实实在在的机器学习！尽管这个简单的线性回归模型不要很多的tf核心代码，但是为了给模型提供更复杂的数据，你必须用更多代码来实现和调用更复杂的模型和方法。因此，tf提供了公共模式、结构以及功能的高级抽象。我们将在下一节学习这些抽象。



## 完整的程序（Complete program）

完整的可训练线性回归模型如下所示：

```

import tensorflow as tf

# Model parameters
W = tf.Variable([.3], dtype=tf.float32)
b = tf.Variable([-.3], dtype=tf.float32)
# Model input and output
x = tf.placeholder(tf.float32)
linear_model = W*x + b
y = tf.placeholder(tf.float32)

# loss
loss = tf.reduce_sum(tf.square(linear_model - y)) # sum of the squares
# optimizer
optimizer = tf.train.GradientDescentOptimizer(0.01)
train = optimizer.minimize(loss)

# training data
x_train = [1, 2, 3, 4]
y_train = [0, -1, -2, -3]
# training loop
init = tf.global_variables_initializer()
sess = tf.Session()
sess.run(init) # reset values to wrong
for i in range(1000):
  sess.run(train, {x: x_train, y: y_train})

# evaluate training accuracy
curr_W, curr_b, curr_loss = sess.run([W, b, loss], {x: x_train, y: y_train})
print("W: %s b: %s loss: %s"%(curr_W, curr_b, curr_loss))
```


运行完后输出：
```
W: [-0.9999969] b: [ 0.99999082] loss: 5.69997e-11
```

注意损失值是非常小的数（非常接近0）。如果你运行这个程序，你的损失值可能和之前的不一样，因为模型是用伪随机数值初始化的。

这个更复杂的程序也可以在TensorBoard中可视化：

![](http://tech-blog-pictures.oss-cn-beijing.aliyuncs.com/2018/强化学习/强化学习之一：【趁手兵器】从TensorFlow开始/4.png)

# tf.estimator

tf.estimator是一个高级的tf框架，它可以简化机器学习的机制，它包括以下部分：

- 执行训练循环（running training loops）
- 运行评估循环（running evaluation loops）
- 管理数据集（managing data sets）

tf.estimator定义了很多公共模型：

## 基本使用（Basic usage）

注意我们之前的简单线性回归程序在使用tf.estimator后变得多么简单：
```
# NumPy is often used to load, manipulate and preprocess data.
# NumPy总是用来加载、操作和预处理数据
import numpy as np
import tensorflow as tf

# Declare list of features. We only have one numeric feature. There are many
# other types of columns that are more complicated and useful.
# 声明特征列表。我们只有一个数值特征，还有很多其他类型的列，它们更复杂也更有用。
feature_columns = [tf.feature_column.numeric_column("x", shape=[1])]

# An estimator is the front end to invoke training (fitting) and evaluation
# (inference). There are many predefined types like linear regression,
# linear classification, and many neural network classifiers and regressors.
# The following code provides an estimator that does linear regression.
# 一个estimator是调用训练（拟合）和评估方法的前端（接口）。有很多预定义的类型像线性回归、线性分类，还有很多神经网络分类器和回归器。下面的代码提供了一个做线性回归的estimator。
estimator = tf.estimator.LinearRegressor(feature_columns=feature_columns)

# TensorFlow provides many helper methods to read and set up data sets.
# Here we use two data sets: one for training and one for evaluation
# We have to tell the function how many batches
# of data (num_epochs) we want and how big each batch should be.
# tf提供了很多帮助函数供阅读和设置数据集。这里我们用到两个数据集：一个用以训练，一个用以评估。我们需要告诉函数我们将用多少batches的数据(num_epochs)，以及每个batch的大小。
x_train = np.array([1., 2., 3., 4.])
y_train = np.array([0., -1., -2., -3.])
x_eval = np.array([2., 5., 8., 1.])
y_eval = np.array([-1.01, -4.1, -7, 0.])
input_fn = tf.estimator.inputs.numpy_input_fn(
    {"x": x_train}, y_train, batch_size=4, num_epochs=None, shuffle=True)
train_input_fn = tf.estimator.inputs.numpy_input_fn(
    {"x": x_train}, y_train, batch_size=4, num_epochs=1000, shuffle=False)
eval_input_fn = tf.estimator.inputs.numpy_input_fn(
    {"x": x_eval}, y_eval, batch_size=4, num_epochs=1000, shuffle=False)


# We can invoke 1000 training steps by invoking the  method and passing the
# training data set.
# 我们可以触发1000次训练步骤通过调用方法并传入训练数据集。
estimator.train(input_fn=input_fn, steps=1000)

# Here we evaluate how well our model did.
# 评估我们的模型性能
train_metrics = estimator.evaluate(input_fn=train_input_fn)
eval_metrics = estimator.evaluate(input_fn=eval_input_fn)
print("train metrics: %r"% train_metrics)
print("eval metrics: %r"% eval_metrics)
```

运行后输出：

```
train metrics: {'average_loss': 1.4833182e-08, 'global_step': 1000, 'loss': 5.9332727e-08}
eval metrics: {'average_loss': 0.0025353201, 'global_step': 1000, 'loss': 0.01014128}
```

注意我们的评估数据的损失值相对训练集数据的损失值更高，但是也很接近0了，这表示我们的模型学的不错。


## 一个自定义模型（A custom model）

tf.estimator并不会局限你只使用预定义模型。假设我们想创造一个tf中没有的自定义模型，我们仍然可以保持对数据集、喂数据、训练等过程的高度抽象。为了解释这一点，我们将展示如何用低阶tf API来实现我们的线性回归的等价模型。

要定义一个可以和tf.estimator协作的自定义模型，我们需要使用tf.estimator.Estimator。tf.estimator.LinearRegressor就是一个tf.estimator.Estimator的子类。相比于继承Estimator，我们只是提供Estimator一个函数model_fn以告诉tf.estimator它如何评估预测值、训练步骤和损失。代码如下所示：

```
import numpy as np
import tensorflow as tf

# Declare list of features, we only have one real-valued feature
# 声明特征列表，我们只有一个实值特征
def model_fn(features, labels, mode):
  # Build a linear model and predict values
  # 建立一个线性模型并预测值
  W = tf.get_variable("W", [1], dtype=tf.float64)
  b = tf.get_variable("b", [1], dtype=tf.float64)
  y = W*features['x'] + b
  # Loss sub-graph
  # 损失子图
  loss = tf.reduce_sum(tf.square(y - labels))
  # Training sub-graph
  # 训练子图
  global_step = tf.train.get_global_step()
  optimizer = tf.train.GradientDescentOptimizer(0.01)
  train = tf.group(optimizer.minimize(loss),
                   tf.assign_add(global_step, 1))
  # EstimatorSpec connects subgraphs we built to the
  # appropriate functionality.
  # EstimatorSpec将我们建立的子图连接到合适的功能上
  return tf.estimator.EstimatorSpec(
      mode=mode,
      predictions=y,
      loss=loss,
      train_op=train)

estimator = tf.estimator.Estimator(model_fn=model_fn)
# define our data sets
# 定义数据集
x_train = np.array([1., 2., 3., 4.])
y_train = np.array([0., -1., -2., -3.])
x_eval = np.array([2., 5., 8., 1.])
y_eval = np.array([-1.01, -4.1, -7., 0.])
input_fn = tf.estimator.inputs.numpy_input_fn(
    {"x": x_train}, y_train, batch_size=4, num_epochs=None, shuffle=True)
train_input_fn = tf.estimator.inputs.numpy_input_fn(
    {"x": x_train}, y_train, batch_size=4, num_epochs=1000, shuffle=False)
eval_input_fn = tf.estimator.inputs.numpy_input_fn(
    {"x": x_eval}, y_eval, batch_size=4, num_epochs=1000, shuffle=False)

# train
# 训练
estimator.train(input_fn=input_fn, steps=1000)
# Here we evaluate how well our model did.
# 评估模型性能
train_metrics = estimator.evaluate(input_fn=train_input_fn)
eval_metrics = estimator.evaluate(input_fn=eval_input_fn)
print("train metrics: %r"% train_metrics)
print("eval metrics: %r"% eval_metrics)
When run, it produces

train metrics: {'loss': 1.227995e-11, 'global_step': 1000}
eval metrics: {'loss': 0.01010036, 'global_step': 1000}
```

注意到我们自定义的model_fn()函数的内容非常近似于我们用低阶API实现的手动模型训练部分。

# 下一步（Next steps）

现在你已经了解了tf的基本运作方式。我们还有一些教程你可以继续参考学习。如果你是一个机器学习的新手，可以看一下MNIST的新手教程，不然你可以看为专业人士准备的深度MNIST教程。
