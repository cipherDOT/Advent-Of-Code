# Advent Of Code 2020 day 4

# function that returns wheter a given field list meets
# the validation criteria of passports
def valid(arr):
    count = 0
    tests = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']
    for test in tests:
        if test in arr:
            # to make sure it met all the charecter in the test array
            # we use a count variable to keep track of the pass cases
            count += 1

    # only if every test is passed i.e., count = 7
    if count == 7:
        return True
    return False


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
            # we take the first three charecter of the elements
            # in a list of elements split by spaces from a stripped line,
            # and add that to the last arr in the data array.
            data[i] += [i[:3] for i in line.strip().split(' ')]


# variables that hold number of valid and
# non valid passports
valid_f = 0
non_valid_f = 0

for row in data:
    if valid(row):
        valid_f += 1
    else:
        non_valid_f += 1

print('valid : ' + str(valid_f))
print('non valid : ' + str(non_valid_f))
