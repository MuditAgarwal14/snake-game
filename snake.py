import turtle
from turtle import Turtle
import random

POSITION = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0
COLORS = ['red', 'white', 'blue', 'yellow', 'pink', 'green', 'orange', 'gold', 'purple', 'chocolate', 'skyblue', 'cyan']

user_color = turtle.numinput(prompt="What is the color of the snake? Type: 0 for white or 1 for colorful",
                             title="Chose color")
user_shape = turtle.numinput(prompt="What is the shape of the snake? Type: 0 for square or 1 for circle",
                             title="Chose shape")


class Snake:

    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        for position in POSITION:
            self.add_segment(position)

    def add_segment(self, position):
        if user_shape == 1:
            new_turtle = Turtle(shape='circle')
        else:
            new_turtle = Turtle(shape='square')

        if user_color == 1:
            new_turtle.color(random.choice(COLORS))
        else:
            new_turtle.color('white')

        new_turtle.penup()
        new_turtle.goto(position)
        self.segments.append(new_turtle)

    def extend(self):
        self.add_segment(self.segments[-1].position())

    def move(self):
        for seg in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg - 1].xcor()
            new_y = self.segments[seg - 1].ycor()
            self.segments[seg].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)
