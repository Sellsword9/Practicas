# pylint: disable=invalid-name
"""
This is a very inefficient sorting algorithm. 
It works by generating random permutations of the list until it finds one that is sorted.
This script is a simple implementation of the algorithm.
Also it checks how much time do quicksort takes 
to sort a randomized list of a given size
and how much time does bogosort take to sort the same list.
"""
import random
import time
import sys

def protector(iterations_now: int):
    """
    Ends the program if the iterations exceed one billion
    and prints iterations conditionally.
    """
    # checks if the iterations are a multiple of 5 by functional programming
    if not iterations_now % 5:
        if iterations_now < 10^6:
            if not iterations_now % 5000:
                print("Iterations:", iterations_now, sep=" ")
        else:
            if iterations_now < 10000:
                print("Iterations:", iterations_now, sep=" ")
            else:
                if not iterations_now % 500:
                    print("Iterations:", iterations_now, sep=" ")


    if iterations_now > 1_000_000_000:
        print("The algorithm took too long to sort the list.")
        print("Please try again with a smaller list.")
        sys.exit()
def get_random_list(length: int, border: int) -> list:
    """
    Returns a list of random integers of a given length and border.
    """
    return [random.randint(0, border) for i in range(length)]

def is_sorted(list_to_check: list) -> bool:
    """
    Returns True if the list is sorted in ascending order, False otherwise.
    """
    return list_to_check == sorted(list_to_check)

def quicksort(list_to_sort: list):
    """
    Returns a sorted list using the quicksort algorithm
    and the number of iterations it took to sort the list.
    """
    if len(list_to_sort) <= 1:
        return list_to_sort, 0
    pivot = list_to_sort[random.randint(0, len(list_to_sort) - 1)]
    less = []
    equal = []
    greater = []
    iteraciones = 0
    for element in list_to_sort:
        if element < pivot:
            less.append(element)
        elif element == pivot:
            equal.append(element)
        else:
            greater.append(element)
        iteraciones += 1
        protector(iteraciones)

    left, left_iterations = quicksort(less)
    right, right_iterations = quicksort(greater)
    return left + equal + right, iteraciones + left_iterations + right_iterations

def main():
    """
    The main function.
    """
    try:
        list_length = int(input("Enter the length of the list: "))
        list_border = int(input("Enter the border of the list: "))

        random_list = get_random_list(list_length, list_border)
        list_to_sort = random_list.copy()
        list_to_sort2 = random_list.copy()
        print("Random list:", random_list, sep="\n")
        start_time = time.time()
        temp_iterations = 0
        list_to_sort, temp_iterations = quicksort(list_to_sort)
        end_time = time.time()
        duration = end_time - start_time
        print("Quicksort:", list_to_sort, sep="\n")
        print("Time taken:", duration, "seconds", sep=" ")
        print("Iterations:", temp_iterations, sep=" ")
        # Resets the iterations counter
        temp_iterations = 0
        start_time = time.time()
        while not is_sorted(list_to_sort2):
            random.shuffle(list_to_sort2)
            temp_iterations += 1
            protector(temp_iterations)
        end_time = time.time()
        duration = end_time - start_time
        print("Bogosort:", list_to_sort2, sep="\n")
        print("Time taken:", duration, "seconds", sep=" ")
        print("Iterations:", temp_iterations, sep=" ")


    except ValueError:
        print("Invalid input.")
        main()
# Executes the main function
main()
