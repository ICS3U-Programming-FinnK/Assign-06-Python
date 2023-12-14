#!/usr/bin/env python3
# Created by: Finn Kitor
# Created on: December 13th, 2023
# this program asks for the user to input numbers
# and it will display if the number is a perfect square.
def find_perfect_squares(numbers):
    # Checking if the input is a list
    if not isinstance(numbers, list):
        raise TypeError("Input should be a list.")

    perfect_squares = []

    # Iterating through each number in the list
    for num in numbers:
        try:
            # Trying to convert the number to an integer
            num = int(num)

            # Checking if the number is a perfect square
            if num >= 0 and int(num**0.5) ** 2 == num:
                perfect_squares.append(num)
        except ValueError:
            # Catching the error if the number is not a valid integer
            pass

    return perfect_squares


def main():
    try:
        # Asking the user for a list of whole numbers
        numbers = input("Please enter a list of whole numbers, separated by commas: ")
        numbers = [
            int(x) for x in numbers.split(",")
        ]  # Convert input string to a list of integers
        perfect_squares = find_perfect_squares(
            numbers
        )  # Finding the perfect squares from the list

        # Printing the list of perfect squares
        print("These numbers are perfect squares:", perfect_squares)
    except ValueError:
        # Catching the error if the input is not a valid list
        print("Invalid input. What you entered is not a number.")


# Calling the main function to start the program
if __name__ == "__main__":
    main()
