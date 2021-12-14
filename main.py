#Basic Snake Game
import turtle
import time
import random

#Variables
delay = 0.06
seg = []
curr_score = 0
high_score = []

#Screen Setup
window = turtle.Screen()
window.title('Basic Snake Game')
window.bgcolor('lightblue'), window.setup(width=1000, height=1000)
window.tracer(0) #stops updates

#Snake Setup
snake = turtle.Turtle()
snake.speed(0), snake.shape('square'), snake.color('black')
snake.penup()
snake.goto(0,0)
snake.direction = 'stop'

#Food
food = turtle.Turtle()
food.speed(0), food.shape('circle'), food.color('red')
food.penup()
food.goto(random.randint(-450,450),random.randint(-450,450))

#Score Board
score = turtle.Turtle()
score.speed(0), score.shape('square'), score.color('white')
score.penup()
score.hideturtle(), score.goto(0,400)
score.write("Score: 0   Highest Score: 0",\
align="center", font=("Courier", 24, "normal"))

#Functions
def go_up():
    if snake.direction != 'down':
        snake.direction = 'up'

def go_down():
    if snake.direction != 'up':
        snake.direction = 'down'

def go_left():
    if snake.direction != 'right':
        snake.direction = 'left'

def go_right():
    if snake.direction != 'left':
        snake.direction = 'right'

def move():
    if snake.direction == 'up':
        snake.sety(snake.ycor() + 20)
    elif snake.direction == 'down':
        snake.sety(snake.ycor() - 20)
    elif snake.direction == 'left':
        snake.setx(snake.xcor() - 20)
    elif snake.direction == 'right':
        snake.setx(snake.xcor() + 20)

def update_score_board():
    score.clear()
    score.write("Score: {}   High Score: {}".format(curr_score, max(high_score)),\
align="center", font=("Courier", 24, "normal"))

#Bindings
window.listen()
window.onkeypress(go_up, 'w'), window.onkeypress(go_down, 's')
window.onkeypress(go_left, 'a'), window.onkeypress(go_right, 'd')

#Main code
while True:
    window.update()

    #Check for border collision
    if snake.xcor() > 480 or snake.xcor() < -480 or\
snake.ycor() >480 or snake.ycor() < -480:
        time.sleep(1), snake.goto(0,0)
        snake.direction = 'stop'

        #Remove segments and clear seg list
        for x in seg:
            x.goto(1100,1100)
        seg = []
        curr_score, delay = 0, 0.06
        update_score_board()

    #Check for food collision and update food location
    if snake.distance(food) < 20: #pixel size is 20
        food.goto(random.randint(-450,450),random.randint(-450,450))

        #Update snake body
        new_seg = turtle.Turtle()
        colors = ['orange', 'yellow', 'green', 'blue', 'violet']
        col = random.choice(colors)
        new_seg.speed(0), new_seg.shape('square'), new_seg.color(col), new_seg.penup()
        seg.append(new_seg)
        delay -= 0.001
        curr_score += 10
        high_score.append(curr_score)
        update_score_board()

    #Update end seg with new seg if food collected and shift everything up
    for i in range(len(seg)-1, 0, -1):
        x, y = seg[i-1].xcor(), seg[i-1].ycor()
        seg[i].goto(x,y)

    #Update seg 0 to head
    if len(seg) > 0:
        x, y = snake.xcor(), snake.ycor()
        seg[0].goto(x,y)

    move()
    #Check for self collision with seg
    for i in seg:
        if i.distance(snake) < 20:
            time.sleep(1), snake.goto(0,0)
            snake.direction = 'stop'

            #Remove segments and clear seg list
            for x in seg:
                x.goto(1100, 1100)
            seg = []
            curr_score, delay = 0, 0.06
            update_score_board()

    time.sleep(delay)


