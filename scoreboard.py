from turtle import Turtle

ALIGNMENT = 'CENTER'
FONT = ('Consolas', 20, 'normal')


class Scoreboard(Turtle):

    def __init__(self) -> None:
        super().__init__()
        self.score = 0
        self.data = open('data.txt', 'r')
        self.highest_score = int(self.data.read())
        self.data.close()
        self.goto(x=0, y=250)
        self.penup()
        self.color('spring green')
        self.hideturtle()
        self.speed('fastest')
        self.update()

    def update(self):
        self.clear()
        self.write(f'Score: {self.score} Highest score: {self.highest_score}', False, ALIGNMENT, FONT)

    def reset_data(self):
        self.data = open(file='data.txt', mode='w')
        self.data.write(str(0))
        self.data.close()
        self.highest_score = 0
        self.update()

    def increase_score(self):
        self.score += 1
        self.update()

    def game_over(self):
        self.clear()
        self.goto(x=0, y=0)
        self.write('Game over.', False, ALIGNMENT, FONT)
        self.sety(self.ycor() - 30)
        self.write(f'Score: {self.score}', False, ALIGNMENT, FONT)
        if self.score > self.highest_score:
            self.data = open(file='data.txt', mode='w')
            self.data.write(str(self.score))
            self.data.close()
