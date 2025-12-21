from turtle import Turtle, Screen

screen = Screen()
screen.setup(width=700,height=550)
screen.bgcolor("black")
screen.title("Snake Game")


class Snake:
    pass
middle=Snake()
front =Snake()
back =Snake()

#Middle square-part (turtle) of the snake
middle.turtle = Turtle("square")
middle.turtle.color("white")
middle.turtle.goto(0,0)

#Front square-part (turtle) of the snake
front.turtle = Turtle("square")
front.turtle.color("white")
front.turtle.goto(x=-20,y=0)

#Back square-part (turtle) of the snake
back.turtle = Turtle("square")
back.turtle.color("white")
back.turtle.goto(x=20,y=0)



screen.exitonclick()