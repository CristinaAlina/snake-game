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
            self.add_body_snake(True)
        self.snake_head = self.body_snake[0]
        self.head_orientation = self.snake_head.heading()

    def add_body_snake(self, is_start_of_the_game):
        """Create the snake if is_start_of_the_game = True or
        add a new square to the snake body if start_of_the_game = False"""
        new_square = Turtle("square")
        new_square.penup()
        new_square.pensize(20)
        new_square.color("DarkGreen", "DarkGreen")
        self.body_snake.append(new_square)
        if is_start_of_the_game:
            # for each new square added in the list, we need to positioned it starting with 0,
            # by -MOVE_DISTANCE on x-axis
            # according to its index from the list, format a continue line of squares, one by one
            new_square.goto((-MOVE_DISTANCE * self.body_snake.index(new_square)), 0)
        else:
            self.move()

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

    def verify_collision_tail(self):
        """Returns True if a collision with the snake tail is detected, or False otherwise"""
        for square in self.body_snake[1:]:
            if self.snake_head.distance(square.position()) < 2:
                return True
        return False

    def reset_snake(self):
        for square in self.body_snake:
            square.hideturtle()
        self.body_snake = []
        # create the starting shape of snake with 3 squares
        for index_square in range(3):
            self.add_body_snake(True)
        self.snake_head = self.body_snake[0]
        self.head_orientation = self.snake_head.heading()
