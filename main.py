from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time


screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor('black')
screen.title('My snake game')
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(snake.up, 'Up')
screen.onkey(snake.down, 'Down')
screen.onkey(snake.left, 'Left')
screen.onkey(snake.right, 'Right')


game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    # detect collision with food
    if snake.snake_head.distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.increase_score()

    # detect collision with wall
    if snake.snake_head.xcor() > 280 or snake.snake_head.xcor() < -280 or snake.snake_head.ycor() > 280 or \
            snake.snake_head.ycor() < -280:
        scoreboard.reset()
        snake.reset()

    # detect when snake collides with own tail
    for segment in snake.segments[1:]:  # skip the first segment as this is the head itself

        if snake.snake_head.distance(segment) < 10:
            scoreboard.reset()
            snake.reset()





























# screen = Screen()
# screen.setup(width=600, height=600)
# screen.bgcolor('black')
# screen.title('My snake game')
# screen.tracer(0)
#
# # create a snake body (3 squares)
#
# starting_positions = [(0, 0), (-20, 0), (-40, 0)]
#
# segments = []
#
# for position in starting_positions:
#     new_segment = Turtle("square")
#     new_segment.color("white")
#     new_segment.penup()
#     new_segment.goto(position)
#     segments.append(new_segment)
#
#
# game_is_on = True
#
# while game_is_on:
#     time.sleep(0.1)
#     screen.update()
#
#     for seg_num in range(len(segments)-1, 0, -1): #start, #stop, #skip
#         new_x = segments[seg_num - 1].xcor()
#         new_y = segments[seg_num - 1].ycor()
#         segments[seg_num].goto(new_x, new_y)
#
#     segments[0].forward(20)
#     segments[0].left(90)
#
#
# screen.exitonclick()























screen.exitonclick()