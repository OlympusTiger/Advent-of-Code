from math import sqrt,ceil
with open('2023\Day6\input.txt') as f:

    lines=f.read().splitlines()
lines=[int(l[l.index(':')+1:].replace(' ','')) for l in lines]




d=lines[0]**2-4*lines[1]
s1 = (lines[0]-sqrt(d))/2
s2 = (lines[0]+sqrt(d))/2
if int(s2)==s2 or int(s1)==s1:
    print(ceil(s2)-ceil(s1)-1)
else:
    print(ceil(s2)-ceil(s1))
