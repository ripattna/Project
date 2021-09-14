import multiprocessing as mp
from multiprocessing import Process


def lang_func(lang):
    print(lang)
    # print('The CPU count:', mp.cpu_count())  # Printing the CPU of the machine


if __name__ == "__main__":
    languages = ['Python', 'C', 'JAVA', 'PHP']
    processes = []
    for i in languages:
        proc = Process(target=lang_func, args=(i,))
        processes.append(proc)
        proc.start()

    for j in processes:
        j.join()





