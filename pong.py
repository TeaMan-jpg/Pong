import turtle
import random
import time
import keyboard
sc = turtle.Screen()
sc.setup(600,600)
sc.title("Pong!")
turtles2 = turtle.Turtle()
turtles3 = turtle.Turtle()
bar1 = turtle.Turtle()
bar2 = turtle.Turtle()
ball = turtle.Turtle()
turtles = turtle.Turtle()
turtles1 = turtle.Turtle()
turtles.shape('square')
turtles1.shape('square')
ball.shape('square')
bar1.shape('square')
bar2.shape('square')
bar1.penup()
bar2.penup()
ball.penup()
turtles.penup()
turtles1.penup()
bar1.goto(500,0)
bar2.goto(-500,0)
ball.goto(0,0)
bar1.turtlesize(stretch_wid=6.5)
bar2.turtlesize(stretch_wid=6.5)
bar1.turtlesize(stretch_len=1)
bar2.turtlesize(stretch_len=1)
ball_speed = 7
bar1.dy = 10
bar2.dy = 10
ball.dx = ball_speed
ball.dy = ball_speed
direction = 1
direction1 = 1
n = 0
s = 0
scoreLeft = 0
scoreRight = 0

for i in range(13):
  turtles.clone()
  n += 30
  turtles.goto(0,n)
  turtles1.clone()
  s -= 30
  turtles1.goto(0,s)

turtles2.penup()
turtles2.goto(250,200)
turtles2.write(f"{scoreRight}",True, align="right",font=('Inconsolata',25,'bold'))
turtles2.hideturtle()
turtles3.penup()
turtles3.goto(-250,200)
turtles3.write(f"{scoreLeft}",True, align="left",font=('Inconsolata',25,'bold'))
turtles3.hideturtle()
def up():
    y1 = bar1.ycor()
    turtle.tracer(1)
    y1 += bar1.dy
    bar1.sety(y1)
    if y1 >= 320:
        y1 = 320
        bar1.sety(y1)

def down():
    y2 = bar1.ycor()
    turtle.tracer(1)
    y2 -= bar1.dy
    bar1.sety(y2)
    if y2 <= -320:
        y2 = -320
        bar1.sety(y2)
    
def left():
 
    x2 = bar1.xcor()
    turtle.tracer(1)
    x2 -= 10
    bar1.setx(x2)

def right():
    x1 = bar1.xcor()
    turtle.tracer(1)
    x1 += 10
    bar1.setx(x1)


def up1():
    y3 = bar2.ycor()
    turtle.tracer(1)
    y3 += bar2.dy
    bar2.sety(y3)
    if y3 >= 320:
        y3 = 320
        bar2.sety(y3)
    
def down1():
    y4 = bar2.ycor()
    turtle.tracer(1)
    y4 -= bar2.dy
    bar2.sety(y4)
    if y4 <= -320:
        y4 = -320
        bar2.sety(y4)

def ball_mov():
  global direction
  global direction1
  x = ball.xcor()
  y = ball.ycor() 
  x += (direction * ball.dx)
  y += (direction1 * ball.dy)
  ball.setx(x)
  ball.sety(y)

  if y >= 390:
    direction1 *= -1
  if y <= -390:
    direction1 *= -1

  print(y)
def left1():
    x3 = bar2.xcor()
    turtle.tracer(1)
    x3 -= 10
    bar2.setx(x3)

def right1():
    x4 = bar2.xcor()
    turtle.tracer(1)
    x4 += 10
    bar2.setx(x4)


def collisionright():
  global direction
  global direction1
  x5 = ball.xcor()
  y5 = ball.ycor()
  x6 = bar1.xcor()
  y6 = bar1.ycor()
  print('Call1')
  if (x5 in range(x6+20,x6+21)) and (y5 == y6):
     direction *= -1

def collisionleft():
  global direction
  global direction1
  x5 = ball.xcor()
  y5 = ball.ycor()
  x6 = bar2.xcor()
  y6 = bar2.ycor()
  print('Call2')
  if (x5 in range(x6+20,x6+21)) and (y5 == y6):
    direction *= -1
    direction1 *= random.choice([1,-1])

