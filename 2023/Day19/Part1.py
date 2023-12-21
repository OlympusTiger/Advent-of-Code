import re 
from time import sleep
with open('2023\Day19\input.txt') as f:
    instr=f.read().split('\n\n')[0].splitlines()
    f.seek(0)
    items=f.read().split('\n\n')[1].splitlines()

part=[item.strip('\{\}').split(',') for item in items]

parts=[]
for item in part:
    parts.append({i.split('=')[0]:int(i.split('=')[1]) for i in item})

wflow={ins[:-1].split('{')[0]:ins[:-1].split('{')[1] for ins in instr}   

def work(ins,x):
    for i in wflow[ins].split(','):
  
        if i in 'AR':
            return i

        if i[1]=='<':

            if x[i[0]]<int(re.search('\d+',i).group()):                         
                return i.split(':')[1]
            else:
                continue

        elif i[1]=='>':

            if x[i[0]]>int(re.search('\d+',i).group()):
                return i.split(':')[1]
            else:
                continue

        return i

def acc_rej(part):
    g='in'
 
    while work(g,part) not in 'AR':
        g=work(g,part)

    else:
        if work(g,part)=='A':
            return part
        else:
            return None

accepted=[]
for item in parts:
    if acc_rej(item):
        accepted.append(item)

nums=0
for i in accepted:
    nums+=sum(i.values())

print(nums)
