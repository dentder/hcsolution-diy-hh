# this code module use for crop image from a image
from PIL import Image
print "Reading file..."
# Read a Master Image which get from camera
imgMaster = Image.open("DSCN1091.JPG")
imgRef = Image.open("clantont2.jpg")
(w,h) = imgRef.size
print w,h
# define position of begining
(wposition,hposition) =(2815,1080)

# define function imgCrop
def imgCrop(im):
    
    box = (wposition, hposition, wposition+h, hposition+w)
    print box
    region = im.crop(box)
    region.save("CROPPED.jpg")
# end of function crop

imgCrop(imgMaster)

#print dm_read.decode(img.size[0], img.size[1], buffer(img.tostring()))
#print dm_read.count()
#print dm_read.message(1)
#print dm_read.stats(1)
