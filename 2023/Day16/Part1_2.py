from time import time
s=time()
with open('input.txt') as f:
    grid=[list(i) for i in f.read().splitlines()]

Part2=True

entrances = [((i,0),(0,1)) for i in range(len(grid))]+[((i,len(grid)-1),(0,-1)) for i in range(len(grid))]+[((len(grid)-1,i),(-1,0)) for i in range(len(grid[0]))]+[((0,i),(1,0)) for i in range(len(grid[0]))]


def track_beam(tile,heading,energized=[],path_used=[]):
    dir_map={'\\':{(0,1):(1,0),(0,-1):(-1,0)}
            ,'/':{(0,1):(-1,0),(0,-1):(1,0)}
            ,'|':{(0,1):((1,0),(-1,0)),(0,-1):((1,0),(-1,0))}
            ,'-':{(1,0):((0,1),(0,-1)),(-1,0):((0,1),(0,-1))}}
  
    while (tile,heading) not in path_used:

        i,j=tile

        if not (0<=i<len(grid) and 0<=j<len(grid[0])):
            prev=tuple(map(lambda x:-x,heading))
            exit_=tuple(map(sum,zip(tile,prev)))

            if (exit_,prev) in entrances:
                entrances.remove((exit_,prev))
            return energized

        energized.append(tile)
        symbol=grid[i][j]

        if symbol=='.':          
            tile=tuple(map(sum,zip(tile,heading)))

        elif symbol in '-|' and heading not in list(dir_map[symbol].keys()):
            path_used.append((tile,heading))
            tile=tuple(map(sum,zip(tile,heading)))

        else:
            if symbol in '-|':     
                path_used+=[(tile,heading),(tile,tuple(map(lambda x:-x,heading)))]
                
                head0=dir_map[symbol][heading][0]
                new0=tuple(map(sum,zip(tile,head0)))
                energized=track_beam(new0,head0,energized,path_used)

                head1=dir_map[symbol][heading][1]
                new1=tuple(map(sum,zip(tile,head1)))
                energized=track_beam(new1,head1,energized,path_used)

            else:
                path_used.append((tile,heading))

                try:    
                    head=dir_map[symbol][heading]
                    new=tuple(map(sum,zip(tile,head)))
                    
                    energized=track_beam(new,head,energized,path_used)

                except KeyError:    
                    head=list(dir_map[symbol].keys())[list(dir_map[symbol].values()).index(heading)]
                    new=tuple(map(sum,zip(tile,head)))

                    energized=track_beam(new,head,energized,path_used)
    
    return energized

def main():
    if not Part2:
        return len(set(track_beam((0,0),(0,1))))

    combs=[]
    for en in entrances[::-1]:
        t,h=en
        combs.append(len(set(track_beam(t,h,[],[]))))

    return max(combs)

print(main())
print(time()-s)
