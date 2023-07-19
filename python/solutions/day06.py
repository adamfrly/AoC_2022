import time
from python.utils import get_input

day = 6 

def main(input):
    results = []
    buffers = input.split("\n")
    for buffer in buffers:
        for i, _ in enumerate(buffer):
            if len(set(buffer[i:i+4])) == 4:
                results.append(i+4)
                break
    print(results)
                

if __name__ == '__main__':
    start = time.perf_counter()
    main(get_input(day))
    print(f"{(time.perf_counter() - start) * 1000:.3f}ms")