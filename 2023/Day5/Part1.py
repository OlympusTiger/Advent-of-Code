with open('2023\Day5\input.txt') as f:
    seeds=list(map(int,f.readline().strip('\n').split()[1:]))
    maps=list(map(lambda x:x[x.index(':')+1:].strip('\n ').split('\n'),f.read().split('\n\n')))

def get_map(m):
    return list(map(lambda x:[int(i) for i in x.split()],m))

def source_to_dest(l,nums):
    mp=get_map(l)
    for i,s in enumerate(nums):
        for r in mp:
            if s in range(r[1],r[1]+r[2]):
                nums[i]=s-r[1]+r[0]

    return nums

def result(data):
    for map_ in maps:
        data=source_to_dest(map_,data)
    print(min(data))

result(seeds.copy())


