import turtle
import time

delay = 0.1

wn = turtle.Screen()
wn.title("Snake Game")
wn.bgcolor("#000033")
wn.setup(width=600, height=600)
wn.tracer(0)

head = turtle.Turtle()
head.speed(0)
head.shape("square")
head.color("#ffffff")
head.penup()
head.goto(0,0)
head.direction = "left"

def move():
    if head.direction == "up":
        y = head.ycor()
        head.sety(y+20)
        
    if head.direction == "down":
        y = head.ycor()
        head.sety(y-20)
        
    if head.direction == "left":
        x = head.xcor()
        head.setx(x-20)
    

while True:
    wn.update()
    
    move()
    
    time.sleep(delay)


wn.mainloop()
