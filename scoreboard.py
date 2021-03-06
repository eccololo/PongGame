from turtle import Turtle


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.r_score = 0
        self.l_score = 0
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(150, 200)
        self.write(self.r_score, align="center", font=("Verdana", 45, "normal"))
        self.goto(-150, 200)
        self.write(self.l_score, align="center", font=("Verdana", 45, "normal"))

    def l_score_point(self):
        """This method updated left player score and displays it on screen."""
        self.l_score += 1
        self.update_score()

    def r_score_point(self):
        """This method updated right player score and displays it on screen."""
        self.r_score += 1
        self.update_score()

    def update_score(self):
        """This method updates score on the screen."""
        self.clear()
        self.goto(150, 200)
        self.write(self.r_score, align="center", font=("Verdana", 45, "normal"))
        self.goto(-150, 200)
        self.write(self.l_score, align="center", font=("Verdana", 45, "normal"))

    def end_game(self):
        """This method check if right or left player scored 5 points and prints Game Over on the screen."""
        if self.l_score >= 5:
            self.clear()
            self.goto(0, 0)
            self.write("Game Over.\nComputer Wins!", align="center", font=("Verdana", 55, "normal"))
        elif self.r_score >= 5:
            self.clear()
            self.goto(0, 0)
            self.write("Game Over.\nYou Win!", align="center", font=("Verdana", 55, "normal"))