import time
from python.utils import get_input

day = 4

def main(input):
    result = 0
    pairs = input.split('\n')
    for pair in pairs:
        if pair[0] <= pair[4] and pair[2] >= pair[-1]: # First surrounds second
            result += 1
        elif pair[4] <= pair[0] and pair[-1] >= pair[2]: # Second surrounds first
            result += 1
    print(result)

if __name__ == '__main__':
    start = time.perf_counter()
    main(get_input(day))
    print(f"{(time.perf_counter() - start) * 1000:.3f}ms")