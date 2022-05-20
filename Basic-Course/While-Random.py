import random
from turtle import *
number = 1
turtle = Turtle()
while number != 0:
    number = random.randrange(10)
    print(number)
    turtle.color("green")
    turtle.circle(number*10)
    turtle.left(number*2)