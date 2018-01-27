[toc]

# HTTP请求

## 概念

### HTTP

HTTP(HyperText Transfer Protocol，又称超文本传输协议)是一套计算机通过网络进行通信的规则。计算机专家设计出HTTP，使HTTP客户端（如Web浏览器）能够从HTTP服务器(Web服务器)请求信息和服务，HTTP目前协议的版本是1.1。

HTTP是一种**无状态**的协议，无状态是指Web浏览器和Web服务器之间不需要建立持久的连接，这意味着当一个客户端向服务器端发出请求，然后Web服务器返回响应(response)，**连接就被关闭了**，在服务器端不保留连接的有关信息。这种数据通信方式称之为**请求(Request)/应答(Response)模型**：Web浏览器向Web服务器发送请求，Web服务器处理请求并返回适当的应答。所有HTTP连接都被构造成一套请求和应答。

**HTTP使用内容类型**，是指Web服务器向Web浏览器返回的文件都有与之相关的类型。所有这些类型在MIME　Internet邮件协议上模型化，即Web服务器告诉Web浏览器该文件所具有的种类，是HTML文档、GIF格式图像、声音文件还是独立的应用程序。大多数Web浏览器都拥有一系列的可配置的辅助应用程序，它们告诉浏览器应该如何处理Web服务器发送过来的各种内容类型。

## HTTP请求流程/通信机制

HTTP通信机制是在一次完整的HTTP通信过程中，Web浏览器与Web服务器之间将完成下列7个步骤：

1.建立TCP连接

在HTTP工作开始之前，Web浏览器首先要通过网络与Web服务器建立连接，该连接是通过TCP来完成的，该协议与IP协议共同构建Internet，即著名的TCP/IP协议族，因此Internet又被称作是TCP/IP网络。HTTP是比TCP更高层次的应用层协议，根据规则，**只有低层协议建立之后才能进行更高层协议的连接**，因此，首先要建立TCP连接。

2.Web浏览器向Web服务器发送请求命令

一旦建立了TCP连接，Web浏览器就会向Web服务器发送请求命令，例如：
```
GET/sample/hello.jsp HTTP/1.1
```

3.Web浏览器发送请求头信息

浏览器发送其请求命令之后，还要以**头信息**的形式向Web服务器发送一些别的信息，之后浏览器发送了一**空白行**来通知服务器，它已经结束了该头信息的发送。

4.Web服务器应答

客户机向服务器发出请求后，服务器会客户机回送应答，
```
HTTP/1.1 200 OK
```
应答的第一部分是协议的版本号和应答状态码

5.Web服务器发送应答头信息

正如客户端会随同请求发送关于自身的信息一样，服务器也会随同应答向用户发送关于它自己的数据及被请求的文档。

6.Web服务器向浏览器发送数据

Web服务器向浏览器发送头信息后，它会发送一个空白行来表示头信息的发送到此为结束，接着，**它就以Content-Type应答头信息所描述的格式**发送用户所请求的实际数据。

7.Web服务器关闭TCP连接

一般情况下，一旦Web服务器向浏览器发送了请求数据，它就要关闭TCP连接，然后如果浏览器或者服务器在其头信息加入了这行代码：
```
Connection:keep-alive
```
TCP连接在发送后将仍然保持打开状态，于是，浏览器可以继续通过相同的连接发送请求。保持连接节省了为每个请求建立新连接所需的时间，还节约了网络带宽。

## HTTP请求格式


### 客户端请求格式

当浏览器向Web服务器发出请求时，它向服务器传递了一个数据块，也就是请求信息，HTTP请求信息由3部分组成：

- 请求方法/URI协议/版本
- 请求头(Request Header)
- 请求正文(Request Body)

下面是一个HTTP请求的例子：

```
GET/sample.jspHTTP/1.1 // 请求方法/URI协议/版本

Accept:image/gif.image/jpeg,*/*  // 请求头(Request Header)
Accept-Language:zh-cn
Connection:Keep-Alive
Host:localhost
User-Agent:Mozila/4.0(compatible;MSIE5.01;Window NT5.0)
Accept-Encoding:gzip,deflate
 
username=jinqiao&password=1234 // 请求正文(Request Body)
```

1.请求方法/URI协议/版本

请求的第一行是“请求方法/URL协议/版本”：
```
GET/sample.jsp HTTP/1.1
```

以上代码中“GET”代表请求方法，“/sample.jsp”表示URI，“HTTP/1.1代表协议和协议的版本。

根据HTTP标准，HTTP请求可以使用多种请求方法。例如：HTTP1.1支持7种请求方法：GET、POST、HEAD、OPTIONS、PUT、DELETE和TARCE。在Internet应用中，最常用的方法是GET和POST。

URL完整地指定了要访问的网络资源，通常只要给出相对于服务器的根目录的相对目录即可，因此总是以“/”开头，最后，协议版本声明了通信过程中使用HTTP的版本。


2.请求头(Request Header)

