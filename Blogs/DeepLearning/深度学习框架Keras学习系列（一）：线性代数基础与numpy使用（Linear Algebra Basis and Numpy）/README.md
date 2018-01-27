
  又开一个新坑~~

  因为确实很有必要好好地趁着这个热潮来研究一下深度学习，毕竟现在深度学习因为其效果突出，热潮保持高涨不退，上面的政策方面现在也在向人工智能领域倾斜，但是也有无数一知半解的人跟风吹捧，于是希望借此教程，让自己和读者一起借助keras，从上到下逐渐摸清楚深度学习领域的相关知识，包括它的前世今生，它的使用方法，它的应用领域等等。

  该系列教程各部分链接：

  [深度学习框架Keras学习系列（一）：线性代数基础与numpy使用](http://blog.csdn.net/qq_32690999/article/details/78594220)
  [深度学习框架Keras学习系列（二）：神经网络与BP算法]()
  [深度学习框架Keras学习系列（三）：深度学习概念初探]()
<br><br><br><br><br>


另外，请先安装好python的jupyter notebook工具，后面的代码结果演示都将是基于jupyter notebook的，这样方便大家可以跟着运行程序看效果~~


[toc]


# 线性代数基础

## 向量与矩阵

这个请看这篇博客[OpenGL学习脚印: 向量和矩阵要点(math-vector and matrices)](http://blog.csdn.net/wangdingqiaoit/article/details/51383052)

重点在于了解向量与矩阵的基本概念，以及向量和矩阵的加减乘除运算规则。并且理解向量就是一种特殊的矩阵。

## 张量（Tensor）

这个请看这篇博客[tensorflow中张量的理解](http://blog.csdn.net/pandamax/article/details/63684633)

简而言之，张量是线性代数中的一种概念，它可以被理解为一个n维数组，它的描述单位是阶。我们规定，0阶的张量是标量（scalar，如1，4，23这样的数字），1阶张量是向量（vector，如[1,2]），2阶张量是矩阵（matrix，如[[1,2,3],[2,3,4]]），三阶张量[[[1,2],[3,4]],[[5,6],[7,8]]]，以此类推。所以，张量实际是对数的表示的一种推广。

之所以要理解张量，是因为张量是tensorflow这个人工智能框架的基本元素，而keras实际上是在tensorflow与Theano（另一个相似框架，[已经被维护者宣布不再继续支持](http://baijiahao.baidu.com/s?id=1579858971719279005&wfr=spider&for=pc)）之上做了一层封装，使得我们可以很简单地通过keras的接口去建模，因此，当后面要了解人工智能算法的原理时，是绕不开对于tensorflow的理解的，也就绕不开对其核心计算元素张量的理解。（目前，我个人对为什么tensorflow要用张量作为运算元素的一个动机理解是，张量用于描述模型的输入特征值时，是非常合适的）。




# Numpy

## 为什么用Numpy

     Numpy是python中的一款高性能科学计算和数据分析的基础包，是Python的一种开源的数值计算扩展。这种工具可用来存储和处理大型矩阵，比Python自身的嵌套列表（nested list structure)结构要高效的多（该结构也可以用来表示矩阵（matrix））。据说NumPy将Python相当于变成一种免费的更强大的MatLab系统。
    
    其内部工具包括：包括：1、一个强大的N维数组对象Array；2、比较成熟的（广播）函数库；3、用于整合C/C++和Fortran代码的工具包；4、实用的线性代数、傅里叶变换和随机数生成函数。numpy和稀疏矩阵运算包scipy配合使用更加方便。
    
    NumPy（Numeric Python）提供了许多高级的数值编程工具，如：矩阵数据类型、矢量处理，以及精密的运算库。专为进行严格的数字处理而产生。多为很多大型金融公司使用，以及核心的科学计算组织如：Lawrence Livermore，NASA用其处理一些本来使用C++，Fortran或Matlab等所做的任务。

  因为深度学习的运算中会涉及大量线性代数的运算，即向量与矩阵相关的一些运算，而Numpy中封装好了许多高效的线性代数运算方法，我们只需调用即可，多么方便。

## Numpy的使用

一般来说，python中约定俗成的引入numpy的方式是：

```
  import numpy as np
```

之后调用的时候，我们用np.方法名()就ok。

下面，我们从numpy中最常用的一些类来展开描述。

### 多维数组：ndarray

参考[Quickstart tutorial](https://docs.scipy.org/doc/numpy-dev/user/quickstart.html)

  ndarray是numpy中数组的类，它是numpy最主要的一个构成要素（也被称为数组(array)），其本质是元素同质的多维数组，也可说是同类元素的一张表（一般元素是数字），索引任一元素的方式是通过一个元组来进行。而在numpy中，维度被称为“axes（轴）”，轴的数量成为“rank（阶）”。

比如说，一个3d空间中的点的坐标为[1,2,1]是一个阶为1的数组，因为它只有一个轴，而这个轴的长度为3. 而[[1,0,0],[0,1,2]]是一个二阶（2维的）的数组，它第一个维度（轴）的长度为2，第二个维度（轴）的长度为3.

- ndarray的常用属性

  - ndim：数组的轴（维度）的数量，即阶。
  - shape：数组的维度。是一个表示数组在每个维度上的尺寸的元组。
  - size：数组中的元素的总数量。
  - dtype：描述数组元素类型的一个对象。
  - itemsize：数组元素的大小（以字节为单位）。
  - data：一个包含数组元素的缓冲区。

- 举例

```
>>> import numpy as np
>>> a = np.arange(15).reshape(3, 5)
>>> a
array([[ 0,  1,  2,  3,  4],
       [ 5,  6,  7,  8,  9],
       [10, 11, 12, 13, 14]])
>>> a.shape
(3, 5)
>>> a.ndim
2
>>> a.dtype.name
'int64'
>>> a.itemsize
8
>>> a.size
15
>>> type(a)
<type 'numpy.ndarray'>
>>> b = np.array([6, 7, 8])
>>> b
array([6, 7, 8])
>>> type(b)
<type 'numpy.ndarray'>
```

- Array的创建方法

1. 用python的list作为参数传入numpy的array的构造函数中：

```
 >>> import numpy as np
>>> a = np.array([2,3,4])
>>> a
array([2, 3, 4])
```

这种方法常见的一种错误是错传成了多个数字参数，而不是list：

```
>>> a = np.array(1,2,3,4)    # WRONG
>>> a = np.array([1,2,3,4])  # RIGHT
```

而如果要创建多维的数组，则需要传入多层嵌套的序列（suquence），因为array方法会将序列的序列转换成二维数组，而将序列的序列的序列转换为三围数组，以此类推。

```
>>> b = np.array([(1.5,2,3), (4,5,6)])
>>> b
array([[ 1.5,  2. ,  3. ],
       [ 4. ,  5. ,  6. ]])
```

另外，数组元素的类型是可以在创建时明确声明的：
```
>>> c = np.array( [ [1,2], [3,4] ], dtype=complex )
>>> c
array([[ 1.+0.j,  2.+0.j],
       [ 3.+0.j,  4.+0.j]])
```

2. numpy的zeros(),ones(),empty()方法

在很多时候创建数组时，我们可能并不知道数组的具体数值，于是我们可以先用一些随机值代替，这时，numpy内置的一些函数就可以发挥作用了。

zero（）函数的默认元素是0，ones（）函数的默认值是1，empty（）函数的默认值是随机化的值。它们所需传入的参数都是一个元组，元组的元素是数组各个轴的长度。

```
>>> np.zeros( (3,4) )
array([[ 0.,  0.,  0.,  0.],
       [ 0.,  0.,  0.,  0.],
       [ 0.,  0.,  0.,  0.]])
>>> np.ones( (2,3,4), dtype=np.int16 )                # dtype can also be specified
array([[[ 1, 1, 1, 1],
        [ 1, 1, 1, 1],
        [ 1, 1, 1, 1]],
       [[ 1, 1, 1, 1],
        [ 1, 1, 1, 1],
        [ 1, 1, 1, 1]]], dtype=int16)
>>> np.empty( (2,3) )                                 # uninitialized, output may vary
array([[  3.73603959e-262,   6.02658058e-154,   6.55490914e-260],
       [  5.30498948e-313,   3.14673309e-307,   1.00000000e+000]])
```

3. numpy的arange()与linspace()

arange（）函数类似于python内置的range（）函数。分别传入起始值，终止值还有步长，就可以返回一个从起始值按照步长生成的数组。（如果不写第一个起始值参数，只写一个终止值，则默认起始值为0）
```
>>> np.arange( 10, 30, 5 )
array([10, 15, 20, 25])
>>> np.arange( 0, 2, 0.3 )                 # it accepts float arguments
array([ 0. ,  0.3,  0.6,  0.9,  1.2,  1.5,  1.8])
```

但是arange（）函数的一个缺点是，它无法准确确定生成的数组中所包含的元素的个数，因为它是自己依靠步长生成的，而linspace（）函数就可以明确制定元素数量。

```
>>> from numpy import pi
>>> np.linspace( 0, 2, 9 )                 # 9 numbers from 0 to 2
array([ 0.  ,  0.25,  0.5 ,  0.75,  1.  ,  1.25,  1.5 ,  1.75,  2.  ])
>>> x = np.linspace( 0, 2*pi, 100 )        # useful to evaluate function at lots of points
>>> f = np.sin(x)
```

- 基本操作

numpy内置的一些运算操作符可以对数组中的元素逐个进行处理，并返回一个新的数组对象用以存储处理后的数组，包括矩阵的加减法，乘方，乘数还有判断：

```
>>> a = np.array( [20,30,40,50] )
>>> b = np.arange( 4 )
>>> b
array([0, 1, 2, 3])
>>> c = a-b
>>> c
array([20, 29, 38, 47])
>>> b**2
array([0, 1, 4, 9])
>>> 10*np.sin(a)
array([ 9.12945251, -9.88031624,  7.4511316 , -2.62374854])
>>> a<35
array([ True, True, False, False], dtype=bool)
```

numpy中的*运算符是对矩阵元素逐个进行运算的（elementwise），而如果要得到矩阵之间的乘积，是需要用dot（）函数来获得的，可以是矩阵A.dot(矩阵B)，也可以用np.dot(矩阵A，矩阵B)的方式，看下面的例子理解*运算符和dot（）函数之间的区别：

```
>>> A = np.array( [[1,1],
...             [0,1]] )
>>> B = np.array( [[2,0],
...             [3,4]] )
>>> A*B                         # elementwise product
array([[2, 0],
       [0, 4]])
>>> A.dot(B)                    # matrix product
array([[5, 4],
       [3, 4]])
>>> np.dot(A, B)                # another matrix product
array([[5, 4],
       [3, 4]])
```

还有一些一元的操作方法，比如计算所有数组元素的和，也被ndarray类实现了：

```
>>> a = np.random.random((2,3))
>>> a
array([[ 0.18626021,  0.34556073,  0.39676747],
       [ 0.53881673,  0.41919451,  0.6852195 ]])
>>> a.sum()
2.5718191614547998
>>> a.min()
0.1862602113776709
>>> a.max()
0.6852195003967595
```



这些一元方法默认将整个数组当成一个list中的数，而无所谓其shape。不过，我们可以通过axis轴参数来决定我们对数组的具体某个轴进行我们的统一操作：
```
>>> b = np.arange(12).reshape(3,4)
>>> b
array([[ 0,  1,  2,  3],
       [ 4,  5,  6,  7],
       [ 8,  9, 10, 11]])
>>>
>>> b.sum(axis=0)                            # sum of each column
array([12, 15, 18, 21])
>>>
>>> b.min(axis=1)                            # min of each row
array([0, 4, 8])
>>>
>>> b.cumsum(axis=1)                         # cumulative sum along each row
array([[ 0,  1,  3,  6],
       [ 4,  9, 15, 22],
       [ 8, 17, 27, 38]])
```


- 普遍函数（Universal Functions）

Numpy提供了一些数学函数如sin，cos，exp等，这类函数被称为“universal functions”（ufunc），这些函数也是对数组进行逐元素的处理（elementwise），并返回处理后的数组。

```
>>> B = np.arange(3)
>>> B
array([0, 1, 2])
>>> np.exp(B)
array([ 1.        ,  2.71828183,  7.3890561 ])
>>> np.sqrt(B)
array([ 0.        ,  1.        ,  1.41421356])
>>> C = np.array([2., -1., 4.])
>>> np.add(B, C)
array([ 2.,  0.,  6.])
```

- 索引，切片和迭代

一维的数组可以很简单的索引，切片和迭代就像python中的list和其它序列。

```
>>> a = np.arange(10)**3
>>> a
array([  0,   1,   8,  27,  64, 125, 216, 343, 512, 729])
>>> a[2]
8
>>> a[2:5]
array([ 8, 27, 64])
>>> a[:6:2] = -1000    # equivalent to a[0:6:2] = -1000; from start to position 6, exclusive, set every 2nd element to -1000
>>> a
array([-1000,     1, -1000,    27, -1000,   125,   216,   343,   512,   729])
>>> a[ : :-1]                                 # reversed a
array([  729,   512,   343,   216,   125, -1000,    27, -1000,     1, -1000])
>>> for i in a:
...     print(i**(1/3.))
...
nan
1.0
nan
3.0
nan
5.0
6.0
7.0
8.0
9.0
```


而多维的数组可以在每个轴上由一个索引，这些索引是以一个由逗号分隔的元组表示的：

```
>>> def f(x,y):
...     return 10*x+y
...
>>> b = np.fromfunction(f,(5,4),dtype=int)
>>> b
array([[ 0,  1,  2,  3],
       [10, 11, 12, 13],
       [20, 21, 22, 23],
       [30, 31, 32, 33],
       [40, 41, 42, 43]])
>>> b[2,3]
23
>>> b[0:5, 1]                       # each row in the second column of b
array([ 1, 11, 21, 31, 41])
>>> b[ : ,1]                        # equivalent to the previous example
array([ 1, 11, 21, 31, 41])
>>> b[1:3, : ]                      # each column in the second and third row of b
array([[10, 11, 12, 13],
       [20, 21, 22, 23]])
```

而若当某提供的索引数少于数组轴的数量时，缺失的索引会被认为是对响应的轴进行完全切片：

```
>>> b[-1]                                  # the last row. Equivalent to b[-1,:]
array([40, 41, 42, 43])
```

对多维数组进行其第一个轴上的迭代：

```
>>> for row in b:
...     print(row)
...
[0 1 2 3]
[10 11 12 13]
[20 21 22 23]
[30 31 32 33]
[40 41 42 43]
```

而如果想对多维数组的元素逐个进行迭代，则需要用到数组的flat属性（将数组”展开平铺“）：

```
>>> for element in b.flat:
...     print(element)
...
0
1
2
3
10
11
12
13
20
21
22
23
30
31
32
33
40
41
42
43
```

- 形状控制（shape manipulation）

形状(shape)即为数组在每个轴上的长度/元素个数。

```
>>> a = np.floor(10*np.random.random((3,4)))
>>> a
array([[ 2.,  8.,  0.,  6.],
       [ 4.,  5.,  1.,  1.],
       [ 8.,  9.,  3.,  6.]])
>>> a.shape
(3, 4)
```

数组的形状可以用各种各样的函数进行修改，注意以下的ravel（）、reshape（）、.T属性都是返回一个修改后的数组，而不是在原数组的基础上进行修改：

```
>>> a.ravel()  # returns the array, flattened
array([ 2.,  8.,  0.,  6.,  4.,  5.,  1.,  1.,  8.,  9.,  3.,  6.])
>>> a.reshape(6,2)  # returns the array with a modified shape
array([[ 2.,  8.],
       [ 0.,  6.],
       [ 4.,  5.],
       [ 1.,  1.],
       [ 8.,  9.],
       [ 3.,  6.]])
>>> a.T  # returns the array, transposed
array([[ 2.,  4.,  8.],
       [ 8.,  5.,  9.],
       [ 0.,  1.,  3.],
       [ 6.,  1.,  6.]])
>>> a.T.shape
(4, 3)
>>> a.shape
(3, 4)
```

与reshape（）函数形成对比的是ndarray的resize（）函数，两者的区别是，resize（）函数是改变了数组本身：

```
>>> a
array([[ 2.,  8.,  0.,  6.],
       [ 4.,  5.,  1.,  1.],
       [ 8.,  9.,  3.,  6.]])
>>> a.resize((2,6))
>>> a
array([[ 2.,  8.,  0.,  6.,  4.,  5.],
       [ 1.,  1.,  8.,  9.,  3.,  6.]])
```
