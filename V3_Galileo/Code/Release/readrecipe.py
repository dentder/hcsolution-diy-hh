###################################################################################
# code to read recipe from file
#  Nguyen Hoang Hai
# Input: Recipe File, Image
# Output: result file
# Process: decode all pre-define boxes of image, and put on Result file
# Version: 1.0 Date: 10:03PM 18-04-2014
###################################################################################
from PIL import Image
from pydmtx import DataMatrix
import os
import mmap

#import PIL.ImageOps # use for invertcolor

strfi="VLV_27_27_recipe.txt"
strfo="result.csv"
strfojade="views/result2.jade"
strfImage = "IMG_4581.JPG"
strVIDs = "public/uploads/VID.txt"
fRecipe = open(strfi, 'r') # open Recipe file for read
fResult = open(strfo, 'w') # open Result file for write
fResultjade = open(strfojade, 'w') # open Result file for write Jade
imgMaster = Image.open(strfImage) #open Image

fVIDs = open(strVIDs,'r')
sVID = mmap.mmap(fVIDs.fileno(), 0, access=mmap.ACCESS_READ)
print sVID
# Function definition is here
def space(number):
   # Add both the parameters and return them."
   strSpace ="";
   for x in range(1, number):
       strSpace +=" "

   return strSpace;

print "processing... \n"
#decode the first line
line = fRecipe.readline() 
values = line.split() # split value of first lines

(iTotalUnit,iRow,iCol,wRef,hRef) = (int(values[0]), int(values[1]),int(values[2]), int(values[3]),int(values[4])) # parse first line value to varables

print iTotalUnit,iRow,iCol,wRef,hRef

# write the first line of Result
fResultjade.write("extends default\nblock content\n"+space(2)+"div(align='center')\n")
fResultjade.write(space(3)+"table.intel-table\n"+space(4)+"thead\n"+space(5)+"tr\n" )
# create result table
for x in range(1, iCol):
    fResult.write("Col" + str(x) + ",")
    fResultjade.write(space(6)+"th" +" Col" + str(x) + "\n")
fResult.write("Col" + str(iCol) + "\n")
fResultjade.write(space(6)+"th" +" Col" + str(iCol) + "\n")
# end of write first line of Result

fResultjade.write(space(4)+"tbody\n"+space(5)+"tr\n")
# read position
line = fRecipe.readline()
iCount = 1
iCount2 = 1
while iCount2<(iTotalUnit+1):
    

    values = line.split()
    # get unit position
    (wposition,hposition) = (int(values[0]), int(values[1]))
   
    # begin detect 
    box = (wposition, hposition, wposition+wRef, hposition+hRef)
    print box
    imgRegion = imgMaster.crop(box)
    #inverted_image = PIL.ImageOps.invert(image)
    #imgRegion = PIL.ImageOps.invert(imgRegion) #invert color
    dm_read = DataMatrix(max_count = 1, timeout = 400) 
        # simply setting timeout to a certain number of milliseconds, we restrict the total detection time per image.
    strResult = dm_read.decode(imgRegion.size[0], imgRegion.size[1], buffer(imgRegion.tostring()))
    #imgRegion.save("Cropped" + str(iCount2) + ".jpg") #save file
    #box.kill()
    #dm_read.kill()    
    #imgRegion.kill()
    # end of detect
    # save file result
    if dm_read.count() == 0:
         strResult="None"
 
    fResult.write(strResult)
    print strResult + " : "+str(sVID.find(strResult)) + "\n"
    if sVID.find(strResult)!=-1:
         fResultjade.write(space(6)+"td(style=\"background-color:yellow;\") "+strResult+"\n")
         print " Found: " + strResult + "\n"
    else:
         fResultjade.write(space(6)+"td "+strResult+"\n") 
    #strResult.kill()
    if iCount>(iCol-1):
          iCount = 0
          fResult.write("\n")
          fResultjade.write(space(4)+"tr\n")
    else:
          fResult.write(",")
    # -----------------
    # READ NEXT LINE 
    line = fRecipe.readline()
    iCount +=1
    iCount2 +=1    

#os.remove(strfImage) # Delete file
fRecipe.close() #close recipe file
fResult.close() #close Result file
fResultjade.close() #close Result JAde for web file
fVIDs.close() # close the VID list file
sVID.close() # close memory of file
print "processing...Done"
