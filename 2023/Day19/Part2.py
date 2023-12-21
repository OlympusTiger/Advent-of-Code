import re 
from functools import reduce
from time import time
t1=time()
with open('2023\Day19\input.txt') as f:
    instr=f.read().split('\n\n')[0].splitlines()

wflow={ins[:-1].split('{')[0]:ins[:-1].split('{')[1] for ins in instr}   

def range_intersect(r1, r2):
    return range(max(r1.start,r2.start), min(r1.stop,r2.stop))


def find_range_pos(x):
    cat=x[0]
    num=int(re.search('\d+',x).group())

    if '>' in x:      
        r=range(num+1,4001)
        
    else:
        r=range(1,num)

    accepted[count][cat]=range_intersect(accepted[count][cat], r)


def find_range_neg(x):
    cat=x[0]
    num=int(re.search('\d+',x).group())

    if '<' in x:         
        r=range(num,4001)
        
    else:            
        r=range(1,num+1)

    accepted[count][cat]=range_intersect(accepted[count][cat], r)


def track_parent(child):

    for p in wflow.keys():
        if child in re.findall('[AR]|[a-z]{2,3}',wflow[p]):           
            ind=re.findall('[AR]|[a-z]{2,3}',wflow[p]).index(child)   

            for i,cond in enumerate(wflow[p].split(',')):
                if child==cond:
                    return None if p=='in' else track_parent(p)

                elif i==ind:
                    find_range_pos(cond)
                    return None if p=='in' else track_parent(p)
             
                else:
                    find_range_neg(cond)


def find_As(child,v,ind,end):

    for k,cond in enumerate(v.split(',')):
        if cond=='A':
            track_parent(child)
            return

        elif k==ind:
            find_range_pos(cond)
            track_parent(child)
            return 

        else:
            find_range_neg(cond)

          
count=0
accepted=[]
for i,value in enumerate(wflow.values()):
    start=list(wflow.keys())[i]

    for j,part in enumerate(value.split(',')):
        if 'A' in part:

            accepted.append(dict.fromkeys(['x','m','a','s'], range(1,4001)))            
            find_As(start,value,j,':A'in part)

            count+=1
   
    
total=0
for d in accepted:
    total+=reduce(lambda x,y:x*y,map(len,d.values()))

print(total)
    

print(time()-t1)














# def work(ins,x):
#     for i in wflow[ins].split(','):
           
#         if i in 'AR':
#             return i

#         if i[1]=='<':

#             if x[i[0]]<int(re.search('\d+',i).group()):                         
#                 return i.split(':')[1]
#             else:
#                 continue

#         elif i[1]=='>':

#             if x[i[0]]>int(re.search('\d+',i).group()):
#                 return i.split(':')[1]
#             else:
#                 continue

#         return i

# def acc_rej(part):
#     g='in'
 
#     while work(g,part) not in 'AR':
#         g=work(g,part)

#     else:
#         if work(g,part)=='A':
#             return part
#         else:
#             return None

# accepted=[]
# for item in parts:
#     if acc_rej(item):
#         accepted.append(item)

# nums=0
# for i in accepted:
#     nums+=sum(i.values())

# print(nums)

