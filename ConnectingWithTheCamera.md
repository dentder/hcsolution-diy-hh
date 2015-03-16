# What We Know #

  1. The target camera to be used is the existing department's Nikon Coolpix P300
  1. This camera uses PTP protocol and does not mount using the USB Mass Storage protocol (like Flash thumb drives)
  1. An open source library and commandline, libgphoto2 and gphoto2 respectively, are available and has been used on RasberryPi
  * http://www.gphoto.org/
  1. We can access the microSD card as it is mounted in /media/mmcblk0p1
  * I copied a few jpg files and one png file to the microSD card using the SD converter directly connected to my laptop but have not checked the files are actually there in the Linux commandline

# What We Don't Know #

  1. Why the other Linux image had so much issues with compilation

# What I've accomplished so far #

> ## Creating the Linux image ##
> > Downloaded LINUX\_IMAGE\_FOR\_SD\_Intel\_Galileo\_v0.7.5.7z from: https://downloadcenter.intel.com/Detail_Desc.aspx?agr=Y&DwnldID=23171
> > Extracted image to 4GB microSD card
> > Didn't work!!!
> > followed instructions to create boot partition (see Image 1 on sidebar)
> > Then it booted up from the microSD card (take a while) and the Blink sketch was retained after reboot!

> ## Problems with unable to upload Sketches ##
> > There seems to be a bug with Arduino 1.5.3 and the Yocto 0.7.5 image that causes  it to hang. Found the procedure to recover from here: https://communities.intel.com/thread/48975?start=0&tstart=0
> > > IDE hangs on:
> > > > echo "Deleting existing sketch on target" $fixed\_path/lsz.exe --escape -c "mv -f /sketch/sketch.elf /sketch/sketch.elf.old" <> $tty\_port\_id 1>&0

> > > Procedure to recover:
> > > > Exiting the Arduino IDE
> > > > Killing the lsz.exe process
> > > > Rebooting the Galileo (unplug power)

> ## Establishing communications with the Linux partition ##
> > use Poor Man's Telnet sketch from here: https://communities.intel.com/thread/48654?start=0&tstart=0
> > > upload sketch
> > > open up Serial Monitor
> > > set line terminator to Carriage Return
> > > set baud rate to 115200
> > > tested by using the following commands:
> > > > uname -a
> > > > ls
> > > > mkdir Melvin
> > > > ls
> > > > rmdir Melvin
> > > > ls

> > > This method is limited though: "The script always spawns a new child prcess. The child process executes the cd command and then dies." but at least I know now that the Linux image is alive and working

> > To get full communications we'll need to establish connection via Ethernet or serial cable... https://communities.intel.com/message/212631#212631
> > > I don't have a serial cable, USB-to-serial converter or a computer that has a serial port so we'll shelve that option for now. We'll go for the Ethernet connection
> > > I can't get StartEthernet.ino to work for me both in the office or home network to establish an SSH connection.
> > > Telnet worked: https://communities.intel.com/message/208564#208564 Yay!
> > > > Establishes a telnet connection using putty
> > > > Tested working in both direct laptop connection and home network connection modes (on my home laptop)
> > > > Make sure to know the subnet and available ipaddress to use
> > > > > I tried just letting the network assign dynamic IP using DHCP but it didn't work
> > > > > Setting static ip worked on my home network:
> > > > > > system("ifconfig eth0 192.168.11.88 netmask 255.255.255.0 up");

> > > > Select telnet in putty and type in the ipaddress and I was able to get full access to the Linux commandline interface!
> > > > ### Now to get this to work in the office using the work laptop... the saga continues ###

