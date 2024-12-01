with open('input.txt') as f:
    left = []
    right = []

    for line in f.read().split('\n'):
        l,r = line.split()
        left.append(int(l))
        right.append(int(r))
    left.sort()
    right.sort()

    def part1(left_list: list[int], right_list: list[int]):
        distance = 0
        for x in zip(left_list, right_list):
            distance += abs(x[0] - x[1])
        return distance

    p1_solution = part1(left, right)
    print(p1_solution)

    def part2(left_list: list[int], right_list: list[int]):
        similarity = 0
        for x in range(len(left_list)):
            similarity += left[x] * sum(y == left_list[x] for y in right_list)
        return similarity

    p2_solution = part2(left, right)
    print(p2_solution)