from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import ScoreBoard
import time
scoreboard=ScoreBoard()
screen=Screen()
screen.tracer(0)
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")

snake=Snake()
food=Food()
screen.listen()


screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")


game_is_on=True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()
#detect collision
    if snake.head.distance(food)<15:
        food.refresh()
        snake.extent()
        scoreboard.increase_score()
        #detect collision with wall
    if snake.head.xcor()>280 or snake.head.xcor()<-290 or snake.head.ycor()>280 or snake.head.ycor()<-290:
        scoreboard.reset()
        snake.reset()
        # game_is_on=False
        # scoreboard.game_over()
    # detect collision with tail.
    for segment in snake.segments[1:]:
        if snake.head.distance(segment)<10:
            scoreboard.reset()
            snake.reset()
            # game_is_on=False
            # scoreboard.game_over()
    #if head collides with any segment in the tail:

screen.exitonclick()