> > > Using this sketch worked for me: accessing via SSH in Unbuntu 12.04
```
#include <SPI.h>
#include <Ethernet.h>
// Netwoking ver 2. Nguyen Hoang Hai.
// network configuration. dns server, gateway and subnet are optional.

byte mac[] = { 0x98, 0x4F, 0xEE, 0x00, 0x6D, 0x16 }; // Galileo MAC address
//the IP address for the Galileo: (will be used if there’s no DHCP server on your network)
IPAddress ip(192, 168, 11, 11);
boolean Networking;

// the dns server ip
IPAddress dnServer(192, 168, 11, 1);
// the router's gateway address:
IPAddress gateway(192, 168, 11, 1);
// the subnet:
IPAddress subnet(255, 255, 255, 0);

//the IP address is dependent on your network
int led = 13;

void setup() {
  Serial.begin(9600);

  // initialize the ethernet device
  Ethernet.begin(mac, ip, dnServer, gateway, subnet);
  //print out the IP address
  Serial.print("IP = ");
  Serial.println(Ethernet.localIP());
  pinMode(led, OUTPUT); // setting led for
}

void loop() {
  // blink so that you know your board is work
  digitalWrite(led, HIGH);   // turn the LED on (HIGH is the voltage level)
  delay(200);               // wait for a second
  digitalWrite(led, LOW);    // turn the LED off by making the voltage LOW
  delay(200); 
  // end of blink
  Serial.print("IP = ");
  Serial.println(Ethernet.localIP()); // tell the local IP
}
```

> ## Establishing connection with the camera though USB ##
> > Although my research on the Internet and actually checking the USB descriptors indicate that this camera indeed uses PTP and not the USB Mass Storage protocol I still had to try...
> > First was to learn to mount a Flash drive to establish a frame of reference
> > > Using a USB-to-go cable I bought for my Android phone, I connected my 32GB Sandisk Cruzer flash thumb drive and the kernel recognized it as a USB Mass Storage device in /dev/sda1 by checking the kernel log via the dmesg Linux command (or lsusb)
> > > I was able to mount it to a directory I created called /flashdrive using mount /dev/sda1 /flashdrive https://www.suse.com/communities/conversations/manually-mounting-a-usb-flash-drive-in-linux/

> > I tried plugging-in the Nikon Coolpix P300 but, as expected, it was not recognized as a USB Mass Storage Device. I tried with 3 other cameras, 2 Canon and 1 Olympus, lying around in the house hoping one of them might work. Unfortunately, all of them use PTP
> > I tried running gphoto2 but the command is not found. Obviously this was not installed in the stock Yocto Linux image 0.7.5
> > ### Need to ask for help if someone has an image with gphoto2 installed or learn to do it myself!!! ###
## Compiling gphoto2 into the linux image ##
  1. i replaced the 0.7.5 linux image with one that has compiling capability https://communities.intel.com/message/228273
  1. downloaded the source code for libgphoto2 and gphoto2
  1. copied the source code into the image
  1. tried to `./configure` and got this error message:
```
root@clanton:/media/mmcblk0p1/libgphoto2-2.5.4# ./configure
checking for a BSD-compatible install... /usr/bin/install -c
checking whether build environment is sane... configure: error: newly created file is older than distributed files!
Check your system clock
```
  1. seems like the system clock is not set correctly... after some quick research this is expected since we dont have a battery installed to retain a "real" clock.
  1. tried running `ntpupdate pool.ntp.org` but got this:
```
root@clanton:/media/mmcblk0p1/libgphoto2-2.5.4# ntpdate pool.ntp.org
Error resolving pool.ntp.org: Name or service not known (-2)
11 Mar 23:09:54 ntpdate[1679]: Can't find host pool.ntp.org: Name or service not known (-2)
11 Mar 23:09:54 ntpdate[1679]: no servers can be used, exiting
```
  1. set the date using `date -s "10 APR 2014 18:46:00"`
  1. tried `./configure` again and got to here:
```
checking ltdl.h usability... no
checking ltdl.h presence... no
checking for ltdl.h... no
checking that we can compile and link with libltdl... no
configure: error: cannot compile and link against libltdl
libgphoto2 requires libltdl (the libtool dl* library),
but cannot compile and link against it.
```
  1. downloaded `libtools` from http://ossm.utm.my/gnu/libtool/libtool-2.4.2.tar.gz
  1. copied to SD card
  1. run `./configure` no errors!
  1. run `make`
  1. run `make install`
  1. now back to libgphoto2
  1. run `date -s "10 APR 2014 18:46:00"`
  1. run `./configure`, `make`, and `make install`
