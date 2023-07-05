import time


class CodeTimer:
    def __init__(self):
        self.start = None

    def __enter__(self):
        self.start = time.time()

    def __exit__(self, exc_type, exc_val, exc_tb):
        t = time.time() - self.start
        print(f'kod rabotal {t} sec.')

        if exc_type is IndexError:
            return True



timer = CodeTimer()

with timer:
    l = [x for x in range(100_100_100)]



