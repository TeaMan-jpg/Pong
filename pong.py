import turtle
import random
#import math
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
#bar1.setheading(90)
#bar2.setheading(90)
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
#bar1.shapesize(stretch_wid=6.5,stretch_len=1)
#bar2.shapesize(stretch_wid=6.5,stretch_len=1)
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
#def increaseSize():
 #   size = bar1.turtlesize()
 #   increase = tuple([ball_speed * num for num in size])
  #  bar1.turtlesize(*increase)

#def increaseSize2():
#    size = bar2.turtlesize()
#    increase = tuple([ball_speed * num for num in size])
#    bar2.turtlesize(*increase)

#increaseSize()
#increaseSize2()
def up():
    #tim.setheading(90)
    y1 = bar1.ycor()
    turtle.tracer(1)
    y1 += bar1.dy
    bar1.sety(y1)
    if y1 >= 320:
        y1 = 320
        bar1.sety(y1)

#def up3()
 #   #tim.setheading(90)
  #  y1 = tim.ycor()
   # turtle.tracer(1)
    #y1 += tim.dy
    #tim.sety(y1)

def down():
    #tim.setheading(270)
    y2 = bar1.ycor()
    turtle.tracer(1)
    y2 -= bar1.dy
    bar1.sety(y2)
    if y2 <= -320:
        y2 = -320
        bar1.sety(y2)
    
    
#def down3():
#    #tim.setheading(270)
#    y2 = tim.ycor()
#    turtle.tracer(1)
 #   y2 -= 10
  #  tim.sety(y2)


def left():
   # tim.setheading(180)
    x2 = bar1.xcor()
    turtle.tracer(1)
    x2 -= 10
    bar1.setx(x2)

def right():
   #tim.setheading(0)
    x1 = bar1.xcor()
    turtle.tracer(1)
    x1 += 10
    bar1.setx(x1)


def up1():
    #tim.setheading(90)
    y3 = bar2.ycor()
    turtle.tracer(1)
    y3 += bar2.dy
    bar2.sety(y3)
    if y3 >= 320:
        y3 = 320
        bar2.sety(y3)
    
#def up2():
    #tim.setheading(90)
 #   y3 = tim2.ycor()
  #  turtle.tracer(1)
   # y3 += 10
    #tim2.sety(y3)
    #if y3 <= 140:
     #   tim.sety(y3)
def down1():
    #tim.setheading(270)
    y4 = bar2.ycor()
    turtle.tracer(1)
    y4 -= bar2.dy
    bar2.sety(y4)
    if y4 <= -320:
        y4 = -320
        bar2.sety(y4)
#def down2():
#  y4 = tim2.ycor()
#  turtle.tracer(1)
#  y4 -= 10
 # tim2.sety(y4)
def ball_mov():
  #randomise direction1 for change in direction
  #direction variable would change based on who won the previous round
  global direction
  global direction1
  x = ball.xcor()
  y = ball.ycor() 
  x += (direction * ball.dx)
  y += (direction1 * ball.dy)
  ball.setx(x)
  ball.sety(y)
  #takes into account angle
  #make it more flexible
 # if x >= 300:
    
 #   x = 100
 #   y = 70
 #   ball.setx(x)
 #   ball.sety(y)
    #x *= -(ball.dx)
    #ball.setx(x)
 # if x <= -300:
    
 #   x = 100
 #   y = 70
 #   ball.setx(x)
 #   ball.sety(y)
    #x *= -(ball.dx)
    #ball.setx(x)

  if y >= 390:
    direction1 *= -1
  if y <= -390:
    direction1 *= -1

  print(y)
def left1():
   # tim.setheading(180)
    x3 = bar2.xcor()
    turtle.tracer(1)
    x3 -= 10
    bar2.setx(x3)

def right1():
   #tim.setheading(0)
    x4 = bar2.xcor()
    turtle.tracer(1)
    x4 += 10
    bar2.setx(x4)



#def ballmov():
#  headings = [0,45,90]
#  ball.setheading(random.choice(headings))
#  ballx = ball.xcor()
#  bally = ball.ycor()
  
#turtle.listen()

def collisionright():
  global direction
  global direction1
  x5 = ball.xcor()
  y5 = ball.ycor()
  x6 = bar1.xcor()
  y6 = bar1.ycor()
  print('Call1')
   #x5 == x6 
  if (x5 in range(x6+20,x6+21)) and (y5 == y6):
   # x5 *= -1
   # y5 *= -1
   # ball.setx(x5)
   # ball.sety(y5)
   direction *= -1

def collisionleft():
  global direction
  global direction1
  x5 = ball.xcor()
  y5 = ball.ycor()
  x6 = bar2.xcor()
  y6 = bar2.ycor()
  print('Call2')
   #x5 == x6
  if (x5 in range(x6+20,x6+21)) and (y5 == y6):
    
   # x5 *= -1
   # y5 *= -1
   # ball.setx(x5)
   # ball.sety(y5)
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
   #x5 == x6
  if (x5 in range(x6-20,x6-11)) and (y5 in range(y6,y6+66)):
    #if range is not working then change back to y6,y6+65
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
   #x5 == x6
  if (x5 in range(x6+10,x6+21)) and (y5 in range(y6,y6+66)):
    #if range is not working then change back to y6,y6+65
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
   #x5 == x6
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
    #direction *= -1
    #direction1 *= -1
    #if direction1 == -1:
    #  direction1 *= 1

