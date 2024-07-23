from turtle import Turtle

class scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.score=0
        try:
            with open("data.txt", "r") as data:
                content = data.read()
                if content.strip():
                    self.high_score = int(content)
                else:
                    self.high_score = 0
        except (FileNotFoundError, ValueError):
            self.high_score = 0
        self.penup()
        self.goto(0,270)
        self.write(f"Score : {self.score} High Score : {self.high_score}", True, align="center", font=("Courier New", 15, "normal"))
        self.hideturtle()
        
    def score_update(self):
        self.clear()
        self.goto(0,270)
        self.write(f"Score: {self.score} High Score: {self.high_score}", align="center", font=("Courier New", 15, "normal"))

    def increase_score(self):
        self.score += 1
        self.score_update()

    def reset(self):
        if self.high_score < self.score:
            self.high_score = self.score
            with open("data.txt", mode="w") as data:
                data.write(f"{self.high_score}")
        self.score = 0
        self.score_update()