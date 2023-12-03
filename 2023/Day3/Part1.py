from itertools import product
from operator import sub
import re
with open('2023\Day3\input.txt') as f:
    f=f.read()
    eng=[i for i in f.splitlines()]
    symbols=set([i for i in f if i!='.' and not i.isdigit()])
def unpack_iter(it,ind):
    return it.group(),ind,it.start(),sub(*it.span()[::-1])
def get_numbers(eng):
    nums=[]
    for i,k in enumerate(eng):
        for l in re.finditer('\d+', k):
            nums+=[(unpack_iter(l,i))]
    return nums
def get_adjacent():
    nums=get_numbers(eng)
    exclude=[]
    for n,ind,start,span in nums:
        if all(eng[ind+x][start+y] not in symbols for x,y in product([-1,0,1],range(-1,span+1)) if 0<=ind+x<len(eng) and 0<=start+y<len(eng[0]) and not(x==0 and y in range(span))):
            exclude.append(n)
    return nums,exclude

nums,exclude=get_adjacent()
print(sum([int(i[0]) for i in nums])-(sum(map(int,exclude))))




