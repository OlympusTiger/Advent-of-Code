import re
from operator import add
from Part1 import l
d={'one':1,'two':2,'three':3,'four':4,'five':5,'six':6,'seven':7,'eight':8,'nine':9}
keys='|'.join(list(d.keys()))
nums=[]
for c in l:
    n1=re.search(f'{keys}|\d',c).group(0)
    n2=re.search(f'{keys[::-1]}|\d',c[::-1]).group(0)

    nums.append([n1,n2[::-1]])

     
print(sum(map(lambda x:int(add(*map(lambda y:y if y.isdigit() else str(d[y]),x))),nums)))