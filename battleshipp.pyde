from random import *

r1X = 0
r1Y = 0
r2X = 100
r2Y = 100
r3X = 200
r3Y = 200
r4X = 300
r4Y = 300
r5X = 400
r5Y = 400
p = 0
r = 255
g = 255
b = 255
c1 = 0
c2 = 0

def setup():
    global pic
    size(500, 500)
    pic = loadImage("ship.png")
    
def draw():
    global r1X, r1Y, r2X, r2Y, r3X, r3Y, r4X, r4Y, pic, p, sX, sY, c1, c2, r, g, b
    fill(255, 255, 255)
    rect(r1X, r1Y, 100, 100)
    rect(r2X, r1Y, 100, 100)
    rect(r3X, r1Y, 100, 100)
    rect(r4X, r1Y, 100, 100)
    rect(r5X, r1Y, 100, 100)
    rect(r1X, r2Y, 100, 100)
    rect(r2X, r2Y, 100, 100)
    rect(r3X, r2Y, 100, 100)
    rect(r4X, r2Y, 100, 100)
    rect(r5X, r2Y, 100, 100)
    rect(r1X, r3Y, 100, 100)
    rect(r2X, r3Y, 100, 100)
    rect(r3X, r3Y, 100, 100)
    rect(r4X, r3Y, 100, 100)
    rect(r5X, r3Y, 100, 100)
    rect(r1X, r4Y, 100, 100)
    rect(r2X, r4Y, 100, 100)
    rect(r3X, r4Y, 100, 100)
    rect(r4X, r4Y, 100, 100)
    rect(r5X, r4Y, 100, 100)
    rect(r1X, r5Y, 100, 100)
    rect(r2X, r5Y, 100, 100)
    rect(r3X, r5Y, 100, 100)
    rect(r4X, r5Y, 100, 100)
    rect(r5X, r5Y, 100, 100)
    while p < 1:
        xList = [0, 100, 200, 300, 400]
        yList = [0, 100, 200, 300, 400]
        sX = choice(xList)
        sY = choice(yList)
        image(pic, sX, sY, 100, 100)
        p = p + 1
    fill(r, g, b)
    rect(sX, sY, c1, c2)
def mouseClicked():
    global sX, sY, c1, c2, r, g, b
    if mouseX > sX and mouseX < sX + 100 and mouseY > sY and mouseY < sY + 100:
        g = 0
        b = 0
        c1 = 100
        c2 = 100
    elif mouseX > 0 and mouseX < 100:
        if mouseY > 