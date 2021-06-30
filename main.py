from turtle import Screen,Turtle
import time
from scoreboard import ScoreBoard
from food import Food
from snake import Snake
screen = Screen()
screen.tracer(0)
snake = Snake()
food = Food()
sb = ScoreBoard()
screen.setup(width=600,height=600)
screen.bgcolor("black")
screen.listen()
screen.onkey(snake.up,"Up")
screen.onkey(snake.down,"Down")
screen.onkey(snake.left,"Left")
screen.onkey(snake.right,"Right")
count = 0
game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.snake_movement()
    #detect the collision with food
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        sb.increase_score()
    #detect the collosion with wall
    if snake.head.xcor() < -290 or snake.head.xcor() >290 or snake.head.ycor() > 290 or snake.head.ycor() < -290:
        sb.score_reset()
        snake.snake_reset()
    for segment in snake.segments[1:]:
            if snake.head.distance(segment)<10:
                sb.score_reset()
                snake.snake_reset()





















screen.exitonclick()