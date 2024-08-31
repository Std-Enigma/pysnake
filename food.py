from turtle import Turtle
from random import randint


class Food(Turtle):

    def __init__(self) -> None:
        super().__init__()
        self.speed('fastest')
        self.penup()
        self.shape('circle')
        self.shapesize(stretch_wid=0.5, stretch_len=0.5)
        self.color('red')
        self.refresh()

    def refresh(self):
        self.goto(x=randint(-280, 280), y=randint(-280, 280))
