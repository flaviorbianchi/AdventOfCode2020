# Link: https://adventofcode.com/2020/day/3

def find_trees(rows, right, down):
    row_length = len(rows[0])
    cur_pos = 0
    tree_counter = 0
    double_down = True
    
    for index in range(0, len(rows), down):

        row = rows[index]

        if row[cur_pos] == '#':
            tree_counter += 1

        cur_pos += right

        if cur_pos >= row_length:
            cur_pos = cur_pos - row_length

    return tree_counter

# Read input into list
with open('day03.1-input.txt') as f:
    rows = f.readlines()

rows = [row.replace("\n", "") for row in rows]

slope1 = find_trees(rows, 1, 1)
slope2 = find_trees(rows, 3, 1)
slope3 = find_trees(rows, 5, 1)
slope4 = find_trees(rows, 7, 1)
slope5 = find_trees(rows, 1, 2)

print(slope1 * slope2 * slope3 * slope4 * slope5)