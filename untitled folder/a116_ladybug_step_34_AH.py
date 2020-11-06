#   a116_ladybug.py
import turtle as trtl
ladybug = trtl.Turtle()



#OLD Legs Algorithm shifted by 60degrees
ladybug.pensize(10)
count = 0
legs = 8
angle = 120/legs
length = 70
while (count < legs):
  ladybug.goto(0,-40)
  ladybug.setheading((angle*count)-60)
  ladybug.forward(length)
  count = count + 1
  print("angle*count=", angle*count)
count=0
while (count < legs):
  ladybug.goto(0,-40)
  ladybug.setheading((angle*count)+120)
  ladybug.forward(length)
  count = count + 1
  print("angle*count=", angle*count)



# create ladybug head
ladybug = trtl.Turtle()
ladybug.pensize(40)
ladybug.circle(5)

# and body
ladybug.penup()
ladybug.goto(0, -55) 
ladybug.color("red")
ladybug.pendown()
ladybug.pensize(40)
ladybug.circle(20)
ladybug.setheading(270)
ladybug.color("black")
ladybug.penup()
ladybug.goto(0, 5)
ladybug.pensize(2)
ladybug.pendown()
ladybug.forward(75)

# config dots
num_dots = 1
xpos = -20
ypos = -55
ladybug.pensize(10)

# draw two sets of dots
while (num_dots <= 2 ):
  ladybug.penup()
  ladybug.goto(xpos, ypos)
  ladybug.pendown()
  ladybug.circle(3)
  ladybug.penup()
  ladybug.goto(xpos + 30, ypos + 20)
  ladybug.pendown()
  ladybug.circle(2)

  # position next dots
  xpos = xpos + 15          #X- Now goes up by 15 each time
  ypos = ypos + 9           #Y- Ypos now goes up by 5
  num_dots = num_dots + 1

ladybug.hideturtle()

wn = trtl.Screen()
wn.mainloop()