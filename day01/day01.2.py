# Link: https://adventofcode.com/2020/day/1

# Before you leave, the Elves in accounting just need you to fix your expense
# report (your puzzle input); apparently, something isn't quite adding up.

# Specifically, they need you to find the two entries that sum to 2020 and 
# then multiply those two numbers together.

# Read input into list
with open('day01.1-input.txt') as f:
    expenses = f.readlines()

expenses = [int(expense.replace("\n", "")) for expense in expenses]

for first in range(len(expenses)):
    for second in range(first+1, len(expenses)):
        for third in range(second+1, len(expenses)):
            value1 = expenses[first]
            value2 = expenses[second]
            value3 = expenses[third]

            if (value1 + value2 + value3) == 2020:
                print(value1 * value2 * value3)
