#   a123_apple_letters.py
import random as rand
import turtle as trtl
#TODO Create a function that takes a turtle as its parameter and gives that turtle (apple)
apple_image = "apple.gif"

wn = trtl.Screen()
wn.setup(width=0.5, height=0.5)
wn.addshape(apple_image)
wn.bgpic("background.gif")
apple = trtl.Turtle()

Letter = 'A' #Starting letter is A
letters = ["a","s","d","f","g","h","j","k","l"]
myapplesList = []
appleLetters = []

for i in range(9):
  myapplesList.append(trtl.Turtle())
  appleLetters.append(rand.choice(letters))


def draw_apple(index):
  myapplesList[index].penup()
  myapplesList[index].shape(apple_image)
  wn.tracer(False)
  myapplesList[index].goto(rand.randint(-150,150),rand.randint(-30,125)) #reset position
  myapplesList[index].sety(myapplesList[index].ycor()-30)
  myapplesList[index].color("white")
  myapplesList[index].write(appleLetters[index], align="center",font=("Arial",62,"bold"))
  myapplesList[index].sety(myapplesList[index].ycor()+30)
  myapplesList[index].showturtle()
  wn.tracer(True)
  wn.update()

ground_height = -162
def drop_apple(i):
  myapplesList[i].penup()
  myapplesList[i].clear()
  myapplesList[i].goto(apple.xcor(),ground_height)
  x = myapplesList[i].xcor()
  y = myapplesList[i].ycor()
  myapplesList[i].hideturtle()
  appleLetters[i] = rand.choice(letters)
  draw_apple(i)
def userclickA():
  for i in range(5):
    if appleLetters[i] == 'a':
      drop_apple(i)
def userclickS():
  for i in range(5):
    if appleLetters[i] == 's':
      drop_apple(i)
def userclickD():
  for i in range(5):
    if appleLetters[i] == 'd':
      drop_apple(i)
def userclickF():
  for i in range(5):
    if appleLetters[i] == 'f':
      drop_apple(i)
def userclickG():
  for i in range(5):
    if appleLetters[i] == 'g':
      drop_apple(i)
def userclickH():
  for i in range(5):
    if appleLetters[i] == 'h':
      drop_apple(i)
def userclickL():
  for i in range(5):
    if appleLetters[i] == 'l':
      drop_apple(i)
def userclickJ():
  for i in range(5):
    if appleLetters[i] == 'j':
      drop_apple(i)
def userclickK():
  for i in range(5):
    if appleLetters[i] == 'k':
      drop_apple(i)
def userclickL():
  for i in range(5):
    if appleLetters[i] == 'l':
      drop_apple(i)

def draw_an_A(index):
  myapplesList[index].write(appleLetters[index], align="center",font=("Arial",62,"bold"))

for i in range(5):
  draw_apple(i)


wn.onkeypress(userclickA,'a')
wn.onkeypress(userclickS,'s')
wn.onkeypress(userclickD,'d')
wn.onkeypress(userclickF,'f')
wn.onkeypress(userclickG,'g')
wn.onkeypress(userclickH,'h')
wn.onkeypress(userclickJ,'j')
wn.onkeypress(userclickK,'k')
wn.onkeypress(userclickL,'l')

wn.listen()

wn.mainloop()
