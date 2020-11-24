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

wn = trtl.Screen()
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
  active_apple.showturtle()
  active_apple.color("pink")
  active_apple.write("a", font=("Arial", 74, "bold"))
  wn.tracer(True)
  wn.update()    

def drop_apple(active_apple):
  active_apple.penup()
  active_apple.goto(active_apple.xcor(),ground_height)
  x = active_apple.xcor()
  y = active_apple.ycor()
  apple.hideturtle()
  draw_apple(apple)

def drop_apple_key():
    drop_apple(apple)

#TODO Create a function that takes a turtle (apple) and its corresponding letter from the letter
# list and draws that letter on that turtle (apple)
def draw_an_a():
  apple.write("a", font=("Arial", 74, "bold")) 
  apple.showturtle()


letters = ["a","s","d","f","g","h","j","k","l"]
turtles = []
number_of_apples = 10
x = 0
y = int(len(letters))
print(y)
y = y - 1
draw_apple(apple)
wn.onkeypress(drop_apple(apple),"a")


#TODO Create a function that takes a turtle as its parameter and gives that turtle (apple)
# a new location on the tree, only if the list of letters is not empty. Associate the 
# turtle with a new letter selected at random from the list of letters

wn.listen()
#-----function calls-----

wn.mainloop()