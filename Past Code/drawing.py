import turtle as trtl

painter = trtl.Turtle()

#Asking for what colors
color = input("What color would you like your wagon")
border = input("What color would you like the border to be")
painter.pensize(10)
painter.pencolor(border)
painter.fillcolor(color)
painter.begin_fill()

#Wheel Location corner
painter.penup()
painter.goto(-150,0)
painter.pendown()

#Circle Wheel 
painter.circle(30)
painter.end_fill()

#Wagon Location corner
painter.penup()
painter.goto(-150,100)
painter.pendown()
painter.right(90)
painter.forward(40)
painter.right(270)
painter.forward(200)
painter.right(270)
painter.forward(40)

#Wagon Location corner
painter.penup()
painter.goto(80,30)
painter.pendown()


#Circle Wheel 
painter.begin_fill()
painter.circle(30)
painter.end_fill()
painter.penup()




#Drawing Board
wn = trtl.Screen()
wn.mainloop()

