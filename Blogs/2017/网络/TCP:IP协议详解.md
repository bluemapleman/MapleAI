本文转载自[菜鸟教程TCP/IP 教程](http://www.runoob.com/tcpip/tcpip-tutorial.html)

[TOC]

# TCP/IP 教程

TCP/IP 是因特网的通信协议。

TCP/IP 通信协议是对计算机必须遵守的规则的描述，只有遵守这些规则，计算机之间才能进行通信。

您的浏览器与服务器都在使用 TCP/IP 协议

浏览器与服务器使用 TCP/IP 协议来链接因特网。

浏览器使用 TCP/IP 协议进入服务器，服务器使用 TCP/IP 协议来发送 HTML 到浏览器。
您的 E-Mail 使用 TCP/IP 协议

您的电子邮件也通过 TCP/IP 协议来发送和接收邮件。
因特网地址是 TCP/IP 协议

因特网地址比如 "42.120.45.233" 就是一个 TCP/IP 协议。

# TCP/IP 介绍

TCP/IP 是用于因特网 (Internet) 的通信协议。

## 计算机通信协议（Computer Communication Protocol）

计算机通信协议是对那些计算机必须遵守以便彼此通信的的规则的描述。就像人之间交流用一套有规则的语言，计算机之间交流也有一套语言，这些语言也是有规则的，这些规则就是协议。


## 什么是 TCP/IP？

TCP/IP 是供已连接因特网的计算机进行通信的通信协议。

TCP/IP 指传输控制协议/网际协议（Transmission Control Protocol / Internet Protocol）。

TCP/IP 定义了电子设备（比如计算机）如何连入因特网，以及数据如何在它们之间传输的标准。

## 在 TCP/IP 内部

在 TCP/IP 中包含一系列用于处理数据通信的协议：

    TCP (传输控制协议) - 应用程序之间通信
    UDP (用户数据报协议) - 应用程序之间的简单通信
    IP (网际协议) - 计算机之间的通信
    ICMP (因特网消息控制协议) - 针对错误和状态
    DHCP (动态主机配置协议) - 针对动态寻址

## TCP 使用固定的连接

TCP 用于应用程序之间的通信。

当应用程序希望通过 TCP 与另一个应用程序通信时，它会发送一个通信请求。这个请求必须被送到一个确切的地址。在双方"握手"之后，TCP 将在两个应用程序之间建立一个全双工 (full-duplex) 的通信。

这个全双工的通信将占用两个计算机之间的通信线路，直到它被一方或双方关闭为止。

UDP 和 TCP 很相似，但是更简单，同时可靠性低于 TCP。
## IP 是无连接的

IP 用于计算机之间的通信。

IP 是无连接的通信协议。它不会占用两个正在通信的计算机之间的通信线路。这样，IP 就降低了对网络线路的需求。每条线可以同时满足许多不同的计算机之间的通信需要。

通过 IP，消息（或者其他数据）被分割为小的独立的包，并通过因特网在计算机之间传送。

IP 负责将每个包路由至它的目的地。
## IP 路由器

当一个 IP 包从一台计算机被发送，它会到达一个 IP 路由器。

IP 路由器负责将这个包路由至它的目的地，直接地或者通过其他的路由器。

在一个相同的通信中，一个包所经由的路径可能会和其他的包不同。而路由器负责根据通信量、网络中的错误或者其他参数来进行正确地寻址。
## TCP/IP

TCP/IP 意味着 TCP 和 IP 在一起协同工作。

TCP 负责应用软件（比如您的浏览器）和网络软件之间的通信。

IP 负责计算机之间的通信。

TCP 负责将数据分割并装入 IP 包，然后在它们到达的时候重新组合它们。

IP 负责将包发送至接受者。

总结：TCP做数据包，IP负责传数据包。

# TCP/IP 寻址

TCP/IP 使用 32 个比特或者 4 组 0 到 255 之间的数字来为计算机编址。
IP地址

## IP地址

每个计算机必须有一个 IP 地址才能够连入因特网。

每个 IP 包必须有一个地址才能够发送到另一台计算机。

在本教程下一节，您会学习到更多关于 IP 地址和 IP 名称的知识。
## IP 地址包含 4 组数字：

TCP/IP 使用 4 组数字来为计算机编址。每个计算机必须有一个唯一的 4 组数字的地址。

每组数字必须在 0 到 255 之间，并由点号隔开，比如：192.168.1.60。
##32 比特 = 4 字节

TCP/IP 使用 32 个比特来编址。一个计算机字节是 8 比特。所以 TCP/IP 使用了 4 个字节。

一个计算机字节可以包含 256 个不同的值：

00000000、00000001、00000010、00000011、00000100、00000101、00000110、00000111、00001000 ....... 直到 11111111。

现在，您应该知道了为什么 TCP/IP 地址是介于 0 到 255 之间的 4 组数字。
## IP V6

IPv6 是 "Internet Protocol Version 6" 的缩写，也被称作下一代互联网协议，它是由 IETF 小组（Internet 工程任务组Internet Engineering Task Force）设计的用来替代现行的 IPv4（现行的）协议的一种新的 IP 协议。

我们知道，Internet 的主机都有一个唯一的 IP 地址，IP 地址用一个 32 位二进制的数表示一个主机号码，但 32 位地址资源有限，已经不能满足用户的需求了，因此 Internet 研究组织发布新的主机标识方法，即 IPv6。

在 RFC1884 中（RFC 是 Request for Comments document 的缩写。RFC 实际上就是 Internet 有关服务的一些标准），规定的标准语法建议把 IPv6 地址的 128 位（16 个字节）写成 8 个 16 位的无符号整数，每个整数用 4 个十六进制位表示，这些数之间用冒号（:）分开，例如：

686E：8C64：FFFF：FFFF：0：1180：96A：FFFF

冒号十六进制记法允许零压缩，即一串连续的0可以用一对冒号取代，例如：

FF05：0：0：0：0：0：0：B3可以定成：FF05：：B3

为了保证零压缩有一个清晰的解释，建议中规定，在任一地址中，只能使用一次零压缩。该技术对已建议的分配策略特别有用，因为会有许多地址包含连续的零串。

冒号十六进制记法结合有点十进制记法的后缀。这种结合在IPv4向IPv6换阶段特别有用。例如，下面的串是一个合法的冒号十六进制记法：

0：0：0：0：0：0：128.10.1.1

这种记法中，虽然冒号所分隔的每一个值是一个16位的量，但每个分点十进制部分的值则指明一个字节的值。再使用零压缩即可得出：

：：128.10.1.1

## 域名

12 个阿拉伯数字很难记忆。使用一个名称更容易。

用于 TCP/IP 地址的名字被称为域名。runoob.com 就是一个域名。

当你键入一个像 http://www.runoob.com 这样的域名，域名会被一种 DNS 程序翻译为数字。

在全世界，数量庞大的 DNS 服务器被连入因特网。DNS 服务器负责将域名翻译为 TCP/IP 地址，同时负责使用新的域名信息更新彼此的系统。

当一个新的域名连同其 TCP/IP 地址一起注册后，全世界的 DNS 服务器都会对此信息进行更新。


# TCP/IP 协议

TCP/IP 是不同的通信协议的大集合。
## 协议族

TCP/IP 是基于 TCP 和 IP 这两个最初的协议之上的不同的通信协议的大集合。
TCP - 传输控制协议

TCP 用于从应用程序到网络的数据传输控制。

TCP 负责在数据传送之前将它们分割为 IP 包，然后在它们到达的时候将它们重组。
IP - 网际协议（Internet Protocol）

IP 负责计算机之间的通信。

IP 负责在因特网上发送和接收数据包。
HTTP - 超文本传输协议(Hyper Text Transfer Protocol)

HTTP 负责 web 服务器与 web 浏览器之间的通信。

HTTP 用于从 web 客户端（浏览器）向 web 服务器发送请求，并从 web 服务器向 web 客户端返回内容（网页）。
HTTPS - 安全的 HTTP（Secure HTTP）

HTTPS 负责在 web 服务器和 web 浏览器之间的安全通信。

作为有代表性的应用，HTTPS 会用于处理信用卡交易和其他的敏感数据。
SSL - 安全套接字层（Secure Sockets Layer）

SSL 协议用于为安全数据传输加密数据。
SMTP - 简易邮件传输协议（Simple Mail Transfer Protocol）

SMTP 用于电子邮件的传输。
MIME - 多用途因特网邮件扩展（Multi-purpose Internet Mail Extensions）

MIME 协议使 SMTP 有能力通过 TCP/IP 网络传输多媒体文件，包括声音、视频和二进制数据。
IMAP - 因特网消息访问协议（Internet Message Access Protocol）

IMAP 用于存储和取回电子邮件。
POP - 邮局协议（Post Office Protocol）

POP 用于从电子邮件服务器向个人电脑下载电子邮件。
FTP - 文件传输协议（File Transfer Protocol）

FTP 负责计算机之间的文件传输。
NTP - 网络时间协议（Network Time Protocol）

NTP 用于在计算机之间同步时间（钟）。
DHCP - 动态主机配置协议（Dynamic Host Configuration Protocol）

DHCP 用于向网络中的计算机分配动态 IP 地址。
SNMP - 简单网络管理协议（Simple Network Management Protocol）

SNMP 用于计算机网络的管理。
LDAP - 轻量级的目录访问协议（Lightweight Directory Access Protocol）

LDAP 用于从因特网搜集关于用户和电子邮件地址的信息。
ICMP - 因特网消息控制协议（Internet Control Message Protocol）

ICMP 负责网络中的错误处理。
ARP - 地址解析协议（Address Resolution Protocol）

ARP - 用于通过 IP 来查找基于 IP 地址的计算机网卡的硬件地址。
RARP - 反向地址转换协议（Reverse Address Resolution Protocol）

RARP 用于通过 IP 查找基于硬件地址的计算机网卡的 IP 地址。
BOOTP - 自举协议（Boot Protocol）

BOOTP 用于从网络启动计算机。
PPTP - 点对点隧道协议（Point to Point Tunneling Protocol）

PPTP 用于私人网络之间的连接（隧道）。
