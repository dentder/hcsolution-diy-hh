# code to read recipe from file
from PIL import Image

# define function imgCrop
def imgCrop(im):
    
    box = (wposition, hposition, wposition+h, hposition+w)
    #print box
    region = im.crop(box)
    #region.save("CROPPED.jpg")
# end of function crop

strfi="VLV_27_27_recipe.txt"

fRecipe = open(strfi, 'r')

#decode the first line
line = fRecipe.readline()
values = line.split()

(iTotalUnit,iRow,iCol,wRef,hRef) = (values[0], values[1],values[2], values[3],values[4])
print iTotalUnit,iRow,iCol,wRef,hRef

# read position
line = fRecipe.readline()
while line:
    
    values = line.split()
    # get unit position
    (wposition,hposition) = (values[0], values[1])
   
    # begin detect 
    box = (wposition, hposition, wposition+wRef, hposition+hRef)
    #print box
    #region = im.crop(box)
    # end of detect
    # save file
    # READ NEXT LINE 
    line = fRecipe.readline()

fRecipe.close()
