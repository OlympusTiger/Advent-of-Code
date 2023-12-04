import re
with open('2023\Day2\input.txt') as f:
    games=f.read().splitlines()
possible=[]
for game in games:
    r=re.findall('\d+(?= red)',game)
    g=re.findall('\d+(?= green)',game)
    b=re.findall('\d+(?= blue)',game)
    if all(int(i)<=12 for i in r) and all(int(i)<=13 for i in g) and all(int(i)<=14 for i in b):
        possible.append(int(re.search('\d+',game).group(0)))
print(sum(possible))