def collisiontopright():
  global direction
  global direction1
  x5 = ball.xcor()
  y5 = ball.ycor()
  x6 = bar1.xcor()
  y6 = bar1.ycor()
  print('Call')
  if (x5 in range(x6-20,x6-11)) and (y5 in range(y6,y6+66)):
    direction *= -1
    direction1 *= 1
    ball.dx = ball_speed
    ball.dy = ball_speed
    if direction1 == -1:
      direction1 *= -1
      ball.dx = ball_speed
      ball.dy = ball_speed

def collisiontopleft():
  global direction
  global direction1
  x5 = ball.xcor()
  y5 = ball.ycor()
  x6 = bar2.xcor()
  y6 = bar2.ycor()
  print('Call4')
  if (x5 in range(x6+10,x6+21)) and (y5 in range(y6,y6+66)):
    direction *= -1
    direction1 *= 1
    ball.dx = ball_speed
    ball.dy = ball_speed
    if direction1 == -1:
      direction1 *= -1
      ball.dx = ball_speed
      ball.dy = ball_speed

def collisionbottomleft():
  global direction
  global direction1
  x5 = ball.xcor()
  y5 = ball.ycor()
  x6 = bar2.xcor()
  y6 = bar2.ycor()
  print('Call5')
  if (x5 in range(x6+10,x6+21)) and (y5 in range(y6-65,y6)):
    direction *= -1
    if direction1 == -1:
      direction1 *= 1
      ball.dx = ball_speed
      ball.dy = ball_speed
    else:
      direction1 *= -1
      ball.dx = ball_speed
      ball.dy = ball_speed
      
def collisionbottomright():
  global direction
  global direction1
  x5 = ball.xcor()
  y5 = ball.ycor()
  x6 = bar1.xcor()
  y6 = bar1.ycor()
  print('Call7')
  if (x5 in range(x6-20,x6-11)) and (y5 in range(y6-65,y6)):
    direction *= -1
    if direction1 == -1:
      direction1 *= 1
      ball.dx = ball_speed
      ball.dy = ball_speed
    else:
      direction1 *= -1
      ball.dx = ball_speed
      ball.dy = ball_speed
      
      
def scoreCounterRight():
  global scoreRight
  turtles2.clear()
  scoreRight += 1
  turtles2.goto(250,200)
  turtles2.write(f"{scoreRight}",True, align="right",font=('Inconsolata',25,'bold'))

def scoreCounterLeft():
  global scoreLeft
  turtles3.clear()
  scoreLeft += 1
  turtles3.goto(-250,200)
  turtles3.write(f"{scoreLeft}",True, align="left",font=('Inconsolata',25,'bold'))

def victoryright():
    global direction
    global direction1
    x7 = ball.xcor()
    if x7 >= 550:
        ball.hideturtle()
        ball.goto(0,random.randrange(-100,101))
        time.sleep(1.1)
        ball.showturtle()
        direction *= 1
        direction1 *= random.choice([1,-1])
        scoreCounterLeft()
        ball.dx = ball_speed
        ball.dy = ball_speed

def victoryleft():
    global direction
    global direction1
    x8 = ball.xcor()
    if x8 <= -550:
        ball.hideturtle()
        ball.goto(0,random.randrange(-100,101))
        time.sleep(1.1)
        ball.showturtle()
        direction *= 1
        direction1 *= random.choice([1,-1])
        scoreCounterRight()
        ball.dx = ball_speed
        ball.dy = ball_speed



while True:
    if keyboard.is_pressed("W"):
      up1()
    if keyboard.is_pressed("S"):
      down1()
    if keyboard.is_pressed("Up"):
      up()
    if keyboard.is_pressed("Down"):
      down()
    turtle.update()
    ball_mov()
    collisiontopleft()
    collisionbottomleft()
    collisiontopright()
    collisionbottomright()
    victoryright()
    victoryleft()
    if scoreLeft + scoreRight == 5:
      break  
