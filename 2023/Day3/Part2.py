from Part1 import nums,eng,product
from itertools import groupby
gears=[]
for n,ind,start,span in nums:
    for x,y in product([-1,0,1],range(-1,span+1)):
        if 0<=ind+x<len(eng) and 0<=start+y<len(eng[0]) and not(x==0 and y in range(span)) and eng[ind+x][start+y]=='*':
            gears.append((n,ind+x,start+y))
res=0
for i,j in groupby(sorted(gears,key=lambda x:(x[1],x[2])) ,key=lambda x:(x[1],x[2])):
    if len(l:=list(j))==2:
        res+=int(l[0][0])*int(l[1][0])
print(res)
    

    
