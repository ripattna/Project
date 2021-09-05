import multiprocessing as mp
from multiprocessing import Process

print(mp.cpu_count())  # Printing the CPU of the machine


def my_function():
    print("Hello!!")


if __name__ == "__main__":
    proc = Process(target=my_function)
    proc.start()
    proc.join()
