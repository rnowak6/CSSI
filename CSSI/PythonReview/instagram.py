from PIL import Image

cats=Image.open("cat.jpg")
print cats.getdata()[200]

def getRed(pixel):
    return pixel[0]

def getGreen(pixel):
    return pixel[1]

def getBlue(pixel):
    return pixel[2]

def getAveragePixel(pixel):
    numb=(getRed(pixel) + getGreen(pixel) + getBlue(pixel))/3
    return (numb, numb, numb)

new_pixels = []
size=cats.height * cats.width
old_pixels=cats.getdata()
for i in range(size):
    old_pixel=old_pixels[i]
    if(i>size/3)*2:
        new_pixel=(getGreen(old_pixel), getBlue(old_pixel), getRed(old_pixel))
    elif(i>size/3):
        new_pixel=getAveragePixel(old_pixel)
    else:
        new_pixel=old_pixel
    new_pixels.append(new_pixel)

#for pixel in cats.getdata():
    #new_pixels.append(pixel)
    #red_value=getRed(pixel)
    #green_value=getGreen(pixel)
    #blue_value=getBlue(pixel)
    #new_pixel=getAveragePixel(pixel)
    #new_pixels.append(new_pixel)

print new_pixels[200]

new_image = Image.new("RGB", (cats.width, cats.height*2))
new_image.putdata(new_pixels)
offset=(0, cats.height)
new_image.paste(cats, offset)
new_image.show()
