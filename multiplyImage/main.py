# !/usr/bin/env python3
import sys

if len(sys.argv) != 3:
    print("Missing Arguments")
    sys.exit(0)

try:
    from PIL import Image
except:
    print ("Pillow has to be installed")
    sys.exit(0)

def resizeImg(pImage, pSize):
   wpercent = (pSize/float(pImage.size[0]))
#   hSize = int((float(pImage.size[1])*float(wpercent)))
   hSize =int(wpercent)
   pImage = pImage.resize((pSize, hSize), Image.ANTIALIAS)
   return pImage

def getAvgColor(pX, pY, lenght, height, pImg):
    currentImg = pImg.load()
    color = 0
    testedPixel = 0

    for x in range(pX, lenght):
        for y in range(pY, height):

            pixelColor = currentImg[x,y]
            color += (pixelColor[0] + pixelColor[1] + pixelColor[2])/3
            testedPixel += 1

    return color/testedPixel


img = Image.open(sys.argv[1])
print(getAvgColor(0,0,img.size[0], img.size[1], img)
