from itertools import combinations

with open('input.txt') as f:
	sky=[i for i in f.read().splitlines()]

exp_rows=[]
for i,s in enumerate(sky):
	if set(s)=={'.'}:
		exp_rows.append(i) 

exp_cols=[]
for i in range(len(sky[0])):
	if all(s[i]=='.' for s in sky):
		exp_cols.append(i) #

galaxies=[]			
for i in range(len(sky)):
	for j in range(len(sky[0])):
		if sky[i][j]=='#':
			galaxies.append((i,j)) 

Part2=False #Change for Part2 result

multiplier=1
if Part2:
	multiplier=999999
distance=0
for i,j in combinations(galaxies,2): 
		
		c1=len(set(range(min(i[0],j[0]),max(i[0],j[0]))) &set(exp_rows)) 
		c2=len(set(range(min(i[1],j[1]),max(i[1],j[1]))) &set(exp_cols)) 
		
		d=abs(j[0]-i[0])+abs(j[1]-i[1])+multiplier*c1+multiplier*c2 
		distance+=d
		
print (distance)