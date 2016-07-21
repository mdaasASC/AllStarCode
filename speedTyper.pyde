from random import *
from time import *
myList = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]

x = 0
y = randint(10, 500)
i = choice(myList)
c = 0

def setup():
    size(500,500)

def draw():
    sleep(0.1)
    global i, x, y, c
    textSize(32)
    r = randint(1,255)
    g = randint(0,255)
    b = randint(0,255)
    background(0)
    fill(r, g, b)
    text(i, x, y)
    x = x + 3
    if x > 450:
        c = c + 1
        x = 0
        y = randint(10, 500)
        i = choice(myList)
    if c == 4:
        background(0)
        text("You lose", 180, 250)
        if keyPressed:
            if key == "1":
                c = 0
                background(0)
                x = 0
                y = randint(10, 500)
                i = choice(myList)
    if keyPressed:
        if key == i:
            background(0)
            x = 0
            y = randint(10, 500)
            i = choice(myList)
        elif c < 4:
            c = c + 1