from PIL import Image
import sys

if len(sys.argv) != 3:
    print("Missing Arguments")
    sys.exit(0)


im = Image.open(sys.argv[1])
pix = im.load()

(width, lenght) = im.size

for y in range(lenght):
    for x in range(width):
        pixelColor = pix[x,y]

         #Red
        if pixelColor[0] > 127:
            red = 255
        else:
            red = 0

        #Green
        if pixelColor[1] > 127:
            green = 255
        else:
            green = 0

        #Blue
        if pixelColor[2] > 127:
            blue = 255
        else:
            blue = 0
        '''
        red = pixelColor[0]
        green = pixelColor[1]
        blue = pixelColor[2]
        finalColor = int((blue + red + green)/3)
        '''
        pix[x,y] = (red, green, blue)
im.save(sys.argv[2])
