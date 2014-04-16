from pydmtx import DataMatrix
from PIL import Image

print "Reading file..."
# Read a Data Matrix barcode
dm_read = DataMatrix()
img = Image.open("clantont2.jpg")

print dm_read.decode(img.size[0], img.size[1], buffer(img.tostring()))
print dm_read.count()
print dm_read.message(1)
print dm_read.stats(1)
