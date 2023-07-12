import re
n = int(input())
condition = re.compile('^[A-F]?A+F+C+[A-F]?$')
for i in range(n):
    string = input()
    if condition.match(string):
        print('Infected!')
    else:
        print('Good')