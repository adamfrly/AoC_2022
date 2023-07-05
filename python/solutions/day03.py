import time
from python.utils import get_input

day = 3

def main(input):
    sacks = input.split("\n")
    result = 0
    for sack in sacks:
        half_1 = list(sack[:len(sack)//2])
        half_2 = list(sack[len(sack)//2:])
        priority = ord(set(half_1).intersection(half_2).pop())
        priority = priority - 96 if priority >= 97 else priority - 38
        result += priority
    print(result)
    
if __name__ == '__main__':
    start = time.perf_counter()
    main(get_input(day))
    print(f"{(time.perf_counter() - start) * 1000:.3f}ms")