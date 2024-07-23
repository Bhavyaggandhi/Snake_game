from turtle import Turtle

STARTING_POSITION=[(0,0),(-20,0),(-40,0)]

class Snake:

    def __init__(self):
        self.segment=[]
        self.create_snake()
        self.head=self.segment[0]

    def create_snake(self):
        for position in STARTING_POSITION:
            self.add_segment(position)

    def add_segment(self, position):
        new_segment=Turtle(shape="square")
        new_segment.color("white")
        new_segment.penup()
        new_segment.goto(position)
        self.segment.append(new_segment)

    def extend(self):
        self.add_segment(self.segment[-1].position())
        
    def move(self):
        for seg_num in range(len(self.segment)-1,0,-1):
            self.segment[seg_num].goto(self.segment[seg_num-1].xcor(),self.segment[seg_num-1].ycor())
        self.head.forward(20)

    def reset(self):
        for seg in self.segment:
            seg.goto((1000,1000))
        self.segment.clear()
        self.create_snake()
        self.head=self.segment[0]

    def up(self):
        if self.head.heading() !=270:
            self.head.setheading(90)

    def down(self):
        if self.head.heading() !=90:
            self.head.setheading(270)

    def left(self):
        if self.head.heading() !=0:
            self.head.setheading(180)

    def right(self):
        if self.head.heading() !=180:
            self.head.setheading(0)