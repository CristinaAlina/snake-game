
# TODO: Move the snake
# TODO: Create snake food
# TODO: Detect collision with food
# TODO: Create a score board
# TODO: Detect collision with wall
# TODO: Detect collision with tail

from turtle import Turtle, Screen

# TODO: Create a snake body
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

snake_body = []
# create the starting shape of snake with 3 squares
for index_square in range(3):
    add_body_snake(snake_body)


screen.exitonclick()