#   a118_turtles_in_traffic.py
#   Move turtles horizontally and vertically across screen.
#   Stopping turtles when they collide.
import turtle as trtl

# create two empty lists of turtles, adding to them later
horiz_turtles = []
vert_turtles = []

# use interesting shapes    and colors
turtle_shapes = ["circle","circle", "circle", "square", "triangle", "classic"]
horiz_colors = ["red", "blue", "green", "orange", "purple", "gold"]
vert_colors = ["darkred", "darkblue", "lime", "salmon", "indigo", "brown"]

tloc = 50 # turtle location ? 
# create turtles and move them horizontally
for s in turtle_shapes:

  ht = trtl.Turtle(shape=s) # create turtle object with a different shape
  horiz_turtles.append(ht)
  ht.penup()
  new_color = horiz_colors.pop()
  ht.fillcolor(new_color)
  ht.goto(-350, tloc)
  ht.setheading(0)

  vt = trtl.Turtle(shape=s)
  vert_turtles.append(vt)
  vt.penup()
  new_color = vert_colors.pop()
  vt.fillcolor(new_color)
  vt.goto( -tloc, 350)
  vt.setheading(270)
  
  tloc += 50

# TODO: move turtles across and down screen, stopping for collisions



steps = 0
distance = 3
pixel_size = 20
while steps < 50:
    steps = steps + 1
    for ht in horiz_turtles:
        for vt in vert_turtles:
            ht.forward(distance)
            vt.forward(distance)

            #collide if too close
            if (abs(ht.xcor() - vt.xcor()) < pixel_size):
              if (abs(ht.ycor() - vt.ycor()) < pixel_size):
                  for ht in horiz_turtles:
                    for vt in vert_turtles:
                      ht.forward(-distance)
                      vt.forward(-distance)
                      if (abs(ht.xcor() - vt.xcor()) > pixel_size+60):
                        if (abs(ht.ycor() - vt.ycor()) > pixel_size+60):
                          ht.forward(distance)
                          vt.forward(distance)
                              


wn = trtl.Screen()
wn.mainloop()
