#
# Space Invaders Game
#
from turtle import Screen
from ship import Ship
from invaders import Invader
from scoreboard import Scoreboard
import time

SHIP_GIF = "./assets/icons/ship.gif"
INVADER_GIF = "./assets/icons/invader.gif"
UFO_GIF = "./assets/icons/ufo.gif"
BG_GIF = "./assets/background/black_night.gif"

screen = Screen()
screen.register_shape(SHIP_GIF)
screen.register_shape(INVADER_GIF)
screen.register_shape(UFO_GIF)

screen.setup(800, 800)
screen.bgpic(BG_GIF)
screen.title("Space Invaders")
screen.tracer(0)  # screen tracer

scoreboard = Scoreboard(y_position=0)

ship = Ship(SHIP_GIF)

invader = Invader(INVADER_GIF)
invader.create_invaders(INVADER_GIF, -200, 125)
invader.create_invaders(INVADER_GIF, 100, 180)
invader.create_invaders(INVADER_GIF, 200, 235)
invader.create_invaders(INVADER_GIF, 300, 290)

screen.listen()

screen.onkeypress(key="Left", fun=ship.move_left)
screen.onkeypress(key="Right", fun=ship.move_right)
screen.onkeypress(key="space", fun=ship.create_bullet)

game_is_on = True

while game_is_on:
    screen.update()

    # while (ship.bullet.ullet.xcor() < 300 and bullet.xcor() > -300) and (bullet.ycor() < 150 and bullet.ycor() > -150):
# 	#move bullet
# 	bullet.forward(10)
# print(ship.xcor())
# print(ship.ycor())
# print(bullet.xcor())
# print(bullet.ycor())

# time.sleep(ball.move_speed)  # increase the ball speed after each bounce
# ball.move()
# Wall collision
# if ball.ycor() > 280 or ball.ycor() < -280:  # ball width is 20px
#     ball.bounce_y()

# # Detect Collision paddles:
# if (
#     ball.xcor() > 320
#     and ball.distance(r_paddle) < 50
#     or ball.xcor() < -320
#     and ball.distance(l_paddle) < 50
# ):
#     ball.bounce_x()

# # Detect Ball out of bounds right paddle
# if ball.xcor() > 380:
#     ball.ball_reset()
#     l_scoreboard.increase_score()

# # Detect Ball out of bounds left paddle
# if ball.xcor() < -380:
#     ball.ball_reset()
#     r_scoreboard.increase_score()


screen.exitonclick()
