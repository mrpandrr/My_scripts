#   a123_apple_letters.py
import turtle as trtl
import random as rand
from random import randint

apple_image = "apple.gif" # Store the file name of your shape
ground_height = -162

wn = trtl.Screen()
wn.setup(width=0.5, height=0.5)
wn.addshape(apple_image) # Make the screen aware of the new file
wn.bgpic("background.gif")


#TODO Create a function that takes a turtle as its parameter and gives that turtle (apple)
apple = trtl.Turtle()
letters = ["a","s","d","f","g","h","j","k","l"]
turtles = []
y = 0
y = int(len(letters))
y = y - 1
print(y)
def param(apple):
    y = int(len(letters))
    y = y - 1
    apple.goto(apple.xcor()+20,apple.ycor())
    z = letters.pop(randint(0,y))
    letterturtle = apple.shape("z")
    turtles.append(letterturtle)
    print(letterturtle)
    wn.listen()
    y = y - 1
    y = 

# a new location on the tree, only if the list of letters is not empty. Associate the 
# turtle with a new letter selected at random from the list of letters

#TODO Create a function that takes a turtle (apple) and its corresponding letter from the letter
# list and draws that letter on that turtle (apple)
def drawing(apple):
    turtle = turtles.pop()
    turtle.stamp()

param(apple)
drawing(apple)

#TODO Create a function that takes a turtle (apple) and its corresponding ltter from the letter
# list and set that turtle to be shaped by the image file, call the letter drawing function,
# and update the Screen
def draw_apple(active_apple):
  active_apple.shape(apple_image)
  wn.update()

def drop_apple(active_apple):
  active_apple.penup()
  active_apple.goto(active_apple.xcor(),ground_height)
  x = active_apple.xcor()
  y = active_apple.ycor()
  active_apple.goto(x,ground_height)
  wn.listen()
draw_apple(apple)
drop_apple(apple)
#TODO Iterate over the numbers from 0 to the number of apples, creating that many turtles
# calling your function that resets the apples by giving them a new random location
# add the new apples to a list of apples to be used in the rest of the program.
# The loop below executes the correct number of times by using the range() function
# to create a list of numbers to iterate over.
  #Your code here

#TODO Create a function that takes a letter as its parameter, uses that letter to retrieve the
# corresponding turtle (apple) and causes both to drop from the tree simultaneously. Once the 
# apple and letter have dropped, call the apple reseting function.

#TODO define a function per letter that you will use in your program. Each function should check
# to see if the given letter is in the list of letters; if it is, it should drop the corresponding
# apple.

#TODO use the onkeypress method of wn to correlate the functions you defined above with each
# of the letters that the user might type.
# onkeypress requires that you name one function that must take
# no arguments to be called when the specified key is pressed.
trtl.mainloop()