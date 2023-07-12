import re
tag = re.compile('(<.+?>)|([^<>]+)')
s = input()
s = re.split(tag,s)
res = []
for i in s:
    if i == '' or i == None:
        continue
    elif '<' in i and '>' in i:
        res.append(i)
    else:
        j = i.split()
        for k in j:
            res.append(k[::-1])
try:
    for i in range(len(res)):
        if '<' in res[i+1]:
            print(res[i],end='')
        elif '<' in res[i]:
            print(res[i],end='')
        else:
            print(res[i],end=' ')
except IndexError:
    print(res[i],end='')