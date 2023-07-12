import re
a = re.compile('[aeiou]',re.I)
while True:
    string = input()
    if string == '#':
        break
    print(len(a.findall(string)))