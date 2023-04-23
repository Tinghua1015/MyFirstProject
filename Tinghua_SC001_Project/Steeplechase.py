"""
File: Steeplechase.py
Name: Tinghua Chen
---------------------------------
TODO:
"""

from karel.stanfordkarel import *


def main():
    for i in range(7):
        while front_is_clear():
            move()
        up()
        move()
        down()


def up():
    turn_left()
    while not right_is_clear():
        move()
    turn_right()


def turn_right():
    for i in range(3):
        turn_left()
def down():
    while right_is_clear():
        turn_right()
        move()
        turn_left()






    pass


# ----- DO NOT MODIFY CODE BELOW THIS LINE ----- #
if __name__ == '__main__':
    execute_karel_task(main)
