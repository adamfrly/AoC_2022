import time
from python.utils import get_input

day = 0

def main(input):
    pass

if __name__ == '__main__':
    start = time.perf_counter()
    main(get_input(day))
    print(f"{(time.perf_counter() - start) * 1000:.3f}ms")