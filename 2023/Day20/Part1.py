from time import sleep
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
    
    global Lows,Highs

    while que:     
        s,m,p=que[0]
        
        if p=='L':
            Lows+=1
        else:
            Highs+=1
        
        if m not in modules.keys():
            que.pop(0)
            continue

        elif modules[m].type=='%' and p=='L':
           que+=[(m,d,'H') if modules[m].state==False else (m,d,'L') for d in modules[m].dest]
           modules[m].state=not modules[m].state         

        elif modules[m].type=='&':
            modules[m].mem[s]=p
            que+=[(m,d,'L') if all(b=='H' for b in modules[m].mem.values()) else (m,d,'H') for d in modules[m].dest]

        que.pop(0)
  
    return {m.name:m.state for m in modules.values()}

modules={m.name:m for m in map(Module,config)}


for n in modules.keys():
    if modules[n].type=='&':
        for a,b in modules.items():
            if n in b.dest:
                modules[n].mem[a]='L' 
Highs=0
Lows=0    

initial={m.name:m.state for m in modules.values()}
states=initial.copy()

start=True 
loop=0

while (loop<1000 and states!=initial) or start:
    start=False
    queue=[('B',d,'L') for d in modules['broadcaster'].dest]
    Lows+=1
    states=sequence(queue)
    loop+=1

print(Lows*Highs)
    










