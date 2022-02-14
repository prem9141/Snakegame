from turtle import Turtle

MOVE = False
ALIGN = "center"
FONT = ('Courier', 15, 'bold')


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.hideturtle()
        self.penup()
        self.setpos(0, 270)
        self.display_score()

    def display_score(self):
        self.clear()
        self.write(f"Score: {self.score}", MOVE, ALIGN, FONT)

    def update_score(self):
        self.score += 1

    def game_over(self):
        self.home()
        self.write("GAME OVER", MOVE, ALIGN, FONT)
