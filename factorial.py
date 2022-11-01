#!/usr/bin/env python3

# Created By: Kestrel Bryce
# Date: Oct. 26, 2022
# This program asks for a number
# and shows all the steps leading up to
# the factorial as well as the number's
# factorial itself

import math


def main():
    # introductory paragraph
    print("This program asks for a number")
    print("and shows all the steps leading up to")
    print("the factorial as well as the number's")
    print("factorial itself")
    print("")

    # input
    # getting user_num_string
    user_num_string = input("Enter a positive number: ")

    # initializing counter
    counter = 1

    # initializing factorial_num
    factorial_num = 1

    # process
    # checking that user_num_string is an integer
    try:
        user_num_int = int(user_num_string)
    except ValueError:
        print("\n")
        print(("Please enter a positive number."))
    finally:
        print("")

        # checking that user_num_int is positive
        if user_num_int <= 0:
            print("Please enter a positive number.")

        # output
        while counter <= user_num_int:
            # updating factorial_num
            factorial_num = factorial_num * counter
            # printing the numbers
            print(("{}").format(factorial_num))
            # incrementing counter
            counter = counter + 1
        else:
            print(("The factorial is {}").format(factorial_num))


if __name__ == "__main__":
    main()
