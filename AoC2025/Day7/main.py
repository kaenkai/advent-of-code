def part1(in_file: str) -> None:
    """Part 1"""
    n_split = 0
    timelines = 0
    beams = set()
    with open(in_file, 'r') as file:
        for i, s in enumerate(file.readline()):
            if s == 'S':
                beams.add(i)
                break
        for r in file:
            for i, s in enumerate(r):
                if s == '^' and i in beams:
                    if i == 0:
                        beams.add(i+1)
                    elif i == len(r) -1:
                        beams.add(i-1)
                    else:
                        beams.update([i-1, i+1])
                    beams.remove(i)
                    n_split += 1
                    timelines += 3
    print('Times split:', n_split)
    print('Timelines:', timelines)


def part2(in_file: str) -> None:
    """Part 2"""
    beams = set()
    with open(in_file, 'r') as file:
        for i, s in enumerate(file.readline()):
            if s == 'S':
                beams.add(i)
                break
        for r in file:
            for i, s in enumerate(r):
                if s == '^' and i in beams:
                    if i == 0:
                        beams.add(i+1)
                    elif i == len(r) -1:
                        beams.add(i-1)
                    else:
                        beams.update([i-1, i+1])
                    beams.remove(i)


if __name__ == '__main__':
    part1('AoC2025/Day7/test.txt')
