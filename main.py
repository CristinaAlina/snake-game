

# TODO: Create snake food
# TODO: Detect collision with food
# TODO: Create a score board
# TODO: Detect collision with wall
# TODO: Detect collision with tail

from turtle import Turtle, Screen
import time


def add_body_snake(body_snake):
    new_square = Turtle("square")
    new_square.pensize(20)
    new_square.color("DarkGreen", "DarkGreen")
    new_square.penup()
    body_snake.append(new_square)
    new_square.goto((-20 * body_snake.index(new_square)), 0)


screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)

snake_body = []
# create the starting shape of snake with 3 squares
for index_square in range(3):
    add_body_snake(snake_body)

# TODO: Move the snake
game_over = False
while not game_over:
    screen.update()
    time.sleep(0.1)
    for square_num in range(len(snake_body)-1, 0, -1):
        new_x = snake_body[square_num-1].position()[0]
        new_y = snake_body[square_num-1].position()[1]
        snake_body[square_num].goto(new_x, new_y)
    snake_body[0].forward(20)


screen.exitonclick()
