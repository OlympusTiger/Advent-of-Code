from Part1 import cards
d=dict.fromkeys(range(len(cards)), 1)
matches=[len(set(i[0])&set(i[1])) for i in cards]

for i,m in enumerate(matches):
    for j in range(m):
        if i+j+1<len(d):
            d[i+j+1]+=d[i]
print(sum(d.values()))

    
