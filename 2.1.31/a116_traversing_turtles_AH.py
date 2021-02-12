#   a117_traversing_turtles.py
#   Add code to make turtles move in a circle and change colors.
import turtle as trtl

# create an empty list of turtles
my_turtles = []

# use interesting shapes and colors
turtle_shapes = ["arrow", "turtle", "circle", "square", "triangle", "classic","arrow","circle"]
turtle_colors = ["red", "blue", "green", "orange", "purple","gold","pink","orange"]

for s in turtle_shapes:
  t = trtl.Turtle(shape=s)
  # setting last color in turtle_colors as turtle's color and then removing
  # that color from turtle_colors
  t.color(turtle_colors.pop())
  t.penup()
  my_turtles.append(t)

#Start at 0,0
#Variables equal = startx starty 
startx = 0
starty = 0
heading = 90 #starting direction

# Loop go to 0,0 and right 45 forwrard 50 and then add 50 to x and y
for t in my_turtles:
  t.pensize(10)
  t.turtlesize(3)
  t.goto(startx, starty)
  t.setheading(heading)
  t.pendown()
  t.right(45)     
  t.forward(125)
# Adds spacing for variables
  startx = t.xcor()
  starty = t.ycor()
  heading = t.heading()
wn = trtl.Screen()
wn.mainloop()