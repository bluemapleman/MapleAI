很多涉及或者并行式机器学习工作或者大数据处理的岗位，基本都会有要求会使用Hadoop/Hive/Spark/Storm这几个开源工具，那么针对其中比较主流的Spark，我在这里做一个比较简单地总结。

[TOC]

# 什么是Spark？

      在技术不断告诉更迭的程序圈，一个新的工具的出现与流行必然是因为它满足了很大一部分人长期未被满足的需求，或是解决了一个长期让很多人难受的一个痛点。

![这里写图片描述](http://img.blog.csdn.net/20170905105920516?watermark/2/text/aHR0cDovL2Jsb2cuY3Nkbi5uZXQvcXFfMzI2OTA5OTk=/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70/gravity/SouthEast)

  以上这个定理提醒我们，要学一个新技术，就有必要先了解这门技术出现的意义。这样，我们才能更好明白：它是应用到什么场景的，相比同类工具它的优缺点是什么，因此什么时候用它比其它工具好或差等等等等。只有至少理解了这些，才好说自己是真正掌握了这个工具，否则只能说是浅尝辄止，半生不熟。

  Spark，最早是2009年Berkeley大学AMPLab实验室开发的一个分布式、内存式、流式计算引擎，初衷为了可以高速地进行大量的数据的一系列处理工作。后来项目给了Apache基金会运营。14年的Databricks团队使用Spark刷新数据排序世界记录，可算是让Spark一战成名。 (参考 [wiki-Spark](https://zh.wikipedia.org/wiki/Apache_Spark#cite_note-8))
 

# 为什么要用Spark？


说到底，Spark的就是一个非常非常“快”的大数据计算引擎，可以高速地完成大量数据的复杂处理任务。

而我们用Spark，也是因为它的快！它非常快，以至于我们可以在很短的时间内完成原来需要很长时间完成的相同量级的任务。那它具体快到什么程度？Spark为什么可以这么快呢？我们来看看它的wiki说明：

    相对于Hadoop的MapReduce会在运行完工作后将中介数据存放到磁盘中，Spark使用了内存内运算技术，能在数据尚未写入硬盘时即在内存内分析运算。Spark在内存内运行程序的运算速度能做到比Hadoop MapReduce的运算速度快上100倍，即便是运行程序于硬盘时，Spark也能快上10倍速度。Spark允许用户将数据加载至集群内存，并多次对其进行查询，非常适合用于机器学习算法。

“100倍”！“10倍”！和同类的工具比较起来，已经不是一个数量级的速度了（当然下任何结论都是要给条件和约束的，这里只是一个比较简单粗暴的说明，目的是给大家一个比较直观的感受。就好像spark的快，是应该在一定环境下说的，比如跑什么类型的任务，机器的性能如何等等。）。而简单说来，在满足性能需求的情况下，Spark确实在很多同类任务上都能实现远超Hadoop的效率！
                                                         
 这里出现了与它的一个同类大胸弟——Hadoop的对比，同样是大数据处理的常用工具（具体有关Hadoop的简明教程我会另开一篇文章来写），说明中告诉我们，Spark是一直在*内存*里面算，Hadoop是运行过程中会将中间的数据不断写入再读出*磁盘*，而我们也知道，系统I/O操作是一个比较耗时的操作，Hadoop由于其实现机制问题，不得不地进行大量I/O操作，而Spark一直在内存中干活，就省去了这些麻烦，只在数据完全处理完毕后一次性输出。

另外，从两者任务的执行机制来看，Spark是将任务做成了DAG有向无环图的模式，而Hadoop是用MapReduce(MR)模式，而DAG模式本身是比MR模式在处理效率上更高，因为DAG可以有效减少Map和Reduce任务之间传递数据的过程。（这里只是大概的一个表述，言语不恰当处请见谅）

其它的具体对比可以参照知乎上的[回答](https://www.zhihu.com/question/26568496)。

另外，Spark本身在需要大量迭代的运算上非常有优势，而机器学习算法恰恰是会涉及到许多迭代操作的，因此Spark跑机器学习算法是非常完美的配合。

![这里写图片描述](http://img.blog.csdn.net/20170905122316127?watermark/2/text/aHR0cDovL2Jsb2cuY3Nkbi5uZXQvcXFfMzI2OTA5OTk=/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70/gravity/SouthEast)



# Spark的相关工具与开发语言

## 生态圈

![这里写图片描述](http://img.blog.csdn.net/20170905122732673?watermark/2/text/aHR0cDovL2Jsb2cuY3Nkbi5uZXQvcXFfMzI2OTA5OTk=/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70/gravity/SouthEast)

Spark毕竟是一个单兵，而它自己还需要得手的武器，以及和其它的伙伴的配合，才能完整地发挥它的作用。

而它自己的军火库里有：

- Spark Streaming：流处理库
- graph-parallel：图并行处理库
- ML：机器学习库
- Shark SQL：并行式SQL查询库

而它的好伙伴有：

- HDFS、Tachyon：分布式文件存储系统（大量数据的存储）
- Mesos，YARN：资源管理框架（调度计算任务）

这些丰富的库和其它工具使得Spark可以胜任多种类型的计算任务，在各种实际需求下都能游刃有余地发挥其最大的效用。

## 开发语言

Spark程序本身支持用Scala（Spark的开发语言），Java，Python三种语言编写，熟悉其中任一门语言的都可以直接上手编写Spark程序，可谓非常方便。


# Spark的运行架构


Spark的一个最大特点就是它的集群式/分布式计算，就是它可以将一个大任务分解成很小任务，交给很多台机器去分别完成，最后汇总。就是“人多力量大”的道理。

而它要完成这种分布式的计算，就需要有一套标准的逻辑去负责分解、分配任务，以及搜集最后的处理结果，这些就是通过以下的架构来实现的。

以下部分参考[这里](http://blog.csdn.net/u011204847/article/details/51010205)
{
Spark架构采用了分布式计算中的Master-Slave模型。Master是对应集群中的含有Master进程的节点，Slave是集群中含有Worker进程的节点。Master作为整个集群的控制器，负责整个集群的正常运行；Worker相当于是计算节点，接收主节点命令与进行状态汇报；Executor负责任务的执行；Client作为用户的客户端负责提交应用，Driver负责控制一个应用的执行，如图1-4所示：
 
 ![这里写图片描述](http://img.blog.csdn.net/20170905125332502?watermark/2/text/aHR0cDovL2Jsb2cuY3Nkbi5uZXQvcXFfMzI2OTA5OTk=/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70/gravity/SouthEast)
 
 

下面详细介绍Spark的架构中的基本组件。

- ClusterManager：在Standalone模式中即为Master（主节点），控制整个集群，监控Worker。在YARN模式中为资源管理器。
- Worker：从节点，负责控制计算节点，启动Executor或Driver。在YARN模式中为NodeManager，负责计算节点的控制。
- Driver：运行Application的main（）函数并创建SparkContext。
- Executor：执行器，在worker node上执行任务的组件、用于启动线程池运行任务。每个Application拥有独立的一组Executors。
- SparkContext：整个应用的上下文，控制应用的生命周期。
- RDD：Spark的基本计算单元，一组RDD可形成执行的有向无环图RDD Graph。
- DAG Scheduler：根据作业（Job）构建基于Stage的DAG，并提交Stage给TaskScheduler。
- TaskScheduler：将任务（Task）分发给Executor执行。
- SparkEnv：线程级别的上下文，存储运行时的重要组件的引用。SparkEnv内创建并包含如下一些重要组件的引用。
- MapOutPutTracker：负责Shuffle元信息的存储。
- BroadcastManager：负责广播变量的控制与元信息的存储。
- BlockManager：负责存储管理、创建和查找块。
- MetricsSystem：监控运行时性能指标信息。
- SparkConf：负责存储配置信息。


Spark的整体流程为：Client提交应用，Master找到一个Worker启动Driver，Driver向Master或者资源管理器申请资源，之后将应用转化为RDD Graph，再由DAGScheduler将RDD Graph转化为Stage的有向无环图提交给TaskScheduler，由TaskScheduler提交任务给Executor执行。在任务执行的过程中，其他组件协同工作，确保整个应用顺利执行。
}



# 应用场景

(本部分参考[这里](http://blog.csdn.net/u011204847/article/details/51010205))

Spark使用了内存分布式数据集，除了能够提供交互式查询外，还优化了迭代工作负载，在Spark SQL、Spark Streaming、MLlib、GraphX都有自己的子项目。在互联网领域，Spark在快速查询、实时日志采集处理、业务推荐、定制广告、用户图计算等方面都有相应的应用。国内的一些大公司，比如阿里巴巴、腾讯、Intel、网易、科大讯飞、百分点科技等都有实际业务运行在Spark平台上。下面简要说明Spark在各个领域中的用途。 

1. 快速查询系统     基于日志数据的快速查询系统业务构建于Spark之上，利用其快速查询以及内存表等优势，能够承担大部分日志数据的即时查询工作；在性能方面，普遍比Hive快2～10倍，如果使用内存表的功能，性能将会比Hive快百倍。 

2. 实时日志采集处理     通过Spark Streaming实时进行业务日志采集，快速迭代处理，并进行综合分析，能够满足线上系统分析要求。 

3. 业务推荐系统     使用Spark将业务推荐系统的小时和天级别的模型训练转变为分钟级别的模型训练，有效优化相关排名、个性化推荐以及热点点击分析等。
4. 定制广告系统     在定制广告业务方面需要大数据做应用分析、效果分析、定向优化等，借助Spark快速迭代的优势，实现了在“数据实时采集、算法实时训练、系统实时预测”的全流程实时并行高维算法，支持上亿的请求量处理；模拟广告投放计算效率高、延迟小，同MapReduce相比延迟至少降低一个数量级。 

5. 用户图计算     利用GraphX解决了许多生产问题，包括以下计算场景：基于度分布的中枢节点发现、基于最大连通图的社区发现、基于三角形计数的关系衡量、基于随机游走的用户属性传播等。




# Spark程序编写

Spark的各方面基本知识了解了，就可以开始尝试编写程序用它跑起来了。

而Spark程序的具体开发知识网上较为详细的教程还不是很多，需要参考一些书籍来学习，这里就推荐一本自己看过的觉得还可以的[《Spark快速大数据分析》](http://download.csdn.net/download/wangcunlin/9547494)。