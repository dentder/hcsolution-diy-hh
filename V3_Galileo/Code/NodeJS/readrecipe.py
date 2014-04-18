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

strfi="VLV_27_27_recipe.txt"
strfo="result.csv"
strfImage = "PN4Mb.jpg"
fRecipe = open(strfi, 'r') # open Recipe file for read
fResult = open(strfo, 'w') # open Result file for write
imgMaster = Image.open(strfImage) #open Image

print "processing... \n"
#decode the first line
line = fRecipe.readline() 
values = line.split() # split value of first lines

(iTotalUnit,iRow,iCol,wRef,hRef) = (int(values[0]), int(values[1]),int(values[2]), int(values[3]),int(values[4])) # parse first line value to varables

print iTotalUnit,iRow,iCol,wRef,hRef

# write the first line of Result
for x in range(1, iCol):
    fResult.write("Col" + str(x) + ",")
fResult.write("Col" + str(iCol) + "\n")
# end of write first line of Result


# read position
line = fRecipe.readline()
iCount = 1
iCount2 = 1
while line:
    

    values = line.split()
    # get unit position
    (wposition,hposition) = (int(values[0]), int(values[1]))
   
    # begin detect 
    box = (wposition, hposition, wposition+wRef, hposition+hRef)
    print box
    imgRegion = imgMaster.crop(box)
    dm_read = DataMatrix()
    strResult = dm_read.decode(imgRegion.size[0], imgRegion.size[1], buffer(imgRegion.tostring()))
    #imgRegion.save("Cropped" + str(iCount2) + ".jpg") 
    #box.kill()
    #dm_read.kill()    
    #imgRegion.kill()
    # end of detect
    # save file result
    if dm_read.count() == 0:
         strResult="None"
 
    fResult.write(strResult)
    #strResult.kill()
    if iCount>(iCol-1):
          iCount = 0
          fResult.write("\n")
    else:
          fResult.write(",")
    # -----------------
    # READ NEXT LINE 
    line = fRecipe.readline()
    iCount +=1
    iCount2 +=1    

fRecipe.close() #close recipe file
fResult.close() #close Result file

print "processing...Done"
