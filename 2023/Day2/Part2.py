from Part1 import games,r,g,b
import re
powers=[]
for game in games:
    r=re.findall('\d+(?= red)',game)
    g=re.findall('\d+(?= green)',game)
    b=re.findall('\d+(?= blue)',game)
    powers.append(max(map(int,r))*max(map(int,g))*max(map(int,b)))
print(sum(powers))
