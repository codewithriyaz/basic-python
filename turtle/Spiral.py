import turtle
pen = turtle.Pen()
pen.shape("turtle")
pen.color("red")
pen.speed(0)
for i in range(200):
    pen.circle(i*2)
    pen.left(10)