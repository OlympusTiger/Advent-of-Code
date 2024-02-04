from time import time
st=time()
from math import lcm

with open('2023\Day20\input.txt') as f:
    config=[l.split(' -> ') for l in f.read().splitlines()]

class Module:
    def __init__(self,line):
        if line[0]=='broadcaster':
            self.name=line[0]
            self.type='B'
            
        else:
            self.name=line[0][1:]
            self.type=line[0][0]
        
        self.state=False      
        self.dest=line[1].split(', ')
        
        if self.type=='&':
            self.mem={}

modules={m.name:m for m in map(Module,config)}

def sequence(que):
    
    global mods

    while que:       
        s,m,p=que[0]
        
        if m not in modules.keys():            
            que.pop(0)
            continue

        elif modules[m].type=='%' and p=='L':
           que+=[(m,d,'H') if modules[m].state==False else (m,d,'L') for d in modules[m].dest]
           modules[m].state=not modules[m].state            

        elif modules[m].type=='&':
            modules[m].mem[s]=p
           
            if all(i=='H' for i in modules[m].mem.values()):
                modules[m].state=True
                if m in mods:
                    mods[m]+=[loop]
                
            else:
                modules[m].state=False
                
            que+=[(m,d,'L') if all(b=='H' for b in modules[m].mem.values()) else (m,d,'H') for d in modules[m].dest]

        que.pop(0)
           
    return mods

modules={m.name:m for m in map(Module,config)}

for n in modules.keys():
    if modules[n].type=='&':
        for a,b in modules.items():
            if n in b.dest:
                modules[n].mem[a]='L'

mods={}
for m in modules:
    if modules[m].dest==['rx']:
        for a,b in modules.items():
            if m in b.dest:
                for k,l in modules.items():
                    if a in l.dest:
                        mods[k]=[]

loop=1

while [] in mods.values():
    queue=[('B',d,'L') for d in modules['broadcaster'].dest]
    mods=sequence(queue)

    loop+=1

print(lcm(*list(map(lambda i:i[0],mods.values()))))


  










