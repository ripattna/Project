import multiprocessing as mp


def sqr(x, q):
    q.put(x * x)


if __name__ == '__main':
    q = mp.Queue()
    processes = [mp.Process(target=sqr, args=(i, q))for i in range(2, 10)]

    for p in processes:
        p.start()

    for p in processes:
        p.join()

    result = [q.get() for p in processes]
    print(result)
