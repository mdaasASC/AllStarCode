def setup():
    size(500, 500)
def draw():
    stroke(255, 255, 255)
    fill(255, 255, 255)
    rect(0, 0, 20, 20)
    stroke(0, 0, 0)
    fill(0, 0, 0)
    rect(50, 0, 50, 50)
    stroke(255, 0, 0)
    fill(255, 0, 0)
    rect(100, 0, 50, 50)
    stroke(0, 255, 0)
    fill(0, 255, 0)
    rect(150, 0, 50, 50)
    stroke(0, 0, 255)
    fill(0, 0, 255)
    rect(200, 0, 50, 50)
    stroke(255, 255, 0)
    fill(255, 255, 0)
    rect(250, 0, 50, 50)
    stroke(255, 0, 255)
    fill(255, 0, 255)
    rect(300, 0, 50, 50)
    stroke(0, 255, 255)
    fill(0, 255, 255)
    rect(350, 0, 50, 50)
    stroke(250, 104, 0)
    fill(250, 104, 0)
    rect(400, 0, 50, 50)
    stroke(130, 90, 44)
    fill(130, 90, 44)
    rect(450, 0, 50, 50)
def mouseClicked():
        if mouseX < 50 and mouseY < 50:
            fill(255, 255, 255)
            stroke(255, 255, 255)
            rect(0, 475, 25, 25)
        elif mouseX > 50 and mouseX < 100 and mouseY < 50:
            fill(0, 0, 0)
            stroke(0, 0, 0)
            rect(0, 475, 25, 25)
        elif mouseX > 100 and mouseX < 150 and mouseY < 50:
            fill(255, 0, 0)
            stroke(255, 0, 0)
            rect(0, 475, 25, 25)
        elif mouseX > 150 and mouseX < 200 and mouseY < 50:
            fill(0, 255, 0)
            stroke(0, 255, 0)
            rect(0, 475, 25, 25)
        elif mouseX > 200 and mouseX < 250 and mouseY < 50:
            fill(0, 0, 255)
            stroke(0, 0, 255)
            rect(0, 475, 25, 25)
        elif mouseX > 250 and mouseX < 300 and mouseY < 50:
            fill(255, 255, 0)
            stroke(255, 255, 0)
            rect(0, 475, 25, 25)
        elif mouseX > 300 and mouseX < 350 and mouseY < 50:
            fill(255, 0, 255)
            stroke(255, 0, 255)
            rect(0, 475, 25, 25)
        elif mouseX > 350 and mouseX < 400 and mouseY < 50:
            fill(0, 255, 255)
            stroke(0, 255, 255)
            rect(0, 475, 25, 25)
        elif mouseX > 400 and mouseX < 450 and mouseY < 50:
            fill(250, 104, 0)
            stroke(250, 104, 0)
            rect(0, 475, 25, 25)
        elif mouseX > 450 and mouseX < 500 and mouseY < 50:
            fill(130, 90, 44)
            stroke(130, 90, 44)
            rect(0, 475, 25, 25)