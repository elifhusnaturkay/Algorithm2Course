#Q1: square

import turtle
wn = turtle.Screen()
wn.bgcolor("lightpink")
alex = turtle.Turtle()
alex.speed(2)
alex.pensize(10)
alex.color("green yellow")
alex.shape("turtle")

tess = turtle.Turtle()
tess.color("gold")
tess.pensize(10)
tess.shape("turtle")
tess.penup()
size = 4
for i in range(30):
   tess.stamp()             
   size = size + 3          
   tess.forward(size)      

tes = turtle.Turtle()
tes.color("gold")
tes.pensize(10)
tes.shape("turtle")
tes.penup()

alex.forward(50)
alex.left(90)
alex.forward(50)
alex.left(90)
alex.forward(50)
alex.left(90)
alex.forward(50)
alex.left(90)
alex.forward(100)

#tringle
for i in range(3):
  tess.forward(120)            
  tess.left(120)

for i in range(4):
  alex.forward(120)
  alex.left(90)

for i in range(3):
  alex.right(120)
  alex.forward(120) 

for i in range(3):
  tes.right(90)
  tes.forward(120) 
  
tess.forward(50)            
tess.left(100)
tess.forward(50)
tess.left(130)
tess.forward(60)
tess.left(130)

wn.mainloop()


#Q1
for i in range(1000):
  print("We like Python's turtles!")



