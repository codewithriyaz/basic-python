import turtle
turtle.shape("turtle")
turtle.speed(1)
turtle.fillcolor("red")
turtle.pencolor("blue") 
turtle.begin_fill()
for i in range(4):
    turtle.forward(100)
    turtle.right(90)
turtle.end_fill()
turtle.done()