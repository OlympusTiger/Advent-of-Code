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

b=12
def parse_map(inp):
    grid=[list(l) for l in inp.splitlines()]

    start=0,0
    end=b,b
    return grid,start,end

def valid(grid,pos,pred):
    x,y=pos
    
    
    if 0 <= x < len(grid) and 0 <= y < len(grid[0]):
        
        print(pred)
        pred+=[pos]
       
        if len(pred) >=4:
            x_directions = [i[0] for i in pred[-4:]]
           
            y_directions = [i[1] for i in pred[-4:]]
            

            if len(set(x_directions)) == 1 or \
               len(set(y_directions)) == 1:

               
               return False
            print(x_directions)
            print(y_directions)
        return True
    
    return False

def get_neighbors(grid,pos,prev):
    
    
    rec=[pos]
    p=pos
    while p!=(0,0):
        rec.insert(0,prev[p])
        p=prev[p]
   
    lst=[(0,1),(0,-1),(1,0),(-1,0)]
    x,y=pos
    
    for i in lst:
        
        pos=(x+i[0],y+i[1])
    
        if valid(grid,pos,rec):
    
            yield pos


def get_shorter_paths(weights, positions, through):
    path = weights[through]
  
    for position in positions:
        if position in weights and weights[position] <= weights[through]:
            continue
        
        yield position, path


def find_path(map):
    lines, origin, destination = parse_map(map)
    
    weights = dict.fromkeys([(i,j) for i,j in product(range(len(lines)),repeat=2)],inf)
    weights[origin]=0
    
    
    queue = []
    heapq.heappush(queue, (0, origin))
    prev=dict.fromkeys([(i,j) for i,j in product(range(len(lines)),repeat=2)],None)
    certain = set()
    while destination not in certain:
        
        _ig,current = heapq.heappop(queue)
       
      
        if current in certain:
            continue
        certain.add(current)
        neighbors = set(get_neighbors(lines, current,prev)) - certain
      
        
        shorter = get_shorter_paths(weights, neighbors, current)
        
        for neighbor, path in shorter:
            weights[neighbor] = path+int(lines[neighbor[0]][neighbor[1]])
            prev[neighbor]=current
            heapq.heappush(queue, (weights[neighbor], neighbor))
    if destination in weights:
        
        return weights[destination],prev
    else:
        raise ValueError("no path")        

d,pred=find_path(inp)

print(d)
