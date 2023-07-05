import time
from python.utils import get_input

day = 3

def main(input):
    sacks = input.split("\n")
    result = 0
    for sack in sacks:
        half_1, half_2 = list(sack[:len(sack)//2]), list(sack[len(sack)//2:])
        overlap = set(half_1).intersection(half_2).pop()
        result += get_priority(overlap)
    print(result)

def get_priority(ch):
    return 1 + (ord(ch) - ord('a') if ch.islower() else ord(ch) - ord("A") + 26)

if __name__ == '__main__':
    start = time.perf_counter()
    main(get_input(day))
    print(f"{(time.perf_counter() - start) * 1000:.3f}ms")