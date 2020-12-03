# Link: https://adventofcode.com/2020/day/3

# Read input into list
with open('day03.1-input.txt') as f:
    rows = f.readlines()

rows = [row.replace("\n", "") for row in rows]

row_length = len(rows[0])
cur_pos = 0
tree_counter = 0

for row in rows:

    if row[cur_pos] == '#':
        tree_counter += 1

    cur_pos += 3

    if cur_pos >= row_length:
        cur_pos = cur_pos - row_length

print(tree_counter)