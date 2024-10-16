import os
import time

# global vars
clock_speed = 0.1
score = 0
game_space = [[] for i in range(3)]

def reset_game_space():

    game_space[0] = [" " for i in range(25)]
    game_space[1] = [" " for i in range(25)]
    game_space[2] = ["_" for i in range(25)] 

    game_space[0][24] = str(score)
def update_game_space():
    pass

def draw_game_space():
    for i in game_space:
        print("".join(i))

def clear_screen():
    os.system('clear')

# game loop
running = True

while running:
    reset_game_space()
    draw_game_space()

    # set constant framerate
    time.sleep(clock_speed)

    clear_screen()