def collisionbottomright():
  # ball goes down diagonally on the bar on the right
  global direction
  global direction1
  x5 = ball.xcor()
  y5 = ball.ycor()
  x6 = bar1.xcor()
  y6 = bar1.ycor()
  print('Call7')
  #x5 == x6
  if (x5 in range(x6-20,x6-11)) and (y5 in range(y6-65,y6)):
    #direction *= -1
    #if direction1 == -1:
    #  direction1 *= 1
    #else:
    #  direction1 *= -1
    #ball.dx += ball_speed
    #ball.dy += ball_speed
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





#turtle.onkey(up, "Up")  # This will call the up function if the "Left" arrow key is pressed

# <REMOVE IF FAILED>
# turtle.onkey(fun=up,key='Up')
# turtle.onkey(fun=down,key='Down')

#turtle.onkey(fun=left,key='Left')
#turtle.onkey(fun=right,key='Right')
#up1()
#up()
#while True:
#  time.sleep(ball_speed)
#  down2()
#  time.sleep(1)
#  up3()
#  time.sleep(ball_speed)
#  up2()
 # time.sleep(1)
##  up3()
#turtle.onkey(down, "Down")
#turtle.onkey(left, "Left")
#turtle.onkey(right, "Right")

#turtle.onkey(up1, "w")  # This will call the up function if the "Left" arrow key is pressed
#turtle.onkey(down1, "s")
#turtle.onkey(left1, "a")
#turtle.onkey(right1, "d")

# <REMOVE IF FAILED>
# turtle.onkey(fun=up1,key='w')
# turtle.onkey(fun=down1,key='s')

# Please be more smarter thank you toby
#turtle.onkey(fun=left1,key='a')
#turtle.onkey(fun=right1,key='d')

#create a ball later


#ball.setheading(45)
#ballx = ball.xcor()
#bally = ball.ycor()
#headings = [45,0,-45,135,180,-135] 

#balls = math.sqrt(ball.dx**ball_speed + ball.dy**ball_speed)
#balls.left(random.choice(headings))
#time.sleep(5)
#ball.forward(balls)
#ballx += ball.dx
#bally += ball.dy
"""
class KeyState:
  def __init__(self, k):
    # initialises the class
    self.is_down = False

    def selfDown():
      # checks if key is pressed
      self.is_down = True
    def selfUp():
      # checks if key is not pressed
      self.is_down = False
    
    turtle.onkeypress(fun=selfDown,key=k)
    turtle.onkeyrelease(fun=selfUp,key=k)
  def func_is_down(self):
    # returns if the key is pressed or not
    return self.is_down

keyW = KeyState("w")
keyS = KeyState("s")
keyUP = KeyState("Up")
keyDOWN = KeyState("Down")

lastRefresh = 0
"""
while True:
  #currentTick = time.clock_gettime(1);
 ## if currentTick-lastRefresh > 0.04:
 #   lastRefresh = currentTick
    if keyboard.is_pressed("W"):
      up1()
   # if keyW.func_is_down() == True:
    #  up1()
    if keyboard.is_pressed("S"):
      down1()
    #if keyS.func_is_down():
     # down1()
    if keyboard.is_pressed("Up"):
      up()
    #if keyUP.func_is_down() == True:
     # up()
    if keyboard.is_pressed("Down"):
      down()
    #if keyDOWN.func_is_down():
     # down()
    turtle.update()
    #print(bar2.ycor())
   # print(ball.ycor())
    ball_mov()
   # collisionleft()
   # collisionright()
    collisiontopleft()
    collisionbottomleft()
    collisiontopright()
    collisionbottomright()
   # collisionleft()
   # collisionright()
    #if ball.xcor() >= 300:
    victoryright()
    
    #elif ball.xcor() <= -300:
    victoryleft()
    if scoreLeft + scoreRight == 5:
      break  
 # ball.setx(ball.xcor() + ball.dx)
 # ball.sety(ball.ycor() + ball.dy)
 # x = ball.setx(ball.xcor() + ball.dx)
 # y = ball.sety(ball.ycor() + ball.dy)
 # if x >= 300 or y >= 70:
 #   x = 300
 #   ball

#ballsdif = balls1 - bally
#ballsdif1 = balls - ballx

#ball.left(0.5*120)

#make the ball go left at an angle
#add collision
#maybe add reset if ball goes beyond bar/paddle
#use pygame for more complex projects
 #   ball

#ballsdif = balls1 - bally
#ballsdif1 = balls - ballx

#ball.left(0.5*120)

#finale (maybe)
# add scoring system -- ongoing but getting close
