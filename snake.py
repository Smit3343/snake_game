from turtle import Turtle

STARTING_POSITION = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:
    def __init__(self):
        self.segment_list = []
        self.create_snake()
        self.head_segment = self.segment_list[0]

    def create_snake(self):
        for pos in STARTING_POSITION:
            self.add_segment(pos)

    def add_segment(self, position):
        new_segment = Turtle('square')
        new_segment.penup()
        new_segment.color('white')
        new_segment.goto(position)
        self.segment_list.append(new_segment)

    def extend(self):
        self.add_segment(self.segment_list[-1].position())

    def move(self):
        for i in range(len(self.segment_list) - 1, 0, -1):
            segment_pos = self.segment_list[i - 1].position()
            self.segment_list[i].goto(segment_pos)

        self.segment_list[0].forward(MOVE_DISTANCE)

    def up(self):
        if self.head_segment.heading() != DOWN:
            self.head_segment.setheading(UP)

    def down(self):
        if self.head_segment.heading() != UP:
            self.head_segment.setheading(DOWN)

    def left(self):
        if self.head_segment.heading() != RIGHT:
            self.head_segment.setheading(LEFT)

    def right(self):
        if self.head_segment.heading() != LEFT:
            self.head_segment.setheading(RIGHT)
