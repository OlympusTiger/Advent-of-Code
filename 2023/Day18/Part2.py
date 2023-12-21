from shapely import Polygon,Point

with open('2023\Day18\input.txt') as f:
    guide=[x.split()[-1] for x in f.read().splitlines()]
print(guide)
heading={'0':(0,1),'2':(0,-1),'3':(-1,0),'1':(1,0)}

guide=[(int(g[2:7],16),heading[g[-2]]) for g in guide]

pos=(0,0)
corners=[pos]

for g in guide:
    pos=tuple(map(lambda x:x[0]+x[1]*int(g[0]), zip(pos, g[1])))
    corners.append(pos)

shape=Polygon(corners)

print(1+shape.area+shape.length/2)
