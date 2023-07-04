import time
from python.utils import get_input

def main(input):
    weights = list(map(sum, [list(map(int, x.split("\n"))) for x in input.rstrip("\n").split("\n\n")]))
    print(max(weights))

if __name__ == '__main__':
    start = time.perf_counter()
    main(get_input(1))
    print(f"{(time.perf_counter() - start) * 1000:.3f}ms")