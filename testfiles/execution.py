import time

def run_test():
    n = 2
    t = time.time()
    run = 0

    while True:
        if time.time() > (t + 1):
            print(run)
            run = 0
            t = time.time()
        run += 1
        void = n + n
