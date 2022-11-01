#!/usr/bin/env python3

# Created By: Kestrel Bryce
# Date: Oct. 31, 2022
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
    else:
        print("")

        # output
        while True:
            #while counter <= user_num_int:
            # updating factorial_num
            factorial_num = factorial_num * counter
            # printing the numbers
            print(("{}").format(factorial_num))
            # incrementing counter
            counter = counter + 1
            # ending loop
            #break
            if counter > user_num_int:
                break
        # ending remark
        print(("The factorial is {}").format(factorial_num))


if __name__ == "__main__":
    main()
