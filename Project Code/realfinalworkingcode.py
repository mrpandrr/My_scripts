import random as rand
import turtle as trtl
#TODO Create a function that takes a turtle as its parameter and gives that turtle (apple)
def userclickW():
        apple.setheading(90)
        apple.forward(x)
        moveapple()
def userclickA():
        apple.setheading(180)
        apple.forward(x)
        moveapple()
def userclickS():
        apple.setheading(270)
        apple.forward(x)
        moveapple()
def userclickD():
        apple.setheading(360)
        apple.forward(x)
        moveapple()
def tronclickW():
        tron.setheading(90)
        tron.forward(x)
        movetron()
def tronclickA():
        tron.setheading(180)
        tron.forward(x)
        movetron()
def tronclickS():
        tron.setheading(270)
        tron.forward(x)
        movetron()
def tronclickD():
        tron.setheading(360)
        tron.forward(x)
        movetron()
def yellowcolorY():
        tron.color("yellow")
def greencolorG():
        tron.color("green")
def distnacex():
        x = tron.xcor()
        ox = apple.xcor()
def checkboundary():
        distancextron = tron.xcor()
        distanceytron = tron.ycor()
        distancexapple = apple.xcor()
        distanceyapple = apple.ycor()
        print(distancexapple)
        print(distanceyapple)
        print("check",distancexapple)
        if(distanceyapple > 199 or distanceyapple < -199 or distancexapple > 199 or distancexapple < -199):
                wn.clear()
                apple.goto(0,0)
                tron.goto(0,0)
                apple.write("Game over tron1 left the screen", align = ("center"), font = ("Arial",52,"bold"))
        if(distanceytron > 199 or distanceytron < -199 or distancextron > 199 or distancextron < -199):
                wn.clear()
                apple.goto(0,0)
                tron.goto(0,0)
                apple.write("Game over tron2 left the screen", align = ("center"), font = ("Arial",52,"bold"))
        
appleOneList = []
appleTwoList = []
tronOneList = []
tronTwoList = []
x = []

weareat = 0 
def moveapple():
        appleOneList.append(apple.xcor())
        appleTwoList.append(apple.ycor())
        checkboundary()
        print(appleOneList)
        print(appleTwoList)
def movetron():
        tronOneList.append(tron.xcor())
        tronTwoList.append(tron.ycor())
        print(tronTwoList)
        print(tronOneList)
"""def checkCollision():
        applenumber = int(len.appleTwoList) - 1 
        tronnumber  = int(len.tronTwoList) - 1
        xdistance = abs(appleOneList[applenumber] - tronOneList[tronnumber])
        ydistance = abs(tronTwoList[tronnumber] - appleTwoList[tronnumber])
        if(xdistance < 15 and ydistance < 15):
                wn.clear()
                apple.goto(0,0)
                tron.goto(0,0)
                apple.write("Collision you failed", align = ("center"), font = ("Arial",52,"bold"))"""
                


def checkCollision7():
        lena = int(len(appleOneList))
        lent = int(len(tronOneList))
        lent = lent - 1
        lena = lena - 1
        xtronvalue = tronOneList[lent]
        ytronvalue = tronTwoList[lent]
        xapplevalue = appleOneList[lena]
        yapplevalue = appleTwoList[lena]
        distanceapartx = abs(xtronvalue-xapplevalue)
        distanceaparty = abs(ytronvalue-yapplevalue)
        if(distanceaparty < 5 and distanceapartx < 5):
                print("cheese")
                wn.exitonclick()

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


applexcorlist = []
appleycorlist = []
tronxcorlist = []
tronycorlist = []


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
