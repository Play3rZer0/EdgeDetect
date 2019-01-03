from PIL import Image, ImageFilter, ImageChops

img = Image.open("a1.jpg")
img2 = Image.open("a3.jpg")

img = img.filter(ImageFilter.FIND_EDGES)
img2 = img2.filter(ImageFilter.FIND_EDGES)

img3 = ImageChops.add(img,img2,1,4)

img3.show()
img3.save("a4edged.jpg")
