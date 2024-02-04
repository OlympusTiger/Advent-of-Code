
from functools import cache
import re

with open('2023\Day12\input.txt') as f:
	field=[i.split() for i in f.read().splitlines()]
field=list(map(lambda x: [x[0],tuple(map(int,x[1].split(',')))],field))
for i in range(len(field)):
    field[i][0]=re.sub('\.+','.',field[i][0])


Part2=False


@cache
def match_next(spr,nums): 
    combs=0
    for i,p in enumerate(spr):
        if nums and '#' not in spr[0:i] and len(spr[i:])>=nums[0]:
            if '.' not in spr[i:i+nums[0]] and (len(spr)==nums[0]+i or spr[nums[0]+i]!='#'):
                if len(nums)==1 and (len(spr)==nums[0]+i or '#' not in spr[nums[0]+i:]):
                    combs+=1                                                    
                    continue
                else:
                    combs+=match_next(spr[nums[0]+i+1:],nums[1:])
                    continue
            else:
                continue
        else:
            return combs
    
    return combs

c=0
m=1
if Part2:
    m=5

for i,f in enumerate(field):
    new=f[0]+('?'+f[0])*(m-1)
    n=f[1]*m
    b=match_next(new,n)
    c+=b

print(c)



	

			