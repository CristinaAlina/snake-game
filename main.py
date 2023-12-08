# TODO: Detect collision with wall
# TODO: Detect collision with tail

from turtle import Screen
import time
from snake import Snake
from food import Food
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()
screen.listen()


game_over = False
while not game_over:
    screen.update()
    time.sleep(0.1)

    screen.onkey(fun=snake.up, key="Up")
    screen.onkey(fun=snake.down, key="Down")
    screen.onkey(fun=snake.left, key="Left")
    screen.onkey(fun=snake.right, key="Right")

    scoreboard.update_scoreboard()
    snake.move()

    # if the snake head is within 15 pixels of the food, or even closer, relocate the food location
    if snake.snake_head.distance(food) < 15:
        food.go_to_random_location()
        scoreboard.increase_score()
        snake.add_body_snake(False)


screen.exitonclick()
