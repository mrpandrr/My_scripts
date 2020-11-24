import random as rand
import turtle as trtl
#TODO Create a function that takes a turtle as its parameter and gives that turtle (apple)
apple_image = "apple.gif"

wn = trtl.Screen()
wn.setup(width=0.5, height=0.5)
wn.addshape(apple_image)
wn.bgpic("background.gif")
apple = trtl.Turtle()
tron = trtl.Turtle()
tron.color("green")
tron.pensize(5)
tron.penup()
tron.goto(20,20)
tron.pendown()
apple.pensize(5)
x = 15
def userclickW():
    apple.setheading(90)
    apple.forward(x)
def userclickA():
    apple.setheading(180)
    apple.forward(x)
def userclickS():
    apple.setheading(270)
    apple.forward(x)
def userclickD():
    apple.setheading(360)
    apple.forward(x)
def tronclickW():
    tron.setheading(90)
    tron.forward(x)
def tronclickA():
    tron.setheading(180)
    tron.forward(x)
def tronclickS():
    tron.setheading(270)
    tron.forward(x)
def tronclickD():
    tron.setheading(360)
    tron.forward(x)
def yellowcolorY():
    tron.color("yellow")
def greencolorG():
    tron.color("green")

wn.onkeypress(userclickW,'w')
wn.onkeypress(userclickA,'a')
wn.onkeypress(userclickS,'s')
wn.onkeypress(userclickD,'d')

wn.onkeypress(tronclickW,'t')
wn.onkeypress(tronclickA,'f')
wn.onkeypress(tronclickS,'g')
wn.onkeypress(tronclickD,'h')
wn.onkeypress(yellowcolorY,'y')
wn.onkeypress(greencolorG,'u')



wn.listen()

wn.mainloop()
