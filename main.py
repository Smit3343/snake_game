import time
from turtle import Screen
from snake import Snake
from food import Food
from scoreBoard import ScoreBoard

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor('black')
screen.title('My Snake Game')
screen.tracer(0)

snake = Snake()
food = Food()
scoreBoard = ScoreBoard()

screen.listen()
screen.onkey(key='Up', fun=snake.up)
screen.onkey(key='Down', fun=snake.down)
screen.onkey(key='Left', fun=snake.left)
screen.onkey(key='Right', fun=snake.right)

is_game_on = True
while is_game_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    # detect collision with food
    if snake.head_segment.distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreBoard.increase_score()

    # delect collision with tail
    # if head collides with any segment in the tail:
    # game over
    for segment in snake.segment_list[1:]:
        if snake.head_segment.distance(segment) < 10:
            scoreBoard.game_over()
            is_game_on = False
            break

    if snake.head_segment.xcor() > 280 or snake.head_segment.xcor() < -280 or snake.head_segment.ycor() > 280 or snake.head_segment.ycor() < -280:
        is_game_on = False
        scoreBoard.game_over()

screen.exitonclick()
