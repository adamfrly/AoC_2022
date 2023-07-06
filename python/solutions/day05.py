import time
from typing import Tuple, List
from python.utils import get_input, ints

day = 5

def main(input):
	original_crates, moves = parse_input(input)
	for move in moves:
		m_num, m_from, m_to = ints(move)
		
		for _ in range(m_num):
			original_crates[m_to].append(original_crates[m_from].pop(-1))
	result = [crate[-1] for crate in original_crates if crate]
	result.pop(0)
	print(result)

def parse_input(text: str) -> Tuple[List[List[str]], List[str]]:
	stack, moves = text.split('\n\n')
	crates = [['?'], [], [], [], [], [], [], [], [], []]  # Empty crate in position zero, nine other crates
	for line in stack.split('\n')[-2::-1]:  # Reverse order, skip the first line (crate numbers)
		for i in range(9):
			if 4 * i + 1 < len(line) and (c := line[4 * i + 1]) != ' ':
				crates[i + 1].append(c)
	return crates, moves.split('\n')

if __name__ == '__main__':
	start = time.perf_counter()
	main(get_input(day))
	print(f"{(time.perf_counter() - start) * 1000:.3f}ms")