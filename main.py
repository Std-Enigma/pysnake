from turtle import Screen
from time import sleep
from snake import Snake
from food import Food
from scoreboard import Scoreboard

is_game_over = False
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600
GAME_TITLE = 'Snake'
BACKGROUND_COLOR = 'black'

screen = Screen()
screen.setup(width=SCREEN_WIDTH, height=SCREEN_HEIGHT)
screen.bgcolor(BACKGROUND_COLOR)
screen.title(GAME_TITLE)
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(fun=snake.go_up, key='Up')
screen.onkey(fun=snake.go_down, key='Down')
screen.onkey(fun=snake.go_right, key='Right')
screen.onkey(fun=snake.go_left, key='Left')
screen.onkey(fun=scoreboard.reset_data, key='r')


def is_collided_with_food() -> bool:
    if snake.head.distance(food) > 15:
        return False
    return True


def is_collided_with_wall() -> bool:
    if abs(snake.head.xcor()) <= SCREEN_HEIGHT / 2 - 10 and abs(snake.head.ycor()) <= SCREEN_WIDTH / 2 - 10:
        return False
    return True


def is_collided_with_tale() -> bool:
    for segment in snake.segments[1:len(snake.segments)]:
        if snake.head.distance(segment) < 10:
            return True


while not is_game_over:
    screen.update()
    sleep(0.1)
    snake.move()
    if is_collided_with_food():
        scoreboard.increase_score()
        snake.extend()
        food.refresh()
    elif is_collided_with_wall() or is_collided_with_tale():
        is_game_over = True
        scoreboard.game_over()

screen.exitonclick()
