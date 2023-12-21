from time import sleep
with open('2023\Day16\input.txt') as f:
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
            # prev=(-heading[0],-heading[1])
            # exit_=(tile[0]+heading[0],tile[1]+heading[1])
            # if (exit_,prev) in entrances:
            #     entrances.remove((exit_,prev))
            return energized

        energized.append(tile)
        symbol=grid[i][j]

        if symbol=='.':          
            tile=(tile[0]+heading[0],tile[1]+heading[1])

        elif symbol in '-|' and heading not in list(dir_map[symbol].keys()):
            path_used.append((tile,heading))
            tile=(tile[0]+heading[0],tile[1]+heading[1])

        else:
            if symbol in '-|':     
                path_used+=[(tile,heading),(tile,(-heading[0],-heading[1]))]
                
                head0=dir_map[symbol][heading][0]
                new0=(tile[0]+head0[0],tile[1]+head0[1])
                energized=track_beam(new0,head0,energized,path_used)

                head1=dir_map[symbol][heading][1]
                new1=(tile[0]+head1[0],tile[1]+head1[1])
                energized=track_beam(new1,head1,energized,path_used)

            else:
                path_used.append((tile,heading))

                try:    
                    head=dir_map[symbol][heading]
                    new=(tile[0]+head[0],tile[1]+head[1])
                    
                    energized=track_beam(new,head,energized,path_used)

                except KeyError:    
                    head=list(dir_map[symbol].keys())[list(dir_map[symbol].values()).index(heading)]
                    new=(tile[0]+head[0],tile[1]+head[1])

                    energized=track_beam(new,head,energized,path_used)
    
    return energized

def main():
    if not Part2:
        return len(set(track_beam((0,0),(0,1))))

    combs=[]
    for en in entrances:
        print(en)
        t,h=en
        combs.append(len(set(track_beam(t,h,[],[]))))

    return max(combs)

print(main())

