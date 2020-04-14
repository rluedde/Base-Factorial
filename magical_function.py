# function produces some magical outputs based on what USER wants!
import random
import time


def magicalize():
    magic_me = input("Hey user, what word do you want to see MAGICALIZED? ")
    times_to_magic = random.randint(1, 10)
    newlines = random.randint(1,3) * "\n"
    for i in range(0, times_to_magic):
        before_spaces = random.randint(0,25) * " "
        after_spaces = random.randint(0,25) * " "
        print(before_spaces + "*" + magic_me + "*" + after_spaces + newlines)

