from turtle import Turtle
import random

COLORS = ["cornflowerBlue", "aquamarine" , "teal", "medium violet red", "dark orchid", "dark red", "yellow", "red" , "blue" , "green" ]

class Food(Turtle):
    def __init__(self):
        super().__init__()

        self.shape("circle")
        self.penup()
        self.color(random.choice(COLORS))
        self.shapesize(stretch_wid=0.5, stretch_len=0.5)
        self.speed("fastest")
        self.refresh()

    def refresh(self):
        random_x = random.randint(-280, 280)
        random_y = random.randint(-280, 280)
        self.color(random.choice(COLORS))
        self.goto(random_x, random_y)
