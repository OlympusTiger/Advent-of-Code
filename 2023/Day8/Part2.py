from itertools import cycle
from math import lcm
from Part1 import guide,directions

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
