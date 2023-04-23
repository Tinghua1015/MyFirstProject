"""
File: BeeperRowAdv.py
Name:Tinghua Chen
------------------------------
This program makes Karel fill up
Street 1 with some beepers already
existed
(This should be world insensitive)
"""

from karel.stanfordkarel import *



def main():
    for i in range(11):
        if not on_beeper():
            put_beeper()
        else:
            move()









####### DO NOT EDIT CODE BELOW THIS LINE ########

if __name__ == '__main__':
    execute_karel_task(main)