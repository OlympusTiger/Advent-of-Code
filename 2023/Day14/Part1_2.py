from itertools import cycle

with open('input.txt') as f:
	lines=f.read().splitlines()
lines=list(map(list,lines))
lines=list(map(list,list(zip(*reversed(lines[::-1])))[::-1]))

Part2 = True

def find_load(table,Part2,breakpoint):
	loads=[]
	cycles=0

	for c in cycle(range(4)):
		l=len(loads)       
		for i in range(len(loads)):

			if (l-i)%2==0 and loads[i:i+(l-i)//2]==loads[i+(l-i)//2:] and l-i>2:
				print(loads,l,i)
				breakpoint=(1000000000-i)%((l-i)/2)
				return breakpoint+i

		for i,t in enumerate(table):
			start=0
			for j,item in enumerate(t):	

				if item=='#':
					rocks=t[start:j].count('O')
					table[i][start:j]=['O']*rocks+(j-start-rocks)*['.']
					start=j+1

				elif j==len(t)-1:
					rocks=t[start:j+1].count('O')
					table[i][start:j+1]=['O']*rocks+(j+1-start-rocks)*['.']

		if c==0 and not Part2:
			load=sum([sum([-i for i,item in enumerate(line,-len(line)) if item=='O']) for line in table])
			return load

		if c==3:	
			load=sum([j.count('O')*i for i,j in enumerate(table,1)])
			loads.append(load)
			cycles+=1

			if cycles==breakpoint:
				return load

		table=list(map(list,list(zip(*reversed(table)))))

br=find_load(lines,Part2,breakpoint==-1)

print(find_load(lines,Part2,br))







