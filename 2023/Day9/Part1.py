from itertools import pairwise
from operator import sub

with open('2023\Day9\input.txt') as f:
    seq=[list(map(int,i.split())) for i in f.read().splitlines()]


Part2=False
if Part2:
    seq=[s[::-1] for s in seq]

def get_next(row):
    new=[]
    for pair in pairwise(row):
        new.append(sub(*pair[::-1]))
    if set(new)=={0}:
        return row[-1]
    else:
        return row[-1] + get_next(new)

res=0       
for s in seq:
    res+=get_next(s)

print(res)


        
