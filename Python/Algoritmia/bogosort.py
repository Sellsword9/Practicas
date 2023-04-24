"""
Bogosort is a very inefficient sorting algorithm. 
It works by generating random permutations of the list until it finds one that is sorted.
This script is a simple implementation of the algorithm.
Also it checks how much time do python's built-in sort takes 
to sort a randomized list of a given size
and how much time does bogosort take to sort the same list.
"""
import random
def get_random_list(length: int, border: int) -> list:
    """
    Returns a list of random integers of a given length and border.
    """
    return [random.randint(0, border) for i in range(length)]

def is_sorted(list_to_check: list) -> bool:
    """
    Returns True if the list is sorted in ascending order, False otherwise.
    """
    return list_to_check == sorted(list)

def main():
    """
    The main function.
    """
    try:
        list_length = int(input("Enter the length of the list: "))
        list_border = int(input("Enter the border of the list: "))

        random_list = get_random_list(list_length, list_border)
        print("Random list:", random_list, sep="/n")


    except ValueError:
        print("Invalid input.")
        main()
    