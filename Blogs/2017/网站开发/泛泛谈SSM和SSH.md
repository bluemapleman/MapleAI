本文来自[泛泛谈SSM和SSH](http://blog.csdn.net/mengdonghui123456/article/details/51591399)


最近在学SSH，但突然看到了SSM，感觉两者很相似，于是就开始打破砂锅问到底，网上找了很多资料，但是由于本人对SSM的认识只存在于理论上，所以就泛泛的谈论下自己对这两个java框架的认识，做一个小总结。

 记得很久前看到一个标题，名为“MVC已死”，说的MVC这种思想已经有一些不适应了，新的模式MOVE，正在茁壮成长，MOVE指即Models（模型）、Operations（操作）、Views（视图）、Events（事件），当时看了很多资料，觉得人家分析的真棒，不过现在一点印象都没有了，为什么？因为没有总结，没有形成自己的认识，所以尽管自己没有学习SSM，但是还是想总结对比下，起码来个宏观的认识也是好的。
 
 我们通常所说的SSH指的是：Spring+Struts+Hibernate。而SSM指的是:spring +SpringMVC + MyBatis。关于SSM和SSH 对比其实更多的从SpringMVC 和 Struts这一方面对比，和Hibernate与MyBatis的对比。
 
# SpringMVC与Struts :


  首先两者有个共同之处，那就是两者都数据javaweb层的开发框架，都是mvc模式的的经典产品，都实现了页面分离控制的功能，但是两者之间是有区别的。
  

   因为Spring MVC属于SpringFrameWork的后续产品，已经融合在SpringWeb Flow里面。Spring MVC 分离了控制器、模型对象、分派器以及处理程序对象的角色，这种分离让它们更容易进行定制。而且由于同是属于一个开发公司，所以SpringMVC比Struts更容易契合Spring技术，在扩展和灵活性上更胜一筹。

  Struts的优势在于静态注入，插件机制和拦截器链，但是struts存在漏洞，经常会被作为攻击点进行冲击。相比更加安全简单的SpringMVC，开发者渐渐开发放弃了它。
 
# Hibernate 与MyBatis:


   Hibernate与Mybatis都是流行的持久层开发框架，一句话概括：MyBatis 简单易上手；hibernate成熟，市场推广率高。
   MyBatis可以进行更为细致的SQL优化，可以减少查询字段。
   MyBatis容易掌握，而Hibernate门槛较高。
   更重要的是，mybatis提供了对应各种用途、功能的插件，有需求？好，来个插件就搞定。而hibernate在这一方面是远远比不上mybatis的。

   Hibernate的DAO层开发比MyBatis简单，Mybatis需要维护SQL和结果映射。
   Hibernate对对象的维护和缓存要比MyBatis好，对增删改查的对象的维护要方便。
   Hibernate数据库移植性很好，MyBatis的数据库移植性不好，不同的数据库需要写不同SQL。
   Hibernate有更好的二级缓存机制，可以使用第三方缓存。MyBatis本身提供的缓存机制不佳。
   但是hibernat缺点很明确，如果涉及到多张关联表的调用时：
    1. 多表关联等比较复杂，使用的成本并不低；
    2. 效率比较低，在大型项目中很少会使用到它，因为sql都是自动生成的，不太好进行人工的优化。
 
 
# 结论

  综上，在如今的开发过程中，人们越来越多的喜欢选择SSM，因为它更适合敏捷开发，而敏捷开发是现在市场备受推广的一种方式。

   我想说，我们应该努力学习，第一：知识有个演变的过程，他们都是相同，有了基础学习新的会省力很多。第二：抓紧时间学习，因为我们需要学习的东西太多了。因为这些都是几年前的事情了。