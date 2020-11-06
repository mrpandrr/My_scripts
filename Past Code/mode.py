#   a113_tower.py
#   Modify this code in VS Code to alternate the colors of the 
#   floors every three floors
import turtle as trtl

painter = trtl.Turtle()
painter.speed(0)
painter.pensize(5)

# starting location of the tower
x = -150
y = -150

# height of tower and a counter for each floor
num_floors = 63
floor = 0
extra = 0
# iterate
while floor < num_floors:
  # set placement and color of turtle
  rem = floor %21
  if(rem == 0):
    x = x + 100
    y = 0
  
  painter.penup()
  painter.goto(x, y)
  painter.color("gray")
  y = y + 5 # location of next floor
  floor = floor + 1
  
  extra = extra + 1

  if(extra <= 2):
    painter.color("black")
  if(extra> 2):
    painter.color("orange")
  if(extra > 4):
    painter.color("blue")

  

  #draw the floor
  painter.pendown()
  painter.forward(50)
  if (extra ==6):
    extra = 0

wn = trtl.Screen()
wn.mainloop()