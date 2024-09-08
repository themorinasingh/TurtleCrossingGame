from turtle import Turtle
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.goto(-230,270)
        self.level = 0
        self.color("black")
        self.message_display()

    def message_display(self):
        self.clear()
        self.level += 1
        self.write(arg="Level: " + str(self.level), move=False, font =FONT, align="center")

    def game_over_sequence(self):
        self.goto(0,0)
        self.write(arg="GAME OVER", move=False, font=("Courier", 42, "normal"), align="center")

