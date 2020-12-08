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
            data[i] += [i for i in line.strip().split(' ')]


def alphanum(string):
    total = 0
    for letter in string:
        if letter.isdigit() or letter in ['a', 'b', 'c', 'd', 'e', 'f']:
            total += 1

    if total == len(string):
        return True

    return False


def valid2(arr):
    count = 0
    tests = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']

    for field in arr:
        key = field[:3]
        value = field.split(':')[1]
        # print(key, value)
        if key in tests:
            # print(key)
            if key == 'byr':
                if 1920 <= int(value) <= 2002:
                    # print(1920 <= int(value) <= 2002)
                    count += 1

            elif key == 'iyr':
                if 2010 <= int(value) <= 2020:
                    # print(2010 <= int(value) <= 2020)
                    count += 1

            elif key == 'eyr':
                if 2020 <= int(value) <= 2030:
                    # print(2020 <= int(value) <= 2030)
                    count += 1

            elif key == 'hgt':
                if value[-2:] == 'cm':
                    # print(value)
                    if 150 <= int(value[:-2]) <= 193:
                        count += 1
                elif value[-2:] == 'in':
                    # print(value)
                    if 59 <= int(value[:-2]) <= 79:
                        count += 1

            elif key == 'hcl':
                # print(value)
                if (value[0] == '#' and alphanum(value[1:])):
                    # print(value)
                    count += 1

            elif key == 'ecl':
                if value in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']:
                    # print(value)
                    count += 1

            elif key == 'pid':
                if len(str(value)) == 9:
                    # print(value)
                    count += 1

    if count == 7:
        return True

    return False


valid_f = 0
non_valid_f = 0

print(len(data))
for row in data:
    if valid2(row):
        valid_f += 1
    else:
        non_valid_f += 1


print('valid : ' + str(valid_f))
print('non valid : ' + str(non_valid_f))
