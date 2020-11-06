#   a114_divisible.py
import turtle as trtl
painter = trtl.Turtle
# get two numbers from user
a = int(input("Enter a number"))
b = int(input("Enter a 2nd number"))
c = a % b
# loop whle the numbers are not divisible (the remainder is 0)
while( c > 0):
  
  # inform user of result 
  print("Your numbers were not divisible")
  # gather user input again
  a = int(input("Enter a number"))
  b = int(input("Enter a 2nd number"))
  c = a % b
print("Yes they are divisble")
# inform user of result 