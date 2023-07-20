import threading
import time

def function_one():
    for i in range(5):
        print("Function One")
        time.sleep(1)

def function_two():
    for i in range(5):
        print("Function Two")
        time.sleep(1)

if __name__ == "__main__":
    t_one = threading.Thread(target=function_one)
    t_two = threading.Thread(target=function_two)

    # Start both threads
    t_one.start()
    t_two.start()

    # Wait for both threads to finish
    t_one.join()
    t_two.join()

    print("Both functions have finished.")