from turtle import Turtle
import random


class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_wid=0.5, stretch_len=0.5)
        self.color("blue")
        self.create_food()

    def create_food(self):
        x = random.randint(-290, 290)
        y = random.randint(-290, 290)
        self.setpos(x, y)

