from turtle import Turtle

STARTING_POSITION = [(0, 0), (-20, 0), (-40, 0)]
MOVING_POSITION = 20

#GOlDEN standards of Snake GAME
UP   = 90  #NORTH
DOWN = 270 #SOUTH
LEFT = 180 #EAST
RIGHT= 0   #WEST

class Snake:


    def __init__(self):
       self.segments=[] #[0,1,2]
       self.create_snake()
       self.head = self.segments[0]

    def create_snake(self):
        for position in STARTING_POSITION:
            new_segment = Turtle("square")
            new_segment.penup()
            new_segment.color("white")
            new_segment.goto(position)
            self.segments.append(new_segment)

    def start_game(self):
        for seg_num in range(len(self.segments) - 1, 0,-1):  # range(start,stop,step)  --> start- where to start we want our 3rd segment to reach to 2nd segment and then the second segment to reach the first segment to get a continuous motion. Here 3rd segment is 2 becuase list counts from 0. stop - where to stop (order we want - 3,2,1 so according to list it is 2,1,0) , step = how to reach the final step (either by adding 1 (forward iteration) or subtracting 1 (reverse iteration)
            # SO it will be start = 3(length of segments) -1 =2 , stop = 0 , step = -1 (iterate in reverse order). -> Final order =[2, 1, 0]

            # we want each segment to follow the previous segment
            new_x = self.segments[seg_num - 1].xcor()  # So, we take the x & y cor of the previous segments (3rd segment takes the position of 2nd segment)
            new_y = self.segments[seg_num - 1].ycor()  # And so, 3rd segment's next step will follow the 2nd segment and so does the 2nd follows 1st segment.
            self.segments[seg_num].goto(new_x, new_y)  # Hence, if first segment turns left, every other segment follows, and so it makes the motion of a snake

        self.head.forward(MOVING_POSITION)


#Direction control - Universal logic for Snake game
    def up(self):
        if self.head.heading()!=DOWN:
           self.head.setheading(UP)
    def down(self):
        if self.head.heading()!=UP:
            self.head.setheading(DOWN)
    def left(self):
        if self.head.heading()!=RIGHT:
            self.head.setheading(LEFT)
    def right(self):
        if self.head.heading()!=LEFT:
            self.head.setheading(RIGHT)