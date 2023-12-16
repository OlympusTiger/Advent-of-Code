
from itertools import product

with open('input.txt') as f:
	scetch=[l for l in f.read().splitlines()]

links={'-':([0,1,'7J-'],[0,-1,'-FL']),'7':([1,0,'|LJ'],[0,-1,'-FL']),'J':([-1,0,'|F7'],[0,-1,'F-L']),'F':([0,1,'J-7'],[1,0,'|JL']),'L':([-1,0,'F|7'],[0,1,'-J7']),'|':([-1,0,'7F|'],[1,0,'|JL'])}

def get_next(k,l,p,symb):
	if  0<=k+p[0]<len(scetch[0]) and 0<=l+p[1]<len(scetch[1]):
		pos=(p[0]+k,p[1]+l)	
		prev=symb
		symbol = scetch[pos[0]][pos[1]]
		valid,i,j=valid_symbol(k,l,symbol)
		
		if valid:
			perim.append(pos)
			return symbol,i,j,pos			
	return False,None,None,None
	
def valid_symbol(k,l,s):
	k=-k
	l=-l
	
	if s=='S':
		return True,start[0],start[1]

	if s!='.' and [k,l] in map(lambda x:x[:2],links[s]) :
		edge=list(map(lambda x: x[:2],links[s]))
		edge.remove([k,l])

		return True,edge[0][0],edge[0][1]	

	return False,None,None

for i,l in enumerate(scetch):
	if 'S' in l:
		start=(i,l.index('S'))
		break
#Part1
for i,j in [(-1,0),(0,-1),(0,1),(1,0)]:
	symbol = 'S'
	begin=True
	pos=start
	s=0
	steps=0
	perim=[start]
	while symbol!='S' or begin==True:
		begin=False
		symbol,i,j,pos= get_next(i,j,pos,symbol)
				
		if symbol==False:
			break
		steps+=1

	else:
		if symbol=='S':
			break
print(steps//2)

#Part2
nests=0
d=[i for i in product(list(range(len(scetch))),list(range(len(scetch[0]))))]

for point in set(d)-set(perim):
	count=0
	for i in range(0,point[0]):

		for e,p in enumerate(perim):
			
			if p==(i,point[1])and perim[e][1]!=perim[(e-1)%len(perim)][1]:
				dif1=0
				delta=e
				while dif1==0:

					try:			
						dif1=perim[delta][1]-perim[1+delta][1]
													
					except IndexError:
						dif1=perim[delta][1]-perim[0][1]
						delta=0
					delta+=1

				else :					
					dif2=0
					delta=e
					while dif2==0:	

						try:
							dif2=perim[delta][1]-perim[delta-1][1]
							
						except IndexError:
							dif2=perim[delta][1]-perim[0][1]
							delta=0						
						delta-=1
				
				if dif1*dif2<0:	
					count+=1
	if count%2==1:

		nests+=1
print(nests)
		
					

	

		