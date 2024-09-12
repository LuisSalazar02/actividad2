"""Snake, classic arcade game.

Exercises

1. How do you make the snake faster or slower?
2. How can you make the snake go around the edges?
3. How would you move the food?
4. Change the snake to respond to mouse clicks.
"""

from random import randrange
from turtle import *

from freegames import square, vector

food = vector(0, 0)
snake = [vector(10, 0)]
aim = vector(0, -10)
window_height = 420
window_width = 420

def move_food():
    """Move food to an adjacent contiguous grid cell."""
    while True:
        # Generate random dx and dy from [-10, 10] for contiguous cell movement
        dx = randrange(-10, 11, 10)
        dy = randrange(-10, 11, 10)

        # Ensure dx and dy are not both zero
        if dx == 0 and dy == 0:
            continue

        # Calculate new food position
        new_x = food.x + dx
        new_y = food.y + dy

        # Ensure the new position is within window boundaries
        if 0 <= new_x < window_width and 0 <= new_y < window_height:
            # Ensure new position does not overlap with snake
            if not any(segment.x == new_x and segment.y == new_y for segment in snake):
                food.x, food.y = new_x, new_y
                break

def defineColors():
    colorArray = ["black", "green", "blue", "orange", "pink"]
    randomNumber = randrange(0, len(colorArray))
    snakeColor = colorArray[randomNumber]
    colorArray.pop(randomNumber)
    randomNumber = randrange(0, len(colorArray))
    foodColor = colorArray[randomNumber]

    return snakeColor, foodColor

def change(x, y):
    """Change snake direction."""
    aim.x = x
    aim.y = y

def inside(head):
    """Return True if head inside boundaries."""
    return -200 < head.x < 190 and -200 < head.y < 190

def move():
    """Move snake forward one segment."""
    head = snake[-1].copy()
    head.move(aim)

    if not inside(head) or head in snake:
        square(head.x, head.y, 9, 'red')
        update()
        return

    snake.append(head)

    if head == food:
        print('Snake:', len(snake))
        move_food()  # Move the food to a new position
    else:
        snake.pop(0)

    clear()

    for body in snake:
        square(body.x, body.y, 9, snakeColor)

    square(food.x, food.y, 9, foodColor)
    update()
    ontimer(move, 100)

snakeColor, foodColor = defineColors()
setup(window_width, window_height, 370, 0)
hideturtle()
tracer(False)
listen()
onkey(lambda: change(10, 0), 'Right')
onkey(lambda: change(-10, 0), 'Left')
onkey(lambda: change(0, 10), 'Up')
onkey(lambda: change(0, -10), 'Down')
move()
done()
