from turtle import Screen
import time
from snake import Snake
from food import Food
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600,height=600) # Screen is 300x300 pixels so calculate the positions according to this.
screen.bgcolor("black")
screen.tracer(0) #This method turns off the animation and only call the animation back when we use turtle.update() method - until the works will be done in the background and will not be shown to the human eyes. So it would be looks like a continuous block of motion (resembling a snake's motion) instead of three separate block of motion.
screen.title("Snake Game")

snake = Snake()
food = Food()
scoreboard =Scoreboard()

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


    if snake.head.distance(food) <15:  #If the distance between the head part of the snake and the food becomes less than 10px it will be considered to be collided and change the food to different random position.
        food.refresh()
        snake.extend()
        scoreboard.increase_score()

    # Standard coordinates 280 in all direction but according to my need I'm adjusting it.
    if snake.head.xcor()>280 or snake.head.xcor()<-300 or snake.head.ycor()>285 or snake.head.ycor()<-280:
        game_is_on=False
        scoreboard.game_over()

    #Detecting collision with its own tail. IF HEAD COLLIDIES WITH ANY OF THE TAIL then the game over.

    for segment in snake.segments[1:]:
        if snake.head.distance(segment)<15:
            game_is_on =False
            scoreboard.game_over()


screen.exitonclick()