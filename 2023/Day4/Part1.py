import re
with open('2023\Day4\input.txt') as f:
    cards=[i[i.index(':')+1:].split('|') for i in f.read().splitlines()]
cards=list(map(lambda x:[x[0].split(),x[1].split()],cards))
sum=0

for i in cards:
    
    sum+=int(2**(len(set(i[0])&set(i[1]))-1))
print(sum)

