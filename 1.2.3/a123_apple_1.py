#   a123_apple_1.py
import turtle as trtl
import random as rand
from random import randint
#import os

#dir = os.path.dirname(os.path.abspath(__file__))
#apple_image = os.path.join(dir, "apple.gif")

#-----setup-----
apple_image = "apple.gif" # Store the file name of your shape
ground_height = -162

wn = trtl.Screen()``
wn.setup(width=0.5, height=0.5)
wn.addshape(apple_image) # Make the screen aware of the new file
wn.bgpic("background.gif")

apple = trtl.Turtle()

#-----functions-----
# given a turtle, set that turtle to be shaped by the image file
def draw_apple(active_apple):
  
  active_apple.penup()
  active_apple.shape(apple_image)
  wn.tracer(False)
  active_apple.sety(0)
  active_apple.sety(active_apple.ycor()-30)
  active_apple.color("white")
  active_apple.write("a", font=("Arial", 74, "bold"))
  active_apple.sety(active_apple.ycor()+30)
  wn.tracer(True)
  wn.update()      

def drop_apple(active_apple):
  active_apple.penup()
  active_apple.clear()
  active_apple.sety(-150)
  active_apple.hideturtle()
  active_apple.hideturtle()
  draw_apple(apple)

def drop_apple_key():
  drop_apple(apple)
#----Function Call
draw_apple(apple)



wn.onkeypress(drop_apple(apple), "a")

wn.listen()

wn.mainloop()