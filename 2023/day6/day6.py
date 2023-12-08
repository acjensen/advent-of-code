
import os


def read_input_lines(filename):
    anchor = os.path.dirname(__file__)
    f = open(os.path.join(anchor, filename))
    lines = [l.strip() for l in f.readlines()]
    f.close()
    return lines


for _input in ["input_example", "input"]:
    lines = read_input_lines(_input)

    def pt1():
        time = map(int, lines[0].split()[1:])
        distance = map(int, lines[1].split()[1:])

        ans = 1
        for t, d in zip(time, distance):
            def get_count():
                count = 0
                for x in [(t-t1)*t1 for t1 in range(1, t)]:
                    if x > d:
                        count += 1
                return count
            ans *= get_count()
        print("pt1", _input, ans)
    pt1()

    def pt2():
        t = int(''.join(lines[0].split()[1:]))
        d = int(''.join(lines[1].split()[1:]))

        def get_count():
            count = 0
            for x in [(t-t1)*t1 for t1 in range(1, t)]:
                if x > d:
                    count += 1
            return count
        print("pt2", _input, get_count())

    pt2()
