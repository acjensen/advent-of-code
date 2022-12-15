#!python3

def solve(part: int):

    def window(arr, k):
        for i in range(len(arr)-k+1):
            yield arr[i:i+k]

    with open("2022/day14/input.txt") as f:
        lines = f.read().splitlines()

    stuff = [[pair.split(',') for pair in line.split(' -> ')] for line in lines]

    abyss = 0
    min_x = 10000000000
    max_x = 0
    for s in stuff:
        for pair in s:
            x, y = pair
            x = int(x)
            y = int(y)
            if y > abyss:
                abyss = y
            if x < min_x:
                min_x = x
            if x > max_x:
                max_x = x

    blocked = set()

    for s in stuff:
        for group in window(s, 2):
            left, right = group
            for x in range(min(int(left[0]), int(right[0])), max(int(left[0]), int(right[0])) + 1):
                for y in range(min(int(left[1]), int(right[1])), max(int(left[1]), int(right[1])) + 1):
                    blocked.add((x, y))


    def simulate():
        count = 0
        while True:
            sand = (500, 0)
            if sand in blocked:
                return count
            while True:
                if part == 1 and sand[1] > abyss:
                    return count
                elif part == 2 and sand[1] == abyss + 1:
                    blocked.add(sand)
                    break
                elif not (sand[0], sand[1]+1) in blocked:
                    sand = (sand[0], sand[1]+1)
                elif not (sand[0]-1, sand[1]+1) in blocked:
                    sand = (sand[0]-1, sand[1]+1)
                elif not (sand[0]+1, sand[1]+1) in blocked:
                    sand = (sand[0]+1, sand[1]+1)
                else:
                    blocked.add(sand)
                    break
            count += 1

    print(simulate())

solve(part=1)
solve(part=2)