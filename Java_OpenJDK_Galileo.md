# Introduction #
How to install the full SDK on Galileo

http://ccc.ntu.edu.tw/index.php/news/40

The image here

http://eem.bime.ntu.edu.tw/resource/clchuang/Clanton_Full_SDK_OpenJDK6_Tomcat7.7z
# Details #

1. download the image:

http://eem.bime.ntu.edu.tw/resource/clchuang/Clanton_Full_SDK_OpenJDK6_Tomcat7.7z

2. Follow the instruction in here to install that image.

https://communities.intel.com/servlet/JiveServlet/downloadBody/22204-102-1-25429/Galileo_GettingStarted_329685_005.pdf

3. Put the SD card and boot and waiting until the light of SD is completed off. ( for safe, wait 20 mins)

4. Turn off. connect LAN from router to it. turn on. wait to SD light is off.

5. Find the IP of the clanton.:

```
hai@hai-Inspiron-1545:~$ avahi-browse -a -t -d local
+   eth1 IPv6 hai-Inspiron-1545 [00:26:5e:1d:59:d8]         Workstation          local
+   eth1 IPv4 clanton [98:4f:ee:00:6d:16]                   Workstation          local
+   eth1 IPv4 hai-Inspiron-1545 [00:26:5e:1d:59:d8]         Workstation          local
+   eth1 IPv6 hai-Inspiron-1545                             Remote Disk Management local
+   eth1 IPv4 hai-Inspiron-1545                             Remote Disk Management local
+   eth1 IPv4 OProfile on clanton                           _oprofile._tcp       local
+   eth1 IPv4 clanton                                       SSH Remote Terminal  local
+   eth1 IPv4 clanton                                       SFTP File Transfer   local
hai@hai-Inspiron-1545:~$ avahi-discover
Browsing domain 'local' on -1.-1 ...
Browsing for services of type '_workstation._tcp' in domain 'local' on 3.1 ...
Browsing for services of type '_udisks-ssh._tcp' in domain 'local' on 3.1 ...
Browsing for services of type '_oprofile._tcp' in domain 'local' on 3.0 ...
Browsing for services of type '_ssh._tcp' in domain 'local' on 3.0 ...
Browsing for services of type '_sftp-ssh._tcp' in domain 'local' on 3.0 ...
Browsing for services of type '_workstation._tcp' in domain 'local' on 3.0 ...
Browsing for services of type '_udisks-ssh._tcp' in domain 'local' on 3.0 ...
Found service 'hai-Inspiron-1545 [00:26:5e:1d:59:d8]' of type '_workstation._tcp' in domain 'local' on 3.1.
Found service 'hai-Inspiron-1545' of type '_udisks-ssh._tcp' in domain 'local' on 3.1.
Found service 'OProfile on clanton' of type '_oprofile._tcp' in domain 'local' on 3.0.
Found service 'clanton' of type '_ssh._tcp' in domain 'local' on 3.0.
Found service 'clanton' of type '_sftp-ssh._tcp' in domain 'local' on 3.0.
Found service 'clanton [98:4f:ee:00:6d:16]' of type '_workstation._tcp' in domain 'local' on 3.0.
Found service 'hai-Inspiron-1545 [00:26:5e:1d:59:d8]' of type '_workstation._tcp' in domain 'local' on 3.0.
Found service 'hai-Inspiron-1545' of type '_udisks-ssh._tcp' in domain 'local' on 3.0.
Service data for service 'clanton [98:4f:ee:00:6d:16]' of type '_workstation._tcp' in domain 'local' on 3.0:
	Host clanton.local (*192.168.0.103*), port 9, TXT data: []
Service data for service 'clanton [98:4f:ee:00:6d:16]' of type '_workstation._tcp' in domain 'local' on 3.0:
	Host clanton.local (fe80::9a4f:eeff:fe00:6d16), port 9, TXT data: []
^[

```


In here the clanton has IP: 192.168.0.103

6. check java version + nodeJS ....

```
hai@hai-Inspiron-1545:~$ ssh root@192.168.0.103
root@clanton:~# ls
apache-tomcat-7.0.47  apache-tomcat-7.0.47-embed  lib.tar.gz  openjdk.tar.gz  tomcat-7-full.tar.gz  tomcat-7.tar.gz
root@clanton:~# java -version
java version "1.6.0_24"
OpenJDK Runtime Environment (IcedTea6 1.11.9) (6b24-1.11.9)
OpenJDK Zero VM (build 20.0-b12, interpreted mode)
root@clanton:~# node -version
Error: unrecognized flag -version
Try --help for options

> console.log("hai")
hai
undefined
> 
(^C again to quit)
> 
root@clanton:~# exit

```
---
Add your content here.  Format your content with:
  * Text in **bold** or _italic_
  * Headings, paragraphs, and lists
  * Automatic links to other wiki pages