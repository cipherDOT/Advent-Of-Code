# Advent of Code 2020 day 1

def part1(arr):
    for num in arr:
        if 2020 - num in arr:
            print('part1 : ' + str(num * (2020 - num)))
            break


def part2(arr):
    # since they did not specify that the three
    # numbers will be different(atmost two of them can be the same),
    # we check every single number for each loop(which is a serious efficiency issue)...
    for num in arr:
        for other in arr:
            for third in arr:
                if num + other + third == 2020:
                    print('part2 : ' + str(num * other * third))
                    exit()


# we input the data from the input.txt file (the puzzle input in advent of code)
with open('input.txt') as f:
    # we need to specify int() , because otherwise the strings will have a '\n' in them(new line charecter)
    data = [int(i) for i in f.readlines()]
    f.close()


# outputting the results
part1(data)
part2(data)
