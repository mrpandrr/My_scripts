#   a114_nested_loops_2.py 
import turtle as trtl

painter = trtl.Turtle()
painter.shape("circle")
painter.hideturtle()
painter.penup()

x = -200
while (x < 200): 
  x = x + 50
  y = 200
  while (y > 0):
    y = y - 50
    z = y%100
    painter.goto(x,y)
    painter.color("blue")
    if(z==0):
        painter.color("black")
    if(y==50):
        painter.color("pink")
    painter.stamp()
  painter.goto(x,y)

  painter.color("red")

  painter.stamp()


wn = trtl.Screen()
wn.mainloop()