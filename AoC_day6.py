# Advent Of Code 2020 day 5

# ------------------------------------------------------------------------------------------------------------------------------------------------------- #
# part one

with open('input.txt') as f:
    data = [[]]
    # a variable to keep track of the new line charecters and
    # make new array and to append the data in the current array
    i = 0
    for line in f.readlines():
        # if a ne line charecter appears individually
        # we ignore it and add a new arr to our data array
        if line == '\n':
            i += 1
            data.append([])
        else:
            # we take every element in the array
            data[i] += [i for i in line.strip()]

answers = []

for i in range(len(data)):
    # we use sets because it not add duplicate elements
    answers.append(set())

for i, k in enumerate(data):
    for q in k:
        answers[i].add(q)

total = 0

for a in answers:
    for q in a:
        total += len(q)

# the total is basically the number of non repeating charecter in a given group, added for all the group
print('part 1 : ' + str(total))

# ------------------------------------------------------------------------------------------------------------------------------------------------------- #

# part two

with open('input.txt') as f:
    data = [[]]
    # a variable to keep track of the new line charecters and
    # make new array and to append the data in the current array
    i = 0
    for line in f.readlines():
        # if a ne line charecter appears individually
        # we ignore it and add a new arr to our data array
        if line == '\n':
            i += 1
            data.append([])
        else:
            # we add the total string of each line in the data array
            data[i] += [line.strip()]


# if the letters in first element is present in letters in every element then the number of
# same questioin answered yes is the number of times each element appears.
# There are no duplicate elements in the input data[in the same line]
def sol(arr):
    count = 0
    everything = ''
    for i in arr[1:]:
        everything += i

    for let in arr[0]:
        # this step is important since you are not only checking
        # whether it is present in other elements but, EACH AND EVERY other element
        if everything.count(let) == len(arr[1:]):
            count += 1

    return count


# variable that keeps track of the total
total = 0

for key in data:
    if len(key) == 1:
        # we add the len of the element in the array
        # because technically each and every member has given the same answer
        total += len(key[0])

    else:
        total += sol(key)

print('part 2 : ' + str(total))

