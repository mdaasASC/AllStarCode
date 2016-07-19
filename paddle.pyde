from time import *
from random import *

x = 200
y = 100
vX = 2.5
vY = 2.5
l = 50
w = 60
l1 = 30
l2 = 30
l3 = 30
l4 = 0
w1 = 20
w2 = 20
w3 = 20
w4 = 0



def setup():
    size(400, 400)
    background(0, 0, 0)
    global pic
    global pic2
    global pic3
    global pic4
    global pic5
    pic = requestImage("ye.png")
    pic2 = requestImage("tswiz.png")
    pic3 = requestImage("shoes.png")
    pic4 = requestImage("GO.png")
def draw():
    mX = mouseX
    mX2 = mX + 80
    r = randint(0, 255)
    g = randint(0, 255)
    b = randint(0, 255)
    global x
    global y
    global vX
    global vY
    global pic
    global pic2
    global pic3
    global l
    global w
    global l1
    global l2
    global l3
    global l4
    global w1
    global w2
    global w3
    global w4
    background(b, r, g)
    rect(mX, 360, 80, 20)
    fill(0, 0, 0)
    stroke(r, g, b)
    sleep(0.001)
    image(pic, x, y, 40, 50)
    image(pic2, 50, 70, l, w)
    image(pic3, 70, 360, l1, w1)
    image(pic3, 40, 360, l2, w2)
    image(pic3, 10, 360, l3, w3)
    image(pic4, 120, 150, l4, w4)
    x = x + vX
    y = y + vY
    if x == 380:
        vX = -2.5
    if x == 20:
        vX = 2.5
    if y == 380 and l1 > 0 and w1 > 0:
        l1 = 0
        w1 = 0
        x = 200
        y = 200
    elif y == 380 and l2 > 0 and w2 > 0:
        l2 = 0
        w2 = 0
        x = 200
        y = 200
    elif y == 380 and l3 > 0 and w3 > 0:
        l3 = 0
        w3 = 0
        l = 0
        w = 0
        l4 = 170
        w4 = 120
    if y == 20:
        vY = 2.5
    if y == 340 and x > mX and x < mX2:
        vY = -2.5
    if y < 130 and y > 70 and x < 100 and x > 50:
        l = 0
        w = 0