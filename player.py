from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.shape('images/turtle.gif')
        self.goto(STARTING_POSITION)

    def go_up(self):
        self.setheading(90)
        self.forward(MOVE_DISTANCE)

    def go_down(self):
        self.setheading(270)
        self.forward(MOVE_DISTANCE)

    def is_finish(self, y):
        if FINISH_LINE_Y == y:
            self.goto(STARTING_POSITION)
            return True
        return False
