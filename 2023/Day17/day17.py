import heapq
from time import time
start_time = time()
with open('2023\Day17\input.txt')as f:
	inp=f.read()

Part2=True

def parse_map(inp):
	grid=[list(l) for l in inp.splitlines()]
	start=(0,0)
	b=len(grid)-1
	end=(b,b)
	return grid,start,end

def valid(grid,pos):
	x,y=pos

	if 0 <= x < len(grid) and 0 <= y < len(grid[0]):
		return True  
	return False

def get_neighbors(grid,pos,heading):
    lst=[(0,1),(0,-1),(1,0),(-1,0)]
    back=(-heading[0],-heading[1])
    x,y=pos
    
    for i in lst:     
        if i!=back:
            nxt=(x+i[0],y+i[1])

            if valid(grid,nxt):
             
 	           yield nxt,i


def find_path(map):
    
	global grid
	grid, origin, destination = parse_map(map)

	queue = []         #loss steps  pos   heading
	heapq.heappush(queue, (0, 0, origin, (0,1)))
	heapq.heappush(queue, (0, 0, origin, (1,0)))
	explored = set()

	while queue:
		
		loss, c, current,heading = heapq.heappop(queue)
	
		if (current,heading,c) in explored:
			continue
			
		explored.add((current,heading,c))
			
		if current==destination:
			return loss
				
		neighbors = set(get_neighbors(grid, current, heading))

		for neighbor, h in neighbors:
			con1=3
			con2=0
			if Part2:
				con1=10
				con2=4
			
			if c<con1 and h==heading:
				nloss=loss+int(grid[neighbor[0]][neighbor[1]])		
				heapq.heappush(queue, (nloss, c+1,neighbor, h))
			     
			elif c>=con2 and h!=heading:  
				nloss=loss+int(grid[neighbor[0]][neighbor[1]])		
				heapq.heappush(queue, (nloss, 1,neighbor, h))   
		
		
     

print(find_path(inp))
print(time()-start_time)
