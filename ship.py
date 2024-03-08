from turtle import Turtle

MOVE_DISTANCE = 20

UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0
BULLET_MOVE_Y = 10


# default turtle is 20 px
class Ship(Turtle):
    def __init__(self, shape="square"):
        super().__init__()
        self.shape(shape)
        self.shapesize(stretch_len=5, stretch_wid=1)
        self.color("white")
        self.setheading(LEFT)
        self.penup()
        self.goto(0, -260)

    def move(self):
        self.forward(MOVE_DISTANCE)

    def move_left(self):
        self.setheading(LEFT)
        if self.xcor() > -345:
            self.move()

    def move_right(self):
        self.setheading(RIGHT)
        if self.xcor() < 345:
            self.move()

    def create_bullet(self):
        bullet = Turtle()
        bullet.penup()
        bullet.shape("circle")
        bullet.color("red")
        bullet.setheading(UP)
        bullet.goto(self.position())

    def bullet_move(self):
        self.bullet.foward(10)

        # for _ in range(20):
        #     bullet.forward(BULLET_MOVE_Y)
        #     # self.screen.update()
