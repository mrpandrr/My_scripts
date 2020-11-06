# import turtle module 
import turtle as trtl 

# create turtle object
painter = trtl.Turtle()
painter.pensize(5)

#move turtle without makrking a line
painter.penup()
painter.goto(0,-20)
painter.pendown()

# draw a semi-circle
painter.circle(100,180)

#move turtle without marking a line
painter.penup()
painter.goto(0,20)
painter.pendown()

#draw a 3 step smei circle
painter.circle(100,180,3)
painter.circle(100,180,8)


#create a screen object and make it persist
wn = trtl.Screen()
wn.mainloop()
