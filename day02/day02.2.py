# Link: https://adventofcode.com/2020/day/2#part2

# Read input into list
with open('day02.1-input.txt') as f:
    passwords = f.readlines()

passwords = [password.replace("\n", "") for password in passwords]

valid_passwords = 0

for password in passwords:
    policy, letter, passwd = password.split()

    policyMin, policyMax = [int(item)-1 for item in policy.split('-')]
    letter = letter.replace(":", "")

    if passwd[policyMin] == letter and not passwd[policyMax] == letter:
        valid_passwords += 1
    elif not passwd[policyMin] == letter and passwd[policyMax] == letter:
        valid_passwords += 1

print(valid_passwords)