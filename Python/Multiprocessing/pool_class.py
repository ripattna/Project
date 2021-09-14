from multiprocessing import Pool
import time

task = (["A", 5], ["B", 2], ["C", 1], ["D", 3])


def tasks_exec(tasks_data):
    print(f'Process {tasks_data[0]} waiting {tasks_data[1]} seconds')
    time.sleep(int(tasks_data[1]))
    print(f'Process {tasks_data[1]} finished')


def pool_func():
    p = Pool(2)
    p.map(tasks_exec, task)


if __name__ == '__main__':
    pool_func()
