from time import time
s=time()
with open('2023\Day5\input.txt') as f:
    seeds=list(map(int,f.readline().strip('\n').split()[1:]))
    maps=list(map(lambda x:x[x.index(':')+1:].strip('\n ').split('\n'),f.read().split('\n\n')))

seeds=[[seeds[i],seeds[i]+seeds[i+1]] for i in range(0,len(seeds),2)]

def get_map(m):
    l=list(map(lambda x:[int(i) for i in x.split()],m))
    r=[]
    for i in l:
        r.append([[i[0],i[0]+i[2]],[i[1],i[1]+i[2]]])
    return r

def source_to_dest(d,m):
    m=get_map(m) 
    new=[]
    for i,s in enumerate(d):
        for j in range(len(m)):
            if s[1]<=m[j][1][0] or s[0]>=m[j][1][1]:
                if j==len(m)-1:
                    new+=[[s[0],s[1]]]
                    break
                else:
                    continue
            else:
                if s[0]>=m[j][1][0] and s[1]<=m[j][1][1]:        
                    new+=[[m[j][0][0]-m[j][1][0]+s[0],m[j][0][1]-m[j][1][1]+s[1]]]
                    break

                elif s[0]<m[j][1][0] and s[1]<=m[j][1][1]:
                    new+=[[m[j][0][0],m[j][0][1]-m[j][1][1]+s[1]]]
                    d.append([s[0],m[j][1][0]])
                    break

                elif s[0]>=m[j][1][0] and s[1]>m[j][1][1]:
                    new+=[[m[j][0][0]-m[j][1][0]+s[0],m[j][0][1]]]
                    d.append([m[j][1][1],s[1]])                                           
                    break

                elif s[0]<m[j][1][0] and s[1]>m[j][1][1]:
                    new+=[[m[j][0][0]-m[j][1][0]+s[0],m[j][0][1]-m[j][1][1]+s[1]]]
                    d.append([m[j][1][0],m[j][1][1]])
                    break

                elif j==len(m)-1:
                    new+=[[s[0],s[1]]]
                    break  
                             
    return new

def result(data):   
    for map_ in maps:
        data=source_to_dest(data,map_)
    print(min(list(filter(lambda y:y>0, map(lambda x:x[0],data)))))

result(seeds)




print((time()-s)*1000)
