# Introduction #

Find the lib can decode datamatrix

successfully install in ubuntu
successfully install in galileo

# Details #

http://boy.co.ua/decode.php?lang=EN.

http://www.libdmtx.org/

http://libdmtx.wikidot.com/libdmtx-python-wrapper

1. install libdmtx

2. install dmtx-wrapper

3. use python --> fail on galileo

```
pip install PIL
```




---
install on Galileo.

1. install libdmtx

2. install dmtx-wrapprer for python

3. install PIL for python by this source code

http://effbot.org/downloads/Imaging-1.1.7.tar.gz

4. **Sucessfully!!!!**

```
root@clanton:~/dmtx-wrappers/python# python test_HH2.py 
Reading file...
2R337246A00960
1
2R337246A00960
('2R337246A00960', ((44, 112), (368, 112), (380, 24), (44, 24)))

```

5. Do several experiment:

picture full board: 300kb --> fail, waiting for more than 5 minutes does not return result.

picture full Intel Quack --> fail, waiting for more than 5 minutes does not return result.

picture with only data matrix code 16kb --> return result in around 7s.


---
Add your content here.  Format your content with:
  * Text in **bold** or _italic_
  * Headings, paragraphs, and lists
  * Automatic links to other wiki pages