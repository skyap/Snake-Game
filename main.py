from turtle import Screen
import time
from snake import Snake
from food import Food
from scoreboard import ScoreBoard
import tkinter as tk

screen = Screen()
screen.setup(width=600,height=600)
screen.bgcolor('black')
screen.title("Python Snake Online")
screen.tracer(0)


snake = Snake()
food = Food()
scoreboard = ScoreBoard()

screen.listen()
screen.onkey(snake.up,"Up")
screen.onkey(snake.down,"Down")
screen.onkey(snake.left,"Left")
screen.onkey(snake.right,"Right")

screen.onkey(screen.bye, "q")
game_started = False
start_button = None

def start_game():
    global game_started,start_button
    if not game_started:
        game_started = True
        start_button.destroy() 
        game_loop()

def game_loop():
    global game_started
    if not game_started:
        return

    screen.update()
    snake.move()

    # if abs(snake.head.xcor())>280 or abs(snake.head.ycor())>280:
    #     scoreboard.game_over()
    #     return

    if snake.head.xcor()>280:
        snake.head.goto(-280,snake.head.ycor())

    if snake.head.xcor()<-280:
        snake.head.goto(279,snake.head.ycor())

    if snake.head.ycor()>280:
        snake.head.goto(snake.head.xcor(),-279)

    if snake.head.ycor()<-280:
        snake.head.goto(snake.head.xcor(),279)       

    for segment in snake.segments[1:]:
        if snake.head.distance(segment)<10:
            scoreboard.game_over()
            return

    if snake.head.distance(food)< 15:
        food.refresh() 
        snake.extend()
        scoreboard.increase_score()
        
    screen.ontimer(game_loop,100)




game_loop()

canvas = screen.getcanvas()
root = canvas.winfo_toplevel()
start_button = tk.Button(root, text="Start Game", command=start_game)
canvas.create_window(0, 0, anchor=tk.NW, window=start_button)  # Adjust position as needed


screen.mainloop()

        
screen.exitonclick()