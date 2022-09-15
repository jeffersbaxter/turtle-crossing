from turtle import Turtle

START_POSITION = (0, -275)
MOVE = 10
FINISH_LINE_Y = 300


class Player(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.color("black")
        self.penup()
        self.setheading(90)
        self.reset_pos()

    def move(self):
        self.forward(MOVE)

    def is_at_finish_line(self):
        return self.ycor() > FINISH_LINE_Y

    def reset_pos(self):
        self.goto(START_POSITION)
