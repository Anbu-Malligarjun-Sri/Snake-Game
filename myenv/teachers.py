from turtle import Turtle, Screen
import time
from snake import Snake

screen = Screen()
screen.setup(width=700,height=550)
screen.bgcolor("black")
screen.tracer(0) #This method turns off the animation and only call the animation back when we use turtle.update() method - until the works will be done in the background and will not be shown to the human eyes. So it would be looks like a continuous block of motion (resembling a snake's motion) instead of three separate block of motion.
screen.title("Snake Game")

snake = Snake()

screen.listen()
screen.onkey(snake.up,"Up")
screen.onkey(snake.down,"Down")
screen.onkey(snake.right,"Right")
screen.onkey(snake.left,"Left")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.start_game()



screen.exitonclick()