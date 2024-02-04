from itertools import product
with open('2023\Day21\example.txt') as f:
    garden=[[r for r in rows] for rows in f.read().splitlines()]


shape=len(garden)

up=(-1,0)
down=(1,0)
right=(0,1)
left=(0,-1)

for i in range(shape):
    for j in range(shape):
        if garden[i][j]=='S':
            start=tuple((i,j))
            break
counter=0
for i,j in product(range(shape),repeat=2):
    if (abs(start[0]-i)+abs(start[1]-j))%2==0 and (abs(start[0]-i)+abs(start[1]-j))<=6 and garden[i][j]!='#':
        counter+=1
print(counter)