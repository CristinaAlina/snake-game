from turtle import Turtle

MOVE_DISTANCE = 20
EAST = 0
NORTH = 90
WEST = 180
SOUTH = 270


class Snake:
    def __init__(self):
        self.body_snake = []
        # create the starting shape of snake with 3 squares
        for index_square in range(3):
            self.add_body_snake()
        self.snake_head = self.body_snake[0]
        self.head_orientation = self.snake_head.heading()

    def add_body_snake(self):
        new_square = Turtle("square")
        new_square.pensize(20)
        new_square.color("DarkGreen", "DarkGreen")
        new_square.penup()
        self.body_snake.append(new_square)
        # for each new square added in the list, we need to positioned it starting with 0, by -MOVE_DISTANCE on x-axis
        # according to its index from the list, to format a continue line of squares, one by one
        new_square.goto((-MOVE_DISTANCE * self.body_snake.index(new_square)), 0)

    def move(self):
        for square_num in range(len(self.body_snake) - 1, 0, -1):
            new_x = self.body_snake[square_num - 1].position()[0]
            new_y = self.body_snake[square_num - 1].position()[1]
            self.body_snake[square_num].goto(new_x, new_y)
        self.snake_head.forward(MOVE_DISTANCE)

    def left(self):
        self.update_head_orientation()
        # If current heading is pointing to EAST, it's not allowed to go to WEST
        if self.head_orientation != EAST:
            self.snake_head.setheading(WEST)

    def right(self):
        self.update_head_orientation()
        # If current heading is pointing to WEST, it's not allowed to go to EAST
        if self.head_orientation != WEST:
            self.snake_head.setheading(EAST)

    def up(self):
        self.update_head_orientation()
        # If current heading is pointing to SOUTH, it's not allowed to go to NORTH
        if self.head_orientation != SOUTH:
            self.snake_head.setheading(NORTH)

    def down(self):
        self.update_head_orientation()
        # If current heading is pointing to NORTH, it's not allowed to go to SOUTH
        if self.head_orientation != NORTH:
            self.snake_head.setheading(SOUTH)

    def update_head_orientation(self):
        self.head_orientation = self.snake_head.heading()
