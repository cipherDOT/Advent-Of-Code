# Advent of Code 2020 day 3

# On optimizations:
#   we can use 0s and 1s (binary) instead of using the direct string values in the traverse func.
#   this can be done while making the data array, by replacing every '.' with 0 and
#   every '#' with 1. This may speed up the process a little. We shold also change the path and tree varialbles
#   to being 0 and 1
#
#   ```
#   path = 0
#   tree = 1
#   ```
#   or just delete them. But this doesn't allow for flexibility in the code

def traverse(arr, r, d):
    x = 0
    y = 0
    total_path = 0
    total_tree = 0
    path = '.'
    tree = '#'
    for _ in range(len(arr)):
        current = arr[x][y]
        if current == path:
            total_path += 1
        elif current == tree:
            total_tree += 1

        y += r
        y = y % len(arr[0])
        # The below part is crucial since you need to stop if you reached the bottom-most
        # so the modulus operator won't help. Also you need to break out of the loop if you
        # reached the bottom-most, or else you will be processing the same line many times
        if x <= len(arr) - d:
            x += d
        else:
            break

    print(total_tree)
    return total_tree


with open('input.txt') as f:
    data = [i.strip() for i in f.readlines()]

first = traverse(data, 1, 1)
second = traverse(data, 3, 1)  # (the first part of the puzzle)
third = traverse(data, 5, 1)
fourth = traverse(data, 7, 1)
fifth = traverse(data, 1, 2)

print(first * second * third * fourth * fifth)

# Right 1, down 1.
# Right 3, down 1. (This is the slope you already checked.)
# Right 5, down 1.
# Right 7, down 1.
# Right 1, down 2.
