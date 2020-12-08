
def part1(arr):
    for num in arr:
        if 2020 - num in arr:
            print('part1 : ' + str(num * (2020 - num)))
            break


def part2(arr):
    for num in arr:
        for other in arr:
            for third in arr:
                if num + other + third == 2020:
                    print('part2 : ' + str(num * other * third))
                    exit()


with open('input.txt') as f:
    data = [int(i) for i in f.readlines()]
    f.close()


part1(data)
part2(data)
