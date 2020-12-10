
# variables to represent the rows and colomns
rows = [0, 128]
cols = [0, 8]

# ids array to compare the board ids(bids) array
# ids array consists elements from 0 to 1023 because the maximum id of the plane is 1023
ids = [i for i in range(1024)]
bids = []

# result array to compare and find the single key
result = []
myid = 0


# Pointer object to move up, down, left and right in the plane
class Pointer(object):
    def __init__(self, rows, cols):
        self.rmin = rows[0]
        self.rmax = rows[1]
        self.cmin = cols[0]
        self.cmax = cols[1]

    def point(self):
        return self.rmin * 8 + self.cmin

    def left(self):
        self.cmax -= (self.cmax - self.cmin) // 2

    def right(self):
        self.cmin += (self.cmax - self.cmin) // 2

    def up(self):
        self.rmax -= (self.rmax - self.rmin) // 2

    def down(self):
        self.rmin += (self.rmax - self.rmin) // 2


# getting the input values from the input.txt file
with open('input.txt') as f:
    data = [i.strip() for i in f.readlines()]
    f.close()


# stepping throught the array and getting the ids of the seats
for order in data:
    pointer = Pointer(rows, cols)
    for key in order:
        if key == 'F':
            pointer.up()

        elif key == 'B':
            pointer.down()

        elif key == 'R':
            pointer.right()

        elif key == 'L':
            pointer.left()

    bids.append(pointer.point())

# sorting the ids for convenience and for the ease to work with
bids.sort()
highest_id = max(bids)

# getting the ids of the seats that have not been occupied
for bid in ids:
    if bid not in bids:
        result.append(bid)

# finding that one element that doesn,t match the order of n, n + 1, n + 2...
for i in range(1, len(result)):
    if result[i] != result[i - 1] + 1:
        myid = result[i]
        break

print('highest id : ' + str(highest_id))
print('my id : ' + str(myid))
