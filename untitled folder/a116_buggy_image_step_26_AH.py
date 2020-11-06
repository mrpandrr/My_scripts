#   a116_buggy_image.py
import turtle as trtl
#Create a spider body
spider = trtl.Turtle()  #Create turtle object
spider.pensize(40)      # pen size 40
spider.circle(20)       # pen circle

#Create a spider head


#Configure spider legs
legs = 8
length = 70
angle = 360 / legs
spider.pensize(5)       # pen size
count = 0


#Draw Legs
while (count < legs):
  spider.goto(0,20)
  spider.setheading(angle*count)
  spider.forward(length)
  count = count + 1
  print("angle*count=", angle*count)
spider.hideturtle()
wn = trtl.Screen()
wn.mainloop()