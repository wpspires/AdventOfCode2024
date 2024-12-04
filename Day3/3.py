import re

code = open('input.txt').read()
count = 0

''' 
p1
pairs = re.findall("mul\(([\d]{1,3},[\d]{1,3})\)", code)
for pair in pairs:
    a,b = map(int, pair.split(','))
    count += a * b
'''

#p2
regex = "mul\(([\d]{1,3},[\d]{1,3})\)"
enabled = True
for x in range(len(code)):
    if code[x:].startswith("do()"):
        enabled = True
    if code[x:].startswith("don't()"):
        enabled = False
    if enabled:
        command = re.match(regex, code[x:])
        if command is not None:
            a,b = map(int, command.group(1).split(','))
            count += a * b

print(count)