#Q12
import turtle
wn = turtle.Screen()
wn.bgcolor("lightpink")
alex = turtle.Turtle()
alex.speed(70)
alex.pensize(10)
alex.color("green yellow")
alex.shape("turtle")

for step in range(12):
  alex.penup()
  alex.forward(100)
  alex.left(180)
  size = 4
  for i in range(1):
     size = size + 3          
     alex.forward(size)
     alex.stamp() 
     alex.penup()
  alex.forward(100)
  alex.left(30)

tess = turtle.Turtle()
tess.pensize(1)
tess.color("green yellow")
#tess.shape("square")

for step in range(12):
  tess.penup()
  tess.forward(60)
  tess.left(180)
  size = 4
  for i in range(1):
     size = size + 3          
     tess.forward(size)
     tess.stamp() 
     tess.penup()
  tess.forward(60)
  tess.left(30)

turtle.done()