作为程序编写技术的一个常见术语，以及技术笔试与面试的常考点，这里总结一下设计模式的相关知识。

本文的代码实现均为Java。

[TOC]

本文参考:
[1] [Java之美[从菜鸟到高手演变]之设计模式 ](http://blog.csdn.net/zhangerqing/article/details/8194653#comments) 
[2] [菜鸟教程设计模式](http://www.runoob.com/design-pattern/design-pattern-tutorial.html)
[3] [设计模式：可复用面向对象软件的基础](https://baike.baidu.com/item/设计模式：可复用面向对象软件的基础/7600072?fr=aladdin&fromid=3919457&fromtitle=设计模式：可复用面向对象软件的基础)


# 什么是设计模式

先看一些描述：

	在软件工程中，设计模式（design pattern）是对软件设计中普遍存在（反复出现）的各种问题，所提出的解决方案。这个术语是由埃里希·伽玛（Erich Gamma）等人在1990年代从建筑设计领域引入到计算机科学的。
	
	设计模式是一套被反复使用、多数人知晓的、经过分类编目的、代码设计经验的总结
	
	设计模式并不直接用来完成代码的编写，而是描述在各种不同情况下，要怎么解决问题的一种方案。面向对象设计模式通常以类别或对象来描述其中的关系和相互作用，但不涉及用来完成应用程序的特定类别或对象。设计模式能使不稳定依赖于相对稳定、具体依赖于相对抽象，避免会引起麻烦的紧耦合，以增强软件设计面对并适应变化的能力。
	
	并非所有的软件模式都是设计模式，设计模式特指软件“设计”层次上的问题。还有其他非设计模式的模式，如架构模式。同时，算法不能算是一种设计模式，因为算法主要是用来解决计算上的问题，而非设计上的问题。

简单说来，设计模式来源于软件工程，是一系列软件设计思想，它凌驾于编程语言之上，是一种程序设计的经验总结，这些经验提供了一些软件设计的常见问题的解决方案，或是作为一种规范，可以遵照它写出非常稳健的程序。

因而，设计模式某方面类似于数据结构与算法，它不拘泥于任何一门具体的编程语言，任何语言都可以实现它们，它们只是一种思想。算法与数据结构的思想，是对计算机运算与存储过程中涉及到的数据进行的一种有利于简化问题，提高效率的思想。而设计模式这种思想，是在一个更宏观的层面上，为了指导程序员设计和写出结构更优良的程序而存在的思想。

那么这里就谈到程序员的追求问题了。程序员应该写出“漂亮”的代码，漂亮有三层含义：
- 第一层最浅的是格式漂亮的（缩进，成员命名，大小写等）——此之为扎马步的功夫；
- 第二层就是比较高级的，程序的可读性，即其它同行看你的代码是否能够很快理解你想表达的逻辑，如果能，说明你的代码已经写得比较规范了——此之为精通某一派招式的功夫；
- 第三层最高级的就是写出具有结构规范、高内聚低耦合、可扩展性高等特点的精致程序，而要到达这个境界，你就很需要设计模式来指导你了——此之为已入化境，不需身体行动，内力即可伤人。


# 设计模式的分类

  说的那么缥缈，我们落地来看看，设计模式到底有哪些种类。

## 创建型模式

创建型模式全部是关于如何创建实例的。这组范例可以被划分为两组：类创建范例及对象创建范例。类创建实例在实例化过程中有效的使用类之间的继承关系，对象创建范例则使用代理来完成其任务。（5种）

- 工厂方法 (Factory Method pattern)
- 抽象工厂 (Abstract Factory)
- 构造器 (Builder Pattern)
- 原型 (Prototype pattern)
- 单例模式 (Singleton pattern)



## 结构型模式

这组范例都是关于类及对象复合关系的。（7种）

- 适配器(Adapter pattern)
- 桥接(Bridge pattern)
- 组合(Composite pattern)
- 装饰(Decorator pattern)
- 外观(Façade pattern)
- 享元(Flyweight pattern)
- 代理(Proxy pattern)

## 行为型模式

这组范例都是关于对象之间如何通讯的。（11种）

- 职责链(Chain-of-responsibility pattern)
- 命令(Command pattern)
- 翻译器(Interpreter pattern)
- 迭代器(Iterator pattern)
- 仲裁器(Mediator pattern)
- 回忆(Memento pattern)
- 观察者(Observer pattern)
- 状态机(State pattern)
- 策略(Strategy pattern)
- 模板方法(Template method pattern)
- 参观者(Visitor)
	
## 解读

这个分类最初来源于设计模式四大开山怪GoF94年的《设计模式：可复用面向对象软件的基础》书中的分类方式(参考[wiki](https://zh.wikipedia.org/wiki/%E8%AE%BE%E8%AE%A1%E6%A8%A1%E5%BC%8F%EF%BC%9A%E5%8F%AF%E5%A4%8D%E7%94%A8%E9%9D%A2%E5%90%91%E5%AF%B9%E8%B1%A1%E8%BD%AF%E4%BB%B6%E7%9A%84%E5%9F%BA%E7%A1%80))，也是一直沿用至今的分类方式。可以看出三大模式主要分别用来处理三种面向对象程序设计中的问题：如何创建实例，类与对象之间的关系，对象之间的通讯方式。

那么接下来我们就分别来和5+7+11=23个武林高手来一一过招！

![这里写图片描述](http://img.blog.csdn.net/20170906110901462?watermark/2/text/aHR0cDovL2Jsb2cuY3Nkbi5uZXQvcXFfMzI2OTA5OTk=/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70/gravity/SouthEast)


# 创建型模式：创建对象的N种艺术

## 工厂方法 (Factory Method pattern)

*创建对象的事情包我身上了！你直接拿就是！*

在工厂模式中，我们在创建对象时不会对客户端暴露创建逻辑，并且是通过使用一个共同的接口来指向新创建的对象。

意图：定义一个创建对象的接口，让其子类自己决定实例化哪一个工厂类，工厂模式使其创建过程延迟到子类进行。
	
	主要解决：主要解决接口选择的问题。
	
	何时使用：我们明确地计划不同条件下创建不同实例时。
	
	如何解决：让其子类实现工厂接口，返回的也是一个抽象的产品。
	
	关键代码：创建过程在其子类执行。
	
	应用实例： 1、您需要一辆汽车，可以直接从工厂里面提货，而不用去管这辆汽车是怎么做出来的，以及这个汽车里面的具体实现。 2、Hibernate 换数据库只需换方言和驱动就可以。

工厂模式的好处主要就在于可以向用户隐藏所需对象的实现细节，并提供方便地新对象扩展功能。简单而言：

- 现在当程序需要某个类的实例对象时，程序不需要去自己new一个实例，只要去找那个类对应的工厂类Factory，调用Factory的方法就可以获得一个实例。这样做的好处是：如果创建一个实例的初始化过程比较复杂，比如要传一些参数呀，那么程序不需要了解这些细节，只管伸手找工厂要一个做好的对象就行。

比如你成年之前，很难赚钱（需要的目标对象），你的经济来源只能靠父母（Factory）来给你提供。你如果想自己去赚，因为能力和年龄都不够，所以非常困难。所以只要找父母给你提供就行。

- 程序经常会需要用到某个类的实例对象，但是一般传进来的是这个类不同的几种子类的实例对象之一（ABC）。那么当程序明确自己想要某个具体的子类对象时，只要去找工厂说，我要子类A/B/C的对象，那么工厂就直接把对应的对象给你。这样做的好处是：首先是和上面类似不需要自己去new新对象，而且想要什么类型的对象指定名称就行。其次是，这种结构可以非常方便地实现目标类子类的扩展。

比如你有独立收入前，想走遍中国，于是找父母要一笔人民币（A对象）作为旅游资金。然后你又想去美国玩，那么这时你就需要找你的父母要一笔美金（B对象）。同样，不管你想去哪个国家，你找你爸妈要对应国家的货币就行，而你爸妈要做的就是去银行兑出相应国家的货币给你。（PS：还没有经济独立的朋友，父母的钱来之不易，请用在该用的地方~）


工厂模式实现：

```
步骤 1

创建一个接口。

Shape.java

public interface Shape {
   void draw();
}

步骤 2

创建实现接口的实体类。

Rectangle.java

public class Rectangle implements Shape {

   @Override
   public void draw() {
      System.out.println("Inside Rectangle::draw() method.");
   }
}

Square.java

public class Square implements Shape {

   @Override
   public void draw() {
      System.out.println("Inside Square::draw() method.");
   }
}

Circle.java

public class Circle implements Shape {

   @Override
   public void draw() {
      System.out.println("Inside Circle::draw() method.");
   }
}

步骤 3

创建一个工厂，生成基于给定信息的实体类的对象。

ShapeFactory.java

public class ShapeFactory {
	
   //使用 getShape 方法获取形状类型的对象
   public Shape getShape(String shapeType){
      if(shapeType == null){
         return null;
      }		
      if(shapeType.equalsIgnoreCase("CIRCLE")){
         return new Circle();
      } else if(shapeType.equalsIgnoreCase("RECTANGLE")){
         return new Rectangle();
      } else if(shapeType.equalsIgnoreCase("SQUARE")){
         return new Square();
      }
      return null;
   }
}

步骤 4

使用该工厂，通过传递类型信息来获取实体类的对象。

FactoryPatternDemo.java

public class FactoryPatternDemo {

   public static void main(String[] args) {
      ShapeFactory shapeFactory = new ShapeFactory();

      //获取 Circle 的对象，并调用它的 draw 方法
      Shape shape1 = shapeFactory.getShape("CIRCLE");

      //调用 Circle 的 draw 方法
      shape1.draw();

      //获取 Rectangle 的对象，并调用它的 draw 方法
      Shape shape2 = shapeFactory.getShape("RECTANGLE");

      //调用 Rectangle 的 draw 方法
      shape2.draw();

      //获取 Square 的对象，并调用它的 draw 方法
      Shape shape3 = shapeFactory.getShape("SQUARE");

      //调用 Square 的 draw 方法
      shape3.draw();
   }
}

步骤 5

验证输出。

Inside Circle::draw() method.
Inside Rectangle::draw() method.
Inside Square::draw() method.
```

##抽象工厂 (Abstract Factory)：

*复杂的东西我能全部自己做！*
  
抽象工厂模式（Abstract Factory Pattern）是围绕一个超级工厂创建其他工厂。该超级工厂又称为其他工厂的工厂。

顾名思义，抽象工厂类负责返回的是工厂，因此抽象工厂是工厂的工厂。

那么为什么需要把工厂又做成了产品供应呢？那是因为，生产某些复杂商品可能需要多个简单商品的配合。

比如要生产一把能冒蓝火的加特林（滑稽），是需要生产加特林和生产子弹的两个厂家的。而抽象工厂就是可以生产冒蓝火的加特林的这么一个超级厂家，因为它自带一个加特林厂家和一个子弹厂家。

![这里写图片描述](http://img.blog.csdn.net/20170906182033443?watermark/2/text/aHR0cDovL2Jsb2cuY3Nkbi5uZXQvcXFfMzI2OTA5OTk=/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70/gravity/SouthEast)

因此，抽象工厂是因为要创建某类复杂对象（蓝火加特林，绿火沙漠之鹰，水晶AK47）的需求，而存在的，这类复杂对象需要一些简单对象（枪和子弹）的配合，而这些简单对象又分别需要各自的工厂来完成，因此最好的方法就是将这些小工厂做成一个大工厂。




## 构造器 (Builder Pattern)

*我有标准化的流程来创建复杂的对象*

建造者模式（Builder Pattern）使用多个简单的对象一步一步构建成一个复杂的对象。

一个 Builder 类会一步一步构造最终的对象。该 Builder 类是独立于其他对象的。

	意图：将一个复杂的构建与其表示相分离，使得同样的构建过程可以创建不同的表示。
	
	主要解决：主要解决在软件系统中，有时候面临着"一个复杂对象"的创建工作，其通常由各个部分的子对象用一定的算法构成；由于需求的变化，这个复杂对象的各个部分经常面临着剧烈的变化，但是将它们组合在一起的算法却相对稳定。
	
	何时使用：一些基本部件不会变，而其组合经常变化的时候。
	
	如何解决：将变与不变分离开。
	
	关键代码：建造者：创建和提供实例，导演：管理建造出来的实例的依赖关系。
	
	应用实例： 1、去肯德基，汉堡、可乐、薯条、炸鸡翅等是不变的，而其组合是经常变化的，生成出所谓的"套餐"。 2、JAVA 中的 StringBuilder。 

简而言之，构造器模式处理的是复杂对象的构建问题。此处的复杂对象指的是其成员本身也包含几个其它的对象。比如肯德基的套餐对象，里面就包含了汉堡包、饮料与薯条这三个对象，所以套餐本身是个复杂对象。那么构造器问题处理了复杂对象构建的什么问题呢？

简单说来，就是把复杂对象的创建过程与复杂对象的成员对象的创建过程给分离开。同时，也提高了复杂对象的可扩展性。

下图是构造器模式的结构图（来自[3]）：

![这里写图片描述](http://img.blog.csdn.net/20170906163748364?watermark/2/text/aHR0cDovL2Jsb2cuY3Nkbi5uZXQvcXFfMzI2OTA5OTk=/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70/gravity/SouthEast)

参与者：
• Builder
— 为创建一个Product对象的各个部件指定抽象接口。
• ConcreteBuilder
— 实现Builder的接口以构造和装配该产品的各个部件。
— 定义并明确它所创建的表示。
— 提供一个检索产品的接口。
• Director
— 构造一个使用Builder接口的对象。
• Product
— 表示被构造的复杂对象。ConcreteBuilder创建该产品的内部表示并定义它的装配过程。
— 包含定义组成部件的类，包括将这些部件装配成最终产品的接口。

工作流程：
• 客户创建Director对象，并用它所想要的Builder对象进行配置。
• 一旦产品部件被生成，导向器就会通知生成器。
• 生成器处理导向器的请求，并将部件添加到该产品中。
• 客户从生成器中检索产品。


举个例子帮助理解。车厂老板（客户Client）谈了一笔单子，要做一批宝马和奔驰(两种复杂对象Product)。于是老板分别找了宝马和奔驰的技术主任（Director）来负责生产问题。两个主任各自让车厂（Builder）配了一条生产线（两个ConcreteBuilder），一条线组装奔驰，一条线组装宝马，并分别让人去把对应零件（产品部件）买回来。而车厂老板不在乎你奔驰的各个零件是怎么组合的，也不在乎你宝马用哪些高端的零件，老板只要到期两个主任交付一批奔驰和宝马就ok。

构造器模式实现：（代码来源[这里](http://blog.csdn.net/luhuajcdd/article/details/8806897)）

```
//如果需要一个接口来创建部件：


    package com.designpatten.builder;  
      
      
    public interface Builder {  
        void buildCarWheel() ;  
        void buildSteeringWheel() ;  
        void buildEngine() ;  
        void buildCarFrame() ;  
        Car getCar() ;  
    }  


//在Director中构建复杂对象，将Builder中定义的一个一个部件组装起来。

    package com.designpatten.builder;  
      
    public class Director {  
      
        private Builder builder ;  
          
        public Director(Builder builder){  
            this.builder = builder ;  
        }  
          
        public void getCarTogether(){  
            builder.buildCarFrame() ;  
            builder.buildEngine();  
            builder.buildCarWheel() ;  
            builder.buildSteeringWheel() ;  
        }  
          
    }  

//实现具体的Builder：

    //通过实现接口，来完成部件的构建过程
    //重新获得目标对象接口


    package com.designpatten.builder;  
      
    public class BenzBuilder implements Builder {  
      
        private Benz benz ;  
          
        public BenzBuilder(){  
            benz = new Benz() ;  
        }  
          
        @Override  
        public void buildCarWheel() {  
            System.out.println("Benz add Wheel");  
        }  
      
        @Override  
        public void buildSteeringWheel() {  
            System.out.println("Benz add SteeringWheel");  
        }  
      
        @Override  
        public void buildEngine() {  
            System.out.println("Benz add engine");  
        }  
      
        @Override  
        public void buildCarFrame() {  
            System.out.println("Benz add frame");  
        }  
      
        @Override  
        public Car getCar() {  
            return benz;  
        }  
      
    }  


    package com.designpatten.builder;  
      
      
    public class BMWBuilder implements Builder {  
      
      
        private BMW bmw ;   
          
        public BMWBuilder(){  
            bmw = new BMW() ;  
        }  
          
        @Override  
        public void buildCarWheel() {  
            System.out.println("BMW add CarWheel");  
        }  
      
      
        @Override  
        public void buildSteeringWheel() {  
            System.out.println("BMW add SteeringWheel");  
        }  
      
      
        @Override  
        public void buildEngine() {  
            System.out.println("BMW add Engine");  
        }  
      
      
        @Override  
        public void buildCarFrame() {  
            System.out.println("BMW add Frame");  
        }  
      
      
        @Override  
        public Car getCar() {  
            return bmw;  
        }  
      
      
    }  

//具体的产品信息


    package com.designpatten.builder;  
      
    public interface Car {  
          
        void run() ;  
          
    }  




    package com.designpatten.builder;  
      
    public class BMW implements Car {  
      
        @Override  
        public void run() {  
            System.out.println("BMW ---> run()");  
        }  
      
    }  



    package com.designpatten.builder;  
      
    public class Benz implements Car {  
      
        @Override  
        public void run() {  
            System.out.println("Benz -------> run()");  
        }  
      
    }  

//生产Car

    package com.designpatten.builder;  
      
    public class Client {  
        public static void main(String[] args) {  
            BenzBuilder benzBuilder = new BenzBuilder() ;  
            BMWBuilder bmwBuilder = new BMWBuilder() ;  
              
            Director benzDirector = new Director(benzBuilder) ;  
            benzDirector.getCarTogether() ;  
            Car benz = benzBuilder.getCar() ;  
            benz.run() ;  
            System.out.println("----------------------------");  
            Director bmwDirector = new Director(bmwBuilder) ;  
            bmwDirector.getCarTogether() ;  
            Car bmw = bmwBuilder.getCar() ;  
            bmw.run() ;  
        }  
    }  

//输出结构

    Benz add frame  
    Benz add engine  
    Benz add Wheel  
    Benz add SteeringWheel  
    Benz -------> run()  
    ----------------------------  
    BMW add Frame  
    BMW add Engine  
    BMW add CarWheel  
    BMW add SteeringWheel  
    BMW ---> run()  
```


构造器与抽象工厂会有一些类似，这里[转载](http://blog.csdn.net/hawksoft/article/details/6626775)一个两种模式的对比：

	从形式上来讲，通过角色合并，方法功能的转变，抽象工厂可以和生成器模式形式上取得一致（比如抽象工厂只处理一个产品族，工厂方法都处理同一个产品）。但注意，这仅仅是形式上的，实际上，抽象工厂和生成器模式有着本质的区别：

	1、生成器模式是为了构造一个复杂的产品，而且购造这个产品遵循一定的规则（相同的过程），而抽象工厂则是为了创建成族的产品（系列产品），同族产品的构造在逻辑上并不存在必然的联系（唯一必然的联系就是大家都属于一族）。
	
	2、生成器模式的构造方法是为了构造同一个产品，因此必须有指导者来协调进行工作，构造方法之间存在必然的业务联系，而抽象工厂的构造方法都是独立去构建自己的产品对象，因此他们不存在必然的联系。在生成器模式中客户端不直接调用构建产品部分的方法来获取最终产品，而抽象工厂中客户端是通过调用不同的工厂方法获取不同的产品。
	
	3.在生成器模式中，那些用来构造产品不同部分的方法一般都实现为Protected形式，以防止客户端通过调用这种方法活得不可预料的结果，而抽象工厂中的这些方法必须为Public形式。否则客户无法调用来获得产品结果；
	
	4.生成器模式的角色有生成器，产品和指导者，而抽象工厂的角色有工厂和产品。无论角色和功能怎样变换，但所含的业务逻辑角色都应该存在，这也是两个模式的业务本质。


## 原型模式(Prototype pattern)

*别new了！试试高科技的克隆技术！*

原型模式用于创建*重复*的对象，同时又能*保证性能*。

	这种模式是实现了一个原型接口，该接口用于创建当前对象的克隆。当直接创建对象的代价比较大时，则采用这种模式。例如，一个对象需要在一个高代价的数据库操作之后被创建。我们可以缓存该对象，在下一个请求时返回它的克隆，在需要的时候更新数据库，以此来减少数据库调用。

	使用场景： 1、资源优化场景。 2、类初始化需要消化非常多的资源，这个资源包括数据、硬件资源等。 3、性能和安全要求的场景。 4、通过 new 产生一个对象需要非常繁琐的数据准备或访问权限，则可以使用原型模式。 5、一个对象多个修改者的场景。 6、一个对象需要提供给其他对象访问，而且各个调用者可能都需要修改其值时，可以考虑使用原型模式拷贝多个对象供调用者使用。 7、在实际项目中，原型模式很少单独出现，一般是和工厂方法模式一起出现，通过 clone 的方法创建一个对象，然后由工厂方法提供给调用者。原型模式已经与 Java 融为浑然一体，大家可以随手拿来使用。 	

	关键代码： 1、实现克隆操作，在 JAVA 继承 Cloneable，重写 clone()，在 .NET 中可以使用 Object 类的 MemberwiseClone() 方法来实现对象的浅拷贝或通过序列化的方式来实现深拷贝。 2、原型模式同样用于隔离类对象的使用者和具体类型（易变类）之间的耦合关系，它同样要求这些"易变类"拥有稳定的接口。
	
	注意事项：与通过对一个类进行实例化来构造新对象不同的是，原型模式是通过拷贝一个现有对象生成新对象的。浅拷贝实现 Cloneable，重写，深拷贝是通过实现 Serializable 读取二进制流

简而言之，我们会有需要大量的某个类的实例对象，但是直接new的话可能会非常麻烦，也许该类的构造函数写的特别复杂，对象初始化过程可能非常繁琐，但我们依然需要大量的新对象。再或者，有时候多个用户需要对同一个对象进行修改，但若允许大家一起同时修改的话，很有可能造成操作互相覆盖冲突的问题，这时我们先给每个用户一个该对象的克隆，让大家在各自的克隆上先修改，最后将大家的修改汇总处理，就能有效解决这种问题。

这里用到的技术叫“克隆”，指的就是Java的中的克隆方法clone()。在上面的引用的关键代码部门提到，如果我们想实现原型模式，就要首先让我们的目标类实现克隆操作，即实现Clonenable接口，重写抽象方法clone()，使得它可以返回一个满足我们要求的，对于原对象的一个克隆体。 

而关于克隆有一个知识点：浅拷贝和深拷贝。这里简单说一下。

浅拷贝指的是，克隆体拥有将原始对象的所有简单变量与引用类型变量的拷贝（Java中栈中存放的数据），但是引用类型的变量所指向的实际对象则并未拷贝，而是被克隆体和原始对象共用。而深拷贝则是克隆体拥有原始对象的全部变量拷贝，包括引用变量指向的堆中的实际对象也给拷贝了一遍，并各自享有各自的实际对象。

举个例子，小明有一辆车，浅拷贝是生成一个小刚，和小明长得一模一样，也有一辆车，但是小刚使用的就是小明的车。而深拷贝是，生成一个小刚，和小明长得一模一样，但是给小刚新配一辆和小明的车完全一样的车，两人各自开各自的车。

两种拷贝根据程序的需求来，浅拷贝一般用clone（）来做，而深拷贝用实现Serializable接口来完成。

原型模式的实现方式：

```
  我们将创建一个抽象类 Shape 和扩展了 Shape 类的实体类。下一步是定义类 ShapeCache，该类把 shape 对象存储在一个 Hashtable 中，并在请求的时候返回它们的克隆。

PrototypPatternDemo，我们的演示类使用 ShapeCache 类来获取 Shape 对象。
步骤 1

创建一个实现了 Clonable 接口的抽象类。

Shape.java

public abstract class Shape implements Cloneable {
   
   private String id;
   protected String type;
   
   abstract void draw();
   
   public String getType(){
      return type;
   }
   
   public String getId() {
      return id;
   }
   
   public void setId(String id) {
      this.id = id;
   }
   
   public Object clone() {
      Object clone = null;
      try {
         clone = super.clone();
      } catch (CloneNotSupportedException e) {
         e.printStackTrace();
      }
      return clone;
   }
}

步骤 2

创建扩展了上面抽象类的实体类。

Rectangle.java

public class Rectangle extends Shape {

   public Rectangle(){
     type = "Rectangle";
   }

   @Override
   public void draw() {
      System.out.println("Inside Rectangle::draw() method.");
   }
}

Square.java

public class Square extends Shape {

   public Square(){
     type = "Square";
   }

   @Override
   public void draw() {
      System.out.println("Inside Square::draw() method.");
   }
}

Circle.java

public class Circle extends Shape {

   public Circle(){
     type = "Circle";
   }

   @Override
   public void draw() {
      System.out.println("Inside Circle::draw() method.");
   }
}

步骤 3

创建一个类，从数据库获取实体类，并把它们存储在一个 Hashtable 中。

ShapeCache.java

import java.util.Hashtable;

public class ShapeCache {
	
   private static Hashtable<String, Shape> shapeMap 
      = new Hashtable<String, Shape>();

   public static Shape getShape(String shapeId) {
      Shape cachedShape = shapeMap.get(shapeId);
      return (Shape) cachedShape.clone();
   }

   // 对每种形状都运行数据库查询，并创建该形状
   // shapeMap.put(shapeKey, shape);
   // 例如，我们要添加三种形状
   public static void loadCache() {
      Circle circle = new Circle();
      circle.setId("1");
      shapeMap.put(circle.getId(),circle);

      Square square = new Square();
      square.setId("2");
      shapeMap.put(square.getId(),square);

      Rectangle rectangle = new Rectangle();
      rectangle.setId("3");
      shapeMap.put(rectangle.getId(),rectangle);
   }
}

步骤 4

PrototypePatternDemo 使用 ShapeCache 类来获取存储在 Hashtable 中的形状的克隆。

PrototypePatternDemo.java

public class PrototypePatternDemo {
   public static void main(String[] args) {
      ShapeCache.loadCache();

      Shape clonedShape = (Shape) ShapeCache.getShape("1");
      System.out.println("Shape : " + clonedShape.getType());		

      Shape clonedShape2 = (Shape) ShapeCache.getShape("2");
      System.out.println("Shape : " + clonedShape2.getType());		

      Shape clonedShape3 = (Shape) ShapeCache.getShape("3");
      System.out.println("Shape : " + clonedShape3.getType());		
   }
}

步骤 5

验证输出。

Shape : Circle
Shape : Square
Shape : Rectangle
```

## 单例模式 (Singleton pattern)

*你就是我的唯一！*

这是最简单最好理解的一个设计模式。

顾名思义，单例模式就是只允许是一个对象实例存在，而这种对象是为了这样两种需求，一种有时候某个类的对象常常被拿来用一下，又马上不用了，就被销毁，而不断地短时间内创建销毁其实是一个比较耗费系统资源的事情，因此我们干脆考虑让这个类的一个对象一直存在于内存中，谁需要用它就直接拿过去，用完就释放，这样就免去了不断创建销毁带来的计算资源损耗。另一种则是，有些对象从实际上来讲，就应该只存在一个，好比一个团体只应该有一个核心leader。

具体的使用情形包括： 
- 生产中唯一的序列号
- WEB中对访问人数进行计数的计数器，不用每次刷新都在数据库里加一次，用单例先缓存起来。
- I/O与数据库的连接对象，只需要在内存中缓存一个，随时调用

实现方式：

最常见的是懒汉式和饿汉式这两种方式。

### 懒汉式

```
public class Singleton {  
    private static Singleton instance;  
    private Singleton (){}  
  
    public static Singleton getInstance() {  
	    if (instance == null) {  
	        instance = new Singleton();  
	    }  
	    return instance;  
    }  
}  
```

### 饿汉式

```
public class Singleton {  
    private static Singleton instance = new Singleton();  
    private Singleton (){}  
    public static Singleton getInstance() {  
	    return instance;  
    }  
}  
```

两者的共同点都是首先要写一个私有的构造函数，以防止外界直接实例化对象。而区别在于，懒汉式是“偷懒的”，只在第一次程序需要用到单例类的实例对象时，才去初始化它，称之为懒加载（lazy load），而饿汉式“饥肠辘辘”，在类加载时就初始化好实例对象。

另外，考虑到线程安全层面的话，懒汉式存在问题，因为方法没有同步，导致可能出现两个线程在判断实例是否为空（instance==null）时交换了运行身份，导致创建出两个实例对象，违背了单例的初衷。而若将方法同步保证安全的话，又会牺牲运行效率。相对来说，饿汉式则在类加载时就完成对象实例化，不存在这个问题，但是也因为从一开始程序不需要用到单例的对象时，就实例化了对象，也造成了一定程度上资源的无谓占用。又要有效率，又要线程安全，还不浪费资源，十全十美就尊的这么难吗？

naive！

### 双检锁/双重校验锁（double-checked locking）

```
public class Singleton {  
    private volatile static Singleton singleton;  
    private Singleton (){}  
    public static Singleton getSingleton() {  
	    if (singleton == null) {  
	        synchronized (Singleton.class) {  
		        if (singleton == null) {  
		            singleton = new Singleton();  
		        }  
	        }  
	    }  
	    return singleton;  
    }  
}  
```

通过这种对饿汉式的改良，将同步机制做到判断单例对象是否为空的代码块上，就完美地解决了以上所有问题！妙啊！妙啊！
  
  ![这里写图片描述](http://img.blog.csdn.net/20170906130327900?watermark/2/text/aHR0cDovL2Jsb2cuY3Nkbi5uZXQvcXFfMzI2OTA5OTk=/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70/gravity/SouthEast)


# 后话

由于笔者目前的经验不足，对于一些模式的理解可能也停留在一个较浅的层面，有写的不当的地方，还请大家指教，感激不尽！