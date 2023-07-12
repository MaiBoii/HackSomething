import re
lower = re.compile('[a-z]')
upper = re.compile('[A-Z]')
number = re.compile('\d')
space = re.compile('\s')

while True:
    try:
        line = input()
        print(f'{len(lower.findall(line))} {len(upper.findall(line))} {len(number.findall(line))} {len(space.findall(line))}')
    except EOFError:
        break