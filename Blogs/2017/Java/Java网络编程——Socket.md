网络是连接不同计算机的媒介，不同的计算机依靠网络来互相通信，即传递数据。

Java中与网络编程相关的部分主要是Socket（套接字），它作为一种抽象的结构，实现了与通信相关的各类方法，构成一套完整的通信机制。

当然，Socket本身是独立于编程语言之上的概念，就像数据结构与算法一样，它并不属于Java，而是一种公认的通信的解决方案，大部分语言都实现了与socket相关的通信功能。

# 原理

Socket通过使用TCP（传输控制协议）提供了两台计算机之间的通信机制。具体的方式是：服务器处会首先创建ServerSocket对象，并使其处于监听本地某端口状态，而客户端通过创建一个Socket去连接服务端上的对应端口，于是连接建立，服务端的ServerSocket的accept方法会返回一个Socket对象，现在两台机器就可以都通过Socket对象的标准写入和读取方法来进行通信了。

完整步骤如下：
- 服务器实例化一个 ServerSocket 对象，表示通过服务器上的端口通信。
- 服务器调用 ServerSocket 类的 accept() 方法，该方法将一直等待，直到客户端连接到服务器上给定的端口。
-  服务器正在等待时，一个客户端实例化一个 Socket 对象，指定服务器名称和端口号来请求连接。
- Socket 类的构造函数试图将客户端连接到指定的服务器和端口号。如果通信被建立，则在客户端创建一个 Socket 对象能够与服务器进行通信。
- 在服务器端，accept() 方法返回服务器上一个新的 socket 引用，该 socket 连接到客户端的 socket。



# Java实现

## 服务端——ServerSocket

服务端首先实例化一个ServerSocket类对象，该对象需要调用accept（）方法监听本地的一个端口，之后便进入阻塞状态，直到客户端的Socket的连接请求到来。

ServerSocket 类的方法：

|方法|描述|
|--------|
|public ServerSocket(int port) throws IOException|创建绑定到特定端口的服务器套接字。|
|public ServerSocket(int port, int backlog) throws IOException|利用指定的 backlog 创建服务器套接字并将其绑定到指定的本地端口号。|
|public ServerSocket(int port, int backlog, InetAddress address) throws IOException|使用指定的端口、侦听 backlog 和要绑定到的本地 IP 地址创建服务器。|
|public ServerSocket() throws IOException|创建非绑定服务器套接字。创建非绑定服务器套接字。 如果 ServerSocket 构造方法没有抛出异常，就意味着你的应用程序已经成功绑定到指定的端口，并且侦听客户端请求。|

一般使用的最多的是第一种构造方法，即新建ServerSocket，并让其直接监听本地的某一端口。

还有一些 ServerSocket 类的常用方法：

|方法|描述|
|-----|--|
|public int getLocalPort()| 返回此套接字在其上侦听的端口。|
|public Socket accept() throws IOException|侦听并接受到此套接字的连接。|
|public void setSoTimeout(int timeout)|通过指定超时值启用/禁用 SO_TIMEOUT，以毫秒为单位。|
|public void bind(SocketAddress host, int backlog)|将 ServerSocket 绑定到特定地址（IP 地址和端口号）。|

## 客户端

客户端直接进行Socket类的实例化，并尝试连接服务器的对应端口。

首先看Socket类的构造方法。

|方法|描述|
|--|--|
|public Socket(String host, int port) throws UnknownHostException, IOException.|创建一个流套接字并将其连接到指定主机上的指定端口号。|
|public Socket(InetAddress host, int port) throws IOException|创建一个流套接字并将其连接到指定 IP 地址的指定端口号。|
|public Socket(String host, int port, InetAddress localAddress, int localPort) throws IOException.|创建一个套接字并将其连接到指定远程主机上的指定远程端口。|
|public Socket(InetAddress host, int port, InetAddress localAddress, int localPort) throws IOException.|创建一个套接字并将其连接到指定远程地址上的指定远程端口。|
|public Socket()|通过系统默认类型的 SocketImpl 创建未连接套接字|

而Socket在构造后，其实会首先自动地去尝试连接指定的服务器与端口。

## 连接建立

连接建立后，两边的Socket就可以开始自由交流了，交流过程中，两边的Socket对象本质都一样了（服务端的ServerSocket调用accept（）方法后已经返回了Socket对象，因此服务端现在也是一个Socket对象在进行交流）。

下面是通信过程中socket对象可以调用的一些方法：

|方法|描述|
|--|--|
|public void connect(SocketAddress host, int timeout) throws IOException|将此套接字连接到服务器，并指定一个超时值。|
|public InetAddress getInetAddress()| 返回套接字连接的地址。|
|public int getPort()|返回此套接字连接到的远程端口。|
|public int getLocalPort()|返回此套接字绑定到的本地端口。|
|public SocketAddress getRemoteSocketAddress()|返回此套接字连接的端点的地址，如果未连接则返回 null。|
|public InputStream getInputStream() throws IOException|返回此套接字的输入流。|
|public OutputStream getOutputStream() throws IOException|返回此套接字的输出流。|
|public void close() throws IOException|关闭此套接字。|


# 实例
Server类：

    /**
     * 
     */
    package socket;
    
    import java.io.PrintStream;
    import java.net.ServerSocket;
    import java.net.Socket;
    
    /**
     * @author Tom Qian
     * @email tomqianmaple@outlook.com
     * @github https://github.com/bluemapleman
     * @date 2017年8月18日
     */
     
    public class Server
    {
        private static int port=10000; 
        private static String ip="127.0.0.1";
        
        /**
         * @param args
         */
        public static void main(String[] args) throws Exception
        {
            ServerSocket ss=new ServerSocket(10000);
            while(true){
                Socket s=ss.accept();
                PrintStream ps=new PrintStream(s.getOutputStream());
                ps.print("您好，您收到了服务器的新年祝福！");
                
                ps.close();
                s.close();
            }
    
        }
    
    }


Client类：
    
    /**
     * @author Tom Qian
     * @email tomqianmaple@outlook.com
     * @github https://github.com/bluemapleman
     * @date 2017年8月18日
     */
    package socket;
    
    import java.io.BufferedReader;
    import java.io.InputStreamReader;
    import java.net.Socket;
    
    public class Client
    {
    
        /**
         * @param args
         */
        public static void main(String[] args) throws Exception
        {
            int port=10000;
            Socket socket=new Socket("127.0.0.1",port);
            BufferedReader br=new BufferedReader(new InputStreamReader(socket.getInputStream()));
            String line=br.readLine();
            System.out.println("来自服务器的数据："+line);
            br.close();
            socket.close();
    
        }
    
    }

先启动Server类，再启动Client类（否则Client这边会报ConnectException，拒绝连接错误！当然啦！服务端那边连个收信员都没有，你的信怎么可能发的过去呢？），效果如下：

![这里写图片描述](http://img.blog.csdn.net/20170825180838712?watermark/2/text/aHR0cDovL2Jsb2cuY3Nkbi5uZXQvcXFfMzI2OTA5OTk=/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70/gravity/SouthEast)



本文参考：
[1] [菜鸟教程——Java网络编程](http://www.runoob.com/java/java-networking.html)