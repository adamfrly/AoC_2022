def get_input(day: int, path: str = 'inputs/day%02d.txt') -> str:
    with open(path % day, 'r', encoding='utf-8') as f:
        return f.read()