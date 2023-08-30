import time
from python.utils import get_input

day = 10

def main(input):
    instructions = input.split("\n")
    register_vals = []
    for instruction in instructions:
        if instruction.startswith("noop"):
            if len(register_vals) == 0:
                register_vals.append(1)
            register_vals.append(register_vals[-1])
        elif instruction.startswith("add"):
            if len(register_vals) == 0:
                register_vals.append(1)
            register_vals.append(register_vals[-1])
            register_vals.append(register_vals[-1] + int(instruction.split(" ")[-1]))
    print(register_vals)
    result = 20 * register_vals[19] + 60 * register_vals[59] + 100 * register_vals[99] + 140 * register_vals[139] + 180 * register_vals[179] + 220 * register_vals[219]
    print(result)

if __name__ == '__main__':
    start = time.perf_counter()
    main(get_input(day))
    print(f"{(time.perf_counter() - start) * 1000:.3f}ms")