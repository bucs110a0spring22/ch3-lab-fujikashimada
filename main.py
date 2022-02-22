import turtle               #1. import modules
import random

#Part A
window = turtle.Screen()       # 2.  Create a screen
window.bgcolor('lightblue')


michelangelo = turtle.Turtle()    # 3.  Create two turtles
leonardo = turtle.Turtle()
michelangelo.color('orange')
leonardo.color('blue')
michelangelo.shape('turtle')
leonardo.shape('turtle')
michelangelo.speed(1)
leonardo.speed(1)

michelangelo.up()          # 4.  Pick up the pen so we don’t get lines
leonardo.up()
michelangelo.goto(-100,20)
leonardo.goto(-100,-20)

## 5. your code goes here
random_a1 = random.randrange(1,100)
michelangelo.forward(random_a1)
leonardo.forward(random_a1)
michelangelo.goto(-100,20)
leonardo.goto(-100,-20)


for i in range(10):
    michelangelo.forward(random.randrange(1,10))
    leonardo.forward(random.randrange(1,10))
michelangelo.goto(-100,20)
leonardo.goto(-100,-20)
  
# Part B - complete part B here
sides = (3,4,6,9,12)
for i in (sides):
    for shapes in range(i):
      michelangelo.down()
      michelangelo.forward(50)
      michelangelo.left(360/i)
    michelangelo.clear()
     
window.exitonclick()
