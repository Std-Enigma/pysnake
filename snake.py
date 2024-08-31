import random
from cicc_colors import colors
from turtle import Turtle

STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 20)]
MOVE_DISTANCE = 20
NORTH = 90
SOUTH = 270
EAST = 0
WEST = 180


class Snake:

    def __init__(self) -> None:
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def __generate_random_color__(self) -> str:
        r = random.randint(0, 255)
        g = random.randint(0, 255)
        b = random.randint(0, 255)
        return colors.RGB2Hex(r, g, b, with_hash=True)

    def go_up(self):
        if self.segments[0].heading() != SOUTH:
            self.segments[0].setheading(NORTH)

    def go_down(self):
        if self.segments[0].heading() != NORTH:
            self.segments[0].setheading(SOUTH)

    def go_right(self):
        if self.segments[0].heading() != WEST:
            self.segments[0].setheading(EAST)

    def go_left(self):
        if self.segments[0].heading() != EAST:
            self.segments[0].setheading(WEST)

    def create_snake(self):
        for position in STARTING_POSITIONS:
            turtle = Turtle('square')
            turtle.color(self.__generate_random_color__())
            turtle.penup()
            turtle.goto(position)
            self.segments.append(turtle)

    def add_segment(self, position):
        turtle = Turtle('square')
        turtle.color(self.__generate_random_color__())
        turtle.penup()
        turtle.goto(position)
        self.segments.append(turtle)

    def extend(self):
        self.add_segment(self.segments[-1].position())

    def move(self):
        for index in range(len(self.segments) - 1, 0, -1):
            self.segments[index].goto(x=self.segments[index - 1].xcor(), y=self.segments[index - 1].ycor())
        self.segments[0].forward(MOVE_DISTANCE)