> > errors at the end of make install:
```
make[1]: Entering directory `/media/mmcblk0p1/libgphoto2-2.5.4'
make[2]: Entering directory `/media/mmcblk0p1/libgphoto2-2.5.4'
 /bin/mkdir -p '/usr/local/bin'
 /usr/bin/install -c gphoto2-config '/usr/local/bin'
rm -f /usr/local/include/gphoto2/gphoto2
rm: cannot remove '/usr/local/include/gphoto2/gphoto2': Is a directory
make[2]: *** [install-data-local] Error 1
make[2]: Leaving directory `/media/mmcblk0p1/libgphoto2-2.5.4'
make[1]: *** [install-am] Error 2
make[1]: Leaving directory `/media/mmcblk0p1/libgphoto2-2.5.4'
make: *** [install-recursive] Error 1
```
  1. now onto `gphoto2`
  1. run `./configure`, `make`, and `make install`
> > error during ./configure
```
checking popt.h usability... no
checking popt.h presence... no
checking for popt.h... no
checking popt.h usability... no
checking popt.h presence... no
checking for popt.h... no
configure: error: 
* Cannot autodetect popt.h
*
* Set POPT_CFLAGS and POPT_LIBS correctly.
```
> > > download and install popt from http://www.linuxfromscratch.org/blfs/view/svn/general/popt.html
> > > ./configure --prefix=/usr --disable-static >log\_configure.txt
> > > make >log\_make.txt
> > > make install >log\_makeinstall.txt
  1. errors at make and make install
  1. trying popt-1.14 pre-compiled for Quark from Nicolas
  1. run `./configure`, and `make install` (no need to run `make`)
  1. some warnings due to date set incorrect
  1. set the date using `date -s "15 APR 2014 18:46:00"`
  1. re-run `make install`, no more warnings!
  1. ### waiting... ###
  1. rerun `./configure` for gphoto2
  1. still problem autodetecting popt
```
root@clanton:/media/mmcblk0p1/gphoto2-2.5.4# ./configure >log_configure2.txt./configure: line 14460: test: : integer expression expected
configure: error: 
* Cannot autodetect library directory containing popt
*
* Set POPT_CFLAGS and POPT_LIBS correctly.
```
  1. run:
```
POPT_CFLAGS=-I/usr/local/include
POPT_LIBS="-L/usr/local/lib -lpopt"
```
  1. run `./configure --prefix=/usr/local`
  1. finally got past popt.h but still error at
```
checking whether popt is required... yes                            
checking popt.h usability... yes                                      
checking popt.h presence... yes                             
checking for popt.h... yes                                                     
checking for poptStuffArgs in -lpopt... no                       
checking for poptStuffArgs in -lpopt... no                                  
checking for poptStuffArgs in -lpopt... no                           
checking for poptStuffArgs in -lpopt... no                   
checking for poptStuffArgs in -lpopt... no               
checking for poptStuffArgs in -lpopt... no
configure: error: 
* Cannot autodetect library directory containing popt
*
* Set POPT_CFLAGS and POPT_LIBS correctly.
```
  1. did some more searching and now I try passing the flags into the configure by running `./configure POPT_CFLAGS=-I/usr/local/include POPT_LIBS="-L/usr/local/lib -lpopt"`
```
root@clanton:/media/mmcblk0p1/gphoto2-2.5.4# ./configure POPT_CFLAGS=-I/usr/local/include POPT_LIBS="-L/usr/local/lib -lpopt" >log_configure5.txt
./configure: line 14460: test: : integer expression expected
config.status: WARNING:  'po/Makefile.in.in' seems to ignore the --datarootdir setting
```
  1. oh yeah! configure succeeded! now let's `make'!
  1. but still an error:
