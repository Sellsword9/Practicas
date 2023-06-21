""" Testing the performance of threads and threading use itself"""
# Imports
import time # For time.sleep()
from threading import Thread # For threading
# Do some example functions
def function1():
    """
    First example function
    """
    print("Function 1 started")
    time.sleep(4)
    print("Function 1 ended")
def function2():
    """
    Second example function
    """
    print("Function 2 started")
    time.sleep(3)
    print("Function 2 ended")

def ask_threads():
    """
    Asks if the user wants to run the program with threads or not
    """
    print("Do you want to run the program with threads?")
    print("1. Yes")
    print("2. No")
    answer = input("Answer: ")
    if answer == "1":
        return True
    elif answer == "2":
        return False
    else:
        print("Please enter a valid answer")
        ask_threads()

# Runs the program with threads
def run_threads(start_time: float):
    """
    module docstring may affect performance, so it's duplicated
    """
    print("Running with threads")
    th1 = Thread(target=function1)
    th2 = Thread(target=function2)
    th1.start()
    th2.start()
    th1.join()
    th2.join()
    print("Time taken: " + str(time.time() - start_time))

# Runs the program without threads
def run_no_threads():
    """
    module docstring may affect performance, so it's duplicated
    """
    print("Running without threads ...")
    function1()
    function2()

# Main function
def main():
    """
    Runs the program
    """
    if ask_threads():
        # Saves the local time to know how much it took to run the program
        start_time = time.time()
        run_threads(start_time)
    else:
        start_time = time.time()
        run_no_threads()
        print("Time taken: " + str(time.time() - start_time))

main()
print("""
Results: 
    As expected, the program runs faster with threads.
    Also expected, the program takes the time of the longest function to run if thread are used.
     but takes the time of the sum of the functions if threads are not used.
    Theres a minimal possible error of 0.1~ seconds in the time taken.
""")
print("Press enter to exit ...")
