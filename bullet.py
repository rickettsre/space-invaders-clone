from turtle import Turtle

MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Bullet(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("square")
        self.x_move = 0
        self.y_move = 10
        self.move_speed = 1
        self.shapesize(stretch_len=0.6, stretch_wid=0.4)
        self.color("red")
        self.setheading(UP)
        self.penup()
        self.goto(0, -260)

    def fire(self):
        # new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(0, new_y)

    def bounce_x(self):
        self.x_move *= -1
        self.move_speed *= 0.9

    def ball_reset(self):
        self.goto(0, 0)
        self.move_speed = 0.1
        self.bounce_x()
