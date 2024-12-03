## -- INPUT PREP -- ##
right = []
left = []
with open("../input/01-historian-hysteria-input.txt") as f:
    for line in f:
        # split the line and convert directly to an integer
        r, l = map(int, line.split())
        right.append(r)
        left.append(l)


## -- PART 1 -- ##
# sort lists
right.sort()
left.sort()

# calculate distances
total_distance = sum(abs(r - l) for r, l in zip(right, left))

# print results
print("Total Distance: ", total_distance)

## -- PART 2 -- ##
# get unique list of right list numbers
unique_right = list(set(right))

# create a dict with value: count
unique_right_dict = {}
for item in unique_right:
    unique_right_dict[item] = 0

# iterate over right, if value in keys, increment value
for item in left:
    if unique_right_dict.get(item) is not None:
        unique_right_dict[item] += 1

# get similarity by summing the value of key * value
similarity = 0
for key, value in unique_right_dict.items():
    similarity += int(key) * value

print("Similarity Score: ", similarity)