请求头**包含许多有关的客户端环境和请求正文的有用信息**。例如，请求头可以声明浏览器所用的语言，请求正文的长度等。
```
Accept:image/gif.image/jpeg.*/* //请求数据格式
Accept-Language:zh-cn //浏览器所用语言
Connection:Keep-Alive //维持TCP连接
Host:localhost
User-Agent:Mozila/4.0(compatible:MSIE5.01:Windows NT5.0) //用户代理，即所用浏览器信息
Accept-Encoding:gzip,deflate. //接受编码
```

3.请求正文

请求头和请求正文之间是一个空行，这个行非常重要，**它表示请求头已经结束**，接下来的是请求正文。请求正文中可以包含客户提交的查询字符串信息：
```
username=jinqiao&password=1234
```
在以上的例子的HTTP请求中，请求的正文只有一行内容。当然，在实际应用中，HTTP请求正文可以包含更多的内容。


#### HTTP请求方法

这里只讨论最常用的GET方法与POST方法的异同。

##### GET

GET方法是默认的HTTP请求方法，我们日常用GET方法来提交表单数据，然而用GET方法提交的表单数据只经过了简单的编码，同时它**将作为URL的一部分向Web服务器发送**，因此，如果使用GET方法来提交表单数据就存在着安全隐患上。例如
```
Http://127.0.0.1/login.jsp?Name=zhangshi&Age=30&Submit=%cc%E+%BD%BB
```

从上面的URL请求中，很容易就可以辩认出表单提交的内容，包括姓名为zhangshi，年龄为30等（？之后的内容）。另外由于GET方法提交的数据是作为URL请求的一部分所以提交的数据量不能太大。

各种浏览器也会对url的长度有所限制，下面是几种常见浏览器的url长度限制：

|浏览器|限制（单位：字符）|
|--|--|
|IE | 2803|
|Firefox|65536|
|Chrome|8182|
|Safari|80000|
|Opera|190000 |

##### POST

POST方法是GET方法的一个替代方法，它主要是向Web服务器提交表单数据，尤其是大批量的数据。POST方法克服了GET方法的一些缺点。通过POST方法提交表单数据时，**数据不是作为URL请求的一部分而是作为标准数据传送给Web服务器，这就克服了GET方法中的信息无法保密和数据量太小的缺点**。因此，出于安全的考虑以及对用户隐私的尊重，通常表单提交时采用POST方法。

从编程的角度来讲，如果用户通过GET方法提交数据，则数据存放在QUERY＿STRING环境变量中，而POST方法提交的数据则可以从标准输入流中获取。

## 服务端应答格式

HTTP应答与HTTP请求相似，HTTP响应也由3个部分构成，分别是：

- 协议状态版本代码描述
- 响应头(Response Header)
- 响应正文

下面是一个HTTP响应的例子：
```
HTTP/1.1 200 OK
Server:Apache Tomcat/5.0.12
Date:Mon,6Oct2003 13:23:42 GMT
Content-Length:112
 
<html>
<head>
<title>HTTP响应示例<title>
</head>
<body>
Hello HTTP!
</body>
</html>
```

协议状态代码描述HTTP响应的第一行类似于HTTP请求的第一行，它表示通信所用的协议是HTTP1.1服务器已经成功的处理了客户端发出的请求（200表示成功）:

```
HTTP/1.1 200 OK
```

### 响应头(Response Header)

响应头也和请求头一样包含许多有用的信息，例如服务器类型、日期时间、内容类型和长度等：
```
Server:Apache Tomcat/5.0.12
Date:Mon,6Oct2003 13:13:33 GMT
Content-Type:text/html
Last-Moified:Mon,6 Oct 2003 13:23:42 GMT
Content-Length:112
```

### 响应体(Response Body)

响应正文响应正文就是服务器返回的HTML页面：
```
<html>
<head>
<title>HTTP响应示例<title>
</head>
<body>
Hello HTTP!
</body>
</html>
```

响应头和正文之间也必须用空行分隔。

# Java实现

