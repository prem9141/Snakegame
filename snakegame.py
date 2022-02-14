from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import ScoreBoard
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Classic Snake Game")
screen.tracer(0)
screen.listen()

snake = Snake()
food = Food()
scoreboard = ScoreBoard()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

is_game_over = False
while not is_game_over:
    scoreboard.display_score()
    screen.update()
    time.sleep(.10)
    snake.move()

    # Detect Snake collision with Food
    if snake.head.distance(food) < 15:
        food.create_food()
        snake.extend()
        scoreboard.update_score()

    # Detect Snake collision with Wall
    if snake.head.xcor() > 290 or snake.head.xcor() < -290 or snake.head.ycor() > 290 or snake.head.ycor() < -290:
        is_game_over = True
        scoreboard.game_over()

    # Detect Snake collision with Tail
    for square in snake.squares[1:]:
        if snake.head.distance(square) < 10:
            is_game_over = True
            scoreboard.game_over()

screen.exitonclick()
