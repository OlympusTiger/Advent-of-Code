from math import sqrt,ceil
with open('2023\Day6\input.txt') as f:

    lines=f.read().splitlines()
    z=zip(map(int,lines[0].split()[1:]),map(int,lines[1].split()[1:]))
res=1
for t in z:
    d=t[0]**2-4*t[1]
    if d<0:
        continue
    s1 = (t[0]-sqrt(d))/2
    s2 = (t[0]+sqrt(d))/2
    if int(s2)==s2 or int(s1)==s1:
        res*=ceil(s2)-ceil(s1)-1
    else:
        res*=ceil(s2)-ceil(s1)
print(res)
