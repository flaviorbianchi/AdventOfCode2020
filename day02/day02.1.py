# Link: https://adventofcode.com/2020/day/2

# Read input into list
with open('day02.1-input.txt') as f:
    passwords = f.readlines()

passwords = [password.replace("\n", "") for password in passwords]

valid_passwords = 0

for password in passwords:
    policy, letter, passwd = password.split()

    policyMin, policyMax = policy.split('-')
    letter = letter.replace(":", "")

    if passwd.count(letter) >= int(policyMin) and passwd.count(letter) <= int(policyMax):
        valid_passwords += 1

print(valid_passwords)