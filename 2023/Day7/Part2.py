with open('2023\Day7\input.txt') as f:
    lines=f.read().splitlines()


hands=[[l.split()[0],l.split()[1]] for l in lines]


def get_counts(hand):
    counts=[]
    for i in set(hand):
        if hand.count(i)>1 and i!='J':
            counts.append(hand.count(i))
    sorted(counts,reverse=True)
    if 'J' in hand:
        c=hand.count('J')
        if counts:
            counts[0]+=c
        else:
            if c==5:
                counts.append(5)
            else:
                counts.append(c+1)

    return (set(counts),len(counts))

def custom_order1(y):
    combs=[(set(),0),({2},1),({2},2),({3},1),({2,3},2),({4},1),({5},1)]
    return combs.index(get_counts(y))

def custom_order2(z):
    s=['J','2','3','4','5','6','7','8','9','T','Q','K','A']
    return [s.index(i) for i in z]

def main():
    sorted_hands=sorted(hands,key=lambda x:(custom_order1(x[0]),custom_order2(x[0])))
    res=0
    multi=1
    for h in sorted_hands:
        res+=int(h[1])*multi
        multi+=1
    return res

print(main())




