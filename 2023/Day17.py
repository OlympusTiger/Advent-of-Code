import heapq
from time import sleep
from math import inf
from itertools import product
inp='''\
2413432311323
3215453535623
3255245654254
3446585845452
4546657867536
1438598798454
4457876987766
3637877979653
4654967986887
4564679986453
1224686865563
2546548887735
4322674655533
'''

b=12 # grid size
def parse_map(inp):
    grid=[list(l) for l in inp.splitlines()]

    start=0,0
    end=b,b
    return grid,start,end

def valid(grid,pos):
    x,y=pos

    if 0 <= x < len(grid) and 0 <= y < len(grid[0]):
        return True  
    return False


def get_neighbors(grid,pos):
    
    lst=[(0,1),(0,-1),(1,0),(-1,0)]
    x,y=pos
    
    for i in lst:        
        pos=(x+i[0],y+i[1])
    
        if valid(grid,pos):
            yield pos,i


def get_shorter_paths(weights, c, positions, through):
    path = weights[through]

    for position,h in positions:
        if weights[position] <= path+int(lines[position[0]][position[1]]):         
            continue
        
        yield position, c, path, h


def find_path(map):
    global lines
    lines, origin, destination = parse_map(map)
    
    weights = dict.fromkeys([(i,j) for i,j in product(range(len(lines)),repeat=2)],inf)
    weights[origin]=0
    
    queue = []        #  loss c   pos   heading
    heapq.heappush(queue, (0, 0, origin, None))
    
    prev=dict.fromkeys([(i,j) for i,j in product(range(len(lines)),repeat=2)],None)
    explored = set()
    while destination not in explored:
   
        _loss, c,current,heading = heapq.heappop(queue)
            
        if current in explored:
            continue

        explored.add(current)

        neighbors = set(get_neighbors(lines, current)) - explored    
        shorter = get_shorter_paths(weights, c, neighbors, current)
        
        for neighbor, c, path, h in shorter:
            weights[neighbor] = path+int(lines[neighbor[0]][neighbor[1]])
            prev[neighbor]=current

            if c==3 and h==heading:
                continue
            elif h!=heading:
                heapq.heappush(queue, (weights[neighbor], 1, neighbor, h))
            else:
                heapq.heappush(queue, (weights[neighbor], c+1, neighbor, h))
           
            
    if destination in weights:     
        return weights[destination],prev

    else:
        raise ValueError("no path")        

d,pred=find_path(inp)
print(d)


p=(b,b)
prev=[p]
while p!=(0,0):
    prev.append(pred[p])
    p=pred[p]
    
print(prev[::-1])

