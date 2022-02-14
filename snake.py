from turtle import Turtle

INITIAL_POSITION = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP_ANGLE = 90
DOWN_ANGLE = 270
LEFT_ANGLE = 180
RIGHT_ANGLE = 0


class Snake:
    def __init__(self):
        self.squares = []
        self.create_snake()
        self.head = self.squares[0]

    def create_snake(self):
        for position in INITIAL_POSITION:
            self.add_snake(position)

    def add_snake(self, position):
        square = Turtle("square")
        square.color("white")
        square.penup()
        square.setpos(position)
        self.squares.append(square)

    def extend(self):
        self.add_snake(self.squares[-1].position())

    def move(self):
        for square_pos in range(len(self.squares) - 1, 0, -1):
            x, y = self.squares[square_pos - 1].position()
            self.squares[square_pos].setpos(x, y)
        self.head.forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != DOWN_ANGLE:
            self.head.setheading(UP_ANGLE)

    def down(self):
        if self.head.heading() != UP_ANGLE:
            self.head.setheading(DOWN_ANGLE)

    def left(self):
        if self.head.heading() != RIGHT_ANGLE:
            self.head.setheading(LEFT_ANGLE)

    def right(self):
        if self.head.heading() != LEFT_ANGLE:
            self.head.setheading(RIGHT_ANGLE)
