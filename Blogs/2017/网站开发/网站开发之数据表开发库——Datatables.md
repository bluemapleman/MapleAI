我们在做网站开发时，很常见的一个需求是做数据展示表，并且可能需要数据表能够实现一些数据筛选、排序等能够定制展现方式功能，也包括对表的样式美观会有一些需求。而这些全部都已经由Javascript的一个库——Datatables做到了，我们只需要学习一下这个库的使用，就可以轻松地做出比较美观，功能全面，高度可定制化的表格。

[Datatables中文网站](http://datatables.club/)

[Datatables官方站](http://datatables.net/)

# 开始

官方提供的简单demo如下。只要引入JQUERY库以及DT(Datatables)的css和js三个文件就可以开始使用DT了。

```
<!--第一步：引入Javascript / CSS （CDN）-->
<!-- DataTables CSS -->
<link rel="stylesheet" type="text/css" href="http://cdn.datatables.net/1.10.15/css/jquery.dataTables.css">
 
<!-- jQuery -->
<script type="text/javascript" charset="utf8" src="http://code.jquery.com/jquery-1.10.2.min.js"></script>
 
<!-- DataTables -->
<script type="text/javascript" charset="utf8" src="http://cdn.datatables.net/1.10.15/js/jquery.dataTables.js"></script>
 
 
<!--或者下载到本地，下面有下载地址-->
<!-- DataTables CSS -->
<link rel="stylesheet" type="text/css" href="DataTables-1.10.15/media/css/jquery.dataTables.css">
 
<!-- jQuery -->
<script type="text/javascript" charset="utf8" src="DataTables-1.10.15/media/js/jquery.js"></script>
 
<!-- DataTables -->
<script type="text/javascript" charset="utf8" src="DataTables-1.10.15/media/js/jquery.dataTables.js"></script>
 
 
 
 
<!--第二步：添加如下 HTML 代码-->
<table id="table_id_example" class="display">
    <thead>
        <tr>
            <th>Column 1</th>
            <th>Column 2</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>Row 1 Data 1</td>
            <td>Row 1 Data 2</td>
        </tr>
        <tr>
            <td>Row 2 Data 1</td>
            <td>Row 2 Data 2</td>
        </tr>
    </tbody>
</table>
 
 
 
<!--第三步：初始化Datatables-->
$(document).ready( function () {
    $('#table_id_example').DataTable();
} );
```

<!--第一步：引入Javascript / CSS （CDN）-->
<!-- DataTables CSS -->
<link rel="stylesheet" type="text/css" href="http://cdn.datatables.net/1.10.15/css/jquery.dataTables.css">
 
<!-- jQuery -->
<script type="text/javascript" charset="utf8" src="http://code.jquery.com/jquery-1.10.2.min.js"></script>
 
<!-- DataTables -->
<script type="text/javascript" charset="utf8" src="http://cdn.datatables.net/1.10.15/js/jquery.dataTables.js"></script>
 
生成的表格效果如下：
![这里写图片描述](http://img.blog.csdn.net/20170905184439159?watermark/2/text/aHR0cDovL2Jsb2cuY3Nkbi5uZXQvcXFfMzI2OTA5OTk=/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70/gravity/SouthEast)

可以通过下拉框选择每页表格展示的记录条数，并通过右下方的按钮进行翻页；可以通过点击列旁边的按钮改变记录的排序;也可以在search框直接输入文字查询相关记录（搜索所有列的内容）。大家可以实际在[这里](http://datatables.club/example/basic_init/zero_configuration.html)感受一下。


# 定制自己的table

DT的一个比较突出的地方时它具有比较方便进行定制的特点，也就是你可以很简单地控制table要哪些控件，不要哪些控件，能提供哪些功能，不能提供哪些。

```
DataTables是一个可高度配置化的类库，可以在生成HTML tables过程中的所有方面实现定制。所有特性可以通过打开、关闭或者定制来满足你对表格所有的要求。 定制要先定义一个options，然后传入$().DataTable()构造函数，通过定制options的内容来实现定制。 - 例如下面的代码 scrollYOption 和 pagingOption 选项用来允许滚动和禁止分页：


$('#myTable').DataTable( {
       scrollY: 300,
       paging: false
   } );
```

如上所述，只要在DT表的初始化函数里面用键值对的方式去对DT表的一些特性进行配置，就可以完成对生成表格的定制。很多的特性都是bool型的，用true和false就可以完成绝大多数的功能控制，就像开关一样简单。其它的就基本是一些数值类型的值配置。

再看一下这个例子：

```
$('#myTable').DataTable( {
            searching: false,
            ordering:  false
        } );
```

生成的表格效果如下：

![这里写图片描述](http://img.blog.csdn.net/20170905185909906?watermark/2/text/aHR0cDovL2Jsb2cuY3Nkbi5uZXQvcXFfMzI2OTA5OTk=/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70/gravity/SouthEast)

可以看到，表格右上角的搜索框没了，列旁边的排序按钮也没了，因为我们在初始化函数里已经把这两个功能关闭了！so easy！

DT表的所有可配置选项在[这里](http://datatables.club/reference/option/)，以下是一些比较常用的选项：

|选项|作用|
|--|--|
| jQueryUIOption | 控制是否使用jquerui的样式（需要引入jqueryui的css）|
|infoOption | 控制是否显示表格左下角的信息|
|lengthChangeOption | 是否允许用户改变表格每页显示的记录数|
|orderingOption | 是否允许Datatables开启排序|
|pagingOption|  是否开启本地分页|
|processingOption|是否显示处理状态(排序的时候，数据很多耗费时间长的话，也会显示这个)|
|scrollXOption|设置水平滚动|
|scrollYOption|设置垂直滚动|
|searchingOption|是否允许Datatables开启本地搜索|
|serverSideOption|是否开启服务器模式|
|stateSaveOption|保存状态 - 在页面重新加载的时候恢复状态（页码等内容）|
|autoWidthOption|控制Datatables是否自适应宽度|
|deferRenderOption|控制Datatables的延迟渲染，可以提高初始化的速度|



不过注意，如果配置时不小心把属性拼写错了，或者用到了DT表本身没有的属性，那么表格会变回普通的HTML原生表格的样式，这时回头检查一下刚才的配置哪里错了就行。


更具体的使用方式大家去看[官网的手册](http://datatables.club/manual/#data)就好啦！




