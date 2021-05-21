import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.listen()

player = Player()
screen.onkey(player.move, "Up")

car_manager = CarManager()
score_board = Scoreboard()

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    car_manager.create_car()
    car_manager.move_cars()

    #detect collision with a car:
    for car in car_manager.all_cars:
        if car.distance(player) < 20:
            score_board.write_game_over()
            game_is_on = False

    #detect finish_line:
    if player.is_at_finish_line():
        score_board.increase_level()
        player.go_to_start()
        car_manager.increase_speed()

screen.exitonclick()
