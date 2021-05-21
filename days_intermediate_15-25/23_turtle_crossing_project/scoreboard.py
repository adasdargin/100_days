from turtle import Turtle
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.goto(-295, 270)
        self.level = 0
        self.increase_level()

    def increase_level(self):
        self.clear()
        self.level += 1
        self.write(f"Level: {self.level}", align="left", font=FONT)

    def write_game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", align="center", font=FONT)

