#Import from the PIL library
from PIL import Image, ImageFilter, ImageChops

#Open the files you want to compare
#filename1 is the first file (original) defined in img
#filename2 is the file you want to compare with defined in img2
img = Image.open("<filename1>")
img2 = Image.open("<filename2>")

#Apply a filter called FIND_EDGES for edge detection in the image
img = img.filter(ImageFilter.FIND_EDGES)
img2 = img2.filter(ImageFilter.FIND_EDGES)

#Do pixel by pixel comparison with ImageChops for img and img2
img3 = ImageChops.add(img,img2,1,4)

#Show bitmap of the img3 to verify the operation
img3.show()

#Save to a file called filename3 (give it a name)
img3.save("<filename3>")
