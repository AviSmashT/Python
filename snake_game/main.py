from turtle import Screen
import time
from snake import Snake
from food import Food
from score import Score

LIMIT = 300  # Window borders
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")  # Background color
screen.title("Snake")  # Window title
screen.tracer(0)  # Tracer - 0 => freeze the screen, to unfreeze use "screen.update()"

# Initialize objects:
snake = Snake()  # Snake
food = Food()  # Food items to collect
scoreboard = Score()  # Write on screen - Score and Game over

# Key binding:
screen.listen()
screen.onkey(key="Up", fun=snake.up)
screen.onkey(key="Down", fun=snake.down)
screen.onkey(key="Left", fun=snake.left)
screen.onkey(key="Right", fun=snake.right)


game_is_on = True  # Bool true id game is on
while game_is_on:
    screen.update()  # unfreeze screen
    time.sleep(0.1)  # 0.1 sec delay
    # moving the head of the snake:
    snake.move()

    # food collision:
    if food.distance(snake.head) <= 15:  # if snake head distance from food is about 15:
        food.refresh()  # new food item
        snake.increase_size()  # Snake increase in size
        scoreboard.increase_score()  # increase score

    # wall collision:
    if snake.head.position()[0] >= LIMIT or snake.head.position()[0] <= -LIMIT-5 or snake.head.position()[1] >= LIMIT+5 or snake.head.position()[1] <= -LIMIT:
        scoreboard.game_over()
        game_is_on = False

    # tail collision:
    # for segment in snake.segments:  # if snake head collides with any of snake segments
    #     if snake.head == segment:  # don't check distance with head segment
    #         pass
    #     elif snake.head.distance(segment) < 10:
    #         scoreboard.game_over()
    #         game_is_on = False
    # for i in range(5, len(snake.segments)):
    #     if snake.head.distance(snake.segments[i]) <= 20:
    #         scoreboard.game_over()
    #         game_is_on = False
    # tail collision:
    for segment in snake.segments[3:]:  # if snake head collides with any of snake segments (exclude the first 3 segments)
        if snake.head.distance(segment) < 10:
            scoreboard.game_over()
            game_is_on = False


screen.exitonclick()
