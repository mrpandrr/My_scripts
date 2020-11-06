# import turtle module
import turtle as trtl

# create turtle object
painter = trtl.Turtle()

# set the pen and fill colors
painter.pencolor("red")
painter.fillcolor("blue")
painter.begin_fill()
# then draw a circle
painter.circle(50)
painter.end_fill()


# move the turtle to another part of the screen
painter.penup()
painter.goto(0,-100)
painter.pendown()
# change both the pen and fill colors
painter.pencolor("blue")
painter.fillcolor("brown")
# then draw a polygon of your choice
painter.begin_fill()
painter.circle(45,360,9)
painter.end_fill()
# create screen object and make it persist
wn = trtl.Screen()
wn.mainloop()