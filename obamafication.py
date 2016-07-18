from Myro import *

pic = makePicture(pickAFile())

ObamaDarkBlue = makeColor(0,51,76)

ObamaRed = makeColor(217, 26, 33)

ObamaBlue = makeColor(112,150,158)

ObamaYellow = makeColor(252, 227, 166)

for pixel in getPixels(pic):
    if getGray(pixel) > 180:
        setColor(pixel, ObamaYellow)
    elif getGray(pixel) > 120:
        setColor(pixel, ObamaBlue)
    elif getGray(pixel) > 60:
        setColor(pixel, ObamaRed)
    elif getGray(pixel) < 60:
        setColor(pixel, ObamaDarkBlue)

show(pic)