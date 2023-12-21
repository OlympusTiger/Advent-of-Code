from shapely import Polygon,Point

with open('2023\Day18\input.txt') as f:
    guide=[x.split() for x in f.read().splitlines()]

heading={'R':(0,1),'L':(0,-1),'U':(-1,0),'D':(1,0)}

pos=(0,0)
corners=[]

for g in guide:
    pos=tuple(map(lambda x:x[0]+x[1]*int(g[1]), zip(pos, heading[g[0]]))) #(0,0)    3   (0,1)
    corners.append(pos)

shape=Polygon(corners)

print(1+shape.area+shape.length/2)

