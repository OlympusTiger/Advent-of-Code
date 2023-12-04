with open('2023\Day1\input.txt') as f:
    l=f.read().split()
    nums=[[i for i in c if i.isdigit()]for c in l]
    print(sum(map(lambda x:int(x[0]+x[-1]) if len(x)>1 else int(2*x[0]),nums)))