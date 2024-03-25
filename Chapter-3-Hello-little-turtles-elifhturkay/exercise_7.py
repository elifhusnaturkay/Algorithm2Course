#Q7
import turtle
alex = turtle.Turtle()
alex.speed(2)
alex.pensize(10)
alex.color("green yellow")
alex.shape("turtle")

data = [160, -43, 270, -97, -43, 200, -940, 17, -86]
for i in data:
  alex.left(i)
  alex.forward(100)

