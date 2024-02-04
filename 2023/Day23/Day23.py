from collections import defaultdict

with open('2023\Day23\input.txt') as f:
	grid=[list(l) for l in f.read().splitlines()]
shape=len(grid)

for i in range(shape):
	if grid[0][i]=='.':
		start=(0,i)
	if grid[shape-1][i]=='.':
		end=(shape-1,i)

Part2=False
		
lst={(0,1):'>',(0,-1):'<',(1,0):'v',(-1,0):'^'}

#CONDENCE GRID    VVVVVVVV

def back(h):            #avoid going backwards
	return (-h[0],-h[1])

def next_pos(pos,heading):
	
	for h in lst:
		if h!=back(heading):
			p=(pos[0]+h[0],pos[1]+h[1])
			
			try:	
				if grid[p[0]][p[1]]!='#':
					yield p,h
			except IndexError:
				continue
		
	
def find_edge(p,heading):
	
	x,y=p
	pos=(x+heading[0],y+heading[1])
	steps=0
	nxt=[(p, heading)]
	
	while len(nxt)==1 or nxt[0][0]==end:
		steps+=1
		pos, heading=nxt[0]
		
		if pos==end:
			return pos,nxt,steps
		
		nxt=list(next_pos(pos,heading))
            
	else:
		return pos,nxt,steps 
		
def queue():
	edges={}
	Q=[(start,start,(1,0))]
	explored=set()

	while Q:
		st,pos,h=Q.pop(0)
		
		if pos in explored or pos==end:		
			continue
		
		explored.add(pos)
		new_pos,nxt,steps=find_edge(pos,h)
		edges[(st,new_pos)]=steps
		
		if new_pos in explored:
				continue

		for new_p,new_h in nxt:
			if not Part2 and grid[new_p[0]][new_p[1]]!=lst[new_h]: #condition for Part1 - avoid uphill
				continue
                  
			explored.add(new_pos)
			Q.append((new_pos,new_p,new_h))
	
	return edges

edges=queue()

nodes=set([i[0] for i in edges.keys()]+[i[1] for i in edges.keys()])
adj_list=defaultdict(dict)
for n,d in edges.items():
    adj_list[n[0]][n[1]]=d
    if Part2:	                # for Part2 add both directions to adjacent list
        adj_list[n[1]][n[0]]=d


#CONDENCE GRID    ^^^^^^^^^
        

if Part2:                       #Part2:find the top and bottom outer edges for optimization-
                                #going up or left for the bottom or top outer edge respectively means you're trapped in a closed shape and can't reach end.
    edge_nodes=[]               #nodes that are on the outer edge of the grid
    for i in adj_list:
        if len(adj_list[i])==3:
            edge_nodes.append(i)
    cycle=[[],[]]

    corner=list(adj_list[start].keys())[0]
    corner2=list(adj_list[end])[0]

    for i,n in enumerate(adj_list[corner],-1):

        if n==start:
            continue
        
        cycle[i].append(corner)
        begin=True
        
        while n!=corner2 or begin==True:
            begin=False
            cycle[i].append(n)
            
            for x in adj_list[n]:
                if x in edge_nodes and x not in cycle[i] and x!=end:
                    n=x
                    continue
        else:
            cycle[i].append(n)			
		

steps=[]
def nxt(p,ad):
    return (p[0]+ad[0],p[1]+ad[1],p[2]+1)

def path(pos,vis=[]):
    vis=vis.copy()
    possible=[]
    while True:
        i,j,s=pos
		
        if (i,j)==end:
            steps.append(s)
            return
        
        vis+=[(i,j),(j,i)] 
        for adj in adj_list[(i,j)]:
            if Part2:               #Apply outer egdes
                for c in cycle:
                    if (i,j) in c and adj in c:
                        if c.index(adj)<c.index((i,j)):
                            continue

            if adj not in vis:
                possible.append((*adj,s+adj_list[(i,j)][adj]))
				
        if not possible:
            return

        while len(possible)>1:
            path(possible.pop(0),vis)
			
        else:
            pos=possible.pop(0)
			
path(start+(0,))
print(max(steps)-1)
