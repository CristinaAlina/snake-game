from turtle import Screen
import time
from snake import Snake
from food import Food
from scoreboard import Scoreboard

ALIGNMENT = "center"
FONT = ("Courier", 13, "bold")

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(fun=snake.up, key="Up")
screen.onkey(fun=snake.down, key="Down")
screen.onkey(fun=snake.left, key="Left")
screen.onkey(fun=snake.right, key="Right")

game_over = False
while not game_over:
    screen.update()
    time.sleep(0.1)

    scoreboard.update_scoreboard()
    snake.move()

    # if the snake head is within 15 pixels of the food, or even closer, relocate the food location
    if snake.snake_head.distance(food) < 15:
        food.go_to_random_location()
        scoreboard.increase_score()
        snake.add_body_snake(False)

    # detect collision with wall
    if (snake.snake_head.xcor() > 295 or snake.snake_head.xcor() < -295 or
            snake.snake_head.ycor() > 295 or snake.snake_head.ycor() < -295):
        game_over = True

    # detect collision with tail
    if snake.verify_collision_tail():
        game_over = True

scoreboard.end_of_game()

screen.exitonclick()
