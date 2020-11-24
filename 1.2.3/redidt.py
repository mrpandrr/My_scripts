#   a123_apple_1.py
import turtle as trtl
import random 
import time
#-----setup-----
apple_image = "apple.gif" # Store the file name of your shape
pear_image = "pear.gif"
wn = trtl.Screen()
wn.setup(width=1.0, height=1.0)
wn.bgpic("background.gif")
wn.addshape(apple_image)
wn.addshape(pear_image) # Make the screen aware of the new file
apple = trtl.Turtle()
apple.hideturtle()
pear = trtl.Turtle()
drawer = trtl.Turtle()
drawer.hideturtle()
apple.hideturtle()
#-----functions-----
def draw_an_A():
  drawer.penup()
  drawer.goto(18,40)
  drawer.pendown()
  drawer.color("white")
  drawer.write("A", font=("Arial", 55, "bold")) 
def apple_fall(active_apple):
  apple.penup()
  xcor = random.randint(-100,100)
  ycor = 180
  apple.goto(xcor,ycor)
  time.sleep(.1)
while ycor > -165:
    apple.showturtle()
    apple.goto(xcor,ycor)
    ycor -=4
# This call to the onkeypress function sets draw_an_A as the function
draw_an_A()
# that will be called when the "a" key is pressed.
# given a turtle, set that turtle to be shaped by the image file
def draw_apple(active_apple):
  active_apple.shape(apple_image)
  wn.update()

def draw_pear(active_pear):
  active_pear.shape(pear_image)
  wn.update()

#-----function calls-----
draw_apple(apple)
wn.onkeypress(apple_fall, "a")
wn.listen
wn.mainloop()