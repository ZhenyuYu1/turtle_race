import turtle
import random
import time

t1 = turtle.Turtle()
t2 = turtle.Turtle()
drawer = turtle.Turtle()
noFinish = True

color_list = ["red", "green", "blue", "yellow", "cyan", "magenta"]
speed = random.randint(0, 20)
t1.shape("turtle")
t2.shape("turtle")
t1.color(random.choice(color_list))
t2.color(random.choice(color_list))
t1y = random.randint(-330, 330)
t2y = random.randint(-330, 330)
distance = random.randint(0, 25)

#creates starting and finishing line
drawer.speed(4000)
drawer.penup()
drawer.goto(-300, 340)
drawer.pendown()
drawer.right(90)
drawer.forward(800)
drawer.penup()
drawer.goto(300, 340)
drawer.pendown()
drawer.forward(800)
style = ("Courier", 30, "italic")
turtle.hideturtle()
turtle.write("On your marks, get set...", font = style, align = "center")
time.sleep(2)
turtle.clear()
turtle.write("Get set...", font = style, align = "center")
time.sleep(2)
turtle.clear()

#put the 2 racing turtles into position at the starting line
t1.penup()
t1.setposition(-310, t1y)

t2.penup()
t2.setposition(-310, t2y)

turtle.write("GO!", font = style, align = "center")
time.sleep(2)
turtle.clear()

while noFinish:
    if ((t1.xcor() < 300) or (t2.xcor() < 300)):
        distance = random.randint(0, 25)
        t1.forward(distance)
        t2.forward(distance)
    else:
        noFinish = False

turtle.mainloop()
