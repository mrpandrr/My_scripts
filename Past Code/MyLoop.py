#   a113_numeric_comparison.py
#   Predict what the following code will do.
import turtle as trtl

painter = trtl.Turtle()

# new starting location so the entire
# octagon is visible
painter.penup()
painter.goto(-50, 150)
painter.pendown()
painter.shape("circle")

count = 0
while (count < 18):
  painter.right(20)
  painter.forward(20)
  painter.stamp()
  count = count + 1 # Recall this is incrementing, adding one to  
                    # the value stored in a variable and then storing 
                    # the result back into the same variable.

wn = trtl.Screen()
wn.mainloop()