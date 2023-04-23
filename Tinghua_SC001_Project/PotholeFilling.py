"""
File: PotholeFilling.py
Name: Tinghua Chen
--------------------------
This program shows karel filling 3
potholes. Students learn the concept of
decomposition through the process.
"""

from karel.stanfordkarel import *


def main():
    for i in range(3):
        go_in()
        put_beeper()
        go_out()

def go_in():
    move()
    turn_right()
    move()
def go_out():
    turn_around()
    move()
    turn_right()
    move()
def turn_right():
    turn_left()
    turn_left()
    turn_left()
def turn_around():
    turn_right()
    turn_right()

    pass


# ----- DO NOT EDIT CODE BELOW THIS LINE ----- #
if __name__ == '__main__':
    execute_karel_task(main)
