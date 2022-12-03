
with open("data.txt", "r") as file:
    raw_data = [line.strip() for line in file.readlines()]
    file.close()

bag_data = {}

for data in raw_data:
    bag, items = data.split(" contain ")

    bag = bag.strip().rstrip("s")

    items = [i.strip().rstrip("s") for i in items.strip('.').split(',')]
    items = [' '.join(i.split(' ')[1:]) if i.split(" ")[0].isnumeric() else i for i in items]
    bag_data[bag] = items if items != ['no other bag'] else None

shiny = "shiny gold bag"

def check_bag(bag):
    if bag_data[bag] == None:
        return 0
    elif bag == shiny:
        return 0
    else:
        can_hold_shiny_bag = 0
        for new_bag in bag_data[bag]:
            if new_bag == shiny:
                return 1
            else:
                can_hold_shiny_bag += check_bag(new_bag)

        return 1 if can_hold_shiny_bag > 0 else 0

total_score = 0

for bag in bag_data.keys():
    total_score += check_bag(bag)

print(f"Part 1: {total_score}")

