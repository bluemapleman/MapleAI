[toc]

[Keras官方网站](https://keras.io/)

# Introduction

Keras是一个**高级的神经网络API**，用Python实现，并可以基于TensorFlow，CNTK与Theano等计算框架运行。

Keras的核心是神经网络，它的意义主要在于**使得神经网络的实现更加方便快捷**，因此它本质上是在一些知名的计算框架上进行了一层简化的封装，只对Keras使用者暴露出一些简单易用的接口，使用者可以很快了解并上手实现复杂的神经网络架构，而不用关心底层的实现细节。

Keras作为一个深度学习的库，有以下显著特征：

- 简单、快速地构造原型（兼具用户友好性、模块性以及可扩展性）
- 支持卷积网路和循环网络，包括二者的结合体
- 可以无缝在CPU和GPU上运行

# Installation

首先需要选择Keras的底层框架：TensorFlow，CNTK或Theano。（鉴于Bengio已经宣布将停止继续维护Theano，故推荐使用Google的TensorFlow），并进行安装，然后再安装Keras的库。另外，Keras默认以TensorFlow作为底层计算框架，如果使用CNTK或者Theano的话，则需要在Keras的配置文件中[进行修改](https://keras.io/backend/)。

具体参考[官方说明](https://keras.io/#installation)

# Fast Overview

我们知道，神经网络中最基本的构成单元是神经元（neuron），而若干神经元可以组成一个层（layer），若干层（输入层+隐藏层+输出层）就构成了一个神经网络的原型。而Keras中最核心的数据结构就是**model**，我们便是基于model来进行神经网络层（layers）的组装。而model最简单的一种类型便是**Sequential**，它对层进行线性堆叠。

通过以下代码便能实例化一个Sequential：

```
from keras.models import Sequential

model = Sequential()
```

而要往Sequential上面叠加层，只需使用.add()方法:

```
from keras.layers import Dense

model.add(Dense(units=64, activation='relu', input_dim=100))
model.add(Dense(units=10, activation='softmax'))
```

如上是先后加了两层。第一层是Dense层（全连接层），共64个神经元（units=64），激活函数为ReLU（activation='relu'），输入的是维度为1\*100的列向量（input_dim=100）。第二层是也是一个Dense层，10个神经元，激活函数为softmax，输入的是前一层的输出向量，即维度为1\*64的列向量。

第一层默认为神经网络的隐藏层第一层，故需要指定输入向量的维度，即输入的特征向量的维度。

Once your model looks good, configure its learning process with .compile():

```
model.compile(loss='categorical_crossentropy',
              optimizer='sgd',
              metrics=['accuracy'])
```

有需要的话，我们也可以自定义优化器（optimizer）。Keras最核心的设计理念就是在最大化保证易用性的同时，提供给使用者充分的自由去对模型进行全面地控制。

```
model.compile(loss=keras.losses.categorical_crossentropy,
              optimizer=keras.optimizers.SGD(lr=0.01, momentum=0.9, nesterov=True))
```

这里，我们的损失函数选择的是交叉熵（loss=keras.losses.categorical_crossentropy），优化器选择的是学习率为0.01，动量为0.9的随机梯度下降（optimizer=keras.optimizers.SGD(lr=0.01, momentum=0.9），并启用Nesterov动量（不同的优化方法可参考[这里](http://blog.csdn.net/luo123n/article/details/48239963)）。


现在我们就可以以batch的形式来迭代训练我们的模型了:

```
# x_train and y_train are Numpy arrays --just like in the Scikit-Learn API.

model.fit(x_train, y_train, epochs=5, batch_size=32)
```

我们也可以手动地把batch分批喂给模型训练：

```
model.train_on_batch(x_batch, y_batch)
```

一行代码便能获得训练好的模型的性能评估：

```
loss_and_metrics = model.evaluate(x_test, y_test, batch_size=128)
```

让模型对新的数据进行预测：

```
classes = model.predict(x_test, batch_size=128)
```

> 无论是想建立一个问题回答系统，一个图像分类模型，一个神经图灵机，还是任何机器模型，都可以尽可能快。这些深度学习背后的思想都很简单，所以为什么它们的实现过程要那么痛苦呢？这就是存在的意义。
> 

# Sequential model

序列模型（Sequential model）是对**神经层的堆叠**，而要构建一个序列模型也和容易，通过将List形式组织的layer实例给序列类的构造器即可：

```
from keras.models import Sequential
from keras.layers import Dense, Activation

model = Sequential([
    Dense(32, input_shape=(784,)),
    Activation('relu'),
    Dense(10),
    Activation('softmax'),
])
```

也可以用.add()方法来仅仅加上一层：

```
model = Sequential()
model.add(Dense(32, input_dim=784))
model.add(Activation('relu'))
```

## Specifying the Input Shape

序贯模型需要知道所预期给它的输入的形状（shape），而也只有模型的第一层需要手动指明input_shape（后面的层会自己进行形状推断）。

对于Dense这样的2D层，也可以用参数input_dim来直接声明input shape，而像一些3D层就同时支持input_dim和input_length参数。

而如果我们需要声明一个固定大小的batch的输入（这在状态循环网络会用到），我们可以传递参数batch_size给某个层。如果我们同时传递了batch_size=32和input_shape=(6,8)给某个层，那么该层就会预期之后每一次传入的batch输入都具备batch形状(32,6,8)。

如下，两种方式是等价的：

```
model = Sequential()
model.add(Dense(32, input_shape=(784,)))
```
```
model = Sequential()
model.add(Dense(32, input_dim=784))
```

## Compilation

在训练一个模型前，我们需要配置它的学习过程，这通过方法compile来完成。compile方法接受三个参数：

- 一个优化器（optimizer）：用字符串形式指定一个keras已有的优化器名称即可（比如rmsprop或者adagrad），或者传递一个Optimizer类的实例也可以。（参见[optimizers](https://keras.io/optimizers)）
- 一个损失函数（loss function）：这是模型将会尽力去最小化的目标。它也可以是字符串形式指定的keras中已有的损失函数类型（比如交叉熵（categorical_crossentropy）或者最小均方误差(mse)），也可以直接是目标方法名称。（参见[losses](https://keras.io/losses)）
- 一个指标列表(a list of metrics)：对任意分类问题，其指标都应该是metrics=['accuracy']。一个指标可以是字符串形式指定的已存在的一种指标，也可以是自定义的指标计算函数。

下面是一些示例：

``` 
# For a multi-class classification problem 多分类问题
model.compile(optimizer='rmsprop',
              loss='categorical_crossentropy',
              metrics=['accuracy'])

# For a binary classification problem 二分类问题
model.compile(optimizer='rmsprop',
              loss='binary_crossentropy',
              metrics=['accuracy'])

# For a mean squared error regression problem 以mse为损失函数的回归
model.compile(optimizer='rmsprop',
              loss='mse')

# For custom metrics 自定义指标
import keras.backend as K

def mean_pred(y_true, y_pred):
    return K.mean(y_pred)

model.compile(optimizer='rmsprop',
              loss='binary_crossentropy',
              metrics=['accuracy', mean_pred])
```

## Training

keras中的模型要求训练数据以及相应的标签以Numpy中的arrays类型的方式来组织。

一般用fit()函数来训练一个模型：

```

# For a single-input model with 2 classes (binary classification):

model = Sequential()
model.add(Dense(32, activation='relu', input_dim=100))
model.add(Dense(1, activation='sigmoid'))
model.compile(optimizer='rmsprop',
              loss='binary_crossentropy',
              metrics=['accuracy'])

# Generate dummy data
import numpy as np
data = np.random.random((1000, 100))
labels = np.random.randint(2, size=(1000, 1))

# Train the model, iterating on the data in batches of 32 samples
model.fit(data, labels, epochs=10, batch_size=32)
```


```
# For a single-input model with 10 classes (categorical classification):

model = Sequential()
model.add(Dense(32, activation='relu', input_dim=100))
model.add(Dense(10, activation='softmax'))
model.compile(optimizer='rmsprop',
              loss='categorical_crossentropy',
              metrics=['accuracy'])

# Generate dummy data
import numpy as np
data = np.random.random((1000, 100))
labels = np.random.randint(10, size=(1000, 1))

# Convert labels to categorical one-hot encoding
one_hot_labels = keras.utils.to_categorical(labels, num_classes=10)

# Train the model, iterating on the data in batches of 32 samples
model.fit(data, one_hot_labels, epochs=10, batch_size=32)

```

## Examples

keras提供了许多参考的[示例](https://github.com/fchollet/keras/tree/master/examples),我们可以在开始动手搭建自己的网络前先看一下这些范例。

### Example 1: minist_mlp (A simple deep multi-layer perceptron on the MNIST dataset)

```
'''Trains a simple deep NN on the MNIST dataset.
Gets to 98.40% test accuracy after 20 epochs
(there is *a lot* of margin for parameter tuning).
2 seconds per epoch on a K520 GPU.
'''

from __future__ import print_function

import keras
# keras有一个datasets模块，自带了许多经典数据集，包括mnist
from keras.datasets import mnist
from keras.models import Sequential
from keras.layers import Dense, Dropout
from keras.optimizers import RMSprop


batch_size = 128  # batch的大小为128个样例
num_classes = 10  # 一共0-9是个数字，对应10个类别
epochs = 20  # 训练的epochs为20

# the data, shuffled and split between train and test sets
# 注意load_data()方法会首先看当前文件夹下有木有数据源，如果没有，则去指定地址下载
(x_train, y_train), (x_test, y_test) = mnist.load_data()

# mnist的数据都是28*28=784维（像素）的灰度图像
x_train = x_train.reshape(60000, 784)
x_test = x_test.reshape(10000, 784)
x_train = x_train.astype('float32')
x_test = x_test.astype('float32')
# 将像素的灰度值（0-255）统一除以255以归一化，方便计算
x_train /= 255
x_test /= 255
print(x_train.shape[0], 'train samples')
print(x_test.shape[0], 'test samples')

# convert class vectors to binary class matrices
y_train = keras.utils.to_categorical(y_train, num_classes)
y_test = keras.utils.to_categorical(y_test, num_classes)

# 三层全连接层，前两层使用Dropout，最后一层是输出层
model = Sequential()
model.add(Dense(512, activation='relu', input_shape=(784,)))
model.add(Dropout(0.2))
model.add(Dense(512, activation='relu'))
model.add(Dropout(0.2))
model.add(Dense(num_classes, activation='softmax'))

model.summary()

model.compile(loss='categorical_crossentropy',
              optimizer=RMSprop(),
              metrics=['accuracy'])

history = model.fit(x_train, y_train,
                    batch_size=batch_size,
                    epochs=epochs,
                    verbose=1,
                    validation_data=(x_test, y_test))
score = model.evaluate(x_test, y_test, verbose=0)
print('Test loss:', score[0])
print('Test accuracy:', score[1])
```

>这里进行模型训练和评估时的verbose参数说一下：

>verbose的取值只能是0、1或2，表示模型训练或评估时的状况输出模式：0=不输出, 1=进度条, 2=每个epoch输出一行。


### Example 2: Simple Convolutional Neural Network (convnet) on the MNIST dataset

```
'''Trains a simple convnet on the MNIST dataset.
Gets to 99.25% test accuracy after 12 epochs
(there is still a lot of margin for parameter tuning).
16 seconds per epoch on a GRID K520 GPU.
'''

from __future__ import print_function
import keras
from keras.datasets import mnist
from keras.models import Sequential
from keras.layers import Dense, Dropout, Flatten
from keras.layers import Conv2D, MaxPooling2D
from keras import backend as K

batch_size = 128
num_classes = 10
epochs = 12

# input image dimensions
img_rows, img_cols = 28, 28

# the data, shuffled and split between train and test sets
(x_train, y_train), (x_test, y_test) = mnist.load_data()

if K.image_data_format() == 'channels_first':
    x_train = x_train.reshape(x_train.shape[0], 1, img_rows, img_cols)
    x_test = x_test.reshape(x_test.shape[0], 1, img_rows, img_cols)
    input_shape = (1, img_rows, img_cols)
else:
    x_train = x_train.reshape(x_train.shape[0], img_rows, img_cols, 1)
    x_test = x_test.reshape(x_test.shape[0], img_rows, img_cols, 1)
    input_shape = (img_rows, img_cols, 1)

x_train = x_train.astype('float32')
x_test = x_test.astype('float32')
x_train /= 255
x_test /= 255
print('x_train shape:', x_train.shape)
print(x_train.shape[0], 'train samples')
print(x_test.shape[0], 'test samples')

# convert class vectors to binary class matrices
y_train = keras.utils.to_categorical(y_train, num_classes)
y_test = keras.utils.to_categorical(y_test, num_classes)


# 一层卷积，32个3*3的过滤器
# 一层最大池化层
model = Sequential()
model.add(Conv2D(32, kernel_size=(3, 3),
                 activation='relu',
                 input_shape=input_shape))
model.add(Conv2D(64, (3, 3), activation='relu'))
model.add(MaxPooling2D(pool_size=(2, 2)))
model.add(Dropout(0.25))
model.add(Flatten())
model.add(Dense(128, activation='relu'))
model.add(Dropout(0.5))
model.add(Dense(num_classes, activation='softmax'))

model.compile(loss=keras.losses.categorical_crossentropy,
              optimizer=keras.optimizers.Adadelta(),
              metrics=['accuracy'])

model.fit(x_train, y_train,
          batch_size=batch_size,
          epochs=epochs,
          verbose=1,
          validation_data=(x_test, y_test))
score = model.evaluate(x_test, y_test, verbose=0)
print('Test loss:', score[0])
print('Test accuracy:', score[1])
```

