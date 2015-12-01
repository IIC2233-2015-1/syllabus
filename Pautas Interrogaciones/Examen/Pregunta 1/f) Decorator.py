    import threading


    def decorator_f(f):
        def f2():
            lock.acquire()
            try:
                return f()
            finally:
                lock.release()
        return f2


    @decorator_f
    def f():
        for j in range(7):
            print(j)

    if __name__ == "__main__":
        lock = threading.Lock()
        num_threads = 10
        t = []
        for i in range(num_threads):
            my_thread = threading.Thread(target=f)  # , args = (i,)
            t.append(my_thread)
        for th in t:
            th.start()
