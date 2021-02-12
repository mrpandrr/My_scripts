#   encode.py
#   Note this will not run in the code editor and must be downloaded
import tkinter as tk
import turtle as trtl
import subprocess
from PIL import ImageGrab, Image, ImageDraw



message = input("What would you like to encode:") # Change this to encode a different message. Length limit 20 characters.

characters_as_ints = []                 #List created for the message to encode
for cha in message:
  characters_as_ints.append(ord(cha))   #Adds the letters into list and turns letter to unicode
print(characters_as_ints)               #Prints the list

characters_as_bits = []                 #For the           
for integ in characters_as_ints:
  characters_as_bits.append('{0:08b}'.format(integ))  #switch to binary after switching letter to number
print(characters_as_bits) #Prints characters as bits

bits_as_ints = []
for index in range(0,len(characters_as_bits)):  
  for bit in characters_as_bits[index]:      #For bit in characters as bits goes to the number index you are on then adds the value
    bits_as_ints.append(bit)                    
print(bits_as_ints)                           #completely integer now

screen = trtl.getscreen()
screen.screensize(bg="black")           
screen.setup(400,500)
drawer = trtl.Turtle()

topypoint = 121
drawer.penup()
drawer.goto(200,topypoint)
drawer.shape("square")
drawer.color("blue")
drawer.shapesize(2)

message_length = len(bits_as_ints)    # how many letters needed to encode = length of message
index = 0
spacing = -3
while index < message_length:         #When
  if index % 8 == 0:                  #When created 8 you set the row down by 21 points
    drawer.goto(drawer.xcor()-41, topypoint)
  if spacing % 8 == 0:
    drawer.goto(drawer.xcor(), drawer.ycor()-41)
  if bits_as_ints[index]=='1':        #If bits as integers is 1 then you stamp a mark if you binary is on at that value
    drawer.color("blue")
    drawer.stamp()
  if bits_as_ints[index]=='0':        #If bits as integers is 1 then you stamp a mark if you binary is on at that value
    drawer.color("green")
    drawer.stamp()
  drawer.goto(drawer.xcor(),drawer.ycor()-41)                 #After tested or stamp you move on to the next square in your image
  index = index + 1                   #This allows variable to increase and allow loop to continue message length loops until it hits whole message in the image
  spacing = spacing + 1
  print(spacing)



screen = drawer.getscreen()
root = trtl.getcanvas().winfo_toplevel()

# draw the message instead of taking a screenshot for macOS users
def draw_message(im_size, x, y):
    im = Image.new("RGBA", im_size, (255,255,255,0))
    draw = ImageDraw.Draw(im)
    message_length = len(bits_as_ints)
    index = 0
    while index < message_length:
      if index % 8 == 0:
        x = im_size[0]/2-200-10.5
        y += 21
      if bits_as_ints[index]=='1':
        draw.rectangle([x,y,x+21,y+21], fill="blue") #stamp
      x += 21
      index = index + 1
    im.save("macOutput.gif")

def create_image(widget):
    x=root.winfo_rootx()
    y=root.winfo_rooty()
    x1=x+widget.window_width()
    y1=y+widget.window_height()
    im = ImageGrab.grab().crop((x,y,x1,y1))
    im.save("output.gif")
    print(im.size)

    # create an image for macOS users
    draw_message(im.size,im.size[0]/2-200-10.5,im.size[1]/2-221-10.5) # (149.5,98) in ImageDraw is equivalent to (205,275) in PIL 


create_image(screen)

screen.mainloop()