# while loop to change values
# convert to draw()
# move ellipse
# reset ball
# make clouds move

x = 0

def setup():
    size(640, 480)
    
def draw():
    global x
    if x >= 640:
        x = 0
    x += 2
    fill(255)
    background("#87CEEB")
    noStroke()
    ellipse(x + 20, height / 6, 50, 50)
    ellipse(x + 50, height / 6, 50, 50)
    ellipse(x + 80, height / 6, 50, 50)
    
    # ground
    fill(0, 128, 0)
    rect(0, height - 50, width, 50)
    
    y = 0
    if y >= 640:
        y = 0
    y += 60
    fill(64)
    ellipse(y + 50, height / 6, 50, 50)
    ellipse(y + 70, height / 6, 50, 50)
    ellipse(y + 90, height / 6, 50, 50)
    
    fill("#714F06")
    rect(98, 388, 250, 125)
    
    boi = 0
    if boi >= 640:
        boi += 2
        fill(234)
        ellipse(boi + 10, height / 6, 60, 90)
        
    
    
    
