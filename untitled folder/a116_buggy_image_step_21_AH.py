#   a116_buggy_image.py
import turtle as trtl

spider = trtl.Turtle()  #Create turtle object
spider.pensize(40)      # pen size 40
spider.circle(20)       # pen circle
#Variables
legs = 6
length = 70
angle = 380 / legs
spider.pensize(5)       # pen size
count = 0
while (count < legs):
  spider.goto(0,0)
  spider.setheading(angle*count)
  spider.forward(length)
  count = count + 1
  print("angle*count=", angle*count)
spider.hideturtle()
wn = trtl.Screen()
wn.mainloop()