本部分代码来自：[3][HTTP请求工具类(Java)](http://blog.csdn.net/qduningning/article/details/8864281)

```
import java.io.BufferedReader;  
import java.io.IOException;  
import java.io.InputStreamReader;  
import java.io.PrintWriter;  
import java.net.URL;  
import java.net.URLConnection;  
import java.net.URLEncoder;  
import java.util.Map;  
  
/** 
 * @author Administrator 
 * 
 */  
public class HttpUtil {  
  
    /** 
     * 使用Get方式获取数据 
     *  
     * @param url 
     * URL包括参数，http://HOST/XX?XX=XX&XXX=XXX 
     * @param charset 
     * @return 
     */  
    public static String sendGet(String url, String charset) {  
        String result = "";  
        BufferedReader in = null;  
        try {  
            URL realUrl = new URL(url);  
            // 打开和URL之间的连接  
            URLConnection connection = realUrl.openConnection();  
            // 设置通用的请求属性  
            connection.setRequestProperty("accept", "*/*");  
            connection.setRequestProperty("connection", "Keep-Alive");  
            connection.setRequestProperty("user-agent",  
                    "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1;SV1)");  
            // 建立实际的连接  
            connection.connect();  
            // 定义 BufferedReader输入流来读取URL的响应  
            in = new BufferedReader(new InputStreamReader(  
                    connection.getInputStream(), charset));  
            String line;  
            while ((line = in.readLine()) != null) {  
                result += line;  
            }  
        } catch (Exception e) {  
            System.out.println("发送GET请求出现异常！" + e);  
            e.printStackTrace();  
        }  
        // 使用finally块来关闭输入流  
        finally {  
            try {  
                if (in != null) {  
                    in.close();  
                }  
            } catch (Exception e2) {  
                e2.printStackTrace();  
            }  
        }  
        return result;  
    }  
  
    /**  
     * POST请求，字符串形式数据  
     * @param url 请求地址  
     * @param param 请求数据  
     * @param charset 编码方式  
     */  
    public static String sendPostUrl(String url, String param, String charset) {  
  
        PrintWriter out = null;  
        BufferedReader in = null;  
        String result = "";  
        try {  
            URL realUrl = new URL(url);  
            // 打开和URL之间的连接  
            URLConnection conn = realUrl.openConnection();  
            // 设置通用的请求属性  
            conn.setRequestProperty("accept", "*/*");  
            conn.setRequestProperty("connection", "Keep-Alive");  
            conn.setRequestProperty("user-agent",  
                    "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1;SV1)");  
            // 发送POST请求必须设置如下两行  
            conn.setDoOutput(true);  
            conn.setDoInput(true);  
            // 获取URLConnection对象对应的输出流  
            out = new PrintWriter(conn.getOutputStream());  
            // 发送请求参数  
            out.print(param);  
            // flush输出流的缓冲  
            out.flush();  
            // 定义BufferedReader输入流来读取URL的响应  
            in = new BufferedReader(new InputStreamReader(  
                    conn.getInputStream(), charset));  
            String line;  
            while ((line = in.readLine()) != null) {  
                result += line;  
            }  
        } catch (Exception e) {  
            System.out.println("发送 POST 请求出现异常！" + e);  
            e.printStackTrace();  
        }  
        // 使用finally块来关闭输出流、输入流  
        finally {  
            try {  
                if (out != null) {  
                    out.close();  
                }  
                if (in != null) {  
                    in.close();  
                }  
            } catch (IOException ex) {  
                ex.printStackTrace();  
            }  
        }  
        return result;  
    }  

    /**  
     * POST请求，Map形式数据  
     * @param url 请求地址  
     * @param param 请求数据  
     * @param charset 编码方式  
     */  
    public static String sendPost(String url, Map<String, String> param,  
            String charset) {  
  
        StringBuffer buffer = new StringBuffer();  
        if (param != null && !param.isEmpty()) {  
            for (Map.Entry<String, String> entry : param.entrySet()) {  
                buffer.append(entry.getKey()).append("=")  
                        .append(URLEncoder.encode(entry.getValue()))  
                        .append("&");  
  
            }  
        }  
        buffer.deleteCharAt(buffer.length() - 1);  
  
        PrintWriter out = null;  
        BufferedReader in = null;  
        String result = "";  
        try {  
            URL realUrl = new URL(url);  
            // 打开和URL之间的连接  
            URLConnection conn = realUrl.openConnection();  
            // 设置通用的请求属性  
            conn.setRequestProperty("accept", "*/*");  
            conn.setRequestProperty("connection", "Keep-Alive");  
            conn.setRequestProperty("user-agent",  
                    "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1;SV1)");  
            // 发送POST请求必须设置如下两行  
            conn.setDoOutput(true);  
            conn.setDoInput(true);  
            // 获取URLConnection对象对应的输出流  
            out = new PrintWriter(conn.getOutputStream());  
            // 发送请求参数  
            out.print(buffer);  
            // flush输出流的缓冲  
            out.flush();  
            // 定义BufferedReader输入流来读取URL的响应  
            in = new BufferedReader(new InputStreamReader(  
                    conn.getInputStream(), charset));  
            String line;  
            while ((line = in.readLine()) != null) {  
                result += line;  
            }  
        } catch (Exception e) {  
            System.out.println("发送 POST 请求出现异常！" + e);  
            e.printStackTrace();  
        }  
        // 使用finally块来关闭输出流、输入流  
        finally {  
            try {  
                if (out != null) {  
                    out.close();  
                }  
                if (in != null) {  
                    in.close();  
                }  
            } catch (IOException ex) {  
                ex.printStackTrace();  
            }  
        }  
        return result;  
    }  
    
    public static void main(String[] args) {  
    }  
}  
```


# 参考

[1][ HTTP深入浅出 http请求 ](https://www.cnblogs.com/yin-jingyu/archive/2011/08/01/2123548.html)

[2][HTTP请求详解](http://blog.csdn.net/u012125579/article/details/47426737)

[3][HTTP请求工具类(Java)](http://blog.csdn.net/qduningning/article/details/8864281)