```
root@clanton:/media/mmcblk0p1/gphoto2-2.5.4# make >log_make.txt
In file included from actions.c:39:0:
actions.h:24:36: fatal error: gphoto2/gphoto2-camera.h: No such file or directory
```
  1. upon checking, `gphoto2/gphoto2-camera.h` is actually inside libgphoto2, not gphoto. how do i point the compile to grab gphoto2-camera.h from the libphoto directory while I am in the gphoto directory performing the `make`?
```
root@clanton:/media/mmcblk0p1/libgphoto2-2.5.4/gphoto2# ls
gphoto2-abilities-list.h  gphoto2-filesys.h  gphoto2-setting.h
gphoto2-camera.h	  gphoto2-library.h  gphoto2-version.h
gphoto2-context.h	  gphoto2-list.h     gphoto2-widget.h
gphoto2-file.h		  gphoto2-result.h   gphoto2.h

root@clanton:/media/mmcblk0p1# ls
PaxHeaders.1163  core-image-minimal-initramfs-clanton.cpio.gz  libtool-2.4.2
README.txt	 gphoto2-2.5.4				       melvin
boot		 image-full-clanton.ext3		       popt-1.14
bzImage		 libgphoto2-2.5.4			       popt-1.16-fail
```
  1. ### I STOPPED HERE, ARRRGHHH!!! ###
  1. run `make` & `make install`
  1. test gphoto2 by running `gphoto2 -v`
  1. run `gphoto2 --auto-detect`
### Using a different Linux image ###
  1. Using Yocto Project Linux image w/ Clanton-full kernel + general SDKs + OpenJDK-6 + Tomcat 7 from http://ccc.ntu.edu.tw/index.php/news/40
  1. Boot-up the Galileo board and connect via ssh
  1. Set the date `date -s "17 APR 2014 14:00:00"`
  1. Download libgphoto2 from http://sourceforge.net/projects/gphoto/files/libgphoto/2.5.4/libgphoto2-2.5.4.tar.bz2/download
  1. Extract to `home/root/` by `bzip2 -cd libgphoto2-2.5.4.tar.bz2 | tar xvf -`
  1. Go to the directory `cd /libgphoto2-2.5.4`
  1. Set execute attribute by `chmod +x configure`
  1. Run `./configure`
  1. Run `make`
  1. Run `make install`
  1. Download gphoto2 from http://sourceforge.net/projects/gphoto/files/gphoto/2.5.4/gphoto2-2.5.4.tar.bz2/download
  1. Extract to `home/root/` by `bzip2 -cd gphoto2-2.5.4.tar.bz2 | tar xvf -`
  1. Copy over some files `cp ~/libgphoto2-2.5.4/gphoto2/* ~/gphoto2-2.5.4/gphoto2/`
  1. Set execute attribute by `chmod +x configure`
  1. Run `./configure`
  1. Run `make`
  1. Run `make install`
  1. No errors!!!!
  1. Verify gPhoto2 is installed and working by plugging in the camera to the host USB port
```
root@clanton:~/gphoto2-2.5.4# gphoto2 --version
gphoto2 2.5.4

Copyright (c) 2000-2014 Lutz Mueller and others

gphoto2 comes with NO WARRANTY, to the extent permitted by law. You may
redistribute copies of gphoto2 under the terms of the GNU General Public
License. For more information about these matters, see the files named COPYING.

This version of gphoto2 is using the following software versions and options:
gphoto2         2.5.4          gcc, popt(m), no exif, no cdk, no aa, jpeg, readline
libgphoto2      2.5.4          all camlibs, gcc, ltdl, no EXIF
libgphoto2_port 0.10.0         gcc, ltdl, USB, serial without locking
root@clanton:~/gphoto2-2.5.4# gphoto2 --auto-detect
Model                          Port
----------------------------------------------------------
Nikon Coolpix P300 (PTP mode)  usb:002,002
```
  1. ## DONE! ##