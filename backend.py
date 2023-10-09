import turtle

def canvas_builder(title, canvas_width, canvas_height, square_length):
    # CANVAS_COLOR = "red"
    # PEN_COLOR = "black"
    # scr = turtle.Screen()
    # scr.screensize(canvas_width, canvas_height)
    # scr.title(title)
    # scr.bgcolor(CANVAS_COLOR)
    # turtle.setworldcoordinates(0, 0, canvas_width, canvas_height)
    # t = turtle.Turtle()
    # t.color(PEN_COLOR)
    # t.begin_fill()
    # for i in range(4):
    #     t.forward(square_length)
    #     t.left(90)
    # t.end_fill()
    # turtle.done()
    from turtle import Screen
    import time
    from snake import Snake
    from food import Food
    from scoreboard import ScoreBoard

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

    game_is_on = True

    def game_loop():
        screen.update()
        snake.move()

        if abs(snake.head.xcor())>280 or abs(snake.head.ycor())>280:
            scoreboard.game_over()
            return

        for segment in snake.segments[1:]:
            if snake.head.distance(segment)<10:
                scoreboard.game_over()
                return

        if snake.head.distance(food)< 15:
            food.refresh() 
            snake.extend()
            scoreboard.increase_score()
            
        screen.ontimer(game_loop,100)



    # while game_is_on:
    #     screen.update()
    #     time.sleep(0.1)
    #     snake.move()
    #     if snake.head.distance(food)< 15:
    #         food.refresh()

    game_loop()

    screen.mainloop()

            
    screen.exitonclick()