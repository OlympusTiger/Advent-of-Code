from itertools import cycle
from math import lcm
from Part1 import guide,directions
# with open('2023\Day8\input.txt') as f:
#     directions=f.readline()
#     guide={}
#     for line in f.read().splitlines()[1:]:
#         k=line[:3]
#         v1=line[7:10]
#         v2=line[12:15]
#         guide[k]=(v1,v2)
# 
# directions=directions.replace('R','1').replace('L','0').strip('\n')

starting=[k for k in guide.keys() if k[-1]=='A']

loop_len=[]
for pos in starting:
    steps=0
    for i in cycle(directions):
        steps+=1
        pos=guide[pos][int(i)]
        if pos[-1]=='Z':
            loop_len.append(steps)
            break
print(lcm(*loop_len))
