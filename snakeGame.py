import turtle
import time
import random

delay=0.1
score=0
max_score=0

# game window
wn=turtle.Screen()
wn.title("Snake Game")
wn.bgcolor("#000000")
wn.setup(width=600,height=600)
wn.cv._rootwindow.resizable(True,True)
wn.tracer(0)


#snake head

head=turtle.Turtle()
head.shape("square")
head.color("green")
head.penup()
head.goto(0,0)
head.speed(0)
head.direction="stop"


# creat food

food=turtle.Turtle()
shapes=random.choice(["circle"])
colors=random.choice(["red"])
food.shape(shapes)
food.color(colors)
food.speed(0)
food.penup()
food.goto(0,100)

#create score

word=turtle.Turtle()
word.shape("square")
word.color("white")
word.penup()
word.speed(0)
word.goto(0,250)
word.hideturtle()
word.write("Score: 0   High Score: 0",align="center",font=("Arial",30,"bold"))


#motion

def goup():
    if head.direction != 'down':
        head.direction='up'
        
def godown():
    if head.direction != 'up':
        head.direction='down'

def goleft():
    if head.direction != 'right':
        head.direction='left'

def goright():
    if head.direction != 'left':
        head.direction='right'

def move():
    if head.direction =="up":
        y = head.ycor()
        head.sety(y+20)
        
    if head.direction=="down":
        y = head.ycor()
        head.sety(y-20)

    if head.direction=="left":
        x = head.xcor()
        head.setx(x-20)

    if head.direction=="right":
        x = head.xcor()
        head.setx(x+20)
    
# control

wn.listen()
wn.onkeypress(goup,'Up')
wn.onkeypress(godown,'Down')
wn.onkeypress(goleft,'Left')
wn.onkeypress(goright,'Right')

snake=[]

#screen updated

def update_screen():
    wn.update()
    time.sleep(delay)


while True:
    update_screen()

  
    if head.xcor()>290 or head.xcor()< -290 or head.ycor()>290 or head.ycor()< -290:
        time.sleep(1)
        head.goto(0,0)
        head.direction="stop"
        
        shapes=random.choice(["circle","triangle","turtle"])
        colors=random.choice(["black","red","orange","yellow","white"])
       
        for segment in snake:
            segment.goto(1000,1000)

        snake.clear()
        score = 0
        delay=0.1
        word.clear()
        word.write(f"Score: {score}   High Score: {max_score}",align="center",font=("Arial",30,"bold"))

#eating food
    if head.distance(food)<20:
            x = random.randint(-270,270)
            y = random.randint(-270,270)
            food.goto(x,y)

            new_length = turtle.Turtle()
            new_length.shape("square")
            new_length.color('blue')
            new_length.speed(0)
            new_length.penup()
            
            snake.append(new_length)
            delay-=0.001
            score+=10
            
            if score > max_score:
                max_score = score

            word.clear()
            word.write(f"Score: {score}   High Score: {max_score}",align="center",font=("Arial",30,"bold"))

    for index in range(len(snake)-1,0,-1):
        x = snake[index-1].xcor()
        y = snake[index-1].ycor()
        snake[index].goto(x,y)

    if len(snake)>0:
        x =head.xcor()
        y =head.ycor()
        snake[0].goto(x,y)

    move()
