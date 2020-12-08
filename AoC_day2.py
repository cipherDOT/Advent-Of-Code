
# -------------------------------------------------------part one------------------------------------------------------------------#

# we split the password string and get the values first
# then we compare and do the logical part and output the result
def valid_part1(string):
    policy, password = string.split(':')
    instances, letter = policy.split(' ')
    instances = list(instances.split('-'))
    result = password.count(letter)
    if (result >= int(instances[0]) and result <= int(instances[1])):
        return True
    return False


with open('input.txt') as f:
    data = [i.strip() for i in f.readlines()]

valid_p = 0
non_valid_p = 0

for i, p in enumerate(data):
    if valid_part1(p):
        valid_p += 1
    else:
        non_valid_p += 1

print('part one')
print('valid : ' + str(valid_p))
print('non valid : ' + str(non_valid_p))
print('\n')

# -------------------------------------------------------part two------------------------------------------------------------------#

# we again split the password string to get the values
# we do both AND operation and OR operation since they output different results


def valid_part2(string):
    policy, password = string.split(':')
    instances, letter = policy.split(' ')
    instances = list(instances.split('-'))
    if (password[int(instances[0])] == letter and password[int(instances[1])] == letter):
        return 2
    elif (password[int(instances[0])] == letter or password[int(instances[1])] == letter):
        return 1
    else:
        return 0


with open('input.txt') as f:
    data = [i.strip() for i in f.readlines()]

crct = 0
wrng = 0

for i, p in enumerate(data):
    if valid_part2(p) == 1:
        crct += 1
    else:
        wrng += 1

print('part two')
print('correct : ' + str(crct))
print('wrong : ' + str(wrng))
