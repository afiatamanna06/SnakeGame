import turtle

wn = turtle.Screen()
wn.title("Snake Game")
wn.bgcolor("#000033")
wn.setup(width=600, height=600)
wn.tracer(0)

head = turtle.Turtle()
head.speed(0)
head.shape("square")
head.color("black")


wn.mainloop()
