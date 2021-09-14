import multiprocessing as mp
from multiprocessing import Process


def my_function():
    print("Hello!!")
    print('The CPU count:', mp.cpu_count())  # Printing the CPU of the machine


if __name__ == "__main__":
    proc = Process(target=my_function)
    proc.start()   # Start the process
    proc.join()    # Join represent to terminate the process
