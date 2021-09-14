import multiprocessing as mp


def sqr(x, q):
    q.put(x * x)


if __name__ == '__main':
    q = mp.Queue()
    p = mp.Process(target=sqr, args=(4, q))
    p.start()
    p.join()

    result = q.get()
    print(result)

