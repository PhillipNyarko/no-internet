import os
import time
from pynput import keyboard

# global vars
clock_speed = 0.1
score = 0
game_space = [[] for i in range(3)]

def on_press(key):
    if key == keyboard.Key.esc:
        return False  # stop listener
    try:
        k = key.char  # single-char keys
    except:
        k = key.name  # other keys
    if k in ['1', '2', 'left', 'right']:  # keys of interest
        # self.keys.append(k)  # store it in global-like variable
        print('Key pressed: ' + k)
        return False  # stop listener; remove this if want more keys


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

    listener = keyboard.Listener(on_press=on_press)
    listener.start()  # start to listen on a separate thread
    listener.join()  # remove if main thread is polling self.keys

