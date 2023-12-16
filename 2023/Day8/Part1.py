from itertools import cycle

with open('2023\Day8\input.txt') as f:
    directions=f.readline()
    guide={}
    for line in f.read().splitlines()[1:]:
        k=line[:3]
        v1=line[7:10]
        v2=line[12:15]
        guide[k]=(v1,v2)

directions=directions.replace('R','1').replace('L','0').strip('\n')

pos='AAA'
steps=0
for i in cycle(directions):
    pos=guide[pos][int(i)]
    steps+=1
    if pos=='ZZZ':
        break

print(steps)