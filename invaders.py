from turtle import Turtle


class Invader(Turtle):
    def __init__(self, shape):
        super().__init__()
        self.hideturtle()
        self.num_invaders = 10
        self.invaders = []

    def create_invaders(self, shape: str, x_position: int, y_position: int):
        x_position = -345
        for invader in range(self.num_invaders):
            invader = Turtle()
            invader.penup()
            invader.shape(shape)
            invader.showturtle()
            invader.goto(x_position, y_position)
            self.invaders.append(invader)
            x_position += 75

    def remove_invader(self, obj):
        obj.goto(-1000, -1000)
