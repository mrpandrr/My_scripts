import turtle as trt1

my_turtles = []

turtle_shapes = ['arrow', 'turtle', 'circle', 'square', 'triangle', 'classic']
turtle_colors = ['red', 'blue', 'green', 'orange', 'purple', 'gold']

for s in turtle_shapes:
    t = trt1.Turtle(shape=s)
    # setting last color in turtle_colors as turtle's color and then removing
    # that color from turtle_colors
    t.color(turtle_colors.pop())
    t.penup()  # pen up
    my_turtles.append(t)

startx = 0
starty = 0
heading = 90  # starting direction

for t in my_turtles:
    t.goto(startx, starty)
    t.setheading(heading)  # using heading as direction
    t.pendown()  # pen down
    t.right(45)
    t.forward(50)
    startx = t.xcor()  # recording x coordinate for next turtle
    starty = t.ycor()  # recording y coordinate for next turtle
    heading = t.heading()  # recording current direction

wn = trt1.Screen()
wn.mainloop()