"""
Author:     Jared Malooly
Purpose:    Convert a base 10 int to base factorial. That is, such that
                19(base 10)      =    3*3! + 0*2! + 1*1!
"""

def find_factorial(b):
    """
    Returns the factorial of a given integer b
        ex:   4! = 4*3*2*1 = 24
    """
    if b <= 1:
        return b
    return b * find_factorial(b - 1)

def find_highest_fact(n, factorial = 1):
    """
    Returns the highest possible integer to factorialize (is this a word?)
    such that the the integer! <= number n
    """
    if find_factorial(factorial) <= n:
       return find_highest_fact(n, factorial + 1)
    else:
        return factorial - 1

def base_factorial(number, highest, negative, count=0):
    """
    Returns a given int (in base 10) in base factorial

    number:     Base 10 int to convert
    highest:    Highest possible factorialization such that
                highest! <= number
    negative:   String "+" or "-"
                note:   -21     =      -3*3! - 1*2! - 1*1!
                         21     =       3*3! + 1*2! + 1*1!
    count:      Keeps track of amount of times recursed
    """

    if highest == 0:
        return ""

    #
    if find_factorial(highest) > number:
        return str(count) + "*" + str(highest) + "! " + negative + \
            base_factorial(number, highest - 1, negative)

    else:
        number -= find_factorial(highest)
        return base_factorial(number, highest, negative, count + 1)

def format_result(number_in):
    """
    Performs two functions:
    1. catches edge cases like 0 and negative numbers
    2. prints the correct format
    """
    if number_in == 0:
        print(f"The Base Factorial expression of {number_in} is 0")
        return

    if number_in > 0:
        str_out = base_factorial(number_in, find_highest_fact(number_in), "+ ").rstrip("+ ")
        print(f"The Base Factorial expression of {number_in} is {str_out}")
        return

    if number_in < 0:
        number_in *= -1
        str_out = base_factorial(number_in, find_highest_fact(number_in), "- ").rstrip("- ")
        print(f"The Base Factorial expression of {number_in * -1} is -{str_out}")
        return

def main():
    number_in = int(input("Decimal number to convert: "))
    format_result(number_in)

main()
