#   a115_robot_maze.py
import turtle as trtl

#----- maze and turtle config variables
screen_h = 400
screen_w = 420
startx = -100
starty = -100
turtle_scale = 1.5

#------ robot commands
def move():
  robot.dot(10)
  robot.fd(50)

def turn_left():
  robot.speed(0)
  robot.lt(90)
  robot.speed(2)

#----- init screen
wn = trtl.Screen()
wn.setup(width=screen_w, height=screen_h)
robot_image = "robot2.gif"
stop_image = "stopgood.gif"
mustang_image = "mustang.gif"
car_image = "car.gif"
wn.addshape(robot_image)
wn.addshape(stop_image)
stop = trtl.Turtle(shape=stop_image)
stop.penup()
stop.setposition(-500,0)
stop.stamp()

cars = ["robot2.gif","stopgood.gif","audi.gif"]

startx = -100
starty = 50
b = 0
for s in cars:
    car = trtl.Turtle(s) # create turtle object with a different shape
    car.penup()
    car.goto(startx,b)
    car.forward(500)
    b = b+500



    
#----- init robot
'''robot = trtl.Turtle(shape=robot_image)
robot.penup()
while(1==1):
    robot.forward(500)
    robot.forward(-500)'''

#---- TODO: change maze here
#---- TODO: begin robot movement here
# move robot forward with move()
# turn robot left with turn_left()
# sample while loop:
'''
i = 0
while (i < 3): # forward 3
  move()
  i = i + 1 
'''

#---- end robot movement 

wn.mainloop()

