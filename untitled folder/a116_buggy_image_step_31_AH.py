#   a116_buggy_image.py
import turtle as trtl
#Create a spider body
spider = trtl.Turtle()  #Create turtle object
spider.pensize(40)      # pen size 40
spider.circle(20)       # pen circle

#Create a spider head
spider.goto(-30,9)
spider.circle(2.5)
spider.goto(0,0)
#Configure spider legs
legs = 8
length = 34
angle = 120 / legs
spider.pensize(5)       # pen size
count = 0


#Draw Legs
while (count < legs):
  spider.color("blue")
  spider.goto(0,20)
  spider.setheading(angle*count)
  spider.pendown()
  spider.circle(length,120)
  spider.penup()
  count = count + 1
  print("angle*count=", angle*count)
count=0
while (count < legs):
  spider.color("red")
  spider.goto(0,20)
  spider.setheading((angle*count)+310)
  spider.pendown()
  spider.circle(-length,120)
  spider.penup()
  count = count + 1
  print("angle*count=", angle*count)


eyesize = 1
#Spider Eyes
spider.color("Pink")
spider.penup()
spider.goto(-36,18)
spider.pendown()
spider.circle(eyesize)
spider.penup()
spider.goto(-35,2)
spider.pendown()
spider.circle(eyesize)
spider.hideturtle()
spider.penup()

#hide middle from leg
spider.goto(0,20)
spider.pendown()
spider.color('black')
spider.pensize(36)      # pen size 40
spider.circle(10)       # pen circle




wn = trtl.Screen()
wn.mainloop()


