"""
File: DoubleBeepers.py
Name:Tinghua Chen
-------------------------------
TODO:
"""

from karel.stanfordkarel import *


def main():
    move()
    double_beepers()
    move()
    turn_around()
    move_beeper()
    move()
    move()
    turn_around()
def double_beepers():
    while on_beeper():
        pick_beeper()
        move()
        put_beeper()
        put_beeper()
        turn_around()
        move()
        turn_around()
def turn_around():
    for i in range(2):
        turn_left()
def move_beeper():
    while on_beeper():
        pick_beeper()
        move()
        put_beeper()
        turn_around()
        move()
        turn_around()


    """
    Karel will double the beepers
    """
    pass


# ----- DO NOT MODIFY CODE BELOW THIS LINE ----- #
if __name__ == '__main__':
    execute_karel_task(main)
