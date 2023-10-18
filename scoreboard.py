from turtle import Turtle

FONT = ("Verdana", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.level = 0
        self.level_up()

    def level_up(self):
        self.clear()
        self.level += 1
        self.setposition(-280, 260)
        self.write(f'Level: {self.level}', align='left', font=FONT)

    def game_over(self):
        self.setposition(0, 0)
        self.write('Game Over', align='center', font=FONT)
